# Making event services visible: an occasion entry for Armut / ProntoPro
APM case study report, Bulent Çelik, November 2026. Final version (supersedes earlier rankings).

## 1. Goal and constraints
- Goal (brief): increase request volume in event services (wedding photographer, birthday cake, bridal make-up and similar), today a small share of requests.
- Team: 1 backend, 1 frontend, 1 UX designer.
- My working constraint: no change to the shared request flow or the pricing model (a range is shown, the pro sets the price), because both affect every category. Solutions are event-specific layers on top; everything added is display and navigation, outside the flow.
- Scope: Armut (TR), ProntoPro (IT) and Homerun (UK) as one company; the three sites share the same request flow and page templates, so one build can serve all markets (see appendix for the evidence).

## 2. How I worked
- Walked the three entry points from the brief (homepage search, campaign service page, local listing) on all three sites on mobile, and sent real wedding-photographer requests to the end of each flow. Two real quotes came back on Homerun.
- Read public data on the sites: price pages with real past requests (free text, dates, prices) and pro sign-up pages with yearly request counts.
- Worked with Claude as an agent team: researchers, an event-industry expert, supply/ops, engineer, analyst, UX, a fact checker, a red-team critic and a review panel playing hiring-team roles. I set direction and constraints and chose the solution; agents researched, challenged and drafted. The transcript is shared.
- All numbers below are public-page estimates or small samples, labelled as such. Time spent was above the 2-3 hour guide, mostly on verification and waiting for real quotes.

## 3. What I noticed
### 3.1 Homepage search
- Armut's homepage lists 36 services (trending and popular); none is an event service. The search box's default suggestions list moving, painting, cleaning, psychologist, driving lessons.
- ProntoPro shows one event service (wedding photographer) in trending; Homerun shows none.
- Typed search works well: "kına" returns Kına Organizasyon, Kına Mekanları, Kına Fotoğraf Çekimi; "1 yaş" returns Doğum Günü Organizasyonu, Palyaço. Weak spots exist ("takı töreni" returns jewelry making, no photographer).
- Reading: people find event services only if they already know the platform offers them.
### 3.2 Campaign service page
- One "Başla" button, no price, no pro work, review names masked. The price range appears only inside the flow. Same template on all three sites.
- Reading: trust is thin at the point where event buyers, who usually choose from Instagram portfolios, compare.
### 3.3 Local listing
- "En İyi 40" lists include profiles from 2015-2017, off-topic bios and a placeholder text, on all three sites.
### 3.4 The request flow and after it
- Flows: 6 steps + sign-up (Armut), 8 + login (ProntoPro), 4 + login (Homerun). Same "when" options and default ("within three weeks") everywhere.
- After a request, ProntoPro and Homerun promise quotes "within a few hours" with a cancel link; Armut shows no time. None of the three suggests a next service.
### 3.5 Events are bundles, sold one by one
- Real request text (Armut price-page samples): 17-44% of organization requests mention another service (nişan: tables/chairs 44%, music 19%; birthday: tables/chairs 21%, clown 17%); cake requests 6-8%.
- No site groups services by occasion. The only link is ProntoPro's optional make-up add-on in the wedding-photographer flow; Homerun's "Events" group is photography only.
### 3.6 Size and shape of demand (public estimates)
- Armut: ~108,000 event customers a year (birthday-type ~50,000; nişan, kına and wedding ~32,000; nişan organizasyon 12,918 vs düğün organizasyon 2,026) vs moving 186,667.
- Wedding photographer requests: ~0.5% of marriages in TR (2,947 of ~552,000) vs ~1.8% in IT (3,321 of ~180,000). Italy also shows large event services: catering 19,300, DJ 5,717 vs moving 7,832.
- Requests are mostly small and near-date in both markets: civil ceremonies, takı töreni, kına, "Mi sposerò questo venerdì!", 0-6 hours; some long-lead planners too.
- 0 of 315 sample cleaning, moving and furniture requests mention an event, so pushing events to core customers is weak; 37% of table-rental and 52% of yacht-rental samples are events.
### 3.7 Supply and channel
- Supply is not the limit: ~937 wedding photographers listed in Istanbul and ~843 in Milan, roughly 1-2 platform requests each a year (estimate). Pros pay a fee per quote; the platform sees a hire only when the customer selects a quote.
- Event buyers discover vendors on Instagram (strong for boutique cakes, medium for photographers), but Instagram has a trust gap: prepaid albums not delivered, unregistered photographers (Istanbul photographers' chamber, Milliyet 2026-03-23).

## 4. Problem
Event services are invisible on our own surfaces, and they are sold one by one while customers think in occasions. Hypothesis: the low event share in Turkey (vs Italy) comes from low reach, not low need; the test and search data will confirm or reject it.
How might we let someone planning an occasion see everything they need in one place, without changing the request flow?

## 5. Options considered
Rated with the review panel (impact, confidence, effort, fit, risk; /25). The after-request card scores higher, but it only reaches people who already made a request. The occasion entry is the only option that reaches new event demand, so it is the main bet and the card runs alongside it.
| Option | Score | Note |
|---|---|---|
| After-request "what happens next" + next-service card | 22 | Fast companion; gives co-need data |
| Occasion entry + grouped occasion page + search block | 21 | Chosen main bet (biggest lever on discovery and bundles) |
| Campaign headline copy test | 20 | Cheap side test |
| Price/local SEO page upgrade | 19 | Next step for search traffic |
| Birthday reminder | 18 | Slow payoff, consent |
| Trust card + review dates | 17 | Needs legal sign-off |
| Abandoned-request recovery | 16 | Few users reachable |
| "Found on Armut/ProntoPro" creator program | 12 | Off-site channel, later with marketing |
| Listing badge, WhatsApp concierge | 12 | Dropped |
Dropped earlier: price or pro work before the request, optional free text, changing the "when" default (all touch the shared flow); event messages to cleaning/moving customers (no signal).

## 6. Solution: the occasion entry
### 6.1 What it is
- Entry points, covering all three journeys from the brief: homepage occasion tiles ("Evleniyor musun?", "Nişan / kına", "Doğum günü"; IT "Ti sposi?", "Compleanno"; UK "Getting married?", "Birthday") and an "Özel günler" block in the search suggestions (homepage search); a "Bu gün için diğer hizmetler" block on event campaign service pages and local listing pages, linking to the same occasion page; and a link from the after-request screen.
- Each opens an occasion page that groups the services for that occasion (venue, organization, photographer, make-up, cake, tables/chairs, music, bridal car). Each card shows the price range and number of pros the site already shows, and has its own "Teklif al" that opens that service's existing request flow. Services already requested show "Talep edildi".
- No basket and no "request all" button: each service has its own quotes, pros and timing, and pros pay per quote.
### 6.2 Inspiration and benchmarks
- Grocery "everything for one dinner": Getir's ready basket and AI shopping list, Migros "Ne pişirsem?", Instacart shoppable recipes. Lesson: start from the goal and show everything on one page; do not copy the single basket.
- Services: Thumbtack Events groups party services by theme with average prices; Düğün.com shows "everything for your wedding" with category counts; The Knot and Bridebook group wedding categories with a quote per supplier. None has a "request all" button.
### 6.3 Design options (wireframe/occasion-hub-designs.html)
- A. Grouped occasion page (recommended): sections, one card and one CTA per service.
- B. Checklist ticks ("İhtiyacım var", closest to Getir): later variant; three ticks mean three full request flows.
- C. Timeline ("what to book when"): later variant for long-lead weddings; most real requests are near-date.
### 6.4 Why first
- Fixes the biggest observed gap (discovery) and matches how events are bought (bundles).
- No change to the request flow or pricing; one build for all markets.
- Effort: frontend 1-2 weeks, UX 1 week, backend configuration and tracking.
- The after-request card runs alongside as the fast companion and feeds real co-need data into the order of services on the page.

## 7. What I need to know and how I would get it
- Event funnel by entry point and market (visit, start, submit, quote, hire): product analytics.
- How often event words are searched and what follows: search logs, Search Console.
- Co-need across all requests: request data, then the after-request card itself.
- Share of event requests with 0 quotes in 48 hours, by city: marketplace data; decides where to launch.
- Seasonality: requests by month, so tests run before peak.
- Why event buyers choose Instagram or leave: 8-10 short customer interviews.
- Whether event pros want more requests at the current fee: pro survey and quote rates.

## 8. Test and success
- Where: Istanbul, Ankara, İzmir and one Italian city, only where pros answer within 48 hours; before wedding season (Feb-Apr).
- Arms: control / homepage tile -> occasion page / tile -> search block.
- Primary: submitted event requests per exposed visitor.
- Quality: event requests with at least one quote within 48 hours (volume without quotes is not a win).
- Guardrail: total requests per visitor (the tile must not just move clicks from core services); a long-term holdout then measures the real cost to core.
- Diagnostic only: tile and card clicks, share of visitors sending 2+ event requests in 30 days.
- Kill rule: stop in a city if the 0-quote share on new event requests goes above control + 5 percentage points.
- Duration: 4 weeks, or until each arm reaches the sample needed to see a +20% lift (assumed event-submit baseline ~0.3% of homepage visitors; to be replaced by real data).
- Sizing, not forecast: in the order of 1-2 thousand extra event requests a year per market from this layer; the test decides.

## 9. Risks and next steps
- Homepage space vs core services: guardrail and holdout.
- Weak requests cost pros: quote-based north star, supply-gated cities.
- Buyers who start on Instagram: next, a "found on Armut/ProntoPro" creator pilot that links to the occasion page (labelled #reklam/#işbirliği).
- Then: SEO price and local pages, campaign copy test, trust card.
- Assumptions to validate: low reach (not low need) explains the TR gap; co-need holds beyond my samples; supply absorbs more requests.

## Appendix: platform evidence
Request IDs from the three sites were consecutive (Armut 57338138, ProntoPro 57338238, Homerun 57338294) and one account was recognized on all three. Inference: shared job system and accounts; to confirm with the team.
