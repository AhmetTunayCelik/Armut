# 06 Data wish list (Insight Analyst + Product Analyst), as of 2026-11-07
Hypotheses are from handoffs/01-journey-audit.md. Nothing here is measured yet.

| Hypothesis | Data needed | Source | How to get it | Cheap proxy |
|---|---|---|---|---|
| H1 event services invisible on homepage | Logged-out homepage sessions by search term and tile; event click-through | Web analytics | Funnel: homepage view, search or tile click, category | Search "dugun fotografcisi" logged out; count taps to a result |
| H2 request before price or work | Page-to-request-start rate, scroll depth, clicks on price or profile | Analytics, heatmaps | Compare event pages vs a home-service page | Recordings of 20 event-page visits |
| H3 listing cluttered by old profiles | Share of listed profiles active (reply within 7 days, review in 12 months) | Supply database | Query per city and category | Manually audit top 20 on the Istanbul listing |
| H4 mandatory free text, no event date field | Step drop-off; share of requests with an event date; free-text length | Request-flow events | Step funnel by category | Walk the flow on 3 devices and time it |
| H5 related services not linked | Share of customers requesting 2+ event services in 90 days | Request DB by user | Cohort query: photographer plus makeup or cake | Ask in interviews what else they hired |
| H6 seasonality | Weekly requests by event category over 2-3 years; lead time to event | Request DB | Weekly time series | Google Trends by month |
| H7 "within three weeks" default | Share choosing each "when" option in event categories | Request-flow events | Option distribution by category | Compare answer mix vs weddings booked months ahead |
| H8 location step effort | Time and drop-off at location step; autofill share | Step events | Median time per step | 5 users on mobile |

Also pull (tests T4): quotes per request and response time by category, win rate and reviews per event provider, provider churn.
Live check: our 3 test requests (Armut 57338138, ProntoPro 57338238, Homerun 57338294): count quotes, response time, price after 24h.
