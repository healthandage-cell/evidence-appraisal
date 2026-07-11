# Changelog — evidence-appraisal skill

All notable changes to the **method** (SKILL.md + reference checklists) are recorded here.
This tracks the *appraisal method*, not the papers appraised (those live in `..\examples\appraisal-log.md`).

Versioning: bump the `version:` field in `SKILL.md` and add an entry below, then re-package
(`..\repackage.py` or `..\repackage.cmd`) and re-upload in Claude → Settings → Customize → Skills.

## [1.2] — 2026-07-11
### Added — CONSORT 2010
- New `references/consort-2010.md` (25-item checklist) for appraising **individual randomised trial reports** — the reporting counterpart to SPIRIT (protocols).
- SKILL.md: routing row (RCT report → CONSORT 2010), detection cue, and CONSORT added to the tool list / description.
- Note: individual-RCT risk of bias (Cochrane RoB 2) flagged as the companion tool, not yet bundled.

## [1.1] — 2026-07-11
### Added — auditability & provenance
- SKILL.md: new "Auditability & provenance" section; item ratings must quote the supporting text verbatim (or state none found).
- report-template.md: provenance header (source file, supplement Y/N, method version), AI-use disclosure, and a required human **sign-off block**.
- appraisal-log.md: added Supplement, Verified-by and Verified-date columns; DOI in the document column.
- Principle: the skill produces a *draft*; it is not authoritative until a named human verifies it.

## [1.0] — 2026-07-10
Initial release.
- Routing logic: SR/MA manuscript → PRISMA 2020 + ROBIS + AMSTAR-2; network meta-analysis
  → adds PRISMA-NMA; SR protocol → PRISMA-P; clinical trial protocol → SPIRIT 2013.
- Reference checklists: PRISMA 2020 (27 items), PRISMA-NMA, ROBIS (3 phases / 4 domains),
  AMSTAR-2 (16 items, 7 critical, rating algorithm), PRISMA-P (17 items), SPIRIT 2013.
- Report template with verdict table, ROBIS↔AMSTAR-2 reconciliation, prioritised gaps,
  and an explicit "not verified" convention for supplement-dependent items.
- Validated on Di Molfetta et al. 2024 (HCL network meta-analysis) incl. supplement review.

<!-- Template for future entries:
## [1.1] — YYYY-MM-DD
### Added / Changed / Fixed
- ...
-->
