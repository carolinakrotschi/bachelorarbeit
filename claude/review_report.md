# Final QC Review — "Michelson Interferometer for Correction of Translation Stage Deviation"

**Method note:** The prompt referenced `/build/main.pdf` and `/claude/review_report.md` at the filesystem root; this project instead has `pdf/main_thesis.pdf` (compiled fresh from source for this review) and no `/build/` directory, so the compiled PDF at `pdf/main_thesis.pdf` was used as ground truth and this report was written to `claude/review_report.md` inside the project. All 19 `.tex` files (chapters, appendix, pages, preamble, `sources/citation_instances.tex`) and `sources/bachelorarbeit.bib` were read in full. No source file was modified.

---

## 1. Typos, Grammar, Language, Notation

| # | Sev | Location | Issue | Why | Suggested fix |
|---|-----|----------|-------|-----|----------------|
| 1 | **High** | `chapters/chapter-04.tex:238` | Sentence fragment: "...continuously reads the voltage signal of the photodiode and **The main application**, which coordinates the user interface, the measurement process and the control of the electronic translation stage." | Missing verb before "The main application"; stray mid-sentence capital "The". Reads as if a second clause (introducing a second class/component) was cut short during editing. | Likely intended: "...and a `MainApplication` class, which coordinates..." — restore the missing verb/object structure. |
| 2 | Moderate | `chapters/chapter-02.tex` (waist-position notation) | `z_0` denotes the **Rayleigh length** when first introduced (L57, L60, L89–93: "$z_0$ is the Rayleigh range"), but is later silently redefined as the **beam-waist position** ("By shifting the waist position to $z_0$...", L112). `z_R` (Rayleigh range) appears unexplained inside the boxed Gouy-phase equation at L77, before it is formally introduced at L112. | Same symbol `z_0` is used for two different physical quantities (a length vs. a position) within one chapter; `z_R` is used before being defined. This is exactly the kind of silent-notation-swap the review was asked to catch. | Introduce `z_R` for the Rayleigh range from the start (L57 onward) and reserve `z_0`/`z_{0x}` exclusively for the waist position, or add one sentence at L112 flagging the notation change explicitly. |
| 3 | Low | `chapters/chapter-02.tex:250` | "In the **Michelson Interferometer**, the movement of one mirror..." — Title Case in running prose. | Every other body-text occurrence (13 instances) uses lowercase "Michelson interferometer"; only section/subsection headings are legitimately Title Case. | Lowercase "interferometer" at L250. |

---

## 2. Cross-references and Links

| # | Sev | Location | Issue | Why | Suggested fix |
|---|-----|----------|-------|-----|----------------|
| 1 | **High** | `chapters/chapter-05.tex:111` | "As discussed in the introduction, the interferometer was not only intended to improve the accuracy of the translation stage displacement measurement. A second important requirement was the detection of the direction of motion..." | `chapters/introduction.tex` (read in full, 16 lines) never discusses a direction-of-motion requirement at all — it only discusses positioning-accuracy calibration for FRS/EOS. The back-reference points to content that isn't there. | Either add the direction-detection motivation to `introduction.tex`, or change "the introduction" to "Chapter 2" — Section 2.2.2 (`chapters/chapter-02.tex:260–336`) is where this requirement is actually established and motivated. |
| 2 | Low | `chapters/chapter-02.tex:214` | `\label{eq:time_averaged_intensity}` is defined but never used in any `\eqref`. | Not wrong, just dead weight — every other equation label in the document is referenced at least once. | Remove the label or add the missing `\eqref` where the result is reused (e.g. when $\bar I_T$ is substituted into the fringe-counting discussion). |

**Structural scan (automated, all 19 `.tex` files):** every `\ref`/`\eqref`/`\autoref` target resolves to an existing `\label` (0 broken refs); every `\prismcite{N}` maps to a `cite:N` label in `sources/citation_instances.tex` (all 42, bijective, none unused, none missing); every `\fullcite{key}` resolves to an entry in `sources/bachelorarbeit.bib`. Compiling with `pdflatex`+`biber` produces no "undefined reference" warnings. Spot-checked in the rendered PDF: `[N]` citation numbers and `Figure`/`Table`/`Chapter` cross-references render as correctly-targeted blue hyperlinks (checked pp. 6, 18, 20).

---

## 3. Formatting Consistency

| # | Sev | Location | Issue | Why | Suggested fix |
|---|-----|----------|-------|-----|----------------|
| 1 | **High** | Bibliography, all 42 entries (`sources/bachelorarbeit.bib`, rendered PDF pp. 67–70 / printed pages 55–58) | The `language` field of every `.bib` entry (e.g. `language = {de}` at `sources/bachelorarbeit.bib:318`, `language = {EN}` at line 331) leaks into the printed bibliography as a raw token, e.g. entry [2]: *"Experimentalphysik 2.* **de.** *Springer-Lehrbuch..."*, entry [4]: *"...Liquid Samples". **en.** In: 2025 Conference..."*. The tag's capitalization is even inconsistent between entries (`en.`/`de.` vs `EN.` at entry [3]), because it is copied verbatim from however each source's language code was exported. | This is visible on essentially every bibliography page a reader/examiner will look at — the single most visually conspicuous defect found in the compiled PDF. Root cause confirmed: `preamble_thesis.tex` loads `biblatex` with `style=numeric-comp`, which by default prints the `language` field; nothing currently suppresses it. | Add `\AtEveryBibitem{\clearfield{language}}` to `preamble_thesis.tex` (near the biblatex setup, `preamble_thesis.tex:180`) to suppress the field from being printed while leaving it intact for internal use. |
| 2 | Moderate | `chapters/chapter-03.tex:109-110` (Table 3.2, `tab:m2results`) and Figure 3.4 legend (`chapters/chapter-03.tex:91`, image `all_lasers_combined_fit.png`) | Serial numbers are truncated by exactly one trailing digit compared to Table 3.1 (`tab:wavelengths`) and Table 3.3/Appendix B: "Uniphase 1103P **11777**" / "**110838**" here vs. "Uniphase 1103P **1177761**" / "**1108380**" everywhere else. The plotted legend (visible in the compiled PDF, p. 20) shows the same truncation plus a stray artifact: `uniphase1103p11777`, `uniphase110838`, and `uniphase1507p0` (extra trailing "0" not present in any laser's real name). | Same one-digit truncation appears independently in both the table and the raw plot legend, which strongly suggests an upstream bug in the analysis/plotting script (e.g. a string-slicing or dict-key error) rather than a one-off typo — and the legend text is also unformatted code-style text ("uniphase1023p", "M2 = 4.49") inconsistent with the polished naming used in Table 3.1/3.3 and the appendix ("Uniphase 1023P", "$M^2$"). | Fix the serial-number truncation at its source (analysis script) and regenerate Table 3.2 and Figure 3.4; relabel the plot legend with the properly formatted laser names used elsewhere in the thesis. |
| 3 | Low | `chapters/chapter-05.tex:129` | "The Thorlabs **MgF2** (**10mm** thickness) Wollaston prism..." — plain text, no math-mode subscript, no thin space before the unit. | Identical descriptions elsewhere are properly typeset: `chapters/chapter-02.tex:368` — "magnesium fluoride (\(\mathrm{MgF}_2\))"; `appendix/appendix.tex:53` — "\(\mathrm{MgF}_2\), \(10\,\mathrm{mm}\) thickness". This is the only place in the thesis where this component is described without the standard formatting. | Change to `\(\mathrm{MgF}_2\)` and `\(10\,\mathrm{mm}\)` to match `chapter-02.tex:368` / `appendix.tex:53`. |
| 4 | Low | `chapters/chapter-04.tex` (throughout) | Display equations inconsistently use numbered `\begin{equation}` (18×) vs. unnumbered `\[ \]` (11×) with no discernible rule. Most strikingly, the two cooldown-time equations (L144–146, L154–158) are numbered while the structurally identical definitions immediately before and after them ($I_{\min}$/$I_{\max}$ thresholds L52–74, $N=5$ L108–110, $N_{\mathrm{dark}}=N_{\mathrm{bright}}=3$ L130–134, $d_{\mathrm{fringe}}=\lambda/2$ L180–184) are not. None of chapter 4's equations — numbered or not — are ever cross-referenced via `\eqref`, so the numbering currently serves no functional purpose either way. | `chapters/chapter-02.tex` by contrast numbers all 39 of its display equations consistently. The mixed style in chapter 4 looks like an editing artifact rather than a deliberate convention (e.g. "numbered = important, unnumbered = trivial constant") since the split doesn't track that distinction. | Pick one convention for chapter 4 (recommend: number only equations that are later referenced, per the rest of the document) and apply it uniformly. |
| 5 | Low | `chapters/chapter-03.tex:47` (Figure 3.2, `fig:all_corrected_lasers`) | `\includegraphics[width=1.05\linewidth]{...}` — image deliberately set to 105% of the text width. | Confirmed via the `pdflatex` log: `Overfull \hbox (23.19041pt too wide) in paragraph at lines 47--48`, i.e. the figure overflows the right margin by ~8.2 mm in the compiled PDF. Visually subtle at normal zoom (checked p. 18) but present. | Reduce to `width=\linewidth` (or use `\makebox`/`\hspace*{-...}` deliberately if the bleed is intentional for visual impact). |

---

## 4. Derivations and Calculations

**Independently re-derived and confirmed correct:**
- Helmholtz → paraxial Helmholtz equation (`chapter-02.tex:12–37`): substituting $\tilde E=\tilde u\,e^{-ikz}$ into $\nabla^2\tilde E+k^2\tilde E=0$ and dropping $\partial^2\tilde u/\partial z^2$ (SVEA) reproduces $\nabla_T^2\tilde u - 2ik\,\partial\tilde u/\partial z = 0$ exactly.
- Paraboloidal-wave and complex-beam-parameter Gaussian solution (`chapter-02.tex:39–77`): standard form, dimensionally and algebraically consistent.
- $M^2$ beam-propagation formula (`chapter-02.tex:134–157`) is dimensionally consistent and algebraically equivalent to the definition $M^2=\pi w_0\theta/\lambda$ given independently in `chapter-03.tex:79–83` — the two chapters are consistent with each other.
- Michelson intensity derivation (`chapter-02.tex:177–221`): re-derived $[\cos(\omega t+\varphi_1)+\cos(\omega t+\varphi_2)]^2$ term by term (time-averaging $\cos^2\to 1/2$, product-to-sum for the cross term) and confirmed it reproduces $\bar I_T = c\varepsilon_0 RT A_l^2(1+\cos\Delta\varphi)$, and with $I_0=\tfrac12 c\varepsilon_0 A_l^2$ this correctly simplifies to $\bar I_T=2RTI_0(1+\cos\Delta\varphi)$.
- Fringe-counting result $d=N\lambda/2$ (`chapter-02.tex:252–258`) is consistent with the quadrature-homodyne displacement formula $d=\lambda\Delta\varphi/(4\pi)$ (`chapter-02.tex:326–330`): setting $\Delta\varphi=2\pi N$ in the latter recovers the former exactly.
- Chapter 4 numeric examples recomputed and confirmed: $\lambda/2 = 787.3\,\mathrm{nm}/2 = 0.394\,\mu\mathrm{m}$ (`chapter-04.tex:186–198`); $1/5\,\mathrm{ms}=200\,\mathrm{Hz}$, $1/100\,\mathrm{ms}=10\,\mathrm{Hz}$, $200\times5\,\mathrm{ms}=1\,\mathrm{s}$ (`chapter-04.tex:417–452`).

| # | Sev | Location | Issue | Why | Suggested fix |
|---|-----|----------|-------|-----|----------------|
| 1 | Moderate | `chapters/chapter-02.tex:183–191` | $E_1=\sqrt{RT}A_l\cos(\omega t+\varphi_1)$, $E_2=\sqrt{RT}A_l\cos(\omega t+\varphi_2)$ implicitly assumes a lossless, reciprocal beam splitter ($R+T=1$, one reflection + one transmission per arm, no absorption). | Unstated assumption: nothing in the text says the beam splitter is lossless before this substitution is used. | Add one clause, e.g. "for an ideal, lossless beam splitter ($R+T=1$)..." |
| 2 | Moderate | `chapters/chapter-02.tex:218–258` | The relation $\Delta s = 2d$ (round-trip path-difference change equals twice the *mechanical* mirror displacement $d$) is used implicitly between the general phase-difference equation (in terms of $\Delta s$, L218–221) and the fringe-counting result $d=N\lambda/2$ (in terms of $d$, L252–258), but is never explicitly written down. | A reader who only has $\Delta\varphi = 2\pi/\lambda\,\Delta s$ cannot get from there to $d=N\lambda/2$ without independently supplying $\Delta s=2d$, which isn't stated anywhere in the chapter. | Insert one line linking $\Delta s = 2d$ for a single moving mirror before or inside §2.2.1.3 "Fringe Counting". |

**Scope note:** Appendix A (AI-tool disclosure) and Appendix B (equipment table) contain no equations or derivations — there is nothing in the current Appendix to independently re-derive.

---

## 5. Factual / Claim Accuracy

| # | Sev | Location | Issue | Why | Suggested fix |
|---|-----|----------|-------|-----|----------------|
| 1 | **High** | `chapters/conclusion.tex:6–8` | "...the Thorlabs diode laser together with **the camera-based detection system** is the most suitable choice for integration into the final setup... the camera-based detection method is expected to provide more reliable results for future measurements." | This recommends the conventional (camera-based) Michelson configuration, which — per the thesis's own theory (`chapter-02.tex:264–270`, `pages/abstract.tex:11`) — **cannot determine direction of motion**. `chapters/chapter-05.tex:111` frames direction detection as "a second important requirement" needed "in order to enable active correction." The conclusion recommends a system that structurally cannot meet this stated requirement and never addresses the gap. | Either recommend the quadrature-homodyne (photodiode) system despite its noise disadvantage, propose a hybrid (camera for stability + homodyne for direction), or add a paragraph in §"Final System" explicitly explaining why direction-sensitivity is being deprioritized. |
| 2 | Low | `pages/abstract.tex:5` vs. `chapters/introduction.tex:11` | Abstract: "a **mid-infrared pump-probe spectroscopy** experiment." Introduction: "**field-resolved infrared spectroscopy (FRS)** based on **electro-optic sampling (EOS)**." | These name two different measurement techniques; FRS/EOS is not generally synonymous with "pump-probe spectroscopy" in the ultrafast-optics literature, even though both use a delay stage. If both phrasings describe the same underlying experiment, a reader could be confused by the inconsistent naming between the two most-read sections of the thesis. | Use one consistent name (or explicitly note "a pump-probe-style FRS/EOS setup") in both places. |

*(See also §2, item 1 — the same underlying issue, viewed as a broken cross-reference rather than a content contradiction.)*

---

## Executive Summary

| Category | Issues found | High | Moderate | Low |
|---|---|---|---|---|
| 1. Typos/Grammar/Notation | 3 | 1 | 1 | 1 |
| 2. Cross-references/Links | 2 (+ clean structural scan) | 1 | 0 | 1 |
| 3. Formatting consistency | 5 | 1 | 1 | 3 |
| 4. Derivations/Calculations | 2 (+ 6 independently re-derived and confirmed correct) | 0 | 2 | 0 |
| 5. Factual/Claim accuracy | 2 | 1 | 0 | 1 |
| **Total** | **14** | **4** | **4** | **6** |

**Top 5 fixes before submission, in priority order:**

1. **Bibliography `language`-field leak** (§3.1) — add `\AtEveryBibitem{\clearfield{language}}` to `preamble_thesis.tex`. Affects all 42 entries on 4 printed pages; the single most visible defect in the compiled PDF.
2. **Conclusion contradicts the project's own stated requirements** (§5.1) — the recommended final system (camera-based) cannot do the one thing (direction detection) that motivated building the quadrature-homodyne interferometer in the first place. Needs an explicit reconciling paragraph at minimum.
3. **Missing/misplaced motivation for direction detection** (§2.1) — `chapter-05.tex:111` cites "the introduction" for content that isn't in `introduction.tex`; either add it there or repoint the reference to Chapter 2.
4. **Broken sentence in Chapter 4** (§1.1) — `chapter-04.tex:238`, currently unparseable as written.
5. **Truncated laser serial numbers in Table 3.2 / Figure 3.4** (§3.2) — same one-digit truncation in two independent places points to a real upstream data/labeling bug worth fixing at the source before the plots and table are considered final.
