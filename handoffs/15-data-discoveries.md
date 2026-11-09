# 15 Data discoveries (first-hand, armut.com public pages), checked 2026-11-07

## Event demand on Armut, customers a year (Türkiye, "Yılda N ... müşterisi Armut'a ilan veriyor" on armut.com/profesyonel-uye-ol-<id>)
| Service | /yr | Cluster |
|---|---|---|
| Pasta | 18,184 | Birthday |
| Nişan organizasyon | 12,918 | Wedding chain |
| Doğum günü pastası | 8,963 | Birthday |
| Catering | 8,032 | Hosting |
| Palyaço | 7,633 | Birthday |
| Doğum günü organizasyonu | 7,076 | Birthday |
| Masa sandalye kiralama | 5,379 | Hosting |
| Butik pasta | 5,292 | Birthday |
| Gelin arabası süsleme | 3,446 | Wedding chain |
| Düğün fotoğrafçısı | 2,947 | Wedding chain |
| Kına organizasyon | 2,897 | Wedding chain |
| Nişan fotoğrafçısı | 2,557 | Wedding chain |
| Sandalye kiralama | 2,094 | Hosting |
| Düğün organizasyon | 2,026 | Wedding chain |
| Animatör | 1,540 | Birthday |
| Ses sistemi kiralama | 1,541 | Hosting |
| Çeyiz taşıma | 1,522 | Wedding chain |
| Sünnet organizasyon | 1,419 | Other |
| Balon süsleme | 1,382 | Birthday |
Cluster totals: birthday 50,070; wedding chain 28,313; hosting 17,046; all event-related ~96,800 a year.
Compare: moving 186,667; cleaning 84,391. Armut overall says 110,000+ requests a month (info.armut.com/nasil-calisir), so events are roughly 7% (Inference; customers vs requests and overlaps not known).
Inference: Armut's real event strength is home-hosted and small: birthdays and nişan/söz. Nişan organizasyon (12,918) is 6x düğün organizasyon (2,026). Big salon weddings are not where Armut wins.
Caveats: page dates unknown; customer counts may overlap across services; "pasta" may include non-birthday cakes.

## Do core requests mention events? (price-page samples, 5 cities: İstanbul, Ankara, İzmir, Bursa, Antalya)
Method: free text of sample requests, Turkish lowercasing and ASCII folding, word-start roots (dugun, nikah, nisan, kina, kiz iste, soz, dogum gun, mezuniyet, misafir, parti, mevlut, sunnet, ceyiz, yilbasi, iftar, davet), exclusions (nisantasi, makina).
| Service | Sample requests | Mention an event |
|---|---|---|
| Ev temizliği | 105 | 0 |
| Evden eve nakliyat | 105 | 0 |
| Mobilya montaj | 105 | 0 |
| Masa sandalye kiralama | 73 | 27 (37%): söz, nişan, kız isteme, doğum günü, mevlüt |
- Fact: the first naive scan matched "kina" inside "makina" 10 times: keyword rules need word boundaries and exclusions (Engineer's precision rule confirmed).
- Decision: drop the keyword trigger from cleaning/moving (no signal). Keep a hosting bridge from masa sandalye, sandalye, catering, ses sistemi (signal is real).
- Caveat: Armut chooses which examples are shown.

## Other facts gathered today
- Sign-up is the last step of the request flow (audit), so abandoned starts are mostly anonymous.
- Pros pay a non-refundable fee per quote (Armut replies on Şikayetvar 2025).
- Up to 5 quotes; deal agreed by message or phone; hire known only via "Teklifi Seç" (info.armut.com/nasil-calisir).

## Added later: venues and boats (checked 2026-11-07)
| Service | /yr | Event share in Istanbul price-page samples |
|---|---|---|
| Yat kiralama | 8,792 | 11 of 21 (52%): birthdays, after-nikah tours, proposal |
| Tekne kiralama | 7,737 | 7 of 21 (33%): bekarlığa veda, anniversary, after-wedding |
| Düğün salonu | 4,114 | 6 of 8 weddings; some dated 2027 (long lead, planner type) |
Etkinlik mekanı and Davet salonu pages exist (no count shown). Inference: about 7,100 event requests a year sit inside boat services, more than wedding photographer (2,947). Event base revised to ~108,000.

## Supply proxy: pros "ready to serve" per city (price pages, "civarında N ... hizmet vermeye hazır"), checked 2026-11-07
| Service | İstanbul | Ankara | İzmir | Bursa | Antalya | Customers/yr (Türkiye) |
|---|---|---|---|---|---|---|
| Nişan organizasyon | 2,288 | 772 | 656 | 314 | 316 | 12,918 |
| Masa sandalye kiralama | 1,419 | 476 | 425 | 192 | 210 | 5,379 |
| Doğum günü organizasyonu | 961 | 322 | 274 | 131 | 169 | 7,076 |
| Düğün salonu | 955 | 334 | 275 | 161 | 156 | 4,114 |
| Düğün fotoğrafçısı | 937 | 314 | 263 | 138 | 156 | 2,947 |
| Nişan fotoğrafçısı | 879 | 310 | 242 | 117 | 147 | 2,557 |
| Palyaço | 814 | 298 | 252 | 113 | 124 | 7,633 |
| Gelin makyajı | 755 | 261 | 222 | 104 | 112 | n/a |
| Ses sistemi kiralama | 720 | 239 | 219 | 109 | 103 | 1,541 |
| Doğum günü pastası | 617 | 211 | 173 | 92 | 82 | 8,963 |
| Yat kiralama | 434 | 177 | 126 | 59 | 82 | 8,792 |
Reading (Inference): if Istanbul has ~40% of requests (Para Dergi 2026-10-07), Istanbul wedding photographers see roughly 1-2 requests each a year on Armut, nişan organizers ~2. Supply count is not the bottleneck; demand is. Caveat: "ready" counts look loose (yat kiralama shows 177 pros for Ankara, which has no sea), so they likely include pros serving several cities or inactive pros. The real pre-check still needs quote speed data (3+ quotes within 24h).
Implication: event pros are hungry for leads, which supports supply-side distribution ideas (pro Instagram/referral links, QR via pros) and lowers the risk that card leads go unanswered; the per-quote fee still means lead quality must hold.

## Homepage search test (typed live on armut.com, 2026-11-07)
| Typed | Suggestions (first ones) |
|---|---|
| kına | Kına Organizasyon, Kına Mekanları, Sünnet Organizasyon, Nedime Kiralama, Kına Elbisesi Kiralama, Kına Fotoğraf Çekimi, Nikah Organizasyon |
| kız isteme | Kız İsteme Makyajı, Kız İsteme Mekanları, Nişan Mekanları |
| 1 yaş | Doğum Günü Mekanları, Palyaço, Doğum Günü Organizasyonu, Yaş Pasta, Doğum Günü Animatör (then noise: Yas Danışmanlığı, Psikolog) |
| baby shower | Baby Shower Organizasyon, Diş Buğdayı Organizasyon |
| takı töreni | Evde Nişan Organizasyonu, Temsili Nikah Memuru, then jewelry making (no photographer) |
Empty search state "Önerilen hizmetler": Evden Eve Nakliyat, Boyacı, Ev Temizliği, Boş Ev Temizliği, Nakliye, Psikolog, Parça Eşya Taşıma, Direksiyon Dersi, Koltuk Yıkama (no event service).
Reading: search quality is good; the gap is that nothing prompts users to think of Armut for events. Venue services exist for events (Kına/Kız İsteme/Nişan/Doğum Günü Mekanları), which covers the most mentioned second need.
