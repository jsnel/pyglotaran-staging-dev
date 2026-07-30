# Architecture and mathematics review

## Review scope

This review covers the frozen chapter and merged evidence ledger identified in
`00-integrated-snapshot.md`. It checks scientific definitions, coordinate and matrix
orientation, separability, weights and scales, explicit outer parameters versus CLPs,
variable projection and NNLS, CLP relations and constraints, penalties, uncertainty
language, the distinction between global analysis and global dimension, and agreement
among equations, prose, figures, and tables. Current source at pyglotaran revision
`468c4cd57aaf25c10edf85cd197df771bad0a766` was inspected where a ledger claim needed
independent checking. No tests were run, and no other review report was read.

## P0 findings

### P0-1 — The covariance and standard-error claims do not describe the quantities or coordinates actually stored

- **Chapter location:** §4.3, lines 808–815; §5.1, lines 945–954; Figure 5, lines
  979–984; §5.2, lines 1036–1045.
- **Claim:** Pyglotaran calculates a covariance estimate or covariance matrix and
  covariance-derived standard errors for free explicit parameters, subject to general
  local-Jacobian and residual qualifications.
- **Evidence anchor:** `pyglotaran/glotaran/optimization/info.py:170–185` and
  `222–244` show that the field named `covariance_matrix` is the rank-truncated
  \((J^\mathsf{T}J)^+\)-type inverse normal matrix; the residual-variance factor is not
  included. `info.py:212–219` multiplies the square root of its diagonal by the reported
  root-mean-square error only when assigning parameter standard errors.
  `pyglotaran/glotaran/parameter/parameter.py:256–283` shows that a parameter with
  `non_negative=True` is optimized in the logarithmic coordinate and exponentiated on
  update, while `info.py:212–219` assigns the optimization-coordinate error directly to
  the physical-valued `Parameter` without the delta-method factor \(p\).
- **Correction:** Describe `covariance_matrix` by its observed semantics: a
  rank-truncated inverse normal matrix for the outer optimizer coordinates. State that
  the reported standard error is the residual-scale multiplier times its diagonal
  square root. Explicitly warn that, for logarithmically transformed parameters, the
  assigned error remains in the optimizer coordinate and is not converted to an
  approximate error on the exponentiated value. Alternatively, restrict the statistical
  interpretation to untransformed parameters and avoid calling the stored matrix a
  covariance estimate.
- **Rationale:** Calling an unscaled inverse normal matrix a covariance matrix is a
  mathematical category error unless the omitted variance convention is made explicit.
  Attaching a log-coordinate standard error to a parameter shown in physical units can
  also produce a quantitatively wrong uncertainty interpretation. The chapter's generic
  “local diagnostic” caveat does not disclose either deterministic implementation fact.

### P0-2 — Degrees of freedom and derived uncertainty statistics are not valid uniformly across the supported paths

- **Chapter location:** §4.3, lines 808–815; §5.1, lines 945–954; §5.2, lines
  1036–1045.
- **Claim:** The implementation calculates degrees of freedom, reduced chi-square or
  RMSE, and associated uncertainty diagnostics after optimization, with only general
  statistical qualifications.
- **Evidence anchor:** `pyglotaran/glotaran/optimization/info.py:168–185` defines
  `number_of_data_points` as `result.fun.size` and degrees of freedom as that size minus
  the number of outer parameters and reported CLPs. Penalty entries are part of
  `result.fun` because `pyglotaran/glotaran/optimization/objective.py:559–577` appends
  them to the data residual vector. More decisively, the global-element result reshapes
  the fitted coefficient vector to
  \(k_{\mathrm{global}}\times k_{\mathrm{model}}\) at
  `objective.py:656–665` but reports the CLP count as
  \(k_{\mathrm{global}}+k_{\mathrm{model}}\) at `objective.py:670`. The latter count is
  then subtracted in `info.py:170–177`.
- **Correction:** Do not present the reported degrees of freedom and quantities derived
  from it as path-independent statistical diagnostics. State that the current count uses
  the complete least-squares residual length, including soft-penalty entries, and that
  the global-element path reports a sum of the two label-axis sizes even though its
  fitted coefficient array has their product. Either exclude that path from the
  uncertainty statement or identify the fields strictly as current runtime outputs with
  these limitations.
- **Rationale:** Penalty residuals are not ordinary independent observations, and a sum
  rather than product CLP count gives the wrong number of fitted coefficients for the
  Kronecker/global-element problem. Both affect degrees of freedom, reduced chi-square,
  RMSE, and the scale applied to standard errors. General wording about local
  assumptions does not repair this arithmetic mismatch.

### P0-3 — The stated directional alignment behavior is not guaranteed by the inspected `forward` implementation

- **Chapter location:** §3.2, lines 550–560.
- **Claim:** `nearest`, `backward`, and `forward` select the closest permitted value in
  the corresponding direction within the configured tolerance.
- **Evidence anchor:** `pyglotaran/glotaran/optimization/data.py:337–348` filters the
  difference array for `forward` or `backward`, then uses the filtered array's
  `argmin()` as an index into the original, unfiltered `target_axis`. The original
  positions are lost. For example, with an ascending target axis `[1, 5, 6]`, source
  coordinate `5.5`, and tolerance at least `0.5`, the `forward` branch filters to
  `[0.5]`, obtains index zero, and returns `target_axis[0] == 1`, which is neither
  forward nor within the tolerance whose check admitted the match. Ledger claim DP-09
  records the intended directional semantics but does not account for this indexing.
- **Correction:** Until the implementation is corrected, qualify the prose as the
  intended matching policy and disclose that the inspected `forward` path does not
  reliably preserve the filtered target index. Do not state the directional behavior as
  an implemented guarantee.
- **Rationale:** Alignment determines which observations share one inner coefficient
  problem. An incorrect directional match changes the joint numerical problem rather
  than merely its presentation, so the current source contradicts the unqualified
  architectural claim.

### P0-4 — NNLS constrains the reduced coefficient vector, not necessarily every reconstructed CLP

- **Chapter location:** §4.2, lines 751–757; Table 3, line 876.
- **Claim:** The NNLS alternative restricts fitted CLPs to nonnegative values.
- **Evidence anchor:** `pyglotaran/glotaran/optimization/nnls.py:31–33` constrains the
  coefficient vector passed to SciPy. Before that solve, a CLP relation removes its
  target and folds the target column into the source column
  (`optimization/matrix.py:227–242`). After the solve,
  `optimization/estimation.py:58–64` reconstructs
  `target = relation.parameter * source`. `model/clp_relation.py:9–17` and the
  `ParameterType` definition at `model/item.py:39` impose no nonnegative sign on the
  relation factor. A negative factor therefore reconstructs a negative target CLP from a
  nonnegative reduced source coefficient.
- **Correction:** Say that SciPy NNLS constrains the coefficients of the **reduced inner
  system**. Add that zero/only constraints remain zero on expansion, whereas a
  relation-reconstructed target inherits the relation factor and need not be
  nonnegative unless that factor is itself restricted appropriately. Make the same
  qualification in Table 3.
- **Rationale:** The current prose makes a guarantee about the full CLP set that the
  relation-expansion stage can violate. This matters scientifically whenever sign is the
  reason for selecting NNLS.

## P1 findings

### P1-1 — The symbol \(q\) mixes incompatible numerical granularities, so the displayed matrix dimensions are not general

- **Chapter location:** §4.1, lines 654–674; §4.2, lines 697–729; Table 3, lines
  867–876.
- **Claim:** One dataset or numerical objective unit \(q\) is represented generally by
  \(\mathbf{Y}_q\in\mathbb{R}^{n_{m,q}\times n_{g,q}}\),
  \(\mathbf{M}_q\in\mathbb{R}^{n_{m,q}\times k_q}\), and
  \(\mathbf{B}_q\in\mathbb{R}^{k_q\times n_{g,q}}\), while Table 3 allows \(q\) to mean
  a dataset slice, linked coordinate block, or whole objective contribution.
- **Evidence anchor:** The ordinary path constructs a list of one matrix and one data
  vector per global coordinate (`optimization/matrix.py:292–325`;
  `optimization/objective.py:515–534`). An index-dependent or weighted matrix has shape
  \(n_g\times n_m\times k\), so its matrix can differ with the global index
  (`matrix.py:39–55`, `81–90`, `257–274`). Linked data likewise form a vertically
  concatenated block separately at each aligned global coordinate
  (`matrix.py:187–209`). The global-element path instead flattens the full observation
  and uses a Kronecker-type matrix of shape
  \((n_g n_m)\times(k_g k_m)\) (`matrix.py:151–185`;
  `objective.py:549–557`). Ledger claim NM-16 acknowledges that these paths change the
  realized layout.
- **Correction:** Define a stable per-inner-solve notation, for example
  \[
  \mathbf{y}_{qj}=
  \mathbf{M}_{qj}(\boldsymbol{\theta})\mathbf{b}_{qj}
  \boldsymbol{\varepsilon}_{qj},
  \]
  where \(j\) is an aligned global coordinate and the row count may be a linked block.
  Present \(\mathbf{Y}=\mathbf{M}\mathbf{B}\) as the convenient special case in which a
  common matrix applies across columns. State separately that the global-element path
  uses a flattened observation and a Kronecker-composed matrix. Use the same
  granularity for \(q\) in the outer concatenation and Table 3.
- **Rationale:** As written, one symbol alternates among a full dataset, a coordinate
  slice, and an objective. A single \(n_m\times k\) matrix cannot multiply all columns
  when the matrix or row-block structure changes with the global coordinate, and the
  global-element path does not have the displayed dimensions. The high-level
  separability argument remains sound, but its dimensional statement needs a scoped
  domain.

### P1-2 — “Equal-area” is presented as a coordinate area although the penalty is an unweighted sample sum

- **Chapter location:** §4.3, lines 787–798; Table 3, line 878.
- **Claim:** An equal-area CLP penalty appends a weighted discrepancy between configured
  source and target coefficient areas.
- **Evidence anchor:** `pyglotaran/glotaran/optimization/penalty.py:36–50` selects CLP
  samples by coordinate interval but computes
  \[
  w\left|
  \sum_j |b_{\mathrm{source},j}|
  -\alpha\sum_j |b_{\mathrm{target},j}|
  \right|.
  \]
  It does not use coordinate spacings, quadrature weights, or an integral. The
  `global_axis` is used only to decide which samples fall in each configured interval.
- **Correction:** Describe the observed operation as a weighted difference between sums
  of absolute CLP samples over configured intervals. If retaining the class name
  “equal-area,” explicitly state that this is the implementation's label and is
  proportional to a numerical area only under additional grid-spacing assumptions.
- **Rationale:** On a nonuniform grid—or on source and target intervals with different
  sampling—the sum is not a coordinate area. The current wording adds a mathematical
  interpretation not supported by the implementation.

### P1-3 — The chapter does not distinguish the weighted outer residual from the unweighted residual retained in results

- **Chapter location:** §3.1, lines 523–530; §4.2, lines 722–729; §5.2, lines
  1017–1024.
- **Claim:** Sections 3–4 correctly explain that weights multiply observations and
  matching matrix contributions, but §5 then refers to “the residual array” without
  explaining that it is not the same weighted residual vector consumed by the outer
  optimizer.
- **Evidence anchor:** `optimization/data.py:67–80` applies weights before estimation.
  During result construction, `OptimizationData.unweight_result_dataset` first stores a
  transient `weighted_residual` and then divides `residual` by the weights
  (`data.py:244–251`). The single and linked result paths retain the restored residual
  at `optimization/objective.py:748–758` and `899–927`; only weighted RMSE metadata
  survives in the result abstraction, as ledger claim RR-11 also records.
- **Correction:** Add a bridge in §5 stating that \(\mathbf r_q\) in §4 is the weighted
  optimizer residual, whereas the dataset-level `OptimizationResult.residuals` is
  restored to the measured-data scale. State that weighted RMSE may be retained as
  metadata, but a weighted-residual array is not a top-level retained result field.
- **Rationale:** Without the distinction, a reader can interpret plotted residuals using
  the objective's weighting scale or try to reproduce the reported outer cost from an
  unweighted stored array. This is an architecture-to-mathematics mismatch even though
  each local paragraph is individually plausible.

### P1-4 — The QR variable-projection path lacks the rank condition needed for the claimed inner least-squares solution

- **Chapter location:** §4.2, lines 741–749.
- **Claim:** The staging variable-projection routine uses QR factorization to calculate
  the CLPs and residual for the current matrix, described only as operating “under its
  numerical assumptions.”
- **Evidence anchor:** `optimization/variable_projection.py:33–45` uses an unpivoted QR
  factorization followed by a triangular solve. It performs no rank-revealing pivot,
  pseudoinverse fallback, conditioning test, or explicit handling of the LAPACK status.
- **Correction:** Name the relevant assumption: the reduced inner matrix must have a
  sufficiently well-conditioned, full-column-rank coefficient basis (and enough
  independent rows for that basis). State that the routine is not a rank-revealing
  least-squares solver and that duplicated or linearly dependent effective CLP columns
  can make the inner coefficients nonunique or the solve numerically unreliable.
- **Rationale:** Variable projection eliminates the inner variables, but it does not
  make them identifiable. The rank condition connects the scientific identifiability
  caveat to the concrete numerical method and prevents “QR-based least-squares solution”
  from sounding unconditional.

## P2 findings

### P2-1 — Figure 5 labels the returned quantity as a trial vector instead of a residual vector

- **Chapter location:** Figure 5, line 976, with caption at lines 991–995.
- **Claim:** The arrow from “Concatenate contributions across Experiment objectives”
  back to “SciPy requests a trial residual vector” is labeled “trial vector returned.”
- **Evidence anchor:** `optimization/optimization.py:175–189` writes the trial vector
  into `Parameters` and returns the concatenated objective **residual** vector to SciPy.
  Figure 4, lines 847–849, depicts the distinction correctly: the objective sends one
  residual vector to SciPy, and SciPy proposes another trial.
- **Correction:** Relabel the Figure 5 return arrow “residual vector returned,” or add a
  separate SciPy node with two distinct arrows: trial values to the callback and residual
  values back to SciPy.
- **Rationale:** The current label reverses the fundamental outer-loop data flow and
  disagrees with both the prose and Figure 4.

## P3 findings

No P3 findings. Optional enrichment should wait until the P0 and P1 corrections are made.

## Areas verified without a finding

- The chapter consistently treats separability as a modeling assumption rather than a
  fact established by a two-dimensional measurement.
- The explicit-parameter/outer-parameter/CLP distinction is scientifically and
  computationally sound, including the separation of logarithmic outer positivity from
  inner NNLS.
- The distinction between global analysis as a simultaneous scientific strategy and
  global dimension as a coordinate role is explicit and consistent in §§1.2, 3.1, and
  3.2.
- The placement of CLP relations and zero/only constraints before the inner solve, with
  reconstruction afterward, agrees with source apart from the NNLS sign qualification
  in P0-4.
- Weight and scale are correctly distinguished as residual influence versus
  contribution/block scaling; P1-3 concerns only the missing transition to the
  unweighted stored result residual.

## Snapshot confirmation and recommendation

The frozen inputs were verified against `00-integrated-snapshot.md`:

- Chapter SHA-256:
  `B8104026C07928A8832809B194B9431215B7A37F058E06D0EC0772E5F5327A17`.
- Evidence-ledger SHA-256:
  `59D87C496049A82E1AA29262AFAF775DEE83AA7E877E1E1FAAE79B57FAD63D8B`.
- Authoritative pyglotaran revision:
  `468c4cd57aaf25c10edf85cd197df771bad0a766`.

**Recommendation: revise before acceptance.** The chapter's central architectural thesis
and scientific framing are sound, but the four P0 contradictions—especially the
uncertainty semantics, directional alignment, and NNLS/relation interaction—must be
corrected or explicitly scoped. The P1 notation and residual/penalty qualifications
should be resolved in the same revision so that the equations, code concordance, and
result interpretation agree.
