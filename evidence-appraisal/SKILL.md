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

Open the relevant reference file(s) and work through every item. For each item
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

Use `assets/report-template.md` as the fixed structure. Always include:

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
