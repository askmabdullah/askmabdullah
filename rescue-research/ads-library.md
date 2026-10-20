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


---

# Round 2 additions (agent B, 2026-10-20)

Source: tracks/18-meta-ads-round2.md. Cache: cache/18-meta-ads-searches.md (S1 to S33). 33 searches used of a 35 cap. Meta Ad Library, Google Ads Transparency Center and TikTok Creative Center still could not be opened. Everything below is search snippet or tool summary.

## Result
- **Advertisers evidenced as running Meta, Google, TikTok or LinkedIn ads to sell vibe-code rescue: 0 (still).** Table A above stays empty.
- Searches tried this round: site:facebook.com/ads/library (the site: operator is not honored by this index), facebook.com / instagram.com / tiktok.com / adstransparency.google.com as allowed domains, "saw an ad" buyer reports, agency "we run ads" posts, X, LinkedIn, YouTube, TikTok, and the round 1 seller names with "facebook ads", "instagram", "meta ads".
- Negative results (not proof of absence): Red Leg Dev, Wavect, Chudovo, Innowise, Pragmatic Coders, ULAM Labs, Clockwise, Agence Scroll, Valletta, Beesoul, rapidevelopers, witscode, axonbuild, Slopfix, QuickLaunch, VibeCodeFixers, MetaCTO, Justin McKelvey: none returned any link to Facebook, Instagram, Meta, TikTok or Google ads.

## Table D: sellers added this round (still NOT evidenced as advertisers)

| Seller | Ad evidence | Offer / price as stated in search summary | Funnel | Source | Cache |
|---|---|---|---|---|---|
| MetaCTO "Vibe Rescue" | none | Free 48-hour code audit, takeover plan, production in 30 days, claims 100+ production systems. No price shown. | free audit | metacto.com/solutions/vibe-rescue | S32 |
| Justin McKelvey "vibe code rescue" | none | Free 20-minute repo audit with Loom walkthrough; 4-8 weeks about $25K-$50K fixed price; lighter from $15K; complex SaaS $60K-$100K | free audit then fixed price | justinmckelvey.com/vibe-code-rescue | S32 |
| ULAM Labs | none | Free assessment, improvement plan, cleanup sprints, ongoing care. Tagline "We clean up after vibe coding. Literally." | free audit | ulam.io/software-services/we-clean-up-after-vibe-coding | S21 |
| Clockwise Software | none | Vibe coding cleanup page, client result claims | unknown | clockwise.software/vibe-coding-cleanup | S21 |
| VibeCode Rescue (@VibeCodeRescue on X) | none shown; "the results don't show whether it runs paid ads" | Turns messy AI-generated code into production-ready solutions; free consultation | free consultation | x.com/VibeCodeRescue | S26 |
| VibeCoding Agency (@vibecodingagency, Instagram) | none shown; has an Instagram presence | Claims to be first US agency specialised in vibe coding, Miami (own claim) | unknown | instagram.com/vibecodingagency/ | S29 |
| Slopfix | none | Paste repo or upload zip, fixed quote $30-$100 | instant quote | slopfix.ptolemay.com | S9 |
| Groovyweb | none | Vibe-code rescue / production hardening | unknown | groovyweb.co/service/vibe-coding-development | S32 |
| RapidDev | none; content hub of 509 Lovable pages (SEO signal) | Done-for-you Lovable builds $13K-$25K | content / SEO | rapidevelopers.com/tools/lovable | S22 |

## Table E: ad-adjacent facts added
| Fact | Source | Type | Grade |
|---|---|---|---|
| Lovable (the platform) had 1,079 ads in the Meta library, 304 active, about two thirds video, per one third-party write-up (snapshot, undated); runs Google search ads on "vibe coding" | sprites.ai/blog/lovable-ads-strategy (S15) | vendor | weak |
| Lovable has a built-in Google Ads feature for its users (platform feature) | docs.lovable.dev/integrations/google-ads (S7) | vendor | moderate |
| A vendor TikTok post/ad citing "380,000 assets" and "40% expose sensitive data" was described by the search tool as a "TikTok ad"; no URL or vendor name tied to it; paid vs organic unknown | S29 | tool summary | weak |
| A Hacker News seller says word of mouth and networking bring work and SEO stopped working | S14 | anecdote | weak |
| QuickLaunch (rescue seller, $120k+ in 2025, own Indie Hackers post): one summary said no ads, referrals; a second search could not confirm. UNCONFIRMED | S9, S11 | anecdote | weak |

## Table F: cost benchmarks (all vendor-published unless stated; details in tracks/18-meta-ads-round2.md section 5)
| Metric | Figure | Source | Date | Label |
|---|---|---|---|---|
| Facebook lead campaign CPL, all industries | $27.66 (+21% YoY) | WordStream/LocaliQ | 2025-09 | vendor, own account data |
| Facebook lead CTR / CPC | 2.59% / $1.92 | WordStream/LocaliQ | 2025 | vendor |
| B2B SaaS Meta CPL | $63.40 (most cited); $80-$220 lead forms; $120-$380 landing page | Ryze, Adamigo, GrowthSpree | 2026 | vendor |
| B2B CPL across channels, 153 advertisers | Instagram $138, Facebook $145, LinkedIn $202, Google $524 | Metadata via getpixel.ai | 2026 | vendor, lead definition unpublished |
| Software development lead cost | $680 paid, $510 organic, $591 blended; software/IT SQL $1,680-$3,080 | table via S24; Belkins via Zephra | 2026 | vendor |
| Meta CPM | $9.31 median (AdKit, Sep 2026); about $14 in other roundups | adkit.so; others | 2026 | vendor |
| Meta lead CTR, B2B | 0.92%-1.37% (Focus Digital via compilation) | focus-digital.co | 2026 | vendor |
| Cost per booked call (agency playbook, non-software) | $80-$150 | theblueprint.training | unknown | vendor |
| Show rate / close rate | 75-85% / 20-29% (B2B generic) | various | 2025-26 | vendor |
| Small-agency warm lead win rate | 30-50% (vs 10-20% cold) | pitchsite.io, gigradar.io | 2026 | vendor |
| Google Ads search, all industries | CPC $5.26, CPL $70.11, conversion 7.52% | WordStream | 2025-09-29 | vendor |
| Google CPC, software brands | about $3.88 | Pixis | 2025 | vendor |

No CPC, CPL, cost per call or cost per client was found for rescue, "lovable developer" or "vibe coded app" terms, on Meta or Google.

## Read on the claim "agencies spend heavily on Meta ads and close well"
Unsupported. Zero advertisers evidenced; no buyer reports; no seller says it. Weak counter-signals (word of mouth, SEO hub, free-audit front doors) are snippet-only. Still unproven in either direction because the Ad Library could not be opened. First action for a person with a browser remains the Table A search list in "What the next person should do".
