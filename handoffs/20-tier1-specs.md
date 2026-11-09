# 20 Tier 1 specs, test plans and pre-mortems, 2026-11-07
Shared rules: event categories only; no change to the shared request flow or pricing; every test has a holdout; guardrails below apply to all.
Guardrails (all tests): quotes per request, time to first quote, share of requests with 0 quotes, Teklifi Seç rate, pro complaints about event leads, opt-outs, core-category requests on the same screens. Proposed decision band (to agree with Armut analytics, not a fact): card or message leads keep at least ~80% of the organic hire rate.

## 1. P1 "Sıradaki ihtiyacın" card (Next for your party/wedding)
Where: success page after submit, the request tracker, and the existing confirmation email. Event entry services only.
Wave 1 entry points and rows (evidence in handoff 19):
| After this request | Row 1 | Row 2 | Row 3 |
|---|---|---|---|
| Doğum günü organizasyonu | Masa sandalye kiralama | Palyaço / Animatör | Doğum günü fotoğrafçısı |
| Nişan organizasyon | Masa sandalye kiralama | Ses sistemi kiralama | Nişan fotoğrafçısı |
| Palyaço | Balon süsleme | Ses sistemi kiralama | Doğum günü pastası |
| Masa sandalye kiralama, if free text has an event word | Matching organization (nişan/söz or doğum günü) | Catering | (photographer for that event) |
| Yat / tekne kiralama, if free text has an event word (52% / 33% of samples) | Doğum günü pastası or Evlilik teklifi fotoğraf çekimi | Fotoğrafçı for that event | Ses sistemi or Balon süsleme |
| Düğün salonu (planner type, months ahead) | Düğün fotoğrafçısı | Gelin makyajı | Kına organizasyon |
Wave 2: doğum günü pastası, kına organizasyon, düğün fotoğrafçısı (to gelin makyajı, gelin arabası süsleme), çeyiz taşıma (destination city).
Copy (Turkish, draft): header "Etkinliğin için başka neye ihtiyacın var?"; subline "Talebin alındı. Aynı semt için ücretsiz teklif al."; each row: service name, one-line benefit, the price range Armut already shows, rating as shown on the service page (only if review scope is confirmed), button "Teklif al"; footer "Şimdi değil".
Rules: show once per request; hide a row if the user already has an open request in that service; city from the request (çeyiz: destination city); one tap opens the existing flow for that service (prefill only if the flow already supports it; else no prefill).
Events to log: card_view, row_click(service), request_start(source=card), submit(source=card), dismiss.
Test: user-level 50/50 among submitters of wave-1 entry services. Primary: event requests (other services) within 14 days per submitter. Secondary: row CTR by service. Duration: until planned n (formula in handoff 18), at least 2 full weeks.
Decision: ship if primary lift has a lower confidence bound above 0 and guardrails hold. If CTR < ~1%, change rows and copy before scaling; if one row wins, reorder.
Simulated outcome (handoff 18 v4): about 1,270 extra event requests a year (1,030-1,540).
Pre-mortem (how it fails): (a) people already arranged the other services elsewhere, so CTR is low; check with "already have it" dismiss reason. (b) card leads are low intent and pros pay for quotes that never convert; watch hire rate band. (c) the success page is shared code; needs a category flag (ask engineering first). (d) shown rating is pooled and misleading; only show after scope check. (e) cannibalization: people would have searched anyway; the holdout measures this.

## 2. B2 Recover abandoned event starts
Who: users who started an event request, reached step 2 or later, did not submit within 60 minutes, and are logged in or have the app with push allowed. Most web abandoners are anonymous (sign-up is the last step), so reach is limited.
Messages: push after 1 hour: "Talebin yarım kaldı. Birkaç soru daha, sonra ücretsiz teklifler gelsin." Email after 24 hours only with İYS consent. Link opens the same service flow (resume at the step if supported, else from the start).
Test: 80/20 treatment/holdout among eligible abandoners. Primary: submits within 72 hours per eligible abandoner. Guardrails: push opt-outs, quotes per request on recovered requests.
Pre-requisite: step-level events in analytics and a way to know logged-in status at drop-off. If missing, this waits.
Simulated outcome: about 810 a year (422-1,485).
Pre-mortem: (a) too few reachable abandoners; measure count first, free. (b) resume not possible, so users face the whole flow again; expect lower return. (c) push fatigue across categories; cap at one event push a week.

## 3. B3 Copy angle test (learning test)
Question: is the barrier awareness, trust or speed?
Variants on event campaign pages (headline above "Başla") and in one push to a past-customer segment that consented:
- Awareness: "Armut'ta doğum günü ve nişan organizasyonu da var"
- Trust: "[N] değerlendirme, ortalama [rating]" (real numbers only, after scope check)
- Speed: "Hafta sonuna yetişir: hızlı teklif al"
Primary: submits per 1,000 visits or sends. Guardrail: hire rate and quotes per request by variant (speed may bring low-intent requests).
Use: the winning angle becomes the card copy and the CRM copy.
Pre-mortem: (a) too little traffic to separate three variants; run two at a time. (b) one angle wins clicks but loses on hire; decide on submits x hire, not clicks.

## Next builds (Tier 2 specs, short)
B1 Price/local pages: add occasion links (e.g. nişan organizasyon page links masa sandalye, ses sistemi, nişan fotoğrafçısı), a "küçük nikah / evde nişan" section, aggregated proof ("Son 3 ayda [N] talep, ortalama [X] TL", real numbers only, no copied customer text), a sticky "Teklif al" button. Test: randomize cities into two groups, change pages in one group, compare event requests from these pages before and after (difference-in-differences), 8-12 weeks.
C1 Birthday comeback: eligible = birthday-type requesters 10-13 months ago with consent or app push; send at request date + 11 months - 2 weeks; message "[Ay] yine geliyor: geçen yıl buradan pasta/organizasyon bulmuştun"; 20% holdout; read in ~18 weeks; leave running.

## 6-week plan
Week 0: confirm with engineering whether the success page, tracker and email can show category-specific content; confirm step tracking; pull the event funnel (12 months) and the near-date quote check (3+ quotes in 24h by service and city).
Week 1: launch B3 (no build). Design and build the card (wave 1).
Weeks 2-3: card live for wave 1 entry points in cities that pass the supply check. Start C1 (always on).
Weeks 4-5: read the card; reorder rows; add wave 2. Start B2 if tracking exists.
Week 6: decision review: scale, change or stop each; plan B1.

## D1 Event entry for new users (added after the hiring-manager review)
What: (a) 1-2 event services in the homepage "trending" and "popular" lists and in the search empty state "Önerilen hizmetler", rotated by season (Oct-Mar: nişan, kına, kız isteme; birthday peaks Mar, Sep, Oct per 2019 Armut data); (b) app home: same slot; (c) synonym fixes where search is weak (takı töreni to nikah/nişan photographer).
Fit: merchandising and search config only; the request flow does not change.
Precedent: ProntoPro (same group) shows wedding photographer in its homepage trending list (audit 2026-11-07); ask the ProntoPro team for its event request share and tile CTR as the prior.
Test: user-level 50/50 on homepage and search empty state. Primary: event request starts (and submits) from users with no past event request. Guardrail: total requests per homepage visitor (the slot must not just move clicks away from core services), core request starts.
Simulated outcome: ~1,500 a year (790-2,600); confidence low because homepage traffic is unknown.
Pre-mortem: (a) users ignore event tiles because they come for a core job; measure CTR first week. (b) cannibalizes core clicks; guardrail on total requests. (c) wrong season picks; rotate by real weekly event demand once data is in.
