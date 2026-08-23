=== THIS RUN: POSITIONS — POSTDOCS AND JOBS ===

Owned tabs: postdocs, jobs.

SCOPE — advertised positions the candidate could apply to: postdoc and research
staff posts in academia and research institutes (postdocs.tsv), and roles
beyond academia — industry research, pharma/biotech, clinical research, medical
affairs, medical writing, consulting, science policy (jobs.tsv).

[TODO before the first real run: fill prompts/profile.md, replace every [TODO]
in this file with the agreed fields, geographies and keywords, and regenerate
prompts/out/ with `python3 prompts/build_prompts.py`.]

=== THE FIVE BRANCHES — one subagent each, boundaries are binding ===

BRANCH 1 — EURAXESS AND EU PORTALS.
  euraxess.ec.europa.eu job search, researcher profile R2 (recognised), fields
  [TODO: from the profile], countries [TODO: the YES and MAYBE lists]. Include
  vacancies inside MSCA doctoral/postdoc networks and ERC-funded teams.
  OUT OF SCOPE: national boards (branch 2), industry (branch 4).

BRANCH 2 — ACADEMIC JOB BOARDS, WORLDWIDE.
  jobs.ac.uk, Nature Careers, Science Careers, academicpositions.com,
  findapostdoc.com, AcademicTransfer (NL), university job pages surfaced by
  those boards. [TODO: add/remove boards by target country — e.g. HigherEdJobs
  for the US, Seek for AU, Interfolio-listed searches.]
  OUT OF SCOPE: EURAXESS (branch 1), anything not academic.

BRANCH 3 — INSTITUTION-DIRECT.
  The target institutions from the profile, careers pages opened one by one:
  [TODO: named list once the profile exists — e.g. Max Planck institutes,
  EMBL, Karolinska, Champalimaud, Instituto Cajal, NIH intramural…]. Many
  strong groups never post to aggregators; this branch exists because the
  boards do not cover it.
  OUT OF SCOPE: anything already covered by branches 1-2 this same run.

BRANCH 4 — BEYOND ACADEMIA (jobs.tsv).
  Sectors from the profile's ranking [TODO: e.g. pharma/biotech R&D, CROs,
  medical affairs, medical writing, neurotech, digital health, consulting].
  LinkedIn job search with the profile's role titles [TODO], BioSpace, company
  careers pages of [TODO: named companies]. Record Remote_or_Onsite and Sector
  on every row.
  OUT OF SCOPE: academic posts of any kind.

BRANCH 5 — INBOX AND NOVELTY.
  YOU ARE THE INBOX READER for the week. Nobody else will read the mailbox, so
  a message you fail to log is a message the whole week loses.
  In scope: FIRST the Gmail inbox pass and the inbox_triage table described in
  the shared block — route every relevant message, and use UNCLEAR freely
  rather than guessing. THEN the novelty sweep — positions posted in the last
  7-14 days anywhere, found in newsletters, LinkedIn digests, society job
  boards and other unindexed places.
  OUT OF SCOPE: anything already recorded and unchanged.

=== SEARCH ANGLES TO ROTATE ===

- by role: postdoc, "postdoctoral fellow", "postdoctoral researcher",
  "research fellow", "research scientist", "staff scientist", "junior group
  leader", [TODO: clinical-track titles if the clinic stays in play]
- by topic: [TODO — the profile's research lines and techniques, in English
  and in the languages of the target countries]
- by place: [TODO — target cities/countries from the profile]
- by time: posted-this-week filters, "deadline 2026", newest-first sorts

Each branch must report at least one source it had not used before, or state
explicitly that it looked and found none.

FOR EVERY ROW SCORING 4 OR 5, the Fit_Rationale must answer concretely:
- why it fits HER specifically — which research line, which technique, which
  part of the MD+PhD combination the employer actually values
- what the application needs (letters, research statement, talk, references)
  and how much work that realistically is, against the deadline pressure
- salary/contract terms versus the profile's floor, when published
- visa/relocation implications given the profile's mobility list
- who to contact and with what hook, when a named PI or hiring manager exists
