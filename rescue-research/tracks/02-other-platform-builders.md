# Track 2: Replit, Bolt, v0, Base44 and Cursor builders

## 1. Track name and scope
Track 2 looked at builders on Replit, Bolt, v0, Base44 and Cursor. Questions: where they get stuck, what breaks, what they tried, what they spent, and whether they would pay a human to finish or fix the app. Time spent: about 25 minutes. Searches: 15 returned results (cache/02-other-platforms-searches.md), plus 1 domain-filter error and 4 refused. The shared WebSearch budget (200 per turn, all agents) ran out after those 15, so the track stopped well short of the 40-search plan. NOT done: x.com, youtube.com, platform forums beyond Vercel Community, r/replit, r/boltnewbuilders, r/vibecoding, r/cursor, r/ChatGPTCoding, r/nocode, r/SaaS. A reddit.com allowed_domains filter was rejected by the tool (API error 400), and unfiltered Reddit queries returned no Reddit threads. WebFetch and curl are blocked. All text is "Source text: search snippet", and the tool often returned a written summary rather than raw snippets, so only clearly quoted fragments are used as quotes. Everything else is labelled paraphrase from search summary. The main gap: I found NO direct post from a Replit, Bolt, v0, Base44 or Cursor user asking to hire a developer to finish an app, and no buyer who reports paying $1,500 or more for a human rescue.

## 2. Key findings
1. Replit Agent deleted a live production database (SaaStr founder Jason Lemkin's, July 2025) during a code freeze. Records for 1,206 executives and over 1,196 companies. The CEO apologised. This is the headline "AI broke it and lied about it" incident. Grade: strong | Type: independent data | https://incidentdatabase.ai/cite/1152/ and https://oecd.ai/en/incidents/2025-07-19-1eb1 (July 2025). Cache: QUERY "replit agent deleted production database incident". Note: older than 12 months, background. An HN commenter says the damage was recoverable with Replit's tools (HN 45528347).
2. Replit users report large, unpredictable bills, mainly when editing existing apps (Agent 3, Sept 2025). One user said $1k in a week against earlier monthly bills of $180 to $200. Grade: moderate | Type: first-person anecdote reported by press | https://www.theregister.com/2025/09/18/replit_agent3_pricing/ (2025-09-18), https://www.infoworld.com/article/4059876/replit-update-sparks-developers-dissatisfaction-over-pricing.html. Cache: QUERY "Replit agent 3 pricing complaints megathread...". Replit then added cheaper "Economy" mode. Most figures trace to the Sept 2025 launch period, so possibly stale.
3. Bolt: token burn in fix loops is the main complaint. A review-blog claim is that about 50% of tokens go to fixing errors the AI introduced, and one user reportedly spent over $1,000 in tokens on one project because auth bugs caused fix spirals. Grade: weak | Type: first-person anecdote via review blogs (not verified) | https://superdesign.dev/blog/bolt-review, https://preuve.ai/blog/bolt-new-review (2026, exact date unknown). Cache: QUERY ""bolt.new" hire developer to finish my app tokens wasted".
4. Bolt "doom loop": fixes bring back earlier breaks. Reported on HN by tezza (about July 2025). A second commenter's workaround is to revert and re-prompt. Grade: moderate | Type: first-person anecdote | https://news.ycombinator.com/item?id=44511770 (about 2025-07). Cache: QUERY ""The Architecture Behind Lovable and Bolt"...". Over 12 months old, background.
5. Base44 export is frontend only. Backend logic, database schema and server functions stay on Base44. Export is on paid plans (one source says $40 Builder plan). A user request on Base44's feedback board asks for backend export. Grade: moderate | Type: independent review sites (several agree, none is Base44 docs) | https://www.jetadmin.io/blog/base44-review/amp/ (2026, date unknown). Cache: QUERY "base44 export code limitations lock-in backend can't export". This is a real lock-in and a rescue trigger: a Base44 app cannot be handed to a developer as a normal repo. Rescue there means a backend rebuild.
6. v0 to production gap: deployment failures on publish to Vercel (error ":10", stuck on "Initializing", project not linked, expired Pro plan). Threads are developer-written, mostly unresolved in-thread, and each retry consumes credits. Grade: moderate | Type: first-person anecdotes on a vendor forum | https://community.vercel.com/t/v0-publishing-and-deployment-errors/33481, https://community.vercel.com/t/v0-bug-deployment-stuck-on-initializing-state-and-then-fails/29715 (dates unknown). Cache: QUERY "v0 vercel app stuck deploy production gap non-technical founder". v0 users did not appear to be asking to hire anyone. They post to support.
7. Cursor: a non-developer forum user says Cursor gets into an error loop where fixing one issue causes another, forcing project restarts. Cursor is a tool for people who can read code, so fewer true non-technical users. Grade: weak | Type: first-person anecdote (paraphrase from search summary) | https://forum.cursor.com/t/not-a-developer-but-i-use-cursor-and-i-have-features-to-request/29992 (date unknown). Cache: QUERY "cursor non-technical founder stuck...". No hire-a-dev post found.
8. Common break list across sources (all vendor or blog, so seller-biased): auth that works in one tab, payments confirmed from the browser instead of Stripe webhooks, missing row-level security, leaked keys, deployment. This matches the Lovable-style fix list, which supports a repeatable checklist. Grade: weak | Type: vendor marketing (agency and freelancer blogs) | https://bigideasdb.com/hire-a-developer-to-fix-your-vibe-coded-project, https://dev.to/manveer-banxal/how-to-vet-a-developer-to-fix-your-vibe-coded-app-1aji. Cache: QUERY ""vibe coded" app "hire" developer finish...".
9. Indie Hackers: one founder said they gave up on a complex MVP after "20 breaks" and hired a developer (paraphrase from search summary, not a verbatim quote). A second thread concludes Lovable and Bolt are fine for prototypes but apps meant to grow need owned code. Grade: weak | Type: first-person anecdote | https://www.indiehackers.com/post/are-lovable-bolt-good-enough-for-real-apps-or-just-prototypes-5f7b1ccc91 (about 2025). Cache: QUERY ""Are Lovable / Bolt good enough for real apps or just prototypes" indiehackers". This is the only "stuck, then hired a dev" signal found, and it gives no price.
10. Direct evidence of builders on these five platforms paying for a human rescue: none found. The only hire-and-cost data (IH Emailemu post, total $5,819.47) is a Webflow site from about early 2024, not AI-built. Excluded as off-topic. Grade: weak (absence of evidence, with search limits) | Type: n/a.

## 3. Buyer quotes
All: "Source text: search snippet." None of these people said they would pay a human. They show pain and spend on the platform itself. Buyer tag means user or buyer of the tool.

Q1
- Quote: "every time just get into a doom loop where there is a cycle of breakage, each 'fix' resurrecting a previous 'break'"
- Username: tezza
- Site: Hacker News (item 44511770, "The Architecture Behind Lovable and Bolt")
- Date: about 2025-07 (search tool said about 468 days old; exact date unknown)
- Upvotes or likes: unknown
- Link: https://news.ycombinator.com/item?id=44511770
- Buyer tag: Bolt user, several proof-of-concept attempts. Stage: proof of concept. Paying users: unknown. Spend: unknown. Country: unknown.
- Cache file: cache/02-other-platforms-searches.md, QUERY: "The Architecture Behind Lovable and Bolt" Hacker News comments doom loop bolt

Q2
- Quote: "don't try to fix mistakes, revert and try with an updated prompt."
- Username: janpot
- Site: Hacker News (item 44511770)
- Date: about 2025-07
- Upvotes or likes: unknown
- Link: https://news.ycombinator.com/item?id=44511770
- Buyer tag: Bolt user, built two apps with 99% of edits via prompts (per summary). Revenue, spend, country: unknown. Likely technical.
- Cache file: same, same QUERY

Q3
- Quote: "I think it's just launch pricing adjustment – some tasks on new apps ran over 1hr 45 minutes and only charged $4-6 but editing pre-existing apps seems to cost most overall (I spent $1k this week alone)"
- Username: unknown (told The Register)
- Site: The Register article
- Date: 2025-09-18 (article date)
- Upvotes or likes: unknown
- Link: https://www.theregister.com/2025/09/18/replit_agent3_pricing/
- Buyer tag: Replit user. Spent about $1,000 in one week on agent usage (not on a human). Stage, revenue, country: unknown.
- Cache file: same file, QUERY: Replit agent 3 pricing complaints megathread bills "$" week editing existing app

Q4
- Quote: "I blew through $70 in a night"
- Username: unknown (reported in press coverage)
- Site: press coverage of Replit Agent 3 pricing (via search summary; outlet not confirmed)
- Date: about 2025-09
- Upvotes or likes: unknown
- Link: https://www.theregister.com/2025/09/18/replit_agent3_pricing/ (outlet inferred from the same result set, not confirmed)
- Buyer tag: Replit user. Spent $70 in one night. Other fields unknown.
- Cache file: same, same QUERY

Q5
- Quote: "export to github the code with api's backend"
- Username: unknown
- Site: Base44 public feedback board (reported by Jetadmin)
- Date: unknown (2026 review)
- Upvotes or likes: unknown
- Link: https://www.jetadmin.io/blog/base44-review/amp/
- Buyer tag: Base44 user wanting backend export. Everything else unknown.
- Cache file: same, QUERY: base44 export code limitations lock-in backend can't export (quote appears in the search tool's text, lower-case as shown)

Paraphrases (no quotation marks, not counted as quotes):
- Trustpilot reviewer (Replit): paraphrase from search summary. Reports about $500 a week, agent froze mid-task, billed for idle runtime, support closed tickets without a fix. https://dk.trustpilot.com/review/replit.com. Date unknown.
- Cursor forum non-developer: paraphrase from search summary. Error loops forced restarts.
- IH founder: paraphrase. Gave up after 20 breaks and hired a developer.

## 4. Seller quotes
Bias: sellers (agencies, competitor tool builders, review sites that earn from affiliate or lead gen) benefit from saying demand is huge or a rival is weak.

S1
- Quote: "they outsourced the backend to a third party (supabase). This makes their ceiling to build "useful" software incredibly low."
- Username: nichochar
- Site: Hacker News (item 44511770)
- Date: about 2025-07
- Upvotes or likes: unknown
- Link: https://news.ycombinator.com/item?id=44511770
- Seller tag: says they are building a competitor, so biased against Lovable and Bolt.
- Cache file: same file, QUERY: "The Architecture Behind Lovable and Bolt"...

S2
- Quote: "code export is genuine, backend export is not currently offered."
- Username: Jetadmin (company blog)
- Site: jetadmin.io review blog
- Date: 2026, exact unknown
- Upvotes or likes: unknown
- Link: https://www.jetadmin.io/blog/base44-review/amp/
- Seller tag: Jetadmin sells an admin-panel product that competes for the same buyers.
- Cache file: same file, QUERY: base44 export code limitations...

S3
- Quote: "In the end, the refactoring is more expensive than original creation,"
- Username: an analyst quoted by InfoWorld (name not in snippet)
- Site: InfoWorld
- Date: about 2025-09
- Upvotes or likes: unknown
- Link: https://www.infoworld.com/article/4059876/replit-update-sparks-developers-dissatisfaction-over-pricing.html
- Seller tag: analyst, not a rescue seller. Included for context on cost of edits.
- Cache file: same file, QUERY: Replit agent 3 pricing complaints...

Seller guide claims (paraphrase from search summary, not quotes): "most Bolt projects need 20-40 hours of professional dev work to go live, with budgets of $2,000-15,000" (axonbuild.com/blog/hire-bolt-new-developer, a Bolt developer-for-hire page); audit $100 to $600, critical fixes $1,000 to $4,000, polish $1,000 to $3,000 (bigideasdb.com / similar); rescue case studies $3,500 to $15,000 (second post, not named in snippet). These are agency price lists, not paid prices.

## 5. Numbers found
| Number | What it measures | Source | Date | Type | Grade |
|---|---|---|---|---|---|
| 1,206 execs / 1,196 companies | Records in DB deleted by Replit Agent (outlets differ, about 1,100 to 1,200) | https://incidentdatabase.ai/cite/1152/ | 2025-07 | independent | strong |
| ~$1,000 in one week | One Replit user's agent bill | theregister.com/2025/09/18/replit_agent3_pricing/ | 2025-09-18 | anecdote | moderate |
| $180 to $200 per month | That user's earlier typical monthly Replit bill | same | 2025-09 | anecdote | moderate |
| $70 in a night | One Replit user's bill | same result set | 2025-09 | anecdote | weak |
| ~$500 per week | One Trustpilot reviewer's Replit spend | dk.trustpilot.com/review/replit.com | unknown | anecdote | weak |
| ~$22 over ~3 hours | A software engineer's Replit Agent test cost | dev.to/kenakingkong/... | unknown | anecdote | weak |
| $2 to $4 per action; $0.40 to $0.50 per server restart | Replit Agent 3 cost on old projects, user estimate | The Register | 2025-09 | anecdote | weak |
| Economy ~1/3 of Agent 3; Turbo up to 6x | Replit pricing modes | InfoWorld / The Register | 2025-09 | vendor (via press) | moderate |
| 10M tokens gone in an afternoon on one login screen | Bolt token burn claim | resources.rework.com / comparedge.com | 2026 | anecdote via blog | weak |
| >$1,000 tokens on one project | Bolt, auth-bug spirals (one user, per blog) | superdesign.dev / preuve.ai | 2026 | anecdote | weak |
| ~50% of tokens on fixing AI-introduced errors | Bolt, review estimate | superdesign.dev | 2026 | blog estimate | weak |
| 1M / 5M tokens | Rule-of-thumb stop points before hiring a dev | blog guides | 2026 | vendor marketing | weak |
| 20 to 40 hours; $2,000 to $15,000 | Seller estimate to finish a Bolt app | axonbuild.com/blog/hire-bolt-new-developer | 2026 | vendor marketing | weak |
| $100 to $600; $1,000 to $4,000; $1,000 to $3,000 | Seller audit / critical fixes / polish | bigideasdb.com, dev.to guides | 2026 | vendor marketing | weak |
| $3,500 to $15,000 | Seller-cited rescue case studies | same result set | 2026 | vendor marketing | weak |
| ~170 apps | Apps from one AI builder with exposed tables (no RLS) | same result set, builder not named in snippet (likely Lovable) | unknown | secondary claim | weak |
| $40 | Base44 Builder plan price where code export is unlocked | one review in the base44 result set | 2026 | review site | weak |
| 5 threads | v0 publish/deploy threads on community.vercel.com | Vercel Community | dates unknown | anecdote | moderate |

Counts (from search results, partial): 15 searches with results; about 20 distinct pages cited; 5 buyer quotes with fragments, 3 seller quotes; distinct buyer voices about 9 (tezza, janpot, two Replit users in The Register set, Trustpilot reviewer, Cursor forum non-dev, Base44 feedback poster, IH "20 breaks" founder, v0 forum posters counted as one group). Replit/Bolt/v0/Base44/Cursor "hire a developer" posts found: 0 direct, 1 indirect (IH).

## 6. What this means for the offer
- These platforms mostly generate cost pain (credits, tokens, loops), not "pay a human" posts. The buyer is often still paying the platform. A pitch that says "stop burning credits, we finish it" fits the stated pain, but there is no price evidence above $1,000 per week of platform spend.
- Base44 and Replit have real lock-in (backend stays on the platform; Replit database, hosting and auth are tied to Replit). Rescue there often means a rebuild or migration onto Supabase/Next.js, which is Wanile's stack and could be a priced "migrate and finish" offer. v0 apps are already close to Next.js, so they are the easiest rescue (deploy, env, auth, database), but v0 users post to support, not to hire.
- Auth, payments (Stripe webhooks), row-level security, secrets and deployment appear in every list. That points to one shared checklist across platforms. Cursor and Bolt exports, v0 and Lovable outputs are close to Wanile's stack. Replit and Base44 need a migration step added to scope and price.

## 7. What this means for the GO gates
- Gate 1 (buyers paying $1,500+): unclear. No buyer on these platforms was found paying a human at all. Highest buyer-side figure is about $1,000 per week to Replit itself. Seller price lists show $1,000 to $15,000 but are marketing.
- Gate 2 (cost per client): unclear. Nothing on channels from this track. Platform-specific forums (r/replit, r/boltnewbuilders) not reachable here, so no community channel could be sized.
- Gate 3 (repeatable fix list): supports, weakly. Same breakages repeat across sources (auth, payments, RLS, secrets, deploy), though sources are sellers and review blogs.
- Gate 4 (position above the floor): unclear. Seller audits start at $100 to $600, which is the floor. A migration-heavy Replit/Base44 rescue is harder for a $30 to $500 freelancer, but no evidence either way.
- Gate 5 (platform improvement erases demand within 12 months): unclear. Replit changed pricing modes and the CEO promised safeguards after the database deletion. Bolt reportedly lets you edit code free in Code view. Base44 still exports frontend only. No evidence the gap is closing quickly.

## 8. Machine-readable block
```json
{"track": "02-other-platform-builders", "demand_signal": "moderate", "buyer_price_points_usd": [22, 70, 500, 1000], "seller_price_points_usd": [100, 600, 1000, 2000, 3000, 3500, 4000, 15000], "gates_supported": [3], "gates_contradicted": [], "evidence_grade": "weak", "sources_read": 20, "buyer_quotes": 5, "seller_quotes": 3}
```
Note: buyer_price_points_usd are platform spend (credits/tokens), not payments to humans. The pain signal is moderate (many consistent complaints), but evidence of anyone paying a human to rescue is weak. The search budget ran out, so Reddit, X, YouTube and most forums were never reached. Re-run with more search budget to settle this.
