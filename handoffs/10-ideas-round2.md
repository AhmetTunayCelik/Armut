# 10 Ideas round 2 (agents + critic), 2026-11-07
Inputs: 3 research agents (marketplace tactics, Turkey campaigns and partners, Turkish event life cycle), first-hand Armut price pages (09), critic review.
Constraints (Bulent): no change to the shared request flow; no change to range-then-pro-prices; event categories only or CRM/marketing/merchandising/partner/supply layers; 1 BE, 1 FE, 1 UX; measurable in weeks.

## Reframe from the evidence
Armut's event demand today is short-notice and small: nikah, takı töreni, kına, gelin alma, small birthday cakes (09). One wedding or birthday is several services, but Armut groups them by service type, and after submit the customer sees nothing else. Birthdays repeat every year. So the cheapest growth is more requests from people already here, not turning Armut into a wedding planner (Düğün.com's game).

## Shortlist (after critic)
| ID | Idea | Constraint fit | Effort | Verdict |
|---|---|---|---|---|
| F2 | Same-event cross-sell on success page, tracker, follow-up email. Cake to decoration, balloons, organization, photographer. Photographer to kına, nikah, organization, make-up. One tap into each existing flow | Event-only module after submit, no flow change | S-M | LEAD |
| F1 | Birthday comeback: about 11 months after a birthday cake, organization or photographer request, a reminder 2-3 weeks before the date | CRM only | S | PARALLEL |
| F4 | Seasonal event slot in homepage and app lists | Merchandising | S | LATER (Feb-Mar, total requests as primary) |
| F6 | Faster pro notification for near-date event requests | Supply layer; quote form change would break constraint 1 | M | DEPRIORITIZE (hire rate, not volume) |
| F5 | Event-type hub pages (nişan, kına, sünnet, 1 yaş) | SEO layer | M | ROADMAP (SEO takes months) |
| F3 | Ministry "Evlenecek Gençler" e-Devlet code partnership | Partnership | BD months; who funds discount is open | ROADMAP |

## Lead: F2 detail
- Why: largest reach (every event requester), readout in days, cheap, event-only. Evidence: services split across 3 groups (audit, Fact); bundles in birthdays (2019 Armut data: venue, decoration, figurative cake top add-ons) and weddings (kına+düğün request, Fact n=1); Add to Event and Bridebook show next-supplier patterns (Fact); no published lift from any marketplace (Gap).
- Order: start with birthday cake (same day, same party, highest volume), then wedding photographer.
- Timing fix (critic): make-up books ~3 weeks out, photographer ~1 week, so photographer to make-up may come too late. Prefer same-day pairs.
- Test: randomize by user 50/50 among event-request submitters. Primary: extra event requests per submitter within 7 days. Guardrails: hire rate and quotes per request on cross-sold vs organic requests, pro complaints, unsubscribes.
- Open: carry date and city into the next flow (prefill) is Unknown; without it effort is S, with it M.

## Parallel: F1 detail
- Backtest now: requesters from Dec 2025 to Jan 2026 get the reminder this Dec-Jan, 20% holdout. Primary: event requests within 30 days per reminded user.
- Risks: request date is not the birthday (send 2-3 weeks early); İYS consent needed for SMS/email; push reaches app users only (~40% of requests per Para Dergi 2026-10-07).

## Weak claims to keep labeled
7-day median from 13 published examples (Assumption). 2019 volumes are order of magnitude only. "Pros pay per lead" vs per quote sent: confirm. Homepage check was logged-out web only. Who funds the November 15% discount: unknown.
