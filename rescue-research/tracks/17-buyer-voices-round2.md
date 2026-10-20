# Track 17: Buyer voices (round 2)

## 1. Track name and scope
Round 2 agent A. Goal: find BUYERS (not sellers) who paid, would pay, or were quoted $1,500 or more to fix, finish, harden or take over an AI-built app. This is GO gate 1.

Searches used: 45 of 45 (hard cap). All cached in cache/17-buyer-voices-searches.md as entries S1 to S45. Mode extended on every call. No WebFetch. No page was opened; every fact below comes from search result text.

What I tried: "site:reddit.com", "redlib", "reddit.birdcat.cafe", "r/lovable", "r/vibecoding", thread id 1kvcmfg, exact thread titles, buyer phrases ("hired someone", "quoted me $", "paid a developer", "I'm not technical", "willing to pay"), HN ids 48458586, 47386636, 45320431, 48823359, 45235458, 44739556, Indie Hackers, X, Medium/Substack/dev.to first-person stories, Upwork job posts, Freelancer.com project posts, VibeCodeFixers, VibeFix.

HARD FINDING ABOUT REACH: across about 20 Reddit-targeted queries, ZERO Reddit pages (or Reddit mirror pages) came back. Not one. The "How much to hire a dev" thread (1kvcmfg) was not found. Search ids for HN items (48458586, 47386636, 45320431) return nothing; the tool only matches titles. So the Reddit buyer voices that gate 1 needs are NOT reachable with this tool in this run. This is a tool limit, not proof they do not exist.

What DID work and is new: Upwork and Freelancer.com job posts. These are buyer-authored, with a stated budget, and the search result titles carry the exact price and posting date. This is the first buyer-side price data in the research. Caveat: a job post is a stated budget ("would pay"), not a payment, and the tool did not show whether any post was filled.

## 2. Key findings
1. Zero verbatim buyer statements of "I paid $X to a human to fix my AI-built app" were found. Zero buyer threads on Reddit, HN or IH that ask to hire a developer AND state a figure were reachable. Grade: moderate (as a statement about search reach), weak as a statement about the market. Type: n/a. Cache: S1 to S19, S26 to S30, S33, S36, S38, S40.
2. Buyer-stated budgets exist on Upwork and Freelancer.com for Lovable and Supabase fix work. For work explicitly on a Lovable or AI-built app, stated budgets cluster at $20 to $300. The top confirmed one is $1,000 (refine and deploy a Lovable/Supabase app, 2026-04-03) and $1,200 (review an AI-generated Lovable prototype and build the rest, 2026-10-15). Grade: moderate | Type: first-person (buyer job posts, titles only) | Links in section 3 and 5 | Cache: S20, S23, S37, S42, S44.
3. Two buyer posts at $1,500 or more are about hardening a Supabase codebase, but neither summary says the app is AI-built. (a) $2,500 fixed, posted 2026-10-12, solo founder, childcare marketplace, pre-launch cleanup and possible acquisition: server-side validation, Stripe production audit, email migration. (b) $1,500 fixed on Freelancer.com in two milestones, $1,000 audit and $500 stabilization, poster writes it "may not cover every fix". Grade: moderate (real posts, scope matches our offer) but weak on the "AI-built" link | Type: first-person | Cache: S39, S41, S45.
4. The $1,500 post (b) is a useful price-shape signal. A buyer split the budget into a paid audit ($1,000) and a stabilization step ($500). That is close to our "paid audit credited to the work" idea, but at a budget well under $2,000. Grade: weak (one post) | Type: first-person | Cache: S41, S45.
5. A live app with real users posted a flat $120 per month for an on-call Supabase developer to debug RLS (2026-10-14). This is a retention price signal: a small live-app owner's maintenance budget is about $120 per month. Grade: weak (one post) | Type: first-person | Cache: S37.
6. Secondhand buyer voices on HN. A commenter on "Vibe code is legacy code" (item 44739556) describes a non-technical friend who built a SaaS with Replit and Supabase, got paying customers, and is now hiring a developer to shore it up. No figure. A second comment says a client vibe coded an app and then hired the commenter to assess it and rewrite it (seller reporting a buyer). No figure. Grade: weak | Type: first-person anecdote, secondhand | Cache: S17, S19, S29, S38.
7. Seller price lists remain far above buyer budgets. Vendor lists: rescue pass $2,500 to $15,000 fixed; audit $1,500 to $3,500; stabilization sprint $5,000 to $15,000; hardening sprint $5,000 to $15,000; one Upwork tiered rescue service $500 / $3,000 / $10,000; one freelancer $850 to $2,850. Buyer-posted budgets for confirmed AI-built apps are $20 to $1,250. The gap is a factor of 3 to 10. Grade: moderate | Type: vendor marketing vs first-person | Cache: S5, S14, S22, S32, S42.
8. Buyers' spend on the PLATFORM (not a human) is visible and is high: Trustpilot reviewer "over $100 in credits" with no fix (au.trustpilot.com); a writer with "$607.70 in additional charges" on Replit in 3.5 days; Replit and Bolt amounts in tracks 1 and 2. Grade: weak | Type: first-person anecdote | Cache: S2, S9.
9. Third-party quote: a Substack cites a developer quote of $4,000 and 4 weeks for a meal-planning app (a build, not a rescue). Also a blog says a developer friend would charge "several grand" for a small web app. Both secondhand. Grade: weak | Type: first-person anecdote | Cache: S2, S3.
10. Floor confirmed: Fiverr gigs $20 to $500 and a Fiverr tier of $1,490 for an end-to-end production-ready app (one seller). Upwork vibe-fix jobs of $20, $30, $100, $300. Grade: moderate | Type: marketplace listings | Cache: S20, S31, S36.
11. HN "We charge $10k a week to delete AI-generated code" (item 48823359): coverage says the client pays for the seller's time; no named paying client, case study or testimonial. Grade: weak | Type: vendor marketing | Cache: S11.

## 3. Buyer quotes
Rules used: quotation marks only where the search output itself shows the words in quotation marks, or where the words are a verbatim page title shown by the tool. Everything else is labelled paraphrase. "Source text: search snippet" applies to all. Upvotes: unknown for all. Country: unknown unless shown.

### 3A. Buyer-authored job posts (stated budget = "would pay")
Titles are verbatim from search results (title includes price and post date). Cache file for all: cache/17-buyer-voices-searches.md.

| # | Title (verbatim) | Site | Posted | Stated budget | What they built / stage / spend / country | Query/cache entry |
|---|---|---|---|---|---|---|
| J1 | "Experienced Lovable Developer Needed to Fix and Optimize Website" | Upwork | 2025-10-08 | $20 fixed | Lovable site; stage unknown; country unknown | S20 |
| J2 | "Fix Payment & UI Issues in Lovable Project." | Upwork | 2025-10-15 | $30 fixed | Lovable project, payment bugs; React/Tailwind/Supabase | S20 |
| J3 | "Lovable.dev Website Troubleshooting" | Upwork | 2025-10-23 | $300 fixed | Lovable site; client has 7 other open jobs per summary | S20 |
| J4 | "Expert App Developer (Lovable.dev)" | Upwork | unknown | $100 fixed, contract-to-hire (tool summary) | wants concept to launch in Lovable | S20 |
| J5 | "Fix Vibe Coded App" | Upwork | 2025-09-01 | $100 fixed, expert level, contract-to-hire | AI-built app, backend works, frontend broken; client mentions Claude Code dashboard (unquoted fragment in summary, paraphrase) | S42 |
| J6 | "Refine and Deploy Lovable App with Supabase" | Upwork | 2026-04-03 | $1,000 fixed | existing Lovable/Supabase prototype, get live across staging and production (paraphrase from summary) | S23 |
| J7 | "Senior Full-Stack Developer–Build AI-Powered SaaS Web Platform MVP (Next.js, React,Node.js,Supabase)" | Upwork | 2026-10-15 | $1,200 fixed | review existing AI-generated Lovable prototype, build the rest (paraphrase from summary) | S23, S39 |
| J8 | "Lovable Developer — Build Internal Reporting & Client Dashboard App (Supabase)" | Upwork | 2026-08-19 | $1,250 fixed | new internal tool build, not a rescue | S23 |
| J9 | "Senior Backend Engineer — Marketplace Launch (Supabase / Stripe / Checkr)" | Upwork | 2026-10-12 | $2,500 fixed | solo founder, childcare marketplace, pre-launch hardening and possible acquisition; stack vanilla JS, Supabase, Stripe Connect, Resend, Cloudflare Pages; AI-built NOT stated | S23, S39 |
| J10 | Freelancer.com post, probably "Full-Stack Developer for React TypeScript Audit" (title not confirmed) | Freelancer.com (.au) | unknown | $1,500 fixed: $1,000 audit + $500 stabilization | existing React/TypeScript/Supabase app; AI-built NOT stated | S41, S45 |
| J11 | "On-call Supabase developer, flat $120/month, live café loyalty app (Edge Functions, RLS)" | Upwork | 2026-10-14 | $120 per month fixed | live cafe loyalty app, RLS bugs | S37 |
| J12 | "Publish LOVABLE.DEV App" | Freelancer.com | unknown | $30-250 | convert Lovable app to store-ready mobile apps; bidder offered $50 | S21 |
| J13 | "AI App Security & Code Review Expert" | Freelancer.com | unknown | approx EUR 100-250 fixed (header shows $15-25/hour; conflict) | Lovable/React/Supabase app pre-launch review | S41, S44 |
| J14 | "Supabase App Finalization" | Freelancer.com | unknown | $250-750 | bug fixes, remove hardcoded secrets, SMS verification | S41, S44 |
| J15 | "Fix Authentication and Role Assignment in Supabase (with Lovable AI)" | Freelancer.com | unknown | EUR 30-250 | Lovable + Supabase auth | S44 |
| J16 | "Supabase Expert for Application Troubleshooting and fixing" | Freelancer.com | unknown | $25-50 per hour; 2 to 6 weeks | production fixes across client's apps | S41, S44 |
| J17 | [PARAPHRASE, NOT VERBATIM] "Supabase Schema & RLS Deployment" | Freelancer.com | unknown | EUR 750-1500 | schema and RLS build; Lovable NOT stated | S41 |
| J18 | "Senior Shopify Developer — Productionize Existing Lovable/React Ecommerce Design" | Upwork | about 2026-10-09 ("11 days ago") | not shown; under 30 hrs/week, 1 to 3 months | existing Lovable/React ecommerce design to Shopify | S35 |

Links: J1 upwork.com/freelance-jobs/apply/Experienced-Lovable-Developer-Needed-Fix-and-Optimize-Website_~021975973140985851622/ ; J2 .../Fix-Payment-Issues-Lovable-Project_~021978493599361915271/ ; J3 .../Lovable-dev-Website-Troubleshooting_~021981451658268650866/ ; J4 .../Expert-App-Developer-Lovable-dev-From-Concept-Launch_~021968235852740979884/ ; J5 .../Fix-Vibe-Coded-App_~021962475130074705827/ ; J6 .../Refine-and-Deploy-Lovable-App-with-Supabase_~022040075709636871527/ ; J7 .../Senior-Full-Stack-Developer-Build-Powered-SaaS-Web-Platform-MVP-Next-React-Node-Supabase_~022110751046086488779/ ; J8 .../Lovable-Developer-Build-Internal-Reporting-Client-Dashboard-App-Supabase_~022090075430311641856/ ; J9 .../Senior-Backend-Engineer-Marketplace-Launch-Supabase-Stripe-Checkr_~022109480430597569648/ ; J11 .../call-Supabase-developer-flat-120-month-live-caf-loyalty-app-Edge-Functions-RLS_~022110520330326581289/ ; J12 freelancer.com/projects/app-development/Publish-LOVABLE-DEV-App ; J13 freelancer.com/projects/supabase/App-Security-Code-Review-Expert ; J14 freelancer.com/projects/android/Supabase-App-Finalization ; J15 freelancer.com/projects/software-development/Fix-Authentication-Role-Assignment ; J16 freelancer.com/projects/ai-development/supabase-expert-for-application ; J17 freelancer.com/projects/postgresql/supabase-schema-rls-deployment ; J18 .../Senior-Shopify-Developer-Productionize-Existing-Lovable-React-Ecommerce-Design_~022108203986664942233/ ; J10 fr.freelancer.com/projects/supabase/full-stack-developer-for-react (likely) and freelancer.com.au/jobs/supabase/.
Buyer tag for all J-posts: individual or small-business buyer; revenue unknown; funding unknown; prior spend unknown; country unknown (J9 solo founder, per summary). Whether filled: unknown for all.

### 3B. Quoted fragments (buyer-side)
- Quote: "I understand $1,500 may not cover every fix."
- Username: unknown (poster of J10)
- Site: Freelancer.com (.au listing)
- Date: unknown
- Upvotes or likes: n/a
- Link: https://www.freelancer.com.au/jobs/supabase/ (index page); probable post fr.freelancer.com/projects/supabase/full-stack-developer-for-react
- Buyer tag: existing React/TypeScript/Supabase app; stage unknown; revenue unknown; stated budget $1,500 fixed; country unknown
- Cache file: cache/17-buyer-voices-searches.md, QUERY S41 and S45 (appears in quotation marks in both)
- Source text: search snippet

- Quote: "Now he's hiring a developer to shore it up."
- Username: unknown (HN commenter on item 44739556, describing a non-technical friend)
- Site: Hacker News, "Vibe code is legacy code"
- Date: about 2025-07 (thread about 447 days old per S18)
- Upvotes or likes: unknown
- Link: https://news.ycombinator.com/item?id=44739556
- Buyer tag: SECONDHAND. Friend is non-technical, built a SaaS with Replit and Supabase, has paying customers (per summary). Revenue unknown. Spend unknown. No figure. Country unknown.
- Cache file: cache/17-buyer-voices-searches.md, QUERY S29 (in quotation marks); also S19, S38
- Source text: search snippet

Paraphrases (no quotation marks, not counted as quotes):
- HN 44739556: another commenter says a client vibe coded an app, then hired the commenter to assess it and ultimately rewrite it. Seller reporting a buyer. No figure. (S17, S38)
- Trustpilot (au.trustpilot.com/review/lovable.dev): a reviewer says the AI could not fix an issue in their architecture and they spent over $100 in credits on repeated fix requests. Spend on the platform, not a human. (S2)
- Replit writer: "$607.70 in additional charges beyond my $25/month Core plan" appears in the S9 tool text but its attribution is a writer, not a named buyer. Platform spend. (S9)
- Onaitech Substack: cites a developer quote of $4,000 and 4 weeks for a meal-planning app. A QUOTED price (build, not rescue), secondhand. (S2)
- Blog author: a developer friend said a professional would charge several grand for an app built in Lovable. Hearsay. (S3, S4)
- Founder-side account: after a 5-hour prototype hit 90%, remaining work (rate limits, token expiry) made it cheaper to pay $23/month for an existing tool. Lost-sale signal, no developer hired. (S13)

### 3C. Running table of buyer price points
Separated by type. "Paid" means money actually spent. Nothing in the first block was found.

| Type | Amount | Who / source | Date | Counts toward $1,500 gate? |
|---|---|---|---|---|
| PAID to a human to rescue an AI-built app | none found | n/a | n/a | no data |
| WAS QUOTED | $4,000 and 4 weeks (meal-planning app build) | Onaitech Substack, secondhand | unknown | no: a build, not a rescue |
| WAS QUOTED | "several grand" (small web app) | blog author's developer friend | unknown | no: vague, hearsay |
| WOULD PAY (stated budget) | $1,500 fixed ($1,000 audit + $500 stabilization) | J10 Freelancer.com | unknown | borderline: exactly $1,500, AI-built not stated |
| WOULD PAY (stated budget) | $2,500 fixed | J9 Upwork, solo founder, pre-launch hardening | 2026-10-12 | yes on amount; AI-built not stated |
| WOULD PAY | EUR 750-1500 | J17 Freelancer.com Supabase schema + RLS | unknown | no: top of range about $1,500 to $1,700, AI-built not stated |
| WOULD PAY | $1,250 | J8 Upwork Lovable internal tool (new build) | 2026-08-19 | no |
| WOULD PAY | $1,200 | J7 Upwork, finish an AI-generated Lovable prototype | 2026-10-15 | no (under $1,500) |
| WOULD PAY | $1,000 | J6 Upwork, refine and deploy Lovable/Supabase app | 2026-04-03 | no |
| WOULD PAY | $250-750 | J14 Supabase App Finalization | unknown | no |
| WOULD PAY | $300 | J3 Lovable troubleshooting | 2025-10-23 | no |
| WOULD PAY | $100, $100, $30, $20, $30-250, EUR 100-250, EUR 30-250 | J1, J2, J4, J5, J12, J13, J15 | 2025 to 2026 | no |
| WOULD PAY (recurring) | $120 per month | J11 live cafe app, on-call RLS fixes | 2026-10-14 | no: retention price floor signal |
| WOULD PAY (hourly) | $25-50 per hour | J16 | unknown | no |
| PAID to the platform | over $100 (Trustpilot); $607.70 (Replit writer); $1,000 in a week (Replit user, track 2) | various | 2025 to 2026 | no: not a human fix |

## 4. Seller quotes
Kept separate. Bias: sellers benefit from saying prices and demand are high.
- Vendor guide (frenchydigital.com/blog/vibe-coding-app-fix-pricing-2026): vibe code health check (audit) $1,500 to $3,500; stabilization sprint $5,000 to $15,000. (S32, paraphrase of tool text)
- Developer blog (zlatkomarjanovic.com): fixed rescue scope often $2,500 to $7,500 for stabilization; rescue pass covering auth, RLS, deploy, Stripe live and error handling typically $2,500 to $15,000 fixed. (S5, S14)
- Rescue shop public pricing per a guide: about $1,500 for a single integration fix and $7,500 to $15,000 for a full production-readiness pass. (S5)
- Agency (verycreatives.com/services/lovable-to-production): hardening sprint 2 to 4 weeks, $5,000 to $15,000. (S21)
- Upwork service listing "AI-Built Codebase Rescue": Starter $500, Standard $3,000, Advanced $10,000. (S42)
- Upwork freelancer: plans $850 to $2,850, 10 to 22 days; another fixed-scope fix $1,500 to $6,000. (S22)
- Fiverr seller tiers $100 / $990 / $1,490 (production-ready end to end). (S31)
- VibeCodeFixers.com: developers about $40 to $70 per hour; the site is a directory and publishes no rescue pricing. (S29, S32)
- Odra "Slopfix": $10,000 for one week, three engineers; payment proportional to reduction target. No named client. (S11, HN 48823359)
- 404 Media via Slashdot (tool text, in quotation marks): "Freelance developers and entire companies are making a business out of fixing shoddy vibe coded software"; one Fiverr seller works with 15 to 20 clients regularly. (S29)
- Vendor claims on Upwork demand (+178% AI integration, 40% premium) have no shown method. (S22, S25)

## 5. Numbers found
| number | what it measures | source link | date | type | grade |
|---|---|---|---|---|---|
| 0 | Reddit or mirror pages returned across about 20 Reddit-targeted searches | cache S1-S4, S7, S9, S12, S13, S15-S17, S33, S34 | 2026-10-20 | tool limit | n/a |
| 0 | buyer threads on Reddit/HN/IH that ask to hire a dev AND state a figure | all | 2026-10-20 | not reachable | n/a |
| 18 | distinct buyer job posts found (Upwork 11, Freelancer.com 7), by title | section 3A | 2025-09 to 2026-10 | anecdote (buyer-authored) | moderate |
| 17 | of those 18 with a visible budget | section 3A | same | anecdote | moderate |
| [UNVERIFIED] 11 | of those 18 that are fix, finish or review work on an app stated as Lovable or AI-built (J1, J2, J3, J5, J6, J7, J12, J13, J14, J15, J18) | section 3A | same | anecdote | moderate |
| 2 | posts with a budget of $1,500 or more (J9 $2,500; J10 $1,500) | Upwork; Freelancer.com | 2026 | anecdote | weak: AI-built not stated |
| 0 | posts with a budget of $1,500 or more that state the app is AI-built or Lovable-built | section 3A | 2026 | anecdote | weak |
| $1,250 | highest budget on a post that names Lovable | J8 (a new build); highest rescue/finish: $1,200 (J7) | 2026-08-19 / 2026-10-15 | anecdote | moderate |
| $20 to $300 | range of budgets on Lovable "fix" posts (J1-J5) | Upwork | 2025-09 to 2025-10 | anecdote | moderate |
| $120 per month | flat on-call Supabase developer for a live app | J11 | 2026-10-14 | anecdote | weak |
| 153 | Supabase developer job postings in 30 days to 2026-09-14, across Upwork and other boards | devsnipe.com/blog/freelance-supabase-developer-jobs-2026 | 2026-09 | vendor blog | weak |
| 109 | vibe-coding jobs listed on Upwork's vibe-coding page (one snapshot) | upwork.com/freelance-jobs/vibe-coding/ | 2026-10 | independent (marketplace page) | moderate |
| 1,304 | Upwork postings analysed by vibehackers.io (no findings visible) | vibehackers.io/blog/upwork-vibe-coding-jobs | 2026 | vendor | weak |
| 95 points | HN "The Software Engineers Paid to Fix Vibe Coded Messes" (item 45235458, 2025-09-13) | news.ycombinator.com/item?id=45235458 | 2025-09-13 | independent | moderate |
| 138+ points | HN "We charge $10k a week to delete AI-generated code" per Ground Truth | groundtruth.day | 2026 | secondary | weak |
| 391 points, 538 comments | Ask HN "How to deal with shipping AI-written code you don't understand?" (item 50151036) | news.ycombinator.com/item?id=50151036; aiweekly.co | 2026 | independent | moderate |
| $1,500 to $3,500; $5,000 to $15,000 | vendor audit; stabilization | frenchydigital.com | 2026 | vendor | weak |

Note: J4 is a build from concept, J8 a new build, and J9, J10, J16, J17 do not say AI-built. They are excluded from the 11.

Threads asking to hire a developer: on Reddit/HN/IH: 0 reachable. On Upwork/Freelancer.com: 18 posts (11 clearly AI-built fix/finish). Posts that mention a figure: 17 of 18.

## 6. What this means for the offer
- Buyers who post jobs for Lovable or AI-built fixes name budgets of $20 to $1,250. A fixed $2,000 weekly sprint is 2 to 100 times those posts. The only $1,500+ buyer posts are Supabase hardening jobs ($2,500 and $1,500) where AI-built is not stated.
- The shape that buyers seem to accept is a split: a paid audit first ($1,000 in J10) then a stabilization step. A "$1,000 to $1,500 audit that is credited to a $2,500+ hardening" is closer to posted budgets than a $2,000 sprint as the front door.
- Target the buyer in J9: a solo founder who is about to launch or sell, with Stripe and Supabase. Their scope (server-side validation, Stripe live audit, email migration, webhook checks) is the same list as our checklist. This buyer type appears to pay more than the "fix my Lovable site" crowd.

## 7. What this means for the GO gates
- Gate 1 (buyers paying $1,500 or more): UNCLEAR, leaning not met. Zero evidence of buyers PAYING $1,500+ for rescue. Two buyer-stated budgets at $1,500 and $2,500 exist for Supabase hardening, but neither is shown as AI-built. For confirmed Lovable or AI-built fix posts the top budget is $1,200. Reddit, where the strongest buyer evidence should be, was unreachable (0 pages in about 20 tries).
- Gate 3 (repeatable fix list): supports, weakly. J9, J13, J14, J2 all list the same items: RLS, hardcoded secrets, Stripe live and webhooks, auth and roles, server-side validation, email.
- Gate 4 (position above the low-cost floor): contradicts in part. Buyers who name Lovable on marketplaces set budgets near the floor ($20 to $300). A position above the floor depends on finding the J9 type of buyer, who is not on those boards by title.
- Gate 5 (platform improvements erase demand): unclear. No evidence from this track.

## 8. Machine-readable block
```json
{"track": "17-buyer-voices-round2", "demand_signal": "weak", "buyer_price_points_usd": [20, 30, 100, 120, 300, 1000, 1200, 1250, 1500, 2500, 4000], "seller_price_points_usd": [500, 850, 1500, 2500, 2850, 3000, 3500, 5000, 7500, 10000, 15000], "gates_supported": [3], "gates_contradicted": [4], "evidence_grade": "weak", "sources_read": 45, "buyer_quotes": 2, "seller_quotes": 11}
```
Notes: 120 is per month. 4000 is a secondhand quote for a build. 1500 and 2500 are stated budgets on posts where AI-built is not shown. Searches: 45 of 45.

## Appendix: unverified items
- Section 5, "11 of those 18 ... stated as Lovable or AI-built (J1, J2, J3, J5, J6, J7, J12, J13, J14, J15, J18)": number differs. Cache S41/S44 describe J14 (Supabase App Finalization) only as bug fixes, hardcoded secrets, SMS verification; no Lovable or AI-built statement. Supported count is 10, not 11. (Does not change the gate 1 reading: no $1,500+ post is shown as AI-built either way.)
- J17 title "Supabase Schema & RLS Deployment" (downgraded to PARAPHRASE, NOT VERBATIM): cache has only the lower-case summary phrase "Supabase schema and RLS deployment" and the URL slug, not a verbatim title.
