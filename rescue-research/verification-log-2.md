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
