# 01 Journey audit: wedding photographer, Armut vs ProntoPro vs Homerun

Owner: Journey Auditor, merged by Product Lead
Date checked: 2026-11-07 (Saturday evening, Istanbul). Live numbers change daily.
Inputs: the 12 links in CLAUDE.md, opened in the built-in browser. Screenshots in screenshots/ (names end with the date).
Labels: Fact = seen on the page. Inference = my reading of facts. Assumption = needs evidence.
Fact Checker status: first pass done 2026-11-07. The Fact Checker could not fetch the pages (domains not on the fetch allowlist), so it reviewed labels only. Its label fixes are applied. The key page claims were re-run in the browser with a keyword script (see 'Check log' at the end). A full independent check of the Fact lines is still open.

## What the browser showed me
The browser pane rendered the mobile layout on every page. All screenshots and notes are the mobile view. Desktop was not checked.

## Armut, three entry points

### 1. Homepage search (https://armut.com/)
- Fact: the 12 "trending services" are moving, painting, cleaning, insurance, massage, plumbing, psychologist and similar. None is an event service.
- Fact: the "popular services" list has 24 items (cleaning, boiler service, moving, tiling, tutoring, decoration and similar). None is an event service. (The word "dekorasyon" appears 3 times, as home decoration: wall, home, kitchen. I do not count it as an event service.)
- Fact: the search box suggests the right service for all three brief examples. "düğün fotoğrafçısı" gives Düğün Fotoğrafçısı and Düğün Hikayesi. "doğum günü pastası" gives Doğum Günü Pastası. "gelinlik saç makyaj" gives Gelin Saç Makyaj, Saç ve Makyaj, Nişan Saç Makyaj and others.
- Gap: I did not open the "Menü". There may be categories there.
- Inference: event services are found only by people who already know what to type. The homepage does not suggest them.

### 2. Campaign service page (https://armut.com/d/dugun-fotografcisi/194)
- Fact: headline "1.762 Düğün Fotoğrafçısı hazır." Promise: "4 fiyat teklifi al, karşılaştır." One main button: "Başla".
- Fact: proof shown is 4,8 rating, 2.937 satisfied customers, 5.185 verified reviews, and 8 review texts. Reviewer names are masked as "xxxx".
- Fact: the page shows no price, no price range, no pro names, no photos of work and no FAQ. The only price-related element is a "Fiyat hesapla" button near the bottom.
- Fact: reviews mention events outside the big cities (a Bodrum wedding) and henna (kına) shoots.
- Inference: a visitor must start a request before seeing any price or any example of work.

### 3. Local listing (https://armut.com/istanbul-dugun-fotografcisi)
- Fact: the page title says "En İyi 40 İstanbul Düğün Fotoğrafçısı". The hero says "5 İstanbul Düğün Fotoğrafçısı Fiyat Teklifi Al". It also says 937 photographers, 2.738 reviews, 1.577 people a year in Istanbul.
- Fact: each of the 40 entries shows a name, a date, a district and a short bio. The page text shows no rating and no price per entry. I did not scroll to check for photos.
- Fact: the dates on entries range from 2016 to 2026.
- Fact: several bios are not about weddings: product, property, corporate and video work. One bio is placeholder text ("Dneme deneme..."). One says the person is a high school student with no prior work. One talks about loving cats and dogs.
- Inference: the list looks uncurated. A couple choosing between photographers has little to compare.
- Fact: ProntoPro's Milan list also shows entries from 2015-2017, a student bio and commercial-photography bios. Homerun's list has a property photographer. Inference: this is probably a platform-wide pattern, not Armut only.

### Request flow (https://consumer.armut.com/request-creation/quote/services/194/steps/1?...)
- Fact: a price range is shown from step 1: 5.000 TL - 30.000 TL. It narrows as answers are given (6.000-20.000 at step 2, 5.000-12.000 at steps 3 and 4).
- Fact: a banner says "Bu hizmet Kasım ayında %15 indirimli!" on every step.
- Fact: steps: 1 venues (multiple choice), 2 included services (album, video, drone, print, story, clip, digital delivery, CD/DVD), 3 hours (0-1, 2-4, 5-8 all day), 4 free text "İhtiyacın detayları neler?" with a voice option and two examples.
- Fact: step 4 is mandatory. Pressing "Devam" empty shows "Zorunlu alan".
- Fact: the event date is not a question. It appears only in the free-text examples.
- Gap: I stopped at step 4. Typing into the box was blocked by the permission check, so steps after 4 (expected: contact details) are not walked. This is an Assumption.

## Benchmarks (same wedding photographer service)

| | Armut (TR) | ProntoPro (IT) | Homerun (UK) |
|---|---|---|---|
| Wedding photographer in homepage "trending" | No | Yes: 1.563 pros, 5,0 (2.963 reviews) | No (Photographer is only in the "popular" list) |
| Campaign page main button | "Başla" | "CONFRONTA" (compare) | "See our instant prices™" / "CONTINUE" |
| Price on campaign page | None | None | None (button text says "See our instant prices™") |
| Reviews on campaign page | 5.185 total, 8 shown, names masked | 2.963 total, 8 shown, names masked, longer texts | 56 total, 5 shown, names masked |
| Pros for the service | 1.762 (country), 937 (Istanbul) | 843 (Milan) | 326 (UK), 325 on local page |
| Local list contents | 40 entries; some old (2016), off-topic or placeholder bios | 40 entries; some old (2015-2017), student or commercial-only bios | 40 entries; one property photographer bio seen in the part read |
| Price range in the flow | From step 1: 5.000-30.000 TL | From step 1: 380-1500 EUR | From step 1: 250-700 GBP |
| Steps before the free-text box | 3 choice steps, text is step 4 (mandatory) | 5 choice steps, text is step 6 ("75% completato") | 1 choice step, text is step 2 |
| Related services in flow | None seen | Step 3 optional add-ons include "Make up e stylist" (can skip) | Not seen |
| Date question | In text only | Not seen in steps 1-6 | In text examples only |

Notes on the benchmark
- Inference: all three flows use the same platform template (same layout, price bar, choice steps, free-text step). Differences are in the questions and the order. Only the first steps were walked.
- Fact: ProntoPro puts wedding photographers in its trending list. Armut and Homerun do not.
- Fact: ProntoPro's add-on step names makeup and styling. Armut's step 2 lists only photography deliverables.

## Candidate problems and opportunities (hypotheses, not decisions)
Each is an Inference or Assumption. The last column is what would confirm or reject it.

| # | Hypothesis | Label | What would confirm or reject it |
|---|---|---|---|
| H1 | Event services are invisible on the Armut homepage, so demand starts only from people who already search for them | Inference | Homepage category clicks and search terms; share of event requests that start from search vs campaign vs local pages |
| H2 | The campaign and local pages ask the visitor to start a request before showing price or work. The price range appears only inside the flow | Inference | Drop-off from landing page to step 1; test with a price range on the page |
| H3 | The local listing is uncurated (old, off-topic, placeholder profiles), which hurts trust | Inference | Click and request rates on local pages; share of listed pros with recent activity or event jobs |
| H4 | The mandatory free-text step 4 is a drop-off point, and a structured date question is missing | Assumption | Step-by-step drop-off at step 4; compare completion with and without a date question |
| H5 | Wedding and related event services are bought together, but Armut does not connect them in the flow | Assumption | Share of wedding requesters who also request makeup, cake, venue or other services; ProntoPro add-on usage if available |
| H6 | Seasonality matters (the November banner suggests promotions already run) | Assumption | Monthly request volume by event service, wedding season peaks, past promo results |

## Data wish list (feeds step 6 of the plan)
1. Funnel by entry point: homepage search, campaign page, local listing to request start, step 1 to submit, quotes received, job won.
2. Step-level drop-off in the event request flows.
3. Request volume and share by event service and month.
4. Supply: active pros per city and service, response time, quote count per request.
5. Search logs: event terms searched, no-result searches.
6. Customer interviews: how couples find and choose a photographer today (Instagram, referral, other).

## Not covered yet (gaps)
- Desktop layout, the "Menü" navigation, pro profile pages.
- Birthday Cake and Bridal Make-up flows. Only the wedding photographer was walked.
- Armut flow after step 4. ProntoPro flow after step 6 (stopped at the free-text box). Homerun flow after step 2.
- Cookie banners: declined on Armut, left untouched on ProntoPro and Homerun.
- Nothing was submitted on any site.

## Next
1. Fact Checker re-checks the Fact lines against the live pages.
2. Competitor Researcher and Insight Analyst start (plan step 2), using this file.

## Check log
- 2026-11-07, Fact Checker (subagent): could not fetch any page (not on the fetch allowlist). It reviewed labels and found 4 wording problems. All 4 fixed above, plus the "Menü" line moved to gaps.
- 2026-11-07, Product Lead, keyword script in the browser, same pages re-opened:
  - Armut homepage text has 0 hits for düğün, nişan, gelin, pasta, makyaj, fotoğraf, organizasyon, davet, doğum günü. PASS.
  - ProntoPro homepage still lists "Fotografo per Matrimoni, 1.563 professionisti, 5,0 (2.963 recensioni verificate)" in the trending block. PASS. Note: the trending block rotates weekly, so this may change.
  - Homerun homepage: 0 hits for "photograph" or "wedding" in the trending block; "photographer" is in the popular list. PASS.
- Still open: counts, headlines and local-list details were read once from page text and not re-checked by someone else. Counts drift daily, so use "as of 2026-11-07" in the deck.

## Update 2: Armut request flow, steps 4 to account (2026-11-07, 21:40)
Walked with a realistic answer (wedding on 12 June 2027, Istanbul, all day, digital delivery). No personal data typed. Nothing submitted.
- Fact: step 4 accepted free text and moved on. Step 5 "Nerede?" asks Il, İlçe, Mahalle (three dropdowns) or "Lokasyonumu kullan". Neighbourhood level is asked for a wedding that may be in a venue elsewhere.
- Fact: step 6 "Ne zaman?" asks when the service is needed, not the event date. Options: a set date within three weeks (pre-filled: 14 Nov 2026, 09:00), within two months, within six months, "Sadece fiyat bakıyorum" (just looking at prices).
- Inference: for a wedding planned months ahead, the pre-selected "within three weeks" does not fit and the event date is still not asked. It is only in the free text.
- Fact: the progress label reads "%84 tamamlandı" at step 5 and "%100 tamamlandı" at step 6, and still "%100" on the next screen, the account step.
- Fact: after step 6 the flow goes to /account/email: "Email adresini gir ... talebini oluşturmak için email adresine ihtiyacımız var" with "Bu bilgiyi kimseyle paylaşmıyoruz." Request creation needs an account step. So the flow is 6 steps, then email.
- Fact: the "just looking at prices" option exists, but the email step comes after it. Inference: price browsing still ends in an email wall. Confirm with funnel data on that option.
- Stopped here. Reason: creating an account or entering a password is something I may not do. Waiting for Bulent to take over this step.

## Update 3: Armut account step (2026-11-07, 21:45)
- Fact: email [test email] (given by Bulent) entered at /account/email. The next URL is /account/signup/name, so this email was treated as a new user and moved into sign-up.
- Fact: sign-up step "Lütfen adını ve soyadını gir" asks for first and last name. Note under it: providers reply faster to requests that have a name. Progress label still "%100 tamamlandı".
- Inference: the sign-up is built into the request. A new user gives email, then name, then probably more (phone, verification, password) before the request exists. Not seen yet.
- Stopped. Sign-up is account creation, which Bulent does himself in the pane.

## Update 4: Armut after sign-up (2026-11-07, 21:50)
Bulent did the sign-up and submitted the request himself. I read the screens after that. The screens between "name" and "request created" (phone, verification, password) were not seen by me. Ask Bulent to list them if the deck needs them.
- Fact: the request exists: "Düğün Fotoğrafçısı, Altı ay içinde, Abbasağa Mah, Beşiktaş, İstanbul". Request number 57338138. Status "Teklifler yolda! Teklif geldiğinde haber vereceğiz." No time estimate for the first quote is shown.
- Fact: the details page has a tracker: Talep alındı, Teklif toplanıyor, Teklif seç, Hizmet tamamlandı (Yorum yaz). It also shows "Telefonla arayabilirler, numaram gizli kalsın", so a phone-visibility choice was part of the flow.
- Fact: the details page repeats all answers. The event date appears only inside the free text. The "when" field says "Altı ay içinde" (the event is about seven months away).
- Fact: the "İşlerim" page and a promo bar push the app download ("Uygulamayı indir") twice on first view.
- Fact: below the request, "Trend Olan Hizmetler" is a long, grouped list of all services. Event-type services are spread over three groups: "Organizasyon" (Organizasyon, Pasta, Catering, Davul Zurnacı Kiralama, Tabldot Yemek, Palyaço, Evde Nişan Organizasyonu, Dansöz Kiralama), "Güzellik" (Makyaj, Kuaför, Gelin Saç Makyaj, Saç ve Makyaj and others) and "Fotoğraf ve Video" (Nişan Fotoğrafçısı, Düğün Fotoğrafçısı, Düğün Video Çekimi and others).
- Inference: there is no single "wedding" or "events" group. A couple planning a wedding must pick photographer, makeup, cake and more from three separate groups, one request each. This supports H5 (related services are not connected). Confirm with data on how many requesters ask for more than one event service.
- Inference: the full service list is seen only after sign-up; the logged-out homepage shows 12 trending services without events (see Armut homepage). Confirm by opening the "Menü" logged out.
- Open: what quotes arrive. The live request lets us measure time to first quote, number of quotes and prices for a wedding seven months ahead. Check again in 24 hours (Assumption: Armut sends quotes to the email and phone Bulent used).
- Note for Bulent: the request is live. Photographers may email or call. Cancel it in "Detaylar" if you do not want that.

## Update 5: ProntoPro request flow to the login step (2026-11-07, 22:05)
Walked with a realistic answer (wedding 12 June 2027, Milan, all day, digital delivery, ceremony). Add-ons skipped. Nothing submitted.
- Fact: 8 steps before the account step: 1 hours, 2 time of day, 3 add-ons (optional, includes "Make up e stylist"), 4 which event, 5 where (church, town hall, restaurant, landscape, other), 6 free text, 7 location (Provincia, Città/Comune, Zona; or "Usa la mia posizione"), 8 when.
- Fact: step 8 "Quando hai bisogno del servizio?" is the same question as Armut step 6, with the same pre-selected default "In una data precisa (entro tre settimane)" (14 Nov 2026, 09:00) and the same options (two months, six months, "Sto solo cercando il prezzo"). I chose "Entro sei mesi".
- Fact: the price range moves with answers: 380-1500 EUR at step 1, 500-1500, then 650-1700 EUR from step 3.
- Fact: the progress label reads "75% completato" at step 6, "88%" at step 7, "100%" at step 8, and still "100%" on the email and login screens. Same as Armut.
- Fact: after the email ([test email], given by Bulent) the next URL is /account/login: "Questa email è già associata a un account. Accedi per continuare." Options: password, "Accedi senza password", "Accedi con il numero di telefono". A note says the phone number is shared with the professionals who send quotes. The button reads "Invia richiesta".
- Inference: the email created on Armut an hour earlier was already known to ProntoPro. The accounts look shared across the group's countries. Confirm by asking Armut or checking on Homerun.
- Inference: ProntoPro asks 7 questions plus a login; Armut asked 6 plus sign-up. ProntoPro's extra questions (time of day, which event, venue type) are more wedding-specific; Armut's are fewer. Which converts better is unknown (Assumption; needs funnel data).
- Stopped at the login screen. Bulent signs in himself.

## Update 6: ProntoPro after submit (2026-11-07, 22:15)
Bulent logged in and sent the request himself. I read the success screen.
- Fact: success page: "Abbiamo ricevuto la richiesta di Fotografo per Matrimoni, ora scarica l'app!" Job id 57338238.
- Fact: it sets an expectation: "Di solito i professionisti inviano il preventivo entro poche ore" (usually within a few hours). Notice by email and SMS. Next steps: "I preventivi sono in arrivo", then "Confronta e scegli".
- Fact: it shows a red "Cancella richiesta" link directly on the success page. Armut's details page showed a status tracker but no time estimate (see Update 4).
- Fact: the Armut request number (57338138) and the ProntoPro job id (57338238) are close, created minutes apart. Inference: both countries use the same job system (shared backend). Assumption; confirm with the team.
- Inference: ProntoPro tells the user when quotes will come. Armut does not. For a high-value event purchase, a time promise reduces "did it work?" anxiety. Confirm by comparing real time to first quote in the two live requests (check in 24 hours).
- Open: compare quotes that arrive on both requests (count, prices, response time).

## Update 7: Homerun request flow to the login step (2026-11-07, 22:30)
Walked with a realistic answer (wedding 12 June 2027, London, all day). Nothing submitted yet.
- Fact: 4 steps before the account step: 1 hours, 2 free text (not marked mandatory in what I tested; I typed text), 3 location, 4 when. The shortest of the three flows (Armut 6, ProntoPro 8).
- Fact: location is one postal code field with a lookup ("W2 2SZ - Hyde Park Ward, City of Westminster, London") or "Use my location". Armut asks city, district, neighbourhood. ProntoPro asks province, city, zone.
- Fact: "When? (date of the job)" has the same options and the same default as Armut and ProntoPro: "Specific Time (Within three weeks)", 14 Nov 2026 09:00, In Two Months, In Six Months, Just Looking For Price. I clicked "In Six Months"; the screenshot tool showed a stale image, so I cannot confirm the choice registered. Check on the request details page after sending.
- Fact: progress label: "75% completed" at step 3, "100% completed" at step 4 and on the email and login screens. Same pattern as the other two.
- Fact: price range moves with answers: £250-£700 at step 1, £380-£850 from step 2.
- Fact: after the email ([test email]) the page is /account/login: "This email address is already in use. Please login", with password, "Log in without a password", "Login with phone number". Note: the phone number is shared with professionals who send quotes. Button "Send request".
- Inference: the account is shared across Armut, ProntoPro and Homerun. The same email was known to all three within an hour. Strong now (two benchmarks recognized it). Confirm with the team.
- Fact: the "when" step is word for word the same question and default in all three products. Inference: one shared template; a change to the "when" step could be tested once and rolled out to all.
- Stopped at login. Bulent logs in and sends.

## Update 8: Homerun after submit, and full flow comparison (2026-11-07, 22:50)
Bulent logged in and sent the Homerun request. Job id 57338294. Details page confirms "Within six months", 5-8 hours, postal code area, and my text.
- Fact: success page copy matches ProntoPro's: "Pros usually send quotes within a few hours", email and SMS notice, "Cancel request" link, app download push.
- Fact: Homerun's grouped service list has an "Events" group. It contains only photography: Airbnb, Wedding, Property, Birthday, Event, Family Photographer, Fashion Photography. No makeup, cake or catering.
- Fact: the three job ids (57338138, 57338238, 57338294) were created within the same hour. Inference: one shared job system.

### Flow comparison, wedding photographer, mobile, 2026-11-07 (all three walked to the end)
| | Armut (TR) | ProntoPro (IT) | Homerun (UK) |
|---|---|---|---|
| Steps before account | 6 | 8 | 4 |
| Questions asked | venues, included services, hours, free text (mandatory), location, when | hours, time of day, add-ons (optional, includes makeup), which event, where, free text, location, when | hours, free text, location, when |
| Location input | City, district, neighbourhood | Province, city, zone | One postal code with lookup |
| "When" step | Same options, same default (3 weeks, 14 Nov) | Same | Same |
| Event date as its own field | No | No | No |
| Price range shown | From step 1, narrows | From step 1, narrows | From step 1, narrows |
| Progress label hits 100% | At step 6, then 2 more screens | At step 8, then 2 more screens | At step 4, then 2 more screens |
| Account step | Email, then sign-up (new email) | Email, then login (existing account) | Email, then login (existing account) |
| After sending | Tracker, no time promise, no cancel on first screen | "A few hours" promise, cancel link | "A few hours" promise, cancel link |
| Related services | None in flow | Makeup and styling add-on | None in flow |

Reading
- Inference: all three share one template and one account system. Differences are the question set and order. Any fix to shared steps (the "when" default, the progress label, no event date field) can be built once.
- Inference: Armut's success path lacks the time promise and a visible cancel that the two siblings have. Cheap to copy. Confirm real time to first quote on the live requests first.
- Inference: the pre-selected "within three weeks" fits home services but not weddings planned months ahead. All three share it, so the fix applies to the whole event category on all three.

### Hypothesis update
- H4 (mandatory free text, missing date field): Armut asks free text at step 4 of 6, ProntoPro at step 6 of 8, Homerun at step 2 of 4. The missing event-date field is common to all three. Keep as Assumption: needs step-level drop-off data.
- H5 (related services not connected): ProntoPro's makeup add-on is the only link seen in the three flows. Still an Assumption: needs data on multi-service requests.
- New H7: "When" step defaults to "within three weeks", which mismatches a wedding booking. Label: Inference. Confirm: share of event requests that keep the default vs change it; how many event requests have a date far in the future in the free text.
- New H8: the three-field Armut location (down to neighbourhood) adds effort compared with Homerun's single postal code. Label: Inference. Confirm: drop-off at the location step.

### Still open
- Quotes: all three requests are live. Check in 24 hours: number of quotes, response time, price, how pros reply. This is our only first-hand data on supply and speed.
- Desktop layout, Armut "Menü", pro profile pages, birthday cake and bridal makeup flows (plan step 2).
- Fact Checker: the flow facts (steps, labels, ranges) were read from live pages once. Ask a second agent with browser access to re-walk, or accept as first-hand observation with date.
- Cleanup: three live requests exist for [test email]. Cancel them after the quote check if not wanted.
