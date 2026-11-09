# 05 First change, test and metrics (Product Lead + Product Analyst), 2026-11-07
Gates passed: G1 problem statement accepted, G2 pick accepted (Bulent, 2026-11-07): lead O2, pair O1, guardrail O8.

## The first change
**O2: show price and work before the request.** On the wedding photographer campaign page (/d/dugun-fotografcisi/194) and the Istanbul local listing, add one block above the "Basla" button:
1. Typical price range for this city and service, from Armut's own recent quotes (Assumption: this data exists and is clean; confirm with the data team).
2. 3-4 sample work cards from active, reviewed pros (cover photo, first name, rating, review count).
3. One line on what happens next: answer a few questions, get up to 4 quotes, no obligation (check wording against current terms).
4. Same CTA, now with context ("Get quotes for your wedding").

**O1 (pair): event date question.** In the request flow for wedding photographer, replace the "within three weeks" default with an event-date picker plus the existing options. No default selected.

Out of scope for now: homepage tile (O3), multi-service request (O5), listing cleanup (O4).

## Why this and not more
- Targets the strongest needs found: trust in real work, price clarity, comparing a few (T1, T3, T5). All are hypotheses until interviews and funnel data.
- Small enough for 1 frontend, 1 designer, 1 backend: a content block, a price query, a date field.
- One category and one city first, so a failed test is cheap.

## Test design
- Cheapest first (a few days, no build): hand-pick 12 Istanbul pros with good galleries and reviews, take the price range from the last 90 days of Istanbul quotes, ship a static block. Needs pro consent to show their work (Risk).
- Then A/B on page: 50/50 split of sessions on the campaign page and Istanbul listing. Control = current page. Variant A = block (O2). Variant B = block + date question (O1+O2). Date question only touches people who enter the flow, so judge it on step completion, not page traffic.
- Unit: session landing on the page. Run through at least two full weekly cycles.
- Sample size rule of thumb, per arm n ~ 16 x p x (1-p) / d^2 (80% power, 5% significance, d = absolute lift). Illustration only, not a forecast: if baseline were 5% and we want to detect 1 point, n is about 7,600 sessions per arm. Real baseline is Unknown; get it first (data wish list H2).
- Seasonality: winter is below the July-September wedding peak, so compare only within the same weeks, and expect slow traffic. If traffic is too low, extend duration or add more cities rather than reading early.
- Stop rules: stop early if guardrails break (below).

## Metrics
Primary: submitted requests per 100 page sessions, wedding photographer, Istanbul.
Supporting (diagnostic): click-through to "Basla"; request start to submit completion; completion at the "when" step; share of requests with an event date.
Guardrails (must not get worse):
- Quotes per request and time to first quote (lead quality, O8).
- Pro-side: lead-purchase rate and pro complaints about event leads.
- Share of quotes landing far outside the shown price range (range is honest).
- Page speed; requests in other categories unaffected.
- Non-event traffic is not affected (flag off outside the test pages).
Win (proposal, Bulent to confirm): primary up with statistical significance and a lower confidence bound above zero, guardrails not worse beyond an agreed tolerance (to set with the data team, no number invented here).
Longer-term (not in test window): repeat requests per couple (photographer plus makeup, cake), request-to-hire rate if data exists.

## Risks
- Price range anchors customers low, or pros object to a public range. Mitigation: show a range, not a price; start with Istanbul where range can be checked.
- Showing pro work needs consent and quality control; audit found masked reviews ("xxxx"), so ratings may need a fix first.
- Few event requests today means low power. Mitigation: longer window or more cities.
- More requests but weaker leads. Mitigation: guardrails above.

## Open assumptions to confirm
Price data exists by city and service; pros consent to showing work; baseline conversion known; analytics events exist per step. Evidence: data wish list (06) and 5-8 couple interviews (A1-A3 in 03).
