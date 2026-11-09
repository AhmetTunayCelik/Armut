# Case study answers (platform-wide: Armut TR, ProntoPro IT, Homerun UK), draft 2026-11-08
Drafted by the Product Lead agent from all handoffs; numbers are public-page estimates. Evidence: handoffs 01, 15, 19, 28, 31, 32.

## (1) Most important opportunities and problems
- Users can't find event services. Armut's homepage lists 36 services and none is an event service; search suggestions show none either. ProntoPro shows one (wedding photographer, in trending); Homerun shows none. Typed search works, but only if the user already knows the service name.
- Events are bought as bundles, but the product sells them one at a time. 17-44% of organization requests mention a second need (tables/chairs, palyaço, music); cake requests 6-8%. No market groups services by occasion; only ProntoPro has an in-flow make-up add-on.
- The moment after a request is wasted. ProntoPro and Homerun promise quotes "within a few hours"; Armut gives no time. None of the three suggests a next service, though the customer has just told us about the event.
- Campaign and local pages don't build trust: one CTA, no pro work, masked reviews; listings show stale (2015-2017) and off-topic profiles on all three sites. This matters more for events, because buyers come from Instagram where they see portfolios, and Instagram has a trust gap (prepaid albums not delivered, unregistered photographers).
- Event demand is small but real. TR ~108k event customers/yr vs moving 186,667; wedding photographer ~0.5% of marriages in TR vs ~1.8% in IT (3,321 of ~180k). That points to low reach in TR, not low need.
- Many requests are small and near-date (civil ceremony, takı töreni, kına, "Mi sposerò questo venerdì"), so the shared "within three weeks" default fits them; long-lead planners exist too.

## (2) Extra information and how to get it
- Event funnel by entry point (visit, start, step drop-off, submit, quote, hire), split by market: product analytics.
- How often event terms are typed, misspelled or end with no click: internal search logs, Google Search Console.
- Co-need rate across all requests, not my sample: request text, and the post-submit card itself.
- Share of event requests with 0 quotes in 48h by city: marketplace data; decides where we can safely add demand.
- Seasonality, so tests run before peak: request history by month.
- Why event buyers leave or choose Instagram: 8-10 short interviews with recent requesters and drop-offs.
- Whether event pros want more requests at the current per-quote fee: pro survey and quote-rate data.

## (3) Which first and why
Main bet: an occasion entry ("Evleniyor musun?" / "Ti sposi?" / "Getting married?") opening a grouped occasion page; each service goes into its own existing request flow; plus an occasion block in search suggestions. It fixes the biggest problem (users can't find event services), fits how events are bought (bundles), and doesn't touch the shared flow or pricing.
First and fastest test: a post-submit "what happens next" message plus a 2-row next-service card. Small (1 FE + UX in days), closes a gap the benchmarks already closed, and gives real co-need data to choose the services on the occasion page.

## (4) What I'd change or test first
- Test A (weeks 1-2): after an event request, show the expected quote time (real median if known), the cancel link, and 2 related services for the same occasion, each opening its own existing flow (city/date prefilled only if the flow supports it).
- Test B (main): occasion card on the homepage and in search suggestions, leading to a grouped wedding/nişan page in TR; then replicate in one IT market.
- Only in cities where pros answer within 48h (Istanbul first); before peak season.
- Next: price/local SEO page upgrade, then a campaign headline copy test.

## (5) How I'd measure success
- Primary: submitted event requests per exposed user, test vs control.
- North star: event requests with 1+ quote in 48h. Volume without quotes is not a win.
- Guardrail: total requests per visitor (event cards must not pull users away from core services).
- Kill rule: stop or narrow if the 0-quote share of event requests rises above control.
- Long-term holdout for the real effect on core services and pro quote spend.
- Win = more event requests per exposed user, no drop in total requests, quote coverage held. Test A also: share who click a next service and submit.

## Solution suggestions (ranked; simulated judge scores /25 in handoff 31)
1. Post-submit "what happens next" + next-service card (22): fastest, low risk, gives data for everything else.
2. Occasion entry + grouped page + search block (21): biggest lever on discovery and bundles, no flow change.
3. Campaign headline copy test (20): cheap; shared template makes it reusable across markets.
4. Price/local SEO page upgrade (19): fresh pros and real work on high-intent search pages.
5. Birthday reminder (18): birthdays repeat yearly.
6. Trust card + review recency (17): answers the Instagram trust gap; needs legal sign-off.
7. Abandoned start recovery (16): helps, not event-specific.
8. Creator program "found this customer on Armut/ProntoPro" (12): reaches buyers where they discover; pilot later with marketing.
9. Listing badge, WhatsApp concierge (12): low score, high ops cost.

## Key assumptions and how I'd validate
- Low TR event share is a reach problem, not low need (0.5% vs 1.8%): search logs, homepage-to-event funnel.
- The 17-44% co-need holds beyond my sample: Test A click and submit rates.
- Supply can absorb more requests: 0-quote share by city, pro survey.
- Showing quote time increases trust and lowers cancels: A/B on cancels and quote acceptance.
- Instagram-first buyers will use a marketplace if trust is shown: interviews, trust card test.
