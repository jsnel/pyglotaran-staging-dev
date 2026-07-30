# 6. Extending the framework and evaluating its trade-offs

## 6.1 Registered extension surfaces

A common optimizer is useful only if new scientific contributions and file formats can
enter through explicit boundaries. Otherwise, adding a new kinetic contribution or
measurement format would require edits throughout data handling, estimation, and result
construction. Pyglotaran addresses this problem with separate registries: directories
that connect a name to an available implementation. The inspected staging code maintains
one registry for Element classes, one for measured-data input/output (I/O), and one for
project-level I/O. These are related mechanisms, not a single unrestricted plugin API.

Installed packages advertise providers through **entry points**, metadata that identifies
Python modules to load for a named extension group. When pyglotaran is imported, its
loader inspects three groups—for Elements, data I/O, and project I/O—and imports the
declared provider modules. Registration code in those modules then adds implementations
to the appropriate directory. The built-in distribution uses the same mechanism for
scientifically different Elements such as kinetics, baseline, spectral contributions,
coherent artifacts, and damped oscillations, as well as several data and project formats.
Entry-point discovery therefore determines what is available; it does not replace the
typed responsibilities each provider must implement.

A scientific Element provider supplies a subclass that can calculate a labeled matrix
contribution and create its contribution-specific result dataset. It may also declare a
specialized DataModel type. When a serialized dataset specification refers to Elements,
the package combines the corresponding contributed DataModel capabilities into the typed
per-dataset object. A new scientific contribution can thus add both numerical behavior
and the configuration needed to describe it, while the central optimization path
continues to work through matrices, coefficient labels, residuals, and Element results.
This boundary is narrower than allowing an extension to substitute arbitrary optimizer
behavior.

The two I/O surfaces answer different questions. A data-I/O provider translates a
measurement file into or out of an xarray `Dataset` or `DataArray`. A project-I/O provider
loads or saves `Parameters`, Schemes, and Results. Their base interfaces allow a provider
to implement only the operations its format supports, while the public dispatch
functions select a registered format, pass through format-specific options, protect
against accidental overwriting where applicable, and update verified source-path
metadata. Keeping these registries separate prevents a provider for a scientific array
format from implicitly becoming responsible for serializing a complete analysis.

Each registered implementation has a convenient short access name and a **fully
qualified name**, the complete module-and-class path that distinguishes providers even
when they request the same short name. In the inspected registry, the first provider
keeps an occupied short binding; a conflicting provider is retained under its full name
and a warning explains how to choose it explicitly. **Pinning** is this deliberate
rebinding of a short name to a registered fully qualified provider through the appropriate
`set_*_plugin` function. It provides an explicit response to the ambiguity, although it
does not constitute a promise that third-party implementations will remain compatible
with future releases.

Registered typing also reaches editor support. The JSON-schema utility constructs a
Scheme schema together with a generated DataModel schema based on DataModel subclasses
loaded in the current process. If explicit parameters are supplied, their labels can be
inserted as allowed references. This **generated schema** can help an editor offer
completion and detect some malformed declarations. It reflects currently loaded types;
it is not an independent model language and does not eliminate runtime reference
resolution or scientific issue checking.

**Table 4. Extension surfaces in the inspected staging implementation**

| Registry or interface | Extension supplies | Core-side behavior in inspected staging | Resulting capability |
|---|---|---|---|
| Element registry and `Element` contract | A typed Element class; matrix calculation; contribution-specific result creation; optionally a specialized DataModel type | Resolves the registered type, incorporates contributed dataset fields, composes its matrix through the common numerical path, and adds Element identity to its result dataset | Additional scientific contributions can use the shared optimization and result lifecycle |
| Data-I/O registry and `DataIoInterface` | Load and/or save behavior for one or more measurement-data format names | Dispatches by registered or inferred format, exchanges xarray labeled arrays, and records source path and provider identity on loaded data | Additional measured-data formats can enter without changing scientific Elements |
| Project-I/O registry and `ProjectIoInterface` | Load and/or save behavior for Parameters, Schemes, and Results | Dispatches analysis-object persistence, applies overwrite checks, and updates supported source paths | Additional declarative and result formats can represent a related analysis artifact set |

<!-- Insert Mermaid source from ../figures/fig-06-extension-boundaries.mmd here. -->

**Figure 6. Registered extension and surrounding ecosystem boundaries.** Solid arrows
show registration, use, or data flow as labeled; dotted arrows show provider discovery
through installation metadata. The three registries mediate different contracts.
Numerical libraries, notebooks, examples, and extras surround the core rather than
registering alternative outer optimizers.

Table 4 and Figure 6 show the same separation at two levels. The table states what a
provider supplies and what the core does with it. The figure adds discovery and the
external scientific environment. Extensions therefore participate by satisfying a
specific boundary, while matrix realization, nested estimation, and result assembly
remain common services.

## 6.2 Simulation and the surrounding scientific ecosystem

The same scientific definitions can be useful before fitting, when generating expected
observations, and after fitting, when inspecting them with external tools. Here,
**simulation** means generating calculated labeled data from a DataModel, explicit
parameters, coordinates, and either supplied CLPs or a global Element contribution. The
current `simulate(...)` function resolves the DataModel, determines the model and global
coordinate roles, constructs `OptimizationMatrix` objects, and combines the matrices
with CLPs. It therefore reuses reference resolution and matrix construction from the
analysis architecture but does not invoke the outer least-squares optimizer. For the
running example, simulation can generate a time-by-wavelength surface from chosen
temporal shapes and spectra before measured data are fitted.

Several general-purpose libraries provide foundations beneath this path. xarray carries
labeled observations, coordinates, and result arrays. NumPy supplies array operations.
SciPy supplies the outer least-squares routine, the supported non-negative least-squares
solver, and linear-algebra functions used by numerical components. Numba is used in
selected built-in matrix kernels. These libraries provide numerical capabilities; the
scientific meaning of a rate, spectrum, instrument response, or coefficient relation
comes from the pyglotaran specification and Element implementations.

The surrounding **ecosystem** consists of tools and repositories that cooperate with the
core without belonging to its optimizer. Jupyter notebooks can coordinate loading,
analysis calls, explanatory text, and plots in one external working document, a role
emphasized in the published problem-solving-environment account of pyglotaran
(van Stokkum et al., 2023). The `pyglotaran-examples` repository supplies notebook case
studies and current compositions, including fluorescence, transient-absorption,
multi-dataset, and damped-oscillation analyses. Such examples establish intended usage at
the user boundary but do not prove internal runtime behavior. `pyglotaran-extras`
separately supplies plotting and higher-level exploration conveniences. The boundary is
therefore functional: core constructs scientific results; notebooks organize a workflow;
examples demonstrate one; and extras helps inspect it.

## 6.3 Verified trade-offs

Separating responsibilities controls one kind of complexity by making other coordination
work explicit. A **trade-off** is such a paired consequence: an architectural choice
provides a capability while imposing work or constraints elsewhere. The pairs below are
interpretations of the inspected mechanisms, not performance claims.

First, a declarative network of reusable Elements and dataset specifications makes shared
scientific structure inspectable and avoids repeating definitions. The corresponding
cost is that names must be connected to typed objects, extension chains and parameter
references must be resolved, and supported issues must be checked before numerical work
begins.

Second, plugin-contributed typing lets a scientific extension add configuration fields
alongside matrix behavior. It also means that the available schema depends on the types
loaded in the process. Short names improve readability, but multiple installed providers
can claim the same name, requiring warnings, fully qualified identities, and explicit
pinning.

Third, the separation of explicit outer parameters from CLPs lets heterogeneous
contributions share the nested estimation machinery. The cost is an interface constraint:
an Element must expose its contribution as a compatible labeled matrix so that the inner
coefficient problem remains visible to the common runtime.

Fourth, labeled arrays preserve the meaning of coordinates in observations and results.
At the numerical boundary, however, dimensions still have to be inferred or declared,
oriented consistently, sliced, and—where multiple datasets are linked—aligned according
to configured rules. Labels reduce one source of ambiguity but do not remove numerical
coordination.

Fifth, structured residuals, decompositions, diagnostics, paths, and contribution results
give a researcher more evidence for validation than a final parameter vector would.
Their nested mappings, optional fields, and configurable persistence make the result
structure correspondingly more complex. Consumers must account for what was retained
under the selected saving policy.

Finally, notebook-centered work can combine code, narrative, and many Python tools
without placing an interactive environment inside the optimizer. It does not reproduce
every guided affordance of the historical dedicated desktop interface, and reproducible
use still depends on disciplined recording of inputs and software context. This is a
workflow consequence, not evidence that one interface is universally preferable.

These paired effects provide the evidence needed for the chapter's final synthesis. The
conclusion can now assess whether the separations, taken together, support the cycle of
scientific specification, estimation, inspection, and revision established at the
outset.

<!--
Citations used:
- van Stokkum et al. (2023), used only for the notebook-centered problem-solving-environment rationale and not as authority for current staging classes, syntax, registries, or runtime behavior.

Incoming bridge proposal:
Section 5 should close by noting that reusable, contribution-aware result construction depends on common extension contracts.
This section begins with the practical question of adding scientific contributions or file formats without replacing the common optimizer.

Outgoing bridge proposal:
This section ends after evaluating paired benefits and coordination costs, without deciding the chapter's central thesis.
The coordinator's conclusion can integrate those trade-offs with the scientific model-discovery cycle.

Five-item self-check:
1. Registries and entry points are explained in ordinary language before implementation names.
2. Element, data-I/O, and project-I/O contracts remain distinct, and Table 4 contains no undifferentiated plugin claim.
3. Short/full names, conflict behavior, pinning, contributed DataModel typing, and schema generation are limited to verified behavior.
4. Simulation reuse and the roles of numerical libraries, notebooks, examples, and extras respect the core/ecosystem boundary.
5. Six trade-offs are paired and evidence-backed; no compatibility, v1, performance, or architecture-pattern promise is made.

Integration note:
- Assumptions: Registry behavior is described only for the inspected staging revision. “Generated schema” is preferred over an implication that schemas are a stable plugin ABI.
- Deliberate omissions: Built-in providers are examples of heterogeneity, not a catalog. Planned compatibility tooling, agent skills, plugin roadmaps, and future-v1 behavior are outside scope.
- Dependencies: The coordinator should embed `fig-06-extension-boundaries.mmd` at the marker. Cross-packet trade-offs depend on AR evidence for declarative resolution, DP/NM evidence for labels and the outer/CLP boundary, and RR evidence for result complexity.
- Proposed contract changes: None.
- Unresolved questions: None affecting the section. No `[VERIFY]` marker remains in prose or this packet's extension claims.
-->

