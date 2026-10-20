# Track 19: Delivery reality and practitioner detail (round 2, agent C)

## 1. Track name and scope
Round 2 agent C. Q6 (delivery reality) plus the practitioner-economics gaps from track 10 and the missing searches in track 11 section 5b. Used all 35 of 35 WebSearch calls (hard cap). All raw results are in `cache/19-delivery-searches.md`, numbered N=1 to N=35. Every item below cites the N number. No WebFetch was tried (blocked per NETWORK-NOTES). Full pages, thread comment trees, usernames, points and dates were never opened. Everything is "Source text: search snippet".

What worked: HN thread existence and some comment text, vendor and practitioner blog pages, dev.to, Wavect and Red Leg Dev page text.
What did NOT work: Reddit. Five queries (N=8, 9, 10, 30, plus the HN-targeted ones) returned zero Reddit threads, even with "reddit" and "site:reddit.com" in the query. So buyer and practitioner Reddit voices on hours, scope creep and refund fights are still missing. Medium and Substack hits were generic. Fiverr and Upwork pages for Hamid Siddiqi and for rescue job budgets were not found.
Big caveat: almost everything on fix effort and rebuild rules is seller content (people who sell rescue). Treat all of it as marketing until a buyer confirms.

## 2. Key findings

1. **No published hours-per-task table exists.** I searched for RLS, auth, Stripe webhooks, secrets, deploy and performance hours (N=5, 23, 27). Only these fragments came back: (a) a dev.to auditor says the five most common patterns "take 2-4 hours to fix if you know what you're looking for" (tool-rendered, wording unconfirmed, covers all five patterns, not RLS alone); (b) a vendor sample audit lists ~2 hours for a critical Supabase key exposure; (c) vendors claim a fix "usually 1 to 2 days" or sell a week-long production pass; (d) a quick-fix tier [PARAPHRASE, NOT VERBATIM] "starting around $299" for Stripe webhook verification. No hours for auth rewrite or deploy.
Grade: weak | Type: vendor marketing | N=5, 23, 27 | links: https://dev.to/systagproject/i-audited-9-vibe-coded-apps-in-24-hours-here-are-the-5-patterns-that-show-up-every-single-time-ebk , https://vallettasoftware.com/vibe-coding-cleanup , https://vibecoding.app/blog/vibe-coded-codebase-rescue | date 2026

2. **Whole-app timelines are in weeks, not hours.** Agency estimates seen: 6 to 8 weeks for a 12.7k-line Next.js plus Stripe app; 4 to 6 weeks to production quality for a 39k-line Expo plus Supabase app; 1 to 2 week remediation sprint (another vendor); 4 weeks for triage, secrets and auth, data layer and tests on a small SaaS under 30k lines (playbook); Red Leg Dev [PARAPHRASE, NOT VERBATIM] "2-6 weeks depending on the size and complexity of the codebase, starting with an audit"; McKelvey 4 to 8 weeks.
Grade: weak | Type: vendor marketing | N=27, 29, 22 | https://redleg.dev/vibe-coding , https://justinmckelvey.com/vibe-code-rescue

3. **Hours from the HN "100 hour gap" thread (item 47386636).** The post (Marcin Budkowski, Cryptosaurus app) says about 100 hours of vibecoding after a first working prototype in the first hour. Comments (paraphrase from search summary): improvement drops to about 2 to 3x once back-and-forth and code review are counted; "80% of 100 hours is considerably less than 80% of 600 hours" is a sibling comment title (item 47388250). This is about BUILDING a product with AI, not about fixing someone else's app. It is the best public hours anchor and it says a "finished" simple app is ~100 hours.
Grade: moderate (post exists, numbers are the author's own) | Type: first-person anecdote | N=1 | https://kanfa.macbudkowski.com/vibecoding-cryptosaurus , https://news.ycombinator.com/item?id=47386636

4. **Repeatability: rescuers name nearly the same list.** Table in section 5b compares 9 independent sellers. Core items that appear in at least 5 of 9: exposed or committed secrets and keys; missing or weak authorization (row ownership, RLS); fake or client-side auth; payments and webhooks that are wrong or unverified; error handling and validation gaps; no separation of staging and production; no tests or CI. Independent research (Wiz, via tool summary) names four patterns: client-side authentication, hardcoded secrets, permissive data access policies, internal tools deployed publicly. The lists are written by sellers who have an incentive to look systematic, and no seller states a share ("X% of our jobs share this list"). So repeatability of the PROBLEM CLASSES is supported; repeatability of the FIX TIME is not measured.
Grade: moderate for problem classes, weak for fix-time | Type: vendor marketing plus one independent research mention | N=4, 5, 6, 13, 12, 29, 23

5. **Rescue vs rebuild: no hard rule, no share of jobs that became rebuilds.** Searches for a percentage found none (N=17, 21, 35). What exists: (a) one vendor heuristic: rebuild may be faster if more than 40% of deployments cause a bug or outage; refactor works under 15%; if refactor estimate is 60% or more of rewrite estimate, rewrite wins (explicitly "vendor heuristics, not research"); (b) structural triggers: architecture wrong, data model cannot represent the domain, every change touches ten files; (c) "Rewrites are almost always the wrong call when the app already has users" (vibecoding.app playbook, quoted in tool output); (d) Wavect and Red Leg Dev both say rescue is the usual answer; Wavect: "A full rebuild costs months and most vibe-coded apps do not need one" is the tool's paraphrase, not a verified quote; (e) HN freelancer: "I ended up recommending that I just rewrite the whole codebase (I reused one tiny piece)" and "hired me to assess it, and ultimately rewrite it" (two HN commenters; both ended in rewrite); (f) axonbuild audit of 21 AI-built apps: 958 confirmed findings, 58 critical (about 6%), author argues most other findings would be redone in a new build anyway.
Grade: weak | Type: vendor marketing plus first-person anecdote | N=17, 21, 25, 30, 35

6. **Fixed-price and refund terms exist in the market but no dispute stories were found.** Zero reports of chargebacks, refund fights or fixed-price overruns (N=21). Wavect, per page text: weekly cancellation, [PARAPHRASE, NOT VERBATIM] "final week refunded if the work doesn't impress", not billed hourly, fixed scope, senior engineers. McKelvey: free 20-minute repo audit then fixed price. Vibe Code Rescue: $299 audit credited to a $1,500 sprint. Absence of stories is NOT evidence of no disputes: I could not search Reddit.
Grade: weak | Type: vendor marketing | N=21, 28 | https://wavect.io/services/vibe-coding-rescue/

7. **Client behaviour: "clients keep vibe-coding on top" appears only as a summary, not as a verbatim quote.** The tool summary of HN search N=25 says one commenter noted clients often keep vibe-coding on top of cleaned-up code so the cycle repeats. HN item 44832986 (N=26) has a commenter whose client modified a small library with AI-generated code, it broke, and the commenter did "good-faith assurance work" to fix it. Regression loops (fix one thing, lose another) are described by a vendor (AppStuck) with the advice to freeze known-good behaviour with tests. No practitioner account of a client overwriting a fixed Lovable project mid-engagement was found. The contract ideas in N=34 (code freeze, change control, no liability for outside edits) were the search tool's own synthesis, not sourced.
Grade: weak | Type: first-person anecdote (HN, paraphrase) | N=25, 26, 34 | https://news.ycombinator.com/item?id=44832986

8. **AI tooling for rescue: no measured share of work automated.** Best data points: Slopfix (odra.dev) press coverage says the team uses AI agents to cut repos "by up to 65%" (X post title by Tom's Hardware) and hands over a CLAUDE.md, lint rules and CI checks; its example went from 100,000 to 35,000 lines; it reviews the repo free and rejects jobs with too little dead weight. McKelvey (seller) self-reports feature work of 60 to 90 minutes manual becoming 10 to 15 minutes with Claude Code. A dev.to author says an agent produced three different error-handling patterns and cost a Saturday that would have taken about an hour by hand. A Substack report says about 30% productivity gain, with floundering on UI and state. An agency case (Anish Gandhi, Lovable app plus Claude Code, 73 bugs closed) says every commit passes a human gate; no hours (N=19, 20). An open-source Claude Code plugin does read-only production-readiness audits across eight lenses. My read: audits and mechanical refactors automate well; auth, data model and payment logic still need a human. No percentage can be sourced.
Grade: weak | Type: vendor marketing plus anecdote | N=3, 19, 20, 32 | https://x.com/tomshardware/status/2074851068794867831

9. **Slopfix is real press-wise but has no named clients or results beyond one example.** Sources in N=3: letsdatascience, Tom's Hardware (X), syntackle, lavx, whats-ai, shiftdelete. Terms: $10,000 for one week, three engineers, payment in proportion to the deletion target hit, two-week defect warranty. One article (blackwire.world) calls Odra.dev an extortion site; the tool could not corroborate it; ignore as unreliable. Different company: slopfix.ptolemay.com quotes $30 to $100 per fix with a 20% deposit (N=28). Do not conflate.
Grade: weak | Type: vendor marketing (press repeats the pitch) | N=3, 16, 28

10. **QuickLaunch: still only the Indie Hackers post.** Confirmed again: "$120k+" in 2025, began as an idea-to-MVP platform, "Rescue Sprint" service; examples named: oversized React components with dozens of state hooks, WebSocket subscription memory leak. Sprint price, client count, conversion and channel details were NOT in any snippet (N=2, 12). The earlier claim of "word of mouth, no ads" in track 10 comes from the tool's summary of the post, not seen again here. Do not confuse with vibecoderescue.dev "Rescue Sprint" ($1,500, $299 audit credited).
Grade: weak | Type: vendor marketing (self-report) | https://www.indiehackers.com/post/how-quicklaunch-made-120k-fixing-vibe-coded-apps-in-2025-y05kJ7G9VG4wdJplBIb8

11. **404 Media Sept 2025 and VibeCodeFixers volumes.** Hamid Siddiqi (Fiverr): says he has done this since late 2023 and works with "around 15-20 clients regularly, with additional one-off projects throughout the year" (tool shows this in quotes). His Fiverr price and reviews were not found. VibeCodeFixers.com founder Swatantra Sohni: "over 300" programmers signed up per 404 Media; Indeed later says 500; his own wiki bio says 550 and "600+". Projects matched: 30 to 40, without advertising (summary of 404). A Ukrainian outlet says "a few dozen clients". Ulam Labs: "we clean up after vibe coding." One outlet mentions a client who burned $5,000 in OpenAI credits. No fixer hourly rate appears in the 404 coverage as returned. Supply side outnumbers demand side by 10x or more on this marketplace.
Grade: moderate (secondhand of a real publication) | Type: anecdote plus vendor self-report | N=14, 24 | https://developers.slashdot.org/story/25/09/13/054206/the-software-engineers-paid-to-fix-vibe-coded-messes

12. **Conversion rates, close rates, lead sources, average ticket: no evidence found.** Searched N=31. Nothing from any named practitioner. Upwork has job posts titled "Vibe Coded Project Review" (less than 30 hrs/week, less than 1 month) but no budget visible. A Freelancer.com debug post had budget "$100 per project" with 153 bidders averaging $96 (N=33): a buyer-side price at the floor.
Grade: n/a | Type: n/a

13. **Price anchors seen this round (sellers, new beyond tracks 7, 8, 10).** Vibe Code Rescue (vibecoderescue.dev): $299 audit, $1,500 fixed sprint, about a week, 48-hour turnaround. Other sprints listed by the tool: from $1,400; £495 to £2,000 typical (one UK freelancer); stabilisation sprint from $10,000; two-week sprint from $6,000; sprint from EUR 3,500 and audits from EUR 600. frenchydigital: health check $1,500 to $3,500, stabilisation sprint $5,000 to $15,000. kodingklouds: 48-hour audit $199 credited. McKelvey: pre-launch review $200 to $1,000; post-launch rescue $3,000 to $15,000; typical full rescue $25K to $50K (from $15K); a 6-week fixed $40K rebuild replacing a $150K agency quote; $15,000 fix on payments with broken webhook handling. Metacto: $50K to $150K. goodfirms-type guide: $1,000 to $15,000+; cleanup adds 20 to 30% to build cost; $60 to $100+/hr freelancers. vibeyourwebsite: $60/hr in 30-minute blocks.
Grade: weak (all sellers) | Type: vendor marketing | N=2, 11, 22, 28, 33

## 3. Buyer quotes
None verified. No buyer voice with a username surfaced in 35 searches.
One buyer-side data point, not a quote: Freelancer.com job to debug vibe-coded apps, budget "$100 per project", 153 freelancers bidding at average $96 USD (tool text). Buyer tag: unknown on all fields. Cache: N=33. Link: https://www.freelancer.in/projects/backend-development/experienced-developer-for-vibe-coding
HN commenters who describe clients (anecdotes, practitioner-reporting-on-buyers, not buyers): see section 4.

## 4. Seller quotes
Bias flag: all below are people who sell, or could sell, this work. They benefit from saying it is needed and systematic. Source text: search snippet. Usernames, points and dates are unknown unless stated. Wording is as shown inside quotation marks in the tool output.

- "As a freelance developer, I've already had one job that was essentially vibe coding cleanup - though I ended up recommending that I just rewrite the whole codebase (I reused one tiny piece)."
  - Username unknown; HN; [UNVERIFIED] date about 2025-09; points unknown; [UNVERIFIED] https://news.ycombinator.com/item?id=45320431 ; Cache N=25.
- "One of my current clients vibe coded an app then hired me to assess it, and ultimately rewrite it."
  - Username unknown; HN; date unknown; https://news.ycombinator.com/item?id=45320431 (thread attribution from tool, item not confirmed); Cache N=25.
- "I've been getting more requests than ever to debug AI-generated codebases where the original "developer" can't explain what any of it does. The security audit work alone is keeping me busy"
  - Username unknown; HN; date unknown; item not confirmed; Cache N=25.
- "Most AI-generated v1s have the same gaps: error handling, security, real-world load, missing tests, no CI/CD."
  - Red Leg Dev company page (redleg.dev/vibe-coding), 2026; https://redleg.dev/vibe-coding ; Cache N=29.
- "In most cases, fixing is faster and cheaper than starting over."
  - Red Leg Dev; same page; Cache N=29. Pure marketing.
- "Currently, I work with around 15-20 clients regularly, with additional one-off projects throughout the year."
  - Hamid Siddiqi, Fiverr freelancer, via 404 Media, 2025-09; Cache N=24.
- "we clean up after vibe coding."
  - Ulam Labs website via 404 Media, 2025-09; Cache N=24.
- "Rewrites are almost always the wrong call when the app already has users"
  - vibecoding.app playbook (publisher also sells vibe-coding content and agency listings); https://vibecoding.app/blog/vibe-coded-codebase-rescue ; Cache N=30.
- "Exposed API keys (OpenAI, Stripe, Supabase service role, AWS) are the most common finding in rescue work"
  - same page; Cache N=30.
- "take 2-4 hours to fix if you know what you're looking for"
  - dev.to author systagproject (sells VibeScan, a scanner); the quote is shown inside the tool's own sentence, wording unconfirmed; https://dev.to/systagproject/i-audited-9-vibe-coded-apps-in-24-hours-here-are-the-5-patterns-that-show-up-every-single-time-ebk ; Cache N=27.
- "this article doesn't add much; it's a thin advertorial for their services."
  - HN commenter on "Vibe coding cleanup as a service"; Cache N=25.
- "maintenance work: $100/hr; vibe-coding cleanup: $200/hr" (a jab, not an invoice).
  - HN; Cache N=25.
- "Across 21 third-party AI-built apps audited in June and July 2026, 958 confirmed findings included 58 confirmed criticals."
  - axonbuild (vendor); https://axonbuild.com/blog/cleanup-or-rebuild ; Cache N=35.
- "Currently ... " not repeated. "we ... good-faith assurance work" is a tool paraphrase from HN item 44832986; not a quote.

## 5. Numbers found

| Number | What it measures | Source | Date | Type | Grade |
|---|---|---|---|---|---|
| about 100 hours | Build time to take a simple app (Cryptosaurus) from prototype to working product | https://kanfa.macbudkowski.com/vibecoding-cryptosaurus ; N=1 | [UNVERIFIED] 2026-03 | anecdote | moderate |
| about 2-3x | Speedup commenters say AI gives once back-and-forth is counted (HN 47386636, summary) | https://news.ycombinator.com/item?id=47386636 ; N=1 | [UNVERIFIED] 2026-03 | anecdote | weak |
| 2-4 hours | Fix time for the five most common audit patterns (vendor scanner author) | dev.to systagproject ; N=27 | 2026 | vendor | weak |
| about 2 hours | Fix time for critical Supabase key exposure in one vendor's sample audit | N=27 | 2026 | vendor | weak |
| 1-2 days | Vendor-claimed typical fix time | N=23 | 2026 | vendor | weak |
| 8 of 9 | Audited apps with permissive RLS (same dev.to author) | N=27 | 2026 | vendor | weak |
| 1-2 weeks | Vendor remediation sprint length | N=27 | 2026 | vendor | weak |
| 4 weeks | Plan for small SaaS under 30k lines, triage to tests | vibecoding.app playbook ; N=27 | 2026 | vendor | weak |
| 6-8 weeks / 12.7k lines | Agency estimate, Next.js plus Stripe app | N=27 | 2026 | vendor | weak |
| 4-6 weeks / 39k lines | Agency estimate, Expo plus Supabase app | N=27 | 2026 | vendor | weak |
| 2-6 weeks | Red Leg Dev rescue length | https://redleg.dev/vibe-coding ; N=29 | 2026 | vendor | weak |
| 4-8 weeks, $25K-$50K | McKelvey typical rescue | https://justinmckelvey.com/vibe-code-rescue ; N=22, 28 | 2026 | vendor | weak |
| 6 weeks, $40K | McKelvey fixed rebuild of YC-backed B2B SaaS (no real auth, Stripe "just a button") vs $150K agency quote | https://justinmckelvey.com/blog/vibe-code-rescue-case-study ; N=22 | 2026 | vendor | weak |
| $15,000 | Rescue of a marketplace payment system that double-charged (missing webhook verification) | N=22 (forum summary), N=11 (McKelvey $15K webhook fix) | 2026 | vendor/anecdote | weak |
| $1,500 / $299 | Vibe Code Rescue sprint / audit (credited) | https://vibecoderescue.dev/ ; N=2 | 2026 | vendor | weak |
| $10,000 per week, 3 engineers | Slopfix (odra.dev) | N=3 | 2026-07 | vendor | weak |
| 100,000 to 35,000 lines; up to 65% | Slopfix example and claimed cut range | N=3 | 2026-07 | vendor | weak |
| $30-$100, 20% deposit | A different Slopfix (ptolemay) per-fix price | https://slopfix.ptolemay.com/ ; N=28 | 2026 | vendor | weak |
| $120k+ | QuickLaunch 2025 revenue | IH post ; N=12 | 2025/26 | vendor | weak |
| 15-20 regular clients | Hamid Siddiqi | N=24 | 2025-09 | anecdote | weak |
| 30-40 projects matched; 300 / 500 / 550 / 600+ experts | VibeCodeFixers volume vs supply (404, Indeed, own bio) | N=24 | 2025-09 onward | vendor | weak |
| 958 findings, 58 critical (6%) | axonbuild audit of 21 AI-built apps | N=35 | 2026-06/07 | vendor | weak |
| 33% to 67% | Share of AI code needing manual fixes (rescue-shop claim) | N=17 | 2026 | vendor | weak |
| more than 40% / under 15% / 60% | Rewrite-vs-refactor heuristics | N=17 | 2026 | vendor | weak |
| 73 bugs | Closed in one Lovable-plus-Claude-Code agency case | N=19 | 2026 | vendor | weak |
| 60-90 min to 10-15 min | Self-reported feature speedup with Claude Code | N=32 | 2026 | vendor | weak |
| $100 per project; 153 bidders; $96 avg | Freelancer.com debug-vibe-code job | N=33 | 2026 | buyer-side listing | weak |
| 20% to 30% | Post-build cleanup added to total cost (vendor guide) | N=33 | 2026 | vendor | weak |
| $3,500-$15,000 / $25K-$50K | Targeted fix / full rescue (consultant blog; also McKelvey) | N=2, 12 | 2026 | vendor | weak |

### 5b. Repeatability: practitioner problem lists compared
Legend: Y = named in the snippet I saw. Blank = not seen (does not mean absent). Sources: Wavect N=13; Red Leg N=29; McKelvey N=4; dev.to systag N=5/6/27; Axonbuild "26 audits" N=13; QuickLaunch N=12; Hamid Siddiqi N=14; vibecoding.app playbook N=30; Wiz via hyrax N=6 (independent research, via tool summary).

| Problem class | Wavect | Red Leg | McKelvey (7) | systag (dev.to) | Axonbuild | QuickLaunch | Siddiqi | vibecoding.app | Wiz |
|---|---|---|---|---|---|---|---|---|---|
| Exposed / committed secrets | Y | | Y | Y | | | | Y | Y |
| Broken access control / RLS / ownership | Y | | | Y | Y | | | Y | Y |
| Fake / client-side auth | | | Y | | | | | | Y |
| Payments / webhooks wrong | Y | | Y | Y (JWT off on webhooks) | | | | | |
| Error handling / validation | Y | Y | Y | | | | | | |
| Staging and prod share one DB / no env separation | Y | | | | | | | | |
| No tests / CI | Y (adds regression suite) | Y | | | | | | | |
| Performance (N+1, memory leaks, huge components) | | Y (real-world load) | | | | Y | Y (slow code) | | |
| UI / branding inconsistency | | | | | | | Y | | |
| Unmaintainable code | | | Y | | | Y | | | |
| Internal tools public with no auth | | | | | | | | | Y |

Read: the SECURITY and DATA core (secrets, access control, auth, payments, error handling) recurs across at least 6 of 9 sources. Performance and UI polish are what the cheaper, Fiverr-style sellers list (Siddiqi). The four-pattern Wiz finding (client-side auth, hardcoded secrets, permissive data policies, public internal tools) is the only independent confirmation, and I got it only through a tool summary.

## 6. What this means for the offer
- A fixed "security and data hardening" week is a defensible, repeatable unit: secrets rotation, RLS and ownership checks, auth hardening, webhook signature verification, staging/prod split, error handling and basic tests. Seller after seller lists these, and the only hour fragments (2 to 4 hours for the five top patterns; about 2 hours for a key exposure) suggest the checklist items are small when the app is small. Do NOT promise "finish the app": every whole-app estimate found is 2 to 8 weeks and 4 to 8 weeks at $25K to $50K for the sellers who offer it.
- Sell the audit first and make the sprint conditional on it. Every serious seller does this (Vibe Code Rescue $299 credited; McKelvey free 20-minute audit; Slopfix free repo review and rejection; Metacto 48-hour audit). Put a written rescue-or-rebuild gate in the audit using the vendor heuristics as a starting point (data model sound; app has users; failure rate; refactor cost vs rebuild cost), then price a rebuild or a longer sprint separately. HN practitioners report ending in a rewrite at least twice, so assume some jobs convert.
- Add a code-freeze and change-control clause (client stops prompting the AI tool, or works on a branch we review), plus acceptance tests that define "done". The AI-tool regression loop and client re-prompting are the plausible scope-creep source; evidence for it is thin, so treat it as a risk to test in the first 30 days, not a proven cost.

## 7. What this means for the GO gates
- Gate 1 (buyers paying $1,500+): unclear. All $1,500+ prices found this round are seller prices. The one buyer-side listing is $100 per project. No change from round 1.
- Gate 2 (channel under 30% of project value): unclear. This round found no source for how practitioners got clients beyond QuickLaunch's referral claim from round 1 (not re-seen) and no conversion rates.
- Gate 3 (repeatable fix list): supports for the problem list, unclear for fix time. Nine sources converge on the same security and data core; no source gives measured hours per fix or a share of jobs that fit the list.
- Gate 4 (position above the low-cost floor): mildly supports. Floor sellers list UI and polish fixes at $20 to $100; credible-looking sellers list secrets, access control and payments with fixed-price audits and conditional rebuilds at $1,500 and up. The line is "security and data hardening with proof", not "bug fixing".
- Gate 5 (platform improvement): unclear. Not tested here. One tool summary says Lovable's own scanner checks RLS presence rather than effectiveness (track 11); no new evidence this round.

## 8. Machine-readable block
```json
{"track": "19-delivery-round2", "demand_signal": "moderate", "buyer_price_points_usd": [100], "seller_price_points_usd": [30, 100, 199, 299, 1500, 3500, 5000, 10000, 15000, 25000, 40000, 50000], "gates_supported": [3, 4], "gates_contradicted": [], "evidence_grade": "weak", "sources_read": 35, "buyer_quotes": 0, "seller_quotes": 13}
```

---
## Appendix A. Direct answers for the orchestrator (not part of template)

Gate 3 read: LEAN PASS on problem classes, UNPROVEN on time. A rescue checklist covering secrets, RLS and ownership, auth, webhooks, error handling and env split matches what 6+ of 9 independent sellers say they find, plus one independent research summary. But nobody publishes a share of jobs that fit, and the share of jobs that end as rewrites has not been sized (two HN freelancers both ended in rewrites; the only rule of thumb is a vendor's). Mark gate 3 "supported for the checklist, to be proven by the first 3 paid audits".

Is a fixed-price week viable? Yes for a scoped hardening week on a small app (say under 20 to 30k lines, one stack, Supabase plus Stripe), if (a) a paid audit comes first and gates the sprint, (b) scope is a named checklist with acceptance tests, (c) rebuild candidates are priced separately, (d) a code freeze is in the contract. No for "finish my app" at $2,000: the market sellers who offer finishing charge $15K to $50K and 4 to 8 weeks. Our cost side (my arithmetic, assumption): an engineer at roughly $1,000 to $1,100 a month is about $6 to $7 per working hour at 160 hours; a 40-hour engineer week plus 8 hours of lead review costs on the order of $300 to $600 even with a 2x overrun. So delivery cost is not the risk. The risks are acquisition cost, a 3x overrun on a bad codebase eating a second week for free, and refund or dispute handling. A 2x overrun is survivable; a rebuild-grade app sold as a week is not. Triage in the audit.

Evidence gaps: Reddit voices on hours, client re-prompting, refund fights; QuickLaunch sprint price, client count and channel; Siddiqi Fiverr price and reviews; 404 Media prices and names beyond what is above; any conversion rate; share of rescues that became rebuilds. Reddit access remains the blocker.

## Appendix: unverified items
- Section 5, "2026-03" date for the Cryptosaurus post and HN 47386636 (two table rows): not in cache. N=1 shows no date for the post or the thread.
- Section 4, first HN quote ("As a freelance developer, I've already had one job..."): date "about 2025-09" and item id 45320431 not supported. N=25 says "Item ids/usernames/dates/points not shown". The quote wording itself is verified (inside quotation marks in the tool text).
- Finding 1, "starting around $299" (downgraded): cache N=27 says "a quick-fix tier starting ~$299", not in quotation marks and different wording.
- Finding 2, Red Leg Dev "2-6 weeks depending on the size and complexity of the codebase, starting with an audit" (downgraded): cache N=29 has "Timing 2-6 weeks depending on size, starting with an audit." in the tool summary, not in quotation marks and shorter.
- Finding 6, Wavect "final week refunded if the work doesn't impress" (downgraded): cache has "the final week is refunded if the work doesn't impress" in the tool summary, not in quotation marks. (Track 20 has a verbatim version of the Wavect line, "Last week refunded if we didn't blow you away".)
