# Armut case study: progress log

Update this after every work session. Newest entries at the bottom. Include the date, what was done, URLs checked, and what is next.

## 2026-11-07
- Case study PDF read. Brief, roles, plan and rules saved in CLAUDE.md.
- No research done yet. Next step: plan step 1, the journey audit, starting with Armut.

## 2026-11-07 (later)
- Reviewed https://github.com/deanpeters/Product-Manager-Skills (checked today). Used as a method reference only.
- Created agents-and-roles.md: 8 agents, 4 decision gates for Bulent, workflow order, rules, handoffs/ and screenshots/ folders.
- Next: plan step 1, journey audit, Armut first.
- Read the repo in detail (cloned, commit cfcb697). Copied 15 relevant skills + discover/prioritize commands to reference/pm-skills/. Updated agents-and-roles.md with what we adopt and what we skip.

## 2026-11-07 (evening): plan step 1, journey audit (first pass done)
- Walked the 3 entry points and the request flow for wedding photographer on Armut, ProntoPro, Homerun in the built-in browser (mobile layout). All 12 links in CLAUDE.md opened. URLs and numbers in handoffs/01-journey-audit.md. 18 screenshots in screenshots/.
- Armut flow stopped at step 4: typing into the form was blocked by the permission check. ProntoPro stopped at step 6, Homerun at step 2, same reason. No form was submitted.
- Main findings: no event service on Armut homepage trending or popular lists; campaign page has no price or work examples; local list is uncurated; step 4 text is mandatory; ProntoPro lists wedding photographer in trending and offers makeup as an add-on.
- Next: Fact Checker pass, then plan step 2 (competitors, insights, data).
- Fact Checker pass: subagent could not fetch pages (allowlist); fixed 4 label issues it found; key claims re-run in browser. Plan step 1 ticked as first pass.
- Armut flow walked to the email/account step (steps 4 to 6 with realistic answers). Stopped at account creation; Bulent will do the account step in the pane. ProntoPro and Homerun wait until Armut is done. Details in handoffs/01-journey-audit.md "Update 2".
- Armut: email entered, flow moved to signup/name. Stopped for Bulent to do sign-up in the pane.
- Armut flow finished by Bulent (sign-up + submit). Read post-submit screens: request 57338138, tracker, grouped service list (events split over 3 groups). Next: ProntoPro flow, then Homerun.
- ProntoPro: flow walked to account/login (email already has an account there). Waiting for Bulent to log in. Homerun after.
- ProntoPro: request sent by Bulent (job 57338238). Success screen read. Next: Homerun flow.
- Homerun: flow walked to login (shared account recognized). Waiting for Bulent to log in/send.
- Homerun: request sent by Bulent (job 57338294). All three flows walked to the end. Full comparison in handoffs/01-journey-audit.md (Update 8). Open: check quotes in 24h; cancel test requests after.

2026-11-07: Step 2 done. Wrote handoffs/02-competitors.md, 03-insights.md, 06-data-wishlist.md. Label fixes applied (T3 to Inference; company claims marked). Open: re-open key URLs by hand, birthday cake and bridal makeup flows not walked, quotes check on 3 test requests.

2026-11-07: Step 3 draft written: handoffs/04-opportunities.md (9 items scored). Waiting for Bulent: G1 problem statement, G2 pick (suggested O2, with O1 pair, O8 guardrail).

2026-11-07: G1 and G2 accepted by Bulent. Steps 3-6 done: handoffs/04, 05, 06. Chosen: O2 lead, O1 pair, O8 guardrail. Next: step 7 wireframe, then G3 outline, deck.

2026-11-07: Step 7 done: wireframe/first-change.html (3 panels: today, new page, date step). Next: G3 outline to Bulent, then deck.

2026-11-07: G3 approved. Deck v1 built (15 slides, Slides artifact): https://claude.ai/artifact/42CKjFLkY7ShaFpgRgnukh . Not visually checked yet. Open: review by Bulent, re-open source links, quotes check on 3 test requests, export conversation, cake and makeup flows not walked.

2026-11-07: Bulent ruled out O2 and O6 (Armut keeps range-then-pro-prices; no shared-structure changes). Deck paused. 2 real quotes received (GBP): handoffs/07. New ideas: handoffs/08. Next: Bulent finalizes ideas, then redo 05 test/metrics and wireframe, then the deck.

2026-11-07: Ideation round 2 (3 agents + critic + Armut price pages). New first-hand finding: event demand is short-notice and small (handoffs/09). Shortlist in handoffs/10: lead F2 same-event cross-sell, parallel F1 birthday comeback, F4 later. Waiting for Bulent.

2026-11-07: Round 3 (awareness/trust). Found çeyiz taşıma bridge (45,882 reviews) and event ratings 4.8-4.9 vs core 4.1-4.4. Proposed first change: "Next for your wedding" card after submit (çeyiz, event, birthday cake). handoffs/11, 12. Waiting for Bulent.

2026-11-07: Bulent approved "Next for your wedding". Checked post-quote workflow (info.armut.com/nasil-calisir): deals close by message/phone, hire known only via Teklifi Seç; T2 moved to roadmap. Sizing from pro pages (cake 8,963/yr, wedding photographer 2,947/yr, çeyiz 1,522/yr). Review counts likely pooled: corrected. New ideas N1-N5 and metric tree in handoffs/13.

2026-11-07: Brainstorm with agents (5 new roles hired). 32 ideas, cross-reviewed. Shortlist in handoffs/14: card + keyword trigger, Misafir gelmeden önce, price pages upgrade, copy angle test, abandoned-start recovery; supply pre-check. Pros pay per quote, non-refundable.

2026-11-07: Round 3 + data discoveries (event volumes ~96,800/yr; cleaning/moving 0/315 event mentions; masa sandalye 37%), comparisons, Monte Carlo simulations (simulation/), final ranking in SOLUTIONS-RANKING.md. Waiting for Bulent to pick.

2026-11-07: Independent review of simulation; v2 numbers and ranking (card program 1,161; abandoned starts 726; combined ~2,800 +2.9%). Files: SOLUTIONS-RANKING.md, handoffs/18, simulation/.

2026-11-07: Second-need scan (handoff 19): start card after organization requests, not cake. Sim v3: card 1,024/yr. Tier 1 specs + pre-mortems + 6-week plan (handoff 20). Wireframe redrawn for the card.

2026-11-07: Found hidden event demand in yat/tekne kiralama (52%/33% events) and düğün salonu. Event base ~108k. Sim v4: card 1,269/yr; combined ~3,100. Specs and ranking updated.

2026-11-07: Search tested live (works); homepage/search empty state show no events. Added D1 discovery idea (rank 1). Hiring-manager review answered (handoff 22). Ranking v5 rewritten: recommended set ~4,300/yr (3,300-5,600). Specs + D1 in handoff 20.

2026-11-08 00:00-01:30: Grading panel (4 judges + red team), 3 rounds: 68 -> 76 -> ~79.5. Fixes in handoffs 23, 24, 26, 27; ranking v8; wireframe v3; interview prep handoff 25. Note: Bulent to cancel the 3 live test requests.

2026-11-08 ~01:45: Cycle 4: channel preference medium (strong for butik pasta); Armut indexed for event keywords; title-fix idea refuted; pro share link moved to next after P1. Handoff 28.

2026-11-08 ~02:00: Cycle 5 trust layer: pick guidance card + review recency (handoff 29).

2026-11-08 ~02:15: Round 4 judges: HoP 79; red team attacks noted; final v9 ranking (D1 photographer + organization only, pre-season timing, holdout decides core cost, next-if-wins line). Interview prep updated.

2026-11-08 15:50: Bulent ideas discussed by panels: occasion page (D1 destination) and creator tagging (second bet). Handoff 30, ranking v10.

2026-11-08 16:05: Final rating of all ideas (handoff 31): top = post-submit card 22, occasion entry 21, copy test 20, SEO pages 19; creator program 12 (later, with marketing).

2026-11-08 16:40: Platform framing (handoff 32): findings across Armut, ProntoPro, Homerun; recommendation as platform layers. Gap: ProntoPro/Homerun demand data not checked.

2026-11-08 17:00: Cross-market data (ProntoPro IT counts, Milano samples; Homerun small) and CASE-ANSWERS.md (platform-wide answers to the 5 questions + ranked solutions).

2026-11-08 18:30: Solution 2 chosen by Bulent. Benchmarks (handoff 33, screenshots/benchmarks), 3 design options (wireframe/occasion-hub-designs.html), slide content (PRESENTATION-CONTENT.md).

2026-11-08 18:50: FINAL: REPORT.md (full content, occasion entry as main bet) and SLIDES-SUMMARY.md. Final review 76/100 -> 5 wording fixes applied (main-bet reason, all 3 entry points covered, constraint wording, simplified metrics with kill threshold and duration, panel scores removed). Older ranking files superseded.

2026-11-08 18:45: HTML deck (deck/slides.html, 15 slides, arrow keys) and clickable prototype (deck/prototype.html) built from SLIDES-SUMMARY.md. Not visually checked yet.

2026-11-08 23:45: Deck final pass: Getir screenshot dropped (feature removed per Bulent), "So what" callouts on key slides, closing "In one sentence" slide, appendix with transcript placeholder (17 slides). Rendered and checked: layout fixed on slides 4 and 12; prototype flow works.
