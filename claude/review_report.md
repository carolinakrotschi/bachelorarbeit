# Final QC Review — "Michelson Interferometer for Correction of Translation Stage Deviation"

**Method note:** This is a fresh review of the current working tree (uncommitted changes on top of commit `52e70f4`), which itself already fixes most items from the previous review round (bibliography language-field leak, figure overflow, PI/Thorlabs stage inconsistency, conclusion vs. requirements contradiction, truncated serial numbers, broken sentence in Ch. 4, FRS/FRIS acronym). All 19 `.tex` files and `sources/bachelorarbeit.bib` were read in full. The project was recompiled from scratch with `pdflatex`+`biber` (3 passes, into `compilation/`, which is gitignored) to obtain a ground-truth PDF and check for LaTeX warnings; the final pass produced **zero** warnings (no undefined references, no overfull/underfull boxes). No source file was modified.

---

## 1. Typos, Grammar, Language, Notation

| # | Sev | Location | Issue | Why | Suggested fix |
|---|-----|----------|-------|-----|----------------|
| 1 | **High** | `chapters/chapter-02.tex:218–260` | Symbol `d` is used for three incompatible quantities within one subsection: "optical path difference" (L218, L221, L228, L236), then "mechanical mirror displacement" per the prose at L250, then literally both at once in `d = 2d_{\mathrm{mirror}}` (L253), then "stage displacement" again at L257/L260 (`d = N\lambda/2`). | This is a regression from the current edit pass: `\Delta s` (path difference) was renamed to `d` at L218/221/228/236, colliding head-on with the pre-existing use of `d` for mechanical mirror/stage displacement everywhere else in the chapter (figure caption L173, L257–260, L334, and all of Ch. 4). The bridging equation `d = 2d_{\mathrm{mirror}}` at L253 is self-contradictory as written: the sentence immediately before it (L250) calls the *mechanical* displacement "\(d\)", but the equation then uses `d` for the *optical path difference* and introduces `d_{\mathrm{mirror}}` for the mechanical quantity — the opposite of what the sentence just said. A reader cannot resolve which quantity `d` denotes without guessing from context. | Reintroduce a distinct symbol for the optical path difference (e.g. restore `\Delta s`) for L218–241, keep `d` exclusively for the mechanical mirror/stage displacement as used everywhere else, and rewrite L250–255 as "\(\Delta s = 2d\)" (path difference equals twice the mechanical displacement) — this was in fact the correct, simpler relation before this edit. |
| 2 | Moderate | `chapters/chapter-03.tex:48` | Figure 3.2 caption: 1023P spectrum is implied unsaturated (used to represent both sources), but the next sentence lists 1023P among the "minor saturation" spectra. | "...Therefore, the unsaturated spectrum is used to represent both sources. Although minor saturation occurred for some spectra (such as the Uniphase 1507P **and 1023P**)..." — the caption first uses 1023P's spectrum specifically *because* it is unsaturated (in contrast to 1103P/1177761), then two sentences later says 1023P itself had minor saturation. Internally inconsistent within the same caption. | Clarify: either "minor saturation, distinct from the severe saturation of 1103P (1177761), occurred for 1507P and 1023P but did not prevent accurate peak determination" or drop 1023P from the second list if it was in fact unsaturated. |
| 3 | Low | `chapters/chapter-04.tex` (equation formatting, unchanged from prior review) | Display equations inconsistently use numbered `\begin{equation}` (18×) vs. unnumbered `\[ \]` (11×) with no discernible rule, e.g. the cooldown-time equations (L144–146, L154–158) are numbered while the structurally identical `I_min`/`I_max` thresholds (L52–74), `N=5` (L108–110), and `N_dark=N_bright=3` (L130–134) are not. | None of Ch. 4's equations are ever cross-referenced via `\eqref`, so the numbering currently serves no functional purpose; the split looks like an editing artifact rather than a deliberate convention. `chapter-02.tex` by contrast numbers all display equations consistently. | Pick one convention (recommend: number only equations later referenced) and apply uniformly across Ch. 4. |

---

## 2. Cross-references and Links

**Structural scan (automated, all `.tex` files, fresh 3-pass `pdflatex`+`biber` compile):** every `\ref`/`\eqref`/`\autoref` target resolves to an existing `\label` (0 broken refs, 0 "Label(s) may have changed" after final pass); every `\prismcite{N}` (76 call sites, N∈1–42) maps to a `cite:N` label in `sources/citation_instances.tex`; every `\fullcite{key}` resolves to an entry in `sources/bachelorarbeit.bib`. No undefined-reference or undefined-citation warnings in the final log.

| # | Sev | Location | Issue | Why | Suggested fix |
|---|-----|----------|-------|-----|----------------|
| 1 | Low | `chapters/chapter-02.tex:214` | `\label{eq:time_averaged_intensity}` is defined but never used in any `\eqref`. | Not wrong, just dead weight — every other equation label in the document is referenced at least once. | Remove the label, or reference it where \(\bar I_T\) is reused in the fringe-counting discussion. |

*(The previous review's item — "chapter-05.tex cites 'the introduction' for content not present there" — no longer applies: `chapters/introduction.tex:13–16` now explicitly discusses the direction-of-motion requirement, and `chapter-05.tex:111` no longer contains an explicit "as discussed in the introduction" back-reference. Resolved.)*

---

## 3. Formatting Consistency

| # | Sev | Location | Issue | Why | Suggested fix |
|---|-----|----------|-------|-----|----------------|
| 1 | **High** | `sources/bachelorarbeit.bib:91` (renders in printed bibliography, entry [4], p. 56) | `booktitle` field contains `\&amp;`, printing literally as **"Electro-Optics Europe &amp; European Quantum..."** in the compiled PDF. | Confirmed by text-extracting the freshly compiled PDF: entry [4]'s booktitle shows the raw HTML entity `&amp;` instead of a rendered ampersand. Root cause: the field was copied from an HTML-escaped source (`\&` for LaTeX plus a leftover literal `amp;`) without cleanup. Entry [5]'s `shorttitle` (`sources/bachelorarbeit.bib:103`) has the same underlying string but correctly escaped as `\&` alone — direct evidence this is a copy-paste artifact, not a stylistic choice. | Change `\&amp;` to `\&` at `sources/bachelorarbeit.bib:91`. |
| 2 | **High** | `chapters/chapter-02.tex:463`, citation `\prismcite{37}` → `sources/bachelorarbeit.bib:349` / `sources/citation_instances.tex:37` | Claim about the **Thorlabs LTS300C/M** stage's operating principle (lead screw + rolling-element linear bearings) is footnoted with the **Physik Instrumente (PI) L-836 user manual** — a different, no-longer-used stage. | The current edit pass replaced all PI-stage hardware references with the Thorlabs LTS300C/M throughout the thesis (confirmed consistent in `appendix/appendix.tex`, `chapter-05.tex`) but missed updating this citation. `sources/citation_instances.tex:37` still points to `piUserManualL836`, titled "User Manual for the L-836 Stepper Motor Linear Stage" (PI GmbH), which is not a valid source for a claim now explicitly made about a different manufacturer's product. | Replace citation 37 with the Thorlabs LTS300C/M datasheet/manual, or with a generic lead-screw/linear-bearing reference (citation 38, Slocum's *Precision Machine Design*, already covers this generically and is cited alongside it). |
| 3 | Moderate | `chapters/chapter-03.tex:56,61,69,75` vs. `appendix/appendix.tex:39` | The beam-profiling camera is called the **"RayCi beam profiling camera"** in Ch. 3 (used 3×, including in a figure-caption device label "CAM"), but **"RayCi software"** in the same chapter (2×), while the appendix equipment table lists the actual hardware as **Cinogy CinCam CMOS-120** with no mention of "RayCi" at all. | RayCi and CinCam are two distinct Cinogy products (RayCi = beam-analysis software, CinCam = the camera hardware) per the appendix's own separate listing; Ch. 3 conflates them by calling the camera itself "RayCi," which is inconsistent with the appendix and internally inconsistent between "RayCi camera" and "RayCi software" within the same chapter. | Rename to "CinCam beam profiling camera" (or "Cinogy CinCam CMOS-120") wherever the hardware is meant (L56, L61 ×2), reserving "RayCi" for the analysis software (L69, L75), matching the appendix. |
| 4 | Low | `chapters/chapter-03.tex:52` | "The Uniphase HeNe laser sources emitted wavelengths close to the expected wavelength of approximately 632.8 nm." — plain-text "nm" without `\,\mathrm{}` math formatting, unlike the rest of the document (e.g. `\(632.8\,\mathrm{nm}\)` at `chapter-02.tex:400`). | Minor unit-typesetting inconsistency; this is the only place a laser wavelength is given entirely in plain text rather than math mode. | Change to `\(632.8\,\mathrm{nm}\)` for consistency with `chapter-02.tex:400` and Table 3.1. |

*(Previously flagged items — bibliography `language`-field leak, Figure 3.2 overfull hbox at `width=1.05\linewidth`, truncated laser serial numbers in Table 3.2/Fig. 3.4, `MgF2`/`10mm` plain-text formatting in `chapter-05.tex` — are all resolved in the current tree: `preamble_thesis.tex:185` now suppresses the language field via `\DeclareListFormat{language}{}`, Fig. 3.2 uses `width=\linewidth` with no overfull box in the fresh compile log, Table 3.2/Fig. 3.4 captions use full serial numbers matching Table 3.1, and `chapter-05.tex:129` now uses `\(\mathrm{MgF}_2\)`/`\(10\,\mathrm{mm}\)`.)*

---

## 4. Derivations and Calculations

**Independently re-derived and confirmed correct:**
- Helmholtz → paraxial Helmholtz equation (`chapter-02.tex:12–37`).
- Paraboloidal-wave and complex-beam-parameter Gaussian solution (`chapter-02.tex:39–77`).
- \(M^2\) beam-propagation formula (`chapter-02.tex:134–157`), consistent with the independent definition in `chapter-03.tex:79–83`.
- Michelson intensity derivation (`chapter-02.tex:193–221`): re-derived term by term; \(\bar I_T = 2RTI_0(1+\cos\Delta\varphi)\) confirmed correct.
- Chapter 4 numeric examples recomputed and confirmed: \(\lambda/2 = 787.3\,\mathrm{nm}/2 = 0.394\,\mu\mathrm{m}\) (L186–198); \(1/5\,\mathrm{ms}=200\,\mathrm{Hz}\), \(1/100\,\mathrm{ms}=10\,\mathrm{Hz}\), \(200\times5\,\mathrm{ms}=1\,\mathrm{s}\) (L417–452).
- Fringe-counting result \(d=N\lambda/2\) is, taken on its own (ignoring the notation collision in §1.1 above), still algebraically the correct classical result and consistent with the quadrature-homodyne formula \(d=\lambda\Delta\varphi/(4\pi)\) (`chapter-02.tex:334`) under \(\Delta\varphi=2\pi N\).

| # | Sev | Location | Issue | Why | Suggested fix |
|---|-----|----------|-------|-----|----------------|
| 1 | **High** | `chapters/chapter-02.tex:250–255` | See §1.1 above — the derivation step from "path difference doubling" to "\(d=N\lambda/2\)" is now written as a symbol-colliding, self-contradictory equation (`d = 2d_{\mathrm{mirror}}`) rather than a clean, correctly-labeled relation. | Same root cause as §1.1, listed here because it is specifically a derivation-chain defect: a reader trying to verify the step from "one fringe per wavelength of path-difference change" to "\(d=N\lambda/2\)" cannot follow the logic as currently notated. | Same fix as §1.1 item 1. |

**Scope note:** Appendix A/B contain no equations or derivations.

---

## 5. Factual / Claim Accuracy

No unresolved high-severity issues remain in this category — the two items from the previous review round are both fixed:
- The conclusion (`chapters/conclusion.tex:6`) now explicitly recommends integrating the quadrature homodyne setup for direction-sensing, reconciling it with the stated requirement in the introduction; the camera-based system is now correctly framed as the more *stable* choice, not the final recommended system for direction detection.
- The abstract (`pages/abstract.tex`) and introduction (`chapters/introduction.tex`) now consistently use "field-resolved infrared spectroscopy (FRIS)".

| # | Sev | Location | Issue | Why | Suggested fix |
|---|-----|----------|-------|-----|----------------|
| 1 | Low | `chapters/chapter-02.tex:463`, citation 37 | Same issue as §3 item 2 — flagged here too since it is also a factual-accuracy problem (a claim about hardware X is sourced to hardware Y's manual), not just a formatting one. | See §3 item 2. | See §3 item 2. |

---

## Executive Summary

| Category | Issues found | High | Moderate | Low |
|---|---|---|---|---|
| 1. Typos/Grammar/Notation | 3 | 1 | 1 | 1 |
| 2. Cross-references/Links | 1 (+ clean structural scan) | 0 | 0 | 1 |
| 3. Formatting consistency | 4 | 2 | 1 | 1 |
| 4. Derivations/Calculations | 1 (+ 5 independently re-derived and confirmed correct) | 1 | 0 | 0 |
| 5. Factual/Claim accuracy | 1 (cross-listed with §3.2) | 0 | 0 | 1 |
| **Total (unique issues)** | **9** | **3** | **2** | **4** |

**Top fixes before submission, in priority order:**

1. **Fix the `d` / optical-path-difference notation collision** (§1.1, §4.1) in `chapters/chapter-02.tex:218–260` — this was introduced by the current edit pass while trying to address the *previous* review's feedback, and now makes the fringe-counting derivation self-contradictory as written. Restore a distinct symbol (e.g. `\Delta s`) for optical path difference, keep `d` for mechanical displacement, and state `\Delta s = 2d` explicitly.
2. **Wrong equipment manual cited for the Thorlabs stage** (§3.2/§5.1) — `chapter-02.tex:463` cites the Physik Instrumente L-836 manual (citation 37) to support a claim now explicitly made about the Thorlabs LTS300C/M. Leftover from the PI→Thorlabs hardware-reference cleanup; needs a correct source.
3. **`\&amp;` leaking into the printed bibliography** (§3.1) — `sources/bachelorarbeit.bib:91`, one-character fix (`\&amp;` → `\&`), visible in entry [4] on the bibliography page.
4. **RayCi vs. CinCam naming inconsistency** (§3.3) — Chapter 3 calls the beam-profiling camera "RayCi" (the software's name per the appendix's own equipment table), which is confusing and inconsistent within the document itself.
5. **Figure 3.2 caption self-contradicts on which laser's spectrum was saturated** (§1.2) — minor but worth a one-sentence clarification before submission.

*For reference, issues already resolved by the current (uncommitted) edit pass and not re-flagged above: bibliography `language`-field leak, Figure 3.2 overfull-hbox margin bleed, truncated laser serial numbers in Table 3.2/Fig. 3.4, broken sentence in `chapter-04.tex` (SingleDiodeHandler paragraph), missing motivation for direction-detection in the introduction, conclusion contradicting the stated direction-detection requirement, `MgF2`/`10mm` plain-text formatting, and inconsistent PI/Thorlabs stage references across chapters.*
