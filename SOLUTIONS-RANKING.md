# [SUPERSEDED: final answer is REPORT.md and SLIDES-SUMMARY.md, 2026-11-08]
# Solutions ranking for Bulent (v10, with Bulent's occasion-page and creator ideas), 2026-11-08
Goal (brief): grow request volume in event services, a small share today. Constraints (Bulent): no change to the shared request flow or pricing; event-only or layers on top; team 1 BE, 1 FE, 1 UX.
Panel average: 68 (round 1), 76 (round 2), ~79.5 (round 3, graders say "ready"), handoff 23. Changes: handoffs 24, 26, 27, 28 (channel preference: medium; lead D1 with photographer and organization services, cake as a test).

## Problem in one sentence
Event services are invisible on Armut's own surfaces: event customers are an estimated ~8% of demand, the homepage lists, search suggestions and the after-request screen show no event service, while typed search works and pros have spare capacity.

## What I noticed (the evidence the panel rated highest)
- Homepage: no event service in 36 listed services or in search suggestions; typed search maps event words well; ProntoPro already shows wedding photographer in its trending list.
- Campaign page: one "Başla" button, no price or work, masked reviews. Local listing: profiles from 2016, off-topic bios.
- Real demand (public Armut page estimates): ~108k event customers a year, mostly small and home-hosted; nişan organizasyon ~6x düğün organizasyon; wedding photographer requests are short-notice (13 dated examples).
- 0 of 315 cleaning/moving/furniture requests mention an event; 27 of 73 table-rental requests do. Organization requests often mention a second need; cake requests rarely do.
- Pros pay a fee per quote; hire is visible only via "Teklifi Seç".

## v11: platform framing (handoff 32)
Armut/ProntoPro is one company on one platform (shared job IDs and accounts). Findings and solutions are framed for all three markets; Armut data is labelled TR; occasion content is localized per market; tests start in TR with a ProntoPro replication. Final rating: handoff 31.

## v10 update (handoff 30)
D1 is now an occasion entry: homepage tile "Evleniyor musun? / Nişan, kına, düğün" and "Doğum günü mü var?" opening a grouped occasion page (Getir-inspired), each service into its own existing request flow, plus the search-suggestion block. Test: tile -> occasion page vs tile -> search overlay. Second bet: "Armut'ta buldum" creator program for event pros (quote-fee credit per tracked request, #reklam labels).

## The bet (one first priority: D1; order and pre-test in handoff 27)
Week 0: data pull + 1-week tile pre-test + 5 customer interviews (checks the competing explanation: event buyers may prefer Instagram, venues or düğün.com). Weeks 1-4: D1, geo-targeted to supply-gated cities, with wedding photographer and nişan/kına organization only (cake dropped: strong Instagram preference and it would mix two signals). Timing: run pre-season (Feb-Apr) or read a seasonally adjusted lift; a November test is off-season. The 10% long-term holdout (8+ weeks), not the 4-week test, decides the core cost. P1 after D1's first read; its metric is second event request within 14 days per submitter.
1. D1 (leads the story, only lever for new event demand): one variant = homepage tile + "Düğün ve etkinlik" block at the top of the search empty state (wedding photographer, bridal make-up, birthday cake + one seasonal item). The tile opens the search overlay with that block expanded (no new page). It tests an editorial seasonal slot against today's popularity ranking; ProntoPro already does this, so its tile data is the prior.
2. P1 (reads first, strongest evidence): after an event request, "Ne olacak?" first (median time to first quote for that service and city if known, else none; cancel link), then a 2-row next-service card from measured second needs.
Both run in parallel on separate layers (P1 week 2, D1 week 3), only in service x city cells where pros quote within 48h (start: İstanbul, Ankara, İzmir).
Campaign page now: event headline copy test (awareness / trust / speed), primary = landing to submitted request. Local listing now: one request to the head of product to hide event profiles inactive 24+ months, guardrail quotes per request. Bigger page changes need the head of product (price or work before the request).

## How success is measured
Primary: submitted event requests per exposed user. North star: event requests with 1+ quote within 48h. Diagnostic: starts, CTR. Segment (D1): users with no past event request.
D1 runtime (assumed: ~1.3M organic visits a month, 20-40% see homepage or empty search, 0.3% event submit baseline): +20% lift readable in 2-4 weeks; plan 4 weeks.
Guardrail: total submitted requests per exposed visitor, "no detectable drop" at the size the test can see (~3.5% relative); real core cost from a 10% long-term holdout over 8+ weeks. Break-even: each -0.5% core needs +5.6% events.
Kill rule: 0-quote share on new event requests more than ~5 points above organic after week 1 (to agree with analytics) stops that cell.
Decision: up and guardrail holds: ship and rotate by season. Inconclusive after 4 weeks: keep as low-risk seasonal default, focus on P1. Guardrail or kill rule breaks: stop.
Also: pro quote rate, Teklifi Seç rate vs organic, pro complaints, opt-outs. Hygiene: separate layers, daily sample-ratio check, 2+ full weeks, control-arm quote watch, low-season caveat.

## Impact, honestly
Sizing, not forecast. If they work, D1 and P1 could each add roughly 1-2 thousand event requests a year (assumption-driven; the test decides). Three assumptions move it most: homepage event CTR, card CTR, incrementality. The Monte Carlo is in the appendix (handoff 18).

## Two-sided check
Pro cost per hire on new leads must not be worse than organic; quote rate by lead time before pushing near-date demand; supply count is not the limit. Disclosure: test requests used real pro quote fees; cancel them.

## Data I would ask for first
Event request funnel (12 months) by step, entry point, traffic source and logged-in status; quote rate within 48h by service, city and lead time; ProntoPro homepage tile CTR and make-up add-on attach rate.

## Backlog (one line each)
Next if D1 wins (one line on the slide): P1 post-submit card, trust card (needs legal and brand sign-off before any test), pro share link. Trust test (cheap, 2-3 weeks, event campaign and listing pages): "Ön ödeme yapmadan önce..." guidance card + review recency labels (handoff 29); fits as the concrete trust variant of the campaign copy test.
Next after P1: pro share link for Instagram bios and DMs (works with the channel event buyers already use, handoff 28).
Abandoned-start recovery (logged-in/app); price and local page upgrade (city split); campaign landing with message match (needs HoP OK); WhatsApp concierge pilot; birthday comeback reminder; occasion SEO and paid search; offline QR with venues and jewelers; event-only listing freshness rule.
Dropped: price or work before the request, optional free text, "when" default change (shared flow); keyword trigger from cleaning/moving (0/315).

## What you decide
(a) D1 + P1 in parallel as above (recommended); (b) P1 only, if you want the safest, fastest read; (c) add the campaign message-match landing if you can clear it with the head of product.
