# Meta Ad Library scan: advertiser table (Track 5)

Run date: 2026-10-20. Markets requested: US, UK, Australia, Canada.

## READ THIS FIRST: what this file is and is not

1. **The Meta Ad Library page itself could not be opened.** WebFetch and curl are blocked in this environment. Only WebSearch worked. Nothing in this file was read from facebook.com/ads/library.
2. **The search budget ran out.** WebSearch has a limit of 200 calls per turn shared by all 16 agents. After 14 searches that returned results, 1 domain error and 4 refusals, the tool refused further calls. I stopped. I did not work around the limit. The planned budget was about 45 searches. About 19 calls were attempted.
3. **Result: zero advertisers could be evidenced as running Meta ads for this service.** No search result showed an Ad Library listing, an ad screenshot, an ad start date, a number of active ads, or an ad landing page tied to a Meta ad. The table of evidenced advertisers is empty. That is a finding about the tool limits, not proof that nobody advertises.
4. **Ad spend is not shown** in the Meta Ad Library for non-political, non-issue ads. The library does not show spend, reach, CTR, conversions or ROAS for commercial ads. Run length and number of variants are only a rough proxy for profit. (Source text: search summary of Meta help pages, cache/05-meta-ads-searches.md, QUERY 2.)
5. The Ad Library API only covers political and issue ads worldwide, plus ads of any type delivered to the UK or EU in the past year. It does not cover US, Canada or Australia commercial ads. (Same source.)
6. The "agencies spend heavily on Meta ads for this and close well" claim is **unverified**. This scan found no evidence for it and no evidence against it.

## Table A: advertisers evidenced as running Meta ads (page name, country, start date, days running, active ads, offer, price, CTA, landing page, funnel)

| Page name | Country | Ad start date | Days running | Active ads/variants | Offer | Price | CTA | Landing page | Funnel |
|---|---|---|---|---|---|---|---|---|---|
| (none evidenced) | unknown | unknown | unknown | unknown | unknown | unknown | unknown | unknown | unknown |

Count of advertisers evidenced: **0**.

## Table B: sellers of this service found by search (NOT evidenced as Meta advertisers)

These are rescue or audit sellers that appeared in search results. Their sites state the offer. Nothing shows they run Meta ads. Do not treat them as advertisers. Fields come from the search tool summary (paraphrase, not verbatim). All are vendor marketing. Grade: weak for any ad claim, moderate that the offer exists.

| Seller | Country | Ad evidence | Offer as stated by search summary | Price shown | Funnel type | Source | Cache query |
|---|---|---|---|---|---|---|---|
| Red Leg Dev | unknown | none | Works on Lovable, Bolt, v0, Cursor, Replit. Starts with code audit. 2-6 weeks. | unknown | audit first | redleg.dev/vibe-coding | Q "vibe coding cleanup agency book a call" |
| Wavect | unknown | none | Fixed scope, senior engineers, refund on last week if unhappy | unknown | fixed scope | wavect.io/services/vibe-coding-rescue/ | same |
| Chudovo | unknown | none | Free initial codebase assessment, roadmap with cost estimates, then 2-4 weeks | free assessment | audit then fix | chudovo.com/vibe-coding-cleanup/ | same |
| Innowise | unknown | none | Cleanup covering security, tests, performance | unknown | unknown | innowise.com/ai/vibe-coding-cleanup/ | same |
| Pragmatic Coders | unknown | none | Rescue services for AI-generated code | unknown | unknown | pragmaticcoders.com/?p=21920 | same |
| DBB Software | unknown | none | Vibe coding cleanup (Cursor, Lovable, Bubble) | unknown | unknown | dbbsoftware.com/services/vibe-coding-cleanup | same |
| Agence Scroll "Dr Lovable" | France (Paris, per summary) | none | Free audit in 48 hours; outcomes: targeted fix, rebuild, or maintenance | free audit | free audit | agence-scroll.com/en/dr-lovable | Q "free audit" |
| Valletta Software | unknown | none | "Vibe Coding Audit \| Investor-Ready Code \| From $199" (page title, verbatim) | from $199 | paid audit | vallettasoftware.com/blog/post/vibe-coding-audit | Q "free audit" |
| Beesoul | unknown | none | Listed on vibecoding.app with free audits, paid production transformation | free audit | free audit | vibecoding.app/agencies | Q "free audit" |
| Fiverr sellers (techymanny, alicedeveloper_, johndag_addy) | unknown | none | Fix vibe-coded Lovable/Bolt/Replit apps | unknown | marketplace gig | fiverr.com links | Q cleanup and Q "free audit" |
| Joshua Lefebvre (LinkedIn) | unknown | none | Self-promotional post, claims 15+ companies bailed out in 3 months (paraphrase of search summary, teaser only). A second search could not confirm him. | unknown | unknown | linkedin.com (profile not in result list) | Q linkedin |

Inference (not evidence): sellers with a "free audit" front door (Chudovo, Agence Scroll, Beesoul) use the funnel shape that Meta lead-gen usually feeds. That is a guess about funnel design, not proof of ads.

## Table C: Meta-ad-adjacent facts found

| Fact | Source | Type | Grade |
|---|---|---|---|
| Lovable's own LinkedIn page announced users can run ads directly from Lovable (platform feature, not rescue) | search summary of linkedin.com/company/lovable-dev, cache QUERY linkedin | vendor | weak |
| Sprites Ads Library "indexes the live ads of dozens of fast-growing tech and SaaS companies (Cursor, Lovable, ElevenLabs and more)" (search summary) | sprites.ai/blog/the-best-facebook-ad-library-alternatives-in-2025 | vendor | weak. These are platform ads, not rescue ads |
| Third-party spy tools (Foreplay, AdSpy, BigSpy, PowerAdSpy, Minea): no page for vibe-coding terms found | foreplay.co comparison posts (undated in results) | vendor | weak. Absence of results, not absence of ads |

## What the next person should do (needs a browser or open network)

1. Open facebook.com/ads/library, set country to US, then UK, AU, CA, All ads. Search: lovable, vibe coded, vibe coding, fix your app, AI built app, bolt.new, replit app, MVP rescue, finish your app, app stuck, lovable developer, launch your app, "security audit".
2. Filter out Lovable, Bolt, Replit, Cursor own ads. Keep service sellers.
3. For each: record page name, start date, active ads count, offer, CTA, landing page. Screenshot.
4. Check each Table B seller as a first target.
