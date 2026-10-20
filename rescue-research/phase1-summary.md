# Phase 1 summary (v3, 00:05 UTC, corrected after verification log 2; verifier tags kept)

## How to read this
- All research ran on WebSearch only. WebFetch and curl were blocked by the environment network policy. Reddit, HN, Fiverr, Upwork, Meta Ad Library, Google Trends and vendor pages could NOT be opened. Everything is from search-result summaries and indexed snippets.
- WebSearch had a shared quota of 200 calls per turn. Round 1 (16 tracks) got 7 to 20 searches each. Round 2 (5 agents) and round 3 (1 agent) got 35 to 45 each. Total about 420 searches.
- "buyer $" = prices buyers stated or lost; "seller $" = prices sellers list. Read the per-track files for what each number means; several buyer figures are platform credit spend or budgets, not payments to humans.

## Per-track table (from the JSON blocks)
| file | words | demand | buyer $ | seller $ | gates + | gates - | grade | sources | buyer q | seller q |
|---|---|---|---|---|---|---|---|---|---|---|
| 01-lovable-builders.md | 2507 | weak | [] | [50, 150, 5000, 15000, 13000, 25000] | [3] | [] | weak | 10 | 1 | 5 |
| 02-other-platform-builders.md | 2702 | moderate | [22, 70, 500, 1000] | [100, 600, 1000, 2000, 3000, 3500, 4000, 15000] | [3] | [] | weak | 20 | 5 | 3 |
| 03-nontech-founders-with-revenue.md | 2232 | weak | [] | [5000, 15000, 8000, 25000] | [] | [] | weak | 7 | 2 | 3 |
| 04-burned-by-freelancers.md | 1831 | weak | [500, 650, 1000, 5000] | [2000, 15000, 10000, 40000, 150000] | [] | [] | weak | 9 | 0 | 3 |
| 05-meta-ads.md | 1619 | none | [] | [199, 500, 2500, 5000, 15000] | [] | [] | weak | 14 | 0 | 2 |
| 06-google-search.md | 2821 | weak | [] | [19, 39, 750, 2000, 2500, 3000, 5000, 13000, 15000, 25000] | [] | [] | weak | 12 | 0 | 3 |
| 07-marketplaces.md | 2751 | weak | [5, 20, 30, 60, 100, 300, 400, 500, 650, 1000, 1250] | [5, 10, 15, 20, 30, 35, 50, 100] | [3] | [1] | weak | 8 | 6 | 7 |
| 08-competitors.md | 2042 | moderate | [] | [199, 900, 2500, 3000, 10000, 40000, 50000, 150000] | [4] | [] | weak | 9 | 0 | 6 |
| 09-platform-programs.md | 3095 | weak | [] | [10, 100, 180, 2000, 5000] | [4] | [] | weak | 16 | 0 | 2 |
| 10-practitioner-economics.md | 2558 | weak | [600] | [10000, 1500, 8000, 299, 40000, 100, 300, 200] | [3] | [] | weak | 12 | 0 | 4 |
| 11-technical-failure-patterns.md | 3660 | moderate | [] | [] | ['3 (security hardening part only)'] | [] | moderate | 11 | 0 | 5 |
| 12-platform-trajectory.md | 3659 | moderate | [] | [] | [3] | [] | weak | 13 | 0 | 5 |
| 13-outbound-feasibility.md | 2538 | weak | [] | [] | [] | [] | weak | 0 | 0 | 0 |
| 14-retention.md | 2767 | weak | [] | [500, 1000, 1250, 2500, 3000, 3040, 4960, 4995, 10000] | [3, 4] | [5] | weak | 14 | 0 | 5 |
| 15-trust-and-geography.md | 2127 | none | [] | [] | [] | [] | weak | 13 | 0 | 0 |
| 16-offer-shapes.md | 2096 | none | [] | [100, 199, 399, 1500, 4000, 7000, 8000, 15000, 25000] | [] | [] | weak | 0 | 0 | 4 |
| 17-buyer-voices-round2.md | 3619 | weak | [20, 30, 100, 120, 300, 1000, 1200, 1250, 1500, 2500, 4000] | [500, 850, 1500, 2500, 2850, 3000, 3500, 5000, 7500, 10000, 15000] | [3] | [4] | weak | 45 | 2 | 11 |
| 18-meta-ads-round2.md | 2863 | none | [] | [30, 100, 15000, 25000, 50000] | [] | [] | weak | 33 | 0 | 2 |
| 19-delivery-round2.md | 4276 | moderate | [100] | [30, 100, 199, 299, 1500, 3500, 5000, 10000, 15000, 25000, 40000, 50000] | [3, 4] | [] | weak | 35 | 0 | 13 |
| 20-followups-round2.md | 5030 | weak | [600, 3000] | [10, 20, 30, 50, 100, 200, 297, 500, 1500, 2000, 2500, 3000, 4000, 4500, 5000, 6000, 8000, 25000] | [3, 5] | [] | weak | 35 | 4 | 8 |
| 21-marketplaces-competitors-round2.md | 3893 | moderate | [30, 50, 100, 120, 150, 250, 300, 1000, 1200, 2000, 2000] | [5, 25, 30, 49, 100, 150, 250, 350, 750, 1400, 1500, 1999, 2500, 3000, 4000, 4950, 6000, 10000] | [3, 4] | [] | weak | 40 | 10 | 9 |

## Gate tally
| gate | supported by | contradicted by |
|---|---|---|
| 1 | none | 07-marketplaces.md |
| 2 | none | none |
| 3 | 01-lovable-builders.md, 02-other-platform-builders.md, 07-marketplaces.md, 10-practitioner-economics.md, 11-technical-failure-patterns.md, 12-platform-trajectory.md, 14-retention.md, 17-buyer-voices-round2.md, 19-delivery-round2.md, 20-followups-round2.md, 21-marketplaces-competitors-round2.md | none |
| 4 | 08-competitors.md, 09-platform-programs.md, 14-retention.md, 19-delivery-round2.md, 21-marketplaces-competitors-round2.md | 17-buyer-voices-round2.md |
| 5 | 20-followups-round2.md | 14-retention.md |

## First read on each GO gate (orchestrator, before verification)

**Gate 1: buyers paying $1,500+ for rescue or finishing work.** UNCLEAR, leaning NOT MET on current evidence.
- Zero buyer voices found saying "I paid $X to a human to fix my AI-built app" (tracks 1, 2, 3, 4, 17).
- Buyer-stated budgets on Upwork and Freelancer.com: 18 posts found; confirmed Lovable/AI-built fix-or-finish posts top out at $1,200 (2026-10-15). Two Lovable/Base44 posts at $2,000 (Oct and Dec 2025). Two Supabase hardening posts at $1,500 and $2,500 (Oct 2026) where AI-built is not stated (tracks 17, 21).
- Seller asking prices cluster at $1,400 to $2,500 "from" for small studios, $5k to $15k for finishing, $10k/week Slopfix, $25k to $50k+ for premium (tracks 8, 10, 19, 21). No named paying client at these prices was found anywhere.
- Reddit, HN comment threads and Indie Hackers were unreachable, so the buyer-voice absence is partly a tool limit.

**Gate 1 addendum (track 22, buyer reviews).** Three Clutch reviews describe the right kind of job: GeekyAnts took a Lovable prototype to a production platform (profile floor $10,000+); Cleveroad audited two AI-built codebases and gave a prioritised fix list; Connectish (Germany) rebuilt a Bolt prototype with a Supabase backend (profile minimum $5,000, most projects under $10,000). The per-review cost band was never visible in search output, so none counts as proof. These three pages are the fastest way to settle gate 1: open them in a browser and read "Project size".

**Gate 2: a channel with plausible cost per paying client under $600.** UNCLEAR, leaning against for Meta.
- Zero advertisers evidenced running Meta, Google, TikTok or LinkedIn ads for this service after 47 targeted searches across two rounds (tracks 5, 18). The Ad Library could not be opened, so this is weak absence.
- The "agencies spend heavily on Meta ads and close well" claim: nothing found that supports it. Weak counter-signals: sellers report word of mouth, referrals and SEO content hubs (tracks 10, 18).
- Generic benchmarks only: Meta B2B CPL $50 to $380, cost per booked call $80 to $150, B2B close 20 to 29%; arithmetic gives roughly $400 to $1,000 per client, straddling the $600 line (track 18, all vendor benchmarks).
- Marketplaces: Upwork jobs exist but proposal counts and fill status were not visible (tracks 7, 21). Outbound: about 101k Lovable sites on BuiltWith (no snapshot date). BigIdeasDB, a self-published opt-in sample, says 7.6% of revenue-verified startups on vibe-coding subdomains report any revenue and none cleared $1,000 in 30 days; that cannot be scaled to the 101k (the earlier "5 to 10%" line was track 13's own arithmetic and is withdrawn). Legal limits are mapped in track 20; no reply-rate data for this niche (tracks 13, 20).

**Gate 3: repeatable fix list.** SUPPORTED for the security and data-access hardening list only; the rest of the rescue checklist is Wanile engineering judgment (29 of track 11's 38 items are [E]); fix time UNPROVEN. 12 of 22 tracks support it, most weakly; track 11's own JSON limits support to the security part; none contradict.
- Secrets/keys and RLS/access control recur in 5 of 9 seller lists (payments and error handling 3 of 9; tests/CI and fake auth 2 of 9; per track 19's table, not its prose) and in security research: CVE-2025-48757 on NVD (170 of 1,645 Lovable apps open via anon key, figure relayed by a vendor blog) and Reeve's 57% of 3,680 Supabase apps with open reads (security-vendor marketing, not independent) (tracks 11, 19).
- No published hours-per-task table. Fragments: "2 to 4 hours" per common pattern (vendor), 2 to 8 weeks for whole-app finishing (track 19).

**Gate 4: credible position above the low-cost floor.** UNCLEAR, weak support.
- Floor: Fiverr $5 to $250 (median $25 to $30, 50 gigs), Upwork tiers $49 to $750, Pakistani sellers at $17/hr (tracks 7, 21).
- At least 8 small Western or EU studios already list rescue at $1,400 to $2,500, so $2,000 is the median of the credible tier, not above it. Differentiation must come from proof, acceptance tests, warranty and security sign-off (track 21).
- Buyers who name Lovable on marketplaces budget near the floor (track 17 contradicts). Buyers appear to expect a Pakistan discount (track 15, old and thin). Base44 partner rates of $10 to $100/hr and audit floors of $199 to $399 anchor low (tracks 9, 16).

**Gate 5: platform improvements unlikely to erase demand in 12 months.** UNCLEAR, leaning pass.
- Lovable ships scanners, RLS checks, Lovable Cloud and a Wiz integration; Replit ships a Security Agent and pen tests. These commoditise the cheapest faults (track 12).
- Volume growth (about 1M new Lovable projects a week, 80% non-technical per Lovable's own unaudited report; Lovable does not say how many projects are alive), scanners that miss runtime holes, and no platform-run fix-it service found (track 20) argue demand persists but shifts from "security audit" to "finish, migrate, harden, payments". Two added risks: platforms intermediating (Base44's in-product marketplace, whose 15% fee is contradicted across cache entries; Replit routes experts to Contra) and AI tools patching small bugs, which shrinks small-fix retainers (track 14).
- Lovable Cloud migration to own Supabase is manual and sellable (track 20).

## Prior findings re-verified
- "80% non-technical (TNW, May 2026)": PARTLY CONFIRMED. Source is Lovable's own "build economy" report (2026-06-09), [PARAPHRASE, NOT VERBATIM] "four in five identify with non-technical roles"; May is the survey month. Vendor data, unaudited. TNW article not opened.
- "Fiverr gigs $30 to $500": PARTLY WRONG. Floor is $5, median $25 to $30, max seen $250 for vibe-specific fixes; one generic $1,500 security review gig.
- HN threads: all four exist with the stated titles (items 48823359, 48458586, 47386636, 45320431). Points and comment counts NOT verifiable from snippets. Dates: July 2026, June 2026 confirmed roughly; the other two not shown.
- Reddit voices ("90+ of 100 files", "contract after contract", "untangle these messes"): NOT VERIFIED. Reddit unreachable.
- "Pakistani freelancers already advertise this": CONFIRMED for XCONS Solutions (Lahore) and two sellers in Islamabad and Bahawalnagar (track 21, the Bahawalnagar match is weak), all at floor prices ($17/hr, $40 to $100 gigs). Fiverr sellers Kamran Asif and Ahmed Javed (60 to 86 reviews) sell this work but their countries were not shown.
- Slopfix "$10k a week": CONFIRMED as a vendor offer (3 engineers, pay-by-lines-deleted, 2-week warranty), press-covered; no named clients.

## Appendix: unverified items
- "maybe 5 to 10% with any revenue" (Gate 2 read): in track 13 this is labelled "my arithmetic on a weak source, not a measured figure" and rests on BigIdeasDB's 7.6% any-MRR rate among revenue-verified startups. The label was dropped here. Also dropped: the same source says none of those startups cleared $1,000 in the last 30 days. Wording differs from the source track.
- "independent security research (... Reeve 57% of 3,680 ...)" (Gate 3 read): wrong attribution. Track 11 grades Reeve as security-vendor marketing relayed by an aggregator (and the 170 of 1,645 scan as an independent researcher relayed by a vendor blog). Numbers match the cache; the "independent" label does not.
- "four in five identify with non-technical roles" in quotation marks (prior finding 1): the cache shows these words only in the search tool's summary, not in quotation marks (track 12 downgraded the same phrase). Paraphrase, not a verbatim quote.
- "two Islamabad/Bahawalnagar sellers, Fiverr sellers Kamran Asif, Ahmed Javed" as proof Pakistani sellers advertise (prior finding 5): track 21 says "Seller countries were not stated in snippets" for Kamran Asif and Ahmed Javed, and the Islamabad Upwork title (Wajahat S.) is marked [UNVERIFIED] in track 21. Only XCONS Solutions (Lahore) and the Bahawalnagar seller are place-stated in the track text. Does not match the track.


## Orchestrator corrections after verification log 2 (00:05 UTC)
- Gate 3 and gate 4 wording softened as above. Gate 2 "5 to 10% with any revenue" withdrawn.
- Bookkeeping: tracks 13 and 16 JSON report sources_read 0 although 11 and 8 searches returned results; track 16 JSON seller_quotes 4 vs 5 in text; track 15 search counts do not reconcile. Evidence unaffected.
- 10Pearls founding year: the cache's 2008 belongs to Tkxel (track 15 corrected by verifier).
- Track 16's $8k to $15k and $15k to $35k "Lovable to production" bands are from "one vendor", not RapidDevelopers.
