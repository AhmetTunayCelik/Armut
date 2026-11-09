# 14 Brainstorm: agents talking, 2026-11-07
Hired: Growth/CRM Marketer, Supply and Marketplace Ops, Event Industry Expert, Engineer, Customer Panel (simulated). See agents-and-roles.md.
Round 1: Growth, Supply, Event Expert, UX each proposed 8 ideas (32). Round 2: Engineer (effort, shared-flow risk), Product Analyst (metric tree), Critic (constraints, law), Customer Panel (simulated reactions). Product Lead converged.

## New facts surfaced
- Pros pay a non-refundable fee per quote from a prepaid wallet; fee depends on job size, location, timing, profile, competition (Armut replies on Şikayetvar, 2025-07-14 and 2025-12-27; one pro reported 800 TL for one quote). https://www.sikayetvar.com/armut/teklif-verdigim-musteriler-ulasilmiyor-kesilen-ucretin-iadesini-talep-ediyorum
- Peak nikah day 06.06.2026: one Istanbul hall had 56 couples vs ~20 normal (DHA). https://www.dha.com.tr/gundem/istanbulda-nikah-salonlarinda-06-06-2026-yogunlugu-2886514
- Armut already lists masa sandalye kiralama, sünnet organizasyonu, kız isteme makyajı, evlilik teklifi fotoğraf çekimi (Fact, armut.com pages).
- İYS (Law 6563): commercial messages need prior opt-in; in-session cards do not. Whether a post-submit card counts as commercial: confirm with legal (Assumption).

## Where the agents disagreed
- WhatsApp share of quotes (G5): panel liked it most (families decide together, simulated); Critic dropped it (hire not volume, pro data in a link, pushes deals off Armut). Decision: roadmap, with a privacy-safe version (share a link to "get your own quotes", no pro data).
- Pro quote template (S1): panel and Supply liked it (comparable quotes, trust); Critic and Analyst: pro composer is shared and it lifts hire, not volume. Decision: roadmap, an enabler.
- "Küçük tören, yarın bile" copy: fits the 7-day median, but the pro persona and Zeynep persona find it cheap or low-intent (simulated). Decision: keep in the copy test with a lead-quality guardrail.
- Countdown "photographers book 3-6 months ahead" (U5): dropped, contradicts our own data.

## Converged shortlist
| # | Idea | Problem | Effort (eng-weeks BE/FE) | Primary metric |
|---|---|---|---|---|
| 1 | "Next for your party/wedding" card (approved), plus keyword trigger from core free text, in-session only. Cake first | Awareness, volume | 1.5/0.5 + card | Event requests within 14 days per exposed submitter |
| 2 | "Misafir gelmeden önce": hosting card and landing from cleaning, koltuk yıkama, masa sandalye to cake, kız isteme makyajı, organization | Awareness (enters through trusted service) | 0.25/1 + card | Event requests per 1,000 core submitters |
| 3 | Event price pages upgrade: occasion links, small-nikah section, aggregated real-demand proof (no copied free text), sticky CTA | Awareness, trust | 0.5/1.5 | Price page to request start, then submit |
| 4 | Copy angle test on campaign pages and pushes: awareness vs trust vs speed | Find the real barrier | 0/0.5 | CTR to start and submit per angle |
| 5 | Recover abandoned event starts (app push or consented users) | Volume | 1/0.5 | Recovered submits / abandoned starts |
Pre-check before any demand push (Analyst): share of near-date (<7 days) event requests with 3+ quotes within 24h, by service and city. Launch only in cells that pass; elsewhere first run the peak-date supply alert (E3).
Keyword detection (Engineer): Turkish lowercasing then ASCII folding, prefix roots (dugun, nikah, nisan, kina, soz, kiz iste, dogum gunu, mezuniyet), edit distance 1 for 5+ letters, exclusions (nisantasi). Rules first, 90%+ precision on ~500 labeled texts before go-live.
Tagging (Engineer): use a short redirect armut.com/q/<code> that sets utm and a cookie, then opens the existing flow. No flow change. Prefill of city and date: unknown; if not supported, ask the date in the card instead.

## Roadmap
Offline QR pilot (kuyumcu, gelinlik, venues via pros, belediye nikah office), life-moment campaigns (karne, mezuniyet, evlilik teklifi sequence), pro quote template, near-date routing, SEO per nikah salonu, privacy-safe family share, broad-audience campaigns to mothers for kına (no inferred family data).
## Dropped
Intent signals to pros before paying (changes what the fee buys, all categories), event pro teams (too big), higher quoting bar (shrinks supply), imported unverified reviews (legal), occasion block in search (shared), countdown with 3-6 months claim, event fit line on quote cards (shared, hire only).

## Metric tree (Analyst)
Event requests per month = organic base + cross-sell (submitters x trigger share x card view x CTR x submit) + owned pages (sessions x start x submit) + CRM/paid (audience x reach x click x start x submit) + offline (scans x start x submit) + recovery (abandoned x return x submit).
Biggest unknowns: keyword-hit share in core free text (measurable for free on history), card CTR, consented reach.
Illustration only, not a forecast: 279,434 core requesters x 2% hit x 30% CTR x 40% submit = about 670 event requests a year.
Guardrails across all: quotes per request, time to first quote, share with 0 quotes, Teklifi Seç rate, pro complaints about event leads, opt-outs, core hire rate.
Hire-only ideas (off-goal unless used as enablers): quote template, routing, galleries, ranking, Teklifi Seç reminder, photo reviews.

## Questions for Armut staff (interview or first week)
1. Event funnel by category: landing, start, submit, 1+ quote, Teklifi Seç. How much hiring is off-platform?
2. Are success page, quote view, search, listing templates shared code, or per-category flags?
3. Share of event customers with İYS consent; share of event requests with a quote within 24h.
## Real interviews (from the simulated panel; validate before building)
Couple: how did you find and pick your last vendor? What did you need to see before messaging one? Parent: after booking the cake, what else did you still need? Mother of the bride: who had a say, how did you share options? Pro: of the event quotes you paid for last month, how many became jobs? What would you put in a package template?
