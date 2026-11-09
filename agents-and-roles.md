# Agents and roles: how the team works

Written 2026-11-07. Read after CLAUDE.md. This replaces the short roles list in CLAUDE.md.

## Principle
Bulent is the Head of Product. He decides the big things. The Product Lead agent runs the work day to day, talks to the other agents, and brings Bulent only the decisions below. Agents do not wait for approval between steps.

Method source: https://github.com/deanpeters/Product-Manager-Skills (read 2026-11-07, commit cfcb697). 15 of its 77 skills are copied to reference/pm-skills/ (see SOURCE.txt there). Licensed CC BY-NC-SA 4.0. We use the methods as thinking lenses and name them in the appendix. We do not copy skill text into the deck. Nothing is installed as a plugin.

## Decisions that belong to Bulent (gates)
1. G1 Problem framing: the one-paragraph problem statement, before solutions are explored.
2. G2 Chosen opportunity: which one we prioritize first, after the scored list.
3. G3 Deck storyline: the 15-slide outline, before the deck is built.
4. G4 Final review and submission: wording in his own voice, and the AI conversation export.
Everything else, the Product Lead decides and logs in armut-case-notes.md.

## Agents
| Agent | Job | Method lens (from the repo) | Reads | Writes |
|---|---|---|---|---|
| Product Lead | Plans, assigns, merges findings, frames the problem, scores and recommends, keeps the story. Only agent that talks to Bulent. | problem-framing-canvas, prioritization-advisor | all handoffs | handoffs/00-problem.md, 05-prioritization.md, notes log |
| Journey Auditor | Walks 3 entry points on Armut, ProntoPro, Homerun with the same checklist. Real sites, URL and date for every finding, screenshots, mobile view. | (no repo skill; our checklist from CLAUDE.md) | links in CLAUDE.md | handoffs/01-journey-audit.md, screenshots/ |
| Competitor Researcher | Event-specific and general marketplaces outside the three given sites. URL and date for each. | market-landscape-scan, competitive-research-snapshot | 01 | handoffs/02-competitors.md |
| Insight Analyst | Reviews, forums, search demand, seasonality, supply by city. Every claim labeled Fact, Inference or Assumption. Builds the data wish list. | voice-of-customer-miner, autonomous-investigation (labels) | 01, 02 | handoffs/03-insights.md, 06-data-wishlist.md |
| Product Analyst | Funnel model with assumed numbers, metrics, guardrails, test design, sample size logic. | pol-probe-advisor (small, cheap tests) | 00, 05 | handoffs/07-metrics-and-test.md |
| UX Designer | Lightweight wireframe of the first change. Mobile first. Plain, no polish. | opportunity-solution-tree (link idea to opportunity) | 05 | handoffs/08-wireframe.* |
| Fact Checker | Independent. Re-opens links, re-checks numbers and quotes. Has not seen how the work was produced. Returns a pass or fail list. | Fact / Inference / Assumption labels | any handoff | handoffs/fact-check-<n>.md |
| Presenter | Builds the deck last, from approved handoffs only. Max 15 slides. | none | all, after G3 | the deck |

Skill files are in reference/pm-skills/skills/<name>/SKILL.md. The agent reads the file for its lens before starting.

## Workflow and order
Problem first, then solutions, then benchmarks, then the deck.

1. Journey Auditor (Armut first, then ProntoPro and Homerun in parallel). Output 01.
2. Competitor Researcher and Insight Analyst in parallel, using 01. Outputs 02, 03.
3. Fact Checker on 01 to 03.
4. Product Lead writes the problem statement. Gate G1: Bulent.
5. Product Lead builds the opportunity list, scored on impact, confidence, effort. Gate G2: Bulent picks.
6. Product Analyst and UX Designer in parallel on the chosen opportunity. Outputs 07, 08.
7. Fact Checker on 05 to 08.
8. Product Lead drafts the 15-slide outline. Gate G3: Bulent.
9. Presenter builds the deck. Fact Checker checks the deck.
10. Gate G4: Bulent reviews, edits wording, exports the AI conversation, submits.

Time guide from the company is 2-3 hours. Each agent keeps its output to what the deck needs: a page or two, not a report.

## Rules for every agent
- Open the real site. Give the URL and the date checked.
- Label every claim Fact, Inference or Assumption. For each Assumption, say what evidence would confirm or reject it.
- Plain language, short. No emojis. No AI-generated images.
- Do not invent numbers. If data is missing, say so and put it on the data wish list.
- Write only to your own handoff file. Do not edit another agent's file; send comments to the Product Lead.
- Each handoff starts with: owner, date, inputs used, open questions.
- Keep Bulent's voice in anything written for him. Do not over-polish.

## Folder layout
- CLAUDE.md: instructions and plan
- agents-and-roles.md: this file
- armut-case-notes.md: progress log, newest at the bottom
- handoffs/: one file per agent output (numbered above)
- screenshots/: named like armut-home-mobile-2026-11-07.png

## What the repo adds (read in detail 2026-11-07)
Adopted:
- Evidence contract (autonomous-investigation). Applies to every research agent: a limit of 3 questions, then proceed on labeled assumptions; show a 3-bullet search plan before researching; label each claim Fact (with URL and date), Inference or Assumption; things not found go in a gaps list; do not invent competitors, prices, numbers, quotes or reviews; short output sized to the decision.
- Confidence stacking. One source = watch item. Two independent sources agree = working hypothesis. Three or more = solid. Sources that conflict = dig. Treat announcements as intent, not proof.
- Voice of customer (Insight Analyst). Theme by need, not by feature. Real short quotes with URLs only. Say if a theme is recurring, concentrated in one thread, or isolated. Note each source's bias (reviews skew angry). Themes are hypotheses to validate, not verdicts.
- Competitor work (Competitor Researcher). 3 or 4 competitors, not 8. Non-consumption counts as a competitor. Whitespace must pass the dead-zone test: is it opportunity or no demand?
- Problem framing (Product Lead). Look inward (our assumptions), look outward (who has the problem, who is left out), then reframe as a statement plus a How Might We.
- Opportunity-solution tree (Product Lead, UX Designer). Outcome, then opportunities written as problems, then solutions, then one small experiment. Do not write opportunities as disguised solutions.
- Prioritization. Pick the method to fit the data available. We have no internal data, so use a simple Impact, Confidence, Effort score, and say that RICE is not possible without reach numbers.
- Small tests (Product Analyst). Choose the cheapest test that answers the riskiest assumption before asking for engineering time.
- Orchestration (Product Lead). Parallel agents with clear boundaries, handoffs and human review points. Matches our gates.

Not adopted:
- The repo's one-question-at-a-time coaching flow with Bulent. Agents put questions to the Product Lead. Only the Product Lead brings questions to Bulent, and only at gates.
- Market sizing, roadmap, PRD, EOL and leadership skills. Out of scope for a 2-3 hour case.

Journey audit layout: use the stages Awareness, Consideration, Decision, Service from customer-journey-map as rows, with actions, touchpoints, feeling and friction per entry point. Keep it to one table per site.

## Hired 2026-11-07 for the ideation brainstorm
- Growth / CRM Marketer: lifecycle messaging, campaigns, channels, İYS consent. Owns awareness ideas.
- Supply and Marketplace Ops: pro side, credits, quote quality, pro motivation, cancellations. Owns supply ideas and lead-quality guardrails.
- Event Industry Expert: how Turkish weddings, kına, nişan, sünnet and birthdays are planned and bought. Reality check on timing and bundles.
- Engineer (feasibility): what 1 backend + 1 frontend can build in weeks; dependencies, data needed.
- Customer Panel (simulated): personas reacting to ideas. Output is simulated, never evidence; used only to find questions for real interviews.
Brainstorm format: round 1 ideas per role in parallel; round 2 cross-review of the merged list; Product Lead converges.
