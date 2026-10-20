# Track 15: Trust and geography

## 1. Track name and scope
Trust and geography: how US/UK/AU/CA buyers react to offshore and South Asian rescuers, what proof wins them over, which review platforms matter, how Pakistani agencies present location, and "burned by cheap offshore" sentiment.

STATUS: PARTIAL. Only 13 searches ran (11 returned results, 1 domain-blocked error, plus 3 more refused). The WebSearch budget shared by all agents (200 per turn) ran out, so 4 planned searches did not execute and about 20 more were never started. Cache: cache/15-trust-searches.md (all 13 entries logged).
Blocked or not possible: reddit.com is rejected as an allowed_domain ("not accessible to our user agent"), so Reddit threads were only reachable via open-web search, and none surfaced. No X, Quora, G2, GoodFirms, Trustpilot-for-agencies, or "money-back guarantee" searches were run. WebFetch and curl were not tried (network notes say blocked).
Important limit: the search tool mostly returned its own summary of pages, not page text. Per NETWORK-NOTES, those summaries are not quotes. So this file has NO verified buyer quotes. Everything below is paraphrase from search summaries unless marked as a title/snippet.
Time: roughly 15 minutes of the 60 minute budget.

## 2. Key findings
1. Buyer location bias against Pakistani and Indian developers exists but is documented only by anecdote and old forum threads. A Workana job post (May 2024) asked for South American developers and told India and Pakistan applicants not to apply. A Bubble forum hiring post said Pakistan was fine if the time zone was similar. No current (2025-26) buyer study found.
   Grade: weak | Type: first-person anecdote | https://www.workana.com/en/job/looking-for-individual-developers-must-be-from-south-america-no-indians-pakistanis ; https://forum.bubble.io/t/hiring-a-full-time-bubble-dev-for-madhupa-a-silver-agency/355054 | 2024 / unknown
   Cache: 15-trust-searches.md, QUERY "I don't want to hire from Pakistan" OR "no Indian or Pakistani developers"...
2. Upwork lets clients restrict by freelancer location, and a 2017-era HN thread says Upwork added a US-only visibility setting. Upwork staff say (2023) no restriction on Pakistani freelancers stops clients hiring them. So the platform allows geo-filtering but does not block Pakistan.
   Grade: weak (old) | Type: first-person anecdote + platform statement | https://news.ycombinator.com/item?id=14317768 ; https://community.upwork.com/t5/Freelancers/Geo-location-discrimination-for-gigs-which-do-not-require-exact/m-p/961572 | 2017-2023
   Cache: QUERY "US-based developers only"...
3. A freelancing advice blog says buyers filter toward US, UK, Eastern European and Indian profiles before Pakistani ones at the same skill and rate, and that clients expect a Pakistan discount. Upwork's own Pakistan page says freelancers there often compete on cost. The blog also says the trust gap is smaller than ten years ago.
   Grade: weak | Type: vendor marketing / advice blog | https://www.lilachbullock.com/freelancing-websites-in-pakistan-that-pay/ ; https://www.upwork.com/hire/pk/ ; https://www.nsave.com/pakistan/upwork | 2026 (nsave title says 2026)
   Cache: QUERY reddit "pakistani" developer upwork trust...
4. HN offshoring threads (mostly 2015-2023, India-focused, none Pakistan-specific) repeat the same advice: use references from past clients, ask whether they later needed a cleanup team, and use a small team with a paid trial. Commenters tie very low rates to low quality. One commenter reports a positive result (remote Indian developer, about $13K, quality and timing exceeded expectations).
   Grade: moderate for "what HN believes", weak for current relevance | Type: first-person anecdote | https://news.ycombinator.com/item?id=16790664 ; https://news.ycombinator.com/item?id=13777251 ; https://news.ycombinator.com/item?id=23941565 | 2015-2023 (older, background)
   Cache: QUERY offshore agency burned rebuild...; QUERY how to vet offshore dev agency founder...
5. Time-zone overlap is a screening rule for some buyers. One HN commenter counts shared working hours and notes East Coast US with India often gets only 1-2 hours overlap. A vendor blog says 2-4 hours is usual for real-time work, and another commenter argues a 4 hour overlap rule. Pakistan (UTC+5) has similar problems with US East/West coasts; UK and Gulf overlap is better. (The Pakistan inference is mine, not from a source.)
   Grade: weak | Type: first-person anecdote | https://news.ycombinator.com/item?id=13777251 | [UNVERIFIED] 2017 (older)
   Cache: QUERY how to vet offshore dev agency founder...
6. 2026 offshore vendor guides say a very low rate guarantees a mis-hire, that offshore developers using AI produce large diffs seniors must untangle, and that founders should do a 2-4 week paid trial before long contracts. These are sellers selling their own (higher-priced) offshore service. No independent data on how often "burned by cheap offshore" happens.
   Grade: weak | Type: vendor marketing | https://fullscale.io/blog/offshore-software-development-trends/ ; https://www.agilesoftlabs.com/blog/2026/04/how-to-hire-offshore-developers-risk | 2026
   Cache: QUERY hired cheap offshore developer AI code had to rebuild...
7. Review platforms: guides written by agencies say Clutch, G2 and GoodFirms are a shortlist, not proof. They say Clutch does some identity verification, that an overwhelming number of 5-star reviews is suspicious, and that video case studies and a reference call matter more. One agency says Clutch has hardly any negative reviews. All of this is agency-authored. No independent ranking of Clutch vs GoodFirms vs G2 vs Trustpilot vs Google vs Upwork for small dev agencies was found.
   Grade: weak | Type: vendor marketing | https://fullscale.io/blog/how-to-vet-software-development-companies/ ; https://naturaily.com/blog/how-to-find-best-development-company-on-clutch | undated / unknown
   Cache: QUERY Clutch reviews matter for small software agency...
8. Pakistani agencies that sell abroad show Pakistan but lead with a US address. Arbisoft: [PARAPHRASE, NOT VERBATIM] "HQ & Other Offices" lists Plano, Texas first, then Lahore and Islamabad; it also publishes pages on top AI companies in Pakistan; reports 4.9/5.0 on Clutch (self-reported). 10Pearls: HQ Vienna, Virginia (one source says McLean); founded by brothers in Pakistan per one source; its own text says delivery centers in "South Asia" without naming Pakistan in the summarised text. Tkxel: Clutch primary location Reston, Virginia, with Lahore among 4 locations. Pattern: US-first, Pakistan not hidden but not the headline.
   Grade: moderate for the pattern (three consistent examples, but via search summaries and vendor/directory pages) | Type: vendor marketing | https://arbisoft.com/blogs/top-custom-software-development-companies-in-2026 ; https://www.mobileappdaily.com/company/arbisoft ; https://www.builtinchicago.org/company/inspirant-group-10pearls-company ; https://clutch.co/go-to-review/tkxel/103862 | 2026 / undated
   Cache: QUERY Arbisoft..., 10Pearls..., Tkxel...
9. Upwork Top Rated needs a Job Success Score of at least 90% for most of the last 16 weeks and covers the top 10% of talent (Upwork help page, per summary). Top Rated Plus is visible only to Enterprise and Business clients (and select Plus clients); other clients see standard Top Rated. No client testimony about hiring because of the badge was found.
   Grade: moderate for the rules (platform statement), none for buyer effect | Type: independent (platform documentation) | https://support.upwork.com/hc/en-us/articles/360049702614 ; https://community.upwork.com/t5/Announcements/New-talent-badges-are-now-available/m-p/778379 | undated
   Cache: QUERY Upwork Top Rated Plus badge...
10. Lovable's expert program: Certified Lovable Expert badge based on projects shipped, a verified profile with built-and-shipped projects, expert track for individuals and agencies under five people, clients browse by problem solved and manage the relationship directly. A competitor agency blog (July 2026) calls it "the strongest third party signal" for a new build and says each listing shows a verified hired count and hourly rate. No data on how often buyers pick badge holders.
    Grade: weak for buyer effect | Type: vendor marketing | https://lovable.dev/partners/experts ; https://unicoconnect.com/blogs/best-lovable-development-agencies | 2026
    Cache: QUERY lovable expert program...
11. Fiverr Lovable-fix gigs: one gig shown (viccky69) has 3 reviews, all from US clients, praising work after a Lovable app broke on going live. Seller country not shown. Another seller (sohail961) shows a US profile location with Urdu among languages. This shows buyers do pay offshore-looking sellers for Lovable fixes, but proves nothing about trust.
    Grade: weak | Type: vendor marketing (gig pages) | https://fiverr.com/viccky69/fix-debug-and-deploy-your-lovable-dev-app-to-production-with-stripe-and-supabase ; https://fiverr.com/sohail961/review-fix-and-deploy-your-lovable-app | 2026 (undated)
    Cache: QUERY fixed my Lovable app freelancer...

NOT FOUND (no evidence): Western-registered entity, US/UK phone number, Stripe invoicing, founders' LinkedIn, money-back guarantee, pay-after-audit, Loom/video audits, GitHub activity as trust signals; Trustpilot/Google/GoodFirms/G2 weighting for small agencies; how rescue sellers use "burned by cheap freelancer" in marketing; any 2025-26 buyer voice about Pakistan specifically for rescue work.

## 3. Buyer quotes
Zero verified buyer quotes. The search tool returned summaries, not page text, so nothing qualifies as exact text. Below are only truncated thread titles/snippets exactly as returned. They are comment openings whose author role (buyer or seller) is unknown, so do NOT use them as buyer evidence.

- Quote: "IT miracle? More like IT sham. The quality of engineers in India is sketchy at b..."
- Username: unknown | Site: Hacker News | Date: unknown (item 17255004, about 2018) | Upvotes: unknown | Link: https://news.ycombinator.com/item?id=17255004
- Buyer tag: unknown on all fields | Cache file: cache/15-trust-searches.md, QUERY offshore agency burned rebuild startup hire developer india pakistan quality

- Quote: "I've talked with a lot of different Indian and similar 'offshore' engineers, de..."
- Username: unknown | Site: Hacker News | Date: unknown (item 23941565, about 2020) | Upvotes: unknown | Link: https://news.ycombinator.com/item?id=23941565
- Buyer tag: unknown | Cache file: same entry

- Quote: "Offshore developed code is not usually the same quality. Not that we all deserve..."
- Username: unknown | Site: Hacker News | Date: unknown (item 16340680, about 2018) | Upvotes: unknown | Link: https://news.ycombinator.com/item?id=16340680
- Buyer tag: unknown | Cache file: cache/15-trust-searches.md, QUERY "US-based developers only"...

- Quote: "As a US-based developer I do not feel threatened by the "cheap" offshore develop..."
- Username: unknown | Site: Hacker News | Date: unknown (item 45060951, ID range suggests 2025) | Upvotes: unknown | Link: https://news.ycombinator.com/item?id=45060951
- Buyer tag: unknown (a US developer, so a competitor to offshore sellers, not a buyer) | Cache file: same entry

## 4. Seller quotes
Zero verified seller quotes. Seller bias flag: all offshore-vendor guides above (Full Scale, AgileSoft Labs, Naturaily, Unico Connect, Arbisoft, etc.) benefit from the story that offshore is risky unless you pick a vetted partner like them.
Paraphrases only (not quotes): Unico Connect (July 2026) calls the Lovable directory the strongest third-party signal; one agency says Clutch should be taken with a pinch of salt.

## 5. Numbers found
| number | what it measures | source link | date | type | grade |
|---|---|---|---|---|---|
| 90% JSS, 16 weeks, top 10% | Upwork Top Rated threshold | https://support.upwork.com/hc/en-us/articles/360049702614 | undated | independent (platform doc) | moderate |
| 2-4 hours | typical real-time overlap per vendor blog | https://news.ycombinator.com/item?id=13777251 (HN) and vendor blog in same search | 2017 / unknown | anecdote / vendor | weak |
| 1-2 hours | East Coast US with India overlap per HN commenter | https://news.ycombinator.com/item?id=13777251 | [UNVERIFIED] 2017 | anecdote | weak |
| 4 hours | overlap rule one commenter argues for | same search | unknown | anecdote | weak |
| ~$13K | one positive India remote dev project cost | https://news.ycombinator.com/item?id=23941565 area (search summary) | unknown | anecdote | weak |
| $35-50 vs $10-18 per hour | commenter's view of good vs cheap India engineers | HN offshoring search results | unknown | anecdote | weak |
| 2-4 weeks | paid trial length advised before 6-month deal | https://www.agilesoftlabs.com/blog/2026/04/how-to-hire-offshore-developers-risk | 2026-04 | vendor | weak |
| 800+ / 900+ | Arbisoft headcount (two sources disagree) | arbisoft.com blog; mobileappdaily.com | 2026 / unknown | vendor | weak |
| 4.9/5.0 | Arbisoft Clutch score, self-reported | arbisoft.com blog | 2026 | vendor | weak |
| 250-999, founded 2008 | Tkxel size and age per Clutch | https://clutch.co/go-to-review/tkxel/103862 | undated | vendor listing | weak |
| founded 2004 | 10Pearls founding per one source [UNVERIFIED] (another says 2008) | builtinchicago.org listing | undated | vendor listing | weak |
| 3 reviews, all US clients | one Fiverr Lovable-fix gig | fiverr.com/viccky69/... | undated | vendor | weak |
| under 5 people | Lovable Expert track size | https://lovable.dev/partners/experts | 2026 | vendor | weak |

All counts are "from search results, partial".

## 6. What this means for the offer
- Do not rely on location being a non-issue. There is old and scattered evidence that some buyers exclude or discount Pakistan and India, so the offer should carry named proof, a Western-facing presence and a stated overlap window rather than ask buyers to trust a Lahore address.
- Lower the buyer's risk of being wrong: the advice buyers and vendors repeat most is a small paid first step with references (a paid audit or short trial). That fits a paid audit credited to the work. This is inference, not tested.
- Follow the Pakistani agencies' pattern (US address first, Pakistan shown, not headline), but treat that as what sellers do, not proof that it converts. Nothing found shows hiding location helps.

## 7. What this means for the GO gates
- Gate 4 (credible position above the low-cost freelancer floor): unclear. Buyers appear to expect a Pakistan discount, which pushes against a premium position, but the evidence is old advice blogs and anecdotes.
- Gate 1 (buyers paying $1,500+): unclear. Nothing here shows what buyers pay Pakistani sellers; only that Fiverr Lovable-fix gigs exist with US buyers.
- Gates 2, 3, 5: not touched.

## 8. Machine-readable block
```json
{"track": "15-trust-and-geography", "demand_signal": "none", "buyer_price_points_usd": [], "seller_price_points_usd": [], "gates_supported": [], "gates_contradicted": [], "evidence_grade": "weak", "sources_read": 13, "buyer_quotes": 0, "seller_quotes": 0}
```

## Appendix: unverified items
- "10Pearls founding per one source (another says 2008)" (section 5 table only): cache has only one source, 2004. The 2008 in cache belongs to Tkxel, not 10Pearls. Not in cache.
- Date "2017" for HN item 13777251 (key finding 5 and section 5 rows "2-4 hours" / "1-2 hours"): cache gives no date for this item (only "HN threads 2011-2019"). The year looks inferred from the item id. Not in cache.
