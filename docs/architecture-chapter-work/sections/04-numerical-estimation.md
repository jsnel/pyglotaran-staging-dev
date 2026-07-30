# 4. Exploiting conditional linearity during estimation

## 4.1 From two contributions to a matrix model

Once explicit parameters have fixed the temporal shapes in the running example, estimating
their wavelength-dependent amplitudes becomes a linear-combination problem. Suppose two
contributions have temporal profiles \(c_1\) and \(c_2\), while \(s_1\) and \(s_2\) describe
their associated spectral amplitudes. At sampled delay \(t_i\) and wavelength
\(\lambda_j\), the modeling assumption is

\[
y(t_i,\lambda_j)\approx
c_1(t_i;\boldsymbol{\theta})s_1(\lambda_j)
+c_2(t_i;\boldsymbol{\theta})s_2(\lambda_j)
+\varepsilon_{ij}.
\]

Here \(i=1,\ldots,n_t\) indexes sampled delays, \(j=1,\ldots,n_\lambda\) indexes
wavelengths, and \(y(t_i,\lambda_j)\) is one measured signal. The vector
\(\boldsymbol{\theta}\) contains the free explicit outer parameters that determine the
profiles, while \(\varepsilon_{ij}\) collects measurement noise and model mismatch not
explained by the two contributions. The equation does not assert that two components are
uniquely identifiable. It says that, under the proposed model, each measured value is
approximated by adding shape-times-amplitude products (NM-01).

Stacking all measured values gives a matrix rather than a collection of unrelated scalar
equations. To cover one dataset or another numerical objective unit, label that unit \(q\).
The canonical separable model is

\[
\mathbf{Y}_q =
\mathbf{M}_q(\boldsymbol{\theta})\mathbf{B}_q
+\boldsymbol{\varepsilon}_q.
\]

The oriented observation
\(\mathbf{Y}_q\in\mathbb{R}^{n_{m,q}\times n_{g,q}}\) has \(n_{m,q}\) samples along
the model dimension and \(n_{g,q}\) samples along the global dimension.
\(\mathbf{M}_q(\boldsymbol{\theta})\in\mathbb{R}^{n_{m,q}\times k_q}\) contains
\(k_q\) effective shape columns calculated at the current explicit parameters.
\(\mathbf{B}_q\in\mathbb{R}^{k_q\times n_{g,q}}\) contains the conditionally linear
parameters (CLPs), and
\(\boldsymbol{\varepsilon}_q\) has the same shape as the observation. For the running
example, \(n_m=n_t\), \(n_g=n_\lambda\), rows of \(\mathbf{M}\) follow delay time,
and every row of \(\mathbf{B}\) is the spectrum associated with one effective temporal
column.

The current implementation preserves the link between these mathematical columns and their
scientific names. `OptimizationMatrix` carries an array, an ordered `clp_axis`, and
applicable coefficient constraints. Each Element returns labels with its matrix contribution.
An element-specific scale can multiply that contribution before compatible matrices are
combined (NM-02).

Composition is label-aware rather than simple side-by-side concatenation. The combined
matrix uses the union of CLP labels. Contributions with the same label are added into the
same effective column, while new labels create new columns. Index-dependent contributions
can also vary along the global coordinate before one matrix is selected for an inner solve.
Thus \(k_q\) counts effective columns after supported composition and transformation; it is
not necessarily the sum of columns returned independently by every Element (NM-03).

The unexplained term is as important as the product. A small residual can support a proposed
model, but it cannot by itself prove that the chosen profiles correspond to unique physical
states. Separability is a useful structural assumption because it exposes two computational
tasks with different algebra, not because the measured surface establishes a correct
mechanism (van Stokkum et al., 2004).

## 4.2 Inner coefficient estimation

For one trial value of \(\boldsymbol{\theta}\), the temporal or other model-dimension
columns are known. The inner question is then: which coefficient values make those columns
reproduce the observations as closely as possible? The phrase **arg min** means “the
argument—the set of coefficient values—that gives the smallest mismatch.” With weighting
and only the constraints supported by the chosen path, the inner problem is written

\[
\widehat{\mathbf{B}}_q(\boldsymbol{\theta})
=
\underset{\mathbf{B}_q\in\mathcal{C}_q}{\arg\min}\;
\left\|
\mathcal{W}_q\!\left(
\mathbf{Y}_q-\mathbf{M}_q(\boldsymbol{\theta})\mathbf{B}_q
\right)
\right\|_F^2.
\]

The hat marks an estimate. The set \(\mathcal{C}_q\) contains only coefficient restrictions
actually supported by the selected estimator and matrix-reduction path. The operation
\(\mathcal{W}_q\) applies the relevant weights to the difference between observed and
calculated values. The symbol \(\|\cdot\|_F\) is the **Frobenius norm**: square every entry
of a matrix, add the squares, and take the square root. Squaring that norm, as shown, gives
the sum of squared weighted discrepancies. Physically, the inner solve chooses the spectra
or other amplitudes that best combine the trial shapes at all represented coordinates
(NM-01, NM-08).

The general weighting symbol is deliberate. In the ordinary path, pyglotaran multiplies
observations by entry-wise weights when numerical data are initialized and applies matching
weights to matrix contributions when they are calculated. In a specialized global-element
path, weights and data are transposed and flattened. For linked datasets, participating
model-axis vectors and matrix blocks are joined at each aligned global coordinate, with
configured dataset scales applied to their respective matrix blocks. A single
\(\mathcal{W}_q\) captures the shared mathematical intention without claiming that all
cases are implemented as one left-multiplication matrix (NM-08, NM-11).

Before the inner solver is called, supported CLP relations and zero/only constraints reduce
the labeled matrix at the global coordinate where they apply. A relation such as “target is
a factor times source” merges the target column into the source column and removes the
dependent target from the reduced problem. A zero or only constraint removes an affected
column where its interval rule applies. After estimation, the runtime expands the CLP vector
back to the full label set, placing zeros or reconstructed related values in their
appropriate positions (NM-09, NM-10). In the equation, these transformations are part of the
qualified constraint set \(\mathcal{C}_q\); the notation must not be read as support for
arbitrary constraints.

The default inner strategy in the inspected declarations is **variable projection**. The
ordinary idea is to solve the linear coefficients afresh for every trial of the outer
parameters, so that those coefficients need not be included in the outer search vector.
Projecting out the conditionally linear part leaves a smaller outer variable vector and uses
the least-squares solution of the current linear subproblem under its numerical assumptions.
The staging routine uses a QR factorization to calculate the CLPs and residual for that matrix (NM-06). This is
consistent with the variable-projection treatment of separable least squares in the
scientific literature (van Stokkum et al., 2004; Mullen & van Stokkum, 2007), but it should
not be described as a port of TIMP's partitioned algorithm.

The supported alternative is **non-negative least squares (NNLS)**. It asks the same inner
least-squares question while restricting fitted CLPs to nonnegative values. The current
routine delegates that solve to SciPy's `nnls` and then calculates the data-minus-fit
residual (NM-07). This restriction can be scientifically appropriate when negative
amplitudes would contradict the quantity represented, but it is an assumption to be justified,
not an automatic improvement. NNLS acts on CLPs and is distinct from the logarithmic
positivity transformation available for explicit outer parameters.

Estimator selection has two current declarative locations. During the repeated estimation
described here, ordinary and specialized global-penalty objective calculations use the
Experiment's residual-function selection. Specialized global-result reconstruction later
reads the DataModel-level field. This is a staging path distinction, not a new mathematical
category; the inner responsibility remains to return a CLP estimate and residual for the
matrix and data supplied to it (NM-05).

## 4.3 Outer least squares, penalties, and uncertainty

The residual left after the inner estimate tells the outer routine how well the current
shape-producing parameters work. The outer routine changes only the free explicit
parameters, respects their supported bounds or positivity coordinates, updates expression
consequences, and asks all objectives to repeat their matrix and CLP calculations. A
schematic objective that includes several units \(q\) and penalty residuals is

\[
\widehat{\boldsymbol{\theta}}
=
\underset{\boldsymbol{\theta}\in\Theta}{\arg\min}\;
\left\|
\operatorname{concat}_q
\mathbf{r}_q\!\left(
\boldsymbol{\theta},
\widehat{\mathbf{B}}_q(\boldsymbol{\theta})
\right)
\right\|_2^2
+
\left\|\mathbf{p}(\boldsymbol{\theta})\right\|_2^2.
\]

The estimate \(\widehat{\boldsymbol{\theta}}\) is the outer-parameter vector that gives the
smallest represented mismatch within the feasible domain \(\Theta\). That domain includes
applicable bounds and the consequences of fixed, expression-defined, and positivity-transformed
explicit parameters. For each \(q\), \(\mathbf{r}_q\) is the residual contribution after
the inner coefficient estimate. The operator \(\operatorname{concat}_q\) places those
vectors end to end. The vector \(\mathbf{p}\) contains supported soft-penalty residuals and
can depend indirectly on \(\boldsymbol{\theta}\) through the fitted CLPs. The Euclidean
norm \(\|\cdot\|_2\) squares vector entries, adds them, and takes the square root; its square
therefore gives a sum of squared entries.

The displayed sum explains the mathematical intention rather than naming a scalar object
constructed by pyglotaran. In the current path, each objective concatenates its data
residuals. An equal-area CLP penalty can add a weighted discrepancy between configured source
and target coefficient areas as another residual entry. The top-level callback then
concatenates the vectors from all Experiment objectives and gives that one residual vector
to SciPy's `least_squares` (NM-12, NM-13). Squaring and summing are consequences of the
outer least-squares routine's contract.

The timing of recalculation is also visible here. Numerical data wrappers, aligned
coordinates, and linked-group definitions are created when an `OptimizationObjective` is
initialized. During every callback, trial explicit values are written into the selected
`Parameters`; expression-defined values are updated; element matrices are recalculated and
combined; relations and constraints reduce them; and inner CLPs and residuals are estimated.
The architecture therefore does not prepare all matrices once. Only structures independent
of the changing trial parameters can be initialized ahead of the loop (NM-04, NM-14).

SciPy stops according to configured least-squares tolerances, evaluation limits, or failure
conditions. A termination message is evidence about the numerical run, not proof that
the physicochemical model is true or uniquely identifiable. Where the least-squares output
supports it, pyglotaran also calculates degrees of freedom, a covariance estimate, and
standard errors for free explicit parameters. These are local diagnostics based on the
implemented Jacobian and residual assumptions; they should be examined alongside residual
structure and scientific plausibility rather than treated as universal uncertainty
claims (NM-15).

<!-- Insert Mermaid source from ../figures/fig-04-nested-estimation.mmd here. -->

**Figure 4. Nested estimation from trial explicit parameters to an outer residual vector.**
Solid arrows carry numerical values or configured transformations. The dashed return arrow
means that the outer least-squares routine proposes another trial; it does not imply that
parameter-dependent matrices are retained between trials. Plain-language responsibilities
are primary, with current implementation anchors shown in parentheses.

Figure 4 emphasizes why the two kinds of unknowns remain separate. Trial outer values
determine labeled matrices. Those matrices and the oriented observations enter an inner
variable-projection or NNLS solve. Data residuals and supported penalty entries then form the
vector judged by the outer routine, whose next proposal closes the loop. Relations,
constraints, weights, and scales are transformations at particular edges, not a third
optimizer (NM-04 through NM-14).

**Table 3. Mathematics-to-code concordance for nested estimation**

| Equation symbol or operation | Scientific meaning | Current runtime representation | When it participates |
|---|---|---|---|
| \(q\) | One dataset or numerical objective unit in the explanatory equations | A dataset slice, linked coordinate block, or `OptimizationObjective` contribution, depending on the realized path | Used to organize and concatenate residual contributions |
| \(\boldsymbol{\theta}\), \(\Theta\) | Free explicit outer values and their feasible domain | Selected labels/values/bounds from `Parameters`; trial vector handled by `Optimization.objective_function` and SciPy `least_squares` | Updated once per outer callback |
| \(\mathbf{Y}_q\) | Oriented measured observations | `OptimizationData.data_slices`, `flat_data`, or linked data blocks | Data wrappers initialize these numerical views before repeated evaluation |
| \(\mathbf{M}_q(\boldsymbol{\theta})\) | Composed shape columns evaluated at current explicit values | `OptimizationMatrix.array`, built from Element contributions and accompanied by `clp_axis` | Recalculated and transformed during each objective evaluation |
| \(k_q\), matrix-column labels | Number and identities of effective coefficient columns | `OptimizationMatrix.clp_axis` after composition and reduction | Determines the inner coefficient-vector layout |
| \(\mathbf{B}_q\), \(\widehat{\mathbf{B}}_q\) | CLPs and their current inner estimates | `OptimizationEstimation.clp`, later expanded to full labels where needed | Solved inside each current matrix/data problem; not stored in `Parameters` |
| \(\mathcal{W}_q\) | Relative influence assigned to residual entries | Dataset/model weights applied to observed values and corresponding matrices, including flattened forms | Data side at wrapper initialization; matrix side during calculation |
| \(\mathcal{C}_q\) | Supported restrictions on the inner coefficients | Matrix reduction for CLP relations and zero/only constraints; nonnegativity when NNLS is selected | Applied before or within the inner solve, with related labels reconstructed afterward |
| \(\mathbf{r}_q\) | Data mismatch returned for outer least squares | `OptimizationEstimation.residual` concatenated by `OptimizationObjective.calculate` | Recomputed for every outer trial |
| \(\mathbf{p}\) | Soft-condition residual entries | Equal-area CLP penalty values from `calculate_clp_penalties` | Appended to data residuals when configured |
| \(\operatorname{concat}\), \(\|\cdot\|_2^2\) | One vector whose squared entries define the outer least-squares mismatch | NumPy concatenation followed by SciPy `least_squares` | Connects all objectives and penalties to the outer iteration |

The equations now describe the work performed during one objective evaluation and how
successive trials are connected. The next section places that repeated calculation within
the complete lifecycle from a resolved analysis specification to an inspectable result.

<!--
Citations used:
- van Stokkum et al. (2004), used for separability, conditionally linear estimation, variable projection, and uncertainty/identifiability qualification.
- Mullen and van Stokkum (2007), used for separable least squares and variable-projection context; not used as authority for staging implementation details.

Incoming bridge proposal:
Section 3 should end after mapping rate-like shape quantities to explicit outer parameters and associated amplitudes to CLPs.
This section begins by formalizing exactly that two-contribution example before introducing the general matrix and nested objectives.

Outgoing bridge proposal:
This section ends after explaining one repeated objective evaluation and the outer feedback loop.
Section 5 can then separate initialization, repeated evaluation, and post-processing without rederiving the equations.

Five-item self-check:
1. Every displayed equation has a plain-language lead-in, complete symbol and dimension definitions, physical interpretation, and current-runtime mapping.
2. Arg min, Frobenius norm, Euclidean norm, weighting, constraint set, variable projection, and NNLS are defined before being relied upon.
3. Matrix columns retain CLP labels, while explicit outer parameters and CLPs remain separate in both notation and implementation.
4. Relations, constraints, scales, weights, linked blocks, residual concatenation, and penalties are placed at source-verified stages.
5. The text does not claim a TIMP port, one-time matrix construction, convergence, identifiability, or a universal internal matrix orientation.

Integration note:
- Assumptions: The canonical \(\mathbf{Y}=\mathbf{M}\mathbf{B}+\boldsymbol{\varepsilon}\) orientation is an explanatory view of the ordinary path; specialized global-element and linked layouts are explicitly qualified.
- Deliberate omissions: Full lifecycle ordering, result-field storage, provenance, histories, and persistence belong to Section 5.
- Dependencies: Section 3 owns the definitions and metadata of explicit parameters and CLPs. Section 5 should use rather than rederive the inner and outer equations.
- Proposed contract changes: None.
- Unresolved questions: None affecting the draft. Maintainer review may wish to assess the staging coexistence and path-specific use of Experiment-level and DataModel-level residual-function selections, which the text reports without interpreting as a stable design promise.
-->
