# 24 Round 2 improvements after the grading panel, 2026-11-08
Source of each change: handoff 23. Numbers below use public estimates (customers, not requests) and example baselines where Armut data is missing; all labelled.

## 1. One first bet, one next bet
- First bet: D1, event entry where new users look (homepage lists and search empty state). It is the only Tier-1 idea that creates new event demand, which is the brief's "small share" problem.
  Framing: "Armut's lists are most likely ranked by popularity, so events never surface. D1 tests an editorial, seasonal event slot against pure popularity." And: "ProntoPro (same group) already shows wedding photographer in its homepage trending list: port and measure, using ProntoPro's tile data as the prior."
- Next bet: P1 post-submit card, on a separate experiment layer, starting with reassurance (see 5).
- Backlog (one line each in the deck): abandoned-start recovery, price/local page upgrade, copy angle test, WhatsApp concierge, birthday reminder, offline QR, occasion SEO.
- Why campaign page and local listing come next, not first: their fixes (portfolio and proof on the page, list ranking cleanup) touch shared page templates and ranking logic, and showing price or work before the request was ruled out by the head of product; they need that conversation first. The copy test on the campaign headline is the safe step now.

## 2. Metrics (rewritten)
- Primary (both tests): submitted event requests per exposed user (D1: per homepage/search visitor; P1: per submitter).
- North star: event requests that get 1+ quote within 48 hours. Volume only counts if pros answer it.
- Diagnostic: request starts, tile/row CTR, step completion.
- Pre-registered segment (D1): users with no past event request.
- Decisive guardrail (D1): total submitted requests per homepage visitor, non-inferiority margin set before launch (e.g. no worse than -0.5%, to agree with analytics).
- Other guardrails: pro quote rate on event requests; 0-quote share; Teklifi Seç rate on card leads vs organic; pro complaints; opt-outs.

## 3. The trade-off math (break-even)
Armut ~1.32M requests a year (110,000+/month, info.armut.com); event customers ~108,000 (estimate) = ~8%; everything else ~1.21M, 11x the event base.
| Core requests lost on the homepage | Event lift needed to break even |
|---|---|
| -0.5% | +5.6% |
| -1.0% | +11.2% |
| -1.5% | +16.8% |
HoP's interview question ("+20% events, -1.5% core: ship?"): +21,600 event vs -18,180 core = +3,420 net requests. Ship only if (a) the net is positive in value, not just count (event vs core revenue per request, unknown), (b) the core loss is real loss, not deferral (check core requests per user over 4 weeks), (c) event requests still get quotes. Otherwise rotate the slot seasonally to cut the core cost.

## 4. Honest sample sizes (n per arm = 16 p(1-p)/d^2; baselines are examples)
D1, event submits per homepage visitor:
| Baseline | Detect +10% relative | Detect +20% relative |
|---|---|---|
| 0.2% | ~800k | ~200k |
| 0.3% | ~530k | ~133k |
| 0.5% | ~320k | ~80k |
So D1 needs very large homepage traffic or a larger expected lift; real traffic decides duration. Read on the full homepage cohort, not reach/52.
P1, second event request within 14 days, baseline 3% (example), wave-1 entry services ~40,900 a year (~785 a week): +2 points needs ~1,200 per arm (~3 weeks); +1 point needs ~4,700 per arm (~12 weeks).
Test hygiene: mutually exclusive layers for D1 and P1 (a D1 user who submits must not also be in P1 treatment); daily sample-ratio check; at least 2 full weeks (novelty); control-arm quote rate watched (shared pro supply); logged-out unit is a cookie (cross-device dilution); November is low wedding season, so wedding results do not generalise to May-September.

## 5. Two-sided view (new slide)
- Pros pay a non-refundable fee per quote. Measure pro cost per hire on card and slot leads: quotes per request x fee / hires. It must not be worse than organic event leads.
- Quote rate by lead time: will pros quote a 7-day job? Pull it before pushing near-date demand.
- Date availability: a fixed-date event quote from a booked pro is waste for both sides.
- Supply count is not the limit (Istanbul lists ~937 wedding photographers for ~1-2 Armut requests each a year, estimate), so pros want more leads, but only good ones.
- Disclosure: the case used real test requests on Armut, ProntoPro and Homerun; pros spent quote fees on them. Say this in one line and cancel the requests.

## 6. Post-submit: reassure first, then sell
Success page order: (1) "Ne olacak?" block: quotes arrive by notification and email, typical time (ProntoPro and Homerun promise "within a few hours"; Armut's own number from data), cancel link; (2) a 2-row card, collapsed by default, with an honest carry-over label ("Şehir hazır" if prefill works, else "~2 dk"). The time estimate is the cheapest missing post-submit fix and fits the constraint.
Wedding row added: düğün fotoğrafçısı to gelin makyajı and gelin arabası süsleme (the brief's own pair; 7% of photographer requests mention make-up; make-up often books earlier, so measure).

## 7. D1 UX
Block "Düğün ve etkinlik" at the top of the search empty state with a visual marker: Düğün Fotoğrafçısı, Doğum Günü Pastası, Gelin Makyajı (the brief's examples), plus one seasonal item. Homepage tile: "Nişan, kına, doğum günü: ücretsiz teklif al". Synonym fix only for queries that fail today (shown: "takı töreni" suggests jewelry making, no photographer).

## 8. Numbers allowed on slides
Allowed: counts read from Armut pages, labelled "public page estimate"; measured shares with sample size (e.g. "0 of 315"); break-even table; rounded ranges ("roughly 1-2k a year each, the test decides"). Not on slides: P50 point values, ranking scores, yacht 7,100, ratings, 80% band; these stay in the appendix or files.

## 9. Scope and honesty
Deck: 3 opportunities, 1 bet, 1 test, 1 metric set, 1 backlog slide. One line: time spent was above the 2-3 hour guide, and how AI was used (agents for research and critique; decisions by Bulent: kept the request flow and pricing out of scope, chose discovery and next-service as the direction, approved the card).
