# Verification log (Phase 3, merged)

Method: three verifiers re-checked every quote, username, date, price, count and URL in 22 track files, 3 shared tables, phase1-summary.md and 5 model files against the cached WebSearch output in cache/. No web access. Procedure: verification-procedure.md. Items the files label as assumptions ([A], [E], [GK], [V], "my arithmetic") were counted, not verified. Failed items are tagged [UNVERIFIED] in place and listed in each file's "Appendix: unverified items". Quotes whose words appear only in the search tool's summary (not inside quotation marks there) are tagged [PARAPHRASE, NOT VERBATIM].

Important caveat on what "verified" means here: a pass means the item matches the cached search-result text. No source page was ever opened in this run (network policy). So "verified" means "faithfully transcribed from search output", not "confirmed against the original page".

## Totals (approximate, plus or minus 5 to 10%)
| verifier | files | checked | passed | failed | downgraded | labelled assumptions |
|---|---|---|---|---|---|---|
| 1 | tracks 01-08, ads-library, pricing-map, competitors | ~942 | ~915 | 11 | 16 | ~62 |
| 2 | tracks 09-16, phase1-summary | ~1,005 | ~895 | 9 | 21 | ~80 |
| 3 | tracks 17-22, model/* (5 files) | ~1,033 | ~1,003 | 14 | 16 | ~104 |
| total | 31 files | ~2,980 | ~2,813 | 34 | 53 | ~246 |

## Gate-relevant outcome
- No failure changes a GO-gate figure. The gate 1 evidence (two $2,000 Upwork buyer budgets dated 2025-10-28 and 2025-12-31; $1,500 and $2,500 Supabase posts not stated as AI-built; top AI-built fix post $1,200; zero buyer payments at $1,500+; zero Clutch cost bands) is confirmed exactly as stated in the tracks.
- Gate 4 floor figures hold (Fiverr min $5, median $25 to $30, max $250; Upwork fix posts $20 to $300). Do not quote the Fiverr means ($51.2, $40.8): they do not reproduce. Use medians.
- Gate 2: every Meta benchmark is vendor data from other niches; 0 advertisers evidenced. channels.md's cheap channels rest on [A] inputs.
- Gate 3: the security and data-access hardening list is sourced; 29 of 38 checklist items in track 11 are engineering judgment [E].
- Nuance flagged by verifier 3: the two $2,000 posts are feature-scoped finish or launch jobs (add Twilio and Stripe; QA plus migration), seen by title only, so weaker rescue evidence than a pure fix job.
- "Slopfix" is two different vendors: Odra at $10,000 a week and slopfix.ptolemay.com at $30 to $100 per fix. Do not merge them.
- Verifier conflict: track 03's "Now he's hiring a developer to shore it up." was downgraded by verifier 1 but appears inside quotation marks in cache 17 (S19, S29), so it passes as a tool-quoted fragment of HN 44739556. Treat as a verified snippet-quote (secondhand, about a friend).
- Bookkeeping: most tracks' JSON "sources_read" equals searches run, not pages opened (none were). Tracks 13 and 16 report 0. Treat the field as "searches with results".

## Full lists of failures and downgrades
See the three logs below, appended verbatim.


---

# verification-log-1.md

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

---

# verification-log-2.md

# Verification log 2 (Verifier 2)

Date: 2026-10-20. No web access used. All checks are against cache/*.md only.

## Files checked
tracks/09-platform-programs.md, tracks/10-practitioner-economics.md, tracks/11-technical-failure-patterns.md, tracks/12-platform-trajectory.md, tracks/13-outbound-feasibility.md, tracks/14-retention.md, tracks/15-trust-and-geography.md, tracks/16-offer-shapes.md, phase1-summary.md. All nine were checked in full. None skipped.

## Method
- Quotes: normalised phrase search over all cache files, then a check of whether the cache shows the words inside quotation marks. Words found only in the search tool's own summary text (no quotation marks) were downgraded to [PARAPHRASE, NOT VERBATIM].
- Numbers, dates, URLs: every distinct figure, date and URL in each file was searched in the cache; missing ones were checked by hand. Subject match was checked by hand for every gate-relevant figure and for all figures that looked off. Bare ordinals (list numbers, checklist item numbers) and plain years were not counted as items.
- Counts below are approximate (plus or minus about 10%) because the item list was built partly by script (URLs, numbers) and partly by hand (quotes, names).
- Items the files label as [E], "inferred", "my arithmetic", "paraphrase from search summary", "could not verify", "unsettled" or "NOT SEARCHED" are counted as labelled assumptions, not claims.
- Edits: [UNVERIFIED] or [PARAPHRASE, NOT VERBATIM] inserted before the item; an "Appendix: unverified items" section added where something failed. No content deleted.

## Totals (all nine files)
| | checked | passed | failed | downgraded | labelled assumptions |
|---|---|---|---|---|---|
| Total | 1005 | 895 | 9 | 21 | 80 |

## Per file
| file | checked | passed | failed | downgraded | labelled assumptions |
|---|---|---|---|---|---|
| 09-platform-programs | 98 | 88 | 1 | 3 | 6 |
| 10-practitioner-economics | 102 | 89 | 0 | 3 | 10 |
| 11-technical-failure-patterns | 119 | 85 | 1 | 1 (2 places) | 32 (29 [E] checklist items, 2 inference findings, 1 triage hypothesis) |
| 12-platform-trajectory | 148 | 139 | 0 | 4 (5 places) | 5 |
| 13-outbound-feasibility | 113 | 100 | 1 | 2 | 10 |
| 14-retention | 123 | 115 | 0 | 0 | 8 |
| 15-trust-and-geography | 96 | 90 | 2 | 1 | 3 |
| 16-offer-shapes | 78 | 69 | 1 | 6 (8 places) | 2 |
| phase1-summary.md | 128 | 120 | 3 | 1 | 4 |

## Failures (file, item, reason)
1. tracks/09, key finding 4: the label "hire a verified expert" for the Lovable Partner Directory. Not in cache. Cache only says the directory is a "Partner Directory" and a "new way for organizations to discover and hire Experts and Solution Partners". Marked [UNVERIFIED].
2. tracks/11, section 5 table: "30,998 apps scanned" (Reeve August 2026 sample, "from page title"). Number appears nowhere in cache or in any other file. Marked [UNVERIFIED].
3. tracks/13, key finding 10: URL en.internetwache.org/certificate-transparency-as-a-source-for-subdomains-14-12-2017/. Cache has only the title "Certificate Transparency as a source for subdomains (2017)" at internetwache.org, not this URL. Marked [UNVERIFIED].
4. tracks/15, section 5 table: 10Pearls "founded 2004 ... (another says 2008)". Cache has one source (2004). The 2008 in cache belongs to Tkxel. Marked [UNVERIFIED].
5. tracks/15, key finding 5 and two table rows: date "2017" for HN item 13777251. Cache gives no date for that item (only "HN threads 2011-2019"). Looks inferred from the item id. Marked [UNVERIFIED].
6. tracks/16, key finding 8 and section 5 table: "$8,000 to $15,000" and "$15,000 to $35,000" attributed to RapidDevelopers (hiring-a-lovable-developer page). Cache says only "One vendor puts...". Figures are in cache; the named vendor and URL are not tied to them (wrong attribution). Marked [UNVERIFIED].
7. phase1-summary.md, Gate 2 read: "maybe 5 to 10% with any revenue". Track 13 labels this "my arithmetic on a weak source, not a measured figure". Label dropped in the summary. The same BigIdeasDB source also says none of the revenue-verified startups cleared $1,000 in 30 days, which the summary omits. Marked [UNVERIFIED].
8. phase1-summary.md, Gate 3 read: "independent security research (... Reeve 57% of 3,680 ...)". Wrong attribution. Track 11 grades Reeve as security-vendor marketing relayed by an aggregator; the 170 of 1,645 scan is an independent researcher relayed by a vendor blog. Numbers match; "independent" does not. Marked [UNVERIFIED].
9. phase1-summary.md, prior finding on Pakistani freelancers: "two Islamabad/Bahawalnagar sellers, Fiverr sellers Kamran Asif, Ahmed Javed" as proof. Track 21 says "Seller countries were not stated in snippets" for Kamran Asif and Ahmed Javed, and the Islamabad Upwork title (Wajahat S.) is already marked [UNVERIFIED] in track 21. Marked [UNVERIFIED].

## Downgrades ([PARAPHRASE, NOT VERBATIM]): cache shows the words only in the search tool's summary
- 09: "as of September 2026"; "does not charge commissions"; "launch and scale certification programs, training, FDE playbooks".
- 10: "One week. Three senior engineers. $10,000." (the $10,000 / one week / three engineers facts pass; the wording is the tool's); "the market wasn't quite ready"; "only ever bring in consultants when they need a fix and are in a hurry".
- 11: "insufficient database RLS policy in Lovable through April 15, 2025" (key finding 1 and section 4; the cache labels this a tool-written summary, not a quote. The separate NVD "disputed by the Supplier" text IS in quotation marks and passes).
- 12: TechTimes headline "Lovable Says It Hit $500 Million Run Rate: Vibe Coding's Maintenance Test Still Looms" (rebuilt from a URL slug; 3 places); "four in five users identify with non-technical roles"; the runtimewire sentence "The black-box scan found a separate admin dashboard ..." (cache quotes only the part after "scan", and "The black-box scan" was added).
- 13: "101,034 current Lovable customers"; "117,323 websites in this full report, of which 16,289 are redirects" (numbers pass; quoted wording is the tool's).
- 15: "HQ & Other Offices" (cache says "HQ and other offices", no quotes).
- 16: "If we cannot deliver a quoted fix, you do not pay for it" (2 places); "usually $100 or $300"; "when you ship the fixes, we re-verify the critical findings at no extra cost"; "Roadmapping is essentially taking the discovery work ..." (2 places); "fixed price requires airtight scope" (2 places); "free or fixed-price (typically 2-5 business days, $0-$500)" (also drops the word "code").
- phase1-summary: "four in five identify with non-technical roles" (same phrase as track 12; also missing the word "users").

## Notes on passes that depend on another cache file
- 09 "no longer active - it has been replaced by our Solution Partner Program": passes, because cache/20-followups-searches.md shows it inside quotation marks. In 09's own cache it is unquoted.
- 16 "Cancel any week. Last week refunded if we didn't blow you away.": passes via cache/20-followups-searches.md (quoted there). Unquoted in 16's own cache.
- 10 "a thin advertorial" and "maintenance work: $100/hr; vibe-coding cleanup: $200/hr": pass via cache/19-delivery-searches.md (quoted there). Note the cache calls the $100/$200 line a "jab, not invoice".
- 12 URL ecosistemastartup.com/lovable-cruza-us600m-arr-...: path matches the cache, but the cache spells the domain "ecosystemastartup.com" in that entry (and "ecosistemastartup.com" in another). Passed as a cache typo.
- 12 lovable.dev/es/blog/wiz-findings-now-in-lovable: cache lists it as lovable.dev/{de,ja,it,pt-br,id,es,ko,fr,hi}/blog/...; passed.

## The three most consequential failures for the verdict
1. phase1-summary Gate 2 read: the "5 to 10% with any revenue" figure lost its "my arithmetic" label, and the source's "none cleared $1,000 in 30 days" was left out. This makes the outbound pool look more able to pay than the evidence shows. Touches gates 1 and 2.
2. phase1-summary Gate 3 read: Reeve is called "independent". It is vendor marketing. Also, the Gate 3 tally counts track 11 as plain support, but track 11's JSON says "3 (security hardening part only)" and its text says repeatable full-rescue list is "unclear". Touches gate 3.
3. phase1-summary prior finding on Pakistani freelancers: the Fiverr names are used as proof of Pakistani sellers but track 21 says seller countries were not stated. The "brief claim confirmed" status should drop to "partly confirmed (XCONS Lahore, Bahawalnagar seller)". Touches gate 4 (the floor).
No failure in tracks 9 to 16 themselves changes a GO-gate number. All track-level failures are labels, one dated attribution, one URL and one stray number (30,998).

## What should change in the orchestrator's gate read
- Gate 1: no change. Nothing in tracks 9 to 16 is a buyer payment. Every price in 9, 10, 14, 16 is a seller ask or a vendor guide. The one buyer price in these files ($600 for 2 days, track 10) is a second-hand paraphrase through a vendor blog, labelled as such. Keep "UNCLEAR, leaning NOT MET".
- Gate 2: soften the outbound line. Drop "maybe 5 to 10% with any revenue" or restate it as: BigIdeasDB says 7.6% of revenue-verified startups on vibe-coding subdomains report any MRR and none cleared $1,000 in 30 days; the base is founders who opted in, so it cannot be scaled to 101k sites. Also note track 13's legal section is background knowledge, unsourced (the sourced legal map is in track 20, which this log did not check).
- Gate 3: say "security and data-access hardening list is sourced and repeatable; the rest of the checklist is Wanile judgement". In track 11, 29 of the 38 checklist items are [E] (no source), including Stripe webhooks, error handling and deploy. Those are only supported by the seller lists in track 19. Do not count tracks 10, 12 and 14 as strong support: they say "weakly supports", resting on one seller anecdote (10, 14) and inference (12).
- Gate 4: the summary says SUPPORTED. The track files say less. Track 15: buyers appear to expect a Pakistan discount (old anecdotes, but it pushes against a premium position). Track 09: Base44 partner listings sit at $10 to $100/hr (self-declared). Track 16: audit price floor of $199 to $399 exists. Track 14 and 09 give only "weakly supports". Suggest "UNCLEAR, weak support" and add the geography discount risk.
- Gate 5: keep "UNCLEAR, leaning pass". The track 12 numbers (1M projects a week, 50M projects, 80%) are vendor and unaudited, and Lovable does not say how many projects are alive. Add two risks from tracks 9 and 14: platforms intermediating (Base44 in-product marketplace, a 15% fee that two cache entries contradict) and AI-patched small bugs shrinking small-fix retainers. Track 9's open question on Replit "Hire App Builder" is answered in track 20 (redirect to Contra), not in track 9.
- Phase1-summary table: columns "sources" for tracks 13 and 16 show 0 because their JSON blocks say 0 although 11 and 8 searches returned results. Word counts and every other cell in the rows for tracks 9 to 16 match the JSON blocks and the files. Gate tally matches the JSON blocks. (The tally says "11 of 21 tracks" for gate 3; track 22 exists but is not in the table.)

## File-level problems
- 13 and 16: JSON blocks say sources_read 0; text says 11 and 8 searches returned results. 16: JSON seller_quotes 4, section 4 lists 5 (one flagged "do not use").
- 15: text says "13 searches ran (11 returned results, 1 domain-blocked error, plus 3 more refused)"; the cache has 13 result entries plus 1 error entry. Counts do not reconcile.
- 09: text says 11 standard and 5 extended searches; the cache shows 13 standard and 3 extended.
- 09 key finding 6 reports both "no commission" and "15%" for Base44. The file flags the conflict and grades the 15% weak; the cache shows the same conflict. Not a verification failure.
- 10 header says Reddit voices "returned nothing relevant"; consistent with cache. The HN point counts (304, 501, 262, 250) from the brief remain unverified in every file, as the files themselves say.
- 11 cites Tea app date "July 2025" for the breach; cache supports it only through a simonwillison.net/2025/Jul/26 link, not an explicit date. Accepted.
- 12 cache entries are dated 2026-10-20; most other cache files are 2026-10-21. Derived day-counts in track 10 ("104 days old", "132 days") depend on 2026-10-21 and check out arithmetically (about 2026-07-09 and 2026-06-11).
- Other verifiers have been editing tracks 17 to 22 at the same time. Phase1-summary statements that rely on those tracks (Fiverr $5 to $250, "at least 8 studios at $1,400 to $2,500", $17/hr, 18 Upwork posts, $1,200 ceiling, $2,000 posts) were matched only against the track text, not the cache. They are consistent with the track text as it stood, apart from item 9 above.

---

# verification-log-3.md

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
