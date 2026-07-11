#!/usr/bin/env python
r"""
Build a SELF-CONTAINED single-file SKILL.md.

Some hosts (e.g. Claude Desktop's Customize -> Skills upload) keep only SKILL.md
and drop bundled subfolders (references/, assets/). This inlines every checklist
and the report template into one SKILL.md so nothing is lost on install.

Outputs (next to this script):
    standalone/SKILL.md                     -- the single-file skill
    evidence-appraisal-standalone.skill     -- upload THIS to Claude Desktop
    evidence-appraisal-standalone.zip        -- identical (fallback if picker filters to .zip)

Re-run after editing the modular skill or checklists, then re-upload the .skill.
"""
import os, zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(ROOT, "evidence-appraisal")
REFS = ["prisma-2020.md", "prisma-nma.md", "robis.md", "amstar-2.md",
        "prisma-p.md", "spirit-2013.md", "consort-2010.md"]

def read(*p):
    with open(os.path.join(*p), encoding="utf-8") as f:
        return f.read().rstrip()

skill = read(SRC, "SKILL.md")

# Point the workflow at the inlined content instead of external files.
skill = skill.replace(
    "Open the relevant reference file(s) and work through every item.",
    "Work through every item using the relevant checklist in the **Appraisal checklists** "
    "section at the end of this file — every checklist is inlined here, so there are no "
    "external files to open.")
skill = skill.replace(
    "Use `assets/report-template.md` as the fixed structure.",
    "Use the **Report template** at the very end of this file as the fixed structure.")

parts = [skill, "", "---", "",
         "# Appraisal checklists (inlined)", "",
         "The full checklists the routing table above points to. Apply the one(s) for the",
         "detected document type, item by item, quoting the supporting text verbatim."]
for fn in REFS:
    parts += ["", "", "---", "", read(SRC, "references", fn)]

parts += ["", "", "---", "", "# Report template", "", read(SRC, "assets", "report-template.md")]

os.makedirs(os.path.join(ROOT, "standalone"), exist_ok=True)
out_md = os.path.join(ROOT, "standalone", "SKILL.md")
with open(out_md, "w", encoding="utf-8") as f:
    f.write("\n".join(parts) + "\n")

for ext in (".skill", ".zip"):
    with zipfile.ZipFile(os.path.join(ROOT, "evidence-appraisal-standalone" + ext),
                         "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.write(out_md, "SKILL.md")

lines = sum(1 for _ in open(out_md, encoding="utf-8"))
print(f"standalone/SKILL.md: {os.path.getsize(out_md)} bytes, {lines} lines "
      f"(inlined {len(REFS)} checklists + report template)")
