# Evidence-Appraisal — Checklists (knowledge base)

Reference checklists for the evidence-appraisal Copilot agent. Upload this file (or a PDF/DOCX
conversion of it) as the agent's knowledge so it applies the exact rules rather than its memory.



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
