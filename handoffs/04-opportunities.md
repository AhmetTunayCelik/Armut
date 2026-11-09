# 04 Problems and opportunities (Product Lead + Product Analyst), 2026-11-07
Scores are judgment, 1-5. Score = Impact x Confidence / Effort. No reach data, so RICE is not possible. Confidence is low everywhere until the data wish list (06) is answered. Effort assumes the team: 1 backend, 1 frontend, 1 UX.

## Problem statement (for gate G1)
Couples plan weddings weeks or months ahead and want to judge a vendor's work and price before they commit. Armut's event journey is built like an urgent home-service request: event services are not visible on the homepage, the campaign page asks for a request before showing price or work, and the request flow assumes "within three weeks". So fewer couples start a request, and some who start leave.
How might we help a couple go from "I need a wedding photographer" to a sent request with confidence in price and quality, at the time they actually plan?

Evidence base: handoffs 01 (walked 3 flows, Fact), 02 and 03 (research, mostly indirect and dated). No Armut funnel data (Assumption).

## Scored list
| ID | Problem / opportunity | Source | Impact | Conf. | Effort | Score |
|---|---|---|---|---|---|---|
| O1 | "When" step defaults to within three weeks; no event date. Fix: event-date question or sensible default for event categories | H7, H4 | 3 | 2 | 1 | 6.0 |
| O3 | Event services missing from homepage trending and popular lists. Fix: seasonal wedding/event tile | H1 | 4 | 3 | 2 | 6.0 |
| O2 | Campaign and local pages show no price and no work before "Basla". Fix: price range and sample work/reviews on the page | H2, T1, T3, T5 | 4 | 3 | 3 | 4.0 |
| O6 | Mandatory free-text step in the flow. Fix: make optional or add chips | H4 | 3 | 2 | 2 | 3.0 |
| O4 | Local list has old, off-topic, placeholder profiles. Fix: ranking/cleanup | H3 | 3 | 2 | 3 | 2.0 |
| O8 | Providers doubt lead quality (risk to supply and quote speed) | T4 | 4 | 2 | 4 | 2.0 |
| O5 | Event services split across groups, no multi-service wedding request | H5, A1 | 4 | 2 | 5 | 1.6 |
| O9 | Delivery and trust assurance (vetting, deposit) | T1, T2 | 3 | 2 | 4 | 1.5 |
| O7 | Three-level location step adds effort | H8 | 2 | 2 | 3 | 1.3 |

## Why the order is not just the score
- O1 and O3 score highest because they are cheap. But O1 helps only people already in the flow, and O3's impact depends on how many event requests come from the homepage versus search (unknown; ask for data).
- O2 addresses the strongest customer needs found (trust in real work, price clarity, comparing a few vendors) and matches how the benchmark (The Knot) works. It costs more and needs real provider content.
- O8 is a guardrail on everything: more requests must not mean worse leads.
- O5 is the big bet but needs the most build and the weakest evidence. Park for next steps.

## Suggested pick for gate G2 (Bulent decides)
Lead opportunity: O2 (show price and work before the request). Pair it with O1 as a low-cost second change if the test allows. Keep O8 as a guardrail metric.
What would change this pick: funnel data showing most drop-off at the "when" step (then O1 first), or showing homepage is the main event entry (then O3 first).

## REVISION 2026-11-07 (Bulent)
Constraint from Bulent: Armut deliberately shows a price range and leaves the exact price to the pro. Changing that (O2) or the shared request structure (O6, and anything that affects non-event requests) is out. Ideas must work for event services only and not change Armut's overall structure. The slide deck is paused until ideas are final.
Dropped: O2, O6. Under question: O1 and O7 (check if the event-category flow can differ without touching the shared structure).
New idea list with scores: see handoffs/08-event-only-ideas.md.
