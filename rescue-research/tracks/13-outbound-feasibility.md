# Track 13: Outbound feasibility

## 1. Track name and scope
Track 13: can live vibe-coded apps be found at scale, how to spot ones with traction, and the etiquette and legal limits of contacting them. Research only. No contact made, no personal contact details collected, no app probed.

Time and searches: 11 WebSearch calls returned results (plus 3 that returned nothing, see below). I did not open any page. WebFetch and curl are blocked, so every number is "from search results, partial" and every source text is a search snippet or a search-tool summary.

IMPORTANT GAP: the web search budget (200 per turn, shared by all agents) ran out after 11 of my searches. The last 3 searches were refused. I could NOT search these topics: cold email legal rules (CAN-SPAM, GDPR/PECR, Spam Act, CASL), LinkedIn outreach norms, reply rates to "I found a security issue" outreach, agencies already doing this outbound, X posts "built with lovable", Reddit, Lovable Discord, GitHub README search, Product Hunt counts by tag, Wappalyzer counts. Sections below mark these as "no evidence found (not searched)". Re-run needed once search budget is restored.

Searched and answered (partly): BuiltWith count, "Edit with Lovable" badge, lovable-tagger on GitHub, Lovable Launched gallery and third-party directories, platform app counts (Replit, Base44, Bolt), certificate transparency method, published security scans, traction signals.

Cache file for all searches: cache/13-outbound-searches.md. All source text is "Source text: search snippet" (search tool summary, which is NOT a verbatim quote).

## 2. Key findings

1. BuiltWith lists about 101,000 current Lovable sites. The summary says [PARAPHRASE, NOT VERBATIM] "101,034 current Lovable customers" and [PARAPHRASE, NOT VERBATIM] "117,323 websites in this full report, of which 16,289 are redirects". The figures do not fully reconcile and the snapshot date is not shown. This is the best single count for findable Lovable apps, and it includes any site with the Lovable fingerprint, not only lovable.app subdomains.
   Grade: moderate | Type: independent data (third-party tracker, method unknown) | https://trends.builtwith.com/websitelist/Lovable | date unknown (found 2026-10-21) | QUERY: builtwith Lovable technology usage websites count

2. The BuiltWith .ai slice shows 3,937 current Lovable sites. .ai domains skew toward AI startups, so this is a useful pre-filter for "serious" builders (a custom domain is a paid-plan signal and a cost signal).
   Grade: moderate | Type: independent data | https://trends.builtwith.com/websitelist/Lovable/.ai | date unknown | same QUERY

3. Lovable's own numbers are far larger than what trackers find. Aggregator DemandSage says over 60 million projects created, over 8 million users, 1 million projects a week (no primary source; Lovable has not shared 2026 user counts). Sacra: 2.3 million active users and 180,000 paying subscribers in July 2025. So only a small slice of projects is publicly live and detectable.
   Grade: weak (aggregators, secondary) | Type: independent data (secondary) / vendor-adjacent | https://www.demandsage.com/lovable-statistics/ ; https://www.sacra.com/c/lovable | QUERIES: Lovable custom domains connected count...; lovable.app subdomain how many apps deployed...

4. Publishing is free on all Lovable plans and goes to xxx.lovable.app. Custom domains and "Remove the Lovable badge" need a paid plan (Pro). The lovable.app address cannot be removed and stays reachable even with a custom domain. Consequence: free-plan apps are findable by subdomain; a paid custom domain plus no badge is a weak signal of commitment but also makes the app harder to fingerprint by badge.
   Grade: moderate | Type: vendor documentation (via search summary) | https://lovable.dev/faq/domains/management ; https://docs.lovable.dev/features/hosting | QUERIES: lovable.app subdomain...; Lovable apps making money...

5. The "Edit with Lovable" button is reported as present on shared projects and was a viral growth loop (one personal-site generator reportedly made 20,000 sites in a few days, each with the button). Removing the badge is a paid feature. So the badge finds free-plan apps, which are the least likely to have revenue.
   Grade: weak | Type: independent commentary (Substack, reseller listing) | https://lucamastella.substack.com/p/lovable-da-0-a-30m-arr-in-4-mesi | QUERY: "Edit with Lovable" badge built with Lovable apps

6. GitHub: "lovable-tagger" is a Vite dev plugin (data-lov-* attributes) that appears in many public repos (vite.config.ts files, Dependabot PRs, "remove lovable-tagger" PRs). It is a usable fingerprint for repos, but search results gave no count. It is dev-only, so it is not visible on the live site, and many owners are removing it. Repos show the code, not who is paying, and are mostly hobby or student projects in the sample seen (e.g. personal site, algorithm visualiser, breakfast planner).
   Grade: moderate (existence), none (count) | Type: independent data | https://github.com/Khushal-Me/Conscient/blob/main/vite.config.ts ; https://github.com/Unify-Now-Digital/masons/pull/32 | QUERY: "lovable-tagger" github

7. Lovable Launched: AlternativeTo reported in Feb 2025 that Lovable announced "Lovable Launched", a Product Hunt style showcase for apps built with Lovable. I could not confirm that it is live today or its URL or size. A third-party directory, madewithlovable.com, exists ("100+ real examples" on its websites page) and flags projects no longer running on Lovable. Lovable's templates page showed 228 entries. All three are small (hundreds, not thousands).
   Grade: weak-moderate | Type: independent news / third-party directory | https://alternativeto.net/news/2025/2/lovable-announces-lovable-launched--a-platform-for-lovable-apps-discovery ; https://madewithlovable.com/ | QUERY: Lovable Launched page showcase...

8. Product Hunt: no tag-level count found. Lovable's own PH page shows 4.7 stars from 211 reviews and 50K followers. PH "Lovable customers" page names a few products (MindPal, Userflow, Modaal) that credit Lovable for prototyping. PH has a "vibe coding" category page. PH launches are founder-submitted with upvotes and comment counts, so it is a good traction filter but a tiny list.
   Grade: weak | Type: independent data (snippet) | https://www.producthunt.com/products/lovable/customers ; https://www.producthunt.com/categories/vibe-coding | QUERY: Product Hunt built with Lovable launch

9. Other platforms: no official counts for published apps anywhere. Replit: third-party table (Shipper.now, a competitor blog) estimates 5 million AI-generated apps in 2025, not deployed apps. Base44: stats site says over 5,000,000 apps created after Wix integration in Nov 2025; Anthropic case study says 2+ million users in under 6 months; another review says 400,000+ users (conflict). Bolt: Dataprovider lists 41,996 websites on Bolt; Bolt hosts at bolt.host for free. Treat all as "created", not "live".
   Grade: weak | Type: independent estimates / competitor content | https://shipper.now/replit-stats/ ; https://shipper.now/base44-stats/ ; https://www.dataprovider.com/recipes/bolt/ ; https://claude.com/customers/base44 | QUERIES: replit.app...; base44.app...; bolt.host...

10. Subdomain enumeration is technically possible via certificate transparency logs (crt.sh style wildcard queries), but I found no published count of lovable.app or lovableproject.com subdomains. Per the search summary, CT shows only hosts that had certificates issued. We did not run any such query (research only, and it is not needed to answer feasibility).
    Grade: weak (method only) | Type: independent technical guides | [UNVERIFIED] https://en.internetwache.org/certificate-transparency-as-a-source-for-subdomains-14-12-2017/ | QUERY: certificate transparency lovable.app...

11. Scale proof from published research: Symbiotic Sec (April 2026) crawled 65,643 URLs and confirmed 1,085 vibe-coded sites using Supabase; 1,072 fully scanned; 1,046 (98%) had at least one vulnerability; 173 critical. Another researcher: 303 endpoints across 170 Lovable projects lacked proper RLS (2025 CVE). This shows live apps are findable by crawlers at the thousand-plus level, and that the problem is common. It also shows the crawl yield: about 1.7% of crawled URLs were confirmed vibe-coded Supabase sites. We must NOT repeat such scans (BRIEF rule: no probing).
    Grade: moderate | Type: vendor research (security vendor, bias: sells scanning) | https://www.symbioticsec.ai/blog/we-scanned-1-072-vibe-coded-apps-98-had-security-flaws ; https://www.superblocks.com/blog/lovable-rls-breach | QUERY: Lovable apps security scan thousands...

12. Traction base rate is low. BigIdeasDB (self-published research site) reports that among revenue-verified startups on vibe-coding subdomains, 7.6% report any MRR, and none cleared $1,000 in the last 30 days; products sold TO vibe coders earn more often (50%). TrustMRR shows Stripe-verified revenue, but only for founders who opt in. So of ~100k live Lovable-fingerprint sites, a rough 5% to 10% might have any revenue (my arithmetic on a weak source, not a measured figure).
    Grade: weak | Type: independent data (self-published) | https://bigideasdb.com/do-vibe-coded-apps-make-money ; https://trustmrr.com/startup/vibecoded-startups | QUERY: how to tell if a vibe coded app has real traction...

13. Traction signals practitioners point to (from TechRadar summary): conversion to paid, early retention, cost per install. Public, company-level signals we can use without contact: pricing page present, Stripe checkout or payment links in public page, custom domain on a paid plan, no Lovable badge, LinkedIn company page with employees, Product Hunt upvotes, reviews on G2/Trustpilot/app stores, TrustMRR listing, funding news. These are my working list; only the TechRadar and TrustMRR items are sourced.
    Grade: weak | Type: independent commentary + agent inference | https://www.techradar.com/pro/insight-taste-and-distribution-how-to-turn-vibe-coded-apps-into-cash | QUERY: how to tell if a vibe coded app has real traction...

14. NOT FOUND (not searched, budget out): legal rules, reply rates, agency outbound, X posts, Discord, Reddit. See section 5 for what I can say from background knowledge, clearly labelled.
    Grade: none | Type: n/a

## 3. Buyer quotes
None. This track did not search buyer voices. No verbatim quotes were captured (search summaries are not quotes).

## 4. Seller quotes
None captured verbatim. Note on bias: the security scan sources (Symbiotic Sec, Superblocks, Bastion, Sola) are vendors that sell scanning or security products. They benefit from saying vibe-coded apps are broken. BigIdeasDB and rapidevelopers.com are content sites with commercial interest.

## 5. Numbers found

| number | what it measures | source link | date | type | grade |
|---|---|---|---|---|---|
| 101,034 | BuiltWith "current" Lovable customer sites | https://trends.builtwith.com/websitelist/Lovable | unknown | independent tracker | moderate |
| 117,323 (16,289 redirects) | BuiltWith full Lovable report incl. historical/redirects | same | unknown | independent tracker | moderate |
| 3,937 | BuiltWith current Lovable sites on .ai | https://trends.builtwith.com/websitelist/Lovable/.ai | unknown | independent tracker | moderate |
| 60 million+ | Lovable projects created (aggregator) | https://www.demandsage.com/lovable-statistics/ | Aug 2026 per aggregator | aggregator | weak |
| 8 million+ users; 1M projects/week | Lovable (aggregator) | same | 2026 | aggregator | weak |
| 2.3M active users; 180,000 paying subs | Lovable, July 2025 | https://www.sacra.com/c/lovable | 2025-07 | independent research (secondary) | weak-moderate |
| 1.2M apps built; 4,000+ instances hosted | Lovable (Sacra) | https://sacra.com/research/lovable-at-17m-arr/ | older | secondary | weak |
| 228 | entries on Lovable templates page | https://lovable.dev/projects/featured | crawl date unknown | vendor | moderate |
| "100+" | examples on madewithlovable.com websites page | https://madewithlovable.com/categories/websites | 2026 | third-party directory | weak |
| 211 reviews, 4.7 stars, 50K followers | Lovable on Product Hunt | https://www.producthunt.com/products/lovable | 2026 | independent | moderate |
| 41,996 | Dataprovider count of websites using Bolt | https://www.dataprovider.com/recipes/bolt/ | unknown | tracker | weak |
| 5,000,000+ | Base44 apps created (stats site) | https://shipper.now/base44-stats/ | after Nov 2025 | competitor blog | weak |
| 2M+ users in under 6 months | Base44 (Anthropic case study) | https://claude.com/customers/base44 | 2025-26 | vendor case study | weak |
| 5 million (2025) | Replit AI-generated apps (estimate) | https://shipper.now/replit-stats/ | 2025 | competitor blog | weak |
| 65,643 URLs crawled -> 1,085 vibe-coded Supabase sites | crawl yield, Symbiotic Sec | https://www.symbioticsec.ai/blog/we-scanned-1-072-vibe-coded-apps-98-had-security-flaws | 2026-04 | vendor research | moderate |
| 1,046 of 1,072 (98%); 173 critical | scanned sites with vulnerabilities | same | 2026-04 | vendor research | moderate (vendor bias) |
| 303 endpoints / 170 projects | Lovable apps lacking RLS | https://www.superblocks.com/blog/lovable-rls-breach | 2025 | vendor | moderate |
| 48 of 62 (77%); 52% of those with readable tables | small Lovable scan, one developer | https://medium.com/@jacobp96/i-scanned-over-50-lovable-apps-for-security-vulnerabilities-d05b2ad94006 | unknown | anecdote | weak |
| 7.6% any MRR; 0 above $1,000/30 days | revenue-verified startups on vibe-coding subdomains | https://bigideasdb.com/do-vibe-coded-apps-make-money | 2026 | self-published research | weak |
| GBP 22/month | Lovable Pro (custom domain, remove badge) | https://marcandrews.com/lovable-review-2026-ai-app-builder-for-non-coders/ | 2026 | review | weak |

All rows: Source text: search snippet. Cache: cache/13-outbound-searches.md.

### Route-by-route rough counts (from search results, partial)
| route | rough count | label |
|---|---|---|
| BuiltWith Lovable fingerprint | ~101,000 current (~117,000 incl. history) | best figure, partial |
| BuiltWith Lovable on .ai | ~3,900 | partial |
| lovable.app / lovableproject.com subdomains | no published count; CT logs could enumerate, not run | unknown |
| "Edit with Lovable" badge | no count; free-plan apps only | unknown |
| GitHub "lovable-tagger" | many repos, no count in snippets | unknown |
| Lovable Launched / templates / madewithlovable | ~100 to ~230 entries each | small |
| Product Hunt (Lovable-built) | no tag count; handful seen | unknown |
| Bolt (bolt.host) | ~42,000 sites (Dataprovider) | weak |
| Replit (replit.app / repl.co) | no live count | unknown |
| Base44 (base44.app) | no live count; 5M created | unknown |
| Wappalyzer | not found in search | unknown |
| X posts, Discord showcase, Reddit | not searched | unknown |
| Security-research crawl yield | 1,085 Supabase vibe-coded sites from 65,643 URLs | moderate |

### Legal and etiquette (NOT researched here; background knowledge, UNVERIFIED, needs a lawyer check)
Search budget ran out before I could source these. Treat as flags, not findings. Grade: none.
- US CAN-SPAM: B2B cold email is allowed if sender identity is accurate, a physical address is included and there is a working opt-out honoured promptly.
- UK PECR / GDPR: corporate subscribers (limited companies) can be emailed without prior consent, but sole traders and some partnerships count as individuals and need consent. GDPR still applies to personal data (named people), so a legitimate-interest assessment and an opt-out are needed.
- EU: rules differ by country; GDPR applies to named individuals.
- Canada CASL: strict. Needs implied or express consent; B2B has narrow exemptions (e.g. conspicuous publication of the address with no "do not contact" notice and a relevant message). High fines.
- Australia Spam Act: needs consent (express or inferred), sender identification and unsubscribe.
- Security angle: telling a company "I found a security issue in your app" after probing it can breach computer misuse laws (CFAA, UK Computer Misuse Act). Any message must be based on public published facts only, never on testing their app. It can also read as a threat or extortion pitch. Our BRIEF forbids probing, so only public, non-intrusive signals are allowed.
- Reply rates: no sourced data found. Do not assume any number.

## 6. What this means for the offer
- Outbound has a big top of funnel (about 100,000 Lovable-fingerprint sites on BuiltWith alone), but most are hobby or free-plan apps. The target (apps with paying users) is a small slice, maybe a few thousand, and unproven.
- Any outbound message should offer a rescue or finishing audit based on public facts (no scanning, no "we found a hole"). A cold "security issue" angle is a legal and trust risk and cannot be used.
- Platform-specific fingerprints (.ai domains, Pro-plan custom domains, Stripe on page, PH launches) let us build a small, high-quality list instead of mass blasting.

## 7. What this means for the GO gates
- Gate 2 (a channel under about $600 per paying client): unclear. The list exists, but no reply-rate, cost or agency evidence was found (search budget ran out). Outbound cost is mostly labour; I have no sourced conversion data.
- Gate 1, 3, 4, 5: not touched by this track.

## 8. Machine-readable block
```json
{"track": "13-outbound-feasibility", "demand_signal": "weak", "buyer_price_points_usd": [], "seller_price_points_usd": [], "gates_supported": [], "gates_contradicted": [], "evidence_grade": "weak", "sources_read": 0, "buyer_quotes": 0, "seller_quotes": 0}
```

## Appendix: unverified items
- URL https://en.internetwache.org/certificate-transparency-as-a-source-for-subdomains-14-12-2017/ (key finding 10): not in cache. The cache only has the title "Certificate Transparency as a source for subdomains (2017)" at domain internetwache.org, without this URL or the "en." host or date slug.
