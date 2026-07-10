# Evidence-Appraisal — skill, examples & explainer

A self-contained, **global** capability: an AI skill that appraises clinical protocols and
systematic-review manuscripts against the standard reporting and quality tools
(PRISMA 2020, PRISMA-NMA, ROBIS, AMSTAR-2, PRISMA-P, SPIRIT), plus the worked example it
was tested on and a deck explaining it. Not tied to any single project.

> **Owner:** Yvonne · **Created:** 2026-07-10 · **Current method version:** 1.0

---

## Getting this repo (for colleagues)

This repository is the shared, canonical source — grab it here instead of waiting for the tool to be
installed in every environment:

- **Download:** on GitHub, click **Code → Download ZIP**, or clone with `git clone <repo-url>`.
- Then pick the artifact for whatever you use (details in the table below and in *"Sharing it with a colleague on Copilot"*):
  - **Microsoft 365 Copilot** → the `copilot-m365\` folder (agent instructions + `knowledge-checklists.docx`)
  - **Claude** → `evidence-appraisal.skill`
  - **GitHub Copilot CLI** → `evidence-appraisal.zip`

> *Shared openly for the research community under the [MIT License](LICENSE) — reuse and adapt it freely. The explainer deck is a general introduction, not internal material. Please cite the original checklist publications (PRISMA, ROBIS, AMSTAR-2, etc.) when using them.*

## What's in this folder

| Path | What it is | You edit it? |
|---|---|---|
| **`evidence-appraisal\`** | The skill itself — the *method*. This is the editable master (source of truth). | ✅ Yes — when the method changes |
| `evidence-appraisal\SKILL.md` | The skill's brain: when it triggers, the workflow, the routing logic, judgement calls. Carries the `version:`. | ✅ |
| `evidence-appraisal\references\` | The actual checklists the skill applies: `prisma-2020.md`, `prisma-nma.md`, `robis.md`, `amstar-2.md`, `prisma-p.md`, `spirit-2013.md`. | ✅ |
| `evidence-appraisal\assets\report-template.md` | The fixed output structure every appraisal report follows. | ✅ |
| `evidence-appraisal\CHANGELOG.md` | History of changes to the **method** (version by version). | ✅ (add a line per version) |
| **`examples\`** | Outputs — papers actually appraised with the skill. Grows over time. | ✅ Add new appraisals here |
| `examples\appraisal-log.md` | Running audit trail: one row per document appraised, with the method + tool versions used. | ✅ Add a row per appraisal |
| `examples\Di-Molfetta-2024-NMA\` | The worked example (Di Molfetta 2024 HCL network meta-analysis) in `.docx` + `.md`. | Reference only |
| **`Evidence_Appraisal_Skill_explainer.pptx`** | 12-slide VP explainer: what a skill is, how it works, how it was tested, how teams use it. | ✅ (regenerate if needed) |
| `repackage.py` | Rebuilds the installable package from `evidence-appraisal\`. Run after editing the skill. | Run, don't edit |
| `repackage.cmd` | Double-click shortcut that runs `repackage.py`. | Run, don't edit |
| `evidence-appraisal.skill` / `.zip` | The **installable package** (identical contents). Upload this to install/update the skill. | Auto-generated |
| **`copilot-m365\`** | Transfer pack for **Microsoft 365 Copilot**: agent instructions + combined knowledge file + build guide. | Reference / share |

---

## The two things you'll do here

### 1. Appraise a new paper  *(the everyday case)*
You don't touch the skill for this — you just use it and record the result.
1. In Claude, ask it to appraise the document (e.g. *"appraise this systematic review against PRISMA and AMSTAR-2"*). The installed **evidence-appraisal** skill runs.
2. Save the report into a new subfolder under `examples\` (e.g. `examples\<first-author-year>\`).
3. Add a row to **`examples\appraisal-log.md`** — note the date, document, method version, tool versions, and the three verdicts. *This is your audit trail.*

*No repackaging needed — you produced an output, not a change to the method.*

### 2. Improve the skill itself  *(occasional)*
When you change *how* it appraises — add a tool (e.g. CONSORT), refine a checklist, update to a newer PRISMA:
1. Edit the files in `evidence-appraisal\`.
2. Bump `version:` in `SKILL.md` and add an entry to `CHANGELOG.md`.
3. Double-click **`repackage.cmd`** (or run `python repackage.py`).
4. Re-publish: **Claude → Settings → Customize → Skills → Add** → select `evidence-appraisal.skill`. This bumps "Last updated" on the installed skill.

> ⚠️ **Editing the folder does NOT change the installed skill.** The version in Claude is a snapshot taken at upload. You must re-package (step 3) and re-add (step 4) to publish an update. Think of the folder as source code and the installed skill as a deployed build.

---

## Key concept the skill encodes

Two different questions, kept deliberately separate:

- **Reporting completeness** (PRISMA / PRISMA-P / PRISMA-NMA / SPIRIT) — *is it fully written up?*
- **Methodological quality / risk of bias** (ROBIS, AMSTAR-2) — *can it be trusted?*

A review can be beautifully reported yet still high risk of bias. A frequent surprise:
AMSTAR-2 caps its rating on a single **critical** item, so a strong review can score "Low"
just for omitting a list of excluded studies — see the Di Molfetta example.

---

## Sharing it with a colleague on Copilot

**The skill's content is portable** — the workflow and the checklists are plain text, so they move
to almost any AI assistant. *How* depends on which Copilot she uses; these are different products.

### Microsoft 365 Copilot (enterprise) — her environment → see `copilot-m365\`
Microsoft 365 Copilot doesn't use the `SKILL.md` format. The equivalent is a **Copilot agent**:
paste the workflow as its **instructions** and upload the checklists as **knowledge**. A ready-to-use
pack is in **`copilot-m365\`**:
- `agent-instructions.md` — paste into the agent's **Instructions** field.
- `knowledge-checklists.docx` — upload as the agent's **knowledge** (Word, upload-ready; `.md` source is included too).
- `HOW-TO-build-in-m365.md` — step-by-step via the in-Copilot "Create agent" builder or Copilot Studio, with a governance note.

### GitHub Copilot (developer tool) — only if she means the coding one
A different product from Microsoft 365 Copilot:
- **CLI:** supports the Agent Skills format — drop the `evidence-appraisal\` folder in its skills directory.
- **VS Code Chat:** convert to `.github\prompts\evidence-appraisal.prompt.md`, invoked with `/evidence-appraisal`.

> **Whichever route, the `references\` checklists are the real asset.** Make sure they travel with the skill (as the agent's knowledge), not just the workflow.

## Quick facts

- **Installed at:** Claude → Settings → Customize → Skills → *evidence-appraisal* (Author: You)
- **Triggers on:** requests to appraise / critically appraise / QC a systematic review, meta-analysis, NMA, or study protocol against a checklist or risk-of-bias tool.
- **Routing:** SR/MA manuscript → PRISMA 2020 + ROBIS + AMSTAR-2 · NMA → adds PRISMA-NMA · SR protocol → PRISMA-P · trial protocol → SPIRIT 2013.
