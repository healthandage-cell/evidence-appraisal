# Changelog — evidence-appraisal skill

All notable changes to the **method** (SKILL.md + reference checklists) are recorded here.
This tracks the *appraisal method*, not the papers appraised (those live in `..\examples\appraisal-log.md`).

Versioning: bump the `version:` field in `SKILL.md` and add an entry below, then re-package
(`..\repackage.py` or `..\repackage.cmd`) and re-upload in Claude → Settings → Customize → Skills.

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
