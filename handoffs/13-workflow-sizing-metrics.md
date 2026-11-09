# 13 Workflow after the quote, sizing, new ideas, metric tree, 2026-11-07

## How Armut works after the request (Fact, https://info.armut.com/nasil-calisir, checked 2026-11-07)
1. Customer answers short questions (can keep contact details hidden).
2. Up to 5 quotes, depending on job type. Each quote: price, real reviews, contact info, a message written for the job. Armut says it gets 110,000+ requests a month (page date unknown).
3. Customer asks questions, bargains, checks references, and agrees by message or PHONE. To be covered by Armut Garantisi the customer must press "Teklifi Seç".
Inference: the deal often closes off-platform (phone, WhatsApp; our two UK quotes pushed to WhatsApp and calls, 07). Armut only knows the hire if the customer presses "Teklifi Seç". So Armut may not know who was hired, when the event is, or whether the pro cancelled. That makes T2 (event-day backup) weak: Armut cannot trigger a backup it cannot see. Moved to roadmap. Unknown: share of jobs where "Teklifi Seç" is pressed; whether pros pay per quote (credits); what happens when a pro cancels.

## Sizing (Fact, Armut pro sign-up pages armut.com/profesyonel-uye-ol-<id>, "Yılda N ... müşterisi Armut'a ilan veriyor", Türkiye-wide, page date unknown)
| Service | Customers a year |
|---|---|
| Evden eve nakliyat | 186,667 |
| Ev temizliği | 84,391 |
| Doğum günü pastası | 8,963 |
| Mobilya montaj | 8,376 |
| Düğün fotoğrafçısı | 2,947 |
| Çeyiz taşıma | 1,522 |
- Inference: 2,947 wedding photographer customers vs 552,237 marriages in 2025 is about 0.5%. Event demand is tiny next to the market and next to core categories. The problem is awareness, not market size.
- CORRECTION to handoff 11: çeyiz taşıma shows 45,882 reviews but only 1,522 customers a year, so review counts on these pages are likely pooled (pro's whole profile or parent category). Treat all ratings and review counts as "shown on page, scope unknown". The çeyiz bridge is real but small (~1,500 a year); birthday cake (~9,000) is the largest event service.

## New ideas
| ID | Idea | Problem | Effort |
|---|---|---|---|
| N1 | "Did you pick your pro?" reminder for event requests before the event date: press Teklifi Seç to be covered by Armut Garantisi. Gives Armut the hire and the date | Trust + measurement | S |
| N2 | Post-event review with 1-3 photos, sent after the event date (needs N1 or a date in free text) | Trust (real work) | S-M |
| N3 | Pro referral link: event pros send their own Instagram leads into an Armut request (pros have spare capacity: e.g. 937 Istanbul wedding photographers listed vs ~2,947 requests a year nationwide) | Awareness | S-M |
| N4 | Start "Next for your..." card with birthday cake (largest event service) then wedding and çeyiz | Volume | S (re-order of approved idea) |
| N5 | Bridge from mobilya montaj and moving only when free text mentions çeyiz, düğün, evlilik (keyword trigger). Sample of 21 moving requests had none, so low priority | Awareness | M |

## Metric tree
North star: submitted event requests per month (by service, city).
= new event requesters (awareness) + extra requests from existing customers (cross-sell, repeat).
- Awareness: event share of all requests; event searches and event surface clicks per 1,000 active users; requests from new-to-event users.
- Card (approved first change): impression > click > request start > submit, per entry point; primary = event requests within 14 days per submitter, vs 50/50 holdout.
- Repeat: share of birthday requesters who request again 11-13 months later.
- Penetration benchmark: wedding photographer customers / marriages (now ~0.5%).
Guardrails: quotes per request and time to first quote on card-driven vs organic requests; pro quote rate on those requests; Teklifi Seç rate; review rate and rating; core-category request rate on the same success pages; İYS opt-outs.
Health metrics enabled by N1/N2: share of event requests with a known hire and event date; reviews with photos per month.
Sizing illustration (not a forecast): if 5% of ~9,000 cake requesters sent one more event request, that is ~450 a year, about +15% on wedding photographer volume. Real rates unknown.
