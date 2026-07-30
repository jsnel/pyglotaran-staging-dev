# Frozen editorial contract: pyglotaran architecture chapter

**Status:** Gate 0 frozen for parallel drafting on 2026-07-30. Packet authors must not edit this file. Proposed changes belong in each packet's integration note and are decided by the coordinating editor.

## 1. Inspected workspace and authority

The draft describes the staging implementation inspected at these exact revisions:

| Repository | Revision | Branch or state | Working tree |
|---|---|---|---|
| workspace superproject | `f1516d19e1680699c6c6e502e523e51bc9d0cc59` | `main`, three commits ahead of `origin/main` | clean at bootstrap |
| `pyglotaran` | `468c4cd57aaf25c10edf85cd197df771bad0a766` | detached submodule HEAD; package declares `0.8.0.dev0` | clean at bootstrap |
| `pyglotaran-examples` | `7f7fd227bcfb74308523d2242ca811a68ba25214` | detached submodule HEAD | clean at bootstrap |
| `pyglotaran-extras` | `d57940be02751c670ee90f3bc09af7cd954a1d08` | `staging_support` | clean at bootstrap |

The superproject and submodules are read-only evidence for this commission. Existing and subsequent non-documentation changes belong to the user and must be preserved. No agent may reset, clean, reformat, or otherwise alter source repositories.

For present architecture and runtime behavior, evidence authority descends in this order:

1. current source under `pyglotaran/glotaran/`;
2. focused current tests under `pyglotaran/tests/`;
3. staging-compatible material in `pyglotaran-examples/` and the explicitly named local examples;
4. the supplied papers in `Literature/` for scientific definitions and history;
5. documentation and docstrings after verification against source;
6. an explicitly qualified architectural interpretation supported by more than one observation.

Current source contains transitional docstrings mentioning “dataset group” and “megacomplex.” Those strings do not override the implemented `ExperimentModel`, `Element`, `elements`, and `global_elements` vocabulary. They may be noted as stale documentation evidence but must not become current chapter terminology.

Every consequential claim must be classified as an **implemented fact**, **scientific definition**, **historical fact**, **architectural interpretation**, or **maintainer intent**. Maintainer intent is admissible only when directly supplied. Evidence ledgers use:

| Claim ID | Proposed claim | Class | Primary evidence | Corroborating evidence | Confidence | Safe wording | Draft location |
|---|---|---|---|---|---|---|---|

Exact source anchors include repository-relative paths plus symbols or line ranges where practical. Tests corroborate behavior; examples establish intended composition at the user boundary but do not prove internals. Unresolved facts are written as `[VERIFY: precise question and likely source]`, never guessed.

## 2. Commission, thesis, scope, and reader

The deliverable is a self-contained, architecture-first MSc/PhD-thesis-level chapter of approximately 8,000–10,000 words, excluding references. That range is a soft target. Accuracy, explanation, and argumentative continuity take priority; repeated setup, low-value API catalogs, and implementation trivia are removed before useful scientific explanation.

The intended reader is a mathematics, physics, or other science student at bachelor level who knows basic algebra, graphs, matrices, and ordinary curve fitting, but need not know spectroscopy, global or target analysis, separable least squares, variable projection, Python, or pyglotaran.

The working thesis is:

> Pyglotaran lets a researcher describe a scientific analysis using named, reusable building blocks. It connects these definitions to measured data and explicit parameter values, constructs and solves a nested fitting problem, and returns detailed results that support inspection and scientific validation. Separating declarative structure, observations, two computational kinds of unknowns, numerical realization, results, and extension boundaries allows common numerical machinery to serve heterogeneous scientific models, although each separation introduces coordination costs.

Each major section must support, qualify, or expose a trade-off in this thesis. The chapter describes responsibilities, information flow, invariants, and extension boundaries in the inspected staging implementation. It does not promise v1 names, compatibility, stability, performance, or a roadmap. It is not a YAML tutorial, API catalog, package-directory tour, performance study, or guide to plotting.

Core pyglotaran owns typed analysis specifications, explicit parameter handling, semantic resolution, numerical realization, optimization, simulation, results, and extension registries. NumPy, SciPy, xarray, and related libraries supply numerical and labeled-array foundations. Jupyter is an external scientific working environment, not an optimizer component. `pyglotaran-examples` demonstrates analyses. Plotting and higher-level exploration primarily belong to `pyglotaran-extras`.

## 3. Binding terminology

The following meanings are canonical throughout the working artifacts and assembled chapter.

- **Physicochemical model:** a scientific hypothesis about states, species, kinetics, spectra, instrument effects, and related physical structure.
- **Model for the observations:** the physicochemical assumptions together with measurement assumptions, data organization, scaling, weighting, and stochastic residual description used to predict measured values. It spans several software objects.
- **Analysis specification:** the declarative network of experiments and reusable scientific definitions rooted in a `Scheme`. Measured arrays and explicit parameter values enter optimization separately.
- **Scheme:** the declarative orchestration root containing experiments and a model library. It is not a container for all measured arrays or current parameter values.
- **Model library:** named reusable `Element` definitions and extension relationships represented by `ModelLibrary`.
- **Element:** a composable scientific contribution implementing the common matrix-related contract and, where relevant, constraints and element-specific results. Never use the old software term *megacomplex* for this role.
- **Experiment:** the joint-analysis grouping represented by `ExperimentModel`, containing one or more dataset specifications. Never use *dataset group* as current terminology.
- **Data model:** a per-dataset scientific specification represented by `DataModel` or an element-contributed subtype. It connects a data source to elements, optional global elements, dimensions, scales, weights, and other typed configuration. It is not measured xarray data.
- **Measured data:** labeled numerical observations and coordinates, usually represented by an `xarray.DataArray`, supplied or loaded separately.
- **Explicit parameter:** a named serialized `Parameter` held in `Parameters`, with value and metadata such as variation status, bounds, expression, and uncertainty information. A free explicit parameter is an **outer parameter** computationally. Do not call every explicit parameter intrinsically nonlinear.
- **Conditionally linear parameter (CLP):** a coefficient estimated in an inner linear or constrained-linear problem after explicit parameters determine a matrix. CLPs are represented through labels, estimators, decompositions, and results; they are never entries in `Parameters`.
- **Reference resolution** or **binding:** connecting a name to the element, data model, or explicit parameter it denotes, resolving extension relationships, and checking relevant missing or cyclic references.
- **Semantic resolution and validation:** typed instantiation, name/reference resolution, parameter selection, and issue checking. There is no model compiler.
- **Numerical realization:** orienting data and constructing or transforming optimization data, matrices, linked blocks, relations, constraints, scales, weighted residuals, and penalties. Some numerical structures are initialized once; parameter-dependent matrices are recalculated during objective evaluation.
- **Model dimension:** the coordinate along which a model matrix is evaluated. It is time in the running example, not universally.
- **Global dimension:** the coordinate across which CLP contributions are organized or estimated. It is wavelength in the running example, not universally.
- **Global analysis:** simultaneous scientific analysis under shared model structure. It is a method, not an axis and not a synonym for global dimension.
- **Target analysis:** estimation or testing of a specified physicochemical model intended to yield physically interpretable states, species, or spectra. It is composition of scientific structure, not a separate optimizer mode.
- **Residual:** the difference between measured and calculated values after applicable scaling and weighting conventions.
- **Provenance:** information recording where a result came from, including resolved configuration, source paths, versions, input relationships, and element identity to the extent actually stored.
- **Plugin:** a registered extension of element types, data I/O, or project I/O discovered through the corresponding registry and entry-point mechanism. There is no single undifferentiated plugin API.

Preferred process verbs are *instantiate*, *resolve*, *bind*, *validate*, *construct*, *realize*, *calculate*, *estimate*, *evaluate*, and *serialize*. The words *compile*, *compiler*, *intermediate representation*, and *code generation* are forbidden for the current analysis path.

## 4. Frozen running example and notation

The recurring example is a pump–probe-style time- and wavelength-resolved spectroscopy experiment. A short excitation initiates change in a sample. At sampled delays \(t_i\), indexed by \(i=1,\ldots,n_t\), the instrument records a signal at wavelengths \(\lambda_j\), indexed by \(j=1,\ldots,n_\lambda\). The resulting measured surface is

\[
\mathbf{Y}\in\mathbb{R}^{n_t\times n_\lambda},
\]

with time along rows and wavelength along columns for explanatory purposes. In this example only, time plays the model-dimension role and wavelength the global-dimension role. The software can use other physical coordinates and can orient data at the numerical boundary.

Use two contributions for the first intuition: temporal profiles \(c_1(t;\boldsymbol{\theta})\) and \(c_2(t;\boldsymbol{\theta})\), with wavelength-dependent amplitudes or spectra \(s_1(\lambda)\) and \(s_2(\lambda)\). At one coordinate pair,

\[
y(t_i,\lambda_j)\approx
c_1(t_i;\boldsymbol{\theta})s_1(\lambda_j)
+c_2(t_i;\boldsymbol{\theta})s_2(\lambda_j)
+\varepsilon_{ij}.
\]

Packet A may introduce this idea in words and the separable-observation figure, but Packet D owns the formal equations. Packet C may name the two kinds of unknowns without deriving their estimators.

For dataset or objective unit \(q\), the canonical matrix model is

\[
\mathbf{Y}_q =
\mathbf{M}_q(\boldsymbol{\theta})\mathbf{B}_q
+\boldsymbol{\varepsilon}_q.
\]

Here \(\mathbf{Y}_q\in\mathbb{R}^{n_{m,q}\times n_{g,q}}\) is an oriented measured array, \(\mathbf{M}_q(\boldsymbol{\theta})\in\mathbb{R}^{n_{m,q}\times k_q}\) is the composed element matrix evaluated at explicit outer parameters \(\boldsymbol{\theta}\), and \(\mathbf{B}_q\in\mathbb{R}^{k_q\times n_{g,q}}\) contains CLPs. For the running example, \(n_m=n_t\), \(n_g=n_\lambda\), rows of \(\mathbf{M}\) follow delay time, and each row of \(\mathbf{B}\) is an associated spectrum. \(k_q\) is the number of effective labeled matrix columns after supported composition and transformations; do not claim one universal orientation for every internal element contribution.

The inner problem is expressed with a general weighting operation \(\mathcal{W}_q\), avoiding an unsupported claim that all weights are one matrix multiplication:

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

\(\mathcal{C}_q\) denotes only constraints actually supported by the chosen estimator and matrix-reduction path. The outer explanatory objective is

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

\(\Theta\) contains applicable explicit-parameter bounds and expression/fixed-parameter consequences; \(\mathbf{r}_q\) is the residual contribution consumed by the outer least-squares routine; and \(\mathbf{p}\) represents penalty residuals. The prose must state that the implementation can append penalties as residual-vector entries rather than constructing the displayed scalar sum as a separate object.

Notation ownership is frozen:

| Symbol | Meaning | Canonical owner |
|---|---|---|
| \(t_i,\lambda_j,y,\varepsilon_{ij}\) | running measurement coordinates, observed scalar, unexplained component | Packet A introduces in prose/figure; Packet D formalizes |
| \(q,n_m,n_g,k\) | objective or dataset unit and array sizes | Packet D |
| \(\mathbf{Y},\mathbf{M},\mathbf{B}\) | observations, composed matrix, CLPs | Packet D |
| \(\boldsymbol{\theta},\Theta\) | free explicit outer parameters and feasible domain | Packet C defines parameter category; Packet D uses formally |
| \(\mathcal{W},\mathcal{C}\) | weighting operation and supported inner constraint set | Packet D |
| \(\mathbf{r},\mathbf{p}\) | residual and penalty-residual vectors | Packet D |
| fitted arrays, decompositions, covariance, histories | result quantities, with fields only when verified | Packet E |

Every equation must have a plain-language lead-in, definitions and dimensions for all new symbols, a physical interpretation afterward, and a mapping to current runtime responsibilities. Define *arg min*, Frobenius norm, Euclidean norm, constraint set, weighting, and variable projection before relying on the notation.

## 5. Expository and APA style

Use a neutral academic voice. Begin each section from the scientific or architectural question it answers, then proceed in this order where applicable:

1. physical or experimental question;
2. observable data and the difficulty;
3. mathematical abstraction;
4. software responsibility;
5. current implementation anchor.

Explain an ordinary idea before its formal name or Python class. Introduce “a network of named definitions and references” before *object graph*, “connecting a name to what it denotes” before *reference resolution*, “building the numerical fitting problem” before *numerical realization*, and “information recording where a result came from” before *provenance*.

Use one principal claim per paragraph, restrained verbs, and conditional language such as *can*, *commonly*, *under these assumptions*, and *in the inspected implementation*. Avoid promotional adjectives, dense noun phrases, unexplained acronyms, and universal claims. A fit supplies evidence for scientific interpretation; it does not prove a mechanism or automatically establish identifiability.

Every section opens with a premise and closes with a bridge to the next question. Concepts are fully defined once by their owner. Adjacent sections use a one-sentence reminder and cross-reference, not a second definition. Class names appear as current implementation anchors, not in headings and not as the organizing principle.

Use APA author–date citations. Paraphrase rather than quote. Parenthetical examples are `(van Stokkum et al., 2004)`, `(Mullen & van Stokkum, 2007)`, `(Snellenburg et al., 2012)`, and `(van Stokkum et al., 2023)`. Apply sentence case to article titles, preserve author diacritics and lowercase “van,” italicize journal and volume in the reference list, and present DOIs as HTTPS URLs. Verify metadata against PDF title pages or DOI records. The 2023 paper is evidence for scientific framing and v0.7-era history, not authority for staging class names.

The historical lineage is binding:

- TIMP was the R computational and mathematical environment/core.
- Glotaran was a Java graphical front end that used TIMP through Rserve.
- Pyglotaran was a complete Python rewrite of the Glotaran/TIMP computational core.
- The desktop GUI was not recreated as part of the core; notebook-centered work and the Python ecosystem became the surrounding scientific workflow.

Do not reproduce or closely imitate paper figures or distinctive phrasing. All diagrams are original abstractions of inspected evidence. Mermaid captions must state the view and define arrow meanings; diagrams may not rely on color.

## 6. Exclusive ownership and packet interfaces

Only the coordinating editor edits this contract, `00-chapter-skeleton.md`, the assembled chapter, the merged ledger, the final review notes, and the consolidated reference list.

| Owner | Exclusive section/evidence files | Exclusive figures/tables | Evidence prefix |
|---|---|---|---|
| Packet owner A–B | `sections/01-scientific-framing-and-lineage.md`, `evidence/01-framing-ledger.md`, `sections/02-declarative-architecture.md`, `evidence/02-architecture-ledger.md` | Figures 1–3; Tables 1–2 embedded in Section 2 | `FR-*`, `AR-*` |
| Packet owner C–D | `sections/03-data-and-parameters.md`, `evidence/03-data-parameters-ledger.md`, `sections/04-numerical-estimation.md`, `evidence/04-numerical-ledger.md` | Figure 4; Table 3 embedded in Section 4 | `DP-*`, `NM-*` |
| Packet owner E–F | `sections/05-runtime-results-and-provenance.md`, `evidence/05-runtime-results-ledger.md`, `sections/06-extensions-and-evaluation.md`, `evidence/06-extensions-ledger.md` | Figures 5–6; Table 4 embedded in Section 6 | `RR-*`, `EX-*` |
| Coordinating editor | integrated synopsis, transitions, conclusion, references, final three deliverables | final numbering/captions and any integration-only table edits | `ED-*` |

Packet A owns the beginner scientific primer, global/target definitions, iterative model-discovery cycle, and lineage. It exits after establishing separable contributions as the problem structure. Packet B owns architectural drivers, core/ecosystem boundary, static object graph, typed instantiation, reference and extension resolution, and validation-before-numerics. It defers labeled numerical handling and all estimator mathematics.

Packet C owns measured-data versus data-model handling, dimensions, orientation, weights, scales, alignment/linking, and the categorical distinction between explicit parameters and CLPs. It exits by asking how the two unknown kinds are exploited computationally. Packet D owns all displayed estimation equations, matrix/CLP labels, inner estimators, outer least squares, relations/constraints placement, residual and penalty assembly, and the mathematics-to-code concordance. It does not repeat parameter metadata.

Packet E owns temporal ordering from `Scheme.optimize(...)` to `Result`, the boundary between one-time initialization and repeated evaluation, result structure, validation support, persistence, and provenance. It uses but does not rederive Packet D's mathematics. Packet F owns registries, element/data-I/O/project-I/O extension contracts, schema exposure, simulation reuse, ecosystem boundaries, and paired trade-offs. It does not write the chapter conclusion.

Each packet file ends with an HTML comment containing: citations used; incoming/outgoing bridge proposals; a five-item self-check; and an integration note listing assumptions, omissions, dependencies, proposed contract changes, and unresolved questions. These notes do not count as chapter prose and will not be copied into the assembled chapter.

## 7. Required artifacts and quality controls

Working figures:

1. `fig-01-lineage.mmd` — responsibility shift from TIMP through Glotaran to pyglotaran.
2. `fig-02-separable-observation.mmd` — time-by-wavelength observation as temporal contributions times associated spectra plus unexplained variation.
3. `fig-03-object-graph.mmd` — ownership, named references, and separately supplied runtime inputs.
4. `fig-04-nested-estimation.mmd` — explicit outer parameters, element matrices, inner CLP estimate, residuals/penalties, outer optimizer loop.
5. `fig-05-runtime-lifecycle.mmd` — one-time, repeated, and post-processing phases.
6. `fig-06-extension-boundaries.mmd` — element, data-I/O, project-I/O, numerical-library, notebook, examples, and extras boundaries.

Required tables:

1. terminology concordance — Packet B;
2. core entities and responsibilities — Packet B;
3. mathematics-to-code concordance — Packet D;
4. extension surfaces — Packet F.

Before final handoff, the coordinating editor will freeze one integrated snapshot, commission three read-only reviews, and centrally apply accepted corrections. Review priorities are P0 source/mathematical/scientific contradiction, P1 terminology/architecture/evidence inconsistency, P2 readability/duplication/transition/figure/citation issue, and P3 optional enrichment.

Focused tests must be run, if the configured environment permits, for schemes, data models, optimization, and plugin registries. Failures or environment limitations are recorded rather than hidden. The final audit searches for stale terms and unsupported universals, including `megacomplex`, `dataset group`, `model compilation`, `compile the model`, `link_clp`, claims that CLPs are parameter objects, axis/method confusion, performance or caching claims, plugin-stability promises, automatic identifiability/model selection, and v1 predictions.

Gate 0 is passed when this file and the paragraph-level skeleton are present, all artifacts have one owner, notation and the running example are stable, and agents acknowledge exclusive file ownership.
