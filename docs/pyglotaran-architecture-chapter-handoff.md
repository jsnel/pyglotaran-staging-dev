# Handoff plan: an architecture-first thesis chapter on pyglotaran

## Document status

- **Purpose:** execution-ready plan for producing an academic draft chapter about the architecture of the staging version of pyglotaran.
- **Primary executor:** GPT-5.6 Luna, with review by a stronger model or a pyglotaran maintainer at the evidence and synthesis gates.
- **Reference workspace:** the repository containing the `pyglotaran`, `pyglotaran-examples`, `pyglotaran-extras`, and `Literature` directories.
- **Target delivery:** a coherent draft by the end of the working day.
- **Length:** aim for 8,000-9,200 words of chapter body and captions; the body must remain below 10,000 words. The reference list may be counted separately, but the draft should not depend on that exclusion to stay below the limit.
- **Citation style:** APA author-date in-text citations and an APA-formatted reference list.
- **Provisional chapter title:** *The Architecture of pyglotaran: A Composable Framework for Global and Target Analysis*.

This is a planning and handoff document, not the chapter itself. It deliberately gives the writing model narrower assignments, named evidence, terminology rules, and review gates. It should be updated if the staging code changes materially before the draft is written.

## 1. Commission and intended result

Write a self-contained, architecture-first account of pyglotaran at the level expected in an MSc thesis or a book chapter within a PhD thesis. The subject is the Python software package and the scientific-computing architecture embodied by the staging code, not merely the user-facing YAML syntax and not a tutorial for carrying out one analysis.

The chapter should explain how pyglotaran represents a global or target analysis, turns a declarative scientific specification into a numerical estimation problem, composes scientific model contributions, treats measured data and parameters, executes nested parameter estimation, records results, and admits extensions. The argument should be accessible to a scientifically literate reader who understands elementary linear algebra, nonlinear least squares, and the purpose of time-resolved spectroscopy, but who does not already know pyglotaran.

The source code in `pyglotaran/` is authoritative for the present architecture. Tests and staging-compatible examples are the next-best evidence for behavior and terminology. Published literature is authoritative for the scientific problem, mathematical vocabulary, and software lineage. Published descriptions of older pyglotaran releases are not authoritative for current class names or runtime structure.

The draft should remain useful as the staging architecture matures toward a v1 release. “Evergreen” here means that the central exposition is organized around responsibilities, information flows, invariants, and extension boundaries. It does **not** mean predicting an unreleased v1 API or concealing the fact that staging is the inspected reference implementation.

### Central thesis to test and refine

Use the following as a working thesis, not as an unexamined conclusion:

> Pyglotaran translates the iterative practice of global and target analysis into a composable software architecture that separates declarative scientific structure, experimental data, explicit parameters, conditionally linear parameters, numerical realization, and result provenance. This separation permits reusable model elements and plugin-defined capabilities while retaining a common nested optimization workflow.

Every major section should contribute evidence for, qualify, or expose a trade-off in this thesis.

## 2. Deliverables

The execution should produce:

1. `docs/pyglotaran-architecture-chapter-draft.md`  
   The complete chapter draft, including title, short abstract or opening synopsis, numbered sections, original diagrams, tables, equations, conclusion, and APA references.

2. `docs/pyglotaran-architecture-evidence-ledger.md`  
   A compact audit trail mapping consequential architectural and scientific claims to current source files, tests, examples, or literature. This is an internal writing artifact, not necessarily part of the finished chapter.

3. `docs/pyglotaran-architecture-review-notes.md`  
   Remaining uncertainties, facts requiring maintainer confirmation, terminology decisions, exact staging commit inspected, tests run, word count, and known omissions.

If time is tight, the chapter and evidence ledger are mandatory. The review notes may be appended to the ledger, but uncertainties must never be silently converted into facts.

## 3. Non-blocking editorial questions and adopted defaults

The following questions can still be answered by the editor or maintainer. They do not block drafting; use the stated default until directed otherwise.

| Question | Default for the draft |
|---|---|
| Will the text stand alone or sit after a methods chapter that already explains global and target analysis? | Make it stand alone, but keep the scientific primer concise. |
| Does the 10,000-word ceiling include references? | Keep the body and captions at or below 9,200 words, so the answer does not affect compliance. |
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

## 7. Architectural questions the chapter must answer

The final prose should allow a reader to answer all of the following without consulting the code:

1. What scientific and numerical problem is pyglotaran designed to represent?
2. Which concerns are deliberately separated, and why are those separations useful?
3. What is declarative about an analysis, and what remains runtime state?
4. How do a `Scheme`, model library, experiments, data models, elements, measured data, and parameters relate?
5. How are names and references converted into executable relationships?
6. How can multiple model contributions and multiple datasets be combined without giving every scientific model its own optimizer?
7. Why are explicit parameters and CLPs treated differently?
8. How do labeled dimensions become matrix axes and linked numerical blocks?
9. What happens, in order, from `Scheme.optimize(...)` to a `Result`?
10. Where do weighting, scales, coefficient relations, constraints, penalties, and residual functions enter?
11. What does the result preserve for validation, interpretation, and reproducibility?
12. How can third-party scientific elements and I/O formats participate without modifying the central optimizer?
13. Which responsibilities belong to core pyglotaran, and which belong to notebooks, examples, or `pyglotaran-extras`?
14. What trade-offs follow from the architecture?

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

The section budgets below total approximately 7,900-9,050 words, leaving room for transitions and captions while staying below 10,000. A section may move by about 10%, but the assembled draft must be edited back to the 8,000-9,200-word target rather than allowed to approach the ceiling.

### 9.1 Opening synopsis and scope — 300-350 words

**Purpose:** state the scientific-computing problem, the chapter's architectural thesis, the staging/v1 framing, and the evidence basis.

**Required content:**

- one compact description of global and target analysis;
- why architecture matters for extensible scientific model discovery;
- what the chapter covers and excludes;
- the distinction between concepts intended to be stable and implementation names used as evidence.

**Avoid:** a marketing introduction, feature checklist, or long history before the reader knows the present problem.

### 9.2 Scientific problem and software lineage — 750-850 words

**Purpose:** establish the problem that shaped the architecture and give only the history needed to understand design changes.

**Argument:**

- Time-resolved and related multiway measurements require a model for observations built from scientific and measurement assumptions.
- Scientific model discovery is iterative: specify, estimate, validate, revise.
- TIMP supplied an extensible R computational environment and separable-estimation machinery.
- Glotaran supplied an interactive Java GUI around TIMP through Rserve rather than replacing the core.
- Pyglotaran rewrote the computational core in Python and shifted interactive scientific work toward notebooks and the Python ecosystem rather than reproducing the monolithic desktop GUI.

**Evidence:** the 2004 review, TIMP paper, Glotaran paper, and 2023 pyglotaran paper. Cite each historical transition.

**Required nuance:** notebooks are an external working and reporting environment, not a layer inside the core optimizer.

**Figure candidate:** a small lineage diagram showing responsibilities, not a product timeline full of versions.

### 9.3 Architectural drivers, boundaries, and invariants — 600-700 words

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

**Avoid:** presenting the package directory tree as the architecture.

### 9.4 The declarative analysis object graph — 1,050-1,200 words

**Purpose:** give the reader a static mental model.

**Presentation order:**

1. Explain the analysis specification as an object graph rather than as YAML.
2. Introduce `Scheme` as the orchestration root for experiments and a model library.
3. Explain the model library as reusable named element definitions, including extension relationships.
4. Explain an experiment as the joint-analysis boundary for one or more dataset specifications.
5. Explain a data model as per-dataset scientific and data-association configuration.
6. Explain elements as typed, composable matrix-producing scientific contributions.
7. Show measured arrays and explicit `Parameters` entering optimization separately.

**Required distinction:** a serialized YAML or dictionary is one representation of the graph. Pydantic-backed typed objects and plugin-contributed subclasses are the semantic architecture.

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

### 9.5 Composition, typing, and semantic resolution — 650-750 words

**Purpose:** explain how a declarative graph becomes internally coherent without invoking compilation.

**Required flow:**

- serialized or programmatic input creates typed objects;
- element types determine available fields and may contribute data-model subtypes;
- model-library names, extension relationships, item references, and parameter labels are resolved;
- cyclic or missing references and semantic issues are detected;
- only referenced explicit parameters need participate in the analysis;
- the resolved graph remains a scientific specification, not yet a fixed numerical matrix.

**Architectural interpretation:** the architecture combines dependency injection by labels with runtime typing and validation. Use this wording only if the evidence ledger supports it; otherwise describe the mechanism without naming the pattern.

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

### 9.7 Unknown quantities and nested numerical estimation — 1,400-1,550 words

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

**Minimum equations:**

For dataset or experimental unit \(q\), introduce a generic separable model:

\[
\mathbf{Y}_q = \mathbf{M}_q(\boldsymbol{\theta})\mathbf{B}_q + \boldsymbol{\varepsilon}_q,
\]

where \(\boldsymbol{\theta}\) denotes free explicit outer parameters, \(\mathbf{M}_q\) is assembled from element contributions, and \(\mathbf{B}_q\) contains one or more sets of CLPs. Adjust orientation to the chapter's data convention and keep it consistent.

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

### 9.10 Extension architecture and ecosystem boundaries — 550-650 words

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

**Figure:** a port-and-adapter-style boundary diagram is acceptable if the labels are concrete and source-backed. Do not impose that architectural name on the project unless clearly marked as interpretation.

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

2. **Static analysis object graph**  
   `Scheme`, model library, experiments, data models, elements, measured data, and explicit parameters. Distinguish ownership from named references and runtime inputs with different edge styles.

3. **Nested estimation architecture**  
   Explicit outer parameters feed element matrix calculations; composed matrices and observations feed the CLP estimator; residuals and penalties feed the outer least-squares optimizer; updated parameters close the loop.

4. **Runtime lifecycle**  
   Input/deserialize, resolve, validate, realize numerical objectives, repeatedly evaluate, optimize, and construct results. Mark one-time, iterative, and post-processing phases.

5. **Extension and ecosystem boundaries**  
   Core registries and interfaces, element plugins, data/project I/O, external numerical libraries, notebooks, examples, and extras.

Optional sixth figure:

6. **Multi-dataset alignment and block structure**  
   Include only if it clarifies linking more effectively than prose and can be verified exactly from tests.

### Tables

1. **Terminology concordance:** scientific term, architectural concept, current implementation anchor, common confusion.
2. **Core entities and responsibilities:** entity, owns, references, produces, invariant.
3. **Mathematics-to-code concordance:** equation symbol, scientific meaning, runtime representation, lifecycle.
4. **Extension surfaces:** registry/interface, extension supplies, core guarantees, resulting capability.

Avoid a v0.7-to-v0.8 migration table in the main narrative unless reviewers specifically request it. A compact historical terminology note is enough.

## 11. Multi-stage execution plan

Each stage has an output and a gate. Luna must not proceed by assuming a failed gate will be repaired during final editing.

### Stage 0 — Establish the evidence baseline (20-30 minutes)

**Actions:**

- Record the exact commit, branch, and package version for `pyglotaran`.
- Record the commits for `pyglotaran-examples` and `pyglotaran-extras`.
- Check working-tree status without modifying or resetting existing changes.
- Inventory the relevant source, tests, examples, and five supplied PDFs.
- Create the evidence-ledger headings and claim classes.

**Output:** metadata block and empty structured ledger.

**Gate:** the writer can identify which repository is authoritative and can distinguish staging source from older literature.

### Stage 1 — Produce a terminology and scientific brief (45-60 minutes)

**Actions:**

- Read the relevant sections of the 2004 review, TIMP paper, Glotaran paper, and 2023 pyglotaran paper.
- Extract paraphrased definitions for global analysis, target analysis, separability, explicit/nonlinear parameters, CLPs, variable projection, multi-experiment analysis, scientific model discovery, and validation.
- Write the three-generation historical account in no more than 300 working words.
- Populate the literature rows of the evidence ledger.
- Verify APA metadata.

**Output:** a one- to two-page terminology brief in the evidence ledger.

**Gate:** no current source-code term has been imported from the v0.7 paper without confirmation.

### Stage 2 — Reconstruct the static architecture (60-75 minutes)

**Actions:**

- Read the declarative-analysis files in Section 8.1 and relevant tests.
- Trace ownership and references from `Scheme` through library, experiments, data models, and elements.
- Verify what parameters and measured data are passed separately.
- Trace specialized data-model creation and element extension.
- Draft Figure 2 and Tables 1-2.
- Add evidence rows for every arrow and cardinality in the figure.

**Output:** a static architecture brief of 800-1,000 working words plus draft diagram and tables.

**Gate:** every node and relationship in the diagram is supported by current staging source or a focused test.

### Stage 3 — Reconstruct data and parameter architecture (60-75 minutes)

**Actions:**

- Trace measured data from the scheme boundary into `OptimizationData` or `LinkedOptimizationData`.
- Verify dimension inference, orientation, weighting, scaling, and linked-dataset alignment.
- Trace explicit parameter parsing, references, expressions, bounds, variation, free-vector construction, and uncertainty update.
- Trace where CLP labels arise and where CLP values are stored.
- Populate the relevant portions of Tables 1 and 3.

**Output:** two separate briefs: “experimental data organization” and “unknown quantities.”

**Gate:** the briefs never use `DataModel` for the measured array and never put CLPs inside `Parameters`.

### Stage 4 — Reconstruct numerical realization and lifecycle (75-90 minutes)

**Actions:**

- Trace `Scheme.optimize` into `Optimization`, objectives, outer least squares, objective evaluation, inner estimation, information calculation, and result construction.
- Write a source-backed sequence with one-time, repeated, and post-optimization steps.
- Trace element matrices through combination, linking, reduction, weighting, scaling, and residual formation.
- Verify variable-projection and NNLS dispatch.
- Draft the equations and notation concordance.
- Draft Figures 3-4.

**Output:** runtime trace, mathematical brief, and figures.

**Gate:** a reviewer can follow one free explicit parameter from its initial value through matrix recalculation and follow one CLP from a matrix label through inner estimation into the result.

### Stage 5 — Reconstruct results and extension boundaries (45-60 minutes)

**Actions:**

- Inventory top-level, per-experiment, fit-decomposition, metadata, optimization-information, and element-specific result structures.
- Trace serialization and source-path handling.
- Trace plugin registries, entry points, I/O interfaces, name conflicts/pinning, and schema generation.
- Verify how simulation reuses model resolution and matrix construction.
- Establish precise boundaries for notebooks, examples, and extras.
- Draft Figure 5 and Table 4.

**Output:** result/provenance and extensibility briefs.

**Gate:** no plotting responsibility is assigned to core unless present in current core; no single generic “plugin API” is claimed when interfaces differ.

### Stage 6 — Storyboard and evidence review (30-40 minutes)

**Actions:**

- Turn the Section 9 outline into paragraph-level claims.
- Assign evidence-ledger IDs to each paragraph.
- Place equations, figures, and tables where they advance an argument.
- Check section budgets before prose drafting.
- Mark facts that still need maintainer confirmation.

**Output:** paragraph storyboard with word allocation.

**Gate:** every paragraph has a purpose and evidence; no section is merely a class or feature inventory.

### Stage 7 — Draft in bounded work packets (2.5-3.5 hours)

Draft in the work-packet order specified in Section 12. Each packet must:

- stay within its word budget;
- use the terminology contract;
- cite literature in APA style;
- cite or record code evidence in the ledger rather than inventing scholarly citations for local files;
- include transitions to adjacent packets;
- leave explicit `[VERIFY: ...]` markers rather than guessing.

Assemble the packets only after each packet passes its local acceptance criteria.

**Output:** first complete chapter.

**Gate:** complete argument, all figures/tables present, chapter body no more than 9,500 words at first assembly.

### Stage 8 — Technical verification (45-75 minutes)

**Actions:**

- Re-read the exact implementation anchors behind every high-consequence claim.
- Run focused existing tests for schemes, data models, optimization, and plugin registries using the workspace's configured environment. Do not install or upgrade dependencies without approval.
- Check representative staging examples for current vocabulary.
- Verify equation orientations and definitions against code and literature.
- Verify every diagram arrow.
- Search for prohibited or stale terms.

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

**Output:** corrected draft and completed evidence ledger.

**Gate:** no unresolved high-confidence `[VERIFY]` marker; focused tests pass or failures are recorded and scoped.

### Stage 9 — Academic and evergreen edit (45-60 minutes)

**Actions:**

- Replace API-manual prose with responsibility and flow language.
- Ensure every class name has already been motivated by a concept.
- Make the two meanings of “model” explicit at first use and consistent thereafter.
- Remove version-specific details that do not support the architectural argument.
- Where a current name is useful, identify it as an implementation anchor rather than a promised v1 name.
- Check APA in-text citations and reference entries.
- Check every borrowed idea is cited and every figure is original.
- Reduce repetition and bring the body to 8,000-9,200 words.
- Write the conclusion last.

**Output:** reviewable chapter draft and review notes.

**Gate:** the draft remains intelligible if class names are visually treated as annotations rather than the main narrative.

### Suggested same-day schedule

| Elapsed time | Milestone |
|---:|---|
| 0:00-1:00 | Stages 0-1 complete |
| 1:00-3:30 | Stages 2-4 complete |
| 3:30-4:30 | Stages 5-6 complete |
| 4:30-7:30 | First full draft assembled |
| 7:30-9:00 | Technical verification and academic edit |

If less time is available, reduce example detail and the number of figures. Do not skip the terminology, numerical-trace, or verification stages.

## 12. Luna work packets

The smaller writing model should receive one bounded packet at a time, plus this handoff, the current evidence ledger, and only the source subset named for the packet. It should not be asked to “write the whole chapter from the repository” in one pass.

### Packet A — Scientific framing and lineage

**Produces:** Sections 9.1-9.2 and Figure 1; 1,050-1,200 words.

**Read first:** the title pages, introductions, architecture/method sections, and conclusions of the four primary papers.

**Required claims:**

- global and target analysis are model-based analysis strategies;
- scientific model discovery iterates specification, estimation, and validation;
- TIMP was the R computational environment;
- Glotaran was a Java GUI that used TIMP through Rserve;
- pyglotaran is a Python rewrite of the computational core and participates in notebook-centered scientific workflows.

**Forbidden shortcuts:**

- do not say pyglotaran is “Glotaran without the GUI” without immediately explaining the rewrite and ecosystem change;
- do not project the current class graph backward onto TIMP or Glotaran;
- do not spend more than one third of the packet on history.

**Acceptance:** at least one citation supports each generation; the present architectural problem is visible by the end.

### Packet B — Architectural thesis and static object graph

**Produces:** Sections 9.3-9.5, Figure 2, and Tables 1-2; 2,300-2,650 words.

**Read first:** Section 8.1 source and tests, plus current representative YAML.

**Required claims:**

- declarative specification is a typed object graph;
- `Scheme` organizes experiments and a model library;
- measured data and explicit parameter values enter separately;
- elements are reusable scientific matrix contributions;
- data models are per-dataset specifications;
- references and extensions are resolved and validated before numerical use.

**Forbidden shortcuts:**

- no “model compiler” metaphor;
- no claim that YAML itself is the architecture;
- no current “megacomplex” or “dataset group” terminology;
- no exhaustive list of fields.

**Acceptance:** the prose answers who owns, references, and produces what; every Figure 2 edge has evidence.

### Packet C — Data, parameters, and mathematics

**Produces:** Sections 9.6-9.7, Figure 3, Table 3, and the equation set; 2,150-2,400 words.

**Read first:** Sections 8.2-8.3 source and tests; variable-projection sections of the 2004 and TIMP papers.

**Required claims:**

- measured arrays and data models are distinct;
- labeled dimensions are converted into model/global numerical organization;
- explicit parameters and CLPs are distinct;
- element matrices expose conditional linearity to shared estimation machinery;
- inner CLP estimation and outer least squares form a nested workflow;
- weighting, scales, relations, constraints, and penalties occur at verified points.

**Forbidden shortcuts:**

- never say all entries in `Parameters` are intrinsically nonlinear;
- never say CLPs are stored in `Parameters`;
- never identify model dimension with time or global dimension with wavelength without “commonly” or a concrete example;
- never claim the Python variable-projection routine is TIMP's partitioned algorithm unless code proves this.

**Acceptance:** notation is consistent; each symbol maps to a runtime concept; a reader can explain why the inner solve exists.

### Packet D — Lifecycle, results, and provenance

**Produces:** Sections 9.8-9.9 and Figure 4; 1,400-1,600 words.

**Read first:** `scheme.py`, all core optimization orchestration files, `result.py`, result classes, and focused tests.

**Required claims:**

- distinguish initialization, repeated objective evaluation, and post-optimization result construction;
- trace data, explicit parameters, matrices, CLPs, residuals, optimizer output, diagnostics, and result datasets;
- explain why rich results support validation and reproducibility;
- identify element provenance without claiming more than stored metadata supports.

**Forbidden shortcuts:**

- do not say all matrices are prepared once;
- do not portray validation as automated proof of the physicochemical model;
- do not assign plotting to core.

**Acceptance:** ordering matches source; result field claims have implementation anchors.

### Packet E — Extensions, ecosystem, and evaluation

**Produces:** Sections 9.10-9.11, Figure 5, and Table 4; 1,000-1,200 words.

**Read first:** Section 8.4 source/tests, built-in element registration, and relevant sections of the 2023 paper.

**Required claims:**

- element, data-I/O, and project-I/O extensions have distinct contracts;
- entry points and registries mediate discovery and naming;
- element plugins can affect typed declarative capabilities;
- simulation reuses relevant core mechanisms;
- examples, extras, notebooks, and numerical libraries occupy different ecosystem roles;
- discuss verified trade-offs.

**Forbidden shortcuts:**

- do not use “microkernel,” “ports and adapters,” or another named pattern as fact unless the project uses that term; it may be presented as an interpretive analogy;
- do not promise binary compatibility, semantic-version guarantees, or future plugin stability;
- do not invent performance claims.

**Acceptance:** at least four trade-offs are explained as paired benefits and costs, not a list of weaknesses.

### Packet F — Synthesis and copy edit

**Produces:** the assembled chapter, final transitions, conclusion, captions, APA reference list, and word-count report.

**Inputs:** all accepted packets, figures, tables, and completed ledger.

**Actions:**

- remove overlap, especially repeated explanations of the object graph and nested optimization;
- ensure scientific terminology appears before implementation names;
- normalize notation and capitalization;
- replace `[VERIFY]` markers only from evidence;
- check the word ceiling;
- list unresolved issues in review notes.

**Acceptance:** all global quality gates in Section 14 pass.

## 13. Instructions and guardrails for GPT-5.6 Luna

Give Luna these rules verbatim or preserve their force:

1. **Evidence before prose.** For each subsection, write a private bullet list of claims and evidence-ledger IDs before writing paragraphs.
2. **Source code leads architectural terminology.** A term in a paper or docstring is not current merely because it sounds plausible.
3. **Literature leads scientific terminology.** Use the supplied papers for definitions of global analysis, target analysis, separability, model discovery, and validation.
4. **Distinguish description from interpretation.** If the code does not name a design pattern, frame it as a useful interpretation rather than project terminology.
5. **No compilation metaphor.** Say “instantiate,” “resolve,” “bind,” “validate,” “construct,” “realize,” or “evaluate,” according to the observed operation.
6. **No future invention.** The chapter may explain why concepts are likely to be durable, but it must not promise v1 names, compatibility, roadmap features, or performance.
7. **No stale vocabulary.** `Element` and `Experiment` are current. Use `megacomplex`, dataset group, and old CLP-linking APIs only in explicitly historical passages.
8. **Keep data concepts separate.** A `DataModel` configures a dataset; an xarray object contains measured data; an experiment coordinates one or more dataset specifications; numerical wrappers prepare data for estimation.
9. **Keep unknowns separate.** `Parameters` contains explicit parameters. CLPs are inner estimated coefficients represented through matrix labels, estimators, decompositions, and results.
10. **Qualify scientific equivalence.** An explicit outer parameter is often intrinsically nonlinear, but the software distinction is how it participates in computation.
11. **Use dimensions carefully.** “Model” and “global” dimensions are general coordinate roles, not fixed physical quantities.
12. **Treat notebooks correctly.** Jupyter is a user environment around the package, not an internal pyglotaran architectural component.
13. **Treat results as scientific evidence structures.** Explain decompositions and residuals, but do not claim the software establishes scientific truth.
14. **Prefer paragraphs over catalogs.** Class and field lists belong in tables only when they clarify a responsibility boundary.
15. **Use original diagrams.** Do not reproduce paper figures or closely imitate their graphic composition.
16. **Use APA consistently.** Author-date in text; sentence case in reference titles; italic journal and volume; DOI as an HTTPS URL.
17. **Avoid direct quotations.** Paraphrase with citation. If a short quotation is indispensable, include an APA page number.
18. **Expose uncertainty.** Insert `[VERIFY: precise question and likely source]`; never fill a gap with a generic software-architecture claim.
19. **Protect the user's workspace.** Read broadly but modify only the planned documentation artifacts. Do not reset, format, or “clean up” source repositories.
20. **Stay within budget.** Stop adding detail when it does not help answer one of the fourteen architectural questions in Section 7.

### Recommended packet prompt template

```text
You are drafting Packet [letter] of an academic chapter on the staging
architecture of pyglotaran. Read the handoff and current evidence ledger
first. Then inspect only the named source, tests, examples, and literature.

Before drafting, add claim/evidence rows to the ledger. Write [named
sections] in [word range] words. Use the terminology contract and APA
author-date citations. Organize the explanation around responsibilities,
invariants, and information flow; current class names are implementation
anchors, not the outline.

Do not guess. Leave [VERIFY: ...] for unresolved facts. Do not use
"model compilation," current "megacomplex," current "dataset group," or
place CLPs inside Parameters. Do not make v1 promises.

Return:
1. ledger additions;
2. draft prose;
3. figure/table source if required;
4. a five-item self-check against this packet's acceptance criteria.
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

### 14.6 Editorial and format quality

- [ ] Chapter body and captions are 8,000-9,200 words and below 10,000.
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

1. the complete draft exists and is below 10,000 words;
2. the source-led terminology contract is followed throughout;
3. the scientific framing and lineage are supported by APA citations;
4. the static object graph, semantic-resolution path, numerical-estimation path, result path, and extension boundaries are all explained;
5. the equations are consistent with both the literature and the staging execution path;
6. the evidence ledger supports all consequential architectural claims;
7. focused tests have been run or a precise reason for not running them is recorded;
8. all figures are original and verified against source;
9. uncertainties are visible in review notes instead of hidden in prose; and
10. a pyglotaran maintainer can review the chapter by following claim IDs to a small, relevant source set rather than rereading the entire repository.

The most important success criterion is not exhaustive API coverage. It is that a graduate-level reader can explain why the architecture has its present separations, how an analysis moves through them, and how those separations support the scientific cycle of model specification, parameter estimation, and validation.
