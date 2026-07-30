# 3. Giving observations and unknowns numerical roles

## 3.1 Measured arrays are not data models

A table of signal values becomes useful for scientific estimation only when each axis has a
meaning. In the running pump–probe example, a value belongs to a particular delay time and
wavelength; exchanging those axes would change how a numerical routine should read the same
block of numbers. Pyglotaran therefore works with xarray, a labeled-array library that stores
dimension names and coordinate values alongside the numbers. A measured array can enter as
an `xarray.DataArray` or an `xarray.Dataset`. The preparation boundary can turn a DataArray
into a Dataset whose variable named `data` contains the observations, while the coordinate
labels remain available for later interpretation (DP-01).

Those observations must remain distinct from the scientific instructions for using them. A
data model states which scientific contributions apply to one dataset and can configure
element scales, weights, optional global contributions, and a residual-function field. In the
inspected implementation this responsibility is represented by `DataModel`. A resolved
runtime copy can carry an associated Dataset or source path, but the association does not
make the DataModel itself the measured data. The distinction is comparable to that between a
recipe and the ingredients placed beside it: attaching the ingredients to the recipe for
one calculation does not turn the instructions into observations (DP-02).

The labels also determine two coordinate *roles*. The **model dimension** is the coordinate
along which a model matrix is evaluated. The **global dimension** is the coordinate across
which conditionally linear contributions are organized or estimated. In the running example,
delay time has the model role and wavelength has the global role. These are not universal
synonyms. Another element may calculate a matrix along a different physical coordinate, and
“global dimension” names an axis role rather than the scientific method called global
analysis.

For the ordinary two-dimensional path, the contributing elements declare their model
dimension and must agree on it; the other dimension of the measured `data` variable is
inferred as global. The numerical wrapper then obtains both coordinate arrays by name. If the
stored dimension order is the reverse of model-then-global, it transposes a copy before
estimation. Thus a file need not happen to store time along its first memory axis for time to
serve as the model dimension. Labels provide the meaning, and orientation converts that
meaning into the ordering expected by the numerical path (DP-03, DP-04).

Orientation is followed by *slicing*: exposing the data in pieces suited to the calculation.
In the usual path, each global coordinate supplies one vector along the model axis. For the
spectroscopy example, the inner calculation therefore receives one time trace at each
wavelength. The inspected implementation also supports a specialized path in which elements
model both coordinate roles; there the weighted surface is transposed and flattened for a
combined solve. This exception is important because it prevents a convenient teaching
orientation from becoming an unsupported claim about every element matrix (DP-05).

A **weight** changes how strongly selected observations influence the mismatch being fitted.
Weights can be supplied as an xarray variable or constructed from values assigned to
intervals of the model and global coordinates. The numerical wrapper multiplies the observed
values by these factors, while matrix construction applies matching factors to the calculated
contributions. A factor greater than one therefore makes a discrepancy count more strongly;
a factor below one reduces its influence. Because the factors can vary over both axes and can
be flattened on the specialized path, Section 4 represents weighting by a general operation
rather than assuming one fixed matrix multiplication (DP-06).

A **scale** answers a different question. It changes the magnitude of a calculated
contribution or dataset block, rather than directly specifying how residual entries are
judged. A data model can scale an individual element contribution, and a multi-dataset
Experiment can scale a dataset's matrix block before linked blocks are joined. Some scales
may themselves refer to explicit parameters. Keeping “scale” and “weight” separate is
scientifically useful: the former belongs to the prediction being compared, whereas the
latter changes the relative influence of discrepancies (DP-07).

## 3.2 Joint organization across datasets

Related measurements can constrain a scientific explanation more strongly than either
measurement alone. For example, two pump–probe datasets collected under different conditions
may share temporal contributions while differing in sampling, amplitude, or coverage. The
multi-dataset literature treats such shared and dataset-specific quantities as choices that
must be stated by the scientific model rather than assumed from file layout (Mullen & van
Stokkum, 2007). In current pyglotaran, an Experiment is the grouping within which one or more
named dataset specifications can be estimated jointly (DP-08).

Joint estimation first requires the package to decide which global-coordinate values are
comparable. Two spectrometers might report nominally corresponding wavelengths as 500.0 and
500.1 nm, for example. **Alignment** is the numerical act of mapping such coordinate values
onto a common set. A configured **tolerance** gives the largest permitted separation. The
methods `nearest`, `backward`, and `forward` specify whether the closest value, a value in one
direction, or a value in the other direction may be used. These are matching rules, not
claims that two observations have identical scientific content (DP-09).

The inspected linking path builds the union of aligned global coordinates and records which
datasets contribute at each one. If two source coordinates would map ambiguously to the same
target, alignment raises an error rather than silently combining them. At a shared wavelength,
the model-axis vectors from the participating datasets are concatenated into one numerical
block. At a wavelength observed by only one dataset, only that dataset's vector is present.
Configured dataset scales are applied to the corresponding matrix blocks. Consequently,
linking preserves gaps in coverage rather than inventing missing observations (DP-07,
DP-09).

This distinction is reflected in two numerical representations. An objective with one
dataset uses `OptimizationData`, which supplies its axes, weights, and coordinate-wise data
vectors. An objective with several datasets uses `LinkedOptimizationData`, which additionally
records aligned coordinates, participating-dataset combinations, source indices, block
sizes, and dataset scales. These wrappers build numerical inputs; they do not replace the Experiment or
its DataModels as scientific specifications (DP-10).

Alignment alone does not establish that quantities should be shared. That decision comes
from common CLP labels, configured relations, element definitions, and other model choices
discussed in Section 4. Likewise, simultaneous fitting is an instance of global analysis only
because measurements are analyzed under shared scientific structure, not merely because the
software has an axis called global. Once the observed blocks are coordinated, a different
question remains: which unknown quantities belong to the outer fit, and which can be
estimated inside it?

## 3.3 Explicit parameters and conditionally linear coefficients

Some unknown quantities determine the shapes calculated by a scientific contribution,
whereas others only choose how much of each already-calculated shape is present. In the
running example, a decay-rate constant changes a temporal profile. Once that profile is
known, its amplitude at one wavelength can be found by an ordinary linear combination. This
computational distinction motivates two separate representations rather than one undifferentiated
list of “fit parameters” (DP-15).

An **explicit parameter** is a named, serializable quantity whose current value is supplied
to the scientific definitions. The `Parameter` representation includes metadata such as
whether the value may vary, finite lower or upper bounds, an optional expression, a
positivity setting, and a standard-error field. `Parameters` is the collection that holds
these objects by label. A **free** explicit parameter is selected for the outer optimizer; a
**fixed** one retains its supplied value (DP-11, DP-13).

An **expression-defined** parameter is calculated from other explicit parameters. The
implementation marks it as non-varying and updates its value when the independent values
change. It is therefore present in `Parameters` and can be referenced by a scientific
contribution, but it does not occupy an independent position in the outer vector. Bounds,
meanwhile, accompany free values sent to the outer least-squares routine (DP-12, DP-13).

The `non_negative` setting on an explicit parameter deserves careful wording. In the
inspected implementation it uses a logarithmic coordinate during optimization and
exponentiates the trial value on return. It is thus a supported positivity transformation,
not simply a zero lower bound. It is also unrelated to non-negative least squares for the
inner coefficients, which Section 4 introduces separately (DP-13).

A **conditionally linear parameter (CLP)** is one of those inner coefficients. It is
conditional because it can be estimated by a linear or constrained-linear calculation once
the current explicit parameters have fixed the matrix shapes. CLPs are represented through
ordered matrix-column labels and inner-estimation arrays. They are not stored as `Parameter`
objects, do not appear in `Parameters`, and are not independently supplied to the outer
optimizer (DP-14).

Calling a free explicit parameter an **outer parameter** describes where the software
estimates it. It does not claim that every such quantity is intrinsically nonlinear in every
possible scientific reformulation. Conversely, a CLP may have direct physical meaning—such
as an associated spectral amplitude—even though its computational role is linear after the
shapes are fixed. The categories concern estimation structure, not scientific importance
(DP-15).

For the two-contribution example, the rate constants and instrument-response quantities can
be explicit outer parameters because they determine the temporal profiles. The two spectral
amplitudes at each wavelength are CLPs because, for fixed profiles, they enter as
multipliers. The resulting separation raises the mathematical question answered next: how
can pyglotaran solve those inner coefficients during every trial of the explicit outer
parameters?

<!--
Citations used:
- Mullen and van Stokkum (2007), used for the scientific rationale for coordinated multi-dataset modeling and shared versus dataset-specific quantities.

Incoming bridge proposal:
Section 2 should close after the analysis specification has been instantiated, connected, and checked semantically.
This section begins at the next boundary: attaching coordinate meaning and distinct computational roles to measured values and unknown quantities.

Outgoing bridge proposal:
This section ends with explicit outer parameters determining shapes and CLPs determining amplitudes once those shapes are known.
Section 4 can therefore begin from the two-contribution observation equation and develop the nested estimator without redefining either category.

Five-item self-check:
1. Measured arrays and DataModels remain distinct even though a resolved runtime DataModel can carry a data association.
2. Model and global dimensions are defined as coordinate roles, with time and wavelength used only for the running example.
3. Weight, scale, alignment, tolerance, and linked numerical blocks are explained before implementation identifiers carry the argument.
4. Free, fixed, bounded, positivity-transformed, and expression-defined explicit parameters are distinguished from CLPs.
5. CLPs remain outside Parameters, and no explicit parameter is declared intrinsically nonlinear.

Integration note:
- Assumptions: The chapter's ordinary matrix orientation describes the common two-dimensional path; the specialized global-element path is acknowledged but not derived here.
- Deliberate omissions: Matrix equations, inner estimators, CLP relations and constraints, penalties, uncertainty calculations, and lifecycle ordering belong to Sections 4-5.
- Dependencies: Section 2 must have already defined DataModel and Experiment. Section 4 should reuse the final explicit-parameter/CLP distinction rather than restating parameter metadata.
- Proposed contract changes: None.
- Unresolved questions: None. A maintainer may wish to review the coexistence of Experiment-level and DataModel-level residual-function fields, but it does not alter this section's categorical distinctions.
-->
