---
name: evidence-appraisal
version: "1.2"
description: >-
  Appraise a clinical protocol or manuscript against the standard reporting and
  quality-appraisal instruments — PRISMA 2020, PRISMA-NMA, ROBIS, AMSTAR-2,
  PRISMA-P, SPIRIT, and CONSORT. Use this skill whenever the user wants to check, appraise,
  critically appraise, quality-assess, or QC a systematic review, meta-analysis,
  network meta-analysis, review manuscript, or study protocol against a checklist
  or risk-of-bias tool. Trigger on requests like "appraise this SR", "check this
  meta-analysis against PRISMA/ROBIS/AMSTAR", "is this review low risk of bias",
  "run AMSTAR-2 on this paper", "PRISMA completeness check", "critically appraise
  this for my HTA evidence table / umbrella review", "assess this protocol", or
  when the user hands over a review PDF/DOCX and asks how good or how complete it
  is. Also use for self-checking the user's own draft review before submission.
  Prefer this skill over answering from memory — the checklists must be applied
  item by item, not summarised loosely.
---

# Evidence Appraisal

Appraise a document against the appropriate reporting-completeness and
methodological-quality instrument, producing a rigorous, item-by-item Markdown
report with an overall verdict and a prioritised list of gaps.

The value of this skill is **discipline and honesty**: apply every checklist item
against the actual text (not a general impression), cite where each judgement
comes from, and be explicit about what you could not verify. A vague "looks good"
is worthless to someone deciding whether to include a review in an HTA dossier.

## Step 1 — Read the document and detect its type

Extract the full text first. If a PDF won't render (no poppler), extract the text
layer with `pdfplumber` or `pypdf` in Python rather than giving up:

```python
import pdfplumber
with pdfplumber.open(path) as pdf:
    text = "\n".join((p.extract_text() or "") for p in pdf.pages)
```

Then classify the document, because the tools are not interchangeable — applying
the wrong one (e.g. PRISMA to a trial protocol) is a real error, not a harmless
approximation:

| Detected document type | Tools to apply | Reference file(s) |
|---|---|---|
| Systematic review / **pairwise** meta-analysis manuscript | PRISMA 2020 + ROBIS + AMSTAR-2 | `prisma-2020.md`, `robis.md`, `amstar-2.md` |
| Systematic review with **network** meta-analysis (NMA) | PRISMA 2020 **+ PRISMA-NMA items** + ROBIS + AMSTAR-2 | `prisma-2020.md`, `prisma-nma.md`, `robis.md`, `amstar-2.md` |
| Systematic review **protocol** (PROSPERO-style) | PRISMA-P | `prisma-p.md` |
| Clinical **trial protocol** | SPIRIT 2013 | `spirit-2013.md` |
| Individual **randomised trial report** (single RCT) | CONSORT 2010 | `consort-2010.md` |

Detection cues: an NMA mentions "network meta-analysis", "indirect comparison",
"SUCRA", "netmeta", or a treatment network figure — route it through the NMA
branch, since plain PRISMA 2020 misses network-specific reporting. A protocol
describes what *will* be done (future tense, no results); a manuscript reports
what *was* done and found. An **individual trial report** presents the methods and
results of a *single* RCT (one study, not a synthesis) — route it to CONSORT 2010,
the reporting counterpart to SPIRIT (SPIRIT = protocol/planned, CONSORT = report/done).

If the type is genuinely ambiguous, state your best read and why, then proceed —
don't stall. If the user named a specific tool ("run AMSTAR-2 on this"), honour
that even if you'd also add others; note the additions.

**Reporting vs appraisal — keep them distinct.** PRISMA/PRISMA-P/PRISMA-NMA/SPIRIT/CONSORT
check whether the document *reports* things (author-side completeness). ROBIS and
AMSTAR-2 appraise whether the review was *conducted* well enough to trust
(appraiser-side). Good reporting does not imply low risk of bias, and a review can
be rigorous yet score poorly on a checklist item. Never present PRISMA as a
quality verdict.

## Step 2 — Apply each tool item by item

Work through every item using the relevant checklist in the **Appraisal checklists** section at the end of this file — every checklist is inlined here, so there are no external files to open. For each item
record: a rating, the location in the document (section/figure/page), a short
comment, and a **verbatim quote of the supporting text** (a few words is enough) —
or "no supporting text found" if the document is silent, never inferring a rating
from silence. That anchoring is what makes each verdict auditable. Ratings differ by tool — the reference files give the
exact scheme and, for AMSTAR-2 and ROBIS, the algorithm that turns item-level
judgements into an overall verdict. Follow those algorithms exactly; the whole
point of these tools is that the verdict is rule-based, not vibes.

**Handle missing material honestly.** Reviews routinely place the search strategy,
per-study risk of bias, forest plots, and the excluded-studies list in
Supplementary/Supporting Information. If you weren't given the supplement, do not
guess a rating — mark the item *"per SI — not verified"* and say so. This matters
most for AMSTAR-2 item 7 (excluded-studies list) and item 4 (full search), which
frequently decide the AMSTAR-2 rating. Surface these as the first things to check,
because they can move the verdict a whole band.

## Step 3 — Write the report

Use the **Report template** at the very end of this file as the fixed structure. Always include:

- an **at-a-glance verdict table** (one row per tool) up front, so the reader gets
  the answer in five seconds;
- the **AMSTAR-2 / ROBIS reconciliation** when they seem to disagree — explain
  that AMSTAR-2 caps on a single critical domain, so "Low confidence" alongside
  "Low risk of bias" is expected, not contradictory. Readers who don't know this
  will misread a strong review as weak;
- a **prioritised gaps** list ordered by leverage — the item that would move the
  verdict the most goes first, not the most numerous nitpicks;
- an explicit **scope caveat** naming anything you couldn't verify.

Write the report to a `.md` file next to the source document and present a
condensed version inline. Keep the tone evidence-anchored and neutral — this often
feeds an HTA dossier, so no marketing language and no overstating certainty.

## Auditability & provenance

An appraisal that feeds an HTA dossier or a submission has to be *defensible* — a
reviewer or payer must be able to trace every verdict to the source and see who
stands behind it. Build that in, don't bolt it on:

- **Anchor every judgement.** Each item rating cites the exact location and quotes
  the supporting text verbatim (short). A reader should be able to verify any single
  verdict in seconds without re-reading the whole paper. If no supporting text
  exists, say so — never infer a rating from silence.
- **Stamp provenance on every report.** The header records: the appraised document
  (full citation + DOI/PMID and the exact source file name), whether the
  supplement/appendix was included, the method version (this skill's `version:`),
  the tool versions with citations, and the date.
- **Require human sign-off.** This skill produces a *draft*. It is not authoritative
  until a named person has verified it. End every report with a sign-off block —
  "Verified by: ____ (name, role, date)" — left blank for that person to complete.
  Do not present an unverified appraisal as final.
- **Disclose AI involvement.** State plainly that the draft was AI-assisted and by
  what. This is an integrity requirement, not a courtesy — some journals and HTA
  bodies mandate it.
- **Keep an immutable record.** Commit each finalised report to version control
  (git) and add a row to `examples/appraisal-log.md`. Together these give a
  timestamped, tamper-evident trail of what was appraised, by which method, and who
  verified it.

The polish of the output must never substitute for the human check — that is the
line between "a nice report" and "a signed, traceable record".

## Common judgement calls

- **A single AMSTAR-2 critical flaw → "Low".** Don't soften this to "Moderate"
  because the review is otherwise excellent — that misrepresents the tool. Instead,
  state the review's strength narratively *and* report the honest AMSTAR-2 band,
  and note what would raise it.
- **Promotional / derivative summaries** (evidence cards, slide decks summarising a
  review) are not systematic reviews. Don't appraise them against these tools;
  note what they are and, if useful, whether they represent the source faithfully.
- **Currency is not bias.** An old search date is a limitation to flag, but ROBIS
  and AMSTAR-2 judge conduct, not recency — don't downgrade a bias/quality domain
  purely because the review is a few years old.

---

# Appraisal checklists (inlined)

The full checklists the routing table above points to. Apply the one(s) for the
detected document type, item by item, quoting the supporting text verbatim.


---

# PRISMA 2020 — reporting checklist for systematic reviews

Source: Page MJ, McKenzie JE, Bossuoyt PM, et al. The PRISMA 2020 statement.
BMJ 2021;372:n71. A **reporting** guideline — it checks whether a review is
described completely and transparently, *not* its methodological quality or risk
of bias (use AMSTAR-2 / ROBIS for that).

Rate each item: **✅ Yes** (fully reported) · **🟡 Partial** (reported but
incomplete or only referenced in supplement without detail) · **❌ No** (not
reported). Record the location (section/figure) and a one-line comment. There is
no summed score — report the count of ✅/🟡/❌ and describe overall completeness
(High / Moderate / Low). For a network meta-analysis, also apply `prisma-nma.md`.

## Title & abstract
- **1. Title** — Identify the report as a systematic review.
- **2. Abstract** — Structured abstract (see PRISMA-for-Abstracts): background,
  objectives, eligibility, sources, risk-of-bias/synthesis methods, results
  (number of studies/participants, effect estimates, certainty), limitations,
  interpretation, funding, registration.

## Introduction
- **3. Rationale** — Rationale for the review in the context of existing knowledge.
- **4. Objectives** — Explicit statement of objective(s) or question(s), ideally
  in PICO terms.

## Methods
- **5. Eligibility criteria** — Inclusion/exclusion criteria and how studies were
  grouped for syntheses.
- **6. Information sources** — All databases, registers, websites, other sources
  searched or consulted; date each was last searched.
- **7. Search strategy** — Full search strategy for at least one database,
  including any filters/limits (reproducible).
- **8. Selection process** — How many reviewers screened, independently or not,
  whether automation tools were used.
- **9. Data collection process** — Same detail for data extraction; contact with
  study authors.
- **10a. Data items — outcomes** — All outcomes sought; which results were
  collected (e.g. all time points), and how missing/unclear cases were handled.
- **10b. Data items — other variables** — All other variables sought (e.g.
  participant/intervention characteristics, funding).
- **11. Study risk of bias assessment** — Tool(s) used, number of assessors,
  independence, automation.
- **12. Effect measures** — Effect measure(s) used (e.g. risk ratio, mean
  difference) for each outcome.
- **13. Synthesis methods** — (a) how studies were grouped; (b) data preparation;
  (c) tabulation/visual methods; (d) synthesis/meta-analysis methods incl. model,
  heterogeneity, software; (e) heterogeneity exploration (subgroup/meta-regression);
  (f) sensitivity analyses.
- **14. Reporting bias assessment** — Methods to assess risk of bias due to
  missing results (publication bias).
- **15. Certainty assessment** — Methods to assess certainty/confidence in the
  body of evidence (e.g. GRADE).

## Results
- **16a. Study selection** — Numbers screened/included/excluded, ideally with a
  flow diagram.
- **16b. Excluded studies** — Studies that met many but not all criteria, excluded,
  **with reasons**.
- **17. Study characteristics** — Cite each included study and present its
  characteristics.
- **18. Risk of bias in studies** — Assessments for each included study.
- **19. Results of individual studies** — For each study, summary statistics per
  group and effect estimate with precision (e.g. forest plots).
- **20. Results of syntheses** — For each synthesis: (a) study characteristics/RoB;
  (b) summary estimates and precision; (c) heterogeneity; (d) subgroup/sensitivity.
- **21. Reporting biases** — Risk of bias from missing results, per synthesis.
- **22. Certainty of evidence** — Certainty (e.g. GRADE) per outcome.

## Discussion
- **23a. Interpretation** — General interpretation in context of other evidence.
- **23b. Limitations of evidence** — Limitations of the evidence included.
- **23c. Limitations of review processes** — Limitations of the review conduct.
- **23d. Implications** — Implications for practice, policy, and future research.

## Other information
- **24a. Registration** — Registration name and number, or statement of none.
- **24b. Protocol** — Where the protocol can be accessed, or statement of none.
- **24c. Amendments** — Amendments to registration/protocol, or statement of none.
- **25. Support** — Financial/non-financial support and role of funders.
- **26. Competing interests** — Declarations of competing interests.
- **27. Availability of data, code and other materials** — Which of: data
  extraction forms, extracted data, analytic code, other materials are publicly
  available and where.

**Common gaps to watch:** item 7 (full reproducible search — often only in
supplement), 16b (excluded studies **with reasons**), 24c (protocol amendments —
frequently omitted), 23c (review-*process* limitations, distinct from evidence
limitations), 27 (code availability).


---

# PRISMA-NMA — extension for network meta-analyses

Source: Hutton B, Salanti G, Caldwell DM, et al. The PRISMA extension statement
for reporting of systematic reviews incorporating network meta-analyses.
Ann Intern Med 2015;162(11):777-84.

Apply this **in addition to** `prisma-2020.md` when the review includes a network
meta-analysis (indirect / mixed treatment comparisons). It keeps the base PRISMA
items and adds/modifies the following NMA-specific reporting requirements. Rate
each ✅ / 🟡 / ❌ with location and comment, as for PRISMA 2020.

## NMA-specific items (additions/modifications)

- **S1. Title** — Identify the report as incorporating a network meta-analysis
  (not just a systematic review).
- **S2. Geometry of the network** — Describe the network structure: which
  treatments are nodes, which comparisons have direct evidence, number of trials
  and participants per node/comparison. A network diagram should be presented and
  interpreted (sparse links, dominant nodes, disconnected treatments).
- **S3. Summary of network geometry** — Comment on any imbalance/features that may
  bias the analysis (e.g. one comparison dominating, treatments compared only
  indirectly).
- **S4. Description of methods — transitivity/similarity** — Describe the
  assumption of transitivity (that studies are similar enough to combine across
  comparisons) and how the distribution of effect modifiers was assessed across
  comparisons.
- **S5. Description of methods — inconsistency** — Describe how consistency between
  direct and indirect evidence was evaluated (local methods e.g. node-splitting /
  side-splitting; global methods e.g. design-by-treatment interaction model).
- **S6. Results — ranking** — Report treatment rankings and the method used (e.g.
  SUCRA, P-scores, rankograms), with appropriate caution about interpreting ranks
  when certainty is low or CIs overlap.
- **S7. Results — inconsistency** — Present the results of consistency/transitivity
  assessment for each network.
- **S8. Certainty in NMA estimates** — Report confidence/certainty of NMA estimates
  (e.g. CINeMA, or GRADE for NMA), reflecting within-study bias, imprecision,
  heterogeneity, incoherence, and indirectness.

## Judgement notes
- A review can meet base PRISMA 2020 fully yet miss NMA items — network geometry
  reporting (S2/S3) and transitivity justification (S4) are the most commonly
  underreported. Do not let strong base-PRISMA completeness mask an NMA gap.
- Ranking metrics (S6) are easily over-interpreted; note whether the authors
  themselves caution against reading rankings as definitive when certainty is low.
- For ROBIS/AMSTAR-2 on an NMA, the synthesis-appropriateness judgements (ROBIS
  Domain 4; AMSTAR-2 item 11) should reflect whether transitivity and consistency
  were properly handled, not just whether a pooled estimate was produced.


---

# ROBIS — Risk Of Bias In Systematic reviews

Source: Whiting P, Savović J, Higgins JPT, et al. ROBIS: a new tool to assess risk
of bias in systematic reviews. J Clin Epidemiol 2016;69:225-34.

ROBIS assesses the **risk of bias in a completed systematic review** — could the
review's conclusions be distorted by how it was conducted? It is an appraisal
tool (like AMSTAR-2), not a reporting checklist. Work through three phases.

## Phase 1 (optional) — Assess relevance
Only used when appraising reviews against a specific research question (e.g. for an
overview/umbrella review). Judge whether the review's PICO matches the question at
hand. Skip if simply appraising a review on its own terms.

## Phase 2 — Identify concerns with the review process
Four domains. Each has **signalling questions** answered *Yes / Probably yes /
Probably no / No / No information*, where **"Yes" is the low-concern answer**. Then
judge the **level of concern** for the domain as **Low / High / Unclear**.

### Domain 1 — Study eligibility criteria
Signalling questions:
1.1 Did the review adhere to pre-defined objectives and eligibility criteria?
1.2 Were eligibility criteria appropriate for the review question?
1.3 Were eligibility criteria unambiguous?
1.4 Were any restrictions (e.g. language, date, publication status) appropriate
    and justified?
1.5 Were any efforts made to minimise error in application of eligibility criteria?

### Domain 2 — Identification and selection of studies
2.1 Did the search include an appropriate range of databases/electronic sources?
2.2 Were methods additional to database searching used (e.g. reference lists,
    trial registries, contacting authors, hand-searching)?
2.3 Were search terms and structure adequate to retrieve as many eligible studies
    as possible?
2.4 Were restrictions based on date, publication format, or language appropriate?
2.5 Were efforts made to minimise error in selection (e.g. duplicate screening)?

### Domain 3 — Data collection and study appraisal
3.1 Were efforts made to minimise error in data collection (e.g. duplicate
    extraction)?
3.2 Were sufficient study characteristics collected/reported for the review's aims?
3.3 Were all relevant study results collected for use in the synthesis?
3.4 Was risk of bias in included studies formally assessed using appropriate
    criteria?
3.5 Were efforts made to minimise error in risk-of-bias assessment (e.g.
    duplicate assessment)?

### Domain 4 — Synthesis and findings
4.1 Did the synthesis include all studies it should?
4.2 Were all pre-defined analyses reported, or departures explained?
4.3 Was the synthesis appropriate given the nature and similarity of studies
    (e.g. was combining reasonable; for NMA, were transitivity/consistency handled)?
4.4 Was between-study variation (heterogeneity) minimal or addressed?
4.5 Were biases in included studies (risk of bias) accounted for in the synthesis?
4.6 Were biases arising from the review process (e.g. publication bias) minimal or
    addressed?

## Phase 3 — Judge overall risk of bias in the review
Consider concerns from Phase 2 plus three interpretive questions:
- A. Did the interpretation of findings address all concerns identified in
     Domains 1–4?
- B. Was the relevance of identified studies to the review's question appropriately
     considered?
- C. Did the reviewers avoid emphasising results on the basis of statistical
     significance?

**Overall verdict: Low / High / Unclear risk of bias.** A review with all domains
Low concern and no over-interpretation is Low risk of bias. Any High-concern domain
that is not offset by cautious interpretation typically yields High risk of bias;
insufficient information yields Unclear.

## Judgement notes
- ROBIS is about *bias*, not completeness — a poorly *reported* but well-*conducted*
  review can still be Low risk of bias (though you may have less information to
  judge). Conversely, transparent reporting of serious flaws still means High risk.
- Domain 4 is where NMA-specific concerns land: unaddressed inconsistency, high
  heterogeneity glossed over, or selective outcome reporting.
- Weigh whether authors *over-interpreted* (Phase 3C) — pushing a "winner" despite
  low certainty is a bias signal even when the analysis is technically sound.


---

# AMSTAR-2 — methodological quality of systematic reviews

Source: Shea BJ, Reeves BC, Wells G, et al. AMSTAR 2: a critical appraisal tool for
systematic reviews that include randomised or non-randomised studies of healthcare
interventions, or both. BMJ 2017;358:j4008.

AMSTAR-2 appraises **methodological quality / confidence** in a systematic review.
It produces an overall confidence rating (not a summed score) driven by which
domains are met, with extra weight on seven **critical** domains.

Rate each item **Yes / Partial Yes / No** (some items have specific Partial-Yes
criteria below). Record location and comment.

## The 16 items (⭐ = critical domain)

1. Did the research questions and inclusion criteria include the components of
   **PICO**? — Yes if population, intervention, comparator, outcome all specified.

2. ⭐ Did the report contain an explicit statement that the review methods were
   established **prior to conduct**, and were deviations justified? — *Partial Yes*:
   published protocol / registration exists. *Yes*: also states PICO, analysis plan,
   and justifies any deviations.

3. Did the authors explain their selection of **study designs** for inclusion?

4. ⭐ Did the authors use a **comprehensive literature search** strategy? —
   *Partial Yes*: searched ≥2 databases, provided keywords/search strategy,
   justified publication restrictions. *Yes*: also searched trial/study registries,
   included/consulted content experts, searched reference lists of included studies,
   searched grey literature, and conducted the search within 24 months of completion.

5. Did the authors perform **study selection in duplicate**?

6. Did the authors perform **data extraction in duplicate**?

7. ⭐ Did the authors provide a **list of excluded studies and justify the
   exclusions**? — *Partial Yes*: provided a list of potentially relevant studies
   excluded. *Yes*: also justified the exclusion of each. (Studies excluded at
   full-text screening — a PRISMA flow count alone is **not** sufficient.)

8. Did the authors describe the **included studies in adequate detail** (PICO,
   design, setting, follow-up, etc.)?

9. ⭐ Did the authors use a **satisfactory technique for assessing risk of bias**
   in included studies? — For RCTs: allocation concealment, blinding, etc. (e.g.
   RoB / RoB 2). For NRSI: confounding, selection (e.g. ROBINS-I). *Partial Yes*:
   assessed some sources of RoB. *Yes*: assessed all relevant domains.

10. Did the authors report the **sources of funding for the included studies**?

11. ⭐ If meta-analysis was performed, did the authors use **appropriate
    statistical methods** to combine results? — Justified combination, weighted
    appropriately, investigated heterogeneity, used a suitable model; for NMA,
    handled transitivity/consistency appropriately.

12. If meta-analysis was performed, did the authors **assess the potential impact
    of risk of bias** in individual studies on the pooled result?

13. ⭐ Did the authors **account for risk of bias when interpreting/discussing**
    the results?

14. Did the authors provide a satisfactory **explanation for, and discussion of,
    any heterogeneity** observed?

15. ⭐ If quantitative synthesis was performed, did the authors adequately
    **investigate publication bias** (small-study bias) and discuss its likely
    impact? — e.g. funnel plots + a statistical test when enough studies.

16. Did the authors report any **potential sources of conflict of interest**,
    including funding for conducting the review?

## Overall confidence rating (apply exactly)

Weaknesses are classed as **critical** (in the ⭐ domains: 2, 4, 7, 9, 11, 13, 15)
or **non-critical** (all others).

| Rating | Definition |
|---|---|
| **High** | No or **one non-critical** weakness. |
| **Moderate** | **More than one non-critical** weakness (and no critical flaws). |
| **Low** | **One critical flaw**, with or without non-critical weaknesses. |
| **Critically Low** | **More than one critical flaw**, with or without non-critical weaknesses. |

A "Partial Yes" is a partial credit, not a pass — decide per item whether the
residual shortfall constitutes a weakness for rating purposes, and be explicit.

## Judgement notes
- **The rating is gated by critical domains.** A single unmet critical item forces
  "Low" even if all 15 others are met. Item 7 (excluded-studies list) and item 4
  (comprehensive search) are the most frequent silent downgraders. When you assign
  "Low", say plainly which critical item caused it and what would raise the rating.
- Distinguish the *rating* (rule-based) from the *narrative quality*. Report both:
  a review can be excellent yet rate "Low" on a reporting technicality. Do not
  inflate the rating to match your impression, and do not let the low rating imply
  the review is untrustworthy — that reconciliation belongs in the report.
- Item 7 vs a PRISMA flow diagram: counts of excluded records do **not** satisfy
  item 7. Look for an actual list (usually in supplement) with reasons.


---

# PRISMA-P — reporting checklist for systematic review PROTOCOLS

Source: Moher D, Shamseer L, Clarke M, et al. Preferred Reporting Items for
Systematic review and Meta-Analysis Protocols (PRISMA-P) 2015. Syst Rev 2015;4:1.

Apply to a **systematic review protocol** (e.g. a PROSPERO record or a protocol
manuscript) — it checks whether the *plan* is described completely. A protocol
describes intended methods (future tense, no results). Rate each ✅ / 🟡 / ❌ with
location and comment.

## Administrative information
- **1a. Title — identification** — Identify the report as a protocol for a
  systematic review.
- **1b. Title — update** — If an update, indicate so.
- **2a. Registration** — Registration name and number (e.g. PROSPERO), or intent.
- **3a. Contact** — Named contact / corresponding author.
- **3b. Contributions** — Contributions of protocol authors.
- **4. Amendments** — If an amendment, identify changes; otherwise plan for
  documenting amendments.
- **5a. Sources of support** — Financial or other support.
- **5b. Sponsor** — Name of sponsor/funder.
- **5c. Role of sponsor/funder** — Role in developing the protocol.

## Introduction
- **6. Rationale** — Rationale in the context of what is already known.
- **7. Objectives** — Explicit question(s) with PICO components.

## Methods
- **8. Eligibility criteria** — Study characteristics (PICO, design, setting, time
  frame) and report characteristics (years, language, publication status) with
  rationale.
- **9. Information sources** — Intended sources (databases, registers, contact with
  authors, grey literature) with planned coverage dates.
- **10. Search strategy** — Draft search strategy for at least one database,
  including planned limits, such that it could be repeated.
- **11a. Study records — data management** — Mechanisms for managing records/data.
- **11b. Study records — selection process** — Planned screening process (levels,
  number of reviewers, independence).
- **11c. Study records — data collection process** — Planned extraction process,
  including duplicate and author-contact plans.
- **12. Data items** — Variables to be sought and any pre-planned assumptions/
  simplifications.
- **13. Outcomes and prioritisation** — Main and additional outcomes, with rationale.
- **14. Risk of bias in individual studies** — Planned tool and process.
- **15a–15d. Data synthesis** — Criteria for quantitative synthesis; planned summary
  measures; methods of handling data and combining results; planned additional
  analyses (subgroup, sensitivity, meta-regression); if synthesis not appropriate,
  the planned approach.
- **16. Meta-bias(es)** — Planned assessment of publication/selective-reporting bias.
- **17. Confidence in cumulative evidence** — Planned assessment of strength of the
  body of evidence (e.g. GRADE).

## Judgement notes
- The commonest protocol gaps are item 10 (a genuinely reproducible draft search,
  not just named databases), item 13 (outcome prioritisation with rationale), and
  item 17 (planned GRADE). ROBIS/AMSTAR-2 do **not** apply to a protocol — there is
  nothing conducted yet to appraise for bias/quality.


---

# SPIRIT 2013 — reporting checklist for CLINICAL TRIAL protocols

Source: Chan A-W, Tetzlaff JM, Altman DG, et al. SPIRIT 2013 Statement: defining
standard protocol items for clinical trials. Ann Intern Med 2013;158(3):200-7.

Apply to a **clinical trial protocol** (an interventional study plan) — NOT to a
systematic review or its protocol (use PRISMA-P for those). SPIRIT defines the
minimum content a trial protocol should report. Rate each ✅ / 🟡 / ❌ with location
and comment. (33 items across the checklist; grouped below.)

## Administrative information
- **1. Title** — Descriptive title: design, population, interventions, and acronym.
- **2a. Trial registration** — Registry name and identifier.
- **2b. Registration data set** — All items from the WHO Trial Registration Data Set.
- **3. Protocol version** — Date and version identifier.
- **4. Funding** — Sources of financial and material support.
- **5a–5d. Roles and responsibilities** — Contributors, sponsor, sponsor role,
  committees (steering, data monitoring, etc.).

## Introduction
- **6a. Background and rationale** — Including why the trial is needed and a summary
  of relevant studies (benefits/harms).
- **6b. Choice of comparators** — Rationale for the comparator(s).
- **7. Objectives** — Specific objectives or hypotheses.
- **8. Trial design** — Type (parallel, crossover, factorial), allocation ratio,
  framework (superiority, non-inferiority, equivalence).

## Methods — participants, interventions, outcomes
- **9. Study setting** — Sites and settings; where the list of sites can be obtained.
- **10. Eligibility criteria** — Inclusion/exclusion for participants (and, if
  applicable, for centres/individuals performing interventions).
- **11a–11d. Interventions** — Detailed description; discontinuation/modification
  criteria; adherence strategies; concomitant care permitted/prohibited.
- **12. Outcomes** — Primary/secondary/other outcomes, with metric, method of
  aggregation, and time point; explanation of clinical relevance.
- **13. Participant timeline** — Schedule of enrolment, interventions, assessments
  (ideally a diagram).
- **14. Sample size** — Number needed and how it was determined (assumptions).
- **15. Recruitment** — Strategies to reach target sample size.

## Methods — assignment, blinding
- **16a. Sequence generation** — Method to generate the allocation sequence.
- **16b. Allocation concealment mechanism** — How the sequence is concealed until
  assignment.
- **16c. Implementation** — Who generates, enrols, assigns.
- **17a. Blinding (masking)** — Who is blinded and how.
- **17b. Emergency unblinding** — Circumstances/procedure for revealing allocation.

## Methods — data collection, management, analysis
- **18a. Data collection methods** — Plans for assessment/collection, promoting
  data quality (e.g. duplicate measurements, training).
- **18b. Retention** — Plans to promote participant retention and complete follow-up.
- **19. Data management** — Data entry, coding, security, storage.
- **20a–20c. Statistical methods** — For outcomes; for additional analyses
  (subgroup, adjusted); handling of protocol non-adherence and missing data.

## Methods — monitoring
- **21a. Data monitoring committee** — Composition, role, independence (or why none).
- **21b. Interim analyses** — And stopping guidelines.
- **22. Harms** — Plans for collecting, assessing, reporting adverse events.
- **23. Auditing** — Frequency and procedures for auditing trial conduct.

## Ethics and dissemination
- **24. Research ethics approval** — Plans for ethics committee approval.
- **25. Protocol amendments** — Plans to communicate important amendments.
- **26a. Consent** — Who will obtain informed consent and how.
- **26b. Ancillary studies** — Consent for use of data/biological specimens.
- **27. Confidentiality** — How personal information is protected.
- **28. Declaration of interests** — For sponsors and investigators.
- **29. Access to data** — Who has access to the final dataset; contractual limits.
- **30. Ancillary and post-trial care** — Provisions and compensation for harm.
- **31a–31c. Dissemination policy** — Plans to communicate results; authorship
  guidelines; public access to protocol/dataset/code.

## Appendices
- **32. Informed consent materials** — Model consent form(s).
- **33. Biological specimens** — Plans for collection/storage of specimens.

## Judgement notes
- Frequent trial-protocol gaps: 16b (allocation concealment mechanism, distinct from
  sequence generation), 20c (handling of missing data / non-adherence), 21a (DMC),
  22 (harms reporting plan), 31c (public access to protocol/data/code).
- SPIRIT is the protocol counterpart to CONSORT (which governs the trial *report*).
  If the user hands over a completed trial *manuscript* rather than a protocol,
  CONSORT is the right tool — flag this rather than forcing SPIRIT.


---

# CONSORT 2010 — reporting checklist for randomised controlled trials

Source: Schulz KF, Altman DG, Moher D; CONSORT Group. CONSORT 2010 Statement:
updated guidelines for reporting parallel group randomised trials. BMJ 2010;340:c332.

Apply to an **individual randomised controlled trial (RCT) report** — a single trial
manuscript, not a systematic review (use PRISMA) and not a trial protocol (use
SPIRIT). CONSORT is a **reporting** guideline: it checks whether the completed trial
is described completely and transparently, not its risk of bias (for that, appraise
the RCT with Cochrane RoB 2 — see the notes below).

Rate each item ✅ Yes · 🟡 Partial · ❌ Not reported, with location and comment. No
summed score — report the counts and overall completeness (High / Moderate / Low).

## Title and abstract
- **1a. Title** — Identification as a randomised trial in the title.
- **1b. Abstract** — Structured summary of trial design, methods, results, and conclusions (see CONSORT for Abstracts).

## Introduction
- **2a. Background** — Scientific background and explanation of rationale.
- **2b. Objectives** — Specific objectives or hypotheses.

## Methods
- **3a. Trial design** — Description (e.g. parallel, factorial) including allocation ratio.
- **3b. Changes to design** — Important changes to methods after commencement (e.g. eligibility), with reasons.
- **4a. Participants — eligibility** — Eligibility criteria for participants.
- **4b. Settings** — Settings and locations where the data were collected.
- **5. Interventions** — Interventions for each group in enough detail to replicate, including how and when they were administered.
- **6a. Outcomes** — Completely defined pre-specified primary and secondary outcomes, including how and when assessed.
- **6b. Changes to outcomes** — Any changes after the trial began, with reasons.
- **7a. Sample size** — How it was determined.
- **7b. Interim analyses / stopping** — When applicable, interim analyses and stopping guidelines.
- **8a. Sequence generation** — Method used to generate the random allocation sequence.
- **8b. Randomisation type** — Type of randomisation; details of any restriction (e.g. blocking, block size).
- **9. Allocation concealment** — Mechanism used to implement the sequence, and steps taken to conceal it until interventions were assigned.
- **10. Implementation** — Who generated the sequence, who enrolled participants, and who assigned them to interventions.
- **11a. Blinding** — If done, who was blinded after assignment (participants, care providers, outcome assessors) and how.
- **11b. Similarity of interventions** — If relevant, description of the similarity of interventions.
- **12a. Statistical methods** — Methods used to compare groups for primary and secondary outcomes.
- **12b. Additional analyses** — Methods for subgroup and adjusted analyses.

## Results
- **13a. Participant flow** — For each group, numbers randomised, receiving intended treatment, and analysed for the primary outcome (a flow diagram is strongly recommended).
- **13b. Losses / exclusions** — For each group, losses and exclusions after randomisation, with reasons.
- **14a. Recruitment** — Dates defining the periods of recruitment and follow-up.
- **14b. Trial end** — Why the trial ended or was stopped.
- **15. Baseline data** — A table of baseline demographic and clinical characteristics for each group.
- **16. Numbers analysed** — For each group, number included in each analysis and whether by original assigned groups (intention-to-treat).
- **17a. Outcomes and estimation** — For each outcome, results per group and the estimated effect size with its precision (e.g. 95% CI).
- **17b. Absolute and relative effects** — For binary outcomes, presentation of both is recommended.
- **18. Ancillary analyses** — Other analyses performed, distinguishing pre-specified from exploratory.
- **19. Harms** — All important harms or unintended effects in each group (see CONSORT for Harms).

## Discussion
- **20. Limitations** — Sources of potential bias, imprecision, and, if relevant, multiplicity of analyses.
- **21. Generalisability** — External validity / applicability of the findings.
- **22. Interpretation** — Consistent with results, balancing benefits and harms, and considering other relevant evidence.

## Other information
- **23. Registration** — Registration number and name of trial registry.
- **24. Protocol** — Where the full trial protocol can be accessed, if available.
- **25. Funding** — Sources of funding and other support (e.g. drug supply); role of funders.

## Judgement notes
- **CONSORT is reporting, not risk of bias.** To judge how much to trust a single
  RCT's results, use the Cochrane **RoB 2** tool (randomisation, deviations from
  intended intervention, missing outcome data, outcome measurement, selective
  reporting). RoB 2 is the companion appraisal tool for individual trials — it is
  **not** bundled in this skill (a candidate future addition); flag when it is needed.
- **CONSORT vs SPIRIT vs PRISMA.** SPIRIT governs the trial *protocol* (planned);
  CONSORT governs the completed *trial report* (done); PRISMA governs *reviews* of
  many trials. Route by what the document actually is.
- **Common gaps:** 9 (allocation-concealment mechanism, distinct from sequence
  generation), 11 (who was blinded and how), 13b (post-randomisation losses with
  reasons), 16 (intention-to-treat denominators), 17b (absolute effects), 24
  (protocol access).
- **Extensions exist** (cluster, non-inferiority/equivalence, pragmatic, pilot/
  feasibility, harms, PROs, abstracts). This file covers base CONSORT 2010 for
  parallel-group trials — note if an extension applies.


---

# Report template

# Evidence Appraisal Report — [Short study label]

**Appraised document:** [Full citation]. DOI/PMID/URL: [...].
**Source file:** [exact filename appraised]  ·  **Supplement/appendix included:** [Yes — which / No]
**Registration:** [PROSPERO / ClinicalTrials.gov ID, or "none stated"]
**Appraisal date:** [YYYY-MM-DD]  ·  **Method version:** evidence-appraisal v[x.y]
**Tools applied:** [e.g. PRISMA 2020 (+ PRISMA-NMA) · ROBIS · AMSTAR-2] (with versions / citations)
**Prepared by:** AI-assisted draft — [tool/model]  ·  **Verified by:** ____________ (name, role, date)

> **Routing note.** Document type detected = [type]. [Why these tools; note if NMA
> branch or SPIRIT/PRISMA-P applies.]
>
> **Scope caveat.** [State exactly what was and wasn't available — e.g. main text
> only, Supporting Information not provided. Name the items that depend on missing
> material and mark them "not verified".]

---

## 1. Overall verdict at a glance

| Tool | Result | One-line basis |
|---|---|---|
| [Tool 1] | [verdict] | [basis] |
| [Tool 2] | [verdict] | [basis] |
| [Tool 3] | [verdict] | [basis] |

[If ROBIS and AMSTAR-2 appear to disagree, add a one-paragraph reconciliation here:
AMSTAR-2 caps on a single critical domain, so a strong review can read "Low
confidence" while ROBIS reads "Low risk of bias" — this is expected, not a
contradiction. State plainly whether the review is substantively strong or weak.]

---

## 2. [PRISMA 2020 / PRISMA-P / SPIRIT] — item-by-item

Legend: ✅ Yes · 🟡 Partial · ❌ Not reported

*Each comment quotes the supporting text verbatim (short) or states "no supporting text found" — so any rating can be checked against the source.*

| # | Item | Rating | Location / comment |
|---|---|---|---|
| ... | ... | ... | ... |

[If NMA: add the PRISMA-NMA-specific items (network geometry, ranking,
transitivity, consistency, NMA certainty) here or in their own short subsection.]

**Summary:** [count of ✅/🟡/❌]; overall completeness = [High/Moderate/Low]. Clear
reporting gaps: [list].

---

## 3. ROBIS — Risk of Bias in the review
*(Include only for review manuscripts.)*

| Domain | Concern | Basis |
|---|---|---|
| 1. Study eligibility criteria | [Low/High/Unclear] | [...] |
| 2. Identification & selection | [...] | [...] |
| 3. Data collection & appraisal | [...] | [...] |
| 4. Synthesis & findings | [...] | [...] |

**Phase 3 — overall risk of bias: [LOW / HIGH / UNCLEAR].** [Reasoning, including
whether interpretation was appropriately cautious / avoided over-emphasis.]

---

## 4. AMSTAR-2 — methodological quality
*(Include only for review manuscripts.)*

Critical domains ⭐ = items 2, 4, 7, 9, 11, 13, 15.

| # | Item | Rating | Comment |
|---|---|---|---|
| 1 | PICO | [Yes/Partial/No] | [...] |
| ... | ... | ... | ... |

**Overall confidence: [High / Moderate / Low / Critically Low].** [State the
rating logic explicitly: which critical flaw(s), if any, drove it, and what would
change the band.]

---

## 5. Prioritised gaps (highest leverage first)

1. **[Gap]** — [why it matters; which item(s); what to do]. *[Highest leverage if
   it can move the verdict a whole band.]*
2. **[Gap]** — [...]
3. **[Gap]** — [...]

## 6. Notes
[Anything else: derivative/promotional summaries seen and whether faithful;
currency of the search; CONSORT vs SPIRIT flag; etc.]

## 7. Provenance & sign-off

- **Method:** evidence-appraisal v[x.y]; tools as listed above, each with its source citation.
- **Inputs seen:** [source file(s); whether the supplement/appendix was included]. Items that could not be verified from what was provided are marked "not verified" above.
- **AI disclosure:** produced as an AI-assisted draft ([tool/model]). **Not authoritative until verified below.**

**Verification — required before use in a dossier or submission:**

> Verified by: ____________________   Role: ______________   Date: __________
>
> Verifier's note (items checked, changed, or disputed): ____________________

---

*Appraisal caveat: [restate what could not be verified and what to provide to
finalise].*
