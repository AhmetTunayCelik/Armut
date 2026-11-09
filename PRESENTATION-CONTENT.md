# Presentation content (max 15 slides), built on Solution 2: occasion entry
Status: content only; the deck is the last step. One headline + at most one key number per slide. Sources in handoffs.

1. Title. "Making events visible: an occasion entry for Armut / ProntoPro." Bulent Çelik, APM case study, Nov 2026.

2. How I worked (brief). Walked all 3 entry points on Armut, ProntoPro and Homerun and sent real wedding-photographer requests (2 real quotes back). Pulled public data from the three sites (price pages, pro pages). Worked with Claude as an agent team: researchers, event and supply experts, engineer, analyst, UX, a fact checker, a red-team critic and a simulated judging panel (Head of Product, ProntoPro Growth PM, Analytics, Design) that scored the case 4 times (68 -> 79/100). I set the direction and constraints; agents researched and challenged. One line: time went above the 2-3 h guide on verification; transcript shared.

3. The goal and the constraint. Grow event requests; team 1 BE, 1 FE, 1 UX; no change to the shared request flow or pricing, so solutions are layers on top.

4. What I noticed: homepage search. No event service in Armut's homepage lists or search suggestions; ProntoPro shows one service in trending; Homerun none. Typed search works ("kına" -> Kına Organizasyon, Kına Mekanları). Key line: people can find events only if they already know Armut has them.

5. What I noticed: campaign page and local listing. One CTA, no pro work, masked reviews; stale (2015-2017) and off-topic profiles on all three sites. Key line: trust is thin exactly where Instagram is strong.

6. What I noticed: events are bundles, sold one by one. 17-44% of organization requests mention another service (tables/chairs, clown, music); no market groups an occasion; after a request nothing suggests the next service. Key number: 44% of nişan requests also mention tables/chairs (sample).

7. The size of the gap. Wedding photographer requests ~0.5% of marriages in TR vs ~1.8% in IT (public estimates); events are small, home-hosted and often near-date (civil ceremony, kına, "Mi sposerò questo venerdì!"). Key line: low reach, not low need.

8. Problem statement. "Event services are invisible on our own surfaces, and they are sold one by one while customers think in occasions." How might we let someone planning an occasion see everything they need in one place, without changing the request flow?

9. Benchmarks. Getir/Migros/Instacart recipes (everything for one dinner on one page); Thumbtack /events (services grouped by occasion, average prices); Düğün.com (everything for the wedding, firm counts, no fee for couples). Lesson: copy the page, not the basket; no service example has a "request all" button. Screenshots: screenshots/benchmarks.

10. The solution: occasion entry. Homepage tiles ("Evleniyor musun? / Nişan-kına / Doğum günü"; IT "Ti sposi?"; UK "Getting married?"), an occasion block in search suggestions, and a link from the after-request screen. Each opens an occasion page.

11. Wireframe: the occasion page (Option A). Grouped cards with price range and pro count, one "Teklif al" per service into its existing flow, "Talep edildi" state. Options B (checklist ticks) and C (timeline) as later variants, with why not now. Source: wireframe/occasion-hub-designs.html.

12. Why this first. Fixes the biggest gap (discovery), matches how events are bought, no flow or pricing change, one build for all markets (shared platform), 1-2 weeks FE + 1 week UX. Alternatives ranked lower (after-request card as the fast companion; SEO pages next; creator program later).

13. What I need to know and how. Event funnel by entry point and market; search logs for event words; co-need across all requests; 0-quote share in 48h by city; seasonality; 8-10 customer interviews; pro survey.

14. Test and success. TR (İstanbul, Ankara, İzmir) + one IT city, pre-season. Arms: control / tile -> occasion page / tile -> search block. Primary: submitted event requests per exposed visitor. North star: event requests with 1+ quote in 48h. Also: share with 2+ event requests in 30 days. Guardrail: total requests per visitor. Kill rule: 0-quote share rises. Holdout for core cost.

15. Risks and next steps. Homepage space vs core (guardrail + holdout); weak requests cost pros (quote-based north star); Instagram-first buyers (next: "found on Armut/ProntoPro" creator pilot that links to the occasion page); after-request card; SEO pages. Appendix: assumptions, data, AI transcript.
