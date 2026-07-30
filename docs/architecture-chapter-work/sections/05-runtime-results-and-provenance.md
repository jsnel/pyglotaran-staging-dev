# 5. From a resolved specification to evidence for validation

## 5.1 The runtime lifecycle

The same objects play different roles before iteration, during each trial, and after the
optimizer stops. Their ordered passage through those roles is the *runtime lifecycle*.
Here, **initialization** means the one-time work that makes the declared analysis
numerically usable; an **objective evaluation** is one calculation of the residual vector
for a trial set of free explicit parameters; and **post-processing** means the calculations
that package the final state into diagnostics and scientific result structures. Keeping
these phases separate is important because a matrix that depends on a changing rate or
instrument parameter cannot be treated as if it were fixed during initialization.

At the public boundary, `Scheme.optimize(...)` receives three conceptually distinct
inputs: the Scheme, explicit `Parameters`, and measured data or references from which the
data can be loaded. The dataset input is first normalized into a mapping and assigned to
the matching per-dataset specifications. Thus, for the running time-and-wavelength
example, the measured surface is associated with its DataModel before the optimization
orchestrator is created. Data loading is not an operation hidden inside each numerical
trial. It occurs at the orchestration boundary, while the Scheme continues to describe
which Experiment and Element definitions apply to that surface.

Construction of `Optimization` begins the one-time semantic phase. Each Experiment is
resolved against the model library and the supplied initial parameters. During this step,
the explicit parameters referenced by the resolved specifications are collected into an
internal `Parameters` object. The implementation then gathers supported issues from the
resolved Experiments and stops with a model-issues exception if any are reported.
Only after these checks does it create one `OptimizationObjective` for each Experiment.
An objective creates either a numerical wrapper for one dataset or a linked wrapper when
the Experiment contains several dataset specifications. Dimension inference, orientation,
weight preparation, and alignment therefore belong to initialization of these wrappers,
as described in Section 3, rather than to every outer trial.

The outer problem is configured from the free explicit-parameter labels, their initial
values, and their bounds. The selected least-squares method and termination tolerances are
also stored before SciPy is called. This free numerical vector is narrower than the
complete serialized parameter collection: fixed and expression-determined values need not
be independent entries. SciPy's `least_squares` routine then controls the outer sequence
of trial values. Pyglotaran supplies the function that translates each trial into the
residual entries expected by that routine.

An objective evaluation begins by writing the trial values back to the internal explicit
parameters. Each Experiment objective then recalculates its Element matrices. The
matrices are reduced according to configured coefficient relations, and the inner
estimator obtains the conditionally linear parameters (CLPs) for the current outer trial.
Where needed for supported CLP penalties, reduced estimates are mapped back to the
corresponding coefficient labels. Residual entries and applicable penalty entries are
combined within the objective. Finally, the contributions from all Experiment objectives
are concatenated into one vector and returned to SciPy. This is the repeated phase:
parameter-dependent matrices, CLP estimates, and residuals change together as the outer
parameters change. Section 4 explains the mathematics of this nesting; the temporal view
here establishes when those operations occur.

SciPy uses the returned vector to choose another trial or to stop according to its method,
tolerances, and evaluation limit. Pyglotaran captures the termination message and, when
enabled, the textual iteration report from which an optimization-history table can be
constructed. These records describe the numerical run; they do not by themselves
guarantee convergence to a unique solution. A clean termination, a small residual, and a
physically convincing interpretation remain different questions.

After the outer call stops, the implementation evaluates the final state again and asks
each objective to construct its results. One objective corresponds to one Experiment, but
the returned `OptimizationResult` objects are keyed by dataset label and combined into
the top-level mapping. This post-processing reconstructs the final matrices, CLPs,
residuals, and contribution-specific datasets needed for inspection. It also determines
counts used in the diagnostic statistics and creates `OptimizationInfo` from the available
SciPy output. Back in `Scheme.optimize(...)`, covariance-derived standard errors are
assigned to the optimized explicit parameters when covariance is available. Only then is
the top-level `Result` constructed from the Scheme, initial and optimized parameters,
diagnostics, and dataset-keyed numerical results.

<!-- Insert Mermaid source from ../figures/fig-05-runtime-lifecycle.mmd here. -->

**Figure 5. Runtime lifecycle from declared analysis to structured result.** Solid arrows
show normal execution order. The backward arrow inside the middle group denotes repeated
requests from the outer optimizer; the dotted arrow leaves that cycle on termination or a
handled failure. The three groups distinguish one-time association, resolution, and
initialization from repeated objective evaluation and post-optimization result
construction. In particular, the figure does not imply that parameter-dependent matrices
are prepared once.

Figure 5 also locates two failure boundaries. Missing or incoherent relationships detected
by the supported issue checks prevent numerical objectives from being created. A failure
during the outer call can instead be raised or converted into a terminated run according
to the configured exception behavior, after which the package still attempts to describe
the final available state. The lifecycle therefore makes error context and phase as
important as the mere fact that a numerical vector was returned. Its scientific value
becomes clearer when the contents of that returned structure are examined.

## 5.2 Results, provenance, persistence, and validation

A parameter vector alone cannot show where the fit fails or whether the fitted
contributions make physical sense. The top-level `Result` therefore retains the Scheme,
the initial and optimized explicit parameters, optimization information, and a mapping
from dataset labels to numerical results. Its `input_data` convenience property provides
the measured arrays used for those dataset results. This organization places the final
parameter values beside the analysis specification and observations to which they belong,
rather than presenting them as context-free numbers.

Each dataset-level `OptimizationResult` stores the input array, the residual array when it
is available, Element-result and activation-result mappings, a fit decomposition, and
metadata. Calculated or *fitted data* are obtained as input data minus residuals. For the
running experiment, retaining both surfaces allows a reader to compare measured and
calculated signals across time and wavelength, while the residual surface can reveal
localized temporal or spectral structure that a single scalar error measure would hide.
The metadata identify the model and global dimension names, the applied inter-dataset
scale, the root-mean-square error, and an optional weighted root-mean-square error.

The fit decomposition keeps the final CLP array beside the corresponding matrix array. In
the running example these data connect the wavelength-dependent coefficients to the
time-dependent shapes that generated the fitted surface. Separate Element-result datasets
can present contribution-specific quantities in scientifically useful coordinates. They
are produced through each contributing Element's result method and receive an
`element_uid` attribute containing the fully qualified implementation name. This is a
specific form of **provenance**—information recording where a result came from—because it
links an output dataset to the Element implementation that created it. It does not, on
its own, record every environmental detail that could affect reproducibility.

`OptimizationInfo` provides the run-level diagnostic context. Its fields include free
parameter labels, function- and Jacobian-evaluation counts, termination information,
cost and chi-square quantities, the number of data points, outer parameters and CLPs,
degrees of freedom, optimality, a Jacobian, and a covariance matrix when these are
available. The optimized `Parameter` objects can then carry standard errors derived from
that covariance calculation. History objects are retained as well, although their exact
coverage depends on how the current runtime populates them. These quantities can help
assess numerical sensitivity and precision under the fitted model; they are not a
general identifiability analysis, nor do they establish that the stochastic assumptions
behind an uncertainty estimate are adequate.

**Persistence** means converting these in-memory structures into files that can later be
loaded. `Result.save(...)` dispatches through a project-I/O provider, while array fields
are serialized through a data-I/O provider. Under the default saving policy, the Scheme,
initial and optimized parameters, histories, input and residual data, calculated data,
fit decomposition, and contribution-specific datasets can be written as a related set of
files. A minimal policy deliberately omits selected derived arrays, so persistence should
not be described as an unconditional archival guarantee. When measured data were loaded
through the I/O layer, their `source_path` and fully qualified `io_plugin_name` attributes
can also be used to retain the relationship to the original source instead of silently
changing its format. Scheme, parameter, and result paths are updated by the corresponding
save/load wrappers where configured.

These structures support the validation stage of scientific model discovery without
automating it. A researcher can inspect residual patterns, compare fitted contributions,
consider parameter precision, and ask whether the recovered temporal and spectral shapes
are compatible with the proposed physicochemical model (van Stokkum et al., 2004). The
architecture makes those questions answerable from structured outputs, but it cannot
decide whether a mechanism is scientifically true or whether another model would explain
the data equally well. Core pyglotaran supplies the arrays and metadata for that
assessment. Most plotting and higher-level exploration are provided separately by
`pyglotaran-extras`, often used from an external notebook environment.

Result construction is therefore not merely the last formatting step of optimization. It
closes one estimation cycle by preserving observations, differences, decompositions, and
diagnostics that can motivate the next revision of the analysis. Producing comparable
results for heterogeneous scientific contributions and file formats, however, depends on
common extension boundaries, which are the subject of the next section.

<!--
Citations used:
- van Stokkum et al. (2004), used for residual inspection and physicochemical interpretation as parts of scientific validation.

Incoming bridge proposal:
Section 4 should close by observing that its equations describe one residual evaluation rather than the whole run.
This section then separates one-time initialization, repeated evaluation, and post-optimization result construction.

Outgoing bridge proposal:
This section establishes that structured, contribution-aware results support inspection but do not automate scientific judgment.
Section 6 can begin by asking how new scientific contributions and file formats participate in that same lifecycle without replacing the common optimizer.

Five-item self-check:
1. Dataset association, resolution, issue checking, objective construction, repeated evaluation, and result construction follow current source order.
2. One-time wrapper creation is distinguished from matrices recalculated for each objective evaluation.
3. The top-level mapping is described as dataset-keyed; no per-Experiment result container is invented.
4. Result fields, diagnostics, persistence, source relationships, and Element identity are limited to verified fields.
5. Validation is presented as evidence-based scientific assessment, not automated proof; plotting remains outside core.

Integration note:
- Assumptions: Current class names and field layouts are implementation anchors at revision `468c4cd57aaf25c10edf85cd197df771bad0a766`, not stability promises.
- Deliberate omissions: Section 4 owns equations and estimator derivations; Section 6 owns registry mechanics and notebook/extras detail.
- Dependencies: The coordinator should embed `fig-05-runtime-lifecycle.mmd` at the marker and preserve the Section 4-to-5 transition from one evaluation to the full lifecycle.
- Proposed contract changes: Replace any phrase “per-experiment optimization results” with “per-Experiment objectives and dataset-keyed optimization results.”
- Unresolved questions: [VERIFY: Should duplicate dataset labels across Experiments be rejected or namespaced? `optimization.py:137-140` contains a TODO.] [VERIFY: Is `add_svd` intended to control retained result arrays? It is stored but no retained SVD field is verified.] [VERIFY: Should serialized `glotaran_version` preserve the creation runtime rather than recomputing on load?] [VERIFY: Should the diagnostic success flag mirror SciPy convergence status rather than only the presence of a result object?] [VERIFY: Is `ParameterHistory` intended to receive per-iteration snapshots? The inspected path appends once.] [VERIFY: Is a weighted-residual array intended to be retained, or only weighted RMSE metadata?]
-->

