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
