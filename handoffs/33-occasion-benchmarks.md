# 33 Occasion entry: real examples and design patterns, 2026-11-08
Screenshots: screenshots/benchmarks/ (thumbtack-events-hero, thumbtack-events-groups, dugun-com-hero, dugun-com-callback).
## Grocery "recipe -> basket"
- Getir: recipe-to-basket not found on the web (getir.com/tarifler 404; likely app-only). Confirmed features: "Alışveriş Listem" (photo of a list into a cart), "Hazır Sepet" (basket from past orders; company claim ~90% of pilot users kept it unchanged), "Ne Yesem" on GetirYemek (shiftdelete.net, 2025-10-13). Need: app screenshot from Bulent.
- Migros "Ne pişirsem?": pick a dish, see ingredients, one-click order (Webrazzi 2023-08-14, announced).
- Instacart "Shoppable Recipe": button on Hearst/TikTok recipes adds all ingredients (instacart.com company page; ~56M monthly recipe views claim).
- Carries over: start from the goal, show everything needed on one page. Does not: one cart and one delivery. Services have separate quotes, pros and timing.
## Services grouped by occasion
- Thumbtack /events (thumbtack.com/content/events, seen live): hero "Events" + "Hire a pro"; featured "Good food $25 / DJs $500 / Good times $250" with average prices; then themed groups ("For the kids", "For the grown-ups", "For office events", "For going all out", "Just for fun"), each a list of services. Thumbtack wedding planning page: filter by months before the wedding, "related services" block, FAQ price ranges.
- Düğün.com (seen live): "Her Düğün, Düğün.com ile Başlar! Mekandan gelinliğe, düğünün için her şey"; service + city search; call-back form; "çiftlerden hiçbir servisi için komisyon veya ücret almaz"; category cards with firm counts (Mekan 2,340, Fotoğrafçı 968, Saç-Makyaj 1,417, per agent); planning tools in menu (Ajandam, Bütçem).
- The Knot marketplace: category + city search, "Top categories" (venue, photographer first), 3-step carousel. Bridebook: popular vs all categories, checklist/budget tools, "Get a quote" per supplier, no bulk enquiry.
- No service example offers one "request all" button.
## Patterns for Armut/ProntoPro
1. Occasion hub, one card and one CTA per service, price range + pro count (Thumbtack, Düğün.com, Bridebook) -> Option A, recommended.
2. Checklist ticks ("İhtiyacım var") as Getir-like list without a basket -> Option B, later variant.
3. Timeline by months before the date (Thumbtack filter, planner checklists) -> Option C, only for long-lead planners; our data says most requests are near-date.
Designs: wireframe/occasion-hub-designs.html.
