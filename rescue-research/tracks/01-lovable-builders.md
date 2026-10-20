# Track 01: Lovable builders

## 1. Track name and scope
Track 1: Lovable builders. Where and why they get stuck, what they tried, what they spent, what they would pay.

Time/effort: about 10 working searches, then the shared WebSearch budget ran out (the tool said the limit of 200 searches per turn, shared by all agents, was used up). I stopped there and did not work around it. Everything below comes from 10 searches only.

What worked: 10 WebSearch calls (cached in cache/01-lovable-searches.md). Trustpilot, vendor guides, Lovable's own blog and docs, security write-ups showed up.
What was blocked:
- reddit.com as an allowed domain: tool error 400, "not accessible to our user agent". No Reddit thread was read. Reddit appeared in no result.
- WebFetch on thenextweb.com: ENOTFOUND (one attempt, as the notes allow).
- 3 searches (HN, Indie Hackers, community.lovable.dev) were refused by the budget limit. These sources are NOT covered: Hacker News, Indie Hackers, X, YouTube, Lovable community forum, Medium, "hire a developer" asks, Discord.
- Not covered at all: r/lovable, r/vibecoding, r/nocode, r/SaaS.

Important limit on quotes: the search tool returns a tool-written summary plus a link list, not raw page snippets. Only a few phrases appear inside quotation marks in the output. Source text for everything here is: search result summary. Verifiers: no full page was opened.

Bottom line: this track is THIN. It confirms what breaks and the credit-loop pain from third-party sources. It found ZERO first-person "I would pay $X" buyer posts. Do not treat the demand signal as proven by this track.

## 2. Key findings

1. Stall point is described as around 70 to 80% done, on auth, security rules (RLS), and payments/webhooks. Only vendor/blog sources say this. Nothing from a buyer in my results.
   Grade: weak | Type: vendor marketing | Link: dev.to/lakshya_pareek/hire-lovable-developer-the-complete-2026-guide-for-founders-and-startups-2ob7 ; azumo.com/artificial-intelligence/ai-insights/lovable-ai-limitations-benefits | Date: 2026 (exact date unknown) | Cache: QUERY "Lovable app "70%" done last 30%..."

2. Credit burn from "Try to Fix" loops is a repeated complaint. One guide says users spend $15 to $70+ in a loop. Trustpilot reviewers say the AI repeats the same errors and costs them credits.
   Grade: moderate (two kinds of source agree, but both are snippets via summary) | Type: first-person anecdote (Trustpilot) + vendor marketing (guides by RapidDevelopers / VP0, who sell fixes) | Link: uk.trustpilot.com/review/lovable.dev?page=9 ; vp0.com/blogs/lovable-app-not-working-how-to-fix-common-errors ; rapidevelopers.com/md/ai-build-errors/something-went-wrong-while-generating-the-app | Date: unknown | Cache: QUERY "Lovable "ran out of credits"..."

3. Refunds: Trustpilot reviewers say Lovable denies refunds for glitches or lost work hours, and one needed about 3 days to get a refund on unused credits. Support is described as slow (5 days of silence on a domain verification issue) and often a bot. Implication: unhappy buyers have no help from the platform for code-level problems.
   Grade: weak to moderate (summary only, reviews undated in output, paraphrased by the tool) | Type: first-person anecdote | Link: ca.trustpilot.com/review/lovable.dev?page=6 ; au.trustpilot.com/review/lovable.dev?page=4 ; nz.trustpilot.com/review/lovable.dev?page=10 | Cache: QUERY "Lovable Trustpilot review spent credits..."
   Also: a guide says broken forms, layout issues and silent integration failures are outside Lovable support's scope (vendor: rapidevelopers.com/lovable-issues/lovable-support-guide).

4. Security is the best-documented breakage. CVE-2025-48757: a researcher scanned 1,645 apps from Lovable's showcase and found 170 (10.3%) had critical RLS failures that let anyone read data with the public anon key. Separate 2026 platform bug (Feb 3 to Apr 20, 2026) let anyone with a link read chat history and source of public projects; one write-up claims a wider scope (flagged: treat with caution). A dev.to post scanned 15 public Lovable apps and reports 40% load their database in the browser (title only).
   Grade: moderate (several independent write-ups agree on the 170/1,645 figure; several are from security firms that sell audits) | Type: independent data (researcher scan) + vendor marketing (Superblocks, Bastion) | Link: superblocks.com/blog/lovable-rls-breach ; cvemon.intruder.io/cves/CVE-2025-48757 ; bastion.tech/blog/lovable-april-2026-data-breach ; dev.to/romain_durieux_f617a147f5/i-scanned-15-public-lovable-apps-40-load-their-database-in-the-browser-3c2p | Date: 2025 and 2026 | Cache: QUERY "lovable" "supabase" RLS broken...
   Note: track 11 owns security depth.

5. Stripe/webhooks: Lovable's own docs point builders to Supabase edge function logs and Stripe webhook logs; the Stripe docs page is marked deprecated. Common failure given: webhook secret mismatch. Payments do not work in preview; must test after deploy. Fiverr sellers sell exactly this fix.
   Grade: moderate | Type: vendor marketing (Lovable docs, VP0, Fiverr sellers) | Link: docs.lovable.dev/integrations/stripe ; lovable.dev/faq/backend/payments/verify-stripe-webhooks ; fiverr.com/hussainsdev/fix-lovable-ai-supabase-auth-rls-stripe-webhook-and-deployment-errors | Cache: QUERY "lovable" stripe webhook not working...

6. What builders try next (as described by sellers, not buyers): reload version history, duplicate the project, post in Lovable Discord (peer-to-peer, not an official hiring channel), export to GitHub and hand the repo to a contractor.
   Grade: weak | Type: vendor marketing | Link: rapidevelopers.com/lovable-issues/hiring-a-lovable-developer ; azumo.com (above) | Cache: QUERIES 1 and 5 in cache file

7. Prior claim "About 80% of Lovable's builders are non-technical (The Next Web, May 2026)": PARTLY CONFIRMED, date looks wrong. The figure comes from Lovable's own "A first look at the build economy" report, published 9 June 2026 per the search summary (lovable.dev/blog/a-first-look-at-the-build-economy). The Next Web covered it under the title "Lovable hit $500 million in revenue with 146 employees. Its new data shows who is actually building software now." (thenextweb.com/news/lovable-build-economy-500m-arr-vibe-coding). Lovable's phrasing, per the summary: 80% of builders are in [PARAPHRASE, NOT VERBATIM] "self-identified non-technical roles", also "4 in 5". The data are usage data Jan 2025 to May 2026 plus a May 2026 user survey; this is likely where "May 2026" came from, not the article date. TNW coverage reportedly says the figures are not independently audited and that surveying active users skews to enthusiasts. I could not open the TNW page, so I do NOT have the article's own sentence or its date. Exact wording of the TNW sentence: NOT VERIFIED.
   Grade: moderate (figure exists, company self-reported) | Type: vendor marketing (Lovable self-reported) with an independent news outlet repeating it | Cache: QUERIES "80%" Lovable builders non-technical The Next Web ; Lovable build economy report "non-technical" "4 in 5" builders

8. Scale context: Lovable claims $500M ARR, 146 employees, 720M monthly visits to Lovable-built projects, 8 in 10 users plan to monetise, 50M projects (communityone.io, June 2026 headline), 60M projects (other outlet), valuation about $13.3B after a $400M round (Spanish-language outlet, unverified). Large pool of builders, but this says nothing on how many are stuck.
   Grade: moderate | Type: vendor marketing | Cache: QUERIES 3, 4 and "vibe coding Lovable I hired" in cache file

9. Hiring a human: agency guide (RapidDevelopers, a seller) says freelance Lovable developers cost $50 to $150 an hour or $5,000 to $15,000 per project, and agencies $13,000 to $25,000 for a full production build. A seller view of price, not what buyers paid.
   Grade: weak | Type: vendor marketing | Link: rapidevelopers.com/lovable-issues/hiring-a-lovable-developer | Cache: QUERY 1

10. NOT found: any post where a Lovable user asks "where can I hire a developer to finish my Lovable app". Search could not reach Reddit, HN, IH, X, or Lovable's forum. Absence here is a tool limit, not evidence of no demand.
   Grade: n/a | Type: n/a

## 3. Buyer quotes
Only one usable item. No Reddit, HN, IH, X or forum buyer quotes could be retrieved.

- Quote: "the AI repeated the same coding errors, forcing me to spend thousands of dollars on credits just to resolve the same persistent issues."
- Username: unknown (Trustpilot reviewer)
- Site: Trustpilot (Lovable reviews, uk.trustpilot.com page 9 appeared in results)
- Date: unknown
- Upvotes or likes: unknown
- Link: https://uk.trustpilot.com/review/lovable.dev?page=9 (the exact page that carries this review is not certain; the result list also had au.trustpilot.com page 5 and nz page 2)
- Buyer tag: product stage unknown; paying users unknown; revenue unknown; funding unknown; spend stated as "thousands of dollars on credits" (self-reported, unverified); country unknown
- Cache file: cache/01-lovable-searches.md, QUERY: Lovable "ran out of credits" app still broken burned credits fixing same bug
- Source text: search snippet (text appeared in parentheses inside the tool summary; it may be a paraphrase by the tool, so verifiers should treat as lightly supported)

Paraphrases (NOT quotes, no quotation marks): other Trustpilot reviewers, unnamed and undated, said credits disappear fast, the agent uses credits even for apologies, support took 5 days on a domain verification problem, refunds were refused for software glitches. Source: cache entry QUERY: Lovable Trustpilot review spent credits app never worked "support" refund. Count of distinct such reviewers: about 5 to 6, from a partial summary.

## 4. Seller quotes
Bias flag: these sellers earn money when builders believe they are stuck. Treat as marketing.

- Quote: "Users report spending $15-$70+ in cascading error loops."
- Username: unknown (guide author; domain RapidDevelopers or VP0, the tool did not say which)
- Site: vendor blog (vp0.com / rapidevelopers.com)
- Date: unknown
- Upvotes or likes: n/a
- Link: https://vp0.com/blogs/lovable-app-not-working-how-to-fix-common-errors ; https://www.rapidevelopers.com/md/ai-build-errors/something-went-wrong-while-generating-the-app
- Seller tag: agency / dev shop selling Lovable fixes
- Cache file: cache/01-lovable-searches.md, QUERY: Lovable "ran out of credits" app still broken burned credits fixing same bug

- Quote: "clicking 'Try to Fix' creates new bugs that trigger more errors, each consuming credits."
- Same source and cache entry as above.

- Quote (title of a Fiverr gig): "I will fix lovable supabase auth rls stripe and webhook errors"
- Username: hussainsdev (Fiverr seller handle in the URL)
- Site: Fiverr
- Date: unknown
- Link: https://fiverr.com/hussainsdev/fix-lovable-ai-supabase-auth-rls-stripe-webhook-and-deployment-errors
- Seller tag: freelancer; price not shown in result
- Cache file: cache/01-lovable-searches.md, QUERY: "lovable" stripe webhook not working edge function founder asking for help paid developer

- Quote (title of a Fiverr gig): "I will run a supabase rls security audit and fix data leaks in lovable base44"
- Username: ephraim_vibe
- Site: Fiverr; Link: https://fiverr.com/ephraim_vibe/fix-bugs-deploy-and-migrate-lovable-base44-replit-app-to-wordpress-or-shopify
- Seller tag: freelancer; price not shown
- Cache file: cache/01-lovable-searches.md, QUERY: "lovable" "supabase" RLS broken security exposed apps

- Quote (title of a Fiverr gig): "I will lovable expert fix lovable app bugs supabase stripe deploy lovable ai"
- Username: meshbola115
- Site: Fiverr; Link: https://fiverr.com/meshbola115/lovable-expert-fix-lovable-app-bugs-supabase-stripe-deploy-lovable-ai
- Seller tag: freelancer; price not shown
- Cache file: cache/01-lovable-searches.md, QUERY: lovable app stuck "hire a developer" to finish reddit r/lovable

## 5. Numbers found

| number | what it measures | source link | date | type | grade |
|---|---|---|---|---|---|
| 80% / "4 in 5" | share of Lovable builders in self-identified non-technical roles | lovable.dev/blog/a-first-look-at-the-build-economy ; thenextweb.com/news/lovable-build-economy-500m-arr-vibe-coding | report 2026-06-09 (per search summary) | vendor (self-reported), repeated by news | moderate |
| 720 million | average monthly visits to Lovable-built projects | same | 2026-06 | vendor | moderate |
| 8 in 10 | users who plan to monetise | same | 2026-06 | vendor, survey | weak |
| $500M ARR, 146 employees | Lovable revenue, headcount | thenextweb.com title + summary | 2026 | vendor via news | moderate |
| 50M / 60M projects | projects built on Lovable (two different figures from two outlets) | communityone.io (title "50M Projects Built on Lovable", dated 2026-06-09 in URL); ecosistemastartup.com | 2026 | vendor | weak (figures disagree) |
| about $13.3B, $400M round | Lovable valuation, round | ecosistemastartup.com (Spanish) | 2026 | news, unverified | weak |
| 1,645 apps scanned, 170 with critical RLS failures (10.3%) | security scan of Lovable showcase apps | superblocks.com/blog/lovable-rls-breach ; cvemon.intruder.io/cves/CVE-2025-48757 | 2025 | independent research (via security-firm write-ups) | moderate |
| 18,697 user records | one featured app exposed, Feb 2026, attributed to an inverted auth check | superblocks / summary | 2026-02 | vendor write-up | weak |
| Feb 3 to Apr 20, 2026 | window of platform BOLA-type bug exposing public projects' chat and code | bastion.tech/blog/lovable-april-2026-data-breach | 2026-04 | vendor write-up | weak to moderate |
| 40% of 15 scanned apps | public Lovable apps loading DB in browser | dev.to (title only) | unknown | anecdote | weak |
| $15 to $70+ | credit spend reported in "Try to Fix" loops | vp0.com / rapidevelopers.com | unknown | vendor | weak |
| "thousands of dollars" | one Trustpilot reviewer's credit spend | uk.trustpilot.com (page 9) | unknown | anecdote | weak |
| 3 days, "50%+ credits used" | one reviewer's refund delay and a stated refund rule | trustpilot (ca/ie/nz pages) | unknown | anecdote | weak |
| 5 days | support silence on a domain verification problem | trustpilot | unknown | anecdote | weak |
| $50 to $150/hour; $5,000 to $15,000 per project (freelancers); $13,000 to $25,000 (agencies, full build) | seller price lists for Lovable developers | rapidevelopers.com/lovable-issues/hiring-a-lovable-developer | unknown | vendor | weak |
| 0 | buyer posts found asking to hire a dev | n/a | 2026-10-20 | n/a | tool limit |

Counts for this track (from search results, partial): [UNVERIFIED] 10 searches run, 3 blocked by budget, 1 domain rejected, 1 fetch failed. Threads found: 0 Reddit / 0 HN / 0 IH / 0 X / 0 forum. Distinct buyer voices with any quote text: 1 (plus about 5 to 6 paraphrased, unnamed Trustpilot reviewers). Distinct seller voices: about 8 domains/handles (RapidDevelopers, VP0, Azumo, Superblocks, Bastion, lowcode.agency, 3 Fiverr handles). Dates: almost all unknown; only the build economy report (2026-06-09) and incident windows have dates.

## 6. What this means for the offer
- The pain is real but the buyer evidence here is thin: credits wasted, loops, and security. A paid audit that starts with RLS, auth, Stripe webhooks and secrets is the most defensible first step, since those are the same fixes sellers already list.
- Platform support does not fix app code, and refunds for platform glitches are reported as denied. This is the gap a human rescuer fills, but it needs buyer proof from Reddit/HN/IH that I could not get.
- Prices seen are sellers' lists ($5k to $15k projects, $50 to $150/hour), well above the $30 to $500 gigs, but they are not what buyers paid. Do not size the offer on them without real buyer data.

## 7. What this means for the GO gates
- Gate 1 (buyers paying $1,500+): unclear. Only seller price lists found, no buyer receipts.
- Gate 2 (cost per client under 30%): unclear. This track has no channel data.
- Gate 3 (repeatable fix list): supports, weakly. Same items recur across sources: RLS/policies, auth, Stripe webhooks, edge function secrets, credit loops. Track 11 should confirm.
- Gate 4 (position above the floor): unclear. Many Fiverr gigs exist for these exact fixes; prices not captured.
- Gate 5 (platform improvements erase demand in 12 months): unclear. Lovable has shipped security scanning and a Partner Program (title seen: lovable.dev/blog/introducing-lovable-partner-program), which is a possible competitor and channel; track 9 should read it. Not opened here.

## 8. Machine-readable block
```json
{"track": "01-lovable-builders", "demand_signal": "weak", "buyer_price_points_usd": [], "seller_price_points_usd": [50, 150, 5000, 15000, 13000, 25000], "gates_supported": [3], "gates_contradicted": [], "evidence_grade": "weak", "sources_read": 10, "buyer_quotes": 1, "seller_quotes": 5}
```
Note on "demand_signal": rated weak because of coverage, not because demand was disproved. Reddit, HN, IH, X and the Lovable forum were not reachable. A rerun with those sources is needed before relying on this track.

## Appendix: unverified items
(Verifier 1, 2026-10-20. Cache = cache/*.md. Full log: verification-log-1.md.)

FAILED (not in cache / number differs):
- Counts line "10 searches run": cache/01 holds 9 result sets plus 1 domain error (number differs).

DOWNGRADED:
- "self-identified non-technical roles" (key finding 7): in cache/01 only inside the tool summary, not in quotation marks.
