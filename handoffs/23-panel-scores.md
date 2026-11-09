# 23 Grading panel on the case study (round 1), 2026-11-08
Rubric (0-10 each, weights): R1 Problem framing 20%; R2 What you notice 20%; R3 Prioritization 20%; R4 First change/test 15%; R5 Measurement 10%; R6 Assumptions and data plan 10%; R7 Fit to brief 5%.
Panel: Armut Head of Product (hiring manager), ProntoPro Senior Growth PM, Product Analytics Lead, Design Lead, plus a red-team critic (no score). All simulated reviewers given the brief verbatim and the v5 recommendation.

## Head of Product: 74/100, "yes"
R1 7.5, R2 9, R3 6.5, R4 6.5, R5 7.5, R6 8, R7 5.
Impressed: used the product as a customer on three markets to real quotes; turned public page data into demand signals; designed within the HoP constraint.
Fixes: pick ONE first bet (D1), P1 next if D1 holds, plus one slide on why campaign page, local page and supply come later; primary metric = submitted event requests per homepage visitor (starts as diagnostic) with traffic, MDE, 2-4 week duration, seasonality; cut to 15 slides, Monte Carlo and options 3-7 to appendix, ranges labelled assumption-driven, one honest line on time spent and that test requests cost pros quote fees.
Interview question: "+20% event submits and -1.5% core requests: do you ship?"

## ProntoPro Senior Growth PM: 68.5/100, "lean hire"
R1 7, R2 8, R3 6, R4 7, R5 7, R6 7, R7 4.
Missing two-sided view: pro cost per hire on card leads; quote rate by lead time (will pros quote 7-day jobs?); date availability; disclose that test requests charged pros fees.
Benchmark: ProntoPro already has wedding photographer in homepage trending and an in-flow "Make up e stylist" add-on: a natural experiment; ask ProntoPro for tile CTR and add-on attach rate before building. Present D1 as "port and measure".
Gaps: tracker time estimate ("within a few hours") is the cheapest missing post-submit fix; changing the "when" default breaks the constraint; step count is not the main issue.
Fixes: cut to D1 + P1 + tracker time estimate; two-sided slide; benchmark slide around the ProntoPro natural experiment; primary metric = incremental total requests per new visitor, events secondary.

## Product Analytics Lead: 69.5/100
R1 7, R2 8, R3 6, R4 7, R5 6, R6 8, R7 6.
Do not put on a slide: precise P50s (1,521, 1,269), "4,300 (+4%)", ranking scores, yacht 7,100 (21 samples), 0.5% of marriages (only as "headroom exists"), ratings 4.8-4.9, the 80% hire band, the 13-example median as a number.
Base is customers, not requests: relabel.
Metric: primary = submitted event requests per exposed user; north star = event requests with 1+ quote in 48h; starts are diagnostic; "no past event request" is a pre-registered segment; guardrails need numeric non-inferiority margins, one decisive guardrail.
Design flaws: D1 x P1 interference (use mutually exclusive layers); marketplace spillover on shared supply (watch control-arm quote rates); cookie unit for logged-out users; daily SRM check; 2+ full weeks for novelty; November is low season; show real n.
Honest impact slide: "Sizing, not forecast. Event base ~100k customers/yr (estimate). D1 and P1 could each add roughly 1-2k requests/yr. The test decides." Rounded range bars and top 3 assumptions.

## Design Lead: 60/100
R1 6, R2 8, R3 5, R4 6, R5 4, R6 6, R7 6.
Biggest UX weakness: the card is a sales block on the screen where the user needs reassurance (no time estimate, no next step); starting a second full flow is heavy unless date and semt carry over. D1's "Bu sezon" text block is easy to skip and promotes organization services, not the brief's examples.
Coverage: campaign page and local listing (the worst friction) have no wireframe panel.
Fixes: "Ne olacak?" reassurance block above a 2-row collapsed card with honest carry-over labels; rename D1 block "Düğün ve etkinlik", top of empty state, include düğün fotoğrafçısı, doğum günü pastası, gelin makyajı; add annotated "today" panels for campaign page and local listing with why "next, not first".

## Red-team critic (no score)
Strongest attacks: (1) pro lead quality: pros pay per quote, low-intent leads cost them; (2) false-precision numbers that barely move the share (+4% on events = event share ~8.3% to ~8.6%); (3) homepage cannibalization metric gap; Armut's trending lists are probably popularity-ranked, so D1 must be framed as "editorial seasonal slot vs pure popularity".
Also: second needs may be covered by the first pro (organizer brings tables); show the failing search query behind the synonym fix; wedding photographer to bridal make-up is the brief's obvious pair; campaign page needs message match (landing page that delivers the ad's promise), not only a headline test; occasion SEO/paid search grows demand instead of moving it; interviewer will ask what Bulent decided himself.
Single change: one bet, primary metric that reaches Teklifi Seç or quotes, guardrails on total requests per homepage visitor and pro quote rate, break-even lift instead of point estimates, other ideas to a one-line backlog.

## Panel summary
Average 68/100 (74, 68.5, 69.5, 60). All four hire signals positive or lean positive. Strongest: R2 noticing (8-9 everywhere). Weakest: R7 fit/scope (4-6), R3 prioritization (5-6.5), R5 measurement (4-7.5).
Agreed fixes (applied in round 2, see handoff 24):
1. One first bet: D1 (new demand), framed as "editorial seasonal slot vs popularity ranking" and "port and measure" from ProntoPro; P1 second, only if D1 holds or in parallel on a separate layer. Explicit "why campaign page and local listing come next, not first".
2. Metrics: primary = submitted event requests per exposed user; north star = event requests with 1+ quote within 48h; starts are diagnostic; decisive guardrail = total submitted requests per homepage visitor with a preset non-inferiority margin; pro quote rate; test hygiene box.
3. Numbers: rounded ranges, break-even lift, base labelled "customers, estimate"; no point P50s on slides.
4. Two-sided slide: pro cost per hire, quote rate by lead time, supply pre-check; disclose test requests charged pros.
5. Benchmark slide: ProntoPro natural experiment (homepage trending + in-flow make-up add-on); ask for its data.
6. Post-submit: reassurance first (time estimate, what happens next), then a 2-row card; wedding photographer to bridal make-up row.
7. D1 UX: "Düğün ve etkinlik" block at the top with a marker, including the brief's three examples.
8. Wireframe: annotated "today" panels for campaign page and local listing.
9. Campaign page: message-match landing as the next bet (needs HoP OK on showing portfolio; pricing stays in the flow).
10. Scope: deck shows 3 opportunities, 1 bet, 1 test, 1 metric set; everything else is a one-line backlog; one honest line on time and AI use; list Bulent's own decisions.

# Round 2 (v6), 2026-11-08
| Grader | Round 1 | Round 2 |
|---|---|---|
| Head of Product | 74 (yes) | 78 (hire, lean strong) |
| ProntoPro Growth PM | 68.5 (lean hire) | 77 (lean hire) |
| Product Analytics Lead | 69.5 | 77 |
| Design Lead | 60 | 73 |
| Average | 68 | 76.25 |
Biggest gains: R5 measurement (4-7.5 to 7-8.5), R7 fit (4-6 to 6-9), R3 prioritization (5-6.5 to 7).
Remaining issues (all four agree on the first):
1. D1 runtime and reach unproven: no weeks, unknown share of sessions that see the empty search state; may be too small; an inconclusive result has no decision rule. P1 has stronger evidence and reads faster.
2. Guardrail margin (-0.5% total requests) is not detectable at D1's sample (needs ~20M per arm); ship math uses -1.5%, which breaks the margin.
3. Supply side asserted, not gated: launch only where pros quote within 48h; kill rule on 0-quote share.
4. Problem label: "invisible on-site" fits the lever better than "awareness".
5. Homepage tile tap destination undefined; [X saat] promise unchecked.
6. Campaign page and local listing diagnosed but not designed: one wireframed in-constraint change each.
7. Deck density: one headline and at most one key number per slide.
Fixes applied: handoff 26.

# Round 3 (v7), 2026-11-08
| Grader | R1 | R2 | R3 | R4 | R5 | R6 | R7 | Total |
|---|---|---|---|---|---|---|---|---|
| Head of Product | 8 | 9 | 7 | 8 | 8 | 8 | 6 | 79 (lean hire to hire, "ready") |
| ProntoPro Growth PM | 8 | 8.5 | 7.5 | 7.5 | 8.5 | 8 | 8 | ~80 (hire, "ready after 30-min trim") |
| Design Lead | 8 | 8.5 | 7.5 | 8 | 7.5 | 8 | 8 | 79.5 ("ready") |
| Analytics Lead | interrupted, not scored | | | | | | | |
Average of three: ~79.5 (round 1: 68, round 2: 76).
Remaining fixes (all small):
1. Name ONE first priority (D1); P1 "next"; campaign copy test and listing request to backlog with order and reason.
2. P1's metric is second-request rate per submitter (it cannot move the same-session submit).
3. D1 supply gate needs geo-targeting (homepage tile is not city-bound).
4. Competing explanation not tested: event buyers may prefer Instagram / düğün.com (channel preference, not invisibility). Add a cheap pre-test (fake-door tile for 1 week, event share of search logs).
5. Copy promises: "5 ücretsiz teklif" unchecked; "1 hafta bile kalsa" needs a supply check; [N] needs a low-count fallback.
6. Local listing: sketch one panel ("son 12 ayda aktif" filter), not only a request to HoP.
7. Log tile tap separately from the empty-state block; add a request-quality / cancellation guardrail for P1 requests; state the MDE (+20%) behind the 4-week runtime.
8. Too dense for 2-3 h: hygiene detail and Monte Carlo to the appendix.

# Round 4 (v8 + channel + trust), 2026-11-08
Head of Product: R1 8, R2 9, R3 7, R4 8, R5 8, R6 8, R7 6 = 79, "lean hire, close to hire". Last change: one bet only; D1 with photographer + organization (drop cake, which the channel finding argues against and which mixes two signals); fold P1, trust card, share link into one "next if D1 wins" line.
Red team, still landing: (1) a November test runs off-season: run pre-season (Feb-Apr) or read a seasonally adjusted lift; (2) event customers may start on Google/Instagram/venues, not the homepage; (3) impact ~1-2k/yr is small; (8) the trust card's "Garantisi does not cover non-delivery" needs legal and brand sign-off; (9) test requests cost pros real fees. Mostly fixed: power math, supply claim, volume vs value.
Prepared answer to the most likely attack ("customers start on Google and Instagram, and it is only ~1-2k; why first?"): "It is the cheapest event-only change my team can ship in a week, and it answers the key question: are event services invisible or unwanted? If it wins, the same block and supply gate move to the SEO price/local pages and the after-request screen, where the bigger volume is."
Panel trend: 68 -> 76 -> ~79.5 -> 79. Graders say ready; further rounds now give little.
