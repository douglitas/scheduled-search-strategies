=== THIS RUN: FELLOWSHIPS AND FUNDED MOBILITY ===

Owned tabs: fellowships, watchlist_closed.

SCOPE — money the candidate applies to herself and carries to a host: postdoc
fellowships, incoming/outgoing mobility programmes, short-stay and travel
grants, thesis and young-investigator prizes. If the money is attached to an
advertised post someone else opened, it belongs to the positions routine, not
here.

[TODO before the first real run: fill prompts/profile.md, resolve every [TODO]
below, and regenerate prompts/out/ with `python3 prompts/build_prompts.py`.]

=== THE FIVE BRANCHES — one subagent each, boundaries are binding ===

BRANCH 1 — EU AND INTERNATIONAL FLAGSHIPS.
  MSCA Postdoctoral Fellowships (check the mobility rule against the profile's
  last-3-years residence accounting before scoring), EMBO Postdoctoral
  Fellowships (rolling), HFSP, ERC (as a horizon: note when her clock would
  allow a Starting Grant), [TODO: others by field]. FENS and IBRO programmes
  for neuroscience.
  OUT OF SCOPE: national programmes (branch 2).

BRANCH 2 — NATIONAL AND REGIONAL PROGRAMMES.
  By target country from the profile [TODO: keep only the countries in play].
  If Spain: Juan de la Cierva, Ramón y Cajal, and the ISCIII family — Sara
  Borrell, Miguel Servet, Río Hortega — which is built for MD-PhD profiles;
  la Caixa Junior Leader. If Germany: Humboldt, DFG Walter Benjamin. If UK:
  Wellcome Early-Career, MRC fellowships. If US: NIH F32/K99 equivalents where
  a non-citizen is eligible. [TODO: complete per profile.]
  OUT OF SCOPE: EU-level (branch 1).

BRANCH 3 — FOUNDATIONS AND FIELD-SPECIFIC FUNDERS.
  [TODO by research line: disease foundations relevant to her topic, private
  neuroscience funders, women-in-science programmes (e.g. L'Oréal-UNESCO For
  Women in Science), bilateral country funds.]
  OUT OF SCOPE: anything a branch above already owns.

BRANCH 4 — TRAVEL, SHORT STAYS AND PRIZES.
  Conference travel grants, lab-visit and exchange grants (EMBO short-term,
  Company of Biologists, society travel awards), thesis prizes,
  young-investigator awards. Small money, small applications, high
  acceptance — the LOW-competition end of this database.

BRANCH 5 — REOPENINGS AND THE WATCHLIST.
  A separate branch with its own budget, learned the hard way in the sibling
  tracker: bolted onto another branch it hits the call ceiling and rows come
  back unverified.
  In scope: every row in watchlist_closed, one at a time. Has it reopened? Has
  a date been announced? Is the expected-reopen estimate still credible? Also
  chase annual calls whose window is approaching before the text is published.
  OUT OF SCOPE: new discovery of any kind.

=== SEARCH ANGLES TO ROTATE ===

- by instrument: "postdoctoral fellowship", "mobility grant", "career
  development award", "young investigator", beca posdoctoral, ayudas,
  convocatoria, [TODO: terms in target-country languages]
- by funder: name each agency and foundation directly and look for its newest
  call and its call calendar
- by field: [TODO — the profile's research lines]
- by time: "call 2026", "call 2027", deadline calendars, funder newsletters

Each branch must report at least one source it had not used before, or state
explicitly that it looked and found none.

SCORING NOTES SPECIFIC TO THIS RUN

- THE CLOCKS GATE EVERYTHING. Years_PostPhD_Window against the profile's
  defense date; mobility rules against the residence accounting; MD-specific
  tracks noted explicitly (they are rarer and less competed). A call she ages
  out of before its next deadline is CLOSED for her: record it, say so in
  Fit_Rationale, and never surface it again.
- Annual calls: when closed, estimate the next window with a confidence level
  and park the row in watchlist_closed rather than deleting it.
- Host requirement: many fellowships need a committed host group BEFORE
  applying. When that is the case, say so in Host_Requirement and cross-link
  the groups tab in Next_Action («needs host: see L-#### candidates»).

FOR EVERY ROW SCORING 4 OR 5, the Fit_Rationale must answer concretely:
- why it fits HER specifically, and which research line to lead with
- eligibility verified against the clocks, item by item
- what the application needs and how much work it realistically is
- whether a host must be secured first, and how long that usually takes
