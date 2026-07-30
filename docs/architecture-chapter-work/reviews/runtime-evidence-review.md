# Runtime-behavior and source-evidence review

## Scope and disposition

This review is limited to the frozen chapter and evidence-ledger snapshot named in
`00-integrated-snapshot.md`, checked against pyglotaran revision
`468c4cd57aaf25c10edf85cd197df771bad0a766`. Current source is treated as authority for
architecture and runtime behavior. The 2023 paper is treated only as v0.7-era scientific,
historical, and workflow evidence. No tests were run, no other review report was read, and no
file other than this report was edited.

Priority summary:

| Priority | Findings |
|---|---:|
| P0 | None |
| P1 | 3 chapter/evidence findings; 1 maintainer finding |
| P2 | 3 chapter/evidence findings; 2 maintainer findings |
| P3 | None |

## P0 findings

None. I found no source, mathematical, or scientific contradiction that invalidates the
chapter's central architecture or nested-estimation account.

## P1 findings

### P1-1 — Missing-parameter failure is conflated with post-resolution issue collection

- **Chapter location:** Section 2.3, lines 455–460.
- **Ledger location:** `AR-012`, ledger line 107.
- **Source anchors:** `pyglotaran/glotaran/model/item.py:315–328,331–364,385–397`;
  `pyglotaran/glotaran/model/experiment_model.py:75–104`;
  `pyglotaran/glotaran/optimization/optimization.py:71–79`;
  `pyglotaran/glotaran/parameter/parameters.py:297–318`.
- **Finding:** `get_item_issues` can report unresolved parameter-label strings when called on
  an unresolved item. That is not the missing-parameter route taken by `Optimization`.
  Optimization first calls `ExperimentModel.resolve`; resolving a string calls
  `add_to_initial`, whose `initial.get(label)` raises `ParameterNotFoundError` when the label
  is absent. Post-resolution issue gathering is reached only afterward and principally
  handles validators such as element exclusivity and uniqueness. Ledger claim `AR-012`
  incorrectly groups missing parameter labels among issues collected after binding.
- **Safe correction:** State that missing parameter references fail during binding, before
  objective construction, while the subsequent issue-collection pass handles the supported
  validators on resolved experiments. Retain the narrower fact that `get_item_issues` can
  identify unresolved string labels when used directly, but do not present that helper as the
  observed optimization failure path.
- **Rationale:** The chapter's ordering claim remains broadly right—both failures precede
  numerical objectives—but the exception phase and mechanism matter to its explanation of
  semantic resolution and validation.

### P1-2 — Element-result provenance is overgeneralized to the specialized global-element path

- **Chapter location:** Section 5.2, lines 1026–1034.
- **Ledger location:** `RR-13`, ledger line 231.
- **Source anchors:** `pyglotaran/glotaran/optimization/objective.py:632–690,864–878`;
  `pyglotaran/glotaran/model/element.py:100–162`.
- **Finding:** Ordinary result construction iterates `DataModel.elements`, calls
  `element.create_result_with_uid`, and adds `element_uid`. The specialized global-element
  result path in `create_global_result` instead assembles a dataset directly under the
  dataset label; it does not call each global Element's result method and does not add an
  `element_uid` there. The prose's “each contributing Element” wording and the unqualified
  ledger claim therefore exceed the verified path.
- **Safe correction:** Replace the universal wording with: “For ordinary Element results,
  result construction calls each resolved ordinary Element's result method and adds its fully
  qualified `element_uid`. The specialized global-element path assembles its result directly
  and does not provide that per-Element UID in the inspected implementation.”
- **Rationale:** This preserves the valid provenance example without assigning ownership or
  metadata to a path that does not implement it.

### P1-3 — “Fully qualified name” and pinning syntax are generalized across unlike registry keys

- **Chapter location:** Section 6.1, lines 1116–1124; Table 4, lines 1134–1140.
- **Ledger location:** `EX-07` and `EX-08`, ledger lines 262–263.
- **Source anchors:** `pyglotaran/glotaran/plugin_system/base_registry.py:138–190,193–251`;
  `pyglotaran/glotaran/plugin_system/element_registration.py:22–37,98–120`;
  `pyglotaran/glotaran/plugin_system/data_io_registration.py:51–89,127–152`;
  `pyglotaran/glotaran/plugin_system/project_io_registration.py:70–108,146–175`;
  `pyglotaran/glotaran/optimization/objective.py:217–243`.
- **Finding:** Element registry full keys are the module-and-class path returned by
  `full_plugin_name`. Data- and project-I/O providers are instantiated per format, and
  `add_plugin_to_registry` appends `_<format>` to their full registry keys. The exact key
  required by `set_data_plugin` or `set_project_plugin` is therefore not always merely the
  module-and-class path. Separately, loaded data record the unsuffixed module/class value in
  `io_plugin_name`, and result serialization may append the format suffix when selecting the
  registry entry. The conflict rule itself—retain the incumbent short binding and keep the
  newcomer under an unambiguous full key—is correctly described.
- **Safe correction:** Use “fully qualified registry key” as the cross-registry term, then
  distinguish Element keys (`module.Class`) from instantiated I/O keys
  (`module.Class_<format>`). Say that pinning rebinds a short name to the exact full key shown
  by that registry.
- **Rationale:** The present wording can give a reader a pinning value that is valid for
  Elements but not for an actual I/O registry entry.

## P2 findings

### P2-1 — The required version-provenance semantics are absent from Section 5.2

- **Chapter location:** Section 5.2, especially lines 1036–1057.
- **Ledger location:** `RR-18`, ledger line 236; cross-cutting qualification at ledger lines
  295–298.
- **Source anchors:** `pyglotaran/glotaran/optimization/info.py:98–105,128–135`;
  `pyglotaran/tests/project/test_result.py:52–65,134–146` is the focused corroborating test
  already cited by the ledger (not rerun here).
- **Finding:** The skeleton requests version/source metadata, and the ledger correctly records
  the important limitation, but the chapter discusses only source paths and provider identity.
  `OptimizationInfo.glotaran_version` is a computed field read from the currently installed
  `glotaran.__version__`; deserialization explicitly discards the serialized value before the
  field is recomputed. It is not immutable “version used to create this result” provenance.
- **Safe correction:** Add one sentence: “Serialization exposes the currently running
  pyglotaran version through a computed field; on reload it is recomputed rather than retained
  as an immutable creation-version record.”
- **Rationale:** Omitting the field avoids a false claim, but it leaves a required provenance
  boundary unexplained despite the ledger having exact evidence for it.

### P2-2 — History coverage is safe but too vague to communicate current behavior

- **Chapter location:** Section 5.1, lines 938–943; Section 5.2, lines 1041–1045.
- **Ledger location:** `RR-15`, ledger line 233.
- **Source anchors:** `pyglotaran/glotaran/optimization/optimization.py:93–97,143–147`;
  `pyglotaran/glotaran/optimization/optimization_history.py:84–102`;
  `pyglotaran/glotaran/parameter/parameter_history.py:126–154`.
- **Finding:** “Exact coverage depends on how the current runtime populates them” is not
  wrong, but the source supports a much safer and more useful exact statement.
  `ParameterHistory` is appended once during initialization and is not an outer-iteration
  trajectory. `OptimizationHistory` is parsed from captured SciPy verbose text and can
  consequently be empty when that text is unavailable.
- **Safe correction:** Replace the vague sentence with those two field-specific facts.
- **Rationale:** A reader assessing reproducibility could otherwise infer that both objects
  record the changing parameters at every iteration.

### P2-3 — Retained residual semantics should distinguish restored and weighted forms

- **Chapter location:** Section 5.2, lines 1017–1025.
- **Ledger location:** `RR-11`, ledger line 229, which already contains the correct
  qualification.
- **Source anchors:** `pyglotaran/glotaran/optimization/data.py:244–251`;
  `pyglotaran/glotaran/optimization/objective.py:135–153,597–630,748–758,899–927`.
- **Finding:** The chapter correctly lists an optional weighted RMSE and does not invent a
  stored weighted-residual field, but it does not say that result construction first copies
  the objective residual into a temporary `weighted_residual`, restores the reported
  `residual` by dividing by the weights, calculates weighted RMSE from the temporary array,
  and then stores only the restored residual plus the metric.
- **Safe correction:** Add: “When weights are present, the retained residual array is restored
  to the unweighted data scale; weighted residuals are used transiently to calculate
  `weighted_root_mean_square_error` and are not a separate `OptimizationResult` field.”
- **Rationale:** This distinction determines which array a scientist is actually plotting or
  persisting and completes the otherwise accurate weighting account.

## P3 findings

None. Optional enrichment is not needed until the P1 and P2 corrections above are resolved.

## Maintainer findings (do not present these as promised chapter behavior)

### P1-M1 — Dataset-key flattening has unresolved collision semantics

- **Related chapter location:** Section 5.1, lines 945–954; Section 5.2, lines 1009–1015.
- **Source anchor:** `pyglotaran/glotaran/optimization/optimization.py:137–141`.
- **Observation:** One objective is created per Experiment, but objective result maps are
  flattened with `dict(ChainMap(...))` into a top-level dataset-keyed mapping. The source has
  an explicit TODO for multiple experiments containing the same dataset name. A duplicate key
  is not namespaced by Experiment and one mapping wins rather than both being retained.
- **Chapter-safe handling:** Say only that results are flattened by dataset label and that
  collision behavior for repeated labels across Experiments is not a documented contract.
  Do not claim a nested per-Experiment container or reliable duplicate-label handling.
- **Maintainer action:** Decide whether dataset labels must be globally unique, should be
  namespaced, or should trigger an explicit error before flattening.

### P2-M2 — `OptimizationInfo.success` does not mirror SciPy's success flag

- **Related chapter location:** Section 5.1, lines 938–943; Section 5.2, lines 1036–1045.
- **Source anchor:** `pyglotaran/glotaran/optimization/info.py:137–187`.
- **Observation:** `OptimizationInfo.from_least_squares_result` sets `success = result is not
  None`; it does not read `result.success`. SciPy can return an `OptimizeResult` whose own
  success flag is false, for example after an evaluation limit. The chapter wisely does not
  equate this field with convergence.
- **Chapter-safe handling:** If the field is named, describe its inspected semantics as
  “whether a SciPy result object was obtained,” and continue to use termination reason and
  diagnostics for interpretation.
- **Maintainer action:** Either map the field to `result.success` or rename/document it so its
  meaning matches the implementation.

### P2-M3 — The public `add_svd` option is unused and SVD arrays are transient

- **Related chapter location:** Section 5.2 result inventory, lines 1017–1045.
- **Source anchors:** `pyglotaran/glotaran/project/scheme.py:68–103`;
  `pyglotaran/glotaran/optimization/optimization.py:51–97`;
  `pyglotaran/glotaran/optimization/objective.py:52–65,145–153,673–688,748–759,899–927`.
- **Observation:** `Scheme.optimize(add_svd=...)` passes the option into `Optimization`, which
  stores `_add_svd` but never reads it. Result construction calls `add_svd_to_result_dataset`
  regardless, yet then constructs `OptimizationResult` from only input, residual,
  decomposition, metadata, and contribution maps. The calculated singular vectors and values
  are not fields of the returned result.
- **Chapter-safe handling:** Continue not to list retained SVD arrays. If SVD is mentioned,
  call it transient computation in this revision, not result content.
- **Maintainer action:** Wire the option to retained output or remove/deprecate it and avoid
  the unconditional discarded calculation.

## Verified high-risk claims with no finding

- `Scheme` owns the Experiment mapping and `ModelLibrary`; an Experiment owns DataModels; the
  library owns labeled Elements; DataModels refer to Elements and can carry an associated
  source or loaded dataset. The chapter keeps ownership, reference, and runtime-input edges
  distinct.
- There is no staging `ModelLibrary.resolve`. Extension chains are handled during
  `ModelLibrary.__init__`; runtime binding proceeds through `ExperimentModel.resolve`,
  `resolve_data_model`, and item helpers. The chapter and ledger correctly avoid the stale
  method.
- Data wrappers, orientation, weights, and linked-coordinate structures initialize once,
  whereas trial parameters, expression consequences, matrices, reduced matrices, CLPs,
  residuals, and penalties are recalculated through the outer callback.
- Post-optimization result construction performs a final numerical calculation and returns a
  dataset-keyed top-level mapping; the only qualification needed is the duplicate-label
  maintainer issue above.
- Persistence correctly dispatches through separate project- and data-I/O surfaces, is
  saving-policy dependent, and can preserve original data source/plugin relationships.
- Simulation resolves the DataModel and reuses matrix construction with supplied CLPs or
  global Elements without invoking the outer optimizer.
- The core/numerical-library/Jupyter/examples/extras boundaries are supported by current
  package metadata and source. The chapter does not use the 2023 paper as authority for
  staging class names.

## Hash confirmation and recommendation

Before review:

- `docs/pyglotaran-architecture-chapter-draft.md` SHA-256:
  `B8104026C07928A8832809B194B9431215B7A37F058E06D0EC0772E5F5327A17`
- `docs/pyglotaran-architecture-evidence-ledger.md` SHA-256:
  `59D87C496049A82E1AA29262AFAF775DEE83AA7E877E1E1FAAE79B57FAD63D8B`
- `pyglotaran` revision:
  `468c4cd57aaf25c10edf85cd197df771bad0a766`

The two snapshot hashes are reconfirmed unchanged at the end of review.

**Recommendation: REVISE.** The chapter's central architecture and runtime lifecycle are
sound, but the three P1 chapter/evidence distinctions should be corrected before acceptance.
The P2 changes would make the result and provenance account match the unusually careful
field-level evidence already present in the ledger.
