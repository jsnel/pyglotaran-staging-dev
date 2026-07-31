# Coordinating-editor review notes

## 1. Editorial disposition

The chapter and evidence ledger constitute a coherent first draft for the inspected
pyglotaran staging architecture. They were assembled from independently owned section,
evidence, figure, and table packets and then edited centrally into one argument. The final
draft is not a concatenation of packet text: definitions were assigned one first-use
location, notation was normalized, transitions were rewritten, and the synopsis and
conclusion were written after the body had been integrated.

Present software terminology and behavior follow the current staging source. The 2023
pyglotaran paper is used only for scientific aims, history, and v0.7-era architectural
rationale. It is not treated as authority for staging syntax or class names. Proposed
compatibility tooling, agent skills, future v1 names, and unreleased behavior are outside the
chapter's scope.

The editorial recommendation after correction is **accept as a first thesis-chapter
draft, with the maintainer questions in Section 6 below retained for technical review**.

## 2. Revisions and review snapshot

The following revisions were frozen before evidence reconstruction:

| Repository | Inspected revision | Role |
|---|---|---|
| Staging workspace | `f1516d19e1680699c6c6e502e523e51bc9d0cc59` | Chapter workspace and supplied literature |
| `pyglotaran` | `468c4cd57aaf25c10edf85cd197df771bad0a766` | Authority for present architecture, names, and runtime behavior |
| `pyglotaran-examples` | `7f7fd227bcfb74308523d2242ca811a68ba25214` | Corroboration of current user-level composition |
| `pyglotaran-extras` | `d57940be02751c670ee90f3bc09af7cd954a1d08` | Boundary evidence for plotting and higher-level exploration |

No source repository was reset, cleaned, reformatted, or edited. The working-tree changes
created by this task are confined to the chapter artifacts under `docs/`.

The integrated pre-review snapshot is recorded in
`docs/architecture-chapter-work/reviews/00-integrated-snapshot.md`:

| Artifact | Frozen SHA-256 |
|---|---|
| Integrated chapter | `B8104026C07928A8832809B194B9431215B7A37F058E06D0EC0772E5F5327A17` |
| Integrated evidence ledger | `59D87C496049A82E1AA29262AFAF775DEE83AA7E877E1E1FAAE79B57FAD63D8B` |

All three independent reviewers confirmed those hashes before reporting. After central
correction, the production hashes are:

| Artifact | Corrected SHA-256 |
|---|---|
| Chapter draft | `51A17E4C8F2156DB2611F299D891E80EFE93A572F1DF85099681D4E32665A3F1` |
| Evidence ledger | `5AF8C6D5B4E8E033E6E6A76098B523A5BED9F919D08935D543FFED58A9690A41` |

## 3. Independent review record

Three reviewers assessed the same frozen integrated snapshot and reported findings without
editing the assembled chapter:

- `docs/architecture-chapter-work/reviews/architecture-mathematics-review.md` checked the
  object architecture, matrix formulation, estimator semantics, uncertainty quantities, and
  alignment behavior against source.
- `docs/architecture-chapter-work/reviews/runtime-evidence-review.md` checked the lifecycle,
  result structures, persistence, registry behavior, and evidence-ledger traceability.
- `docs/architecture-chapter-work/reviews/readability-style-apa-review.md` checked
  bachelor-level readability, scientific-question-first development, definition order,
  transitions, diagrams, repetition, author–date citations, and the reference list.

The source and mathematics review found four P0 issues in the integrated snapshot. All four
were corrected before production: the semantics of the field named `covariance_matrix`,
degrees-of-freedom limitations, the unreliable `forward` alignment branch, and the scope of
the non-negativity guarantee under NNLS. No P0 finding remains in the corrected draft.

## 4. Finding disposition

| Review finding | Disposition in corrected chapter or ledger |
|---|---|
| Architecture/mathematics P0-1: an unscaled inverse normal matrix was described too much like a covariance estimate | Accepted. Section 4.3 now defines the Jacobian and normal matrix, states the exact residual-scale multiplier used for standard errors, and identifies the unconverted logarithmic optimizer coordinate. Ledger claim NM-15 records the same limitation. |
| Architecture/mathematics P0-2: degrees of freedom were presented too generally | Accepted. Section 4.3 now states that penalty entries are counted as residual entries and that the specialized global-Element path subtracts a sum of CLP-axis sizes although the fitted array uses their product. |
| Architecture/mathematics P0-3: directional alignment was overstated | Accepted. Section 3.2 presents the method names as intended policies and explicitly records the filtered-index defect in the inspected `forward` branch as a maintainer issue. Ledger claim DP-09 was corrected. |
| Architecture/mathematics P0-4: NNLS constrains only the reduced coefficients | Accepted. Section 4.2 and Table 3 now explain that a relation-reconstructed target can be negative when its relation factor is negative. Ledger claim NM-07 was corrected. |
| Architecture/mathematics P1-1: one matrix symbol mixed full surfaces, coordinate slices, linked blocks, and a flattened path | Accepted. The full-surface equation is limited to the common-matrix running example. Stable per-inner-solve notation \(\mathbf{y}_u=\mathbf{M}_u\mathbf{b}_u+\boldsymbol{\varepsilon}_u\) now covers the actual numerical granularities. |
| Architecture/mathematics P1-2: the equal-area penalty was described as an integral | Accepted. It is now described as a weighted difference of sums of absolute CLP samples over selected intervals, with the additional grid-spacing assumption needed for an area interpretation. |
| Architecture/mathematics P1-3: optimizer and retained residual scales were conflated | Accepted. Section 5.2 distinguishes the weighted residual used by the outer objective from the residual restored to the measurement scale in `OptimizationResult`; only weighted RMSE is retained separately. |
| Architecture/mathematics P1-4: the QR rank condition was missing | Accepted. Section 4.2 states the full-column-rank and conditioning assumption and makes clear that the unpivoted QR path is not rank revealing. |
| Runtime/evidence P1-1: missing-parameter failure was assigned to the later issue pass | Accepted. Sections 2.3 and 5.1 now distinguish binding-time failure from subsequent issue collection. Ledger claim AR-012 was corrected. |
| Runtime/evidence P1-2: ordinary Element provenance was generalized to the specialized global path | Accepted. Section 5.2 and ledger claim RR-13 scope `element_uid` to ordinary Element results and state the specialized path's exception. |
| Runtime/evidence P1-3: registry-key forms were generalized | Accepted. Section 6.1 and ledger claims EX-07–EX-08 distinguish Element `module.Class` keys from I/O `module.Class_<format>` keys and require the exact registry key for pinning. |
| Readability/style P1-1 and architecture P2-1: Figure 5 reversed outer-loop values | Accepted. Figure 5 now gives SciPy its own node and uses separate arrows for trial outer values and the returned residual vector. |
| Runtime/evidence P2-1: version provenance absent | Accepted. Section 5.2 states that `glotaran_version` is recomputed in the reader environment rather than preserved as immutable creation metadata. |
| Runtime/evidence P2-2: histories were vague | Accepted. Section 5.2 states that `ParameterHistory` receives one initialization snapshot on this path and that `OptimizationHistory` depends on captured SciPy text. |
| Runtime/evidence P2-3: retained residual semantics were incomplete | Accepted with the weighted/unweighted correction described above. |
| Readability/style P2-1 through P2-13 | Accepted. The synopsis was simplified; pump and probe were explained; entity and terminology tables now follow their definitions; API catalogues were shortened; formal vocabulary follows ordinary-language ideas; uncertainty terms were defined; repeated caveats were reduced; Figure 1 arrow semantics and all figure callouts were clarified; subsection bridges were strengthened; citation placement and ordering were corrected; and the exact `0.8.0.dev0` snapshot is named. |

No P3 enrichment was requested by any reviewer. Extra API enumeration and additional
figures were intentionally not added.

## 5. Validation performed

### Source-focused checks completed before the test stop

Before the user directed the editor to stop spending time on tests, two focused selections
had completed successfully in the configured Python 3.10.19 environment:

- scheme, data-model, experiment, optimization, and plugin-registry selection:
  **180 passed, 1 expected xfail**;
- supplementary result, simulation, and schema selection: **15 passed**.

Initial attempts encountered stale bytecode and pytest temporary-path environment effects;
the same focused selections produced the outcomes above after those environmental paths were
isolated. These checks corroborate the source evidence but do not replace it. In accordance
with the user's instruction, no further tests were run during review or final correction.

### Final text and artifact checks

- Six Mermaid source blocks have balanced fences and six sequential figure captions.
- Four table captions appear in sequence.
- Five displayed equations have paired delimiters.
- The prose contains no unresolved verification marker, packet placeholder, or prohibited
  old chapter terminology.
- The chapter consistently distinguishes global analysis from the global dimension,
  explicit outer parameters from CLPs, the Scheme from separately supplied arrays and
  values, and DataModels from measured xarray data.
- The four in-text literature sources each have one APA-formatted reference entry, and no
  uncited entry remains.
- The two *Journal of Statistical Software* DOI strings were independently confirmed
  against the official JSS article pages:
  [TIMP](https://www.jstatsoft.org/v18/i03/) and
  [Glotaran](https://www.jstatsoft.org/article/view/v049i03).
- The chapter contains approximately **10,555 prose-and-caption words** when tables,
  display equations, Mermaid source, and references are excluded, or approximately
  **11,636 body words** when table and equation text is included but Mermaid source and
  references remain excluded.
- The installed Pandoc parser accepts the Markdown source. A Mermaid command-line renderer
  is not installed, so diagram validation was structural and editorial rather than a
  raster-rendering pass.

## 6. Maintainer-review questions and implementation uncertainties

These items are deliberately separated from the chapter's main architectural claims. They
describe the inspected implementation, not promised intent.

1. **Dataset-label collisions across Experiments.** Objective results are flattened into one
   dataset-keyed mapping. The source contains a TODO concerning repeated dataset names.
   Maintainers should decide whether labels must be Scheme-wide unique or whether result
   keys should preserve Experiment identity.

2. **Meaning of `OptimizationInfo.success`.** The field is set according to whether a
   least-squares result object exists, not from SciPy's `OptimizeResult.success`. The
   intended public meaning should be clarified.

3. **Version provenance.** A serialized `glotaran_version` is discarded on reading and
   recomputed from the reader's environment. If creation-time provenance is required, it
   needs a distinct retained field.

4. **Transient SVD work and `add_svd`.** Result construction calculates SVD variables in a
   local dataset but does not expose them through `OptimizationResult`; the public
   `add_svd` option is stored but not consulted on the inspected path.

5. **Parameter-history coverage.** `ParameterHistory` receives only the initialization
   snapshot in the current optimization path. It is not a trajectory of accepted optimizer
   iterations.

6. **Transitional terminology.** Older “dataset group” and “megacomplex” strings remain in
   selected docstrings, errors, and support code. They should not override current
   `Experiment` and `Element` terminology, but maintainers may wish to identify which
   occurrences are compatibility text and which are cleanup candidates.

7. **Library-resolution anchor.** The handoff named a public `ModelLibrary.resolve` method
   that is absent from this revision. Element-extension chains are resolved during
   `ModelLibrary` construction; Experiment and item binding use other resolution helpers.

8. **`forward` coordinate alignment.** The branch filters candidate distances and then uses
   an index from that filtered array against the unfiltered target axis. Directional
   matching should not be guaranteed until the index mapping is corrected and focused.

9. **Uncertainty fields and counts.** The field named `covariance_matrix` is an unscaled,
   rank-truncated inverse normal matrix. Log-coordinate standard errors are assigned without
   conversion to the displayed physical scale. Penalties contribute to the reported
   residual length, and the specialized global-Element path counts a sum rather than the
   product of its CLP-axis sizes. These points require resolution before quantitative
   uncertainty claims are generalized.

10. **Two residual-function fields.** Repeated ordinary and global-penalty objective
    calculations read the Experiment-level residual-function selection, while specialized
    global-result reconstruction later reads the DataModel-level field. The intended
    relationship between those settings merits clarification.

11. **Element provenance asymmetry.** Ordinary Element-result datasets receive an
    `element_uid`; the specialized global-Element result path assembles its dataset directly
    without the same field.

12. **Registry full-key forms.** Element full keys and I/O full keys do not have identical
    shapes because I/O providers append the selected format. Documentation and future
    compatibility helpers should use exact keys obtained from the relevant registry.

## 7. Justified deviations from the handoff

- The chapter is modestly above the soft 8,000–10,000-word target: approximately 10,555
  prose-and-caption words. The excess was retained because the independent review required
  precise qualifications for multiple numerical paths, uncertainty fields, and
  implementation boundaries. Repeated cautions and low-value API catalogues were removed
  first.
- Testing stopped after the two successful focused selections because the user explicitly
  directed the editor not to spend further time on tests. The remaining validation was
  source inspection, evidence reconciliation, independent review, and text-only structural
  checking.
- Mermaid source is embedded as the original diagram deliverable. No Mermaid CLI was
  available for rendering; arrows, captions, fence balance, and numbering were checked
  directly.
- The 2004 reference conservatively omits an issue number and journal subseries that are not
  printed on the supplied article title page. The article DOI, volume, and page range are
  retained.
- Working figure filenames preserve their packet-era identifiers to avoid collision, while
  the assembled chapter uses final figure numbers in order of appearance.

No deviation was made from the source-authority hierarchy or the terminology contract.

---

## 8. Post-compression accuracy review

Added after the compression pass (commit `cf15163`), which reduced the chapter from 12,300 to
9,818 words excluding references without removing facts, equations, figures, tables, or
citations.

**Authority.** Every finding below was verified directly against the pyglotaran source at
`468c4cd57aaf25c10edf85cd197df771bad0a766`, the revision the chapter cites. Source was treated
as authoritative; the prior architecture analyses formerly under `docs/architecture/` were used
only as cross-checks. Line references are to files under `pyglotaran/glotaran/`.

**Tests.** `pytest tests/optimization tests/model tests/project tests/parameter
tests/plugin_system tests/simulation` — **271 passed, 3 failed, 1 xfailed**. All three failures
are environment artifacts, not defects: cached bytecode under `tests/**/__pycache__` was
compiled while this repository lived at `D:\src\...`, so warning-location assertions compare a
`D:` path against the real `C:` path. Confirmed by inspecting the `.pyc`, which contains
`D:\src` and no `C:\src`. Clearing `__pycache__` resolves them. Nothing was skipped or
suppressed to make the review pass.

### 8.1 Findings, most severe first

All eight have been applied to the chapter.

**1. Equal-area penalty formula was incomplete.** The chapter described the residual as "a
configured weight times the difference between sums of absolute CLP samples." The
implementation is `|Σ|source| − p·Σ|target|| · weight` (`optimization/penalty.py:47`). Two
elements were missing: the configured `penalty.parameter` scaling the target sum, and the
absolute value around the difference. Corrected in §4.3 and in the **p** row of Table 3.

**2. Standard-error multiplier was mis-identified.** The chapter said "the root-mean-square
residual multiplied by the square root of the corresponding diagonal entry." The multiplier is
`sqrt(chi_square / degrees_of_freedom)` (`optimization/info.py:176-184`, consumed at
`info.py:213`), not `sqrt(mean(r²))`. The denominator is the degrees of freedom, which the
chapter separately and correctly notes is path-dependent, so the reported error inherits that
limitation. Compounding this, `OptimizationResultMetaData.root_mean_square_error` *is* the
plain `norm(residual)/sqrt(size)` (`optimization/objective.py:81`): two different quantities
share the field name. The chapter used it correctly in §5.2 and incorrectly in §4.3. Corrected
in §4.3, with an explicit note that the two identically named fields differ.

**3. `residual_function` attributed to the wrong object.** The chapter listed it among
per-dataset DataModel configuration (`model/data_model.py:197`). On the ordinary estimation
path the estimator is selected from `ExperimentModel.residual_function`
(`optimization/objective.py:532`, `:556`). The per-dataset field is read at exactly one site,
`objective.py:654`, inside `create_global_result` — result construction on the specialized
global path. A reader following the chapter would configure the field that has no effect on
their fit. Corrected in §3.1 and flagged as a maintainer-review issue.

**4. Relation and constraint reduction presented as universal.** §4.2 stated that relations and
zero/only constraints reduce the matrix "before the inner solver is called," unqualified.
`OptimizationObjective.calculate_global_penalty` (`objective.py:549-557`) goes from
`OptimizationMatrix.from_global_data` straight to estimation: no reduction, no relations, no
CLP penalties. Corrected in §4.2 with an explicit sentence naming what the global path skips.

**5. `simulate()` signature incomplete.** §6.2 omitted the `ModelLibrary` argument; the
signature is `simulate(model, library, parameters, coordinates, clp=None, ...)`
(`simulation/simulation.py:22`), and the library is what makes the resolution step the chapter
describes possible. Corrected in §6.2.

**6. Minimal saving policy understated.** §5.2 said it "omits selected derived arrays."
`SAVING_OPTIONS_MINIMAL` (`io/interface.py:76`) filters all six bulk keys: `input_data`,
`residuals`, `fitted_data`, `elements`, `activations`, `fit_decomposition`. `input_data` is the
only partial exception, and only because the serializer substitutes the original source path
when `source_path` and `io_plugin_name` are present. Corrected in §5.2.

**7. Attribution gap on variable projection.** The chapter cited the separable-least-squares
literature generally. The implementation is specifically Kaufman's algorithm:
`optimization/variable_projection.py` carries `Kaufman Q2 step 3/4/5` comments and a
`TODO: Reference Kaufman paper`, over LAPACK `dgeqrf`/`dormqr`/`dtrtrs`. Corrected in §4.2;
Kaufman (1975) added to the reference list.

**8. Dataset-label collision across Experiments not noted.** §5.1 described results being
"keyed by dataset label and combined into the top-level mapping" without noting that the
`ChainMap` merge (`optimization/optimization.py:140`) lets identical labels in different
Experiments shadow one another. The source carries a `TODO` about exactly this at
`optimization.py:137`. Corrected in §5.1.

### 8.2 Verified correct, no change needed

Confirmed against source. Several are unusually precise and should survive future edits.

- `covariance_matrix` is a rank-truncated pseudo-inverse of the Jacobian normal matrix and is
  *not* multiplied by a residual variance; the `root_mean_square_error` argument to
  `calculate_covariance_matrix_and_standard_errors` is explicitly unused (`info.py:222-244`).
- On the global-Element path the reported CLP count is the **sum** of the two label-axis sizes
  while the fitted coefficient array uses their **product** (`objective.py:658` vs `:670`).
- The `forward` alignment method does not preserve the index of its filtered candidate:
  `diff.argmin()` indexes the filtered array but is applied to the unfiltered `target_axis`
  (`optimization/data.py:337-348`). `backward` is safe on an ascending axis because its filter
  keeps a prefix; `forward` keeps a suffix.
- `ParameterHistory` receives exactly one snapshot, at `Optimization.__init__`
  (`optimization.py:93-94`).
- `element_uid` is added by `create_result_with_uid` (`model/element.py:161`) on the ordinary
  path only; `create_global_result` assembles its Element dataset directly without one.
- The weighted residual is written into a local working dataset to compute the weighted error
  metric and is not a field of `OptimizationResult` (`data.py:244-251`, `objective.py:624`).
- Degrees of freedom are the full residual-vector length, penalty entries included, minus the
  outer and CLP counts (`info.py:170-174`).
- CLP relation reduction: `array @ relation_matrix` adds `parameter × target column` into the
  source column and deletes the target (`matrix.py:227-242`), consistent with the
  reconstruction `clp[target] = parameter × clp[source]` (`estimation.py:61-64`).
- Element labels `parallel` and `target` used as illustrations are real: `parallel` in
  `glotaran/testing/simulated_data/parallel_spectral_decay.py` and `shared_decay.py`; `target`
  in `pyglotaran-examples/.../ex_two_datasets/models/model.yml`.
- Three entry-point groups, first-registration-wins with `PluginOverwriteWarning`, full dotted
  keys, format suffix on instantiated I/O plugins, and `set_plugin` pinning — all as described
  (`plugin_system/base_registry.py:112-251`).
- `non_negative` uses a logarithmic optimizer coordinate and exponentiates on return
  (`parameter/parameter.py:268-283`); an expression forces `vary = False` (`parameter.py:137`).

### 8.3 Maintainer-review items outside the chapter's claims

Not chapter defects; recorded because they surfaced during verification.

1. `Scheme.optimize(add_svd=...)` is stored as `Optimization._add_svd` and never read. The SVD
   arrays computed by `add_svd_to_result_dataset` are written into a local working dataset and
   discarded, since only `.data` and `.residual` are lifted into `OptimizationResult`.
2. `bounds` are passed to `scipy.optimize.least_squares` unconditionally, including for
   `method="lm"`, which SciPy does not support with bounds (`optimization.py:118-128`).
3. `OptimizationInfo.success` is `result is not None` (`info.py:149`): it records that
   `least_squares` returned, not that it converged.
4. Stale transitional docstrings remain — `model/experiment_model.py:1` still says "dataset
   group", and `simulation/simulation.py` still says "megacomplexes". These do not affect the
   implemented vocabulary but will mislead readers of the generated API documentation.

### 8.4 Open questions added by this review

- Whether the `forward` alignment index behaviour is a defect or an intended selection rule.
  The chapter states it as a maintainer-review issue rather than a guarantee, which remains the
  safe wording until confirmed.
- Whether `DataModel.residual_function` is intended to be authoritative for its dataset — in
  which case the ordinary path reading the Experiment-level field is the defect — or whether
  the per-dataset field should be removed.
- Whether the global-Element CLP count is intended to feed degrees of freedom at all, given
  that the count and the coefficient array disagree.
