# Frozen paragraph-level chapter skeleton

**Status:** Gate 0 frozen on 2026-07-30. Packet authors may propose changes only in integration notes. The coordinating editor owns final numbering, synopsis, transitions, conclusion, and reference list.

## Global argumentative arc

The chapter begins with a scientific difficulty: a measured time-by-wavelength surface does not directly reveal the few physical processes that may have generated it. It then explains why iterative model discovery benefits from separating reusable scientific definitions, measured arrays, explicit outer parameters, conditionally linear coefficients, numerical estimation, and inspectable results. The static architecture is introduced before the numerical path, the two kinds of unknowns before their nested estimator, and the estimator before the runtime lifecycle. Extension boundaries and trade-offs then test the claim that these separations enable reuse without eliminating complexity. The conclusion returns to model specification, estimation, validation, and revision.

## 0. Opening synopsis and scope — coordinator, 350–450 words

**Section purpose:** Orient the reader to the scientific problem, the architectural thesis, the staging evidence basis, and exclusions without front-loading history or classes.

**Claims uniquely owned here:** The chapter's working thesis; the present source is the authority for architecture; staging names are evidence rather than v1 promises; the chapter covers representation, realization, estimation, results, and extensions rather than a user tutorial.

**Definitions introduced here:** *analysis architecture* in ordinary language; one-sentence provisional meanings of global and target analysis, explicitly deferred to Section 1.

**Prior concepts this section may assume:** Basic measurement and curve-fitting ideas only.

**Material explicitly deferred elsewhere:** Full scientific definitions and lineage to Section 1; entity roles to Section 2; mathematics to Section 4; evaluation to Section 6 and conclusion.

**Required evidence namespace:** `ED-*` plus high-level citations to `FR-*`.

**Required equation, figure, or table:** None.

**Opening premise:** A time-resolved experiment can produce far more measured values than directly interpretable physical quantities.

**Paragraph plan:** (1) measurement and inverse problem; (2) global/target analysis and model-discovery cycle in compact form; (3) architectural thesis and principal separations; (4) inspected-staging scope, evidence hierarchy, and exclusions; (5) route through the chapter.

**Exit point or bridge:** To understand the separations, first establish the scientific problem and the software lineage that responded to it.

## 1. From a measured surface to a scientific analysis — Packet A, 900–1,200 words

### 1.1 What the experiment measures

**Section purpose:** Give a non-spectroscopist a concrete mental image of time- and wavelength-resolved observations.

**Claims uniquely owned here:** The running experiment records a signal over delay time and wavelength; overlap in a two-dimensional surface makes direct mechanistic interpretation difficult; separability is a useful modeling assumption, not a fact guaranteed by the data.

**Definitions introduced here:** time-resolved spectrum; measured data surface; temporal contribution; associated spectrum; unexplained variation/noise; identifiability in plain language.

**Prior concepts this section may assume:** Opening synopsis only.

**Material explicitly deferred elsewhere:** Matrix orientation, explicit parameter objects, CLP estimation, and equations to Sections 3–4.

**Required evidence namespace:** `FR-*`.

**Required equation, figure, or table:** Figure 2, original separable-observation diagram. No displayed estimator equation.

**Opening premise:** At one delay the instrument records a spectrum; repeated delays stack those spectra into a surface.

**Paragraph plan:** (1) physical setup and axes; (2) why overlapping contributions obstruct direct reading; (3) two-component explanation in words; (4) observation model versus physicochemical model; (5) assumption dependence and identifiability.

**Exit point or bridge:** Once contributions are hypothesized, analysis requires a disciplined cycle for estimating and testing them.

### 1.2 Global analysis, target analysis, and model discovery

**Section purpose:** Define the scientific strategies before any software objects appear.

**Claims uniquely owned here:** Global analysis fits measurements simultaneously under shared structure; target analysis evaluates a specified physicochemical model and seeks physically interpretable quantities; model discovery iterates specification, estimation, validation, and revision.

**Definitions introduced here:** global analysis; target analysis; physicochemical model; model for the observations; inverse problem; validation.

**Prior concepts this section may assume:** Running observation example and separable contribution idea.

**Material explicitly deferred elsewhere:** Global dimension to Section 3; optimizer details to Section 4; validation data structures to Section 5.

**Required evidence namespace:** `FR-*`.

**Required equation, figure, or table:** None.

**Opening premise:** Fitting is not the endpoint; a proposed explanation must be confronted with the whole measurement and revised when its residual structure or physical interpretation is inadequate.

**Paragraph plan:** (1) simultaneous/global strategy; (2) specified-mechanism/target strategy; (3) two meanings of model; (4) iterative cycle and validation criteria; (5) why reusable computational building blocks matter.

**Exit point or bridge:** This recurring scientific cycle explains why successive software generations separated computation, interaction, and extensibility differently.

### 1.3 Lineage of responsibilities

**Section purpose:** Supply only the history needed to understand the current architectural boundary.

**Claims uniquely owned here:** TIMP was the R computational environment; Glotaran was a Java GUI using TIMP through Rserve; pyglotaran rewrote the computational core in Python; notebooks and the Python ecosystem surround rather than reside inside the core.

**Definitions introduced here:** Rserve in one clause; notebook-centered workflow.

**Prior concepts this section may assume:** Scientific cycle and separable analysis.

**Material explicitly deferred elsewhere:** Current class graph and plugin system.

**Required evidence namespace:** `FR-*`.

**Required equation, figure, or table:** Figure 1, responsibility-lineage diagram.

**Opening premise:** The lineage is best understood by following which system owned computation and which supplied the working environment.

**Paragraph plan:** (1) TIMP responsibility; (2) Glotaran/TIMP boundary through Rserve; (3) Python rewrite and avoidance of “binding” language; (4) notebook/ecosystem shift and its limits; (5) transition from history to present design drivers.

**Exit point or bridge:** The current architecture can now be examined as a response to the recurring need to compose, estimate, inspect, and revise scientific models.

## 2. Separating scientific definitions from execution — Packet B, 2,200–2,700 words

### 2.1 Why divide the package into responsibilities?

**Section purpose:** Motivate the partitions before naming current classes.

**Claims uniquely owned here:** Reuse of scientific contributions, inspectable declarative specifications, joint experiments, separate treatment of unknowns, labeled data, rich results, and registered extensions are verified architectural drivers or interpretations; core, numerical libraries, notebooks, examples, and extras have distinct responsibilities.

**Definitions introduced here:** declarative specification; responsibility boundary; invariant, only if needed and immediately explained.

**Prior concepts this section may assume:** Scientific model-discovery cycle and lineage.

**Material explicitly deferred elsewhere:** Detailed unknowns to Section 3; estimator mechanics to Section 4; result fields to Section 5; plugin mechanics to Section 6.

**Required evidence namespace:** `AR-*`.

**Required equation, figure, or table:** Table 1 may be introduced late in Section 2 after terms have prose definitions.

**Opening premise:** A researcher needs to change a scientific hypothesis without rebuilding data loading, optimization, and result inspection for every new contribution.

**Paragraph plan:** (1) composition problem; (2) declarations versus changing runtime values; (3) reuse across datasets/experiments; (4) common element-to-matrix boundary; (5) core/ecosystem boundary; (6) benefits and coordination costs as transition.

**Exit point or bridge:** These motivations become concrete in the network of owned objects and named references rooted at the analysis specification.

### 2.2 A network of connected scientific definitions

**Section purpose:** Give the static object graph in concept-first order.

**Claims uniquely owned here:** A `Scheme` contains experiments and a model library; a model library owns named element definitions; an experiment owns dataset specifications; a data model references elements and a data source/configuration; measured arrays and parameter values enter separately; serialization is one representation rather than the architecture itself.

**Definitions introduced here:** analysis specification; Scheme; model library; Experiment; DataModel; Element; object graph; ownership versus named reference versus runtime input.

**Prior concepts this section may assume:** Declarative specification and scientific contribution.

**Material explicitly deferred elsewhere:** xarray data mechanics and parameter categories to Section 3; numerical matrices to Section 4.

**Required evidence namespace:** `AR-*`.

**Required equation, figure, or table:** Figure 3 and Table 2, “Core entities and responsibilities.”

**Opening premise:** Before a fit can be run, the package needs a coherent description of what is shared, what belongs to one experiment or dataset, and which scientific contributions each dataset uses.

**Paragraph plan:** (1) graph idea and serialized representations; (2) Scheme root; (3) reusable library; (4) experiment joint-analysis boundary; (5) per-dataset DataModel, explicitly not measured data; (6) Element contribution and heterogeneity; (7) separately supplied arrays and Parameters; (8) walk the figure edges; (9) Table 2 synthesis and static invariants.

**Exit point or bridge:** Names preserve reuse and compactness, but execution requires each name to be connected to the typed object or parameter it denotes.

### 2.3 Connecting names and checking meaning

**Section purpose:** Explain semantic resolution without a compiler metaphor.

**Claims uniquely owned here:** Serialized/programmatic input creates typed objects; element types can contribute DataModel subtypes; library extension chains and named item/parameter references are resolved; relevant missing/cyclic references and model issues are checked; referenced explicit parameters are selected; a resolved graph is still a specification, not a fixed matrix.

**Definitions introduced here:** typed instantiation; reference resolution/binding; element extension versus Python inheritance; validation issue.

**Prior concepts this section may assume:** All static entities and edge types.

**Material explicitly deferred elsewhere:** Data orientation and linking to Section 3; per-evaluation matrices to Section 4; lifecycle ordering details to Section 5.

**Required evidence namespace:** `AR-*`.

**Required equation, figure, or table:** Table 1, “Terminology concordance,” after prose definitions; no equation.

**Opening premise:** Human-readable labels are useful only if the runtime can connect each one unambiguously and report incoherent relationships.

**Paragraph plan:** (1) typed instantiation; (2) plugin-contributed typing without plugin mechanics; (3) library extension resolution and cycle detection; (4) element/data-model/item references; (5) explicit-parameter references and subset; (6) issue validation boundaries and non-universal wording; (7) why resolution is not compilation; (8) Table 1 as concordance.

**Exit point or bridge:** Once meanings are connected, the next boundary translates labeled observations and two distinct kinds of unknowns into numerical roles.

## 3. Giving observations and unknowns numerical roles — Packet C, 1,300–1,700 words

### 3.1 Measured arrays are not data models

**Section purpose:** Explain how labeled measured values become organized inputs while preserving the DataModel/data distinction.

**Claims uniquely owned here:** Measured values use labeled arrays and coordinates; DataModel supplies per-dataset scientific configuration and source association; model/global roles may be inferred or declared; orientation/slicing prepares numerical axes; weights and scales modify the contribution as verified.

**Definitions introduced here:** xarray in ordinary language; coordinate and dimension label; model dimension; global dimension; orientation; weight; scale.

**Prior concepts this section may assume:** DataModel, experiment, measured runtime input.

**Material explicitly deferred elsewhere:** Matrix equation and residual weighting formalism to Section 4.

**Required evidence namespace:** `DP-*`.

**Required equation, figure, or table:** No displayed equation; a compact orientation example is allowed.

**Opening premise:** A table of numbers becomes scientifically interpretable only when the package knows which coordinate each axis represents and how the per-dataset specification relates to it.

**Paragraph plan:** (1) labeled observations; (2) DataModel versus array; (3) model/global coordinate roles with running-example qualification; (4) inference/declaration and orientation; (5) slicing and numerical wrappers; (6) verified weight behavior; (7) verified scale behavior.

**Exit point or bridge:** One experiment may contain several such arrays, requiring alignment before their shared structure can be estimated.

### 3.2 Joint organization across datasets

**Section purpose:** Explain multi-dataset coordination without projecting TIMP's old hierarchy onto staging.

**Claims uniquely owned here:** Experiments can coordinate multiple dataset specifications; supported linking/alignment works across global coordinates with configured method/tolerance; single and linked numerical representations differ; shared and dataset-specific quantities must be described only as current code supports.

**Definitions introduced here:** alignment; linking; tolerance; numerical block.

**Prior concepts this section may assume:** Experiment, model/global dimensions, oriented arrays.

**Material explicitly deferred elsewhere:** Exact estimator loop to Section 4; lifecycle timing to Section 5.

**Required evidence namespace:** `DP-*`.

**Required equation, figure, or table:** Optional compact textual block illustration only if verified; Figure 4 remains Packet D's.

**Opening premise:** Measurements collected under related conditions can constrain one analysis only after their comparable coordinates and intended shared structure are made explicit.

**Paragraph plan:** (1) scientific reason for joint data; (2) experiment grouping; (3) global-coordinate alignment/linking; (4) tolerance/method semantics; (5) single versus linked wrapper; (6) limitations and bridge to unknowns.

**Exit point or bridge:** Coordinated data still leave two computationally different sets of quantities to estimate.

### 3.3 Explicit parameters and conditionally linear coefficients

**Section purpose:** Make the central categorical distinction before estimator mathematics.

**Claims uniquely owned here:** `Parameters` holds named explicit parameters with value/metadata; free outer entries differ from fixed or expression-defined entries; bounds and supported nonnegative metadata influence the outer problem; CLPs are separate coefficients labeled through matrices and estimated internally; “outer” is safer than calling every explicit parameter nonlinear.

**Definitions introduced here:** explicit parameter; free, fixed, bounded, nonnegative, expression-defined; outer parameter; CLP.

**Prior concepts this section may assume:** Scientific contribution shapes and per-dataset data organization.

**Material explicitly deferred elsewhere:** Inner/outer objective equations, variable projection, NNLS, relations, penalties, and uncertainty to Section 4.

**Required evidence namespace:** `DP-*`.

**Required equation, figure, or table:** No displayed equation. A two-column conceptual contrast is allowed only if it does not duplicate Table 3.

**Opening premise:** Some quantities change the shapes calculated by the scientific model, while other coefficients can be solved once those shapes are known.

**Paragraph plan:** (1) shape-changing versus amplitude intuition; (2) explicit Parameter/Parameters role; (3) free/fixed/expression-defined status; (4) bounds/nonnegative qualification; (5) CLP role and separate storage; (6) why computational category is not intrinsic scientific ontology; (7) concrete running-example mapping.

**Exit point or bridge:** This separation raises the mathematical question answered next: how can the inner coefficient solve be nested inside the outer update of explicit parameters?

## 4. Exploiting conditional linearity during estimation — Packet D, 1,500–2,000 words

### 4.1 From two contributions to a matrix model

**Section purpose:** Move from the established physical example to formal separability with all notation explained.

**Claims uniquely owned here:** Element contributions yield labeled matrix columns; compatible contributions are composed and transformed; the oriented observation can be expressed as \(\mathbf{Y}_q=\mathbf{M}_q(\boldsymbol{\theta})\mathbf{B}_q+\boldsymbol{\varepsilon}_q\) under the model assumptions.

**Definitions introduced here:** matrix row/column meanings; separable model; CLP axis/column labels; effective matrix column.

**Prior concepts this section may assume:** Running example, dimensions, explicit parameter/CLP distinction.

**Material explicitly deferred elsewhere:** Runtime phase ordering to Section 5.

**Required evidence namespace:** `NM-*`.

**Required equation, figure, or table:** Scalar two-component equation and general matrix equation from the contract.

**Opening premise:** Once the temporal shapes are fixed by explicit parameters, estimating their wavelength-dependent amplitudes is a linear combination problem.

**Paragraph plan:** (1) recall two contributions in words; (2) scalar equation and symbols; (3) stack values into \(\mathbf{Y}\); (4) define \(\mathbf{M}\) dimensions/physical role; (5) define \(\mathbf{B}\) dimensions/physical role; (6) element matrix composition and label transformations; (7) noise/model mismatch and assumption limits.

**Exit point or bridge:** Conditional linearity allows the coefficients to be estimated inside each trial of the explicit outer parameters.

### 4.2 Inner coefficient estimation

**Section purpose:** Explain the inner problem, supported estimators, and verified transformation stages.

**Claims uniquely owned here:** The runtime estimates CLPs after constructing matrices for a trial parameter set; variable projection eliminates fitted CLPs from the outer variable vector; supported NNLS imposes nonnegativity in the inner solve; relations/constraints and matrix reduction occur at verified stages; weights/scales influence residual formation as verified.

**Definitions introduced here:** arg min; constraint set; weighted residual; Frobenius norm; variable projection; non-negative least squares (NNLS); CLP relation and constraint.

**Prior concepts this section may assume:** Matrix model and parameter distinction.

**Material explicitly deferred elsewhere:** Detailed result storage to Section 5.

**Required evidence namespace:** `NM-*`.

**Required equation, figure, or table:** Canonical inner equation; Figure 4 begins here.

**Opening premise:** For one trial set of explicit parameters, the package can ask which coefficient values make the calculated surface closest to the observations.

**Paragraph plan:** (1) inner question in words; (2) arg-min and mismatch explanation; (3) equation with dimensions; (4) weighting operation and scale placement from source; (5) constraint set limited to supported paths; (6) variable-projection interpretation; (7) NNLS alternative; (8) relations/constraints and label/matrix reductions; (9) scientific meaning.

**Exit point or bridge:** The remaining mismatch becomes the evidence used to update the explicit outer parameters.

### 4.3 Outer least squares, penalties, and uncertainty

**Section purpose:** Close the nested loop and map the mathematics to implementation without overstating statistical guarantees.

**Claims uniquely owned here:** Free explicit parameters form the outer vector; objective contributions and penalty residuals are concatenated for SciPy least squares; parameter-dependent matrices are recalculated per evaluation; supported degrees of freedom, covariance, standard errors, and histories are calculated after or during optimization as verified.

**Definitions introduced here:** Euclidean norm; concatenation; penalty residual; least-squares iteration; covariance/standard error/degrees of freedom in restrained terms.

**Prior concepts this section may assume:** Inner estimate and residual.

**Material explicitly deferred elsewhere:** Full lifecycle and result-field inventory to Section 5.

**Required evidence namespace:** `NM-*`.

**Required equation, figure, or table:** Canonical outer explanatory objective; complete Figure 4; Table 3, “Mathematics-to-code concordance.”

**Opening premise:** A poor inner fit indicates that the current shape-producing explicit parameters should be changed, subject to their outer constraints and any appended penalties.

**Paragraph plan:** (1) outer loop in words; (2) outer equation and symbol definitions; (3) residual concatenation across objectives; (4) penalty residual implementation nuance; (5) recalculation versus initialized structures; (6) termination/optimizer output without convergence promises; (7) uncertainty and degrees-of-freedom qualifications; (8) Table 3 mapping and figure walkthrough.

**Exit point or bridge:** The equations describe one evaluation; the next section places repeated evaluations within the complete route from specification to inspectable result.

## 5. From a resolved specification to evidence for validation — Packet E, 1,300–1,700 words

### 5.1 The runtime lifecycle

**Section purpose:** Turn static and mathematical views into a verified temporal sequence.

**Claims uniquely owned here:** Exact ordering from `Scheme.optimize(...)` through data association/loading, resolution/validation, objective initialization, repeated parameter/matrix/CLP/residual evaluation, SciPy optimization, statistics, and result construction; one-time and repeated work are distinct.

**Definitions introduced here:** lifecycle; initialization; objective evaluation; post-processing.

**Prior concepts this section may assume:** Static graph, semantic resolution, nested estimation.

**Material explicitly deferred elsewhere:** No rederivation of equations; extension registration to Section 6.

**Required evidence namespace:** `RR-*`.

**Required equation, figure, or table:** Figure 5, lifecycle with phase boundaries.

**Opening premise:** The same objects play different roles before iteration, during each trial, and after the optimizer stops.

**Paragraph plan:** (1) inputs at `Scheme.optimize`; (2) data paths/association ordering; (3) resolution and issue validation; (4) objective/numerical wrapper initialization; (5) free vector and optimizer configuration; (6) repeated evaluation sequence; (7) concatenation/iteration; (8) final statistics and result construction; (9) figure walkthrough and caveats.

**Exit point or bridge:** The lifecycle matters scientifically because the package returns more than the final outer vector.

### 5.2 Results, provenance, persistence, and validation

**Section purpose:** Explain how rich result structures support the next model-discovery cycle.

**Claims uniquely owned here:** Verified top-level and per-experiment result contents; fitted data, residuals, CLPs, decompositions, dimensions, scales, metrics, optimization diagnostics, histories, version/source metadata, and element-specific results only where fields exist; persistence preserves verified source relationships; plotting is outside core.

**Definitions introduced here:** result provenance; fit decomposition; persistence/serialization; validation evidence.

**Prior concepts this section may assume:** Residuals, CLPs, explicit parameters, lifecycle.

**Material explicitly deferred elsewhere:** Scientific definition of validation is owned by Section 1; ecosystem plotting detail to Section 6.

**Required evidence namespace:** `RR-*`.

**Required equation, figure, or table:** No new equation or table.

**Opening premise:** A parameter vector alone cannot show where the fit fails or whether the fitted contributions make physical sense.

**Paragraph plan:** (1) top-level Result and initial/optimized parameters; (2) per-experiment arrays and metrics; (3) CLPs and decompositions; (4) optimizer diagnostics/uncertainties/history with field-level caution; (5) element results and identity; (6) source paths, versions, serialization; (7) how these data enable but do not automate validation; (8) core versus extras visualization boundary.

**Exit point or bridge:** Reusable result construction depends on the same common contracts that permit scientific and I/O capabilities to be extended.

## 6. Extending the framework and evaluating its trade-offs — Packet F, 1,000–1,400 words

### 6.1 Registered extension surfaces

**Section purpose:** Explain extension mechanisms to a reader without Python packaging knowledge.

**Claims uniquely owned here:** Element, data-I/O, and project-I/O extensions use distinct registries/interfaces; entry points enable discovery; short/fully qualified names, conflict behavior, and pinning are described only if tests confirm them; element plugins may contribute typed DataModel capability; schemas reflect registered types as verified.

**Definitions introduced here:** registry as a directory of available implementations; entry point as installation metadata used for discovery; fully qualified name; pinning; dynamic schema.

**Prior concepts this section may assume:** Element/DataModel common contracts and typed instantiation.

**Material explicitly deferred elsewhere:** No repetition of static graph or result inventory.

**Required evidence namespace:** `EX-*`.

**Required equation, figure, or table:** Figure 6 and Table 4, “Extension surfaces.”

**Opening premise:** A common optimizer is useful only if new scientific contributions and file formats can enter through explicit boundaries.

**Paragraph plan:** (1) extension problem; (2) registry/entry-point explanation; (3) element contract and DataModel subtype contribution; (4) data-I/O interface; (5) project-I/O interface; (6) verified naming/conflict/pinning; (7) dynamic schema exposure; (8) Table 4 and figure walkthrough.

**Exit point or bridge:** Extensions still rely on core numerical mechanisms rather than bringing a new optimizer for every contribution.

### 6.2 Simulation and the surrounding scientific ecosystem

**Section purpose:** Locate reuse and external tools without turning the prose into a dependency list.

**Claims uniquely owned here:** Simulation reuses verified resolution/matrix mechanisms; numerical libraries supply labeled arrays and solvers; notebooks coordinate work externally; examples demonstrate composition; extras supplies plotting and higher-level exploration.

**Definitions introduced here:** simulation as generating calculated data from a specified model/parameters/CLPs; ecosystem.

**Prior concepts this section may assume:** Numerical realization and extension boundaries.

**Material explicitly deferred elsewhere:** No new optimizer mathematics.

**Required evidence namespace:** `EX-*`.

**Required equation, figure, or table:** Figure 6 includes ecosystem boundary; no equation.

**Opening premise:** The same scientific definitions can be useful before fitting, when generating expected observations, and after fitting, when inspecting them with external tools.

**Paragraph plan:** (1) simulation responsibility and reuse; (2) xarray/NumPy/SciPy/Numba roles at supported level; (3) notebook role; (4) examples role; (5) extras/plotting role; (6) boundary qualification.

**Exit point or bridge:** These boundaries enable reuse, but none is free of coordination cost.

### 6.3 Verified trade-offs

**Section purpose:** Evaluate rather than advertise the architecture, while reserving the final synthesis for the coordinator.

**Claims uniquely owned here:** At least four paired benefits/costs supported by earlier evidence: declarative reuse versus resolution/validation; plugin typing versus schema/name complexity; outer/CLP separation versus model exposure requirements; labeled arrays versus inference/orientation/alignment; rich results versus structural complexity; notebook flexibility versus absence of dedicated-GUI affordances.

**Definitions introduced here:** trade-off.

**Prior concepts this section may assume:** Entire preceding chapter.

**Material explicitly deferred elsewhere:** Final thesis judgment and conclusion.

**Required evidence namespace:** `EX-*` plus cross-references to prior ledger IDs.

**Required equation, figure, or table:** No new figure/table.

**Opening premise:** Separating responsibilities controls one kind of complexity by making other coordination work explicit.

**Paragraph plan:** (1) declarative graph pair; (2) plugin typing pair; (3) nested-estimation pair; (4) labeled-array pair; (5) rich-results pair; (6) notebook-workflow pair, qualified as workflow interpretation; (7) transition to synthesis.

**Exit point or bridge:** The conclusion must decide whether the separations, taken together, support the model-discovery cycle claimed at the outset.

## 7. Conclusion — coordinator, 450–600 words

**Section purpose:** Revisit the thesis using only established evidence and explain how the architecture embodies specification, estimation, validation, and revision.

**Claims uniquely owned here:** Integrated evaluation of the central thesis; no new facts.

**Definitions introduced here:** None.

**Prior concepts this section may assume:** Entire chapter.

**Material explicitly deferred elsewhere:** None.

**Required evidence namespace:** Existing packet claims only; no unsupported synthesis.

**Required equation, figure, or table:** None.

**Opening premise:** The architecture is best judged by whether a researcher can move between a scientific question and a traceable numerical analysis without coupling every model contribution to a bespoke workflow.

**Paragraph plan:** (1) return to measured surface and inverse problem; (2) summarize declarative separations; (3) summarize nested estimation and lifecycle; (4) summarize results/extensions; (5) qualify benefits with verified costs; (6) final judgment tied to iterative model discovery and staging scope.

**Exit point or bridge:** End with the scientific cycle, not a feature slogan or v1 prediction.

## References — coordinator

Consolidate only works cited. Minimum expected primary references are Mullen and van Stokkum (2007), Snellenburg et al. (2012), van Stokkum et al. (2004), and van Stokkum et al. (2023). Verify title-page metadata and DOI strings. The lecture notes may appear only when they supply material not adequately supported by the 2004 review and must be identified appropriately.

## Artifact assignment ledger

| Artifact | Sole owner | Consumed by |
|---|---|---|
| `00-editorial-contract.md` | coordinator | all packets/reviewers |
| `00-chapter-skeleton.md` | coordinator | all packets/reviewers |
| Section/evidence 01; Figures 1–2 | Packet A–B owner | coordinator |
| Section/evidence 02; Figure 3; Tables 1–2 | Packet A–B owner | coordinator |
| Section/evidence 03 | Packet C–D owner | coordinator |
| Section/evidence 04; Figure 4; Table 3 | Packet C–D owner | coordinator |
| Section/evidence 05; Figure 5 | Packet E–F owner | coordinator |
| Section/evidence 06; Figure 6; Table 4 | Packet E–F owner | coordinator |
| integrated chapter, merged ledger, final review notes | coordinator | reviewers/user |
| architecture/mathematics review | assigned review-only agent | coordinator |
| runtime/evidence review | assigned review-only agent | coordinator |
| readability/style/APA review | assigned review-only agent | coordinator |

Gate 0 is frozen. Packet authors must read both `00-` files completely before gathering evidence or drafting.
