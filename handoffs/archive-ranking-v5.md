# Solutions ranking for Bulent (v5), 2026-11-07
Goal: more event requests on Armut. Constraints: no change to the shared request flow or pricing; event-only or layers on top; 1 BE + 1 FE + 1 UX; testable in weeks.

## The story in four lines
1. Armut already has ~108,000 event customers a year (Armut's own pro pages), mostly small and home-hosted: birthday-type 50,070, nişan/kına/wedding chain incl. venues 32,427, plus ~7,100 events hidden in yacht and boat rental. Nişan organizasyon (12,918) is 6x düğün organizasyon (2,026).
2. Supply is not the problem: Istanbul lists 937 wedding photographers for roughly 1-2 Armut requests each a year. Demand is: wedding photographer customers are ~0.5% of 552,237 marriages.
3. Search works for event words (kına, kız isteme, 1 yaş, baby shower tested live), but nothing on the homepage or the search empty state tells people Armut does events, and nothing after a request shows the next service. People do not write event words in cleaning or moving requests (0 of 315), so the bridge is from event-adjacent services (masa sandalye 37%, yat 52%, tekne 33% are events).
4. So: put events where new users look (discovery), show the next service to people already planning (card), and make price pages convert. Measure everything against holdouts and protect pros, who pay per quote.

## Each journey in the brief and its fix
| Journey | What I saw | Fix | Idea |
|---|---|---|---|
| Homepage search | 36 listed services, none event; search empty state lists only core services; search itself maps event words well. Sister site ProntoPro already lists wedding photographer in its homepage trending list (audit, handoff 01) | Event services in homepage lists and the search empty state, seasonal rotation; synonym fix (takı töreni -> photographer) | D1 |
| Campaign service page | One "Başla" button, masked reviews | Copy angle test on the headline (awareness vs trust vs speed); price/proof only on price pages (pricing model unchanged) | B3, B1 |
| Local listing page | Stale and off-topic profiles in "En İyi 40" | Price/local page upgrade now; ranking cleanup is roadmap (ranking logic likely shared) | B1 |
| After submit (not in brief, found in walkthrough) | Tracker only, no next step | "Sıradaki ihtiyacın" card | P1 |
| Drop-off in the flow | Sign-up is the last step | Recover logged-in/app abandoners | B2 |

## Ranking
Method: Monte Carlo middle outcome (P50 extra event requests a year) x confidence x testability / (effort x risk), then a Product Lead check. Real volumes, assumed rates: scenarios, not forecasts (handoff 18, assumptions in handoff 21).
| Rank | Idea | Users reached | P50 /yr (P10-P90) | Effort | Reads in | Primary metric |
|---|---|---|---|---|---|---|
| 1 | D1 Event entry in homepage lists + search empty state (new users) | New to events | 1,521 (787-2,604) | ~1 | ~3 weeks (if homepage traffic is large) | Event request starts from users with no past event request, vs holdout; total requests as guardrail |
| 2 | P1 "Sıradaki ihtiyacın" card after organization, palyaço, venue, event-text masa sandalye and yat/tekne requests | Already planning | 1,269 (1,026-1,542) | ~2 + UX | 2-7 weeks | Other event requests within 14 days per submitter, 50/50 |
| 3 | B3 Copy angle test (awareness vs trust vs speed) | Campaign page visitors, CRM | learning test | ~0.5 | 1-2 weeks | Submits per 1,000 by angle; quotes per request as guardrail |
| 4 | B2 Recover abandoned event starts (logged-in/app) | In the flow | 810 (422-1,485) | ~1.5 | <1 week | Recovered submits / eligible abandoners |
| 5 | B1 Event price/local page upgrade (occasion links, aggregated proof, sticky CTA) | Search visitors | 1,233 (642-2,183) year 1 | ~2 | 8-12 weeks, city split | Event requests from these pages, diff-in-diff |
| 6 | C6 WhatsApp concierge pilot | Event page visitors | 2,246 (1,309-3,480), ops-capped | S + ~0.5 FTE ops | 2-week pilot | Cost per added request |
| 7 | C1 Birthday comeback reminder | Past birthday customers | 215 (132-340), every year | ~1 | ~18 weeks | Requests per reminded user vs holdout |
| Appendix | C3 press cost report, C4 office year-end pack, C5 kreş cake | | small or unsized | | | |
| Drop | Keyword trigger from cleaning/moving | | 32 | | | 0 of 315 mention events |

## Recommended set and ambition
D1 + P1 + B2 + C1 + B1: middle scenario ~4,300 extra event requests a year (+4.0% on ~108,000), range 3,300-5,600. Overlaps are discounted 5-30%.
Stretch framing for the deck: wedding photographer from 0.5% to 1% of marriages would add ~2,900 requests a year from that one service. This set is the first, low-risk step; the data from it decides the bigger bets (offline partnerships, Ministry couples programme, SEO per nikah salonu).

## For the deck (simple view, per the hiring-manager review)
Three opportunities: discovery for new users (D1), next service for people already planning (P1), price pages that convert (B1). One pick to test first: D1 + P1 together (one UX sprint, two placements). One metric set: event request starts and submits per user vs holdout; guardrails quotes per request, time to first quote, 0-quote share, Teklifi Seç rate, pro complaints, core requests. Low / mid / high: 3,300 / 4,300 / 5,600 a year. Monte Carlo and the assumption register go to the appendix.

## Guardrails and enablers
Card and message leads must keep hire rate close to organic (proposed band ~80%+, to agree with analytics); card leads are expected to cost pros 0.8-2.3M TL a year in quotes that do not become jobs. Before pushing demand: share of near-date event requests with 3+ quotes in 24h, by service and city. Peak-date pro alerts. Teklifi Seç reminder.

## Roadmap and dropped
Roadmap: listing ranking cleanup for events, offline QR pilot (kuyumcu, gelinlik, venues, belediye), life-moment campaigns, SEO per nikah salonu, privacy-safe family share, Ministry e-Devlet couples code, event-day backup, no-show money-back, pro quote template, near-date routing, app "Bu hafta sonu" rail, Google Business kit for pros.
Dropped: price/work before the request and optional free text (shared structure); intent signals to pros; pro teams; higher quoting bar; imported reviews; search occasion block; tracker countdown; quote-card fit line; keyword trigger from cleaning/moving.

## What you decide
(a) Recommended set as above; (b) D1 + P1 only for the deck story; (c) add C6 WhatsApp pilot if you want a human-trust angle; (d) your own mix.

## Files
Specs, test plans, pre-mortems: handoffs/20. Assumptions: handoffs/21. Reviews: handoffs/22. Evidence: handoffs/09, 11, 13, 15, 19. Ideas: 14, 16. Comparisons: 17. Simulations: 18 and simulation/. Wireframe: wireframe/next-for-your-event-card.html.
