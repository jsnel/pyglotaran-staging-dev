# 1. From a measured surface to a scientific analysis

## 1.1 What the experiment measures

At one delay after excitation, a pump–probe experiment records a spectrum: a signal sampled
at many wavelengths. Repeating that measurement at successive delays stacks the spectra into
a surface. In the running example, its rows correspond to sampled delay times \(t_i\), and
its columns to sampled wavelengths \(\lambda_j\). A point on the surface is therefore one
observed signal value at one delay and one wavelength. The experiment may contain thousands
of such values even when the scientific question concerns only a few states or processes.
Time-resolved spectra are an important instance of this broader class of multidimensional
measurements (van Stokkum et al., 2004).

The surface does not display a mechanism directly. If two excited states change on similar
time scales and absorb or emit over overlapping wavelength ranges, their signals appear
together at the same measured points. A ridge or decay in the surface can then admit several
explanations. Instrument response, baseline offsets, measurement noise, and an incomplete
scientific hypothesis can add further structure. The task is consequently an inverse problem:
the researcher observes the combined response and asks which smaller set of processes could
have produced it (van Stokkum et al., 2004).

A useful first hypothesis is that each contribution has two parts. Its *temporal
contribution* describes how its strength changes with delay, while its *associated spectrum*
describes how strongly it appears at each wavelength. With two contributions, the signal at
one point can be understood as the first temporal value multiplied by its spectral value,
plus the corresponding product for the second contribution, plus unexplained variation.
Repeating this construction over all sampled points gives two contribution surfaces whose
sum approximates the observed surface. Figure 2 shows this idea without yet introducing the
matrix notation used in Section 4.

<!-- Insert Mermaid source from ../figures/fig-02-separable-observation.mmd here. -->

**Figure 2. A separable modeling hypothesis for a time-by-wavelength observation.** Arrows
mean “contributes to the proposed sum.” They do not assert a uniquely identified mechanism,
and the diagram does not claim that every dataset is separable.

Separability is thus a modeling assumption rather than a property established merely by
recording two axes. Wavelength-dependent instrument behavior can modify temporal shapes,
and different combinations of profiles and spectra can sometimes reproduce the same
observations. The latter difficulty is *identifiability*: whether the available measurements
can distinguish the quantities or alternative explanations being estimated. Additional
experiments, scientifically justified restrictions, or more detailed measurement assumptions
may be needed. Even an excellent numerical fit does not by itself identify a unique physical
mechanism (van Stokkum et al., 2004).

This distinction also clarifies two meanings of *model*. A *physicochemical model* is the
scientific hypothesis about states, transitions, spectra, and instrument effects. A *model
for the observations* is wider: it combines that hypothesis with assumptions about how the
measurements are organized and how unexplained variation is treated. Pyglotaran ultimately
needs both kinds of information, although no single software object represents the whole
model for the observations.

## 1.2 Global analysis, target analysis, and model discovery

Fitting is not the endpoint. A proposed explanation must be confronted with the full
measurement and revised when its remaining structure or physical interpretation is
inadequate. *Global analysis* supports that comparison by analyzing measurements
simultaneously under shared model structure. For example, temporal behavior may be estimated
from all wavelengths rather than by fitting each wavelength independently. Here *global*
describes a scientific strategy. It must not be confused with the software's *global
dimension*, a coordinate role introduced in Section 3 (van Stokkum et al., 2004).

*Target analysis* asks a more specific question: whether a proposed physicochemical model
can account for the observations and yield interpretable states, rates, or spectra. A kinetic
scheme might specify which states interconvert, while spectral or instrument assumptions add
other parts of the observation model. Global and target analysis are therefore not competing
buttons or separate optimizer modes. They describe different levels of scientific
commitment: simultaneous fitting can begin with flexible temporal components, whereas
target analysis places a more explicit mechanism under test (van Stokkum et al., 2004).

Both strategies belong to an iterative process of scientific model discovery. A researcher
first specifies a candidate explanation, estimates its unknown quantities, and then validates
the result. Validation includes more than checking one error number: residual patterns,
parameter precision, agreement with prior knowledge, and the physical plausibility of fitted
contributions can all motivate revision. The revised model is then estimated and examined
again. TIMP described this as a cycle of model formulation, fitting, and validation, and the
2023 pyglotaran account retained the same scientific organization (Mullen & van Stokkum,
2007; van Stokkum et al., 2023).

This recurring cycle creates a software requirement. Scientific contributions must be
changeable without rebuilding data handling, estimation, and inspection for every candidate
model. Reusable building blocks are valuable only when their meanings and assumptions remain
visible enough to criticize. The need to combine reuse with inspection links the scientific
problem to the software lineage.

## 1.3 Lineage of responsibilities

The lineage is best understood by following responsibilities rather than product names.
TIMP supplied an R-based computational environment for multiway spectroscopy. It supported
model specification, parameter estimation, validation, and extensibility within the
interactive model-discovery cycle (Mullen & van Stokkum, 2007).

Glotaran added a Java desktop working environment around that computational capability. It
provided interactive data exploration, assisted model construction, and result viewing, but
delegated the numerical work to TIMP. Communication between the Java application and R used
Rserve, a server interface through which another program could request R computations.
Glotaran was therefore a graphical front end to TIMP rather than a replacement for its
computational core (Snellenburg et al., 2012).

Pyglotaran was subsequently developed as a complete Python rewrite of the Glotaran/TIMP
computational core. The desktop graphical interface was not recreated as part of that core.
Instead, notebook-centered work and the wider Python ecosystem became the surrounding
environment for combining analysis, narrative, and visualization. Jupyter notebooks are
external scientific workspaces that call pyglotaran; they are not a component inside its
optimizer. The published 2023 account documents this predecessor lineage and ecosystem
shift, while its v0.7-era class names are not evidence for the inspected staging
implementation (van Stokkum et al., 2023).

<!-- Insert Mermaid source from ../figures/fig-01-lineage.mmd here. -->

**Figure 1. Responsibility-centered lineage from TIMP and Glotaran to pyglotaran.** Solid
arrows denote run-time use or orchestration. Dashed arrows denote a historical transfer or
reimplementation of responsibility, not continuity of an application programming interface.

The present architecture can now be examined as a response to the same recurring need:
compose a scientific explanation, estimate it against observations, inspect the evidence,
and revise it without coupling every contribution to a separate analysis program.

<!--
Citations used:
- van Stokkum et al. (2004)
- Mullen and van Stokkum (2007)
- Snellenburg et al. (2012)
- van Stokkum et al. (2023)

Incoming bridge proposal:
The opening synopsis should end by asking why a large measured surface benefits from separating scientific definitions, observations, and estimation responsibilities.
This section begins by making that surface concrete before naming software objects.

Outgoing bridge proposal:
The scientific cycle and responsibility lineage establish the design pressure for reusable, inspectable composition.
Section 2 can therefore begin by asking how the staging architecture divides those responsibilities and connects them without fixing the numerical problem too early.

Five-item self-check:
1. The running example introduces delay time and wavelength without assuming spectroscopy knowledge.
2. Global analysis, target analysis, the two senses of model, inverse problem, validation, and identifiability are defined in ordinary language.
3. Separability is qualified as an assumption, and no estimator equation is introduced.
4. TIMP, Glotaran/Rserve, and the pyglotaran/notebook responsibility shift each have literature support.
5. The prose uses current software vocabulary only where present architecture is discussed and makes no v1 promise.

Integration note:
- Assumptions: The binding project lineage is authoritative for the statement that pyglotaran is a complete Python rewrite of the computational core.
- Deliberate omissions: No matrix orientation, explicit-parameter object, CLP estimator, current object graph, or result-field inventory is introduced.
- Dependencies: The coordinator should embed the two Mermaid sources at the marked positions; Section 3 must define global dimension, and Section 4 owns formal separability equations.
- Proposed contract changes: None.
- Unresolved questions: None. The exact rewrite phrase is supplied by the commission; the 2023 paper supports the predecessor/ecosystem account but does not itself use that exact phrase.
-->
