# Verification log 3 (Verifier 3)

Date: 2026-10-20. No web access used. Method: each quote, username, URL, date, price and count was matched against the cache files by script (normalised text, case and punctuation ignored) and then by hand where a number could match the wrong subject. Tracks were checked against their own cache file first, then all of cache/. Model files were checked against the track files they cite (procedure step 6). Counts below are of distinct checkable items I tested. Grouped items (for example a 5-row price table) are counted as one when they share one source. Treat counts as accurate to about plus or minus 5%.

## Files checked

Tracks: 17, 21, 22, 18, 19, 20 (all six, in that priority order).
Model: offers, channels, delivery, risk, brand (all five).
Nothing was skipped for time. Limits: (a) model sentences with no track pointer or tag were not checked, since they are the author's own wording; (b) qualitative claims in the model files that carry a track pointer but no number were spot-checked, not all checked; (c) cross-references inside my tracks to tracks 1 to 16 (for example "$1,000 in a week, track 2") were checked against those track files only, not their caches.

## Totals

Claims checked 1,033; passed 1,003; failed 14; downgraded 16. Labelled assumptions and derived figures, counted separately and not as failures: 104 (30 in tracks, 74 in model files), plus tag counts below.

| scope | checked | passed | failed | downgraded | labelled assumptions or derived |
|---|---|---|---|---|---|
| Track 17 | 70 | 68 | 1 | 1 | 8 |
| Track 21 | 95 | 92 | 2 | 1 | 6 |
| Track 22 | 90 | 83 | 4 | 3 | 4 |
| Track 18 | 100 | 99 | 1 | 0 | 3 |
| Track 19 | 90 | 84 | 3 | 3 | 5 |
| Track 20 | 95 | 92 | 0 | 3 | 4 |
| model/offers.md | 191 | 190 | 1 | 0 | 22 derived plus 18 [A] tags |
| model/channels.md | 174 | 173 | 1 | 0 | 38 derived plus 30 [A], 7 [V], 6 [X] tags |
| model/delivery.md | 30 | 29 | 0 | 1 | 3 plus 108 [E], 6 [V] tags |
| model/risk.md | 55 | 53 | 0 | 2 | 3 plus 27 [GK], 6 [WS1] tags |
| model/brand.md | 117 | 114 | 1 | 2 | 8 derived plus 1 [X] tag |

For the model rows, "checked" counts numeric figures that carry a track pointer plus quotes attributed to a track. "Derived" means the number is the model's own arithmetic or choice (for example $735 fully loaded, $459 to $766, the $1,950 founding price), not something it attributes to a track. I rebuilt the arithmetic spot checks I tried (T18 gate-2 stack: $80 / (0.8 x 0.25) = $400 and $150 / 0.15 = $1,000; Fiverr combined mean from 20 + 30 gigs; median of 11 "from" prices = $2,500; cost-per-client tables in channels) and they are consistent with the stated inputs.

## Per-file results

### Track 17 (buyer voices round 2): 1 failed, 1 downgraded
All 18 job posts (J1 to J18), their prices, posting dates and sites match the cache titles (S20, S23, S35, S37, S39, S41 to S45). Both buyer quotes are in quotation marks in the cache ("I understand $1,500 may not cover every fix." in S41 and S45; "Now he's hiring a developer to shore it up." in S19 and S29). All seller prices, the HN points, the 153, 109 and 1,304 counts, the 404 Media line and the $607.70 line match. The statements of what was NOT found (0 Reddit pages, no buyer who paid) agree with the cache.
- Failed: the count "11 of those 18 posts are fix, finish or review work on an app stated as Lovable or AI-built" includes J14 (Supabase App Finalization). The cache describes J14 only as bug fixes, hardcoded secrets and SMS verification. Supported count is 10.
- Downgraded: J17 title "Supabase Schema & RLS Deployment" is listed as verbatim but the cache has only the lower-case summary phrase and the URL slug.
- File-level: the JSON block reports "sources_read": 45 while the text says no page was opened (45 is the search count). Same pattern in tracks 18 (33), 19 (35), 20 (35) and 21 (40). Track 22 uses 0 correctly.

### Track 21 (marketplaces and competitors round 2): 2 failed, 1 downgraded
Both $2,000 Upwork posts (Twilio and Stripe for a Lovable app, 2025-10-28; Base44 QA and launch, 2025-12-31), the $1,000, $1,200, $150, $100, $30 and $120 posts, and the $1,000 WordPress rebuild post (found in cache 07, not 21) all match. All seller price points (Teyrex, Base44Devs, AfterBuild, Arkroot, GainCafe, Nightlamp, AppStuck, Triple Minds, TopDevz, Escape Base44), Fiverr review counts and levels (86, 62/75, 28, 1), the Pakistan leads, and the 34-competitor count (matches competitors.md) pass. The 40-search split adds up.
- Failed: Upwork profile title "...Cursor, ClaudCod, GPT5..." (cache: "ClaudeCod"). Cosmetic.
- Failed: Fiverr round-2 mean $51.2 (and so the combined $40.8). The cache lists about 35 to 40 qualifying gigs in searches #30 to #37, not the 30 the track names, and a recompute gives a mean near $46 to $47. Min $5, median $30 and max $250 hold.
- Downgraded: "works in preview, fails when deployed" is the tool's wording "App works in preview but not in deployment".

### Track 22 (buyer reviews round 3): 4 failed, 3 downgraded
All three Clutch reviews (R1 GeekyAnts, R2 Connectish, R3 Cleveroad), the "no cost band shown" finding, and every profile-level band ($10,000+, $10,000 - $49,999, $5,000+, 6 of 7 under $10,000, $50,000 to $199,999, $25,000+ for DBB and HQ, $3,000 to $7,000, $1,000+) match the cache. X posts (Santiago, Bramlett, Prajwal, leo, Osika) and their status ids match. The Upwork titles and prices ($650, $30, $18,000, $1,000, $1,250) match.
- Failed (detail only): "GeekyAnts, Bengaluru, India" and "Connectish ... 10 to 49 staff" are not in the cache. URL clutch.co/profile/techstaunch-software-solutions is not in the cache. URL clutch.co/developers/artificial-intelligence (DBB row) is not in the cache.
- Downgraded: "Min project size $10,000+", "most common project size $10,000 - $49,999 based on 75 reviews" and "not asked to build from scratch" are shown in quotation marks but are the tool's own summary wording in the cache. The figures are right.
- The track's central claim, that no review showed a cost band, is consistent with the cache. The cache also contains the tool's warning that the Cleveroad excerpt was garbled, which the track repeats.

### Track 18 (Meta ads round 2): 1 failed
Every benchmark number matches its cache entry in context (WordStream $27.66, 2.59%, $1.92, 554 and 726 campaigns; $70.11, $5.26, 7.52%; Metadata $138/$145/$202/$524; $680/$510/$591; $1,680 to $3,080; GrowthSpree ranges; booked-call, show and close rates; Sprites.ai 1,079 and 304; 95K and 599%). Both seller quotes pass. The gate-2 arithmetic is labelled as the author's own and is correct. The claim of zero advertisers is consistent with the cache (S1, S5, S25, S27, S29).
- Failed: the $14.19 all-industry CPM is attributed to digitalapplied.com. S2 says "in one source" and does not name it.
- Note, not a failure: "Slopfix quotes $30-$100 fixed price" refers to slopfix.ptolemay.com (S9), which looks like a different product from the Odra "Slopfix" at $10,000 a week in tracks 17, 19, 21. Track 19 says so explicitly; track 18 does not.

### Track 19 (delivery round 2): 3 failed, 3 downgraded
Hours, timelines, the 958 findings and 58 criticals, 73 bugs, the 100 hour gap, Slopfix terms, QuickLaunch $120k+, VibeCodeFixers volumes, price anchors, the $100 per project post with 153 bidders and $96 average, and four of the five seller quote groups match. All 17 URLs are in the cache.
- Failed: "2026-03" date for the Cryptosaurus post and HN 47386636 (two table rows). No date in the cache.
- Failed: first HN seller quote, "date about 2025-09" and item id 45320431. N=25 says item ids, usernames and dates were not shown. The quote wording is verified.
- Downgraded: "starting around $299"; Red Leg Dev "2-6 weeks depending on the size and complexity of the codebase, starting with an audit"; Wavect "final week refunded if the work doesn't impress". All three are tool-summary wording, not in quotation marks.

### Track 20 (follow-ups round 2): 0 failed, 3 downgraded
Contra 171/234/$970K, Lovable directory hires and rates, retainer price list, Pakistan and India rate guides, Clutch counts, CAN-SPAM $53,088, PECR, CASL and Spam Act quotes, reply-rate numbers, UpGuard 16,326 and the four buyer-side quotes all match. All 64 URLs are in the cache. Lovable Cloud launch 2025-09-29 is in the cache (S "Lovable announced Lovable Cloud and Lovable AI on September 29, 2025").
- Downgraded: "requires you to: Send a password reset email to every user" (cache: tool paraphrase); "one shipped quick win" (cache: "deliver quick win"); "no commercial messages" (cache: "no statement that commercial messages are unwanted").

### model/offers.md: 1 failed
Section 0 and the buyer-evidence statements restate tracks 17, 21 and 22 correctly ($20 to $1,250; two $2,000 posts, 9+ months old, by title only; $1,500 and $2,500 posts not stated AI-built; zero cost bands). Seller prices and counts pass. Cost model rows are [A] or arithmetic.
- Failed: "$297 (TechPotions)" in the audit price list. The figure is in track 20 section 5; the pointer list on that line omits T20.

### model/channels.md: 1 failed
Benchmarks and funnel inputs map to the T18 table; reply rates to T20 #25; directory data to T20 #1, #7, #8; Upwork data to T17 and T21. The 38 unmatched numbers are all the author's derived or [A] values. The external Upwork Connects addition is labelled [X] in four places (intro tag key, section 3.4, input table, assumption list) with the note "verify in an account". It cannot be checked against the cache. Labelling requirement: met.
- Failed: "5 to 10% with any revenue (weak, T13)". Track 13 gives 7.6%.

### model/delivery.md: 0 failed, 1 downgraded
Evidence tags t19 #4, #5, #6, #8, #11, #13, t20 #4, #8, #19 and t21 #4, #7, #12 map correctly. Checklist items are [E] or [S] as tagged. Downgraded: checklist item F4 quotes "works in preview, fails when deployed" (propagated from track 21).

### model/risk.md: 0 failed, 2 downgraded
Section on commercial risk (the gate 1 paragraph) restates tracks 17 and 21 correctly. [GK] items are counted as assumptions; the one outside search [WS1] (Lovable terms on code ownership) is labelled. Downgraded: Lovable "may change criteria any time" and Slopfix pushback "$200 subscription gets similar value" (both tool paraphrase). Minor, not edited: "reviewer" for the $607.70 Replit figure (track says writer).

### model/brand.md: 1 failed (propagated), 2 downgraded (propagated)
Buyer-quote list (section 3) matches tracks 17, 21, 20. Competitor price table matches track 21. Propagated from track 21: "mean $40.8" marked [UNVERIFIED]; "works in preview, fails when deployed" marked [PARAPHRASE, NOT VERBATIM] in two places.

## Full list of failures and downgrades

| file | item | verdict | reason |
|---|---|---|---|
| tracks/17 | "11 of 18 posts stated as Lovable or AI-built" includes J14 | failed | number differs (supported count 10) |
| tracks/17 | J17 title "Supabase Schema & RLS Deployment" | downgraded | summary wording only |
| tracks/21 | Wajahat S. Upwork title "ClaudCod" | failed | wording differs (cache "ClaudeCod") |
| tracks/21 | Fiverr round-2 mean $51.2 (and combined $40.8) | failed | not reproducible from cache |
| tracks/21 | "works in preview, fails when deployed" | downgraded | summary wording differs |
| tracks/22 | GeekyAnts "Bengaluru, India" | failed | not in cache |
| tracks/22 | Connectish "10 to 49 staff" | failed | not in cache |
| tracks/22 | URL clutch.co/profile/techstaunch-software-solutions | failed | URL not in cache |
| tracks/22 | URL clutch.co/developers/artificial-intelligence | failed | URL not in cache |
| tracks/22 | "Min project size $10,000+" | downgraded | summary wording |
| tracks/22 | "most common project size $10,000 - $49,999 based on 75 reviews" | downgraded | summary wording (75 not in quotes; 77 is) |
| tracks/22 | "not asked to build from scratch" | downgraded | summary wording |
| tracks/18 | $14.19 CPM attributed to digitalapplied.com | failed | wrong or unconfirmed attribution |
| tracks/19 | "2026-03" date, two rows | failed | date not in cache |
| tracks/19 | HN quote 1: date about 2025-09 and item 45320431 | failed | not shown in cache |
| tracks/19 | "starting around $299" | downgraded | summary wording |
| tracks/19 | Red Leg "2-6 weeks depending on the size and complexity..." | downgraded | summary wording |
| tracks/19 | Wavect "final week refunded if the work doesn't impress" | downgraded | summary wording |
| tracks/20 | "requires you to: Send a password reset email to every user" | downgraded | summary wording |
| tracks/20 | "one shipped quick win" | downgraded | summary wording |
| tracks/20 | "no commercial messages" | downgraded | summary wording |
| model/offers | "$297 (TechPotions)" pointer | failed | wrong attribution (figure is in T20) |
| model/channels | "5 to 10% with any revenue (T13)" | failed | number differs (T13: 7.6%) |
| model/brand | mean $40.8 | failed | propagated from T21 |
| model/brand | "works in preview..." x2 | downgraded | propagated from T21 |
| model/delivery | "works in preview..." | downgraded | propagated from T21 |
| model/risk | "may change criteria any time" | downgraded | summary wording (T9/cache 09) |
| model/risk | "$200 subscription gets similar value" | downgraded | paraphrase shown as quote |

(The counts in the totals table group a few of these rows differently, for example the two track 19 date rows count as two items; the list above is the complete set.)

## Failures that touch a GO gate

None of the failures changes a gate-1, gate-2, gate-3 or gate-4 figure. The closest ones:
1. Track 17 "11 of 18" count (gate 1 context). Overstated by one (J14 is not stated as AI-built). It strengthens, not weakens, the point that the fix-post population is smaller than shown. No $1,500+ post is AI-built under either count.
2. Track 21 Fiverr mean $51.2 (gate 4, the price floor). Median $30 and max $250, the figures used in the gate-4 argument, are supported. Only the mean is not.
3. Track 18 $14.19 CPM attribution (gate 2 inputs). The value is in the cache; only the source name is unconfirmed. The channels.md CPM range ($9 to $15) is unaffected.

## What I found that matters for the orchestrator's gate read

- Gate 1: the evidence base is real and says what the tracks say. Verified in the cache: two $2,000 Upwork budgets (2025-10-28 Twilio and Stripe for a Lovable app; 2025-12-31 Base44 QA and launch), one $1,500 and one $2,500 Supabase hardening post where AI-built is not stated, the highest AI-built fix post at $1,200, and zero Clutch reviews with a cost band. No cache entry shows any buyer paying a human $1,500 or more. Reddit returned zero pages in tracks 17, 19, 20 and 22. Read stays "unproven, leaning not met". One nuance the tracks soften: the Twilio and Stripe post is "add Twilio and Stripe to an app whose UI is done" (new backend features) and the Base44 post is QA plus a WordPress migration; both are finish or launch jobs with feature scope, so they are weaker rescue evidence than a pure fix job. Both were found by title and search summary only; nobody opened them.
- Gate 2: nothing found is a measured cost per client. Verified: every Meta benchmark is a vendor number from another niche; T18 found 0 advertisers. channels.md's passes at Mid for platform directories ($425) and Upwork ($470) rest on [A] inputs (inquiries per month, win rates) and not on sourced data; its sourced inputs map correctly to T9, T18, T20, T21. The Upwork Connects costs are an outside search ([X]) that cannot be checked here. Read stays unproven.
- Gate 4: the floor figures (Fiverr median $25 to $30, max $250; Upwork $20 to $300 fix posts) hold. Track 21's "at least 8 small vendors at $1,400 to $2,500" is consistent with the vendors named across tracks 19 and 21.
- Conflict with another verifier's edit: track 03 has "Now he's hiring a developer to shore it up." marked [PARAPHRASE, NOT VERBATIM]. Cache 17 (S19 and S29) shows that sentence inside quotation marks as a tool-quoted fragment of HN item 44739556, so it would pass under the "all of cache/" rule. Worth a re-check by whoever owns track 03.
- Same-name risk: "Slopfix" is two vendors (Odra at $10,000 a week; slopfix.ptolemay.com at $30 to $100 per fix). Tracks 17, 19, 21 treat the first; track 18 uses the second without saying so. Do not merge them in the final report.
- Model files predate or lack track 22: risk.md and brand.md say track 22 was not in the folder when written. Their gate 1 text is still consistent with track 22 (no cost bands), but they do not cite it.
- Propagation timing: tracks 1 to 16 were being edited by other verifiers while I ran. I propagated only what was marked at my last check (tracks 3, 9 to 13, 15, 16 appendices). I grepped all five model files for those items (30,998 apps; RapidDevelopers $8,000 to $35,000; internetwache URL; 10Pearls 2008; HN 13777251 year 2017; "hire a verified expert") and none appears in the model files. Re-run that grep after the other two verifiers finish.

## Edits made

Inline markers and a "## Appendix: unverified items" section were added to: tracks 17, 18, 19, 20, 21, 22 and model/brand, channels, delivery, offers, risk. No content was deleted.
