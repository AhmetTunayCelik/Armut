# 26 Fixes after panel round 2, 2026-11-08

## 1. Problem label
"Event services are invisible on Armut's own surfaces" (homepage lists, search suggestions, after-request screen), while typed search works and pros have spare capacity. Awareness outside Armut (ads, SEO) is a separate, later lever.

## 2. D1 runtime, made concrete (assumptions labelled)
Traffic: armut.com ~1.3M organic visits a month (Ahrefs ranking, date not shown; organic only). Share of visits that see the homepage or the empty search state: assumed 20-40% (check: search-open vs first-keystroke events). So ~60k-120k exposed visitors a week.
| Event submit baseline per exposed visitor (assumed) | Lift to detect | Weeks (50/50) |
|---|---|---|
| 0.3% | +20% | 2-4 |
| 0.3% | +10% | 9-18 |
| 0.5% | +20% | 1-3 |
Commitment for the deck: baseline 0.3%, minimum detectable lift +20%, run 4 weeks (covers 2+ full weekly cycles).
D1 is one variant: homepage tile + empty-state block together (one change to read, not two).
Tile tap: opens the search overlay with the "Düğün ve etkinlik" block expanded. No new page.
Decision rule: (a) primary up and guardrail holds: ship and rotate by season; (b) inconclusive after 4 weeks with guardrail holding: keep as low-risk seasonal default, put effort into P1; (c) guardrail breaks or 0-quote share rises past the kill line: stop.

## 3. Guardrail that can actually be measured
At ~400k per arm and a ~3% total request rate (assumed), the smallest change in total requests we can detect is ~3.6% relative (5.1% at 200k, 7.2% at 100k). So -0.5% cannot be read in a 4-week test.
- In-test guardrail: total submitted requests per exposed visitor, "no detectable drop", with the margin set at the detectable size (~-3.5% relative).
- Core cost measured properly with a long-running 10% holdout for 8+ weeks after launch.
- Ship math uses the same margin; -1.5% stays only as a stress case (break-even table unchanged: -0.5% core needs +5.6% events).

## 4. Supply gate and kill rule
Launch D1 and P1 only in service x city cells where at least most event requests get a quote within 48h (threshold from the data pull; start with İstanbul, Ankara, İzmir). Kill rule: if the 0-quote share on new event requests is more than a set number of points above organic after week 1 (proposed 5 points, to agree with analytics), stop that cell.

## 5. D1 and P1 run in parallel on separate layers
P1 has the stronger evidence (measured second needs) and reads in ~3 weeks; D1 is the only lever for new event demand. So: P1 starts week 2, D1 week 3, mutually exclusive layers. D1 still leads the story because the brief's problem is the small share.

## 6. Time promise on the success page
"Ne olacak?" shows the median time to first quote for that service and city when there is enough data; otherwise no time, only "teklifler bildirim ve e-postayla gelir".

## 7. Campaign page and local listing: one in-constraint change each
Campaign page (paid traffic lands here): headline copy test, event-specific, three variants:
- A awareness: "Armut'ta düğün fotoğrafçısı da var: 5 ücretsiz teklif al"
- B trust: "İstanbul'da [N] düğün fotoğrafçısı, gerçek müşteri yorumları"
- C speed: "Düğününe 1 hafta bile kalsa: bugün teklif al"
Primary: campaign landing to submitted request; guardrail: quotes per request (C may bring low-intent requests).
Local listing: one request to the head of product: in event categories, hide profiles inactive for 24+ months from the "En İyi 40" list. Guardrail: quotes per request and time to first quote (fewer visible pros must not slow quotes).

## 8. Deck rule
One headline and at most one key number per slide. Sample math, Monte Carlo, assumption register and most of the backlog go to the appendix. Time note: half a line.
