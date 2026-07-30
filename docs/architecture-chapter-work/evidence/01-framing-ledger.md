# Packet A evidence ledger: scientific framing and lineage

The literature was inspected locally from the supplied PDFs. PDF page numbers below are
one-based file pages; journal page numbers are added where they are visible. Title pages were
also rendered and visually checked. Claims are paraphrases, not quotations.

| Claim ID | Proposed claim | Class | Primary evidence | Corroborating evidence | Confidence | Safe wording | Draft location |
|---|---|---|---|---|---|---|---|
| FR-001 | A time-resolved spectrum can be formed by measuring a spectroscopic signal over both delay time and wavelength after a short excitation. | Scientific definition | `Literature/van_Stokkum_et_al-Global_and_target_analysis_of_time-resolved_spectra.pdf`, PDF pp. 2–3 (journal pp. 83–84), introduction and §2.1 | `Literature/van_Stokkum_et_al-pyglotaran_a_lego_like_framework_for_gta.pdf`, PDF pp. 1–2 (journal pp. 2413–2414) | High | In the running pump–probe example, spectra recorded at successive delays form a time-by-wavelength surface. | §1.1 |
| FR-002 | Treating the measured surface as a sum of temporal contributions multiplied by associated spectra is a separability assumption, not a fact guaranteed by the data. | Scientific definition | 2004 review, PDF p. 4 (journal p. 85), §2.2.2, including the stated wavelength-dependent caveat | 2004 review, PDF pp. 9–11 (journal pp. 90–92), §§2.6–2.7 | High | Under a separability assumption, a small number of temporal profiles and associated spectra can approximate the surface; instrument and system behavior can violate or qualify that assumption. | §1.1; Fig. 2 |
| FR-003 | Recovering kinetic and spectral properties from observed signals is an inverse problem, and different decompositions or mechanisms may not be identifiable from one dataset. | Scientific definition | 2004 review, PDF pp. 4–5 (journal pp. 85–86), §§2.3–2.4 | 2004 review, PDF pp. 9–10 (journal pp. 90–91), §§2.6.1–2.6.2 | High | A fit need not uniquely reveal the generating mechanism; identifiability asks whether the available observations distinguish the proposed quantities or alternatives. | §1.1 |
| FR-004 | A physicochemical model and a model for the observations are different: the latter also includes measurement and stochastic assumptions. | Scientific definition | 2004 review, PDF p. 3 (journal p. 84), opening of §2 | 2004 review, PDF p. 1 abstract and PDF p. 15 (journal p. 96), §3 | High | Use *physicochemical model* for the scientific hypothesis and *model for the observations* for the wider predictive description that includes measurement organization and unexplained variation. | §§1.1–1.2 |
| FR-005 | Global analysis is simultaneous analysis of measurements under shared model structure; it is a method, not an axis. | Scientific definition | 2004 review, PDF p. 2 (journal p. 83), introduction; PDF p. 10 (journal p. 91), §2.6.2 | 2023 pyglotaran paper, PDF p. 2 (journal p. 2414), introduction | High | Global analysis considers measurements together so that shared structure constrains them jointly. Do not equate it with the later software term *global dimension*. | §1.2 |
| FR-006 | Target analysis tests or estimates a specified physicochemical model and seeks physically interpretable quantities. | Scientific definition | 2004 review, PDF pp. 2, 10 (journal pp. 83, 91), introduction and §2.6.2 | TIMP paper, PDF p. 2, §1.1; 2023 paper, PDF pp. 2–3 (journal pp. 2414–2415) | High | Target analysis places a proposed kinetic or other physicochemical structure under test; a good fit is evidence to assess, not proof of the mechanism. | §1.2 |
| FR-007 | Scientific model discovery is an iterative cycle of specification or formulation, estimation, validation, and revision; validation includes residual structure, parameter precision, and physical interpretability. | Scientific definition | `Literature/Mullen_et_al-TIMP.pdf`, PDF p. 2, §1.1 and Figure 1 | 2004 review, PDF p. 15 (journal p. 96), §3; 2023 paper, PDF pp. 13–15 (journal pp. 2425–2427), §§4–4.3 | High | Estimation is one stage in a cycle: propose, estimate, inspect numerical and physical adequacy, and revise when needed. | §1.2 |
| FR-008 | TIMP was an R package and problem-solving environment that owned the computational and mathematical work for multiway spectroscopic model discovery. | Historical fact | TIMP paper, rendered title page and PDF pp. 1–2, abstract and §1.1 | TIMP paper, PDF p. 38, conclusion; Glotaran paper, PDF p. 1, abstract | High | TIMP supplied the R-based computational environment for specifying, fitting, and validating spectroscopic models. | §1.3; Fig. 1 |
| FR-009 | Glotaran was a Java graphical front end that delegated computation to TIMP through Rserve rather than replacing the R core. | Historical fact | `Literature/Snellenburg_et_al-Glotaran.pdf`, rendered title page and PDF p. 1, abstract | Glotaran paper, PDF pp. 15–17, §4 and conclusion | High | Glotaran supplied interactive desktop exploration, model editing, and result viewing; communication with the R/TIMP computational side used Rserve. | §1.3; Fig. 1 |
| FR-010 | Pyglotaran is the Python rewrite of the earlier Glotaran/TIMP computational core; the desktop GUI was not recreated in that core, and external notebooks and the Python ecosystem became the surrounding workflow. | Historical fact | Frozen editorial contract §5, binding historical lineage | 2023 paper, PDF pp. 1, 15–17 (journal pp. 2413, 2427–2429), §§4.4–4.6 and Table 3, which document the Python framework, predecessor lineage, external tools, Jupyter notebooks, and ecosystem boundary | High for the commissioned lineage; medium-high for wording attributable solely to the paper | State the rewrite as the project lineage supplied for this chapter. Cite the 2023 paper for its published predecessor/ecosystem account, while avoiding claims that its v0.7 names describe staging. | §1.3; Fig. 1 |
| FR-011 | The four primary references have the author, year, venue, pagination, and DOI metadata specified in the frozen APA contract. | Historical fact | Rendered first pages of all four supplied PDFs: 2004 BBA 1657, 82–104, DOI `10.1016/j.bbabio.2004.04.011`; 2007 JSS 18(3), 1–46; 2012 JSS 49(3), 1–22; 2023 PPS 22, 2413–2431, DOI `10.1007/s43630-023-00460-y` | PDF metadata checked with Poppler `pdfinfo`; JSS title pages identify issues 18(3) and 49(3), and provisional DOI strings in the frozen contract are `10.18637/jss.v018.i03` and `10.18637/jss.v049.i03` | High | Use the contract's APA entries, preserving Jörn Weißenborn's diacritic and lowercase “van”; the coordinator owns the consolidated reference list. | Section citations and integration note |

## Metadata check summary

- van Stokkum, Larsen, and van Grondelle: title page visibly reports *Biochimica et
  Biophysica Acta* 1657 (2004), 82–104 and DOI
  `https://doi.org/10.1016/j.bbabio.2004.04.011`.
- Mullen and van Stokkum: title page visibly reports January 2007, *Journal of Statistical
  Software*, volume 18, issue 3; the DOI in the frozen contract is
  `https://doi.org/10.18637/jss.v018.i03`.
- Snellenburg, Laptenok, Seger, Mullen, and van Stokkum: title page visibly reports June
  2012, *Journal of Statistical Software*, volume 49, issue 3; the DOI in the frozen
  contract is `https://doi.org/10.18637/jss.v049.i03`.
- van Stokkum, Weißenborn, Weigand, and Snellenburg: title page visibly reports
  *Photochemical & Photobiological Sciences* 22 (2023), 2413–2431 and DOI
  `https://doi.org/10.1007/s43630-023-00460-y`.

## Evidence-bound caution

The 2023 paper describes a v0.7-era surface and uses historical software vocabulary that is
not imported into the staging chapter. Its scientific-cycle and ecosystem account is used,
while current class and field names come from staging source. The exact phrase “complete
Python rewrite” is supplied by the binding project lineage in the commission; the paper
independently supports the change in computational and working-environment responsibilities
but does not itself use that exact phrase.
