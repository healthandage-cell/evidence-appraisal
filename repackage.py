#!/usr/bin/env python
r"""
Repackage the evidence-appraisal skill into installable files.

Run this after editing anything in .\evidence-appraisal\ (SKILL.md, references, assets).
It reads the version: from SKILL.md and writes two identical packages next to this script:
    evidence-appraisal.skill   (upload this in Claude -> Settings -> Customize -> Skills -> Add)
    evidence-appraisal.zip     (fallback if the file picker only shows .zip)

Then re-add the package in the Skills panel to publish the update (bumps "Last updated").
Editing the folder alone does NOT change the already-installed skill.

Usage:   python repackage.py        (from this folder)
"""
import os, re, sys, zipfile

ROOT = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.join(ROOT, "evidence-appraisal")
SKILL_MD = os.path.join(SKILL_DIR, "SKILL.md")

def main():
    if not os.path.exists(SKILL_MD):
        sys.exit(f"ERROR: SKILL.md not found at {SKILL_MD}")

    # read version for the log line
    ver = "?"
    with open(SKILL_MD, encoding="utf-8") as f:
        m = re.search(r'^version:\s*"?([^"\n]+)"?', f.read(), re.M)
        if m: ver = m.group(1).strip()

    outputs = [os.path.join(ROOT, "evidence-appraisal.skill"),
               os.path.join(ROOT, "evidence-appraisal.zip")]
    files = []
    for dirpath, _, filenames in os.walk(SKILL_DIR):
        for fn in filenames:
            full = os.path.join(dirpath, fn)
            arc = os.path.relpath(full, SKILL_DIR).replace("\\", "/")  # SKILL.md at archive root
            files.append((full, arc))

    for out in outputs:
        with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
            for full, arc in sorted(files, key=lambda t: t[1]):
                z.write(full, arc)

    print(f"Packaged evidence-appraisal v{ver}  ({len(files)} files):")
    for out in outputs:
        print(f"   {out}  ({os.path.getsize(out)} bytes)")
    print("\nNext: Claude -> Settings -> Customize -> Skills -> Add -> select the .skill file to publish the update.")

if __name__ == "__main__":
    main()
