# Handoff plan: an architecture-first thesis chapter on pyglotaran

## Document status

- **Purpose:** execution-ready plan for producing an academic draft chapter about the architecture of the staging version of pyglotaran.
- **Execution pattern:** one coordinating editor plus several parallel research, drafting, and review agents. The plan is model-independent and can be run with a single strong model that delegates work or with several independently scheduled agents.
- **Reference workspace:** the repository containing the `pyglotaran`, `pyglotaran-examples`, `pyglotaran-extras`, and `Literature` directories.
- **Target delivery:** a coherent first draft within approximately two to three hours, followed by maintainer review and later refinement if needed.
- **Length:** aim for approximately 8,000-10,000 words of chapter body and captions. This is a soft editorial target, not a ceiling. Exceed it when additional explanation, evidence, or transitions materially improve accuracy and readability; remove repetition before removing necessary explanation. Count the reference list separately.
- **Citation style:** APA author-date in-text citations and an APA-formatted reference list.
- **Provisional chapter title:** *The Architecture of pyglotaran: A Composable Framework for Global and Target Analysis*.

This is a planning and handoff document, not the chapter itself. It deliberately gives the writing model narrower assignments, named evidence, terminology rules, and review gates. It should be updated if the staging code changes materially before the draft is written.

## 1. Commission and intended result

Write a self-contained, architecture-first account of pyglotaran at the level expected in an MSc thesis or a book chapter within a PhD thesis. The subject is the Python software package and the scientific-computing architecture embodied by the staging code, not merely the user-facing YAML syntax and not a tutorial for carrying out one analysis.

The chapter should explain how pyglotaran represents a global or target analysis, turns a declarative scientific specification into a numerical estimation problem, composes scientific model contributions, treats measured data and parameters, executes nested parameter estimation, records results, and admits extensions. The intended reader is a mathematics, physics, or other science student at bachelor level. No prior knowledge of global analysis, target analysis, time-resolved spectroscopy, separable least squares, or pyglotaran is assumed. Familiarity with basic algebra, graphs, matrices, and the idea of fitting a model to measurements is sufficient.

The source code in `pyglotaran/` is authoritative for the present architecture. Tests and staging-compatible examples are the next-best evidence for behavior and terminology. Published literature is authoritative for the scientific problem, mathematical vocabulary, and software lineage. Published descriptions of older pyglotaran releases are not authoritative for current class names or runtime structure.

The draft should remain useful as the staging architecture matures toward a v1 release. “Evergreen” here means that the central exposition is organized around responsibilities, information flows, invariants, and extension boundaries. It does **not** mean predicting an unreleased v1 API or concealing the fact that staging is the inspected reference implementation.

### Central thesis to test and refine

Use the following as a working thesis, not as an unexamined conclusion:

> Pyglotaran lets a researcher describe a scientific analysis using named, reusable building blocks. It connects these definitions to measured data and parameter values, constructs and solves the fitting problem, and returns enough detail to examine how the result was obtained. By keeping these responsibilities separate, the same numerical machinery can support many scientific models and extensions.

After the chapter has introduced the necessary terms, this can be stated more formally: the architecture separates declarative scientific structure, experimental data, explicit parameters, conditionally linear parameters, numerical realization, and result provenance within a common nested optimization workflow.

Every major section should contribute evidence for, qualify, or expose a trade-off in this thesis.

## 2. Deliverables and collision-free working layout

Parallel agents must not write into one shared draft. The coordinating editor creates and freezes the common contracts, each drafting agent owns unique section, evidence, and figure files, and only the coordinating editor writes the assembled chapter.

Use this working layout:

```text
docs/architecture-chapter-work/
|- 00-editorial-contract.md
|- 00-chapter-skeleton.md
|- sections/
|  |- 01-scientific-framing-and-lineage.md
|  |- 02-declarative-architecture.md
|  |- 03-data-and-parameters.md
|  |- 04-numerical-estimation.md
|  |- 05-runtime-results-and-provenance.md
|  `- 06-extensions-and-evaluation.md
|- evidence/
|  |- 01-framing-ledger.md
|  |- 02-architecture-ledger.md
|  |- 03-data-parameters-ledger.md
|  |- 04-numerical-ledger.md
|  |- 05-runtime-results-ledger.md
|  |- 06-extensions-ledger.md
|  `- helpers/
|- figures/
|  |- fig-01-lineage.mmd
|  |- fig-02-separable-observation.mmd
|  |- fig-03-object-graph.mmd
|  |- fig-04-nested-estimation.mmd
|  |- fig-05-runtime-lifecycle.mmd
|  `- fig-06-extension-boundaries.mmd
`- reviews/
   |- architecture-mathematics-review.md
   |- runtime-evidence-review.md
   `- readability-style-apa-review.md
```

The execution should ultimately produce:

1. `docs/pyglotaran-architecture-chapter-draft.md`  
   The integrated chapter, including title, short abstract or opening synopsis, numbered sections, original diagrams, tables, equations, conclusion, and APA references.

2. `docs/pyglotaran-architecture-evidence-ledger.md`  
   The merged audit trail mapping consequential claims to current source files, tests, examples, or literature.

3. `docs/pyglotaran-architecture-review-notes.md`  
   Remaining uncertainties, facts requiring maintainer confirmation, terminology decisions, exact inspected revisions, tests run, approximate word count, and known omissions.

Only the coordinating editor may modify the two `00-` contract files, the assembled draft, merged ledger, and final review notes. A drafting agent owns exactly one section file and its matching local ledger at a time. Figure ownership is assigned in the chapter skeleton. Cross-reviewers write review notes; they do not rewrite a peer's section. This prevents merge conflicts and makes conflicting definitions visible before integration.

The same packet owner should normally research and draft a topic, retaining sole ownership of its local ledger through Waves 1-2. A research-only helper writes an immutable note under `evidence/helpers/`; it never edits a packet ledger. The packet owner decides which helper findings to incorporate.

## 3. Non-blocking editorial questions and adopted defaults

The following questions can still be answered by the editor or maintainer. They do not block drafting; use the stated default until directed otherwise.

| Question | Default for the draft |
|---|---|
| Will the text stand alone or sit after a methods chapter that already explains global and target analysis? | Make it stand alone. Give a bachelor-level science reader enough spectroscopy and model-fitting context to follow the architecture. |
| Does the approximately 10,000-word target include references? | Treat references separately. A justified overrun in the chapter body is acceptable when it improves clarity or accuracy. |
| Should the chapter use first person, “we,” or an impersonal voice? | Use a neutral academic voice. Use “the package” or “the architecture” for software actions. |
| Should class names appear in headings? | No. Lead with concepts; place current class names in implementation-mapping paragraphs, tables, or figure annotations. |
| Should paper figures be reproduced? | No. Produce original architecture diagrams derived from the source and cite papers only for concepts or historical descriptions. |
| How much future-v1 language is appropriate? | Describe staging as the reference implementation of an architecture intended to mature toward v1; make no claim that a current name or API is guaranteed in v1. |
| Should the chapter contain executable code? | Prefer no code listings. At most, use one short declarative example if it materially clarifies the object graph. |

## 4. Source-of-truth hierarchy

Apply this hierarchy whenever sources disagree:

1. **Current staging source and focused tests** define the implemented architecture and runtime behavior.
2. **Current staging-compatible examples** demonstrate intended composition and vocabulary at the user-facing boundary.
3. **Published literature** defines the scientific problem, established mathematical concepts, and historical systems.
4. **Current documentation and docstrings** help with explanation but may retain transitional names. Verify them against code and tests.
5. **Comments, old examples, older pyglotaran papers, and migration remnants** are historical evidence only.
6. **Inference** is allowed only when labeled as interpretation and supported by multiple observations.

Do not resolve a discrepancy by choosing the source with the clearest prose. Record it in the evidence ledger and follow the hierarchy.

### Claim classes for the evidence ledger

Give each nontrivial claim one of these classes:

- **Implemented fact:** directly visible in current source and preferably exercised by a test.
- **Scientific definition:** established in the supplied literature.
- **Historical fact:** stated in the TIMP, Glotaran, or pyglotaran literature and consistent with the supplied project history.
- **Architectural interpretation:** a synthesis of several code facts; explicitly write “can be understood as,” “functions as,” or equivalent when the interpretation is not a named project concept.
- **Maintainer intent:** include only if supplied directly by a maintainer; do not infer it from a branch name.

Recommended ledger columns:

| Claim ID | Proposed claim | Class | Primary evidence | Corroborating evidence | Confidence | Safe wording | Draft location |
|---|---|---|---|---|---|---|---|

## 5. Literature corpus and its proper use

### 5.1 Scientific and mathematical foundation

Use `Literature/van_Stokkum_et_al-Global_and_target_analysis_of_time-resolved_spectra.pdf` as the primary source for:

- the distinction between the physicochemical model and the model for the observations;
- the measurement process and stochastic component;
- separability of kinetic or temporal and spectral contributions;
- the inverse problem and identifiability;
- global versus target analysis;
- building blocks such as kinetic schemes, instrument-response functions, spectral assumptions, and anisotropy;
- parameter estimation across multiple experiments;
- validation by residual analysis and scientific interpretability.

This 2004 review should normally be cited instead of the expanded lecture notes. Use `Literature/van_Stokkum-lecturenotes3cycle-Global_and_target_analysis_of_time-resolved_spectra.pdf` as a pedagogical aid when developing explanations of variable projection, weighting, multiple experiments, or model-discovery cycles. Treat it as grey literature unless it contributes material not adequately covered by the review.

### 5.2 TIMP

Use `Literature/Mullen_et_al-TIMP.pdf` for:

- interactive scientific model discovery as an iterative cycle of formulation, estimation, and validation;
- multiway and multi-dataset modeling;
- hierarchical scientific models and linked versus unlinked quantities;
- separable nonlinear least squares and partitioned variable projection;
- the historical computational architecture of TIMP;
- extension of TIMP with new model types.

The TIMP implementation is not a template for the present Python class graph. Its importance is conceptual and historical.

### 5.3 Glotaran

Use `Literature/Snellenburg_et_al-Glotaran.pdf` for:

- the historical relation between Glotaran and TIMP;
- the motivations for interactive data exploration, assisted model construction, and result inspection;
- the separation between the Java/NetBeans graphical application and the R/TIMP computational core connected through Rserve;
- the project-oriented analysis workflow.

Do not describe Glotaran as an earlier implementation of the current pyglotaran architecture. It was a graphical front end that delegated computation to TIMP.

### 5.4 Published pyglotaran account

Use `Literature/van_Stokkum_et_al-pyglotaran_a_lego_like_framework_for_gta.pdf` for:

- the problem-solving-environment framing;
- the model-specification, parameter-estimation, model-validation cycle;
- declarative, modular, “Lego-like” composition;
- the value of separating parameter definitions from model definitions through labels or references;
- the role of separable problems, conditionally linear parameters, variable projection, non-negative least squares, constraints, and penalties;
- the role of notebooks and the wider Python ecosystem in scientific practice.

The paper describes pyglotaran v0.7-era concepts. Terms such as `megacomplex`, dataset groups, and the old `link_clp` surface must not be presented as names in the staging architecture unless current code independently supports them. The scientific notion of a physical megacomplex may still be used when discussing a molecular system; it must not be confused with the removed software abstraction.

### 5.5 Provisional APA reference entries

Verify all metadata against the PDF title pages or DOI records before finalizing. Use APA author-date citations, for example `(van Stokkum et al., 2004)` and `(Mullen & van Stokkum, 2007)`.

- Mullen, K. M., & van Stokkum, I. H. M. (2007). TIMP: An R package for modeling multi-way spectroscopic measurements. *Journal of Statistical Software, 18*(3), 1–46. https://doi.org/10.18637/jss.v018.i03
- Snellenburg, J. J., Laptenok, S. P., Seger, R., Mullen, K. M., & van Stokkum, I. H. M. (2012). Glotaran: A Java-based graphical user interface for the R package TIMP. *Journal of Statistical Software, 49*(3), 1–22. https://doi.org/10.18637/jss.v049.i03
- van Stokkum, I. H. M., Larsen, D. S., & van Grondelle, R. (2004). Global and target analysis of time-resolved spectra. *Biochimica et Biophysica Acta (BBA) – Bioenergetics, 1657*(2–3), 82–104. https://doi.org/10.1016/j.bbabio.2004.04.011
- van Stokkum, I. H. M., Weißenborn, J., Weigand, S., & Snellenburg, J. J. (2023). Pyglotaran: A lego-like Python framework for global and target analysis of time-resolved spectra. *Photochemical & Photobiological Sciences, 22*, 2413–2431. https://doi.org/10.1007/s43630-023-00460-y

Do not mechanically preserve title capitalization from the PDFs; apply APA sentence case. Preserve author diacritics and the lowercase “van” in names.

## 6. Terminology contract

This section is binding for all work packets. If current code makes one of these definitions inaccurate, stop and update both the contract and ledger before drafting.

| Preferred term | Meaning in the chapter | Current implementation anchor | Avoid or qualify |
|---|---|---|---|
| **Physicochemical model** | A scientific hypothesis about states, species, kinetics, spectra, instrument effects, and related physical structure. | Realized through configured elements and their relationships. | Do not use bare “model” when this distinction matters. |
| **Model for the observations** | The combination of physicochemical assumptions, measurement assumptions, data organization, and stochastic residual model that predicts observed measurements. | Spans data models, elements, matrices, scaling, weighting, residual functions, and optimization. | Do not imply it is one Python object. |
| **Analysis specification** | The declarative object graph describing experiments and reusable scientific definitions. | `glotaran.project.scheme.Scheme`, together with its `ModelLibrary` and `ExperimentModel` objects. | A `Scheme` does not by itself contain all measured arrays and parameter values passed to optimization. |
| **Element** | A composable scientific contribution that can calculate a matrix contribution, impose relevant constraints, and create element-specific results. | `glotaran.model.element.Element` and built-in element packages. | Do not use the v0.7 software term “megacomplex.” |
| **Model library** | The collection of named, reusable element definitions available to analyses and capable of resolving extension relationships. | `glotaran.project.library.ModelLibrary`. | Do not describe it merely as a YAML dictionary. |
| **Data model** | The per-dataset declarative specification connecting a data source to elements, scales, weighting, dimensions, and optional global elements. | `glotaran.model.data_model.DataModel` and element-contributed subclasses. | It is not the measured numerical dataset. |
| **Measured data** | The labeled numerical observations and coordinates used in estimation. | Usually an `xarray.DataArray`, loaded or passed separately and wrapped by optimization data structures. | Avoid calling it a `DataModel`. |
| **Experiment** | A collection of one or more dataset specifications that may be optimized jointly and may share or link structure. | `glotaran.model.experiment_model.ExperimentModel`. | Do not use the obsolete “dataset group” as the current architectural term. |
| **Explicit parameter** | A named, serialized parameter with value, bounds, variation status, optional expression, uncertainty, and related metadata. It is an outer optimization variable when free. | `glotaran.parameter.Parameter` and `Parameters`. | Not every explicit parameter must be described as intrinsically nonlinear in the scientific sense. “Outer parameter” is the safer computational description. |
| **Conditionally linear parameter (CLP)** | A coefficient estimated by the inner linear or constrained-linear problem after explicit parameters determine the matrix. | CLP labels, estimation routines, fit decompositions, and matrix-reduction/linking logic in `glotaran.optimization`. | CLPs are not entries in `Parameters` and should not be called model parameters without qualification. |
| **Reference resolution or binding** | Replacing labels and extension relationships with the typed objects or explicit parameter references required for execution, with validation of missing or cyclic references. | `ModelLibrary.resolve`, `resolve_data_model`, `Item` reference handling, and optimization initialization. | Do not call this “model compilation.” There is no compiler, intermediate language, or compilation phase in the inspected architecture. |
| **Numerical realization** | The runtime construction and transformation of optimization data, element matrices, linked blocks, relations, constraints, scales, and residual vectors. | `OptimizationData`, `LinkedOptimizationData`, `OptimizationMatrix`, and `OptimizationObjective`. | If “preparation” is used, define it as a convenient umbrella term, not a named compiler stage. |
| **Model dimension** | The coordinate along which a model matrix is evaluated, commonly but not universally time. | Inferred and stored by optimization data/result metadata. | Do not equate it categorically with time. |
| **Global dimension** | The coordinate across which conditionally linear contributions are estimated or organized, commonly but not universally wavelength. | Inferred and stored by optimization data/result metadata. | Do not confuse it with “global analysis.” |
| **Global analysis** | A scientific-analysis strategy in which measurements are analyzed simultaneously under shared model structure. | Supported through matrix construction and experiment/multi-dataset organization. | It is a method, not the name of an array axis. |
| **Target analysis** | Testing or estimating a specified physicochemical model intended to yield physically interpretable states, species, or spectra. | Expressed through configured elements and parameters, not a separate optimizer. | Do not present it as a separate software mode unless current code has one. |
| **Result and provenance** | Numerical estimates, decompositions, residuals, metadata, resolved configuration, and input relationships sufficient to inspect what was fitted. | `glotaran.project.result.Result`, `OptimizationResult`, `OptimizationInfo`, element result datasets, and serialization. | Do not conflate core result construction with plotting supplied by `pyglotaran-extras`. |
| **Plugin** | A registered extension of element types, data I/O, or project I/O discovered and mediated by typed registries and entry points. | `glotaran.plugin_system` and entry points in `pyproject.toml`. | Do not imply arbitrary runtime monkey-patching or a single undifferentiated plugin API. |

### 6.1 What “dataset and parameter architecture” must mean

Do not use the phrase as a vague section label. Split it into two explicit architectural questions:

1. **How experimental data are represented and coordinated:** measured labeled arrays, data-source references, per-dataset scientific configuration, model and global dimensions, weights, scales, experiments containing multiple datasets, alignment or linking across global coordinates, and conversion into numerical optimization data.
2. **How unknown quantities are represented and estimated:** named explicit parameters and references, free versus fixed or expression-defined values, bounds, conditionally linear coefficients, coefficient labels, relations, constraints, penalties, uncertainty metadata, and the boundary between outer and inner estimation.

The chapter should explain the interaction between these questions only after it has defined them separately.

### 6.2 What “model compilation or preparation” must mean

There is no evidence for a compiler architecture. Replace “model compilation” with two observable phases:

1. **Semantic resolution and validation:** instantiate typed specifications from serialized or programmatic input; resolve named elements, extension chains, data-model types, and parameter references; detect missing or cyclic references; select the referenced parameter subset; and validate issues.
2. **Numerical realization:** orient labeled data, infer model and global dimensions, align linked datasets, calculate and combine element matrices, reduce relations and constraints, apply weights and scales, solve for CLPs, and assemble residual and penalty vectors.

Some numerical objects are created during optimization initialization; matrices that depend on changing explicit parameters are recalculated during objective evaluation. Therefore, do not imply that all mathematics is lowered once into an immutable executable plan.

### 6.3 Readability and van Stokkum-inspired style contract

The supplied papers by Ivo van Stokkum and co-authors share several useful expository habits. The chapter should follow these habits at the level of scholarly method and readability. It should not copy sentences, reproduce distinctive phrasing, or imitate surface mannerisms.

**Begin with the scientific question.** Van Stokkum's writing commonly starts from what is measured, what cannot be read directly from the measurements, and what the researcher wants to learn. Follow the order:

1. physical or experimental question;
2. observable data and the difficulty they present;
3. mathematical abstraction;
4. software responsibility;
5. current implementation anchor.

Do not begin a section with a class definition when the reader does not yet know why the class exists.

**Define words that carry more than one meaning.** The 2004 review explicitly pauses to distinguish two senses of “model.” Apply the same care to `DataModel`, experiment, element, parameter, CLP, residual, global dimension, global analysis, and target analysis. When a familiar word receives a specialized meaning, state both the ordinary idea and the technical definition.

**Build explanations from simple components.** Introduce a time- and wavelength-resolved measurement as the recurring example. First explain that the observed signal can be regarded as a combination of changing temporal contributions and their associated spectra. Then introduce matrices, conditional linearity, multiple datasets, constraints, and plugins one step at a time. Use “building block” or “component” language where it clarifies composition, but do not let the metaphor replace a precise definition.

**Connect formalism to physical meaning.** Every equation needs:

- a plain-language lead-in explaining the problem it solves;
- definitions and dimensions for all new symbols;
- a sentence afterward explaining the operation and its experimental meaning;
- a connection to the corresponding software responsibility.

No paragraph should introduce more notation than it immediately explains. Define `argmin`, residual, norm, weighting, constraint set, and variable projection in ordinary language before relying on them.

**Use restrained and qualified claims.** Prefer “can,” “usually,” “in this case,” “under these assumptions,” and “commonly” when a statement is conditional. State limitations and model assumptions directly. Avoid promotional adjectives, universal claims, and unqualified statements that a fit proves a physical mechanism.

**Use concrete signposting.** Tell the reader why the next step is needed. Integrate figures and tables into the explanation rather than attaching them after the fact. End a section by stating what has been established and what question follows.

**Prefer readable sentences over technical compression.** Aim for one principal claim per paragraph. Define acronyms on first use. Prefer concrete verbs such as “loads,” “connects,” “calculates,” “estimates,” and “stores.” Avoid dense noun phrases and long chains of abstractions. Terms such as object graph, semantic resolution, numerical realization, invariant, provenance, registry, entry point, identifiability, nuisance parameter, separability, and variable projection must either be defined immediately or replaced initially with plainer language.

Useful plain-language introductions include:

- “a network of named definitions and references” before **object graph**;
- “connecting a name to the object or parameter it denotes” before **reference resolution**;
- “building the numerical fitting problem” before **numerical realization**;
- “the difference between the measured and calculated values” before **residual**;
- “information that records where a result came from” before **provenance**.

**Write for a science undergraduate without writing down to the reader.** The prose may be mathematically rigorous, but it must supply the conceptual steps. A reader should not need Python knowledge to understand a figure, and should not need spectroscopy experience to understand why time, wavelength, shared kinetics, and associated spectra form a useful running example.

The integration editor must apply this style contract across all independently drafted sections. Stylistic consistency cannot be delegated to section authors alone.

## 7. Architectural questions the chapter must answer

The final prose should allow a reader to answer all of the following without consulting the code:

1. What does a time- and wavelength-resolved measurement contain, and why is it difficult to interpret directly?
2. What scientific and numerical problem is pyglotaran designed to represent?
3. Which concerns are deliberately separated, and why are those separations useful?
4. What is declarative about an analysis, and what remains runtime state?
5. How do a `Scheme`, model library, experiments, data models, elements, measured data, and parameters relate?
6. How are names and references converted into executable relationships?
7. How can multiple model contributions and multiple datasets be combined without giving every scientific model its own optimizer?
8. Why are explicit parameters and CLPs treated differently?
9. How do labeled dimensions become matrix axes and linked numerical blocks?
10. What happens, in order, from `Scheme.optimize(...)` to a `Result`?
11. Where do weighting, scales, coefficient relations, constraints, penalties, and residual functions enter?
12. What does the result preserve for validation, interpretation, and reproducibility?
13. How can third-party scientific elements and I/O formats participate without modifying the central optimizer?
14. Which responsibilities belong to core pyglotaran, and which belong to notebooks, examples, or `pyglotaran-extras`?
15. What trade-offs follow from the architecture?

## 8. Code and example reading map

Read the files below before making the corresponding claim. Use symbol search to follow relevant helpers; do not rely only on the named file.

### 8.1 Declarative analysis and composition

- `pyglotaran/glotaran/project/scheme.py`
- `pyglotaran/glotaran/project/library.py`
- `pyglotaran/glotaran/model/element.py`
- `pyglotaran/glotaran/model/item.py`
- `pyglotaran/glotaran/model/data_model.py`
- `pyglotaran/glotaran/model/experiment_model.py`
- built-in element packages under `pyglotaran/glotaran/builtin/`
- tests under `pyglotaran/tests/project/` and `pyglotaran/tests/model/`

Questions to verify:

- What does a `Scheme` own, and what is passed separately to `optimize`?
- How does a `ModelLibrary` resolve element extension and cycles?
- Which abstract responsibilities must an element implement?
- How can an element contribute a specialized `DataModel` subtype?
- Which constraints are attached to elements, experiments, or data models?

### 8.2 Parameters

- `pyglotaran/glotaran/parameter/parameter.py`
- `pyglotaran/glotaran/parameter/parameters.py`
- parameter-reference and field-introspection logic reachable from `glotaran/model/item.py`
- parameter-related focused tests

Questions to verify:

- Which values and metadata belong to an explicit parameter?
- How are free, fixed, expression-defined, bounded, and nonnegative parameters represented?
- Which subset is passed to the outer optimizer?
- Where are standard errors or covariance-derived quantities written back?
- Which objects contain CLPs instead of explicit parameters?

### 8.3 Numerical execution

- `pyglotaran/glotaran/optimization/optimization.py`
- `pyglotaran/glotaran/optimization/objective.py`
- `pyglotaran/glotaran/optimization/data.py`
- `pyglotaran/glotaran/optimization/matrix.py`
- `pyglotaran/glotaran/optimization/estimation.py`
- `pyglotaran/glotaran/optimization/variable_projection.py`
- `pyglotaran/glotaran/optimization/nnls.py`
- `pyglotaran/glotaran/optimization/info.py`
- focused tests under `pyglotaran/tests/optimization/`

Questions to verify:

- What is constructed once in `Optimization.__init__`, and what is recalculated per objective call?
- How are free explicit parameters updated?
- How are matrices contributed, combined, related, constrained, weighted, scaled, or linked?
- How are CLPs and residuals obtained for variable projection and non-negative least squares?
- How are residuals and penalties concatenated across objectives?
- How are degrees of freedom, covariance, uncertainty, and histories calculated?

### 8.4 Results, persistence, simulation, and extensions

- `pyglotaran/glotaran/project/result.py`
- result classes in `pyglotaran/glotaran/optimization/objective.py`
- `pyglotaran/glotaran/simulation/simulation.py`
- `pyglotaran/glotaran/plugin_system/base_registry.py`
- other registries under `pyglotaran/glotaran/plugin_system/`
- `pyglotaran/glotaran/io/interface.py`
- `pyglotaran/glotaran/utils/json_schema.py`
- entry-point declarations in `pyglotaran/pyproject.toml`
- focused tests under `pyglotaran/tests/plugin_system/`

Questions to verify:

- Which inputs, resolved specifications, fitted quantities, decompositions, residuals, statistics, and source paths are retained?
- How do element-specific result datasets preserve their origin?
- Which numerical path is reused by simulation?
- What are the distinct extension surfaces for elements, data I/O, and project I/O?
- How do short and fully qualified plugin names, conflict handling, and pinning work?
- How does dynamic schema generation expose plugin-contributed types?

### 8.5 Representative current examples

Inspect, but do not turn the chapter into walkthroughs of:

- `pyglotaran-examples/pyglotaran_examples/study_fluorescence/models/global_model.yaml`
- `pyglotaran-examples/pyglotaran_examples/study_fluorescence/models/target_model.yaml`
- the two-dataset example under `pyglotaran-examples/`
- the DOAS example under `pyglotaran-examples/`
- `link-clp-sim/models/sim-scheme.yaml`

Use repository search to locate the latter files if their enclosing directories have moved. Confirm that examples use current `library`, `experiments`, `datasets`, `elements`, `activations`, and `global_elements` structures before citing them.

Examples are evidence for the declarative surface and composition patterns. They are not sufficient evidence for internal runtime claims.

## 9. Proposed chapter structure and word budget

The section budgets below total approximately 8,000-9,250 words and are planning proportions, not acceptance criteria. Individual sections may move by roughly 20%. Aim for a complete chapter near 10,000 words, but permit a justified overrun when it supplies explanation, evidence, or transitions that a bachelor-level reader needs. During integration, remove duplicated introductions, class catalogs, and low-value detail before compressing necessary scientific or mathematical explanation.

### 9.1 Opening synopsis and scope — 300-400 words

**Purpose:** state the scientific-computing problem, the chapter's architectural thesis, the staging/v1 framing, and the evidence basis.

**Required content:**

- one compact description of global and target analysis;
- why architecture matters for extensible scientific model discovery;
- what the chapter covers and excludes;
- the distinction between concepts intended to be stable and implementation names used as evidence.

**Avoid:** a marketing introduction, feature checklist, or long history before the reader knows the present problem.

### 9.2 Scientific problem and software lineage — 850-1,000 words

**Purpose:** establish the problem that shaped the architecture and give only the history needed to understand design changes.

**Argument:**

- A time-resolved spectroscopic experiment records how a signal changes with both time and wavelength, producing a data surface rather than one easily interpreted curve.
- The central interpretive problem is to connect patterns in that surface to a small set of physically meaningful contributions and parameters.
- Time-resolved and related multiway measurements require a model for observations built from scientific and measurement assumptions.
- Scientific model discovery is iterative: specify, estimate, validate, revise.
- TIMP supplied an extensible R computational environment and separable-estimation machinery.
- Glotaran supplied an interactive Java GUI around TIMP through Rserve rather than replacing the core.
- Pyglotaran rewrote the computational core in Python and shifted interactive scientific work toward notebooks and the Python ecosystem rather than reproducing the monolithic desktop GUI.

**Evidence:** the 2004 review, TIMP paper, Glotaran paper, and 2023 pyglotaran paper. Cite each historical transition.

**Required nuance:** notebooks are an external working and reporting environment, not a layer inside the core optimizer.

**Figure candidate:** a small lineage diagram showing responsibilities, not a product timeline full of versions.

### 9.3 Why the package is divided into these responsibilities — 600-700 words

**Purpose:** explain why the package is partitioned as it is before presenting classes.

**Drivers to substantiate:**

- composable scientific building blocks;
- declarative, inspectable specifications;
- reuse across datasets and experiments;
- separation of explicit and conditionally linear estimation;
- labeled multidimensional data;
- extensibility without a separate optimizer for every scientific model;
- preservation of interpretable results and provenance.

**Package boundary:**

- core pyglotaran owns typed analysis specifications, parameter handling, numerical realization, optimization, simulation, results, and extension registries;
- xarray/NumPy/SciPy and related libraries supply numerical and labeled-array foundations;
- notebooks coordinate scientific work outside the core;
- `pyglotaran-examples` demonstrates analyses;
- `pyglotaran-extras` supplies plotting and higher-level exploration utilities.

**Invariants to test in code:**

- elements expose a common matrix-contribution contract;
- names are resolved before numerical use;
- explicit parameters and CLPs remain distinct;
- result creation can be traced back to contributing elements;
- plugins enter through registries and typed interfaces.

**Avoid:** presenting the package directory tree as the architecture. If “invariant,” “declarative,” or another architectural term is useful, explain it first in ordinary language.

### 9.4 How an analysis is assembled from connected definitions — 1,050-1,200 words

**Purpose:** give the reader a static mental model.

**Presentation order:**

1. Explain the analysis specification as an object graph rather than as YAML.
2. Introduce `Scheme` as the orchestration root for experiments and a model library.
3. Explain the model library as reusable named element definitions, including extension relationships.
4. Explain an experiment as the joint-analysis boundary for one or more dataset specifications.
5. Explain a data model as per-dataset scientific and data-association configuration.
6. Explain elements as typed, composable matrix-producing scientific contributions.
7. Show measured arrays and explicit `Parameters` entering optimization separately.

**Required distinction:** a serialized YAML or dictionary is one representation of the analysis. The architecture uses typed Python objects to represent meaningful scientific structures; Pydantic is a current implementation mechanism, and plugins may contribute additional typed structures.

**Required examples:** use one global-analysis and one target-analysis configuration only to illustrate different compositions of the same architecture. Do not reproduce complete YAML.

**Figure:** an original static component diagram:

```text
Scheme
|- ModelLibrary -> named Elements
`- Experiments
   `- Dataset specifications -> element references

Separately supplied:
|- measured labeled arrays
`- explicit Parameters
```

The finished diagram must add ownership, reference, and runtime-input distinctions that the sketch omits.

### 9.5 Connecting named definitions before fitting — 650-750 words

**Purpose:** explain how a declarative graph becomes internally coherent without invoking compilation.

**Required flow:**

- serialized or programmatic input creates typed objects;
- element types determine available fields and may contribute data-model subtypes;
- model-library names, extension relationships, item references, and parameter labels are resolved;
- cyclic or missing references and semantic issues are detected;
- only referenced explicit parameters need participate in the analysis;
- the resolved graph remains a scientific specification, not yet a fixed numerical matrix.

**Architectural interpretation:** named references keep reusable definitions separate until the package connects each name to the element, data model, or parameter it denotes. Describe this concrete mechanism. A named software-design pattern is unnecessary.

**Avoid:**

- “compile,” “compiler,” “intermediate representation,” or “code generation”;
- claiming all invalid models are statically rejected;
- treating inheritance through `extends` as Python class inheritance.

### 9.6 Experimental data and multi-dataset organization — 750-850 words

**Purpose:** explain how labeled observations acquire numerical meaning.

**Required content:**

- separation of a data model from measured data;
- xarray coordinates and dimension labels;
- inference or declaration of model and global dimensions;
- orientation and slicing of arrays for optimization;
- weights and scales;
- experiment-level grouping;
- alignment/linking of datasets across global coordinates using tolerance and method;
- single-dataset versus linked numerical representations;
- experiment-specific scale or nuisance structure where supported.

**Scientific connection:** relate simultaneous analysis of several measurements to the literature on multiway data and shared versus experiment-specific quantities.

**Required warning:** “global dimension” is an array/model coordinate; “global analysis” is a scientific method. They may often align conceptually, but are not synonyms.

**Figure or table:** a small diagram showing two labeled datasets becoming aligned numerical slices or blocks. Verify exact linking semantics in `optimization/data.py` and tests before drawing it.

### 9.7 Two kinds of unknowns and how they are estimated — 1,400-1,550 words

**Purpose:** provide the mathematical and architectural center of the chapter.

**Required narrative:**

1. Distinguish explicit named parameters from CLPs.
2. Explain free, fixed, bounded, nonnegative, and expression-defined explicit parameters.
3. Introduce a generic separable observation model.
4. Explain how elements calculate matrices from coordinates and explicit parameters.
5. Explain matrix composition and labeling of coefficient columns.
6. Explain the inner solution for CLPs and the outer least-squares problem for free explicit parameters.
7. Explain variable projection and non-negative least squares as supported inner estimators.
8. Explain relations, constraints, scales, weights, and penalties at their actual stages.
9. Explain residual concatenation across objectives or experiments.
10. Explain uncertainty and degrees-of-freedom accounting without overstating statistical guarantees.

**Pedagogical order:**

1. State in words that an observed signal can be approximated by adding component shapes multiplied by their amplitudes, plus measurement noise.
2. Give a two-component example in prose or simple scalar notation.
3. Show how values collected over time and wavelength form a matrix.
4. Introduce the general matrix equation and define every row, column, and symbol.
5. Explain the inner and outer estimation problems in words.
6. Only then introduce `argmin`, weighted norms, constraint sets, and penalty terms.

**Minimum equations:**

For dataset or experimental unit \(q\), introduce a generic separable model:

\[
\mathbf{Y}_q = \mathbf{M}_q(\boldsymbol{\theta})\mathbf{B}_q + \boldsymbol{\varepsilon}_q,
\]

where \(\boldsymbol{\theta}\) denotes free explicit outer parameters, \(\mathbf{M}_q\) is assembled from element contributions, and \(\mathbf{B}_q\) contains one or more sets of CLPs. Adjust orientation to the chapter's data convention and keep it consistent.

Before proceeding, explain the dimensions and physical interpretation of \(\mathbf{Y}_q\), \(\mathbf{M}_q\), and \(\mathbf{B}_q\) using the running time-and-wavelength example.

Define the inner problem:

\[
\widehat{\mathbf{B}}_q(\boldsymbol{\theta})
=
\arg\min_{\mathbf{B}_q \in \mathcal{C}_q}
\left\|
\mathbf{W}_q\left[
\mathbf{Y}_q-\mathbf{M}_q(\boldsymbol{\theta})\mathbf{B}_q
\right]
\right\|_F^2,
\]

where \(\mathcal{C}_q\) expresses only constraints actually supported by the selected estimator and matrix-reduction path.

Then define the outer objective schematically:

\[
\widehat{\boldsymbol{\theta}}
=
\arg\min_{\boldsymbol{\theta}\in\Theta}
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

Clarify that the implementation may append penalty residuals rather than evaluate a separately represented scalar penalty term; the equation is explanatory.

Define \(\arg\min\) as “the argument, or set of parameter values, that gives the smallest mismatch.” Explain the Frobenius and Euclidean norms as ways of combining many residual values into one measure of mismatch. Do not expect notation alone to teach these operations.

**Notation concordance:** explicitly map \(\boldsymbol{\theta}\) to free explicit `Parameters`, \(\mathbf{B}\) to CLPs, \(\mathbf{M}\) to `OptimizationMatrix` content, and \(\mathbf{r}\) to the residual vector consumed by SciPy's least-squares routine.

**Scientific connection:** relate this to the separable nonlinear least-squares and variable-projection treatment in the 2004 review and TIMP paper. Do not imply that the Python implementation is a port of TIMP's partitioned variable-projection implementation unless proven.

**Required code nuance:** distinguish initialization-time numerical objects from matrices recalculated as explicit parameters change.

### 9.8 Runtime lifecycle: from specification to result — 800-900 words

**Purpose:** turn the static and mathematical views into a temporal view.

**Required sequence, verified against source:**

1. Receive a scheme, explicit parameters, and data or data references.
2. Load or associate measured data.
3. Resolve library, data-model, element, and parameter references.
4. validate analysis issues;
5. create one or more optimization objectives and numerical data wrappers;
6. select the free outer-parameter vector and configure least squares;
7. for each objective evaluation, update explicit parameters, calculate and transform matrices, estimate CLPs, and build residuals and penalties;
8. concatenate objective contributions and let the outer optimizer iterate;
9. calculate optimization statistics and uncertainties supported by the implementation;
10. construct per-experiment and per-element results, fitted data, decompositions, residuals, metadata, and the top-level result.

Use the exact source to correct ordering. For example, do not say data loading occurs inside optimization if `Scheme.optimize` performs it beforehand.

**Figure:** an original sequence or activity diagram. Visually separate:

- one-time resolution/initialization;
- repeated objective evaluation;
- post-optimization result construction.

**Avoid:** repeating every mathematical detail from the prior section.

### 9.9 Results, validation, provenance, and persistence — 600-700 words

**Purpose:** show that the output architecture supports the model-discovery cycle rather than returning only an optimized vector.

**Required content:**

- top-level `Result`;
- initial and optimized explicit parameters;
- per-experiment optimization results;
- fitted data, residuals, CLPs, matrix/fit decompositions, model/global dimensions, scales, and error metrics where actually present;
- optimization diagnostics, covariance/uncertainty information, histories, versions, and degrees of freedom where actually present;
- element-specific results and element identity/provenance;
- source path and serialization/persistence;
- distinction between core result data and visualization in `pyglotaran-extras`.

**Scientific connection:** validation includes numerical fit quality, residual structure, parameter precision, and physicochemical plausibility. The architecture provides data for validation; it does not decide scientific validity automatically.

### 9.10 How pyglotaran is extended and used with other tools — 550-650 words

**Purpose:** explain how the compositional claim extends beyond built-in kinetics.

**Required content:**

- element-type registration;
- element-contributed data-model types;
- data I/O and project I/O as distinct interfaces;
- entry-point discovery;
- short versus fully qualified names and conflict/pinning behavior, if confirmed;
- dynamic schema generation;
- simulation's reuse of resolution and matrix machinery;
- roles of examples, extras, notebooks, xarray, NumPy, SciPy, and Numba without turning the section into a dependency list.

**Use built-ins as evidence, not as a catalog:** kinetics, spectral contributions, coherent artifact, damped oscillation, baseline, and CLP guidance are enough to demonstrate heterogeneity.

**Figure:** use a concrete boundary diagram showing what each extension supplies and what the core supplies in return. A named software-architecture pattern is unnecessary.

### 9.11 Trade-offs, limitations, and conclusion — 450-550 words

**Purpose:** assess the architecture rather than merely describing it.

**Candidate trade-offs to verify and discuss:**

- declarative composition increases inspectability and reuse but makes reference resolution and validation necessary;
- dynamic plugin-contributed typing supports extension but complicates schemas, error reporting, and name conflicts;
- separation of outer parameters and CLPs exploits problem structure but constrains how models must expose linearity;
- labeled arrays improve semantic clarity but require dimension inference, orientation, and alignment at the numerical boundary;
- preserving rich decompositions and provenance aids validation but produces more complex result structures;
- notebook-centered workflows are flexible and reproducible when disciplined, but do not reproduce all affordances of a dedicated GUI.

Do not invent performance claims, scalability limits, security properties, or roadmap items. End by returning to the central thesis and explaining how the architecture embodies the scientific model-discovery cycle.

## 10. Required figures and tables

All figures must be original abstractions based on the inspected code. Mermaid is acceptable for the Markdown draft. Each diagram must have a caption that states its view and what arrows mean.

### Figures

1. **Scientific-software lineage and responsibility shift**  
   TIMP as R computational core; Glotaran as Java GUI delegating to TIMP through Rserve; pyglotaran as a Python rewrite of the computational core used through notebooks and a broader Python ecosystem. Keep chronology secondary to responsibility.

2. **A separable time- and wavelength-resolved observation**  
   Show a measured time-by-wavelength data surface as the sum of a small number of temporal contributions and their associated spectra, plus unexplained noise. This is the reader's visual entry point to separability, CLPs, and the recurring scientific example. Use plain-language labels; code identifiers do not belong in this figure.

3. **Static analysis object graph**  
   `Scheme`, model library, experiments, data models, elements, measured data, and explicit parameters. Distinguish ownership from named references and runtime inputs with different edge styles.

4. **Nested estimation architecture**  
   Explicit outer parameters feed element matrix calculations; composed matrices and observations feed the CLP estimator; residuals and penalties feed the outer least-squares optimizer; updated parameters close the loop.

5. **Runtime lifecycle**  
   Input/deserialize, resolve, validate, realize numerical objectives, repeatedly evaluate, optimize, and construct results. Mark one-time, iterative, and post-processing phases.

6. **Extension and ecosystem boundaries**  
   Core registries and interfaces, element plugins, data/project I/O, external numerical libraries, notebooks, examples, and extras.

Optional seventh figure:

7. **Multi-dataset alignment and block structure**  
   Include only if it clarifies linking more effectively than prose and can be verified exactly from tests.

For every figure, use plain-language labels first and code identifiers only as secondary annotations. Explain all arrows and phases in the caption, do not rely on color alone, and make the figure intelligible without source-code knowledge.

### Tables

1. **Terminology concordance:** scientific term, architectural concept, current implementation anchor, common confusion.
2. **Core entities and responsibilities:** entity, owns, references, produces, invariant.
3. **Mathematics-to-code concordance:** equation symbol, scientific meaning, runtime representation, lifecycle.
4. **Extension surfaces:** registry/interface, extension supplies, core guarantees, resulting capability.

Avoid a v0.7-to-v0.8 migration table in the main narrative unless reviewers specifically request it. A compact historical terminology note is enough.

## 11. Parallel multi-stage execution plan

The work proceeds in parallel waves with explicit synchronization gates. The coordinating editor may run independent tasks concurrently, but no downstream task may rely on an upstream artifact until its gate has passed. The same plan can be executed serially if only one agent is available.

### Wave 0 — Coordinator bootstrap and contract freeze (15-20 minutes)

Only the coordinating editor works on shared files during this wave.

**Actions:**

- Record the exact commit, branch, and package version for `pyglotaran`.
- Record the commits for `pyglotaran-examples` and `pyglotaran-extras`.
- Check working-tree status without modifying or resetting existing changes.
- Inventory the relevant source, tests, examples, and supplied PDFs.
- Create `00-editorial-contract.md` from the terminology, readability, style, evidence, citation, and anti-hallucination rules in this handoff.
- Create a paragraph-level `00-chapter-skeleton.md`.
- Freeze the physical setup of the running time-and-wavelength example and its notation, including which quantities Packet A introduces and which mathematical development Packet D owns.
- Assign one owner to every definition, equation, figure, table, section file, and evidence namespace.

Each outline entry must state:

```text
Section purpose:
Claims uniquely owned here:
Definitions introduced here:
Prior concepts this section may assume:
Material explicitly deferred elsewhere:
Required evidence namespace:
Required equation, figure, or table:
Opening premise:
Exit point or bridge:
Approximate length:
```

**Gate 0 — Contract freeze:**

- terminology, mathematical notation, reader level, APA conventions, and style contract are stable for the drafting wave;
- every concept has one canonical section owner;
- every agent has an exclusive file set;
- no current source term has been imported from the v0.7 paper without confirmation.

After this gate, agents propose contract changes in their integration notes rather than modifying shared contracts.

### Wave 1 — Parallel evidence reconstruction (25-40 minutes)

Run as many of these evidence lanes concurrently as capacity permits:

1. **Scientific foundations and lineage:** literature definitions, TIMP, Glotaran, pyglotaran history, APA metadata, and the prose-style brief.
2. **Declarative architecture:** `Scheme`, library, elements, data models, experiments, typing, references, and resolution.
3. **Data and unknown quantities:** labeled measured data, dimensions, alignment, explicit parameters, CLPs, relations, constraints, weights, and scales.
4. **Numerical execution:** matrix construction, inner estimation, outer optimization, residual and penalty assembly, and uncertainty.
5. **Runtime results:** lifecycle ordering, result structures, validation data, provenance, and persistence.
6. **Extensions and ecosystem:** simulation reuse, registries, I/O, schemas, examples, extras, notebooks, and verified trade-offs.

Each packet owner writes only its namespaced evidence fragment and retains sole ownership through drafting. If a separate research helper is used, the helper writes a distinct read-only note under `evidence/helpers/`; it does not touch the packet ledger. Consequential claims receive a claim ID, confidence level, safe wording, and exact source anchors before prose drafting.

**Gate 1 — Evidence readiness:**

- every planned diagram edge and mathematical claim has an evidence ID;
- the data-model/measured-data distinction and explicit-parameter/CLP distinction are correct;
- uncertainties are explicit `[VERIFY: ...]` items;
- no agent has edited another agent's evidence file.

### Wave 2 — Parallel section drafting (45-75 minutes)

Section authors work from the frozen skeleton and approved evidence fragments. They draft only their assigned Markdown files. They must not independently write a chapter introduction or final conclusion.

Each author delivers:

- the assigned section draft;
- a local evidence fragment;
- assigned figure or table source;
- citations used for later APA consolidation;
- a two-sentence proposed incoming bridge and outgoing bridge;
- a self-check against the packet acceptance criteria;
- an integration note listing assumptions, deliberate omissions, cross-section dependencies, proposed contract changes, and unresolved questions.

**Anti-duplication rules:**

- define only concepts assigned to the section;
- when another section owns a definition, use a one-sentence reminder and an explicit cross-reference;
- do not repeat the full model-specification, estimation, and validation cycle;
- place implementation inventories in the evidence ledger rather than the prose;
- use shared notation exactly and do not invent synonyms for element, experiment, data model, explicit parameter, CLP, or residual;
- advance the chapter's argument from the section's perspective instead of writing a stand-alone essay.

**Gate 2 — Section freeze:**

- all assigned artifacts are present;
- section-level `[VERIFY]` items are enumerated;
- approximate length is proportionate, with any material overrun explained;
- no section relies on unstated prior knowledge;
- the section ends at the exit point defined by the skeleton.

The editor may begin integrating a frozen section while other section authors finish.

### Wave 3 — Single-owner integration (30-45 minutes)

Only the coordinating editor edits the assembled chapter.

**Actions:**

- assemble accepted section files in argumentative order;
- write the opening synopsis, cross-section transitions, and conclusion;
- introduce scientific ideas before current class names;
- remove duplicated definitions and repeated setup paragraphs;
- normalize terminology, notation, tense, voice, figure references, and APA citations;
- create one deduplicated reference list;
- make the running time-and-wavelength example consistent;
- assess length against the approximately 10,000-word soft target.

The editor must synthesize rather than concatenate. Useful detail should survive a modest overrun; repeated introductions, API catalogs, and unmotivated implementation detail should not.

**Gate 3 — Integrated draft:**

- the chapter has one thesis, one terminology system, and one mathematical notation;
- `Scheme`, `DataModel`, explicit parameters, CLPs, and nested estimation are each fully defined once;
- figures and tables occur where the prose needs them;
- the opening and conclusion reflect the integrated argument rather than one section author's viewpoint.

### Wave 4 — Parallel independent review (20-30 minutes)

Reviewers inspect the same integrated draft but write separate issue reports. They do not patch the chapter.

1. **Architecture and mathematics reviewer:** checks equations, code behavior, lifecycle ordering, dimensions, matrix transformations, and diagram arrows.
2. **Runtime and evidence reviewer:** checks source anchors, tests, results, plugins, stale vocabulary, and unsupported universals.
3. **Readability, style, and APA reviewer:** reads primarily as a bachelor-level science reader; checks definitions, jargon, transitions, van Stokkum-inspired explanatory habits, citations, and reference formatting.

Prioritize findings:

- **P0:** source contradiction, mathematical error, or scientific error;
- **P1:** terminology, notation, architecture, or evidence inconsistency;
- **P2:** readability, duplication, transition, figure, or citation problem;
- **P3:** optional enrichment.

**Gate 4 — Review completeness:** each review reports findings with priority, location, evidence or rationale, and a proposed correction. Reviewers do not silently rewrite peers' work.

### Wave 5 — Final correction and verification (20-35 minutes)

Only the coordinating editor modifies the integrated draft; other agents may perform targeted fact or equation checks on request.

**Actions:**

- triage P0 and P1 findings first, then P2;
- re-read implementation anchors behind all high-consequence claims;
- run focused existing tests for schemes, data models, optimization, and plugin registries using the configured environment;
- check staging examples for current vocabulary;
- verify equation orientations and all diagram arrows;
- resolve high-priority `[VERIFY]` markers or move genuine uncertainties to review notes;
- merge local evidence fragments;
- report word count and justify any material overrun;
- perform a stale-term search.

Suggested stale-term search list:

```text
megacomplex
dataset group
model compilation
compile the model
link_clp
CLP parameter object
global dimension (when global analysis is meant)
```

These strings may occur in historical discussion or an explicit warning, but not as unqualified current architecture.

**Gate 5 — Reviewable draft:**

- focused tests pass or failures are recorded and scoped;
- no unresolved high-confidence architectural claim remains;
- the chapter remains intelligible when class names are treated as annotations rather than the main narrative;
- any length beyond the soft target is caused by necessary explanation or evidence, not repetition.

### Two-to-three-hour schedule

| Elapsed time | Coordinating editor | Parallel agents |
|---:|---|---|
| 0:00-0:15 | Freeze contracts, interfaces, and skeleton | Inventory assigned sources; do not draft or read changing contracts |
| 0:15-0:45 | Release frozen contracts and coordinate evidence | Read contracts and build independent evidence fragments |
| 0:45-1:40 | Monitor boundaries; integrate only sections already frozen | Draft disjoint section files and figures |
| 1:40-2:00 | Freeze the integrated draft, transitions, synopsis, and conclusion | Finish self-checks and remain available for fact questions |
| 2:00-2:25 | Make no edits to the review snapshot | Run three independent review lanes against the same snapshot |
| 2:25-3:00 | Apply findings, merge ledgers, verify, and report | Perform targeted fact checks if requested |

With fewer agents, combine adjacent packets as described in Section 12 and allow a longer first-draft window. Do not shorten the contract, evidence, mathematical-trace, or review gates merely to meet the clock.

## 12. Parallel work packets and artifact ownership

Packets A-F are independent after Gate 1 unless an explicit dependency is listed. Run all six concurrently when capacity permits. With fewer workers, combine adjacent packets without merging their files; one worker can own several files sequentially.

Suggested allocation:

| Available section authors | Allocation |
|---:|---|
| 2 | Author 1: A-B-C; Author 2: D-E-F |
| 3 | Author 1: A-B; Author 2: C-D; Author 3: E-F |
| 4 | Author 1: A; Author 2: B-C; Author 3: D-E; Author 4: F |
| 5 | Author 1: A; Author 2: B; Author 3: C-D; Author 4: E; Author 5: F |
| 6 or more | One author per packet; additional agents perform evidence or figure work |

The coordinating editor is not counted as a section author. It owns the contracts, skeleton, integrated synopsis, transitions, conclusion, reference list, and final draft.

### Packet A — Scientific framing and lineage

**Exclusive artifacts:**

- `sections/01-scientific-framing-and-lineage.md`
- `evidence/01-framing-ledger.md`
- `figures/fig-01-lineage.mmd`
- `figures/fig-02-separable-observation.mmd`

**Produces:** the scientific primer and lineage portion of Sections 9.1-9.2, without the final opening synopsis; approximately 900-1,200 words as guidance.

**Read first:** the title pages, introductions, relevant methods, design sections, and conclusions of the four primary papers.

**Required claims:**

- explain what a time- and wavelength-resolved measurement contains;
- explain global and target analysis as model-based strategies in ordinary language;
- explain scientific model discovery as specification, estimation, validation, and revision;
- identify TIMP as the R computational environment;
- identify Glotaran as a Java GUI using TIMP through Rserve;
- identify pyglotaran as a Python rewrite of the computational core within notebook-centered scientific workflows.

**Forbidden shortcuts:**

- do not say pyglotaran is merely “Glotaran without the GUI”;
- do not project the current class graph backward onto TIMP or Glotaran;
- do not spend more than one third of the packet on history;
- do not assume prior spectroscopy knowledge.

**Acceptance:** each generation has literature support; the separable-observation figure is understandable to a science undergraduate without code knowledge.

### Packet B — Declarative architecture and resolution

**Exclusive artifacts:**

- `sections/02-declarative-architecture.md`
- `evidence/02-architecture-ledger.md`
- `figures/fig-03-object-graph.mmd`

**Produces:** Sections 9.3-9.5 and Tables 1-2; approximately 2,200-2,700 words as guidance.

**Read first:** Section 8.1 source and tests, plus current representative YAML.

**Required claims:**

- motivate the need for a reusable network of named scientific definitions before introducing “object graph”;
- explain how `Scheme` organizes experiments and a model library;
- explain that measured data and explicit parameter values enter separately;
- explain elements as reusable scientific matrix contributions;
- explain data models as per-dataset specifications;
- explain reference and extension resolution in plain language before giving implementation names.

**Forbidden shortcuts:**

- no compiler metaphor;
- no claim that YAML itself is the architecture;
- no current “megacomplex” or “dataset group” terminology;
- no exhaustive field or class catalog;
- no introduction to nested optimization, which belongs to Packet D.

**Acceptance:** the prose answers who owns, references, and produces what; every object-graph edge has evidence.

### Packet C — Experimental data and explicit unknowns

**Exclusive artifacts:**

- `sections/03-data-and-parameters.md`
- `evidence/03-data-parameters-ledger.md`

**Produces:** Section 9.6 and the first part of Section 9.7; approximately 1,300-1,700 words as guidance.

**Read first:** Sections 8.2-8.3 source and tests, stopping before detailed estimator implementation.

**Required claims:**

- distinguish measured arrays from data models;
- explain labeled dimensions, orientation, weights, scales, and multi-dataset alignment;
- distinguish explicit parameters from CLPs;
- explain fixed, free, bounded, nonnegative, and expression-defined explicit parameters;
- define model and global dimensions without fixing them to time and wavelength;
- prepare the reader for separability without teaching the complete inner/outer algorithm.

**Forbidden shortcuts:**

- never say all entries in `Parameters` are intrinsically nonlinear;
- never say CLPs are stored in `Parameters`;
- never equate model dimension with time or global dimension with wavelength except in a clearly marked example;
- do not duplicate the static object-graph definition from Packet B.

**Acceptance:** a novice reader can explain the measured-data/data-model and explicit-parameter/CLP distinctions before reaching the mathematics.

### Packet D — Nested numerical estimation

**Exclusive artifacts:**

- `sections/04-numerical-estimation.md`
- `evidence/04-numerical-ledger.md`
- `figures/fig-04-nested-estimation.mmd`

**Produces:** the mathematical center of Section 9.7 and Table 3; approximately 1,500-2,000 words as guidance.

**Read first:** the optimization matrix and estimator sources/tests, plus the variable-projection sections of the 2004 and TIMP papers. Use the Packet C-to-D interface and shared notation frozen in `00-chapter-skeleton.md`; reconcile Packet C's eventual exit note during integration rather than waiting for it.

**Required claims:**

- build from the two-component observation example to matrix notation;
- explain element matrices and CLP column labels;
- explain inner CLP estimation and outer least squares in words before equations;
- explain variable projection and non-negative least squares at the supported level;
- place relations, constraints, scales, weights, and penalties at verified stages;
- map every symbol to physical meaning and a runtime representation.

**Forbidden shortcuts:**

- no unexplained `argmin`, norm, or constraint-set notation;
- no claim that the Python routine is TIMP's partitioned algorithm unless proven;
- no assumption that all matrices are constructed once;
- no repetition of parameter types already owned by Packet C.

**Acceptance:** a bachelor-level reader can explain why the inner solve exists, and a technical reviewer can trace each equation to code and literature.

### Packet E — Runtime, results, and provenance

**Exclusive artifacts:**

- `sections/05-runtime-results-and-provenance.md`
- `evidence/05-runtime-results-ledger.md`
- `figures/fig-05-runtime-lifecycle.mmd`

**Produces:** Sections 9.8-9.9; approximately 1,300-1,700 words as guidance.

**Read first:** `scheme.py`, core optimization orchestration, `result.py`, result classes, and focused tests.

**Required claims:**

- distinguish initialization, repeated objective evaluation, and post-optimization result construction;
- trace data, explicit parameters, matrices, CLPs, residuals, optimizer output, diagnostics, and result datasets;
- explain why rich results support validation and reproducibility;
- explain provenance first as recording where results came from;
- identify element provenance without claiming more than stored metadata supports.

**Forbidden shortcuts:**

- do not say all matrices are prepared once;
- do not portray validation as automated proof of a physicochemical model;
- do not assign plotting to core;
- do not rederive the equations from Packet D.

**Acceptance:** ordering matches source; result-field claims have implementation anchors; the lifecycle figure separates one-time, repeated, and post-processing steps.

### Packet F — Extensions, ecosystem, and evaluation

**Exclusive artifacts:**

- `sections/06-extensions-and-evaluation.md`
- `evidence/06-extensions-ledger.md`
- `figures/fig-06-extension-boundaries.mmd`
- Table 4, “Extension surfaces,” embedded in the section file

**Produces:** Sections 9.10-9.11 except the final integrative conclusion, Figure 6, and Table 4; approximately 1,000-1,400 words as guidance.

**Read first:** Section 8.4 source/tests, built-in registration, and relevant parts of the 2023 paper.

**Required claims:**

- distinguish element, data-I/O, and project-I/O contracts;
- explain registries and entry points in ordinary language;
- explain how element plugins can affect typed declarative capabilities;
- explain simulation's reuse of relevant core mechanisms;
- distinguish examples, extras, notebooks, and numerical-library roles;
- discuss verified trade-offs as paired benefits and costs.

**Forbidden shortcuts:**

- do not assert named architecture patterns as project facts;
- do not promise compatibility, future plugin stability, or v1 APIs;
- do not invent performance claims;
- do not write the chapter conclusion.

**Acceptance:** at least four trade-offs are explained; plugin concepts remain intelligible without Python packaging knowledge.

### Coordinator packet — Integration, synopsis, and conclusion

**Exclusive artifacts:** the `00-` files, assembled chapter, merged ledger, final review notes, and reference list.

**Wave 3 inputs:** all frozen packet artifacts.

**Wave 5 inputs:** the frozen integrated draft plus the independent review reports.

**Actions:**

- write the opening synopsis and final conclusion only after reading all packets;
- establish one argumentative arc;
- remove overlapping explanations;
- make scientific concepts precede current implementation names;
- normalize notation, capitalization, tense, voice, and figure numbering;
- replace `[VERIFY]` markers only from evidence;
- consolidate and format APA references;
- apply the van Stokkum-inspired style and bachelor-level readability contracts;
- report word count and assess whether any overrun is justified.

**Acceptance:** all global quality gates in Section 14 pass.

## 13. Shared instructions and guardrails for all agents

Give every research, drafting, review, and integration agent the rules relevant to its role. These rules are independent of model or inference mode.

1. **Read the contracts first.** Read `00-editorial-contract.md` and `00-chapter-skeleton.md` before inspecting assigned evidence or drafting.
2. **Respect exclusive ownership.** Modify only assigned working files. Propose shared-contract changes in the integration note.
3. **Evidence before prose.** For each subsection, record claims and evidence-ledger IDs before writing paragraphs.
4. **Source code leads architectural terminology.** A term in a paper or docstring is not current merely because it sounds plausible.
5. **Literature leads scientific terminology.** Use the supplied papers for definitions of global analysis, target analysis, separability, model discovery, and validation.
6. **Distinguish description from interpretation.** If the code does not name a design pattern, frame it as a useful interpretation rather than project terminology.
7. **No compilation metaphor.** Say “instantiate,” “resolve,” “bind,” “validate,” “construct,” “realize,” or “evaluate,” according to the observed operation.
8. **No future invention.** The chapter may explain why concepts are likely to be durable, but it must not promise v1 names, compatibility, roadmap features, or performance.
9. **No stale vocabulary.** `Element` and `Experiment` are current. Use `megacomplex`, dataset group, and old CLP-linking APIs only in explicitly historical passages.
10. **Keep data concepts separate.** A `DataModel` configures a dataset; an xarray object contains measured data; an experiment coordinates one or more dataset specifications; numerical wrappers prepare data for estimation.
11. **Keep unknowns separate.** `Parameters` contains explicit parameters. CLPs are inner estimated coefficients represented through matrix labels, estimators, decompositions, and results.
12. **Qualify scientific equivalence.** An explicit outer parameter is often intrinsically nonlinear, but the software distinction is how it participates in computation.
13. **Use dimensions carefully.** “Model” and “global” dimensions are general coordinate roles, not fixed physical quantities.
14. **Treat notebooks correctly.** Jupyter is a user environment around the package, not an internal pyglotaran architectural component.
15. **Treat results as scientific evidence structures.** Explain decompositions and residuals, but do not claim the software establishes scientific truth.
16. **Write for the defined reader.** Explain the scientific idea in ordinary language before its formal term, equation, or class name.
17. **Follow the shared style.** Begin from the scientific question, define ambiguous terms, connect mathematics to physical meaning, qualify conditional claims, and use concrete signposting.
18. **Do not duplicate another section.** Define only concepts assigned by the skeleton. Use a short reminder and cross-reference for concepts owned elsewhere.
19. **Prefer paragraphs over catalogs.** Class and field lists belong in tables only when they clarify a responsibility boundary.
20. **Use original diagrams.** Do not reproduce paper figures or closely imitate their graphic composition.
21. **Use APA consistently.** Author-date in text; sentence case in reference titles; italic journal and volume; DOI as an HTTPS URL.
22. **Avoid direct quotations.** Paraphrase with citation. If a short quotation is indispensable, include an APA page number.
23. **Expose uncertainty.** Insert `[VERIFY: precise question and likely source]`; never fill a gap with a generic software-architecture claim.
24. **Protect the user's workspace.** Read broadly but modify only the planned documentation artifacts. Do not reset, format, or “clean up” source repositories.
25. **Treat length as guidance.** Add detail when it improves clarity, evidence, or the architectural argument. Remove repetition and low-value API detail first.

### Recommended parallel packet prompt

```text
You own [artifact path] in a parallel academic-writing workflow about
the staging architecture of pyglotaran. Read 00-editorial-contract.md
and 00-chapter-skeleton.md first. Your exclusive scope is [scope].
Other agents own [adjacent scopes].

Inspect the named source, tests, examples, and literature. Record claims
under evidence namespace [PREFIX] before drafting. Write approximately
[word range], treating this as guidance rather than a hard limit. Follow
the shared terminology, notation, APA, reader-level, and style contracts.

Do not modify shared files or the assembled chapter. Do not redefine
concepts owned by other sections. Do not write an independent chapter
introduction or conclusion. Use [VERIFY: ...] instead of guessing.

Produce:
1. your evidence fragment;
2. your section draft;
3. assigned figure or table source;
4. citations used;
5. a five-item self-check;
6. an integration note listing assumptions, deliberate omissions,
   cross-section dependencies, proposed contract changes, and unresolved
   questions.
```

## 14. Global quality gates

### 14.1 Architectural accuracy

- [ ] `Scheme`, library, experiments, data models, elements, measured data, and parameters have distinct, accurate roles.
- [ ] Static ownership and named references are not conflated.
- [ ] Semantic resolution is distinct from numerical realization.
- [ ] Initialization-time and per-evaluation operations are distinguished.
- [ ] Explicit outer parameters and CLPs are represented and estimated separately.
- [ ] Multi-dataset linking, scaling, weighting, relations, constraints, and penalties are placed at verified stages.
- [ ] Result and plugin claims match current source and tests.

### 14.2 Scientific accuracy

- [ ] The two meanings of “model” are defined.
- [ ] Global and target analysis follow literature terminology.
- [ ] Separability and the nested problem are explained with consistent equations.
- [ ] Validation is presented as iterative scientific assessment, not a scalar score.
- [ ] Multiple experiments and shared versus experiment-specific quantities are discussed without forcing TIMP's old hierarchy onto current code.

### 14.3 Historical accuracy

- [ ] TIMP is described as the computational R environment.
- [ ] Glotaran is described as a Java GUI using TIMP through Rserve.
- [ ] Pyglotaran is described as a Python rewrite of the core, not a Python binding to TIMP.
- [ ] Notebook use is presented as an ecosystem/workflow shift.
- [ ] Older pyglotaran terminology is clearly historical.

### 14.4 Academic quality

- [ ] The central thesis is stated, developed, qualified, and revisited.
- [ ] Sections are connected by an argument rather than a feature inventory.
- [ ] Each substantial scientific or historical claim has an APA citation.
- [ ] Architecture claims are traceable through the evidence ledger.
- [ ] All figures are original, readable, captioned, and referenced in the prose.
- [ ] Symbols are defined once and used consistently.
- [ ] The conclusion evaluates trade-offs without introducing new facts.

### 14.5 Evergreen quality

- [ ] Conceptual language leads; class names appear as implementation anchors.
- [ ] No statement promises the unreleased v1 API.
- [ ] The exact inspected staging revision is recorded outside the timeless core argument.
- [ ] Transitional names, stale docstrings, and example remnants have been checked.
- [ ] Removal of a specific class name would not destroy the explanation of its responsibility.

### 14.6 Readability and explanatory style

- [ ] A bachelor-level mathematics, physics, or other science reader can follow the chapter without prior knowledge of spectroscopy, nonlinear optimization, or pyglotaran.
- [ ] Every technical term and acronym is defined at first use.
- [ ] Each section begins from the scientific or architectural question it answers.
- [ ] Every equation has a verbal lead-in, complete symbol definitions, and a physical interpretation afterward.
- [ ] No paragraph introduces more notation than it immediately explains.
- [ ] Every figure can be understood without knowing Python class names.
- [ ] The time-and-wavelength example remains consistent throughout.
- [ ] The text follows the van Stokkum-inspired habits of careful definitions, progressive building blocks, restrained claims, and concrete signposting.
- [ ] Dense noun phrases, avoidable jargon, and unnecessary code identifiers have been removed.
- [ ] A code-independent reviewer can explain the distinctions between measured data and a data model, explicit parameters and CLPs, global and target analysis, and specification and numerical execution.

### 14.7 Editorial and format quality

- [ ] The chapter is proportioned around the approximately 10,000-word soft target; any material overrun is justified in review notes.
- [ ] APA author-date citations and references are consistent.
- [ ] Headings are concept-led and no deeper than necessary.
- [ ] Tables do not repeat prose.
- [ ] Code identifiers use inline code formatting.
- [ ] No unresolved high-priority `[VERIFY]` markers remain.

## 15. Anti-hallucination audit

Before handoff, search the draft for claims in these categories and verify each one:

- statements that a class “always,” “never,” or “guarantees” something;
- performance, memory, convergence, or scalability comparisons;
- claims about thread safety, parallelism, caching, immutability, or lazy evaluation;
- claims that all element matrices have a particular orientation or dimensionality;
- claims about plugin compatibility or schema stability;
- claims about automatic identifiability analysis or scientific model selection;
- statements about v1 plans;
- statements copied conceptually from TIMP or v0.7 and projected onto staging;
- claims based only on one example;
- names that occur only in a docstring, error message, or migration shim.

Replace an unsupported universal statement with a scoped observation, or remove it.

## 16. Definition of done

The work is done when:

1. the complete, coherent draft exists and its length has been assessed against the approximately 10,000-word soft target;
2. the source-led terminology contract is followed throughout;
3. the scientific framing and lineage are supported by APA citations;
4. the static object graph, semantic-resolution path, numerical-estimation path, result path, and extension boundaries are all explained;
5. the equations are consistent with both the literature and the staging execution path;
6. the evidence ledger supports all consequential architectural claims;
7. focused tests have been run or a precise reason for not running them is recorded;
8. all figures are original and verified against source;
9. uncertainties are visible in review notes instead of hidden in prose; and
10. a pyglotaran maintainer can review the chapter by following claim IDs to a small, relevant source set rather than rereading the entire repository.

The most important success criterion is not exhaustive API coverage or exact adherence to a word count. It is that a bachelor-level science reader can explain why the architecture has its present separations, how an analysis moves through them, and how those separations support the scientific cycle of model specification, parameter estimation, and validation.
