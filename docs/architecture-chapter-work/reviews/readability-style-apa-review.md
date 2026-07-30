# Readability, van-Stokkum-inspired style, and APA review

## Review basis and overall assessment

This review covers the frozen integrated chapter and evidence ledger identified in
`00-integrated-snapshot.md`. I read the editorial contract, paragraph-level skeleton,
chapter, merged ledger, and APA helper in full. I also visually checked the title pages of
the four primary literature PDFs. I did not run tests, inspect other review reports, or edit
the reviewed artifacts.

The chapter has a coherent scientific-first arc, a consistently restrained account of what
a fit can establish, and unusually good continuity of the time-by-wavelength example from
the primer through estimation, results, simulation, and conclusion. The four cited works
all have matching reference-list entries, every reference-list entry is cited, author
particles and the Weißenborn diacritic are preserved, and article titles are in sentence
case. The explicit separation of the 2023 paper's v0.7-era evidence from staging-source
authority is also present in the synopsis, lineage, ledger, and conclusion.

Revision is nevertheless recommended. One figure reverses the meanings of trial and
residual vectors, and several expository choices impede the intended first-time bachelor
reader: the synopsis front-loads formal vocabulary, the pump–probe experiment is not
explained, a concordance precedes its prose definitions, and several passages read as API
inventories. The snapshot's approximately 10,406 prose-and-caption words are already just
above the soft target, so the proposed clarifications should be funded mainly by removing
repetition and implementation catalogues rather than by expanding the chapter.

## P0 findings

No P0 readability, style, or APA findings.

## P1 findings

### P1-1 — Figure 5 reverses the trial vector and residual vector

- **Location:** Section 5.1, Figure 5 Mermaid source, chapter lines 968–976; especially
  lines 969 and 976.
- **Finding:** The first node says that SciPy “requests a trial residual vector,” and the
  return edge from concatenated objective contributions is labeled “trial vector returned.”
  The runtime description in lines 918–938 and the evidence ledger say the opposite:
  SciPy supplies or proposes a trial outer-parameter vector, and pyglotaran returns the
  corresponding residual vector.
- **Proposed correction:** Change node G to “SciPy supplies a trial outer-parameter vector”
  (or “SciPy requests the residual for a trial outer-parameter vector”), and change the
  L-to-G edge label to “residual vector returned.” Retain the caption's explanation that
  the backward edge denotes repetition.
- **Rationale:** This is a terminology and information-flow inconsistency in the chapter's
  principal lifecycle figure. A first-time reader could leave with the optimizer interface
  reversed even though the surrounding prose is correct.

## P2 findings

### P2-1 — The synopsis introduces formal machinery before the ordinary ideas

- **Location:** Section 0, chapter lines 22–32.
- **Finding:** The central thesis paragraph introduces `Experiments`, typed instantiation,
  reference resolution, numerical realization, outer least squares, conditionally linear
  parameters, and extension registries before the chapter has explained their ordinary
  purposes. “Numerical realization” is especially abrupt and is not later given a comparably
  direct plain-language definition.
- **Proposed correction:** Recast the paragraph as a short sequence of responsibilities:
  reusable analysis definitions; separately supplied observations and current values;
  connecting names to what they denote; building the numerical fitting problem; estimating
  shape-changing quantities outside and amplitudes inside; and returning inspectable
  results. Introduce the formal terms only after each ordinary statement, for example:
  “The package then builds the numerical fitting problem—its numerical realization—by
  orienting labeled data and assigning the two kinds of unknown their computational roles.”
  Defer class names to Section 2.
- **Rationale:** The synopsis should provide a map for a reader who does not yet know the
  package or separable least squares. The present terminology is accurate but makes the map
  feel like a compressed summary for an already initiated reader.

### P2-2 — “Pump–probe” is assumed rather than explained

- **Location:** Section 1.1, chapter lines 54–59.
- **Finding:** The first scientific paragraph begins “At one delay after excitation, a
  pump–probe experiment…” but never explains what the pump and probe do. The intended reader
  is not assumed to know spectroscopy.
- **Proposed correction:** Open with the physical sequence: a short pump pulse initiates a
  change; after a chosen delay, a probe measurement records the response across wavelength;
  repeating this at many delays stacks spectra into the measured surface. The existing
  \(t_i\), \(\lambda_j\), row, and column explanation can then follow unchanged.
- **Rationale:** This adds the one missing physical premise and makes the running example
  accessible without increasing mathematical detail.

### P2-3 — Table 1 appears before the terms it is meant to consolidate

- **Location:** End of Section 2.1, chapter lines 263–280; the corresponding prose
  definitions occur in Section 2.2, lines 282–345, and Section 2.3, lines 410–470.
- **Finding:** The terminology concordance introduces the model library, Element,
  Experiment, DataModel, and reference resolution before their concept-first explanations.
  This reverses the skeleton's instruction to place the concordance after prose definitions
  and makes the table do definitional work that the following section immediately repeats.
- **Proposed correction:** Move Table 1 to the end of Section 2.3, after line 470, or split
  off only already-defined scientific terms and leave the software concordance until all
  roles have been explained. Adjust the transition at lines 404–408 so that the moved table
  synthesizes rather than previews.
- **Rationale:** Readers can use a concordance effectively after they have a mental model;
  before that point it functions as an API glossary and weakens the ordinary-language-first
  sequence.

### P2-4 — Several main-text passages are removable API catalogues

- **Location:** Section 2.2, lines 322–330; Section 2.3, lines 412–464; Section 5.2,
  lines 1036–1057.
- **Finding:** These passages enumerate `DataModel.data`, `Scheme.from_dict(...)`,
  discriminated unions, Pydantic, several resolution methods, the temporary parameter
  collection, individual diagnostic fields, and save/load mechanics. The facts are
  well-supported, but their method-by-method presentation interrupts the responsibility and
  information-flow argument. Pydantic is also named without explaining why a scientist
  should care about that library.
- **Proposed correction:** Keep one implementation anchor per responsibility and move the
  remaining names to tables or the evidence ledger. For example, reduce lines 322–330 to:
  “At runtime a data model may carry a source reference or an associated labeled array, but
  its responsibility remains to specify how those observations are modeled.” In Section
  2.3, retain the three conceptual steps—construct typed objects, connect references, report
  supported issues—while removing the call sequence and test narration. In Section 5.2,
  group fields into termination/evaluation diagnostics, fit-size statistics, local
  uncertainty information, and retained histories rather than listing each field.
  Use some of the saved space for one concrete Section 2.3 reminder showing how the two
  temporal contributions and their rate-parameter labels are connected in the running
  example.
- **Rationale:** The contract excludes low-value API catalogues and asks class names to
  serve as anchors rather than the organizing principle. These are the clearest places where
  implementation detail overtakes the scientific question.

### P2-5 — A specialized layout exception is explained twice before its term is useful

- **Location:** Section 3.1, lines 515–521, and Section 4.2, lines 722–729.
- **Finding:** The transposed-and-flattened “global-element path” is introduced in Section 3
  without a plain explanation of a global Element, then repeated in the formal weighting
  discussion. The exception is needed to qualify universal matrix-orientation claims, but
  the first occurrence adds implementation load without advancing the running example.
- **Proposed correction:** In Section 3.1, retain only the qualification that some supported
  contribution types use a combined flattened layout, without naming internal wrapper
  details. Keep the fuller explanation once in Section 4.2, where it directly justifies the
  general weighting operator \(\mathcal{W}_q\).
- **Rationale:** Consolidating the exception preserves accuracy, removes repetition, and
  lets Section 3 maintain the time-trace-at-each-wavelength intuition.

### P2-6 — Several formal terms still precede their ordinary explanations

- **Location:** Section 4.2, lines 741–757; Section 5.2, lines 1032–1048; Section 6.1,
  lines 1082–1088; Section 6.2, lines 1208–1214 and 1227–1229.
- **Finding:** “Variable projection,” “provenance,” “persistence,” “registries,” “entry
  points,” “simulation,” and “ecosystem” are named and then glossed. The appositive
  explanations are generally clear, but the sequence conflicts with the chapter's binding
  ordinary-language-before-formal-term style.
- **Proposed correction:** Invert the key sentences. Examples: “At every outer trial, the
  program solves the linear coefficients afresh and leaves them out of the outer search
  vector; this strategy is variable projection”; “The element identifier records where an
  output came from, a specific form of provenance”; and “Pyglotaran keeps three directories
  of named implementations, called registries.” Use the same pattern for installed-package
  metadata (“entry points”), generating expected data (“simulation”), and the cooperating
  external tools (“ecosystem”).
- **Rationale:** The correction is small but consistently lowers the entry barrier for a
  reader without Python or optimization vocabulary.

### P2-7 — The uncertainty quantities are qualified but not actually defined

- **Location:** Section 4.3, lines 808–815; repeated field inventory in Section 5.2,
  lines 1036–1045.
- **Finding:** Degrees of freedom, covariance, standard errors, and the Jacobian are listed
  and appropriately restricted to local diagnostics, but their ordinary meanings are not
  supplied. The skeleton explicitly assigns short, restrained definitions to Section 4.3.
- **Proposed correction:** Add two compact sentences in Section 4.3: identify the Jacobian
  as the derivative matrix describing local residual sensitivity; explain degrees of freedom
  as an implemented count relating residual information to fitted quantities; and describe
  covariance/standard errors as local uncertainty summaries derived from that least-squares
  geometry under the implementation's assumptions. Then shorten Section 5.2 to a reminder
  and cross-reference rather than a second field list.
- **Rationale:** Qualification tells the reader what not to infer, but a bachelor-level
  explanation must also say what the reported quantities are intended to summarize.

### P2-8 — Repeated “fit is not proof” cautions dilute rather than strengthen the message

- **Location:** Section 1.1, lines 106–113; Section 4.1, lines 689–693; Section 5.1,
  lines 938–943; Section 5.2, lines 1043–1065; conclusion, lines 1318–1322 and 1332–1338.
- **Finding:** The important limits on mechanism truth, uniqueness, identifiability,
  convergence, and automated validation recur in near-equivalent form across adjacent
  sections. The repetition is scientifically responsible, but by the fourth or fifth
  statement it becomes defensive and consumes space needed for definitions and bridges.
- **Proposed correction:** Keep the full identifiability explanation in Section 1.1, the
  statistical qualification in Section 4.3, one concise validation boundary in Section 5.2,
  and one final scope sentence in the conclusion. Convert the intervening occurrences to
  brief cross-references or use their space for the next-section bridge.
- **Rationale:** A warning gains force when it is defined once, applied where it matters,
  and recalled concisely. This edit would also bring the prose closer to the soft word
  target without weakening restraint.

### P2-9 — Figure 1's caption does not distinguish its three arrow meanings

- **Location:** Figure 1, chapter lines 80–104, especially caption lines 102–104.
- **Finding:** The caption says that arrows mean “contributes to the proposed sum,” but the
  arrows from temporal profiles and spectra to contribution surfaces mean multiplicative
  combination, the arrows into the sum mean addition, and the final labeled arrow means
  approximation.
- **Proposed correction:** State all three meanings explicitly: profile/spectrum arrows
  combine multiplicatively to form a contribution surface; arrows from the two surfaces and
  unexplained variation add terms to the proposed sum; the labeled final arrow means that
  the sum approximates the measured surface.
- **Rationale:** The diagram is the reader's first visual model of separability. Its caption
  should remove, not introduce, ambiguity about multiplication versus addition.

### P2-10 — Most figures appear before a prose callout

- **Location:** Mermaid blocks for Figures 2–6 begin at chapter lines 178, 347, 817, 956,
  and 1142; the fuller walkthroughs of Figures 3–6 follow at lines 380, 858, 999, and 1200.
- **Finding:** Figure 1 is announced in advance at line 77, but Figures 2–6 are first named
  in their captions and are explained mainly afterward. Figure numbering itself correctly
  follows order of appearance.
- **Proposed correction:** Add or move one orienting sentence immediately before each
  diagram, such as “Figure 4 follows one outer trial through matrix construction, the inner
  coefficient solve, and residual return.” Reuse the existing post-figure walkthrough
  sentences rather than adding new material.
- **Rationale:** Forward callouts tell the reader what relationship to look for before
  confronting a dense diagram and satisfy conventional academic first-mention order.

### P2-11 — Several subsections close without the promised bridge

- **Location:** Ends of Sections 1.1 (lines 115–120), 3.1 (lines 532–538), 4.2
  (lines 751–757), and 6.2 (lines 1227–1237).
- **Finding:** These endings finish a definition or inventory but do not explicitly pose
  the next question. Other transitions in the chapter are stronger, particularly
  Sections 2.1, 2.2, 3.2, 3.3, and 4.3.
- **Proposed correction:** Replace, rather than append to, a final sentence in each location
  with the skeleton's causal bridge: from observation-model information to the estimation
  cycle; from one oriented dataset to joint coordination; from the inner coefficient solve
  to the remaining outer mismatch; and from ecosystem boundaries to their coordination
  costs.
- **Rationale:** Consistent question-to-question transitions are central to the requested
  van-Stokkum-inspired explanatory flow and keep the architecture from reading as adjacent
  component descriptions.

### P2-12 — APA ordering and citation placement need three local corrections

- **Location:** Section 1.2, lines 124–130; Section 2.1, lines 227–235; Section 4.2,
  lines 746–749.
- **Finding:** The multiple-work citation at line 748 is not alphabetized by first author:
  `(van Stokkum et al., 2004; Mullen & van Stokkum, 2007)`. In addition, the citations at
  lines 130 and 235 sit after clauses about the staging-specific “global dimension” and
  present names/relationships. Although the prose explicitly limits their authority, the
  placement can visually attach literature citations to claims that the current source,
  not the papers, supports.
- **Proposed correction:** Change line 748 to
  `(Mullen & van Stokkum, 2007; van Stokkum et al., 2004)`. Move the 2004 citation to the
  end of the sentence defining global analysis, before the sentence contrasting the global
  dimension. Move the 2023 citation immediately after “the earlier published rationale for
  modular, reusable model definitions,” leaving the current-source authority clause
  uncited by that paper.
- **Rationale:** APA 7 orders different authors alphabetically within one parenthesis.
  More precise placement also makes the v0.7-literature/v0.8-staging evidence boundary
  unmistakable.

### P2-13 — Name the development snapshot exactly and close the remaining DOI-verification gap

- **Location:** Staging-scope statements at chapter lines 34–40 and 1332–1336; references
  at lines 1342–1348.
- **Finding:** “v0.8 staging” is directionally correct, but the inspected package declares
  `0.8.0.dev0`; using the exact development label would more clearly distinguish this
  snapshot from a released or stable v0.8 interface. The reference entries match the PDF
  title pages and APA helper. However, the two *Journal of Statistical Software* PDFs do
  not print or embed their self-DOIs, so the otherwise plausible DOI URLs remain locally
  inferred, as the ledger itself records at lines 306–314.
- **Proposed correction:** Use “the inspected `0.8.0.dev0` staging snapshot at revision …”
  in the synopsis and “the inspected `0.8.0.dev0` staging source” in the conclusion. Before
  final freeze, verify `https://doi.org/10.18637/jss.v018.i03` and
  `https://doi.org/10.18637/jss.v049.i03` against authoritative DOI or JSS records. No
  reference-text change is indicated if they resolve to the cited articles; if external
  verification is not performed, retain the existing local-evidence qualification in the
  production record rather than claiming PDF-level DOI confirmation.
- **Rationale:** Exact development-version wording prevents an accidental stability
  implication. The DOI action addresses the only remaining metadata qualification; the
  author, year, title, journal, volume, issue, pages, diacritics, alphabetization, and
  cited/reference matching otherwise pass.

## P3 findings

No additional P3 enrichment is recommended. The running example already has sufficient
coverage; the priority is to make its Section 2 connection more concrete while shortening
catalogues, not to add another figure, equation, or example.

## Recommendation and hash confirmation

**Recommendation: revise.** After correcting Figure 5 and the prioritized P2 issues, the
chapter should be suitable for acceptance from this review perspective. The scientific
arc, central terminology, running-example continuity, restrained claims, reference matching,
and explicit v0.7-paper versus staging-source boundary are fundamentally sound.

The files reviewed match the frozen snapshot:

- Chapter SHA-256:
  `B8104026C07928A8832809B194B9431215B7A37F058E06D0EC0772E5F5327A17`
- Evidence-ledger SHA-256:
  `59D87C496049A82E1AA29262AFAF775DEE83AA7E877E1E1FAAE79B57FAD63D8B`
