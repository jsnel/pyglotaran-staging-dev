# Maintainer uncertainties in the frozen staging implementation

Scope: static inspection of pyglotaran revision `468c4cd57aaf25c10edf85cd197df771bad0a766`, under the frozen editorial contract. No tests were run. The observations below are implemented facts or source-backed implications, not claims of maintainer intent.

## 1. Result keys are flattened across experiments

**Finding.** A `Scheme` owns a mapping of experiments, but optimization passes only the experiment values into one `Optimization` (`pyglotaran/glotaran/project/scheme.py:29–33,90–105`). Each objective returns a mapping keyed by dataset label (`pyglotaran/glotaran/optimization/objective.py:499–503,760–764,792–805`), and `Optimization.run()` combines those mappings into one `dict` through `ChainMap` (`pyglotaran/glotaran/optimization/optimization.py:137–153`). The adjacent TODO explicitly calls out multiple experiments with the same dataset name (`optimization.py:137`). `Result.optimization_results` is correspondingly a single dataset-keyed mapping, not an experiment-nested mapping (`pyglotaran/glotaran/project/result.py:55–75`). Thus equal dataset labels in different experiments cannot both remain independently addressable in the result; no collision validation is visible on this path.

**Confidence:** High — direct result-construction control flow plus an explicit TODO.

**Chapter impact:** Describe results as flattened by dataset label in the inspected implementation and avoid claiming either per-experiment nesting or collision safety. If examples use several experiments, qualify that the current path assumes scheme-wide-unique dataset labels.

**Neutral maintainer-review wording:** “Are dataset labels intended to be unique across all experiments in a `Scheme`? If so, should that invariant be validated; if not, should result keys retain or encode the experiment identity?”

## 2. `OptimizationInfo.success` does not report optimizer convergence

**Finding.** `Optimization.run()` leaves `ls_result` as `None` only when `least_squares` raises; otherwise it retains the returned object and separately copies its message (`pyglotaran/glotaran/optimization/optimization.py:113–135`). `OptimizationInfo.from_least_squares_result()` then sets `success = result is not None` and never reads the returned object's `success` or `status` fields (`pyglotaran/glotaran/optimization/info.py:137–187`). In this implementation, `OptimizationInfo.success` therefore means that the optimizer call returned a result object rather than being caught as an exception; it is not the optimizer's own convergence-success flag.

**Confidence:** High — the Boolean assignment is explicit.

**Chapter impact:** Do not equate this field with numerical convergence. Safe wording is that it records completion without a caught exception, while `termination_reason` carries the returned or caught message.

**Neutral maintainer-review wording:** “Should `OptimizationInfo.success` mirror `OptimizeResult.success`, or is its intended meaning ‘the optimizer returned without raising’? The field docstring could state whichever semantic is intended.”

## 3. `glotaran_version` is recomputed when a result is loaded

**Finding.** `OptimizationInfo.glotaran_version` is a computed property that imports and returns the currently running package's `__version__` (`pyglotaran/glotaran/optimization/info.py:98–105`). Before validation, any serialized `glotaran_version` value is removed (`info.py:128–135`). A saved value can therefore describe the writer at serialization time, but after deserialization the object reports the reader's current version; it is not immutable creation provenance despite the property docstring.

**Confidence:** High — the computed property and input-field removal are explicit.

**Chapter impact:** Do not present this field as preserved creation provenance. State only that serialization exposes a computed package-version field, with the important qualification that loading recomputes it.

**Neutral maintainer-review wording:** “Should the creation-time pyglotaran version be stored as an ordinary immutable field while a separate field reports the current reader version?”

## 4. Result SVD variables are calculated but not exposed

**Finding.** `add_svd_to_result_dataset()` adds data and residual singular vectors and values to a local `xr.Dataset` (`pyglotaran/glotaran/optimization/objective.py:52–65`). All three result-building paths call it (`objective.py:673,749,901`), but then construct `OptimizationResult` from only the dataset's `data` and `residual` variables plus element, activation, and fit-decomposition fields (`objective.py:674–688,752–758,921–927`). `OptimizationResult` itself declares no SVD field (`objective.py:145–153`). Separately, `Scheme.optimize(add_svd=...)` passes the option into `Optimization` (`pyglotaran/glotaran/project/scheme.py:68–103`), where it is assigned to `_add_svd` (`pyglotaran/glotaran/optimization/optimization.py:51–85`) but is not consulted by result construction in the frozen tree. The added SVD variables are therefore transient rather than retained or exposed through `OptimizationResult`.

**Confidence:** High — all result branches and the result schema agree.

**Chapter impact:** Do not list SVD arrays among retained core result quantities. Distinguish the retained `FitDecomposition` (`clp` and `matrix`) from the transient SVD calculation.

**Neutral maintainer-review wording:** “Is `add_svd` intended to gate SVD calculation and retain those arrays in `OptimizationResult`, or should the currently unconditional, transient calculation be removed?”

## 5. `ParameterHistory` receives one initialization snapshot

**Finding.** `Optimization.__init__` creates a `ParameterHistory` and appends the resolved parameter set once (`pyglotaran/glotaran/optimization/optimization.py:93–97`). During every objective call the parameter values are updated, but no history append follows (`optimization.py:175–189`); the original history object is later attached to `OptimizationInfo` (`optimization.py:143–152,163–172`). The append API can store an iteration number, whose default is zero (`pyglotaran/glotaran/parameter/parameter_history.py:126–154`), but the optimization path supplies no later snapshots. This is distinct from `OptimizationHistory`, which parses numerical progress rows from optimizer stdout (`pyglotaran/glotaran/optimization/optimization_history.py:84–102`).

**Confidence:** High — the frozen tree has one call site that appends the optimization's private parameter history.

**Chapter impact:** Say that a serializable `ParameterHistory` object is retained, but do not call it an iteration-by-iteration parameter trajectory; on the inspected path it contains the initialization snapshot only.

**Neutral maintainer-review wording:** “At what cadence is `ParameterHistory` intended to record values: every function evaluation, accepted optimizer iterations, only initial/final states, or not at all? The current optimization path appends only the initial state.”

## 6. Old terminology remains in docstrings and support code

**Finding.** Current type names coexist with transitional text. `ExperimentModel` is still described as a “dataset group” (`pyglotaran/glotaran/model/experiment_model.py:1,31–32`), and linked-data helpers repeat that term (`pyglotaran/glotaran/optimization/data.py:350–355,391–395,427–461`). Simulation documentation and a user-facing error still say “global megacomplex(es)” while the implementation checks `model.global_elements` (`pyglotaran/glotaran/simulation/simulation.py:45–75`). The testing support module retains `Megacomplex` imports, helper names, and a `"megacomplex"` registry key (`pyglotaran/glotaran/testing/plugin_system.py:12–19,47–88,148–186`), whereas the active central registry declares `element`, `data_io`, and `project_io` (`pyglotaran/glotaran/plugin_system/base_registry.py:38–46`).

**Confidence:** High — exact strings and the active declarations are present together.

**Chapter impact:** Treat these strings as transitional documentation/support evidence only. Use the contract's current `ExperimentModel`, experiment, `Element`, `elements`, and `global_elements` terminology; do not infer an active `Megacomplex` type or registry from the support helper.

**Neutral maintainer-review wording:** “Which remaining `dataset group` and `megacomplex` references are intentional compatibility language, and which are cleanup candidates? In particular, should the simulation error and testing registry helpers use the current element vocabulary?”

## 7. The handoff names a nonexistent `ModelLibrary.resolve`

**Finding.** The handoff's reference-resolution row names `ModelLibrary.resolve` (`docs/pyglotaran-architecture-chapter-handoff.md:211`). The frozen `ModelLibrary` has no such public method: extension chains are discovered and combined inside `ModelLibrary.__init__`, with stalled progress raising the cyclic-dependency error (`pyglotaran/glotaran/project/library.py:25–46,60–65`). Other binding proceeds through such paths as `ExperimentModel.resolve()` (`pyglotaran/glotaran/model/experiment_model.py:75–97`).

**Confidence:** High — the cited handoff symbol is absent and the constructor-time implementation is explicit.

**Chapter impact:** Replace the obsolete method anchor. Describe extension resolution behaviorally as occurring during library construction, and cite the actual constructor loop; reserve `resolve` method wording for APIs that exist.

**Neutral maintainer-review wording:** “Is constructor-time extension resolution the intended `ModelLibrary` lifecycle, or is a public resolution phase planned? Until clarified, may the handoff anchor be corrected from `ModelLibrary.resolve` to `ModelLibrary.__init__` and `_get_extended_elements`?”
