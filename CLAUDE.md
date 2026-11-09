# Armut / ProntoPro APM Case Study: Instructions and Context

Read this file first in any new session. Then read agents-and-roles.md for who does what and which decisions go to Bulent. Then read armut-case-notes.md for progress. Then continue from the first unchecked step in the plan.

## Purpose
This is a job application case study for an Associate Product Manager role at Armut/ProntoPro. The user is Bulent (Istanbul). The deliverable is a presentation of up to 15 slides with a lightweight wireframe or prototype. The company cares about product thinking, not visual polish: how the problem is framed, what is noticed, how choices are prioritized, and why.

## How to work (user's instructions)
- Act as a senior product manager and as an agent: plan, research, check, deliver. Do not wait for approval at every step.
- Use simple but effective language. Be concise and direct.
- No AI-generated images. No emojis.
- When researching, always give the URL and open the actual websites. Use current information and note the date checked.
- Mark anything unverified as an assumption and say what evidence would confirm or reject it.
- Order of work: problem first, then possible solutions, then similar products and comparative analysis. The presentation is the last part.
- Keep the AI conversation or an exported transcript. The company asks for it with the submission.
- Company time guide is 2-3 hours of work. Do not over-invest.
- Keep the user's own voice in anything written for them. Do not over-polish.

## The brief (from "Armut_ProntoPro APM 2026 Case Study (1).pdf" in this folder)
- Role: Associate Product Manager. Team: 1 backend developer, 1 frontend developer, 1 UX designer.
- Goal: increase request volume in Event-related services (Wedding Photographer, Birthday Cake, Bridal Make-up and similar). This category is a small share of total requests today.
- Explore the customer journey from three starting points:
  1. Homepage search
  2. Service page reached through a marketing campaign
  3. Local service listing page (e.g. "Wedding Photographer in Istanbul")
- Answer:
  1. What are the most important opportunities or problems?
  2. What extra information would you want to understand and prioritize them, and how would you gather it?
  3. Which opportunity do you prioritize first, and why?
  4. What would you change or test first?
  5. How would you measure success?
- Missing data: state assumptions explicitly and say what evidence would validate or reject them.
- Benchmark screenshots are welcome.

## Links (Wedding Photographer flows)
| Product | Homepage | Campaign service page | Local listing | Request flow |
|---|---|---|---|---|
| Armut (TR) | https://armut.com/ | https://armut.com/d/dugun-fotografcisi/194 | https://armut.com/istanbul-dugun-fotografcisi | https://consumer.armut.com/request-creation/quote/services/194/steps/1?originUrl=https%3A%2F%2Farmut.com%2F |
| ProntoPro (IT) | https://prontopro.it/ | https://prontopro.it/d/fotografo-per-matrimoni/112225 | https://prontopro.it/milano-fotografo-per-matrimoni | https://consumer.prontopro.it/request-creation/quote/services/112225/steps/1?originUrl=https%3A%2F%2Fprontopro.it%2F |
| Homerun (UK) | https://homerun.co.uk/ | https://homerun.co.uk/d/wedding-photographer/516 | https://homerun.co.uk/wedding-photographer | https://consumer.homerun.co.uk/request-creation/quote/services/516/steps/1?originUrl=https%3A%2F%2Fhomerun.co.uk%2F |

Armut is the focus. ProntoPro and Homerun are benchmarks. Other service pages, Pro profiles, landing pages and external competitors are allowed too.

## Roles (agents)
- Product Lead: framing, prioritization, final story
- Journey Auditor: walks 3 entry points on 3 sites, records steps, friction, screenshots
- Competitor Researcher: external and event-specific marketplaces, with URLs
- Insight Analyst: reviews, forums, search demand; builds assumptions and the data wish list
- Product Analyst: funnel model, metrics, experiment design
- UX Designer: lightweight wireframe of the first change
- Fact Checker: checks every claim, link and number
- Presenter: the deck, last

## Plan (tick off as done; log results in armut-case-notes.md)
- [x] 1. Journey audit (done 2026-11-07 for wedding photographer, all 3 flows walked to the end; gaps in handoffs/01-journey-audit.md): 3 entry points x 3 sites. Same checklist each time: first impression, relevance to events, trust signals, price clarity, steps and questions in the request flow, drop-off risks, mobile view. Save screenshots in a screenshots/ subfolder.
- [x] 2. Extra research: other event marketplaces, search demand for event services in Turkey, seasonality, provider supply by city.
- [x] 3. Problems and opportunities list, scored by impact, confidence, effort.
- [x] 4. Pick one opportunity. Define the first change and the test.
- [x] 5. Metrics: primary, guardrails, duration, what counts as a win.
- [x] 6. Data wish list and how to get it (funnel analytics, search logs, interviews, provider data).
- [x] 7. Wireframe (v2: wireframe/next-for-your-event-card.html).
- [ ] 8. Deck (max 15 slides) and AI conversation export.

## Slide skeleton (draft, max 15)
1 Title and goal; 2 Approach and sources; 3 Where event requests stand (assumptions marked); 4 Journey: homepage search; 5 Journey: campaign page; 6 Journey: local listing; 7 Benchmark vs ProntoPro, Homerun, others; 8 Problems and opportunities; 9 What I want to know and how to get it; 10 Prioritization and chosen opportunity; 11 First change (wireframe); 12 Test design; 13 Metrics and guardrails; 14 Risks and next steps; 15 Appendix: sources.

## Where things live
- This folder (armut pm) on the user's computer is the working folder. Save outputs here.
- The claude.ai project "Armut" holds a copy of the brief and plan (claude/case-brief-and-plan.md).
- Deck type: build it last, from the Slides type if available.
