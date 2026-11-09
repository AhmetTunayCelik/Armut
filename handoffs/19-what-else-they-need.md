# 19 What else do event customers need? (first-hand), checked 2026-11-07
Method: free text of sample requests on armut.com/fiyatlari/<city>-<service> pages, 5 cities (İstanbul, Ankara, İzmir, Bursa, Antalya); Turkish lowercasing, ASCII folding, word-start roots. Count of requests that mention another need. Caveat: Armut picks the samples; a need mentioned is not a need unmet.

| Requested service (n) | Other needs mentioned (share of requests) |
|---|---|
| Doğum günü organizasyonu (84) | venue 29 (35%), masa sandalye 18 (21%), palyaço/animatör 14 (17%), photo 7 (8%), cake 5, food 5, music 4 |
| Nişan organizasyon (43) | venue 22 (51%), masa sandalye 19 (44%), süsleme 13, music 8 (19%), flowers 7 (16%), food 6, photo 5 (12%), cake 4, garson 3 |
| Masa sandalye kiralama (73) | organizasyon 18 (25%), venue 12, food/catering 7 (10%), süsleme 5 |
| Palyaço (105) | venue 20, süsleme 17 (16%), music 12 (11%) |
| Kına organizasyon (61) | venue 17 (28%), süsleme 9, photo 5 (8%), music 5, masa 4 |
| Düğün fotoğrafçısı (76) | venue 21 (28%), make-up 5 (7%) |
| Doğum günü pastası (99) | süsleme 8, photo 6 (6%), venue 5 |
| Catering (79) | masa 3, organizasyon 3, cake 2 |
| Gelin arabası süsleme (96) | flowers 17 (part of the same job) |

## What this changes
- Card should start after organization requests (birthday, nişan), not after cake. Cake buyers are focused (6-8% mention anything else); organization buyers mention a second need 17-44% of the time.
- Evidence-based card rows:
  - Doğum günü organizasyonu: Masa sandalye kiralama, Palyaço/Animatör, Doğum günü fotoğrafçısı
  - Nişan organizasyon: Masa sandalye kiralama, Ses sistemi kiralama, Nişan fotoğrafçısı
  - Masa sandalye kiralama (event text): the matching organization (nişan/söz or doğum günü), Catering
  - Palyaço: Balon süsleme, Ses sistemi kiralama, Doğum günü pastası
  - Later: cake, kına, düğün fotoğrafçısı (to gelin makyajı), çeyiz (destination city)
- Venue ("mekan, salon, bahçe") is the most mentioned need everywhere (28-51%). Armut does not list venue rental as a service in what we saw (Assumption to check). Roadmap idea: partner listing of small venues, or "evde/bahçede" hosting content.
- Simulation updated (handoff 18): card CTR priors now split by entry type.

## Added: venue and boat entry points (wave 1 candidates)
- Yat / tekne kiralama with an event word in free text: Doğum günü pastası, Fotoğrafçı (event type), Ses sistemi / DJ or Balon süsleme. Evlilik teklifi text: Evlilik teklifi fotoğraf çekimi.
- Düğün salonu: Düğün fotoğrafçısı, Gelin makyajı, Kına organizasyon (these couples plan months ahead, unlike the short-notice photographer requests).
- Venue is the most mentioned second need (28-51%), and Armut has Düğün salonu, Etkinlik mekanı, Davet salonu: add "Mekan" as a row for organization requests that mention a venue (Assumption: venue supply is thin outside Istanbul; check pro counts).
