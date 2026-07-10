# How to rebuild the skill as a Microsoft 365 Copilot agent

Microsoft 365 Copilot (the enterprise Copilot across Word, Teams, etc.) does **not** use the
`SKILL.md` format — that's GitHub Copilot. The equivalent here is a **Copilot agent**: instructions
plus knowledge. Everything you need is in this folder.

**You have two build routes — pick by how widely it needs to be shared.**

---

## Route A — Lightweight: "Create agent" inside Microsoft 365 Copilot (fastest)

Best for personal use or sharing with a few colleagues.

1. Open **Microsoft 365 Copilot** (the Copilot chat / BizChat, e.g. at m365.cloud.microsoft or in Teams).
2. Go to the **Agents** area and choose **Create agent** (or "Build your own").
3. Switch to the **Configure** tab and fill in:
   - **Name:** Evidence Appraisal
   - **Description:** Appraises systematic reviews, meta-analyses and study protocols against PRISMA 2020, PRISMA-NMA, ROBIS, AMSTAR-2, PRISMA-P and SPIRIT.
   - **Instructions:** paste the whole block from **`agent-instructions.md`**.
4. Under **Knowledge**, upload **`knowledge-checklists.docx`** (Word, upload-ready). This gives the agent the actual checklists to work from.
5. **Create / Save**, then use **Share** to give access to specific colleagues.

## Route B — Governed: Copilot Studio (for org-wide / IT-managed publishing)

Best if the agent should be published to the whole organisation or needs SharePoint knowledge sources.

1. Open **Copilot Studio** → **Create** → **New agent**.
2. Set the name/description as above; paste **`agent-instructions.md`** into the agent's instructions.
3. Add **Knowledge** → upload **`knowledge-checklists.docx`**, or point it at a SharePoint/OneDrive folder holding the checklists.
4. Test in the built-in chat, then **Publish**. Publishing org-wide typically needs **admin approval** in the Microsoft 365 admin centre — loop in your IT/Copilot admin.

---

## Knowledge file format note

Upload **`knowledge-checklists.docx`** — it's already in Word format, which Microsoft 365 knowledge
accepts directly, so there's nothing to convert. (`knowledge-checklists.md` is the editable source;
regenerate the `.docx` from it — e.g. open in Word and Save As, or `pandoc knowledge-checklists.md -o
knowledge-checklists.docx` — whenever you update the checklists.)

## The lightest option of all — a saved prompt

If a full agent is more than she needs, she can save the instruction text as a reusable prompt in the
**Copilot Prompt Gallery** and paste the document in each time. It won't carry the checklists as
grounded knowledge, so it's less rigorous than an agent — fine for a quick check, not for dossier work.

## Governance reminder

Enterprise Copilot agents and their knowledge files sit inside your Microsoft 365 tenant and follow its
data-handling and DLP policies. Uploading published papers and internal drafts as knowledge is normally
fine, but confirm with your Copilot/IT admin before publishing anything beyond your own account.
