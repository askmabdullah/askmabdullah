# Phase 2: Offer design (model/offers.md)

Author: Phase 2 offer designer. Date: 2026-10-20. Inputs: BRIEF sections 1 to 8, phase1-summary.md, all 22 track files, pricing-map.md, competitors.md. Cross-checked against model/risk.md for guarantee and refund terms.
Searches used: 0 of the 3 allowed. Nothing in this file comes from outside the Phase 1 evidence.

Pointer key: [T17 J9] = track 17, buyer post J9. [T21 #7] = track 21, key finding 7. [A] = my assumption, not evidence. "Seller price" = asking price on a vendor page. "Buyer budget" = a stated budget on a job post, not a payment.

## 0. Read this first

1. No source shows a buyer paying $1,500 or more to rescue an AI-built app (gate 1 is still unproven) [phase1-summary, T17 #1, T22 #1]. Every price below is anchored on seller asking prices and a handful of buyer budgets. The offers are built so the first 10 audits tell us whether the prices hold.
2. Buyer budgets for confirmed AI-built apps run $20 to $1,250, with two $2,000 posts (both 9+ months old, by title only) [T17 #2, T21 #1]. Two Supabase hardening posts at $1,500 and $2,500 do not say "AI-built" [T17 J9, J10]. So the sprint prices below sit at or above the top of what buyers posted. This is the main commercial risk and the design answers it with: an audit credited in full, a founding-client price, and an objective guarantee.
3. Delivery cost is not the risk. A one-week sprint costs us $350 at salary and about $735 fully loaded. The risks are the cost of getting a client, an overrun on a bad codebase, and refunds [T19 appendix].
4. Retainer conversion has no evidence at all. Two rounds found zero buyer voices on keeping a developer after a fix [T14 #8, T20 #11]. Maintenance is priced and designed here, but the model should not depend on it.

## 1. Cost model (used for every margin below)

| item | value | basis |
|---|---|---|
| Engineer salary | $1,050 per month | BRIEF section 1 ($1,000 to $1,100, midpoint) |
| Engineer hour | $1,050 / 173.3 h = $6.06 | arithmetic |
| Engineer week (40 h) | $242 | arithmetic |
| Lead reviewer hour | $13.85 | [A] lead costs $2,400 per month; no evidence found |
| Lead review, 8 h | $111 | arithmetic |
| One engineer-week plus 8 h lead | $242 + $111 = $353 | matches the brief's $300 to $400 |
| Loaded multiplier | 1.75 on labour (1.4 for a dedicated engineer) | [A] about 57% billable time, plus AI tool seats, hardware, management. 1.4 = about 71% billable |
| Payment fees | 3.5% of price | [A] card; bank or Wise is lower |
| Tooling per job | $15 audit, $30 week, $60 two weeks | [A] scanners, test projects, monitoring |
| Expected-case overrun | +20% labour | [A] no overrun data exists in the evidence [T19 #12] |
| Expected-case refunds | 5% of price | [A] arithmetic only, no refund data [T16 #11, risk.md] |
| Stress case | labour x2 (a second engineer-week unpaid), 10% refund | [A] |

Three margins are shown for each offer: salary-only (what the brief implies), loaded base, and stress. "Expected" is loaded plus the overrun and refund allowances.

## 2. The offer ladder at a glance

Working names only (brand is decided in model/brand.md).

- A. Launch-Readiness Audit: $495, paid, 100% credited. Entry door and filter.
- B. Hardening Week: $2,500 fixed, one week. Security, data, payments and deploy checklist with pass/fail tests.
- C. Finish-and-Launch Sprint: $4,500 fixed, two weeks. The hardening checklist plus up to 5 named features, launched.
- Add-on E. Cloud Exit (Lovable Cloud to your own Supabase): $1,500 with B or C, $2,000 alone.
- Separate path R. Rebuild quote: written fixed quote after the audit, priced per engineer-week. Not marketed in the first 30 days.
- D. Care plans: Care $450 per month, Support $1,500 per month, Dedicated engineer $3,800 per month.

Rule that holds the ladder together: no sprint is sold without a paid audit finished in the last 14 days. This is how scope gets fixed before money moves (every serious seller does audit first [T19 appendix, T8 #3]), and it is how the Launch Scope List for C gets written.

## 3. Offer A: Launch-Readiness Audit

**Price: $495 fixed** (range $350 to $750; large-app tier $950 for more than 30k lines, more than one repo, or more than 25 tables).
**Unit:** fixed, one report, 3 business days from access.

### Who it is for
- Buyer type 1, the solo founder about to launch or sell, on Supabase plus Stripe, who posts $1,500 to $2,500 hardening jobs [T17 J9, J10]. Most likely first buyer.
- Buyer type 2, a founder with an investor-ready Lovable or Bolt prototype who needs to know what "production" costs [T22 R1, R2].
- Buyer type 3, a technical founder or small team that wants an independent written audit and no rewrite pitch [T22 R3: Cleveroad review, "specifics", "no pitch for a rewrite"].
- Not for: the $20 to $300 Fiverr and Upwork "fix my favicon" crowd [T7, T17 #2, T21 #9]. The price is meant to screen them out.

### What is included
- Read-only repo access and a schema export (or read-only Supabase access). We do not touch production.
- Report of about 12 to 20 pages with file-level findings, ranked Critical, High, Medium. Each finding has a fix-effort estimate in hours. This copies what a buyer praised in the Cleveroad review ("specific numbers and specific files", fix list in priority order) [T22 R3].
- Coverage list (the standard checklist from [T11 6b], [T19 5b]): secrets in code and history, RLS and ownership, auth and roles, Stripe and webhooks, error handling and validation, staging versus production, tests and CI, deploy path.
- A written rescue-or-rebuild verdict with the criteria shown.
- A Launch Scope List (what "launch-ready" means for this app) and a fixed quote for B or C, or a rebuild quote, or "do not buy a sprint from us".
- A 60-minute readout call.
- One free re-verify of the Critical findings within 30 days (Valletta does the same [T16 seller quotes]). About 2 hours of our time.
- 100% credit against B, C, E or a rebuild if signed within 14 days.

### What is excluded (scope-creep stops)
- No code changes and no fixes, including "just this one Critical bug". The only exception is written key-rotation advice for an exposed secret.
- No penetration test, no active exploitation, no testing of the live app beyond what the client authorises in writing. No security certificate or "audit passed" language (risk.md section on disclaimers).
- No compliance attestation (GDPR, SOC 2, PCI, HIPAA).
- No review of design, UX, copy, SEO or marketing.
- No performance or load testing beyond flagging obvious N+1 queries and huge components.
- No second audit after the client changes the code, beyond the one re-verify of Critical findings.
- Large apps above the limits go to the $950 tier or a quote.
- Apps in the excluded categories (gambling, interest lending, adult, alcohol, tobacco and vaping) are declined before payment. Crypto is flagged for a manual decision.

### Deliverables
Report (PDF), findings spreadsheet with hours, Launch Scope List, fixed quote, readout recording.

### Guarantee
Delivery-date guarantee: if the report is more than 5 business days late, the audit fee is refunded (matches risk.md). No refund once the report is delivered. We state "no sprint needed" in the report when that is true.

### Payment terms
100% upfront at booking. Card is fine at this size. The credit is a line on the later invoice, not a refund.

### Why $495: the evidence
- 14 vendor audit prices found in Phase 1 (my count): $49 (AfterBuild), $199 (Valletta, about 80 checks; kodingklouds), $297 (TechPotions) [UNVERIFIED attribution: $297 is in T20 section 5, not in the tracks cited at the end of this line], $299 (Vibe Code Rescue, credited), $350 (Flow Lab), $399 (MobiDev; Arkroot at EUR 399), $497 (Base44Devs), $900 (Relevant), $1,500 (Upwork 72-hour audit, credited; Soatech EUR 1,500; Frenchy low end), $4,950 (TopDevz, credited). Median is about $400. [T16 #6, #1; T19 #13; T21 #7; T22 #6; T8 #4; T17 #7]
- Buyer side, only two audit-specific numbers: $150 for a Base44 security audit (Upwork, 2026-04-08) and a $1,000 audit step inside a $1,500 job (J10) [T21 sec 3, T17 J10]. $495 sits between them.
- Why not free: three sellers give free audits (MetaCTO 48 hours, Agence Scroll, McKelvey 20 minutes) [T20 #19, T19 #6]. A free audit costs us about $183 of salary-only labour (16 engineer hours plus 5 lead hours plus fees) and attracts the $20 crowd. We can still offer a free 15-minute fit call and a 30-minute "does this qualify" glance with no written output. The paid audit is the first deliverable.
- Why not $199 or less: this is the Valletta and AfterBuild floor. It does not cover 5 senior hours plus a readout, and a $199 anchor drags the sprint price down. At $199 the audit loses money loaded.
- Why not $1,500: an audit-then-sprint at $1,500 plus $2,500 puts the minimum spend at $4,000, above every confirmed AI-built buyer budget [T17 #2]. That is the Upwork seller shape ($1,500 audit credited to $4,000 to $8,000) and it has no evidence of closing [T16 #1].
- Why credited in full: seen at 5 vendors (Vibe Code Rescue, Upwork $1,500 seller, Rocking Tech, TopDevz, kodingklouds) [T16 #1, T19 #13, T21 #7]. It also answers the Lahore trust gap with a small paid first step, which buyers and vendors recommend [T15 sec 6].
- Tyre-kicker filter: no conversion or tyre-kicker data exists for any price [T16 #11]. The filter is an assumption [A]: a payment above the impulse range ($200 to $300) removes people who only want free advice.

### Margin
| case | cost | gross margin |
|---|---|---|
| Salary-only plus fees (16 eng h, 5 lead h) | $183 | 63% |
| Loaded base | $323 | 35% |
| Expected (+20% hours) | about $381 | about 23% |
| Stress (32 eng h) | about $613 | about -24% |

The audit is a qualification product, not a profit product. Hard cap: 20 engineer hours; anything larger triggers the $950 tier before work starts. When the client converts, the audit work is reused in the sprint, so the true cost of the audit-first bundle is lower (see section 8).

### Evidence thin
No audit-to-project conversion rate exists anywhere [T16 #11]. The 40% conversion used later is [A]. Review of 3 Clutch pages would not change the audit price but would help gate 1 (T22).

## 4. Offer B: Hardening Week (one-week fixed-scope sprint)

**Price: $2,500 fixed** (range $1,800 to $3,000). **Founding price $1,950 for the first 3 clients** in return for a named case study or quote.
**Unit:** fixed-scope package, 5 working days. Weekly equivalent $2,500. Not billed by the week or the hour.

### Who it is for
- Buyer type 1 (J9): solo founder with a pre-launch or just-launched marketplace or SaaS on Supabase plus Stripe; scope in the post is server-side validation, Stripe production audit, webhook checks, email migration, and the budget was $2,500 [T17 J9].
- Buyer type 2: non-technical founder with paying users on Lovable, Replit, Bolt or Base44 whose prototype now holds customer data [T17 #6, T19 #4].
- Buyer from the audit who needs the security-and-data core done before anything else, whatever else is wrong.
- Not for: someone who wants new features (go to C), someone whose audit verdict is "rebuild" (go to R), or anyone who will keep prompting the platform during the week.

### What is included (Schedule A default list; each item has a written pass/fail test)
1. Repo and environments: client-owned GitHub repo, protected main branch, separate staging and production databases, a verified backup, CI that runs lint, types and build.
2. Secrets: scan of code and git history, rotation of exposed keys (OpenAI, Stripe, Supabase service role), keys moved server-side.
3. RLS and ownership: policies enabled and rewritten for up to 25 tables, storage policies, ownership checks on object ids, tested with two test users and an anonymous user.
4. Auth: server-side route guards, roles not editable by the user, redirect URLs and email templates on the production domain, password reset tested.
5. Payments: Stripe live-mode checklist, webhook signature verification, idempotency, entitlements set from the webhook, up to 3 prices or plans.
6. Validation and errors: server-side validation and error handling on up to 10 edge functions or API routes.
7. Safety net: smoke tests on the top 5 user flows, run in CI.
8. Deploy: production deploy on client-owned hosting and domain, SSL, monitoring and uptime check, rollback note.
9. Handover: recorded 45-minute walkthrough, a runbook on how to change the app safely with Lovable or Cursor, an open-items backlog.

The list follows the draft checklist in [T11 6b] and the core that 6 of 9 independent sellers name (secrets, access control, auth, payments, error handling) plus Wiz's four patterns [T19 #4, 5b]. Fix-time evidence is thin: "2 to 4 hours" for the five most common patterns and "about 2 hours" for a key exposure, both vendor claims [T19 #1]. 40 engineer hours is therefore [A].

### What is excluded (scope-creep stops)
- No new features, no UI change, no redesign, no copy.
- No data model redesign. If the model cannot represent the domain, that is a rebuild signal found in the audit, not a sprint item [T19 #5].
- Limits: more than 25 tables, 10 functions, 30k lines, one repo or one payment provider become a change order or a different offer.
- No mobile build or app store submission.
- No Lovable Cloud migration (add-on E).
- No performance tuning beyond fixing the worst 3 queries named in the audit.
- No third-party account fixes (Twilio registration, email deliverability, Stripe account review).
- No compliance attestation, no penetration test, no "secure" statement. Wording is "hardened against the listed risks" (risk.md).
- Code freeze: the client does not prompt Lovable, Bolt, Replit or Cursor on the main branch during the week. Edits go on a branch we review. This addresses the plausible re-prompting scope creep, whose evidence is weak [T19 #7].
- Change orders at $500 per engineer-day ($2,500 / 5 days). Anything not in Schedule A goes to the backlog.
- Support after day 5 is the 30-day warranty only.
- Excluded business categories (see A).

### Deliverables
Hardened app live on client infrastructure, signed Schedule A with every test marked pass or fail, change log, runbook, recorded walkthrough, backlog, 30-day warranty note.

### Guarantee
Acceptance-test guarantee (section 7). 30-day warranty on accepted in-scope fixes.

### Payment terms
Total $2,500. The $495 audit is credited, leaving $2,005: $1,000 at kickoff, $1,005 on acceptance (acceptance window 3 business days, silent acceptance after that). Bank transfer or Wise preferred over card for the balance (risk.md chargeback table). Founding price $1,950 leaves $1,455: $730 and $725.

### Evidence behind $2,500
- Seller prices for the same unit: Teyrex from $1,400, Base44Devs $1,500, Vibe Code Rescue $1,500, AfterBuild $1,999 (5 to 7 days), Arkroot EUR 1,999, GainCafe from $2,500 (3 to 7 days), Forasoft $2,500 for one week, Upwork 2 to 3 week sprint $4,000 to $8,000 [T21 #7, #8, T8 #4, T19 #13, T16 #2]. These are "from" prices. Median of the 11 fixed-rescue "from" prices is $2,500 [T21 numbers].
- Buyer budgets at or above $1,500: $1,500 (J10), $2,000 and $2,000 (Twilio plus Stripe backend for a Lovable app; Base44 launch and QA) and $2,500 (J9) [T17, T21 #1]. That is a thin base: 4 posts, 2 of them old.
- Audit-first client total stays at $2,500 (audit credited), which equals the one $2,500 buyer budget. After the credit the cash ask at the sprint step is $2,005, close to the $2,000 posts.
- The unit: most budgeted buyer posts in T17 section 3A are fixed-price (J1 to J11 are Upwork "Fixed Price" titles; hourly only on J16 and possibly J13 and J18). Buyers who were burned by credit loops [T1 #2, T17 #8] fear open-ended billing. So the offer is a fixed package, not a weekly subscription like Wavect or Forasoft.

### Price decision: $2,000 versus $2,500 versus others
Expected-case figures from section 1 (labour 40 h engineer, 8 h lead):

| price | expected cost | expected gross margin | 30% CAC cap | profit after a capped CAC |
|---|---|---|---|---|
| $1,500 | $899 | 40% | $450 | $151 |
| $2,000 | $941 | 53% | $600 | $459 |
| $2,500 | $984 | 61% | $750 | $766 |
| $3,000 | $1,026 | 66% | $900 | $1,074 |

Reasons to pick $2,500: (1) it is the median seller "from" price, (2) it raises the gate-2 cap from $600 to $750 and profit after a capped CAC by about two thirds ($459 to $766), (3) it absorbs a 2x overrun and a refund and still earns about 36% (stress case), (4) at $2,000 we would sit in the middle of at least 8 small Western studios already listing $1,400 to $2,500 [T21 #7, #8]. Price will not set a Lahore vendor apart from them; proof, acceptance tests and the warranty have to [T21 sec 6]. So the lower price buys little. Reasons to hold back: it is above every confirmed AI-built buyer budget except the two $2,000 posts. That is why the first three clients get $1,950, and why the plan has a price-down trigger (section 10): if more than 60% of audited leads accept the audit but reject the sprint on price, list price drops to $2,000.
At $1,950 the expected margin is about 52%: still fine.

### Margin
| case | cost | gross margin |
|---|---|---|
| Salary-only plus fees | $441 | 82% |
| Loaded base | $735 | 71% |
| Expected (+20% hours, 5% refund) | $984 | 61% |
| Stress (2x hours, 10% refund) | $1,603 | 36% |

### Evidence thin
Fix hours (40 engineer hours), overrun rate, refund rate and sprint conversion are all [A]. No sprint price has a named buyer paying it.

## 5. Offer C: Finish-and-Launch Sprint (two weeks)

**Price: $4,500 fixed** (range $3,800 to $6,000). **Founding price $3,900 for the first 2 clients.**
**Unit:** fixed-scope package, 10 working days. Weekly equivalent $2,250 (a 10% discount on two B weeks for the longer commitment and shared ramp-up).

### The boundary: "launch-ready for a defined feature list", not "finish everything"
Why the boundary exists: sellers who sell finishing charge $15,000 to $50,000 over 4 to 8 weeks (McKelvey $25K to $50K, 4 to 8 weeks; freelance finish and harden $5,000 to $15,000; agency "Lovable to production" $8,000 to $25,000; Red Leg Dev 2 to 6 weeks) [T19 #2, #13, T16 #8]. The best public hours anchor is about 100 hours of work to take a simple app from prototype to working product [T19 #3]. A $2,000 "finish my app" promise would lose money or collapse into a rebuild. So C is defined by a list, not a feeling.

Launch-ready means all five are true at handover:
1. The full B checklist (compressed into the first 3 to 4 days) passes its tests.
2. The Launch Scope List passes acceptance: up to 5 feature units, each already partly built in the existing app and each written in the audit as a user story with a pass/fail test. A feature unit is one flow of up to about 2 screens, up to 3 tables and one RLS policy set, about 1 to 1.5 engineer days.
3. One payment flow works end to end in live mode.
4. One outside integration works in production (email, SMS or one API).
5. The app is deployed on client-owned hosting with a domain, a staging site, monitoring and a rollback note.

Not part of "launch-ready": everything not on the list. The list is frozen at kickoff.

### Who it is for
- Buyer type 2 and 3: founders with a Lovable or Base44 front end that works and a backend that does not. The two $2,000 posts are this shape: "Twilio and Stripe Integration for Lovable App" (UI done, backend must work) and "Base44 QA and Launch" (estimated 2 to 4 weeks) [T21 #1, sec 3].
- Founder with an investor-ready prototype who needs production (GeekyAnts review shape, but at a fraction of its $10,000 profile floor) [T22 R1].
- Not for: "build my whole product", more than 5 feature units, apps over about 30k lines, anything the audit calls a rebuild.

### What is included
Everything in B, plus the 5 feature units, one payment flow, one integration, a staging site, one mid-sprint demo (end of week 1), a launch-day support window of 2 hours, and the 30-day warranty. Staffing: one engineer for 10 days, a second engineer for 5 days, lead review 16 hours.

### What is excluded (scope-creep stops)
- Everything excluded from B.
- Any feature not on the Launch Scope List. New ideas go to the backlog or a change order at $500 per engineer-day, and only if the schedule allows. The list is not edited after kickoff.
- More than 5 feature units. The audit prices a second sprint instead (back-to-back C sprints, maximum 3, each re-scoped). This is the "finish programme" for bigger apps; at $2,250 a week it is about $9,000 to $18,000 for 4 to 8 weeks, below sellers' $15,000 to $50,000, so it should not be advertised in the first 30 days.
- Native mobile apps and app store submission.
- Admin panels built from scratch, multi-tenant or organisation models, role systems beyond two roles.
- AI or RAG features built from scratch (fixing an existing LLM call is fine).
- Design work, branding, copy, content, SEO or a marketing site.
- Bulk data entry, migration of more than the add-on E limits, data cleaning.
- Load or scale guarantees. We test to the user count in the Launch Scope List only.

### Deliverables
Production app, signed Schedule A with the Launch Scope List marked pass or fail, change log, runbook, recorded walkthrough and launch checklist, backlog, 30-day warranty.

### Guarantee and payment
Acceptance-test guarantee, itemised per feature unit and per checklist group. Total $4,500; audit credit $495 leaves $4,005, paid 40% at kickoff ($1,600), 30% at the end of week 1 after the demo ($1,200), 30% on acceptance ($1,205). Founding price: $3,900 leaves $3,405 in the same split.

### Evidence behind $4,500
- Seller two-to-three week sprints: Upwork $4,000 to $8,000 ($7,000 typical), Triple Minds from $4,000 for 2 to 4 weeks, a two-week sprint from $6,000, Frenchy stabilisation $5,000 to $15,000, Forasoft $2,500 per week [T16 #2, T21 #7, T19 #13, T17 #7, T8 #4].
- Buyer budgets: two $2,000 posts for the same shape [T21 #1], so $4,500 is 2.25 times them. This is the largest price-gap risk in the ladder. If the first 10 audits show buyers scoping C-shaped work at about $2,000, then C is either sold as a smaller scope or dropped.
- Weekly equivalent $2,250 is below B's $2,500 and inside the $2,000 to $2,500 per week band of studios.

### Margin
Labour: 100 engineer hours ($606) plus 16 lead hours ($222) = $827.
| case | cost | gross margin |
|---|---|---|
| Salary-only plus fees | $985 | 78% |
| Loaded base | $1,665 | 63% |
| Expected | $2,180 | 52% |
| Stress | $3,563 | 21% |
At the founding price $3,900 the expected margin is about 45%.

### Evidence thin
No source gives hours for finishing work on a small app, and no source says how many "feature units" fit in two weeks. 5 units in about 8 engineer-days is [A]. The first two C sprints are the test.

## 6. Add-on E and path R

### E. Cloud Exit: Lovable Cloud to your own Supabase
**Price: $1,500 fixed with B or C; $2,000 stand-alone** (range $1,200 to $2,500). **Unit:** fixed, 3 to 5 working days.

Why it is a product: Lovable's own self-hosting guide needs a manual job (schema, data, auth users, storage, a password reset email to every user). Supabase says no automated transfer exists and a Cloud project cannot be switched to an external Supabase connection. No platform automates it end to end [T20 #4]. Lovable Cloud has been on by default since 2025-09-29, so there are about 13 months of projects that sit on it [T20 #3]. A free exporter and a community skill claim to help but are unverified [T20 #4].

Included: new client-owned Supabase project; schema and RLS replicated and tested; data copy and row-count checks; auth users migrated with a forced password reset; storage bucket copy; up to 10 edge functions redeployed; secrets and env rewired; one rehearsal on a copy; a cutover window of up to 2 hours; a rollback plan; a short end-user email template. Limits: up to 25 tables, 1 GB database, 5 GB storage, 3 auth providers.

Excluded: sending the user emails (the client sends them), schema redesign, data cleaning, rewiring services other than Supabase, replacing the platform AI gateway (up to 3 LLM calls swapped to a client-owned key is included, more is a change order), downtime outside the agreed window, and any claim of zero downtime.

Guarantee: acceptance tests (row counts match, a test user logs in after reset, RLS tests pass, the app runs against the client's project). A backup is taken first. Payment: 50% at start, 50% after cutover plus 7 days.

Evidence for the price: Base44Devs migrations $6,000 / $12,000 / $25,000+; Escape Base44 from $2,500; Upwork Replit to Next.js and Vercel $500 for 3 to 5 days; Upwork "Lovable Cloud to Supabase Migration" $30 (floor); seller claims that leaving a platform "runs $2,000 to $15,000" [T21 #7, T22 #14, T7 sec 3, T21 sec 3]. $1,500 sits in the gap between the $30 to $500 floor and the $2,500+ studio prices. Hours (32 engineer plus 6 lead) are [A]. Salary-only cost $329 (78% margin); loaded $557 (63%); stress $1,192 (21%).
Evidence thin: no buyer asking for this at a stated budget except the $30 post; the lever is that the audit will surface it.

### R. Rebuild quote (separate path)
Triggers (the full triage rule is in model/delivery.md; commercial summary here): the audit marks the data model as unable to represent the domain; the fix estimate for B plus the Launch Scope List is more than 2 weeks; or refactor cost is 60% or more of rewrite cost (a vendor heuristic, not research) [T19 #5].
Terms: written fixed quote within 5 business days of the audit; priced at $2,250 to $2,500 per engineer-week of the team (typical 4 to 8 weeks, about $9,000 to $20,000), plus 15% contingency stated openly; audit fee credited; milestone payments (30% start, 40% mid, 30% acceptance); 30-day warranty. Anchors: McKelvey $40K 6-week rebuild replacing a $150K quote, agency Lovable-to-production $8,000 to $25,000, Base44Devs $6,000 to $25,000+, Upwork $4,000 to $8,000 [T19 #13, T16 #8, T21 #7].
Not marketed in the first 30 days. It exists so that we never sell a one-week sprint to an app that needs a rebuild. HN practitioners report at least two jobs ending in rewrites [T19 #5, sec 4].

## 7. Guarantee: recommendation

**Recommend one: the Acceptance-Test Guarantee, with a 30-day fix warranty as its tail.**

How it works: every sprint item in Schedule A has a written pass/fail test and a fee share (for example RLS 20%, secrets 10%, payments 20%). After delivery we get one fix round. If an item still fails its test, that item's fee share is refunded. Total refund can never exceed the sprint fee. After acceptance, in-scope fixes that regress in 30 days are repaired free.

Evidence compared:
| shape | where seen | verdict |
|---|---|---|
| Last-week refund "if we didn't blow you away" | Wavect, weekly billing, no price seen [T16 #3, T20 #19] | Do not copy. "Blow you away" is subjective, so the likely route to a $2,000 dispute with a budget-tight, already burned buyer base (risk.md). |
| Two-week warranty | Slopfix [T8 #5, T19 #9]; aibrify 90-day free repair [T16 #4] | Cheap for us (rework hours at about $6 each) but alone it does not answer "will it work?" Keep as the tail. |
| Pay only if fixed | aibrify, tickets of $100 and $300 [T16 #4] | Works at tiny tickets. At $2,500 it hands the client a free option on a bad-codebase overrun. The itemised version captures the idea safely. |
| "100% success guarantee" | GainCafe [T21 #7] | Vague marketing. Do not copy. |

Why this one: it is objective, it fits a non-technical buyer who can read a pass/fail list, it answers the Lahore trust gap [T15 #6, T20 #16 to #18], and it limits the loss to the failed item. Cost: expected refund about 5% of price ($125 on B) in the model, 10% in stress. The same shape is in model/risk.md section 1.10, so legal and offer agree.
Evidence thin: no source reports refund or dispute rates [T16 #11, risk.md]. Test in the first 30 days.

## 8. Offer D: Care and maintenance

**Three tiers. Month-to-month except Dedicated.** Sold only to clients whose app we hardened (A with fixes, B, C), because maintainers commonly refuse code they did not build ("limited to projects we have built ONLY") and that is also how we limit unknown-code risk [T20 #14].

| tier | price per month | range | what it is |
|---|---|---|---|
| D1 Care | $450 | $300 to $600 | monitoring, backup checks, dependency and Supabase advisor check, 4 hours of small fixes |
| D2 Support | $1,500 | $1,000 to $2,000 | 15 hours a month, one request at a time, 1 business day response, monthly 30-minute call, regression tests kept green |
| D3 Dedicated engineer | $3,800 | $3,000 to $4,500 | one named engineer, 160 hours, lead review 4 hours a month included, 3-month minimum |

### D1 Care: $450
Included: uptime and error monitoring, a weekly backup restore check, a monthly dependency and Supabase advisor review, 4 hours of fixes or small changes, next-business-day response, a one-page monthly report. Unused hours do not roll over.
Excluded: new features, anything over 4 hours (becomes a quote or the Support tier), outage or incident response out of hours, platform outages, work on code others changed without a review, load or security re-audits.
Payment: monthly in advance by card or direct debit; cancel with 30 days' notice; no setup fee.
Evidence: care plan band $300 to $600 is my inference [T14 sec 6]; small SaaS maintenance $500 to $3,000, "Simple Apps" $1,000 to $3,000, Paris SME EUR 500 to 2,500, cleanup guide $500 to $2,000, Clientvenue GBP 500 to 3,000, website plans $50 to $500 [T14 #1, T20 #12]. A Lovable builder's own stack costs $91 to $131 a month [T14 #7], so $450 is 3.4 to 5 times their tool bill, which is a large step.
The $120 per month floor: one live café-app owner posted a flat $120 a month for on-call Supabase and RLS fixes [T17 J11]. One post, but it is the only buyer-side maintenance price. Reading: tiny live apps budget $100 to $200. We should not price to it. An open-ended on-call at $120 is uncapped hours. If a client leaves over price, offer a hidden "Care Lite" at $190 (monitoring, backup check, 1 hour) as a save, never as a headline. Labour cost for Lite is about $30 to $60 a month so it is profitable at salary cost [A].
Margin: salary-only 87%, loaded 75%, expected 66%, stress (hours x2) 58%.

### D2 Support: $1,500
Included: a pool of 15 hours a month; a single queue handled one request at a time (the "one request at a time" flat queue that Designjoy sells, $4,995 for design [T14 #3]); a monthly planning call; regression tests maintained; one month of rollover capped at 15 hours.
Excluded: new product builds (a C sprint instead), 24/7 cover, work beyond the pool without approval (extra hours at $120 each; market rate $100 to $200 an hour [T10 #5, #6; T19 #13]), changes made by the client's own AI tool unless on a branch we review.
Payment: monthly in advance; 30 days' notice.
Evidence: McKelvey optional retainer $1,500 to $3,000; Frenchy $2,000 to $6,000 with SLA; Australian shop $4,500 plus GST; scopenine $500 to $2,000; Indianic $5,000 to $25,000 (3-month minimum); Upwork's own guide $3,000 to $10,000 for Lovable support [T20 #12, T21 #15 and sec 5]. $1,500 is the low end of those, an effective $100 per hour, equal to the "maintenance $100 an hour" comment [T10 #5].
Margin: salary-only 88%, loaded 79%, expected 71%, stress 64%.

### D3 Dedicated engineer: $3,800
Included: one named engineer, about 160 hours a month, 4 hours of overlap with the client's day, daily written update, lead review 4 hours a month, replacement within 5 working days if needed.
Excluded: a second engineer (priced separately), on-call out of hours, management of the client's other contractors, equipment or software licences, hiring or recruiting.
Payment: monthly in advance; 3-month minimum, then 30 days' notice (3-month minimums appear in the market, e.g. Indianic; London retainers 6 to 12 months for a 5 to 15% discount [T14 #1, T20 #12]).
Evidence: Pakistan direct-contractor dedicated developer guides $4,000 to $6,400 mid and $5,600 to $8,000 senior, agencies mark up 50 to 100% [T20 #15]; South Asia mid-level React $3,040 to $4,960 (Secondtalent, 2026-09) [T14 #5]; India $1,500 to $5,000 and $4,500 to $8,500 [T20 #15]; our cost is about $1,050 [BRIEF]. $3,800 undercuts the Pakistan guides' $4,000 floor and sits at the middle of the South Asia band; our proof gap argues against pricing above it. Few buyers will pay this: fractional CTO ($5,000 to $25,000) and Designjoy-style buyers are funded or have revenue [T14 #3, #6].
Margin: salary-only 70% (labour $1,025 including lead), loaded 57%, expected 45%, stress 19%. The thin stress margin comes from fixed 160 hours: there is no overrun lever, so the risk is a poor engineer fit, not hours.

### Conversion and value (all assumptions)
- No source reports a rescue-to-retainer rate. Two rounds found no buyer voice on keeping a developer [T14 #8, #11; T20 #11]. Only seller claims ("many clients choose to keep us") and a non-code rule of thumb of 25 to 40% attach and 70 to 85% 90-day retention [T20 #13].
- Planning assumption [A]: 15% of sprint clients buy Care and stay 6 months. Expected recurring value per sprint client = 0.15 x $450 x 6 = $405 revenue, about $270 margin. Upside case at a 33% attach: $891. This is 16% of one B sprint at 15% attach. Do not build the model on it.
- Argument for recurring: AI fixes re-break things; the regression problem is a seller's argument for retainers [T14 #9]. Argument against: clients now patch small bugs with AI and call a developer only for hard problems [T14 #10].

## 9. One-table comparison

| | A Audit | B Hardening Week | C Finish-and-Launch | E Cloud Exit | D1 Care | D2 Support | D3 Dedicated |
|---|---|---|---|---|---|---|---|
| Price (range) | $495 ($350 to $750) | $2,500 ($1,800 to $3,000); founding $1,950 | $4,500 ($3,800 to $6,000); founding $3,900 | $1,500 with B or C; $2,000 alone ($1,200 to $2,500) | $450/mo ($300 to $600) | $1,500/mo ($1,000 to $2,000) | $3,800/mo ($3,000 to $4,500) |
| Unit | Fixed report | Fixed package, 5 days | Fixed package, 10 days | Fixed, 3 to 5 days | Monthly, 4 h | Monthly, 15 h pool | Monthly, 160 h |
| Buyer | Pre-launch or pre-sale founder; technical founder wanting a no-pitch audit | Founder with paying users or pre-launch on Supabase plus Stripe | Founder with working front end, broken backend, defined launch list | Lovable Cloud app owner who wants ownership | Hardened-app owner with live users | Revenue-earning app owner | Funded or revenue-earning team |
| Main evidence | J9, J10, R3, 14 audit prices | J9, J10, $2,000 posts, 11 studio "from" prices | $2,000 posts, Upwork $4,000 to $8,000, Triple Minds $4K | T20 #4, Base44Devs, Escape Base44 | T14, T17 J11 | T14, T20 #12 | T14 #5, T20 #15 |
| Evidence grade | Moderate (seller), weak (buyer) | Weak to moderate | Weak | Weak to moderate (docs strong, price weak) | Weak | Weak | Weak |
| Gross margin, salary-only / loaded / expected / stress | 63 / 35 / 23 / -24% | 82 / 71 / 61 / 36% | 78 / 63 / 52 / 21% | 78 / 63 / 51 / 21% | 87 / 75 / 66 / 58% | 88 / 79 / 71 / 64% | 70 / 57 / 45 / 19% |
| Guarantee | Delivery date | Acceptance-test refund + 30-day warranty | Same, itemised per feature | Acceptance tests + backup first | Cancel any month | Cancel any month | 3-month minimum, then 30 days; engineer swap |
| Payment | 100% upfront | $1,000 start, balance on acceptance (after $495 credit) | 40 / 30 / 30 (after credit) | 50 / 50 | Monthly in advance | Monthly in advance | Monthly in advance |
| Main risk | Free competitors, no conversion data | Price above buyer budgets; overrun | Scope creep; price gap to $2,000 posts | Cutover data issues | No attach data | No attach data | Thin stress margin; few buyers |

Audit-first bundle (A credited into B, total $2,500): salary-only cost $183 + $441 - $17 duplicate fee = about $607 (76% margin); loaded base about $1,041 (58%); expected about $1,348 (46%); stress about $2,200 (12%). The stress case is thin: that is why the audit is capped at 20 engineer hours and the sprint at the Schedule A limits.

Blended economics per 10 audits sold at an assumed 40% audit-to-B conversion [A]: revenue 6 x $495 + 4 x $2,500 = $12,970; loaded cost 10 x $323 + 4 x $735 = $6,170; gross margin 52%. At the brief's 30% rule, the maximum cost per paid audit is 0.30 x ($12,970 / 10) = about $390. At 25% conversion it is about $300. The channel model in model/channels.md should be tested against these two caps.

## 10. What to test first in the 30-day plan

Order matters; each step needs the one before it.

1. Days 1 to 5: freeze the audit report template, the Schedule A checklist with tests (from [T11 6b]), the contract (from risk.md) and the fit-call script. Run the audit process on a Wanile demo app and time it. Goal: confirm 16 engineer hours or find the real number.
2. Days 3 to 30: sell the audit, not the sprint. Target 10 paid audits at $495 from the cheapest channels first (channel order is in model/channels.md). Qualify out anyone with a budget under $1,000 on the fit call. Ask every lead "what would you pay for the fix?" and log the number: this fills the buyer-budget evidence gap (gate 1).
3. Days 10 to 30: quote B at $2,500 to the first 5 audited leads; the first 3 who accept get $1,950 plus a case-study right. Log every objection and counter-offer.
4. Days 15 to 40: deliver the first two B sprints. Log engineer hours per Schedule A item, first-pass acceptance by item, change orders, client messages and refund requests.
5. Day 30 onward: offer Care $450 at the sprint handover. Log take-up.
6. Opportunistically: offer E when the audit flags Lovable Cloud. Quote C only when the Launch Scope List has 5 units or fewer. Quote R when the verdict is "rebuild". Log what share of audits land in each outcome.

What not to test in the first 30 days: Support, Dedicated, the multi-sprint finish programme, any ad spend on B or C before the audit funnel has data.

## 11. Metrics that prove or kill each offer

Sample sizes are tiny. Rules below are decision aids, not statistics. Revisit at 10 audits.

| offer | prove (keep, scale) | adjust | kill or reshape |
|---|---|---|---|
| A Audit | 8 or more paid audits in 30 days; fit call to paid audit 20% or better; audit to sprint 30% or better; average audit hours 20 or less; 0 refund requests | Fit call to paid audit under 15% from leads who passed the budget screen: test $295. Audit to sprint under 20% after 10 audits: the audit is a stand-alone product at $750, not a funnel | Fewer than 3 paid audits from 30 qualified fit calls at any price from $295 to $495: the buyer pool does not pay (gate 1 failing) |
| B Hardening Week | 3 sprints sold at $1,950 or more by day 45; at least 2 delivered in 5 working days; average 40 hours or less per sprint and none above 80; first-pass acceptance 70% or better of items; 0 chargebacks; 2 named testimonials | More than 60% of audited leads reject the sprint on price: drop list to $2,000. Hours between 40 and 60: keep price, tighten Schedule A limits | Average hours above 60 (expected margin under 40%); or a third of audits end in "rebuild" (the pool is rebuild-shaped); or buyers consistently counter below $1,500 |
| C Finish-and-Launch | At least 1 sold and delivered with 2 or fewer change orders; hours 1.5 times plan or less; the client launched live | Buyers accept C only at $3,000 or less: shrink to 3 feature units at $3,500 | 2 of the first 3 C sprints have a scope dispute; or no audited lead accepts above $3,900 in 10 audits: drop C, sell repeat B sprints instead |
| E Cloud Exit | At least 1 sale from 10 audits; hours 40 or less; clean cutover | Hours over 40: raise to $2,000 with B, $2,500 alone | A failed cutover or data loss event: stop and rewrite the procedure before selling again |
| R Rebuild | At least 1 rebuild quote requested by a client at 4 weeks or more of scope | None in the first 30 days | Not a test; it is a safety valve |
| D1 / D2 | At least 33% of sprint clients take Care at handover (upside case); 90-day retention seen | 10% to 33%: bundle a 30-day Care trial into the sprint price | Under 10% after 8 sprint clients: drop Care as a product, keep the 30-day warranty only; do not count retainer revenue in the model |
| D3 Dedicated | One conversation per month asked as a question; no sale needed in 30 days | | Do not build any plan around it until a buyer asks |
| Guarantee | Refund cost 5% of revenue or less; 0 disputes | 5% to 10%: tighten Schedule A tests | Over 10%, or one chargeback lost: pause card payments above $1,000 and move to bank transfer |

Cross-offer kill signal: if the first 10 qualified leads report budgets of $1,250 or less and none moves up after the audit, the market in front of us is the Fiverr and Upwork floor [T17 #7] and the case for GO WITH CHANGES or NO-GO strengthens (gates 1 and 4).

## 12. Evidence gaps that change these numbers

1. Clutch "Project size" for the three AI-built reviews (GeekyAnts, Connectish, Cleveroad) is unread. Reading it settles whether buyers of the right kind pay $1,500 or more (gate 1) [T22 sec 6].
2. Hours per Schedule A item: nothing published beyond vendor fragments [T19 #1]. All margins depend on 40 and 100 engineer hours.
3. Audit-to-project conversion, refund rate, overrun rate: no evidence found anywhere [T16 #11, T19 #12]. All three are [A].
4. Buyer budgets above $1,250 for confirmed AI-built apps: none found. The two $2,000 posts are old and found by title [T21 #1].
5. Retainer attach rate: no evidence found [T14 #8, T20 #11].
6. Reddit, where most buyer voices would be, was unreachable in all rounds [T17, T19, T20, T22].
7. Lead reviewer cost ($2,400 per month) and the 1.75 loaded multiplier are my assumptions. If the true loaded multiplier is 2.5, B's expected margin falls to about 50% and C's to about 40% [A, not computed from data].

## Appendix: unverified items
- Section 3 audit price list, "$297 (TechPotions)": attribution differs. The figure is in track 20 section 5 (TechPotions two-day triage from $297), but the pointer list at the end of that line does not include T20.
