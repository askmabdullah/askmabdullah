# Verification log 1 (Verifier 1)

Date: 2026-10-20. No web access used. All checks are against cache/*.md.

Method: read BRIEF.md sections 7 and 8, then verification-procedure.md. For each file I listed quotes, handles, dates, prices, counts and URLs. URLs were checked in bulk by script (normalised, case-insensitive substring in cache). Quotes, prices, dates and counts were checked with grep -i -F on distinctive fragments, then read in context (same subject, and whether the words sit inside quotation marks in the cache). For the Fiverr and Upwork tables I re-parsed the cached titles by script (handle, price, posted date) and recomputed the min, median and mean.

Counts are approximate (about 5 percent) because URLs, table rows and prices were checked in bulk. Failures and downgrades are exact.

## Totals (all 11 files)

| | count |
|---|---|
| Items checked | about 942 |
| Passed | about 915 |
| Failed (marked [UNVERIFIED]) | 11 |
| Downgraded (marked [PARAPHRASE, NOT VERBATIM]) | 16 |
| Labelled assumptions or paraphrases (not verified, by rule) | about 62 |

## Per file

| file | checked | passed | failed | downgraded | labelled assumptions |
|---|---|---|---|---|---|
| tracks/01-lovable-builders.md | 66 | 64 | 1 | 1 | 5 |
| tracks/02-other-platform-builders.md | 62 | 59 | 2 | 1 | 6 |
| tracks/03-nontech-founders-with-revenue.md | 38 | 34 | 0 | 4 | 5 |
| tracks/04-burned-by-freelancers.md | 50 | 47 | 1 | 2 | 4 |
| tracks/05-meta-ads.md | 44 | 44 | 0 | 0 | 5 |
| tracks/06-google-search.md | 83 | 79 | 1 | 3 | 3 |
| tracks/07-marketplaces.md | 120 | 118 | 2 | 0 | 4 |
| tracks/08-competitors.md | 59 | 57 | 0 | 2 | 4 |
| ads-library.md (rounds 1 and 2) | 97 | 97 | 0 | 0 | 12 |
| pricing-map.md (rounds 1 and 2) | 200 | 195 | 3 | 0 | 6 |
| competitors.md (rounds 1 and 2) | 123 | 121 | 1 | 3 | 8 |

Notes on counting: the 06 failure is one item that appears in two places (finding 7 and the numbers table). The 03 downgrades are four items (finding 1 pair counted once, B1, B2, S3). The pricing-map failures are three items (the "30 priced" count, the round 2 mean, the combined mean and "50 gigs").

Each edited file now ends with "## Appendix: unverified items". Files with nothing to report (05, ads-library.md) have an appendix that says "none".

## Full list of failures (marked [UNVERIFIED])

| # | file | item | reason |
|---|---|---|---|
| 1 | tracks/01 | Counts line "10 searches run" | number differs: cache/01 has 9 result sets plus 1 domain error |
| 2 | tracks/02 | "5 threads" (v0 deployment threads on community.vercel.com) | number differs: cache/02 lists 7 distinct thread links |
| 3 | tracks/02 | "15 returned results" (search count) | number differs: cache/02 has 14 result sets |
| 4 | tracks/04 | IH post title "Vibe-coding your MVP is free. Your token bill says otherwise" | not in cache. Only "$400 in tokens" and a "token bill post" appear |
| 5 | tracks/06 | "5 of 9" Fiverr pages for "fix my lovable app" (finding 7 and numbers table) | number differs: cache/06 shows 6 of 9 are Fiverr. The track's own handle list also names six |
| 6 | tracks/07 | URL for Jose_ph18 gig | wording differs: track slug "...lovable-ai-developer-ai-developer-v0", cache slug "...lovable-dev-ai-ai-developer-v0". Handle and $30 price verified |
| 7 | tracks/07 | "Only 8 searches returned results: 4 fiverr, 4 upwork" | number differs: cache/07 has 9 result sets (4 Fiverr, 5 Upwork) |
| 8 | pricing-map.md | Round 2 Fiverr "30 priced gigs" | number differs: cache/21 searches #30 to #37 hold about 40 distinct fix/deploy/audit gigs |
| 9 | pricing-map.md | Round 2 "mean $51.2" | number differs: recompute gives about $46 to $47 for 40 gigs (same failure already marked in tracks/21) |
| 10 | pricing-map.md | Combined "50 gigs ... mean $40.8" | number differs: 60 gigs, mean about $39. The combined median $25 does reproduce |
| 11 | competitors.md | Row 31 gig title "fix broken Lovable app in 1hr" | wording differs: cache title is "I will fix broken lovable website or app in 1hr" |

Min $5, median $30 (round 2), median $25 (combined) and max $250 all reproduce. Round 1 Fiverr stats (20 gigs, min $5, median $20, mean $25.25, max $100) reproduce exactly, and every one of the 22 gig handles and prices in track 07 matches its cached title.

## Downgraded (marked [PARAPHRASE, NOT VERBATIM])

The words are in the cache, but only inside the search tool's summary, not inside quotation marks.

1. tracks/01: "self-identified non-technical roles".
2. tracks/02: S1 nichochar quote ("they outsourced the backend ... incredibly low"). Only the word "useful" is quoted in the cache.
3. tracks/03: finding 1 pair, "with little marketing" and "Now he's hiring a developer to shore it up."
4. tracks/03: B1, the same HN sentence in the buyer-quote block.
5. tracks/03: B2, "In my case, i needed around 300 messages to get here."
6. tracks/03: S3, "Plenty of non-technical founders are vibe-coding products..."
7. tracks/04: Create Designs quote ("In one recent case ...").
8. tracks/04: HN quote ("the speed at which AI-generated codebases grow ...").
9. to 11. tracks/06: all three seller quotes (version history, read the exact error message, duplicate the project).
12. tracks/08: MetaCTO "Audit is free (48 hours). Rescue engagements run $50-150k ..." (the track admits the tool did not quote it).
13. tracks/08: Valletta "The Valletta Vibe Coding Audit is a fixed-fee senior-engineer review ...".
14. competitors.md row 2: MetaCTO quote (same as 12).
15. competitors.md row 16: "40+ AI-powered applications".
16. competitors.md row 19: "case studies with live URLs and client outcomes".

Verified as true quotes (inside quotation marks in the cache): the Trustpilot "AI repeated the same coding errors" quote and the two "Try to Fix" lines (track 01), all five tracks/02 buyer quotes and S2 and S3, the Hamid Siddiqi quote and the 404 Media/Slashdot line (track 03), the Contractors quote (track 04), the two X posts from ibo and Santiago (track 05), all Upwork job titles and Fiverr gig titles (tracks 07 and 08), and the Slopfix, PC Gamer and WebProNews titles.

## Three most consequential failures for the verdict

None of the 11 failures touches a GO gate figure. The three that come closest, all on gate 4 (the price floor) or on how much weight a quote can carry:

1. pricing-map.md: the round 2 Fiverr mean ($51.2) and combined mean ($40.8). The floor and the median are what gate 4 uses, and those reproduce. The error is small and the real mean is lower, so the floor is if anything lower than stated.
2. tracks/06: "5 of 9" Fiverr results. The cache shows 6 of 9. This slightly strengthens the "Fiverr owns this query" read.
3. The downgrades on tracks/03 (B1, B2, S3). Both "buyer quotes" in track 03 are now paraphrases, so track 03 has zero verbatim buyer quotes. It was already graded weak.

## Gate-relevant checks that PASSED (no change needed)

- Gate 1 evidence in my files is all verified exactly against cached titles: Upwork buyer budgets of $2,000 fixed (Twilio/Stripe on a Lovable app, posted 2025-10-28; Base44 launch and QA, posted 2025-12-31), $1,000 (Refine and Deploy Lovable App with Supabase, 2026-04-03), $1,200 (2026-10-15) and $1,250 (2026-08-19). Seller prices also verified: Slopfix $10,000 per week, Forasoft $2,500 per week start, GainCafe $2,500, AfterBuild $1,999, Arkroot EUR 1,999, Teyrex $1,400, Base44Devs $1,500 sprint, Justin McKelvey $25K to $50K. No confirmed buyer payment of $1,500 or more exists in any of these files.
- Gate 2 figures verified as vendor-published: WordStream CPL $27.66, Google CPL $70.11, B2B SaaS Meta CPL $63.40 and $80 to $220, software development lead $680 paid, $1,680 to $3,080 per software/IT sales-qualified lead, cost per booked call $80 to $150. Track 05 and ads-library.md are correct that zero advertisers were evidenced.
- Gate 3 and gate 4 figures verified: Fiverr starting prices $5 to $250, $19 and $39 VibeSafe scanners, and the Upwork and Fiverr fix lists.
- Gate 5 is not touched by these files.

## Anything that should change the orchestrator's gate read

1. Track 07 says the top fix/finish price on the marketplaces is $1,000, and its JSON lists gate 1 as contradicted. The round 2 data in pricing-map.md (verified) supersedes that: two Upwork buyer budgets of $2,000 exist. Both are over 9 months old, both are posted budgets and not payments, and one is a QA and migration job, not a pure rescue. Gate 1 should be read as "budgets of $1,000 to $2,000 are posted by buyers; no payment of $1,500 or more is confirmed", not as "contradicted".
2. After the downgrades, the first-person evidence of "founder stuck, then hired a developer" in my files is all second-hand paraphrase (track 03 B1, IH "20 breaks" in track 02). Gate 1 buyer proof must come from other tracks.
3. Search-count claims in tracks 01, 02 and 07 do not match the cache (9 vs 10, 14 vs 15, 9 vs 8). This is a process stat only, but any FINAL-REPORT line that quotes "N searches" for these tracks should use the cache counts.
4. The pricing-map round 2 Fiverr mean should not be quoted. Use the median ($30 round 2, $25 combined) and the min and max.
5. Note on track 04: the G2 review is in the cache as "paid $1,000 for a website rebuild" and "the freelancer took the $650 they had paid". The track says the freelancer "kept $650". The numbers match but the relationship is ambiguous. I did not flag it. Treat it as "$650 lost".

## File-level problems

- tracks/03 JSON block: "buyer_quotes": 2 and "seller_quotes": 3. After verification, 0 buyer quotes and 2 seller quotes are verbatim. The JSON was not edited.
- tracks/06 JSON block: "seller_quotes": 3. None of the three is verbatim in the cache. The JSON was not edited.
- tracks/08 JSON block: "seller_quotes": 6, of which 2 are paraphrase after verification. The JSON was not edited.
- tracks/06 mentions 4 refused searches. The cache confirms it (4 NOT PERFORMED entries), and it also shows 12 searches with results, as claimed.
- tracks/07: the Fiverr table row for James_patience has a URL slug that does not match the title (already flagged by the track itself). The cache confirms both title and slug, so the mismatch is real in the source.
- tracks/02 section 4 labels the "$70 in a night" quote's outlet as inferred. Cache confirms the words and the Register context loosely. Left as the track labelled it.
- Process counts in tracks/03 ("10 HN titles + 10 IH titles + 9 vendor pages + 2 mirror pages") and in several "N gigs seen" lines were not individually recounted. They are the agents' own tallies.
- All files were checked. None were skipped for time.
