=== THIS RUN: ECOSYSTEM — GROUPS, EVENTS, TRAINING ===

Owned tabs: groups, events, training.

SCOPE — the map around the applications: research groups worth approaching
(with or without an open posting), the conferences where the field meets, and
the courses that close a skills gap or put her in the right room.

=== THE FOUR BRANCHES — one subagent each, boundaries are binding ===

BRANCH 1 — GROUP DISCOVERY.
  Find research groups worth approaching in statistical genetics of complex
  traits, psychiatric genetics (GWAS/PRS), infant/toddler sleep genetics, and
  behavioural/cognitive neuroscience, across EU/EEA, Australia, USA, UK and
  other English-speaking countries (lower priority elsewhere, never dropped).
  Rotate the discovery angle weekly so the same names do not come back:
  (a) last month's papers in Nature Genetics, Nature Human Behaviour,
  Molecular Psychiatry, Biological Psychiatry, American Journal of Psychiatry,
  Psychological Medicine, Behavior Genetics, Genes Brain and Behavior, SLEEP,
  Journal of Sleep Research, Nature Mental Health, Human Molecular Genetics,
  PLOS Genetics; (b) speaker and organiser lists of the field's conferences
  (branch 2); (c) fresh grant awards — an ERC, Wellcome or national award
  announced this year is a PI with money to hire; (d) editorial boards and
  society committees; (e) Psychiatric Genomics Consortium (PGC) working-group
  membership lists — a direct map of who is active in GWAS/PRS psychiatric
  genetics right now.
  For every group record: PI, institution, research lines, techniques, whether
  they are known to be hiring (Openings_Known), funding status with its
  source, and the realistic Contact_Route — a cold email to the PI is normal
  in academia; note who to address and with what hook.
  OUT OF SCOPE: groups already in the table (branch 4 owns them).

BRANCH 2 — EVENTS.
  Conferences and congresses: World Congress of Psychiatric Genetics (WCPG —
  the central venue for her GWAS/PRS line), American Society of Human
  Genetics (ASHG) annual meeting, European Society of Human Genetics (ESHG)
  conference, Behavior Genetics Association annual meeting, FENS Forum, SfN
  annual meeting, Sleep Research Society and European Sleep Research Society
  (ESRS) annual meetings (sleep genetics), Biological Psychiatry meeting.
  Record dates, venue, abstract deadline (that is the Deadline column — the
  clock that matters), early-bird fees, and whether the event carries its own
  travel grants (Travel_Grant_Available; cross-link the fellowships routine
  when a separate grant covers it).
  OUT OF SCOPE: courses (branch 3).

BRANCH 3 — TRAINING.
  Summer schools, advanced practical courses, workshops and certifications:
  CAJAL programme, EMBO practical courses, CSHL, the International Statistical
  Genetics workshop ("Boulder Workshop", Colorado — directly on her core
  technique), PGC analyst training/workshops, PLINK/PRSice/LDpred
  methods courses, ESRS summer school (sleep). Record application deadlines,
  fees, stipends and fee waivers (Funding_Available).
  OUT OF SCOPE: degree programmes; anything longer than a few weeks.

BRANCH 4 — GROUPS FOLLOW-UP.
  Existing rows in groups.tsv, one at a time: new papers, new grants, people
  leaving (a departing postdoc is an opening that will never be advertised),
  postings opened since last check. Update the row and Change_Flag; do not
  rediscover what the table already knows.
  OUT OF SCOPE: new discovery (branch 1).

=== BACKSTOP DUTIES — you are the last routine of the morning ===

- `data/inbox_triage.tsv` must end the week with nothing PENDING, whatever the
  beat: resolve every row the earlier routines routed but did not close.
- `data/source_inbox.json` must end the week with nothing PENDING, whatever
  the beat.

=== SEARCH ANGLES TO ROTATE ===

- by people: PI names once known, "lab of X", recent-award announcement pages
- by topic: statistical genetics, complex traits, GWAS, polygenic risk
  scores, psychiatric genetics, behavioural genetics, infant/toddler sleep
  genetics, human GWAS cohorts, PRS methodology
- by place: Spain, EU/EEA broadly, Australia, USA, UK, other English-speaking
  countries; lower priority (not excluded) elsewhere
- by time: "abstract deadline 2026", "applications open", course calendars

Each branch must report at least one source it had not used before, or state
explicitly that it looked and found none.

FOR EVERY ROW SCORING 4 OR 5, the Fit_Rationale must answer concretely:
- groups: why this group for HER — line, technique, culture, funding runway —
  and what the first approach should say
- events: what she gets out of attending (visibility, named contacts, a
  session that matches her work) against cost and clock
- training: which profile gap it closes and whether funding covers it
