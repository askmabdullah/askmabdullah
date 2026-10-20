# Track 4: Founders burned by cheap freelancers or agencies who used AI

Status: PARTIAL. Stopped at 9 successful searches (budget was about 40) because the shared WebSearch limit (200 per turn, shared by all agents) ran out. Everything below is thin. Do not treat this track as a verdict on demand.

## 1. Track name and scope
Track 4. Founders and small businesses who paid a cheap freelancer or agency, got AI-generated or broken work, and then paid again. Also agencies that over-promised with AI.

Looked at (via WebSearch only): HN (via search snippets), Indie Hackers, Upwork forum, G2, news and vendor blogs. Cache: cache/04-burned-searches.md.

Counts: 9 successful searches. 2 refused (reddit.com is not accessible to the search tool: API Error 400). 4 refused (shared search budget used up). 1 WebFetch attempt failed (DNS). No pages were opened. Time: well under 60 minutes.

Blocked or not done: Reddit (r/Upwork, r/Fiverr, r/freelance, r/Entrepreneur, r/startups, r/SaaS, r/webdev, r/ExperiencedDevs) not reached at all. X not searched. Clutch, Trustpilot and YouTube not searched. The search tool returns a model-written summary plus links, not raw page snippets. So almost nothing here is a verbatim buyer quote. All quotes below are labelled "Source text: search snippet" and may sit inside a tool summary.

## 2. Key findings
1. Buyer accounts of "paid a freelancer, got AI output or nothing" exist, but I found only three, all paraphrased by the search tool: a G2 review (paid $1,000 for a website rebuild, got a mostly AI-generated document, freelancer kept $650 and locked them out), an Upwork forum post (paid for 25 hours of iOS work, no finished app, freelancer stopped replying to refund request), and a DevGenius post (freelancer used ChatGPT to rewrite code, result did not work). These are small-ticket and mostly not funded startups.
   Grade: weak | Type: first-person anecdote | https://g2.com/products/upwork/reviews/upwork-review-11073150 (undated), https://community.upwork.com/t5/Clients/Chase-money-back/m-p/1523377 (undated), https://blog.devgenius.io/dont-hire-a-python-freelance-before-read-it-f940f8587f59 (undated). Cache: QUERY "upwork freelancer used ChatGPT delivered broken code client refund founder story 2026".
2. Rebuild stories are told by agencies, not buyers. An agency's Indie Hackers post: a founder spent $5,000 and 2.5 months on a legal app with AI tools, new features broke old ones, agency chose a 2-month rebuild. A consultancy case study: a vibe-coded MVP with a "Stripe integration" that was a button, rebuilt in 6 weeks for $40K against another agency quote of $150K and 4 to 6 months. Both self-reported, unverified.
   Grade: weak | Type: vendor marketing | https://www.indiehackers.com/post/looking-for-founders-ready-to-hand-off-engineering-18af60a20a ; https://justinmckelvey.com/blog/vibe-code-rescue-case-study (dates unknown). Cache: QUERY "founder paid agency $ app built with AI unusable had to rebuild from scratch".
3. Nothing found on the freelancer's origin or country, or on how it changed buyer trust. No evidence found. No claims made.
   Grade: n/a | Type: n/a
4. Agencies that over-promised with AI and rescued their own work: no evidence found. One agency (Create Designs) reports clients arriving after ChatGPT-written code broke a site (see seller quotes). That is an agency cleaning up client DIY, not its own work.
   Grade: weak | Type: vendor marketing | https://www.yahoo.com/news/companies-tried-save-money-ai-100037041.html or the Yahoo "Desperate Companies" link (which one carries the text is not shown). Cache: QUERY "reddit r/startups ...".
5. A vendor guide says fixing and hardening a broken MVP "typically lands between $2,000 and $15,000+" (tool summary wording). This is the only second-time price range found for this track, and it comes from a vendor selling the fix.
   Grade: weak | Type: vendor marketing | https://bigideasdb.com/hire-a-developer-to-fix-your-vibe-coded-project (date unknown). Cache: QUERY "\"hired a developer\" \"vibe coded\" mess second developer fix".
6. Cleanup work is now a priced product. Slopfix (three people) charges $10,000 for one week, paid in proportion to code deleted, repo analysis free, two-week warranty. HN thread title: "We charge $10k a week to delete AI-generated code". Covered by TechRadar, Tom's Hardware, PC Gamer. Seller offer, not a buyer payment.
   Grade: moderate (offer is confirmed by several outlets; no buyer is shown paying) | Type: vendor marketing | https://news.ycombinator.com/item?id=48823359 (about mid-2026, brief says July 2026). Cache: QUERY "\"We charge $10k a week to delete AI-generated code\"".
7. Early proof that AI-using bidders are common on freelance sites: a 2023 hCaptcha experiment. 14 unique bids on a trap job post, 9 answered the screening question, all 9 answers came from an LLM and were wrong. Old (2023), background only.
   Grade: moderate | Type: independent data (as relayed by a tool summary) | https://forums.theregister.com/forum/all/2023/05/09/upwork_chatgpt_problem/ (2023-05-09). Cache: QUERY "reddit r/startups ...".
8. HN "Who wants to be hired" posts in 2026 advertise rescue of "broken or AI-generated codebases". That is supply, not demand.
   Grade: weak | Type: vendor marketing | https://news.ycombinator.com/item?id=49922568 (October 2026). Cache: QUERY "Hacker News Ask HN I hired contractors offshore ...".

## 3. Buyer quotes
Exact verbatim buyer quotes: NONE found. The search tool did not return raw page text for any buyer post. Reddit was blocked entirely.

Paraphrases from the tool summary (NOT quotes, do not quote them in the final report):
- G2 reviewer (small-business owner, paid $1,000 for a website rebuild, $650 paid, locked out, unresolved, Upwork mediation needs both sides to agree). Link: https://g2.com/products/upwork/reviews/upwork-review-11073150. Date: unknown. Country: unknown. Cache: QUERY "upwork freelancer used ChatGPT delivered broken code client refund founder story 2026".
- Upwork forum client "Chase money back" (paid for 25 hours of iOS development, no finished app, freelancer discouraged a dispute then went silent). Link: https://community.upwork.com/t5/Clients/Chase-money-back/m-p/1523377. Date, username, country, upvotes: unknown. Same cache query.
- DevGenius author (freelancer's ChatGPT rewrite of Python code did not work; author raised own rates). A developer, not a founder. Link: https://blog.devgenius.io/dont-hire-a-python-freelance-before-read-it-f940f8587f59. Same cache query.
- HN, 2019 thread "Ask HN: Client replaced me with offshore team" is a freelancer's view, not a buyer burned by AI. Skip.

## 4. Seller quotes
Bias flag: sellers of cleanup work gain from saying demand is large. Commenters below are of unknown role.
- Quote: "In one recent case, a client ended up going without a website for three days and having to pay Create Designs nearly $500 over a small line of code that ChatGPT had written for them."
  Username: unknown (web agency Create Designs, as named in text) | Site: news article via Yahoo | Date: unknown | Likes: unknown | Link: https://www.yahoo.com/news/articles/desperate-companies-now-hiring-humans-204421933.html (or the other Yahoo link in the same result; the source of this line is not shown) | Buyer tag: n/a, seller telling a client story. Client details unknown. Source text: search snippet (appears in parentheses inside the tool summary). Cache: cache/04-burned-searches.md, QUERY "reddit r/startups \"hired\" freelancer ...".
- Quote: "the speed at which AI-generated codebases grow is far in excess of what human developers can achieve. What took years to accumulate in the past can be produced in a few days/weeks."
  Username: unknown HN commenter | Site: HN, thread "Cleaning up after AI rockstar developers" | Date: unknown (thread about 132 days before 2026-10-21 per tool, roughly June 2026) | Likes: unknown | Link: https://news.ycombinator.com/item?id=48458586 | Tag: commenter, role unknown, not a buyer. Source text: search snippet. Cache: QUERY "\"Cleaning up after AI rockstar developers\" Hacker News".
- Quote: "Contractors are incredibly valuable in certain respects, but one thing they don't do generally is write code for future maintainability" (the tool's summary may have altered the ending; unverified wording).
  Username: unknown | Site: HN "Ask HN: Client replaced me with offshore team" | Date: 2019 (background only) | Link: https://news.ycombinator.com/item?id=20339344 | Tag: commenter, not a buyer. Cache: QUERY "Hacker News Ask HN I hired contractors offshore ...".

## 5. Numbers found
All from search results, partial. Source text: search snippet.

| number | what it measures | source link | date | type | grade |
|---|---|---|---|---|---|
| $1,000 paid, $650 kept by freelancer | one buyer's website rebuild loss | https://g2.com/products/upwork/reviews/upwork-review-11073150 | unknown | anecdote | weak |
| 25 hours | iOS dev paid, no finished app | https://community.upwork.com/t5/Clients/Chase-money-back/m-p/1523377 | unknown | anecdote | weak |
| about $500, 3 days offline | one agency client's fix after ChatGPT code | Yahoo link above | unknown | vendor | weak |
| $5,000 and 2.5 months | spent on AI tools for a legal app before rebuild | https://www.indiehackers.com/post/looking-for-founders-ready-to-hand-off-engineering-18af60a20a | unknown | vendor | weak |
| 2 months | agency rebuild time for that app (price not shown) | same | unknown | vendor | weak |
| $40K, 6 weeks vs $150K, 4 to 6 months | rebuild price and time vs another agency quote | https://justinmckelvey.com/blog/vibe-code-rescue-case-study | unknown | vendor | weak |
| $2,000 to $15,000+ | vendor's range to fix and harden a broken MVP | https://bigideasdb.com/hire-a-developer-to-fix-your-vibe-coded-project | unknown | vendor | weak |
| 2 to 6 hours | vendor's paid code audit length | same | unknown | vendor | weak |
| $10,000 per week | Slopfix price (HN title) | https://news.ycombinator.com/item?id=48823359 | 2026 (about July) | vendor | moderate |
| 100,000 to 35,000 lines | Slopfix example target | TechRadar / Tom's Hardware links in cache | 2026 | vendor | weak |
| 14 bids, 9 answered, 9 of 9 LLM and wrong | 2023 hCaptcha Upwork-style test | https://forums.theregister.com/forum/all/2023/05/09/upwork_chatgpt_problem/ | 2023-05-09 | independent (relayed) | moderate, old |
| $400 in tokens | one IH founder's token bill on a comment system | IH "Vibe-coding your MVP is free. Your token bill says otherwise" | unknown | anecdote | weak |
| 9 searches, 3 buyer paraphrases, 0 verbatim buyer quotes | this track's yield | cache/04-burned-searches.md | 2026-10-21 | n/a | n/a |

Not found: any buyer-stated price they accepted the second time; any count of burned-founder threads; any freelancer-origin data.

## 6. What this means for the offer
- The few buyer accounts are small money ($500 to $1,000) and the burned buyers look like small-business owners, not funded founders. Do not size the offer from them.
- Loss-averse buyers (paid, got nothing, no refund) likely want proof before paying again. A free or cheap diagnosis, written scope and a fixed price are consistent with what the vendor sources recommend (2 to 6 hour paid audit). This is a hypothesis, not tested here.
- $2,000 to $15,000+ and $10,000 per week are seller prices. No buyer is shown paying them in this track. Gate 1 still needs buyer proof from other tracks.

## 7. What this means for the GO gates
- Gate 1 (buyers paying $1,500+): unclear. Only seller prices found. Buyer losses seen were $500 to $5,000.
- Gate 4 (position above the low-cost floor): unclear. No evidence on how burned buyers judge a second vendor or on freelancer origin.
- Gates 2, 3, 5: not touched.

## 8. Machine-readable block
```json
{"track": "04-burned-by-freelancers", "demand_signal": "weak", "buyer_price_points_usd": [500, 650, 1000, 5000], "seller_price_points_usd": [2000, 15000, 10000, 40000, 150000], "gates_supported": [], "gates_contradicted": [], "evidence_grade": "weak", "sources_read": 9, "buyer_quotes": 0, "seller_quotes": 3}
```
Note on the JSON: buyer_price_points are what buyers reported LOSING (not paying the second time). seller_price_points include the $150K rival agency quote as a vendor claim. sources_read counts successful searches, not opened pages.
