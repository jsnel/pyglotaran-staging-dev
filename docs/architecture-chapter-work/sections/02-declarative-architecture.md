# 2. Separating scientific definitions from execution

## 2.1 Why divide the package into responsibilities?

A researcher needs to change a scientific hypothesis without rebuilding data loading,
optimization, and result inspection for every new contribution. In the running example, a
first analysis might describe two independent temporal decays. A later analysis might replace
them with states connected by a kinetic scheme, add an instrument-response contribution, or
analyze a second measurement jointly. These changes alter the scientific explanation, but
they do not remove the need to associate labeled observations, estimate unknown quantities,
and inspect residuals. An architecture that couples all of those tasks in one procedure would
make every scientific revision a software revision.

Pyglotaran addresses this composition problem by letting the researcher state *what* belongs
to an analysis separately from the changing numerical state of one fit. Such a
*declarative specification* records named scientific definitions and their relationships
without prescribing a line-by-line execution sequence. It can be inspected or serialized
before measurements and current parameter values are supplied. The distinction is not
absolute isolation: an in-memory dataset specification can hold a data-source association or
a loaded array. The important separation is one of meaning and responsibility. A definition
of which contributions apply to a dataset is not the same thing as the observed values, and
a parameter label in that definition is not the same thing as its current fitted value.

Named definitions also permit reuse. A kinetic contribution can be defined once in a model
library and referenced by several dataset specifications. An experiment can coordinate
several such datasets without duplicating the shared definition. Current global- and
target-analysis examples use the same overall structure—library, experiments, datasets, and
element references—while changing the scientific definitions and restrictions inside it.
Global and target analysis are therefore compositions of scientific structure, not separate
architecture roots or separate optimizer modes. This staging observation is consistent with
the earlier published rationale for modular, reusable model definitions, while the present
source supplies the authoritative names and relationships (van Stokkum et al., 2023).

Reuse requires a common boundary between scientific contributions and numerical machinery.
In the inspected implementation, different `Element` types implement a shared responsibility:
given a resolved per-dataset specification and relevant coordinates, they can provide labeled
matrix content; they can also construct contribution-specific result data. Section 4 explains
how these contributions are combined numerically, and Section 5 explains result creation. At
this point, the architectural consequence is enough: the central estimator can depend on a
common contribution contract rather than on the internal scientific fields of every kinetic,
spectral, or instrumental component.

The same division locates the package within a wider scientific environment. Core
pyglotaran owns typed analysis specifications, explicit-parameter handling, reference
binding, numerical realization, optimization, simulation, results, and extension registries.
NumPy, SciPy, xarray, and related libraries supply numerical and labeled-array foundations.
The `pyglotaran-examples` repository demonstrates complete analyses.
`pyglotaran-extras` is a separate package whose stated purpose is supplementary plotting and
higher-level exploration. Notebooks can coordinate these tools and combine calculations with
scientific narrative, but Jupyter remains an external working environment rather than an
internal optimizer component.

These boundaries make scientific definitions more reusable and the specification more
inspectable, but they move complexity into coordination. Labels must be connected to the
objects and parameters they denote; compatible contribution types must be determined; and
incoherent combinations should be reported before numerical estimation. The motivations
therefore become concrete in the network of owned objects and named references rooted at the
analysis specification.

## 2.2 A network of connected scientific definitions

Before a fit can run, the package needs a coherent description of what is shared, what
belongs to one experiment or dataset, and which scientific contributions each dataset uses.
The ordinary idea is a network of named definitions and references. In software terminology,
this is an *object graph*: objects are the nodes, while ownership and reference relationships
are the edges. A YAML document or Python dictionary can describe the network, but it is only
one serialized representation. The running program instantiates typed objects whose
responsibilities and validity rules are not conveyed by indentation alone.

The root of this graph is the analysis specification represented by `Scheme`. Its principal
structural fields are a mapping of experiments and a `ModelLibrary`. The root gives these
parts a common scope and supplies the user-facing optimization entry point, but it is not a
universal container for measured arrays and current parameter values. This narrow meaning is
important: a scheme declares the analysis structure, while a particular fit also needs
runtime inputs.

The model library owns scientific definitions by label. Each value is a typed `Element`, so
a short name such as `parallel` or `target` can refer to a complete contribution definition.
Labels allow the same definition to be referenced without copying its fields into every
dataset specification. Some element types also support library-level extension: a new
definition names one or more existing definitions and supplies additions or overrides.
This relationship composes scientific configurations. It is distinct from Python class
inheritance, which relates software types rather than user-defined scientific instances.

An experiment is the joint-analysis boundary represented by `ExperimentModel`. It owns a
labeled mapping of one or more dataset specifications and holds configuration that applies
to their coordinated analysis. The name *Experiment* is architectural: it need not imply
that every contained array was acquired in one physical run. It says that the dataset
specifications are intended to participate in one joint analysis. The mechanics for aligning
and linking several measured arrays are deferred to Section 3.

Each entry in the experiment's dataset mapping is a `DataModel`. Despite the familiar word
*data*, this object is a per-dataset scientific specification, not the measured numerical
array. It identifies ordinary `elements`, may identify `global_elements`, and can contain
typed settings contributed by those elements, together with scales, weights, and a data
source association. The scientific meanings of dimensions, weights, and scales belong to
Section 3. Here the key point is that the object describes how one labeled dataset is to be
modeled.

The source implements a useful but easily misunderstood nuance at this boundary.
`DataModel.data` is excluded from ordinary serialization and can contain a source string or
a loaded xarray dataset. When `Scheme.optimize(...)` is called, the separately supplied
dataset mapping is loaded or normalized and associated with matching data models before the
optimization object is created. In addition, `Scheme.from_dict(...)` can immediately load a
string data reference found in a serialized dataset specification. It would therefore be too
strong to claim that specification objects can never point to measured arrays. The accurate
distinction is semantic: the `DataModel` says how a dataset participates in the analysis,
whereas the xarray object contains its labeled observed values.

An `Element` is the smallest common scientific contribution in this graph. Its concrete type
determines which scientific fields it carries, while its shared interface allows the
numerical path to ask for labeled matrix content and later for element-specific result data.
An element can also declare additional fields required in a compatible data model. This
allows heterogeneous contributions to extend the scientific vocabulary while retaining one
dataset-specification boundary. The term describes a software role; it does not imply that
one element necessarily equals one physical species or one uniquely identifiable process.

Measured arrays and explicit parameter values stand beside this declarative graph. The
method `Scheme.optimize(parameters, datasets, ...)` requires both as arguments. Measured
arrays are matched to dataset labels, while named explicit parameters are connected to
parameter-bearing fields during resolution. Section 3 defines the computational categories
of explicit parameters and conditionally linear parameters. For the static graph, the
important invariant is that `Parameters` holds the former and does not contain the latter.

<!-- Insert Mermaid source from ../figures/fig-03-object-graph.mmd here. -->

**Figure 3. Static analysis object graph and separately supplied runtime inputs.** Solid
arrows denote ownership, dashed arrows denote a stored name or scientific reference, and
thick arrows denote association or binding at the fit boundary. A data-source association
does not make the per-dataset specification identical to the measured array.

Figure 3 separates three relationships that can look alike in serialized text. A `Scheme`
owns its library and experiment mapping; an experiment in turn owns dataset specifications,
and the library owns elements by label. A data model normally refers to elements by their
library labels rather than owning copies. At fitting time, the dataset mapping and explicit
parameter collection arrive through the invocation boundary. Conflating these edges would
hide whether a value is reusable definition, per-dataset configuration, or changing runtime
state.

Table 2 summarizes the same graph by responsibility. “Produces or enables” describes the
next architectural boundary rather than claiming that every entity independently performs a
fit.

**Table 2. Core entities and responsibilities in the inspected staging architecture**

| Entity | Owns | References | Produces or enables | Invariant or boundary |
|---|---|---|---|---|
| Analysis root (`Scheme`) | Experiment mapping; model library | Optional source path | Typed construction and the fitting entry point | Its structural graph does not replace separately supplied datasets and parameter values |
| Model library (`ModelLibrary`) | Elements keyed by label | Other library labels in supported extension chains | Reusable, extension-resolved element definitions | Cyclic extension chains are rejected during library construction |
| Experiment (`ExperimentModel`) | Dataset specifications and joint-analysis configuration | Parameter labels in applicable settings | A resolved copy for one joint numerical objective | Every dataset label maps to a per-dataset specification |
| Data model (`DataModel`) | Per-dataset scientific configuration and optional data association | Ordinary and optional global element labels; parameter labels | A typed, resolved dataset specification | It is not the measured xarray dataset |
| Element (`Element`) | Contribution-specific scientific fields and constraints | Explicit parameter labels and, for extendable types, library labels | Labeled matrix content and element-specific result data | Concrete types implement the common contribution and result interfaces |
| Measured data | Labeled observed values and coordinates | Dataset label/source metadata | Numerical observations once associated | Supplied or loaded separately from the scheme's structural fields |
| Explicit parameter collection (`Parameters`) | Named explicit parameter objects and metadata | Expression dependencies among parameters | Current values for bound parameter fields | It contains explicit parameters, not conditionally linear coefficients |

The table also exposes why no directory listing can explain the architecture. Responsibilities
cross module boundaries: typed construction, library composition, item-field inspection, and
optimization initialization cooperate to turn the graph into a coherent runtime input. The
next question is therefore not where a class file resides, but how a human-readable name is
connected to what it denotes.

## 2.3 Connecting names and checking meaning

Human-readable labels are useful only if the runtime can connect each one unambiguously and
report incoherent relationships. The first step is *typed instantiation*: constructing an
object whose concrete type determines its allowed fields and behavior. Library entries carry
a `type` discriminator. The staging type machinery builds the permitted union from
registered element classes, and Pydantic uses the discriminator to instantiate the matching
class. `Scheme.from_dict(...)` then constructs the library, constructs each experiment, and
constructs each dataset specification in that library context.

The library context matters because an element type can contribute a specialized
`DataModel` subtype. `DataModel.from_dict(...)` examines the classes of the referenced
ordinary and global elements, collects any declared data-model types, and creates a
compatible combined subtype before validating the dataset mapping. Focused tests demonstrate
that a dataset referencing such an element receives the contributed subtype, whether the
element appears as an ordinary or global contribution. Section 6 explains how installation
and registries supply extension types; here the relevant fact is that extensibility changes
the typed declarative vocabulary without changing the role of a data model.

Library extension labels are connected during `ModelLibrary` construction. The
implementation repeatedly selects definitions whose dependencies have already been
resolved, combines their parent definitions with the local definition, and stores the
result under the local label. A focused scheme test exercises a nested extension and checks
that inherited entries, local additions, and an override are present. If a pass through the
remaining definitions makes no progress, the library raises a cyclic-dependency error. This
is reference-based composition among element instances, not inheritance among Python
classes.

Execution requires a second kind of connection. *Reference resolution*, or *binding*, means
connecting a stored name to the element or explicit parameter it denotes. An experiment's
`resolve(...)` method creates a copy, resolves each dataset, and resolves experiment-level
parameter-bearing items. `resolve_data_model(...)` replaces element-label strings with the
corresponding library objects and recursively binds parameter-bearing fields. Returning
copies preserves the reusable declarations while giving numerical initialization an object
whose references point to current runtime objects.

Parameter binding also limits which explicit parameters participate. `Optimization`
initializes an empty `Parameters` collection and resolves the experiments against the
collection supplied by the caller. When a parameter label is encountered, the named
parameter is copied into the optimization collection. Expression dependencies are added
recursively so that a referenced expression remains meaningful. Focused tests verify both
copying and dependency-aware selection. This is not yet the distinction between free outer
values and other explicit parameters—that belongs to Section 3—but it explains why the
analysis need not carry every unrelated entry from a larger parameter file.

Typed construction and binding can reveal several kinds of incoherence. Pydantic enforces
declared field types and forbids unexpected fields on the principal models. The item
inspection helpers record missing parameter labels, while data-model checks can report
violations of element exclusivity or uniqueness rules. Optimization gathers the supported
issues after experiment resolution and raises before constructing numerical objectives when
the list is nonempty. Extension cycles are rejected earlier during library construction.
The wording must remain scoped: these checks establish supported structural and semantic
conditions; they do not prove that a physicochemical model is scientifically adequate, and
the source does not promise that every possible invalid relationship has a dedicated error
type.

After these operations, names have types and referents, but there is still no fixed numerical
matrix. Element matrix calculation requires measured coordinates and current parameter
values. Data orientation, alignment, and parameter roles are established in Sections 3–4,
and parameter-dependent matrices are evaluated along the numerical path. Reference
resolution therefore makes the scientific specification coherent without prematurely
turning it into one immutable numerical object.

Table 1 consolidates terms that otherwise invite category errors. Scientific concepts lead
the descriptions; current classes serve as implementation anchors rather than definitions
of the science.

**Table 1. Terminology concordance**

| Scientific or architectural term | Meaning in this chapter | Current implementation anchor | Common confusion to avoid |
|---|---|---|---|
| Physicochemical model | Hypothesis about states, kinetics, spectra, instrument effects, and related physical structure | Realized through configured elements and relationships | It is narrower than the complete model for the observations |
| Model for the observations | Physicochemical and measurement assumptions, data organization, and unexplained-variation description used to predict observations | Spans data models, elements, numerical transformations, and residual construction | It is not one Python object |
| Analysis specification | Declarative network of experiments and reusable scientific definitions | Rooted in `Scheme` | It does not by itself replace measured arrays and current parameter values |
| Model library | Named reusable contribution definitions and supported extension relationships | `ModelLibrary` | It is more than a YAML dictionary |
| Element | Composable scientific contribution with a common matrix-related contract | `Element` subclasses | It need not correspond one-to-one with a physical species |
| Experiment | Joint-analysis grouping of one or more dataset specifications | `ExperimentModel` | It is not an array axis or necessarily one acquisition event |
| Data model | Per-dataset scientific specification and data association | `DataModel` or an element-contributed subtype | It is not the measured xarray object |
| Measured data | Labeled observed values and coordinates | Usually an xarray dataset supplied or loaded separately | It does not define which scientific contributions apply |
| Reference resolution | Connecting a name to the element or explicit parameter it denotes and checking supported issues | `ExperimentModel.resolve`, `resolve_data_model`, and item helpers | It does not construct a permanent numerical matrix |

The specification is now typed, connected, and checked at the level supported by the
current implementation. The next boundary gives labeled observations and the two distinct
kinds of unknowns their numerical roles.

<!--
Citations used:
- van Stokkum et al. (2023), used for the historical declarative/reuse rationale and ecosystem context, not for current staging class names.

Incoming bridge proposal:
Section 1 should close by identifying reusable, inspectable scientific composition as the architectural response to iterative model discovery.
This section then asks how the package separates those responsibilities before any numerical estimator is introduced.

Outgoing bridge proposal:
This section establishes ownership, named references, typed instantiation, binding, and validation while stopping before numerical realization.
Section 3 can begin with the measured-array/DataModel boundary and then define coordinate roles and the two computational kinds of unknowns.

Five-item self-check:
1. The prose motivates responsibility boundaries before introducing current class names.
2. Scheme, model library, Experiment, DataModel, Element, measured data, and Parameters have distinct roles, and every Figure 3 edge is supported by AR ledger entries.
3. Typed instantiation, extension resolution, parameter binding, and supported issue validation are described without implying a fixed matrix is constructed.
4. Tables 1–2 are embedded, concept-led, and do not become exhaustive field catalogs.
5. Current terms are used throughout; staging behavior is qualified, and no v1, performance, compatibility, or universal-validation claim is made.

Integration note:
- Assumptions: Class names are implementation anchors at revision `468c4cd57aaf25c10edf85cd197df771bad0a766`; conceptual responsibilities should survive later renaming.
- Deliberate omissions: Labeled-array orientation, weights/scales, alignment/linking, parameter categories, estimator mathematics, lifecycle timing, result fields, and plugin discovery mechanics are deferred to their owning sections.
- Dependencies: The coordinator should embed `fig-03-object-graph.mmd` at the marker. Section 3 must preserve the semantic distinction between DataModel and measured data and define explicit parameters versus CLPs.
- Proposed contract changes: Correct the handoff's obsolete `ModelLibrary.resolve` anchor in future planning documents. Current staging resolves extendable-element chains inside `ModelLibrary.__init__`; shared frozen files were not edited.
- Unresolved questions: None affecting prose. Transitional old-name docstrings and test/support remnants remain in the repository; they are maintenance-review items, not current terminology evidence.
-->
