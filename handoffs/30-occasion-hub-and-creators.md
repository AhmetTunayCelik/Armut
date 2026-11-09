# 30 Bulent's two ideas, discussed by agent panels, 2026-11-08

## A. Occasion entry + grouped page (Bulent: "Evleniyor musun? Here are our offers", like Getir recipes with all ingredients)
Panel: UX, Engineer, Event Expert, Critic.
- Getir: recipe-to-basket not confirmed in open sources (Assumption: exists in app; add a screenshot). Confirmed Getir features: "Alışveriş Listem" (photo of a list into a cart) and "Hazır Sepet" (~90% of pilot users kept the ready basket unchanged), ekonomim.com, Getir 10th anniversary. Say "inspired by", not proven.
- Carries over: start from the user's goal (the occasion), group what goes together. Does not: no single basket, quotes arrive later per service, booking times differ (venue/photographer months ahead, cake days), pros pay per quote. So no "request all" button: each tile opens its own existing request flow.
- Benchmark: thumbtack.com/events groups party services by occasion with average prices; weddings on a separate page; no timeline.
- Design: one page per occasion (Nişan/Kına/Düğün; Doğum günü), services ordered by measured co-need (tables/chairs 21-44%, palyaço 17%, music 19%), venue first for nişan if data confirms; "Talep edildi" state on used tiles; no timeline until evidenced.
- Effort: FE 1-2 weeks, BE small (service lists config, origin tracking), UX 1 week; only shared touch is the homepage module slot.
- Metrics: event requests per hub visitor; share sending 2+ event requests in 30 days; guardrails total homepage requests, quote-to-hire on hub requests, pro complaints.
- Panel verdict: keep D1's logic, use the hub as the destination. Decision (Product Lead, following Bulent's preference): D1 becomes "occasion tile -> occasion page" plus the search-suggestion block; test arms: tile -> occasion page vs tile -> search overlay. Start with Nişan/Kına and Doğum günü (volume), not wedding photographer alone.

## B. "Armut'ta buldum" creator tagging, sponsored with quote-fee credit
Panel: Growth, Supply Ops, Legal/Brand, Analyst.
- Fact: Trendyol runs a creator program with tracked-link commission (trendyol.com/en/s/trendyol-influencer-program). Thumbtack pro rewards pay for referring pros, not customers.
- Fact: Ministry of Trade influencer guideline: benefit-based posts must be labelled (#reklam / #işbirliği), advertiser shares responsibility (ticaret.gov.tr). A fee credit is a benefit, so labels are required.
- Must-haves: claim must be true (only pros with a real Armut-won job), customer consent for photos (KVKK), written creator agreement, Armut checks posts.
- Design: event pros with 1+ completed Armut job, good rating, active Instagram; reward = quote-fee credit per tracked request (or per hire), not per post; tracking via short redirect armut.com/r/CODE into the existing flow; option: referring pro guaranteed one of the 5 quote slots.
- Customer-influencer variant: skip (pros set prices; Armut would fund discounts).
- Pilot: 20-30 Istanbul event pros, 8 weeks incl. season start. Metrics: tracked requests per pro, request-to-hire, cost per tracked request vs paid-ads cost per request, quote fill. Kill rule: cost per request above paid ads, or under ~1/3 of pros post.
- Cost: CPR = (credits redeemed x real cost per credit + ops/legal) / tracked requests; compare ad CPR.
- Risk: top pros may not send followers where 4 competitors quote (interview 8-10 pros).
- Verdict: second bet, the off-site channel; runs with little FE work, after or in parallel with D1.
