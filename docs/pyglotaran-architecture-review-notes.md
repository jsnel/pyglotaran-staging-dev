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
