# FINAL REPORT: is "vibe-code rescue" a real, paying market for Wanile?

Written 2026-10-21 (Phase 4 synthesis). Inputs: 22 track files, competitors.md, pricing-map.md, ads-library.md, five model files, verification-log.md.

How to read this report:
- Every claim carries a track pointer such as (T17) or (T21, T22). Key numbers carry a date.
- "Vendor" marks seller or platform marketing. Sellers of rescue work gain from saying demand is huge.
- Quotes are tagged buyer or seller, and verbatim or paraphrase.
- No item tagged [UNVERIFIED] by the verifiers is used in sections 1 or 2. They appear only in section 16.
- Items tagged [PARAPHRASE, NOT VERBATIM] appear only as paraphrases, never in quotation marks.
- Figures tagged [A], [E], [GK] or [V] in the model files are assumptions and are called assumptions here.
- One hard limit shapes everything: no web page was opened in this run. Every fact is search-result text (section 16). "Verified" means "faithfully copied from search output", not "checked on the page" (verification-log.md).

## 1. Verdict: the call, the buyer, the offer, the price, the channel, the expected cost per client, in half a page

**The call: GO WITH CHANGES, at low confidence. It is not a GO on the idea as written (a $2,000-a-week rescue business sold through Meta ads).**

What "GO" means here: spend 30 days and about $3,000 to $3,500 of cash, plus engineer time Wanile already pays for, to sell a $495 paid audit through channels that cost almost nothing, and let the first 10 audits settle the two gates the research could not: buyers who pay $1,500 or more, and a channel under $600 a client. Meta gets a bounded $2,500 test only after two preconditions (section 13). Kill numbers are fixed before day one.

Why not GO: no gate passes cleanly (section 2). No buyer was found paying a human $1,500 or more to rescue an AI-built app (T17 #1, T22 #1, T07 #4). The top confirmed AI-built fix post is $1,200 (Upwork, 2026-10-15, T17 J7). Two $2,000 Upwork budgets exist (2025-10-28 and 2025-12-31, T21 #1), but both are feature-scoped finish or launch jobs seen by title only, and a posted budget is not a payment. Zero Meta advertisers were evidenced in 47 searches (T05, T18). At least 8 studios already list rescue "from" $1,400 to $2,500 (T21 #7, #8, vendor), so $2,000 is the median of the visible tier, not above it.

Why not NO-GO: no gate has failed. The unclear gates are unclear mainly because the sources that would settle them could not be opened: Reddit returned zero pages in about 20 targeted searches (T17), the Meta Ad Library was never opened (T05, T18), and the three Clutch reviews of exactly the right job show no cost band in search text (T22). Calling NO-GO on a blocked network is as unsafe as calling GO on vendor prices. The downside of a test is small: a one-week sprint costs about $350 at salary and about $735 fully loaded (offers.md, loading is an assumption), so the risk is wasted time and ad money, not delivery loss.

The changes, named:
1. Lead with a paid $495 audit credited in full, not a $2,000 sprint (offers.md A; shape seen at 5 vendors, T16 #1, T21 #7).
2. The sprint is a "Hardening Week" at $2,500 list, $1,950 for the first three clients, scoped to the sourced security-and-data checklist with pass/fail acceptance tests. Never sell "finish my app" at $2,000: sellers who finish charge $15,000 to $50,000 over 4 to 8 weeks (T19 #2, vendor).
3. Channel order: existing Wanile clients first, then platform directories and Upwork, then communities. Meta is a $2,500 test, not the plan (channels.md section 4).
4. Do the five manual checks in section 16 in week one. Two of them (Clutch cost bands, Ad Library UK and EU) can turn this into NO-GO before any money moves.
5. Run it as an endorsed sub-brand of Wanile. Show Lahore plainly. No fake address (brand.md).
6. Stop at the kill numbers in section 13. No "one more week".

The buyer: a solo or small-team founder with a live or about-to-launch app on Supabase (often Lovable-built) plus Stripe, who has paying users or an investor or acquirer deadline, and needs the backend finished and made safe: server-side validation, RLS, Stripe live mode and webhooks, auth and roles, deploy. That is the shape of the $2,500 post (2026-10-12, T17 J9), the two $2,000 posts (T21 #1) and the Clutch reviews (T22 R1, R3). Not the buyer: the $20 to $300 "fix my Lovable site" poster (T17 #2).

The offer and price: A. Launch-Readiness Audit, $495, 3 business days, credited in full against B within 14 days. B. Hardening Week, $2,500 fixed (founding price $1,950), acceptance-test guarantee, 30-day warranty, quoted only after an audit. C (two-week Finish-and-Launch, $4,500) and E (Lovable Cloud exit, $1,500 add-on) only when the audit calls for them. Care plan at $450 a month offered at handover, not counted on (offers.md).

The channel and expected cost per client (all LOW confidence; every cheap-channel input is an assumption, every Meta input a vendor benchmark from another niche; channels.md): platform directories $425 a client at Mid ($98 High, $1,250 Low), about 0.6 clients a month; Upwork proposals $470 at Mid ($293 to $1,360), about 0.4 a month; communities and referrals $577 at Mid; Meta $3,666 net of audit margin at Mid ($419 High, $19,806 Low), passing the $600 line only in the High case. Existing Wanile client introductions are unmodelled and probably the cheapest of all.

What would flip the call: the "Project size" field on three Clutch review pages (gate 1), and the Meta test's cost per booked call (at or under $100 for 10 days means continue; over $160 means stop).

## 2. The five GO gates, each marked pass, fail or unclear, with the evidence

| gate | test | read | evidence in one line | what settles it |
|---|---|---|---|---|
| 1 | buyers pay $1,500+ for rescue or finishing | UNCLEAR, leaning not met | 0 payments found; two $2,000 budgets (2025); top AI-built fix post $1,200 (2026-10-15); 3 Clutch reviews, 0 cost bands (T17, T21, T22) | "Project size" on the 3 Clutch reviews; budgets logged on the first 10 fit calls |
| 2 | one channel under $600 a client | UNCLEAR, leaning against for Meta | 0 advertisers in 47 searches; Meta Mid $3,666 net; directories and Upwork pass on paper on assumed inputs (T05, T18, channels.md) | Ad Library UK and EU; own Meta test cost per booked call; 20 counted Upwork proposals |
| 3 | most rescues share one fix list | PARTIAL PASS: security and data list sourced; fix time unproven | secrets and RLS in 5 of 9 seller lists; CVE-2025-48757; 29 of 38 checklist items are engineering judgment (T11, T19) | hours log from the first 3 paid audits |
| 4 | credible position above the floor | UNCLEAR, weak support | floor $5 / $25 / $250 on Fiverr; 8+ studios at $1,400 to $2,500; guarantees and named case studies rare (T07, T21, T08) | share of audited leads accepting $1,950 to $2,500 |
| 5 | platforms won't erase demand in 12 months | UNCLEAR, leaning pass | scanners ship; no in-house fix-it service found; 1M projects a week (vendor); 57% open reads in Aug 2026 (vendor) (T12, T20, T11) | monthly platform watch; scanner overlap logged in audits |

Strict reading: GO needs all five true. None is a clean pass. So GO is off the table. None has failed, so NO-GO has no gate to name. The call in section 1 follows.

### Gate 1: buyers paying $1,500 or more. UNCLEAR, leaning not met.
- Payments found: none, across 22 tracks (T17 #1, T22 #1, T07 #4, T10 §3, T03 #9, T04 §6).
- Posted budgets, buyer-written, not payments: $2,000 "Twilio and Stripe Integration for Lovable App" (2025-10-28) and $2,000 "Full-Stack Base44 & QA Engineer for App and Website Launch" (2025-12-31) (T21 #1). Both over 9 months old, seen by title only, no proposal count or hire status (T21 #2). The verifiers note one is adding Twilio and Stripe to an app whose UI is done and the other is QA plus a WordPress migration: feature-scoped finish jobs, weaker than a pure fix (verification-log.md).
- At or above $1,500 but AI-built not stated: $2,500 for pre-launch hardening of a Supabase and Stripe marketplace by a solo founder (2026-10-12, T17 J9); $1,500 on Freelancer.com split as a $1,000 audit plus $500 stabilisation (T17 J10).
- Top confirmed AI-built fix or finish post: $1,200 (2026-10-15, T17 J7); then $1,000 (2026-04-03, T17 J6).
- Three Clutch reviews describe the right job (a Lovable prototype taken to production, a Bolt prototype rebuilt on Supabase, an audit of two AI-built codebases), but the review's "Project size" field was never shown (T22 R1 to R3). Profile floors of $10,000 or more (GeekyAnts) and $5,000 with 6 of 7 projects under $10,000 (Connectish) are suggestive, not proof (T22 #3, #4).
- Secondhand only: $600 for a 2-day fix and $3,000 to make an MVP shippable, relayed from Reddit by a vendor blog (T10 §3, T20 §3, weak); an HN commenter on a non-technical friend with paying customers: "Now he's hiring a developer to shore it up." (buyer side, secondhand, verbatim, about 2025-07, T17 3B), no figure.
- Seller prices are not proof: Slopfix $10,000 a week with no named client (T08 #5, T17 #11); McKelvey $25,000 to $50,000 (T18 #8); 8 or more studios from $1,400 to $2,500 (T21 #7). All vendor.
- Why unclear rather than fail: Reddit returned zero pages in rounds 2 and 3 (T17, T22) and the Clutch bands are unread. The single piece of evidence that settles it: the "Project size" field on the three Clutch review pages, about 10 minutes with a browser (T22 §6).

### Gate 2: a channel under 30% of first-project value (under about $600 on $2,000). UNCLEAR, leaning against for Meta, leaning pass only for low-volume channels on assumed inputs.
- Meta: 0 advertisers evidenced in 47 searches (14 in T05, 33 in T18). The Ad Library was never opened, so this is weak absence. Every benchmark is vendor data from another niche (T18 §5). The model in section 6 gives a cost per sprint client, net of audit margin, of $419 High / $3,666 Mid / $19,806 Low; only the High case approaches $600. The Mid case needs a first project of about $12,220 to pass (channels.md §1.4), which is why Meta may work for $10,000-plus sellers and not for a $2,000 sprint.
- Cheap channels pass on paper at Mid (directories $425, Upwork $470) but on assumed inquiry and win rates, at about 0.4 to 0.6 clients a month each (channels.md §3). Sourced anchors are thin: Contra's Replit page shows 171 experts and 234 hires (vendor, 2026-10, T20 #1); the most-hired Lovable directory expert is also the cheapest (stale listing, T20 #8); Lovable's own pages conflict on whether the Expert track still exists (T20 #7); Base44's 15% fee is contradicted in its own docs (T09 #6); only 6 Lovable or Base44 posts at $1,000 or more were visible in a partial year (T21 #1).
- Settling evidence: the Ad Library for UK and EU, where any ad type is covered for the past year (T05 #6); then our own test's cost per booked call (section 13).

### Gate 3: repeatable work. PARTIAL PASS for the security and data-access hardening list; UNPROVEN for fix time and for the whole-rescue list.
- Sourced and repeated: the RLS and anon-key pattern has a CVE (published 2025-05-30, disputed by Lovable, NVD, T11 #1), platform docs behind it (T11 #3, #14), a 170-of-1,645 showcase scan (2025, researcher via a vendor blog, T11 #2) and 2026 vendor scans at 57% and 98% (T11 #4). Nine seller lists agree on the core: secrets 5 of 9, access control 5 of 9, payments 3, error handling 3, tests or CI 2, fake auth 2 (T19 5b). Marketplace fix lists and the buyer posts J9, J13, J14 and J2 repeat the same items (T07 #6, T21 #12, T17 §7).
- Not sourced: 29 of the 38 draft checklist items in T11 §6b, and 37 of 58 in delivery.md, are engineering judgment. No hours-per-task table exists (T19 #1, T11 #15); only fragments: "take 2-4 hours to fix if you know what you're looking for" for the five commonest patterns (seller, verbatim, T19 §4), about 2 hours for a key exposure and 1 to 2 days per fix (vendor), 2 to 8 weeks for whole apps (vendor, T19 #2). Our own estimate, an assumption: the week-one core is about 46 engineer hours with AI help (25 to 70), so a typical Lovable app with Stripe is two sprint-weeks (delivery.md §3). Rebuild share unknown; two HN freelancers both ended in a rewrite (T19 #5).
- Settling evidence: the hours log on the first 3 paid audits (delivery.md §8: at least 75% of week-one items needed in 2 of 3; actual hours within 1.5x of estimate).

### Gate 4: a credible position above the low-cost floor. UNCLEAR, weak support. The position exists; it is not unique.
- The floor: Fiverr starting prices min $5, median $25 to $30, max $250 for vibe-specific gigs (about 60 gigs over two rounds, 2026-10-20, T07, T21 #9, medians only); Upwork fix posts $20 to $300 (T17 #2) and productized tiers $49 to $750 (T21 #3); Pakistani sellers at $17 an hour and $40 to $100 gigs (T21 #5); Base44 partner rates $10 to $100 an hour, self-declared (T09 #6); audits from $199 to $399 (T16 #6, vendor).
- The tier we would join: 8 or more studios from $1,400 to $2,500, median of 11 "from" prices $2,500 (T21 #7, #8; section 5). Rare in that tier: a public price (about 7 of 29 agency rows, T08 #2), a guarantee (T08 #7), a named case study (T08 #8, T21 §D). That is the opening: price, scope and tests in writing, a warranty, a security sign-off.
- Against: buyers who name Lovable on job boards budget near the floor (T17 §7); advice blogs say clients expect a Pakistan discount (old, weak, T15 #3); one PeoplePerHour buyer wants engineers, not prompt operators (verbatim, T21 §3).
- Settling evidence: whether audited leads accept $1,950 to $2,500 at 30% or better (offers.md §11), and whether prospects drop at "are you in Pakistan?" (brand.md §7).

### Gate 5: platform improvements unlikely to erase demand within 12 months. UNCLEAR, leaning pass.
- Shrink: Lovable's baseline scanners and Wiz integration (2026-05-07, for teams already on Wiz, T12 #11); Lovable Cloud on by default since 2025-09-29 (T20 #3); Replit's Security Agent (2026-04-21) and black-box pen tests (2026-08-17) (T12 #13); clients patching small bugs with AI (HN, paraphrase, T14 #10). Platform claims are vendor.
- Grow: about 1M new Lovable projects a week and 50M total, with no count of live projects (vendor, unaudited, T12 #3); 57% open reads in Aug 2026, 15 months after the CVE (vendor, T11 #4); Replit's black-box scan found an admin dashboard its code scanner missed (T12 #13); Cloud-to-own-Supabase migration is manual (T20 #4); Supabase deprecates anon and service_role keys by end 2026 (T11 #14); no in-house done-for-you rescue service found at Lovable, Replit, Bolt or Base44 (two negative searches, weak, T20 #2).
- Platforms intermediate rather than deliver: Replit routes experts to Contra (T20 #1), Lovable runs a partner directory (T20 #7), Base44 has an in-product marketplace (T09 #6). The risk is lead capture and a fee, not vanishing demand. The cheapest faults (basic RLS, exposed keys) get commoditised first; finishing, payments, data-model repair, migration and a human accountable for production persist.
- Settling evidence: log in each audit what the platform scan already flagged versus what we found (delivery.md §8).

## 3. Demand: who is stuck, what breaks, how urgent, how many, with buyer quotes

Who is stuck. Lovable's own "build economy" report (published 2026-06-09, survey May 2026) says about four in five of its builders identify with non-technical roles (vendor, self-reported, unaudited, paraphrase, T01 #7, T12 #4). Its CEO says 55% have over 11 years of work experience, so "non-technical" means role, not budget (T12 #4, vendor). The other platforms skew differently: Cursor is for people who read code (T02 #7); v0 revenue is over half Teams and Enterprise (T12 #9, Sacra); Base44 exports the frontend only, so its backend stays on the platform (T02 #5).

What breaks (ranked by how often sources repeat it):
1. The fix loop and the credit bill. Lovable's "Try to Fix" loops cost users $15 to $70 or more per loop (vendor guide, T01 #2). A Bolt user on HN: "every time just get into a doom loop where there is a cycle of breakage, each 'fix' resurrecting a previous 'break'" (buyer, verbatim, tezza, about 2025-07, T02 Q1). A Replit user told The Register (2025-09-18): "editing pre-existing apps seems to cost most overall (I spent $1k this week alone)" (buyer, verbatim, T02 Q3).
2. Security and data access. The RLS pattern has a CVE (T11 #1), a 170-of-1,645 scan (2025, T11 #2) and 2026 vendor scans at 57% and 98% (T11 #4). Lovable's own backend had a BOLA flaw from about 3 February to 20 April 2026 that exposed project chats and source (details disputed across sources, T11 #9).
3. Payments. Stripe webhook secret mismatch, payments that do not work in preview, entitlements set from the browser (T01 #5, T02 #8, vendor and docs). One vendor case: a marketplace that double-charged because webhooks were unverified, a $15,000 fix (T19 §5, vendor).
4. Deployment and environments. v0 publish failures on Vercel (T02 #6); apps that work in preview but not when deployed (seller lists, paraphrase, T21 #12); env vars not loading, CORS and redirect mismatches, DNS and SSL (T21 #12).
5. Agent damage. Replit's agent deleted a live production database during a code freeze in July 2025 (independent, T02 #1, T11 #11).
6. Lock-in. Base44 keeps the backend (T02 #5); Lovable Cloud to own Supabase is manual, with a password reset for every user (T20 #4, paraphrase of docs).

How urgent. The triggers that push a builder to pay a human are, in the thin evidence found: a breach or an attacker emailing customers (HN thread, secondhand, T03 #2); paying users arriving ("Now he's hiring a developer to shore it up.", buyer side, secondhand, verbatim, T17 3B); a launch, raise or sale deadline (the $2,500 post, 2026-10-12, T17 J9; the Clutch R1 investor prototype, T22). The platform does not fix app code and Trustpilot reviewers say refunds for glitches are denied (buyer anecdotes, paraphrase, T01 #3). A consultant on HN says clients only bring in help when they need a fix and are in a hurry (seller, paraphrase, T10 #5).

How many. Nobody could count it. Proxies, all weak: about 101,000 current Lovable-fingerprint sites on BuiltWith (snapshot date unknown, T13 #1); 109 jobs on Upwork's vibe-coding page in one snapshot (2026-10, T17 §5); 153 Supabase developer postings in 30 days to 2026-09-14 across boards (vendor blog, T17 §5); over 230 Fiverr results for "vibe code fixer" (news, 2025-09, T10 §5); VibeCodeFixers.com had matched only 30 to 40 projects against 300 to 600 signed-up fixers (2025-09, T10 #4, T19 #11), which says supply outnumbers visible demand by 10x on that marketplace. One Fiverr seller works with "around 15-20 clients regularly" (seller, verbatim, 404 Media via Slashdot, 2025-09-13, T03 S1). BigIdeasDB says 7.6% of revenue-verified startups on vibe-coding subdomains report any MRR and none cleared $1,000 in 30 days (self-published, opt-in sample, T13 #12). The pool is large; the slice with money is small and unmeasured.

Buyer quotes (all search-snippet sourced, page not opened):
- "the AI repeated the same coding errors, forcing me to spend thousands of dollars on credits just to resolve the same persistent issues." (buyer, verbatim, Trustpilot reviewer of Lovable, date unknown, stage and country unknown, T01 §3)
- "I blew through $70 in a night" (buyer, verbatim, Replit user, about 2025-09, T02 Q4)
- "export to github the code with api's backend" (buyer, verbatim, Base44 feedback board, T02 Q5)
- "I understand $1,500 may not cover every fix." (buyer, verbatim, Freelancer.com poster with a React, TypeScript and Supabase app, budget $1,500 as $1,000 audit plus $500 stabilisation, T17 3B)
- A non-technical founder on Indie Hackers gave up after about 20 breaks and is looking for a developer to finish the MVP with little or no budget (buyer, paraphrase, T02 #9, T22 #13).

Prior findings from the brief, re-checked: the 80% figure is partly confirmed as Lovable's own June 2026 report, not a TNW May 2026 finding (T01 #7, T12 #4); "Fiverr $30 to $500" is partly wrong, the floor is $5 and the median $25 to $30 (T07, T21); all four HN threads exist, their point counts could not be verified (T10 #1); the three Reddit voices could not be found (T10 #7); Pakistani sellers of this exact service are confirmed for XCONS Solutions in Lahore and, weakly, one Bahawalnagar profile (T21 #5).

## 4. Money: who can pay $2,000 or more, what they've already spent, the price points

Who can pay, from the evidence (thin, and all budgets, not payments):

| buyer type | evidence | budget seen | date | grade |
|---|---|---|---|---|
| Solo founder, pre-launch or pre-sale, Supabase plus Stripe, wants server-side validation, Stripe production audit, email migration | Upwork post J9 (AI-built not stated) | $2,500 fixed | 2026-10-12 | moderate, buyer post (T17 #3) |
| Founder with a Lovable UI done, backend features not working (pay-per-minute calls, Stripe Connect payouts) | Upwork post | $2,000 fixed | 2025-10-28 | moderate, buyer post (T21 #1) |
| Founder with a Base44 app needing QA, migration and launch, 2 to 4 weeks | Upwork post | $2,000 fixed | 2025-12-31 | moderate, buyer post (T21 #1) |
| Founder with a React, TypeScript, Supabase app, wants audit then stabilise | Freelancer.com post J10 (AI-built not stated) | $1,500 in two milestones | unknown | moderate, buyer post (T17 #4) |
| Founder with a Lovable prototype, review it and build the rest | Upwork post J7 | $1,200 fixed | 2026-10-15 | moderate (T17 J7) |
| Founder with an investor-ready Lovable or Bolt prototype who hires an agency to productionise it | Clutch reviews R1 (GeekyAnts), R2 (Connectish) | not shown; agency floors $10,000+ and $5,000+ | undated; R2 about Oct 2024 | weak for price (T22) |
| Technical founder wanting an independent audit, no rewrite pitch | Clutch review R3 (Cleveroad) | not shown | unknown | weak for price (T22) |

Who cannot: the "fix my Lovable site" poster at $20 to $300 (J1 to J5, 2025, T17 #2); the live cafe app owner offering a flat $120 a month for on-call RLS fixes (2026-10-14, T17 J11); the Freelancer.com buyer paying $100 per project with 153 bidders averaging $96 (T19 #12); the Indie Hackers founder with little or no budget (T22 #13). Only a minority of Lovable builders earn anything: sources conflict between 35% earning and about 1 in 10 earning directly (vendor, T12 #5).

What they have already spent, mostly on the platform, not on a human: "thousands of dollars on credits" (Trustpilot, T01); about $1,000 in a week on Replit against earlier bills of $180 to $200 a month (The Register, 2025-09-18, T02 #2); $607.70 in extra Replit charges in 3.5 days (a writer, T17 #8); over $1,000 in Bolt tokens on one project (review blog, weak, T02 #3); $5,000 and 2.5 months of AI tools before an agency rebuild (agency post, vendor, T04 #2); about $5,000 in OpenAI credits (one outlet, T19 #11). Freelancer losses are small: $650 lost of $1,000 paid for a website rebuild (G2 review, paraphrase, T04 #1), 25 hours of iOS work with no app (Upwork forum, paraphrase, T04 #1).

Price points, buyer side versus seller side (2025-09 to 2026-10):

| tier | buyer-posted budgets | seller asking prices (vendor) |
|---|---|---|
| floor | $20 to $300 Lovable fixes (T17); $100 per project debug (T19) | Fiverr $5 / $25 / $250 (T21); Upwork tiers $49 to $750 (T21 #3) |
| audit | $150 Base44 security audit (2026-04-08, T21); $1,000 audit step inside J10 (T17) | $49 AfterBuild; $199 Valletta; $297 TechPotions; $399 MobiDev; $497 Base44Devs; $900 Relevant; $1,500 Upwork 72-hour audit credited; EUR 1,500 Soatech; $4,950 TopDevz credited (T16, T19, T20, T21, T22) |
| sprint | $1,000 to $1,250 (2026); $2,000 x2 (2025); $2,500 and $1,500 not stated AI-built (2026) | $1,400 to $2,500 "from" at 8+ studios; $4,000 to $8,000 Upwork 2 to 3 week sprint (T16 #2); Triple Minds from $4,000 (T21) |
| finish or rebuild | none found | $5,000 to $15,000 freelance finish; $8,000 to $25,000 agency "Lovable to production" (one vendor, T16 #8); McKelvey $25,000 to $50,000 (T18 #8); MetaCTO $50,000 to $150,000 (T08, paraphrase) |
| per week | none found | Forasoft $2,500; Slopfix (Odra) $10,000 with 3 engineers (T08 #4, #5) |

Read: the gap between confirmed AI-built buyer budgets ($20 to $1,250) and seller prices is a factor of 3 to 10 (T17 #7). The $2,000 to $2,500 budgets come from buyers whose problem is "finish the backend and launch", which is where the offer should point (T21 §6).

## 5. Supply and competition: the competitor table, the price map, the open position

Competitors.md holds 65 rows (31 in round 1, 34 in round 2), about 40 with a rescue, audit or finish offer. All rows are vendor marketing; no page was opened; prices are "from" prices seen in search text (competitors.md, 2026-10-20 and 2026-10-21). The rows that matter for positioning:

| name | country | price seen (vendor) | unit | guarantee | case studies | ads evidenced |
|---|---|---|---|---|---|---|
| Slopfix (Odra) | not shown | $10,000 a week, paid by lines deleted (T08 #5) | week, 3 engineers | two-week warranty | none named | none found |
| MetaCTO | not shown | free 48-hour audit, then rescue $50,000 to $150,000 (paraphrase, T08) | project, about 30 days | none shown | none shown | none found |
| McKelvey | not shown | $25,000 to $50,000 typical, from $15,000 (T18 #8) | 4 to 8 weeks | none shown | one vendor case study ($40,000 rebuild vs $150,000 quote, T04 #2) | none found |
| TopDevz | not shown | $1,500 to $30,000; $4,950 audit credited (T21 #7) | project | none shown | none | none found |
| Triple Minds | not shown | "From $4K, 2-4 weeks" (T21) | project | none shown | none | none found |
| GainCafe | not shown | from $2,500, 3 to 7 days (T21 #7) | fixed sprint | "100% success guarantee", vague | none | none found |
| Forasoft | not shown | about $2,500 for 1 week (T08 #4, paraphrase) | week | none shown | none | none found |
| AfterBuild Labs | not shown | $49 audit; about $1,500 one integration; $1,999 "Production Pass" 5 to 7 days (T21 #7) | fixed passes | none shown | none | none found |
| Arkroot | Germany / EU | audit EUR 399; rescue from EUR 1,999 (T21 #7) | fixed | none shown | none | none found |
| Base44Devs | not shown | $497 audit; $1,500 bug-fix sprint; migrations $6,000 to $25,000+ (T21 #7) | fixed | none shown | none | none found |
| Teyrex | not shown | from $1,400, report from 3 days (T21 #7, paraphrase) | fixed | none shown | none | none found |
| Vibe Code Rescue | not shown | $299 audit credited to $1,500 sprint (T19 #13) | fixed, about a week | none shown | none | none found |
| Wavect | Austria | not shown | weekly | "cancel any week. Last week refunded if we didn't blow you away." (seller, verbatim, T20 #19) | none | none found |
| Valletta Software | not shown | audit "From $199" (T08) | fixed audit | re-verifies critical findings free (paraphrase, T16) | none | none found |
| Innowise, Chudovo, Softteco, Acropolium, DBB, Redwerk, Pragmatic Coders, Relevant | mostly EU and US mid-size | mostly hidden; Relevant audit from $900; Chudovo free 1 to 3 day assessment then 2 to 4 weeks (T08) | project | none shown | DBB claims a 5.0 Clutch rating only | none found |
| Fiverr sellers (about 60 gigs) | countries not stated | $5 to $250, median $25 to $30 (T07, T21 #9) | gig | none | 86 and 62 reviews for the two best-reviewed (T21 #10) | none |

The price map in one line per tier (section 4 table has the detail): scanners $19 to $39 (T06 #12); Fiverr $5 / $25 / $250; Upwork productized $49 to $750, one top package $3,000 (T21 #3); audits $49 to $4,950; studio sprints $1,400 to $2,500; mid agencies $3,000 to $15,000; premium $10,000 a week to $150,000 a project.

Is the market saturated or open? Crowded at the generic agency level: at least 12 mid-size firms run a dedicated "vibe coding cleanup" page (T08 #1), 7 of 9 search results for "vibe code cleanup service" are agency pages (T06 #11), and the studio tier already has 8 or more sellers at our price (T21 #8). Thin at the proof level: almost nobody shows a price (T08 #2), a guarantee (T08 #7) or a named case study (T08 #8, T21 §D). Pakistani supply exists at the floor; no Pakistani studio shows a $1,500-plus price (T21 §D).

The open position, as far as the evidence goes: a public fixed price in the $2,000 to $2,500 band, a written scope tied to a paid audit, pass/fail acceptance tests, a warranty, a security sign-off the buyer can read, client-owned accounts, and two named case studies. Price alone will not set a Lahore vendor apart from a $2,500 EU studio; proof has to (T21 §6, brand.md §2.3). Framing that matches the only $2,000-plus buyer posts: "finish the backend and launch", not "clean up your code" (T21 §6).

## 6. Meta ads: what the Ad Library shows, the funnel model, and an honest read on the "they close well" claim

What the Ad Library shows: nothing, because it could not be opened (ads-library.md). Across 47 searches in two rounds (T05: 14, T18: 33), zero advertisers were evidenced running Meta, Google, TikTok or LinkedIn ads for rescue. No buyer said "I saw an ad". None of 18 named sellers returned any ad link (ads-library.md round 2). The only heavy Meta advertiser found is Lovable itself: one vendor snapshot counts 1,079 Lovable ads, 304 active (undated, T18 #5), which competes for the same audience. Two structural facts: the Ad Library shows no spend or results for commercial ads, so "60 days and many variants" is only a rough proxy for profit; and the Ad Library API covers UK and EU ads of any type for the past year but not US, Canada or Australia commercial ads (Meta help text, T05 #6).

The funnel model (channels.md §1; every input is a vendor benchmark from another niche [V] or an assumption [A]):

| step | High | Mid | Low | source |
|---|---|---|---|---|
| CPM | $9 | $12 | $15 | vendor range (T18) |
| link CTR | 1.37% | 1.15% | 0.78% | B2B vendor figures (T18) |
| cost per lead | $50 | $145 | $250 | B2B low end; Metadata Facebook; GrowthSpree landing page (T18, vendor) |
| lead to booked call | 60% | 50% | 40% | assumption |
| show rate | 85% | 80% | 75% | vendor (T18) |
| held call to paid audit | 29% | 25% | 20% | B2B close rates, vendor (T18) |
| paid audit to sprint | 50% | 35% | 20% | assumption; no data anywhere (T16 #11) |
| cost per booked call | $83 | $290 | $625 | arithmetic |
| cost per paid audit | $338 | $1,450 | $4,167 | arithmetic |
| cost per sprint client, net of audit margin | $419 | $3,666 | $19,806 | arithmetic |

Only the High case gets near the $600 gate, and only net of audit margin. A direct-purchase page would need at least 0.5% of clicks to buy a $495 audit from an unknown Lahore vendor to hit $600 at a 35% audit-to-sprint rate (channels.md §1.5); untested.

The "agencies spend heavily on Meta ads and close well" claim: unsupported by anything found, and not refuted. No advertiser, no buyer report, no seller saying so (T05 #9, T18 §1). Weak counter-signals: an HN seller says "word of mouth and networking is how I get work and SEO has stopped being a useful avenue for a project pipeline quite a while back" (seller, verbatim, T18 §4); QuickLaunch's "$120k+" 2025 revenue post is said in one summary to rest on referrals, unconfirmed in a second search (T18 #6); RapidDev bets on a 509-page SEO hub (T18 #6). Free audits are the common front door (MetaCTO 48 hours, McKelvey 20 minutes, Agence Scroll, Chudovo, ULAM; T18 #7, T20 #19), which is the shape paid lead-gen would feed, but nothing shows ads feed it. The arithmetic adds one honest possibility: at a $10,000 to $15,000 ticket (Slopfix, McKelvey's lighter rescues, vendor prices) the Mid case can carry $3,000 to $4,000 of acquisition cost, so the rumour may be true for premium sellers and false for a $2,000 sprint (channels.md §5). What would change the read: the Ad Library opened for UK and EU with the full term list; a seller naming a cost per lead or close rate; a buyer who found a vendor through an ad; a Google Ads Transparency check of the named sellers; our own test's cost per booked call.

## 7. Other channels, ranked by expected cost per paying client

From channels.md §4. Basis: a first project of about $2,000. Mid case ranks. Confidence is LOW on every row: the cheap channels rest on assumed inquiry and win rates; Meta and outbound on vendor benchmarks stitched across niches.

| rank | channel | cost per client High / Mid / Low | clients a month (Mid) | time to first client | gate 2 at Mid | sourced anchors |
|---|---|---|---|---|---|---|
| 0 | existing Wanile clients and referrals | not modelled | unknown | days | unknown | none in Phase 1; cheapest to test (channels.md §4) |
| 1 | platform directories: Lovable partner directory, Contra for Replit, Base44 hire-a-partner | $98 / $425 / $1,250 | 0.6 | 4 to 8 weeks | yes on paper | Contra 171 experts, 234 hires, jobs $50 to $75 an hour (vendor, 2026-10, T20 #1); Lovable Expert track free, Pro plan needed, under 5 people, pages conflict on whether it still runs (T09 #2, T20 #7); Base44 15% fee contradicted (T09 #6) |
| 2 | Upwork and job marketplaces | $293 / $470 / $1,360 | 0.36 | 2 to 8 weeks | yes on paper | 6 Lovable or Base44 posts at $1,000+ in a partial year, 2 at $2,000 (T21 #1); Connects cost from outside blogs, unverified (channels.md [X]) |
| 3 | communities and word of mouth | $162 / $577 / $6,928 | 0.9 | 6 to 12 weeks | barely | seller anecdotes only (T10 #3, T18 #6); Reddit unreachable, so unsized; r/lovable about 51k members (third-party, weak, T14 #13) |
| 4 | SEO and content | $102 / $508 steady state / $10,167; year one about $1,200 to $2,000 | 2.0 after month 6 | 4 to 12 months | not in year one | SERP owned by agencies and Fiverr: 7 of 9 for "vibe code cleanup service" (T06 #11), 6 of 9 Fiverr for "fix my lovable app" (verifier count); "rescue" is a poor keyword, it returns animal and emergency apps (T06 #14) |
| 5 | Meta ads (paid audit then sprint) | $419 / $3,666 / $19,806 net | 0.6 per $2,500 | 3 to 6 weeks to first audit | no, High only | section 6 |
| 6 | cold outbound to live apps | $1,149 / $4,724 / $27,778 | 0.4 per 1,000 contacts | 4 to 8 weeks | no | about 101,000 BuiltWith Lovable sites, 3,937 on .ai (T13 #1, #2); reply rates 3 to 6% at best (cold-email vendors, T20 #25); CAN-SPAM has no B2B exemption, up to $53,088 per email (FTC, T20 #21); UK PECR consent for sole traders (ICO, T20 #22); CASL and the Australian Spam Act need role-relevant messages (T20 #23, #24); "I found a vulnerability" outreach reads as a nuisance or extortion (T20 #26) and the brief forbids probing |

Read: four channels pass on paper but are volume-capped at about 0.4 to 2 clients a month combined and rest on unsourced inputs. The two that scale with money, Meta and outbound, fail at Mid by 6x to 8x. The plan therefore runs the cheap channels from week one and uses Meta only as the bounded test in section 13.

## 8. Delivery: the playbook, the checklist, the rescue-or-rebuild rule, scope-creep controls

Source: model/delivery.md, built from T11 §6b (38 items) and T19 §5b (9 seller lists). Hours are Wanile estimates; no hours-per-task table exists anywhere (T19 #1, T11 #15).

The playbook, one engineer plus a reviewing lead (engineer hours 3, 8, 8, 8, 8, 5 = 40; lead 8):
- Day 0, intake: fit call and ethics screen; client-owned access to GitHub, Supabase, Stripe test mode, hosting and domain; a database and storage snapshot before anything changes (the Replit agent deleted a live database in a code freeze, T11 #11); code freeze; contract and written test authorisation.
- Day 1, audit: local build; secret scan, dependency audit, Supabase Security and Performance Advisors; RLS probe with two test users and the anon key on a staging copy only; checklist with severity and hours; triage signals; acceptance-test list and parked list; a 2 to 4 page report. No fix work until the client signs the acceptance list.
- Days 2 to 4, fix: rotate exposed keys and move secrets server-side; staging environment; RLS on every table, user-data and money tables first, migrations in git; server-side route guards and ownership checks (the BOLA pattern from Lovable's own 2026 bug, T11 #9); roles not user-editable; edge functions check JWT, validate input and set CORS; Stripe webhooks with signature verification and idempotency, tested in test mode; an RLS test harness and smoke tests on the signed journeys, run in CI with build, lint and secret scan; domain, HTTPS, email DNS and security headers; CLAUDE.md or AGENTS.md guardrails in the repo (Slopfix hands over the same, vendor, T19 #8); a day-3 hours checkpoint at 1.25x plan.
- Day 5, verify and hand over: the full acceptance list passes on staging; release with rollback in a low-traffic window; runbook; a 15 to 20 minute handover video; a security sign-off list with the plain disclaimer that we find and fix what we find and do not certify the app as secure (T11 §6); parked list; our keys rotated and access removed.

The checklist: 58 items in 11 groups; 21 sourced, 37 judgment. Tiers: W1 week-one core (37 items, about 46 engineer hours with AI help, range 25 to 70); IF only if the feature exists (8 items, about 20 hours, mostly payments and LLM calls); W2 second week (11 items, about 36 hours); X separate quote (Lovable Cloud exit, 12 to 30 hours). AI drafts inventory, scans, policies, types, docs, CI and tests; humans own RLS design, auth, ownership checks, payments and sign-off; no AI agent ever holds production credentials (delivery.md §2). A 40-hour week safely holds about 32 hours of checklist work, so a small clean app fits one week and a typical Lovable app with Stripe is two (delivery.md §0).

The rescue-or-rebuild rule (delivery.md §5; thresholds are judgment [E] except the vendor 60% line [V]). Hours rule from the audit, AI-adjusted mid: 32 or less, one week; 33 to 64, two weeks; 65 to 128, extended rescue with a go or no-go after each week; over 128, rebuild quote. Signals that force a rebuild quote: over 30% of tables, or any core table, cannot take owner-based RLS without a schema change; home-made auth or auth spread across most components; a Base44 backend (export is frontend only, T02 #5); fix cost at 60% or more of rebuild cost (vendor heuristic, T19 #5); deploy failures over 40% plus more than half the files touched. Lovable Cloud is amber and adds the migration job (T20 #4). Live paying users plus a red signal still get a "stabilise first" sprint (RLS lockdown, key rotation, backup) while the rebuild is planned. Take the more severe of the two rules. Published evidence is almost nil: two HN freelancers ended in rewrites; one vendor says rewrites are almost always wrong when the app has users (T19 #5).

Scope-creep controls (delivery.md §6; all judgment, since no practitioner account of a client overwriting a fix mid-engagement was found, T19 #7): a code freeze on the client's Lovable project from day 0 to day 5 with a sandbox copy for new ideas; branch protection so our pull request is the only way into main; a daily drift check for outside commits and dashboard schema changes; written change requests with three outcomes only (swap, add at $500 an engineer-day, park); an 8-hour free absorb limit, never silently past 2x; a numbered acceptance list of 15 to 30 tests signed before day 2; a parked list that becomes the next-sprint menu; a day-3 checkpoint. A client who keeps prompting the AI gets one free rebase, then a change request with the clock paused, then a pause with a re-audit fee or a pro-rata partial delivery.

## 9. Unit economics for each offer shape

Inputs (offers.md §1): engineer $1,050 a month, $6.06 an hour; lead reviewer $2,400 a month, an assumption; loaded multiplier 1.75 on labour, an assumption (channels.md uses 1.5, also assumed; delivery.md prices at salary plus tools and fees); payment fees 3.5%; expected case adds 20% hours and 5% refunds; stress case doubles hours and uses 10% refunds. No overrun, refund or conversion data exists in the evidence (T16 #11, T19 #12), so every margin below is arithmetic on assumptions.

| offer | price | labour (engineer h + lead h) | gross margin: salary-only / loaded / expected / stress | main risk |
|---|---|---|---|---|
| A. Audit | $495 (large app $950) | 16 + 5 | 63% / 35% / 23% / -24% | free competitors; no conversion data; it is a filter, not a profit line |
| B. Hardening Week | $2,500 (founding $1,950) | 40 + 8 | 82% / 71% / 61% / 36% | price above confirmed AI-built budgets; overrun on a bad codebase |
| C. Finish-and-Launch | $4,500 (founding $3,900) | 100 + 16 | 78% / 63% / 52% / 21% | scope creep; 2.25x the $2,000 posts |
| E. Cloud Exit | $1,500 add-on, $2,000 alone | 32 + 6 | 78% / 63% / 51% / 21% | cutover data issues |
| D1. Care | $450 a month | monitoring plus 4 fix hours | 87% / 75% / 66% / 58% | no attach data |
| D2. Support | $1,500 a month | 15-hour pool | 88% / 79% / 71% / 64% | no attach data |
| D3. Dedicated | $3,800 a month | 160 + 4 | 70% / 57% / 45% / 19% | few buyers; no overrun lever |

Why $2,500 and not $2,000 for B (offers.md §4): at $2,000 the 30% acquisition cap is $600 and profit after a capped acquisition is $459; at $2,500 the cap is $750 and the profit $766; $2,500 is the median seller "from" price (T21); and $2,000 would sit in the middle of 8 studios where price does not differentiate. The founding price of $1,950 and a price-down trigger (list drops to $2,000 if more than 60% of audited leads reject on price) cover the gap to the two $2,000 posts.

Break-even and acquisition caps (channels.md §2, placeholder prices): on a $2,000 sprint the gate-2 cap is $600, break-even acquisition is $1,322 and 30% net margin allows $722; so gate 2 is a strict test, not a survival test. Blended view (offers.md §9): 10 audits at an assumed 40% audit-to-sprint rate give revenue $12,970, loaded cost $6,170, gross margin 52%; the 30% rule then caps acquisition at about $390 per paid audit, about $300 at 25% conversion. Capacity (delivery.md §4): two engineers can deliver 8 sprint-weeks a month at full load, plan on 6; fixed cost about $3,200 to $3,400 a month, so break-even is about 2 sprint-weeks a month before acquisition cost. The real cost of a 3x overrun is capacity, about $4,000 of unsold weeks, not cash.

## 10. Retention: the path from rescue to maintenance or a dedicated engineer

Evidence: none on the buyer side. Two rounds found zero buyer voices on keeping a developer after a fix and zero conversion, churn or retainer-length figures (T14 #8, T20 #11). Seller claims only: "many clients choose to keep us as their maintenance team after the launch." (seller, verbatim, Akveo, T14 §4); an Indie Hackers commenter: "the regression problem is your recurring revenue. A one-time audit is a project." (seller, verbatim, T14 §4). Against: an HN commenter says clients now fix small bugs with AI and call a developer only for harder problems (paraphrase, T14 #10). Adjacent benchmarks of 25 to 40% attach and 70 to 85% 90-day retention come from non-code Upwork agency guides (vendor, T20 #13).

Prices (all vendor asking prices unless marked): small-app maintenance $500 to $3,000 a month in Western markets (T14 #1); rescue-shop retainers $500 to $2,000 (scopenine), $1,500 to $3,000 (McKelvey), $2,000 to $6,000 (Frenchy), $4,500 plus GST (one Australian shop), $5,000 to $25,000 with a 3-month minimum (Indianic) (T20 #12); dedicated mid-level React developer in South Asia $3,040 to $4,960 a month (Secondtalent, 2026-09, T14 #5) and $4,000 to $6,400 in Pakistan remote-hiring guides (T20 #15). Buyer side: one live cafe app offers a flat $120 a month for on-call RLS fixes (2026-10-14, T17 J11); a Lovable builder's whole stack costs $91 to $131 a month (third-party, T14 #7), so a $450 plan is 3 to 5 times their tool bill. Maintainers often refuse code they did not write: "limited to projects we have built ONLY" (seller, verbatim, Gumroad care plan, T20 #14), a gap a rescue shop can fill.

The path (offers.md §8): 30-day warranty on every sprint; Care $450 a month offered at handover, only for apps we hardened; Support $1,500 a month (15-hour pool, one request at a time) when the app earns; Dedicated engineer $3,800 a month, 3-month minimum, when the client is funded. Planning assumption, not evidence: 15% of sprint clients take Care for 6 months, worth about $405 revenue per sprint client, 16% of one sprint. Do not build the model on it; measure take-up on the first 8 sprint clients and drop Care as a product if under 10%.

## 11. Risks and contract terms

Source: model/risk.md, a planning draft, not legal advice; items marked [GK] there are general knowledge for a lawyer to check. The biggest fact: no track found a single chargeback, refund fight, lawsuit or fixed-price overrun story in this niche (T19 #6, T16 #11), and Reddit was unreachable, so every dispute rate is an assumption.

Contract shape (risk.md §1): a short audit order, then a master agreement plus a statement of work whose Schedule A is the audit checklist. Scope is Schedule A and nothing else; each item has a found status, severity, planned fix, pass/fail test and a fee share. Fixed price only for one stack, one repo, under about 20 to 30k lines, Supabase plus Stripe (T19 appendix A). Stated exclusions: new features, redesign, "finish the app", platform migration (a separate job), app store submission, load testing, third-party outages, compliance certification, code added after the audit date. Acceptance: 5 business days to test, one free fix round, deemed acceptance on silence or production use; 30-day warranty on in-scope fixes (between Slopfix's two weeks and aibrify's 90 days, T19 #9, T16 #4). Change requests in writing, priced per engineer-day. Client duties: access within 1 business day in the client's own accounts; a backup first (T11 #11); a code freeze on main during the sprint; replies within 2 business days; the client pays platform and API costs.

IP and security wording: the client owns deliverables on full payment and keeps what it already owned; we keep our tooling and licence what sits in the repo; no client code goes into public models or repos. Lovable's product terms, read from snippets only, say the customer owns the apps and AI output (risk.md [WS1]); Lovable disputes the CVE on the ground that each customer accepts responsibility for protecting its data (NVD, T11 #1), so our contract says the same. Never "secure", "hack-proof" or "audit passed"; always "hardened against the listed risks". Secrets found are listed, rotation is the client's duty, unrotated secrets are excluded from liability. Liability capped at fees paid; indirect loss excluded. Incident clause: signs of an existing breach mean we stop, tell the client in writing within 24 hours, preserve evidence, and the client decides on notifications.

Refunds and payments (risk.md §1.10, §1.11): the audit is paid upfront, not refundable once delivered, credited in full within 14 days; the sprint refund is itemised, the fee share of any item still failing its test after one fix round; a full refund of unused work if the rescue-or-rebuild call proves wrong in the first 2 days; no refund for change requests, client edits, platform failure or a change of mind. Avoid Wavect's subjective last-week refund at this ticket. Card for the audit and for sprint invoices up to about $2,500 after a signed SOW; bank or Wise above that; an evidence pack per client. Data: work on staging with seeded data; a DPA where real data is unavoidable; cross-border terms for EU, UK, Australian and Canadian clients need a lawyer; never health, children's or card data.

Ethics screen (risk.md §4): decline gambling and betting, interest-based lending, adult content, alcohol-centric businesses, tobacco and vaping; flag crypto, dating and user-generated content, cannabis, political and surveillance tools for a director decision; check at intake and again at audit; a no-fault pro-rata exit clause.

Top register items (likelihood and impact are the author's judgment): buyer budgets too small for $2,000 work (high, high; T17, T21); "fix" heard as "finish" (high, high; T19 #2); AI tools shrinking the gap and pressing price (high, medium; T12, T21 #13); retainer conversion lower than hoped (high, medium; T14, T20); refunds after invisible hardening work (medium, medium); a live break caused by us (medium, high); a missed vulnerability later exploited (medium, high); the Lahore trust gap (medium, medium; T15, T20); platform directories capturing leads (medium, medium; T20 #1, #7).

## 12. Brand decision and positioning

Decision (brand.md §1): an endorsed sub-brand with its own name, domain and page, and Wanile named openly in the footer, about page, contract and invoice. Confidence moderate-low; no track tested brand effect. For: the rescue buyer shops at Upwork and Fiverr prices while Wanile's main brand moves upmarket (BRIEF Q10), and a $2,000 sprint beside $25 gigs would pull Wanile's name toward the floor (T21 #9); Lovable's Expert track is for teams under 5 people, which a small named team can fit (T09 #2); a sub-brand folds back with a redirect or is cut off after a dispute. Against full separation: hiding Wanile hides the best proof (named case studies, 20 engineers, the paid audit-plus-fix record, BRIEF §1), and Clutch, Upwork, Stripe and the directories show the company anyway. Contract party: Wanile Technologies, brand as trading name; a ring-fenced entity is a lawyer question after the first 10 sprints.

Lahore: show it plainly, not as the headline, never with a fake Western address. The distrust evidence is old and thin (a 2024 job post barring Pakistani applicants, T15 #1; one relayed comment about two Pakistani vendors, about 2024, T20 #17), the discount expectation is real but small (T15 #3), and the big Pakistani firms show Pakistan while leading with real US offices (T15 #8). Proof beats location in every source that speaks to it: references and a reference call, a small paid first step, client-owned accounts, verifiable reviews (T15 #4, T20 #18). Build before launch: two named Wanile case studies with permission, a reference-call offer, a redacted sample audit report.

Positioning (brand.md §2.4): against the floor, "a $30 gig fixes one bug; we prove the whole app is safe to launch"; against the studio tier, "same price band, with the scope, tests and warranty in writing"; against premium, "for small apps under about 20 to 30k lines; bigger codebases get told so". Use the words people search ("fix", "finish", "audit", "Lovable", "Supabase", "Stripe"), not "rescue" alone (T06 #14). Name candidates to clear with a trademark search: Last30, Plumbline, GoLive Desk, Steadyship, Shipcheck. Reverse the decision if more than half of audit buyers ask "is this Wanile?" or the sub-brand cannot get its first 3 reviews without the Wanile name (brand.md §7).

## 13. The first 30-day test plan: offer, channel, a Meta budget of about $2,500, daily metrics, and kill criteria (for example: stop if there are no paid audits after a set spend)

Purpose: not a launch. A 30-day test that produces the two numbers the research could not: what audited buyers will pay, and what a booked call costs. Built from offers.md §10 to §11 and channels.md §6.

The offer to lead with: A, the $495 Launch-Readiness Audit, credited in full against B within 14 days. B, the $2,500 Hardening Week ($1,950 for the first three clients who allow a named case study), is quoted only after an audit. C, E and R only when an audit calls for them. Fit-call screen: live app or launch date, users or revenue, budget band; anyone under $1,000 gets a free checklist and a polite no.

Channel order and calendar:
- Days 1 to 5: freeze the audit template, Schedule A with tests, the contract (get a lawyer's review quote), the fit-call script and a one-page site under a working sub-brand name; run the audit on a Wanile demo app and time it (confirm 16 engineer hours or learn the real number); do the five manual checks in section 16; email existing Wanile clients for introductions; apply to the Lovable partner directory, Contra for Replit and Base44 hire-a-partner; open a rescue-specialised Upwork profile under the Wanile agency account.
- Days 3 to 30: sell the audit. Target 10 paid audits at $495. Send 20 counted Upwork proposals to posts at $1,000 or more (only 6 were visible in a partial year, T21 #1, so expect few). Answer, do not pitch, in reachable communities. Log for every lead: platform, live or not, users or revenue, budget band, and the answer to "what would you pay for the fix?". That log is the gate 1 evidence.
- Days 10 to 30: quote B at $2,500 to the first 5 audited leads; log every objection and counter-offer. Days 15 to 40: deliver the first two sprints with an hours log per Schedule A item. Care at $450 is offered at every handover and take-up logged.
- Day 30: decision meeting against the kill numbers below.

The Meta test, $2,500 (channels.md §6). Two preconditions before the first dollar: (1) the Ad Library check for UK and EU is done and written down; (2) the page and booking flow have already carried at least three fit calls from any channel, so a zero result cannot be blamed on a broken page. Set-up: US only; one campaign, two ad sets (the fix-loop angle and the pre-launch safety angle from brand.md §5), four variants; the page books a call with three qualifying questions; the offer is the $495 audit, credited. Spend: $100 a day for days 1 to 5 ($500), then $133 a day for days 6 to 20 ($2,000); measure sprint conversions for 15 more days after spend stops. Expected from $2,500 in the High / Mid / Low cases (vendor-benchmark arithmetic, channels.md §6.3): leads 50 / 17 / 10, booked calls 30 / 8.6 / 4, paid audits 7.4 / 1.7 / 0.6, sprint clients 3.7 / 0.6 / 0.1; chance of zero paid audits 0.1% / 18% / 55%. Honest limit: $2,500 cannot prove a cost per sprint client; it can measure cost per lead and per booked call to about plus or minus 30%, and show whether any held call buys an audit.

Daily metrics (green / amber / red): spend, impressions and CPM (amber above $20); link CTR (swap the ad below 0.5%); CPC (swap above $3); landing-page views and bounce (150 clicks and zero leads means fix the page or the tracking); leads and cost per lead (green at or under $60, amber to $110, red above $110); booked calls and cost per booked call, the main metric (green at or under $100, amber $100 to $160, red above $160); lead quality, counted as qualified only if live, with users or revenue, and a budget at or above $1,500; show rate (tighten reminders below 60%); paid audits and cost per paid audit, logged by hand; frequency (widen the audience above 2.5 in week one). Why $100 and $160: show times close times audit-to-sprint from a booked call is 0.123 in the High case and 0.070 in Mid, so a $600 sprint client needs a booked call at or under $74 (High) or $42 (Mid), and merely breaking even on the sprint's gross profit needs $163 (High) or $93 (Mid) (channels.md §6.2).

Kill and continue rules, written into the ad account before day one:
- K1: by day 3 (about $300), CTR under 0.5% or CPC over $3: pause that ad, not the test.
- K2: cost per booked call over $160 across 10 days (about $1,170 spent): stop Meta.
- K3: 8 or more leads and none qualified: stop Meta, wrong audience.
- K4: fewer than 3 leads at $1,000 spent: stop Meta.
- K5: no paid audit after $1,500 and at least 6 held calls: stop spending and rework the offer, not the ads.
- K6: zero paid audits at $2,500: Meta fails as modelled (this rules out the High case, not the Mid case).
- C1: cost per booked call at or under $100 for 10 days and at least 2 paid audits by day 20: run a second $2,500 at the same settings.
- C2: booked call between $100 and $160: finish the 20 days, no extra spend, decide at day 35 on audit-to-sprint.
- Offer kills (offers.md §11): fewer than 3 paid audits from 30 qualified fit calls at any price between $295 and $495 means the buyer pool does not pay, gate 1 fails, NO-GO. The first 10 qualified leads all at $1,250 or less with none moving up after the audit means the market in front of us is the Fiverr and Upwork floor, gates 1 and 4 fail. More than 60% of audited leads rejecting the sprint on price: list drops to $2,000. Buyers consistently countering below $1,500: kill B. Average sprint hours above 60, or a third of audits ending in "rebuild": reshape the sprint before selling more.
- Channel kills (assumptions): zero qualified directory inquiries in 6 weeks, or fewer than 1 reply per 20 Upwork proposals, means that channel is dead for a new listing; drop it.
- Guarantee kill: refund cost over 10% of revenue, or one lost chargeback: pause card payments above $1,000.

Cash budget for the 30 days: Meta $2,500; directory set-up about $450 (Lovable Pro plan, demo projects); Upwork Connects about $30 to $50 (from outside blogs, verify in the account); a lawyer's first review (quote first). About $3,000 to $3,500 plus engineer time.

## 14. Buyer language: 20 exact phrases with sources

Rule: a phrase is "verbatim" only when it sat inside quotation marks in the cached search output and passed verification. Job-post titles are buyer-written and verbatim. Seller phrases are included only where they mirror a buyer pain and are labelled. No phrase was checked on the live page. Never run any of these as a testimonial.

1. "the AI repeated the same coding errors, forcing me to spend thousands of dollars on credits just to resolve the same persistent issues." Buyer, verbatim. Trustpilot reviewer of Lovable, date and stage unknown (T01 §3).
2. "every time just get into a doom loop where there is a cycle of breakage, each 'fix' resurrecting a previous 'break'" Buyer, verbatim. tezza, Bolt user, HN item 44511770, about 2025-07 (T02 Q1).
3. "don't try to fix mistakes, revert and try with an updated prompt." Buyer, verbatim. janpot, Bolt user, likely technical, HN 44511770, about 2025-07 (T02 Q2).
4. "editing pre-existing apps seems to cost most overall (I spent $1k this week alone)" Buyer, verbatim excerpt of a longer verified quote. Replit user to The Register, 2025-09-18 (T02 Q3).
5. "I blew through $70 in a night" Buyer, verbatim. Replit user, about 2025-09, outlet inferred (T02 Q4).
6. "export to github the code with api's backend" Buyer, verbatim. Base44 feedback-board user via a review site, 2026 (T02 Q5).
7. "I understand $1,500 may not cover every fix." Buyer, verbatim. Freelancer.com poster with a React, TypeScript and Supabase app, budget $1,500, date unknown (T17 3B).
8. "Now he's hiring a developer to shore it up." Buyer side, secondhand, verbatim. HN commenter about a non-technical friend with paying customers, item 44739556, about 2025-07 (T17 3B).
9. "We need somebody that built a clone of one of these two platforms or something similar, not somebody that is using these platforms to vibe code." Buyer, verbatim. PeoplePerHour poster, date unknown, link approximate (T21 §3).
10. "Take over and stabilize the product development after a previous unsuccessful vendor experience" Buyer, verbatim. Clutch reviewer of Empat; a failed-vendor rescue, AI-built not stated (T22 3B).
11. "with specific numbers and specific files" Buyer, verbatim fragment. Clutch reviewer of Cleveroad on an audit of two AI-built codebases; the tool warned the wider excerpt was garbled (T22 R3).
12. "Twilio and Stripe Integration for Lovable App" Buyer, verbatim job title. Upwork, $2,000 fixed, 2025-10-28 (T21 §3).
13. "Senior Backend Engineer — Marketplace Launch (Supabase / Stripe / Checkr)" Buyer, verbatim job title. Upwork, $2,500 fixed, solo founder, 2026-10-12 (T17 J9).
14. "Refine and Deploy Lovable App with Supabase" Buyer, verbatim job title. Upwork, $1,000 fixed, 2026-04-03 (T07 §3, T17 J6).
15. "Fix Vibe Coded App" Buyer, verbatim job title. Upwork, $100 fixed, contract to hire, 2025-09-01 (T17 J5).
16. "Security & Stability Audit (Base44 / AI-Built)" Buyer, verbatim job title. Upwork, $150 fixed, 2026-04-08 (T21 §3).
17. "On-call Supabase developer, flat $120/month, live café loyalty app (Edge Functions, RLS)" Buyer, verbatim job title. Upwork, 2026-10-14 (T17 J11).
18. "clicking 'Try to Fix' creates new bugs that trigger more errors, each consuming credits." Seller, verbatim. Vendor guide (VP0 or RapidDevelopers), date unknown; mirrors the buyer loop in items 1 and 2 (T01 §4).
19. "a live database was readable by anyone with devtools" Seller, verbatim. Fiverr seller describing a client app with RLS never enabled, 2026-10 (T21 §4).
20. "I've been getting more requests than ever to debug AI-generated codebases where the original "developer" can't explain what any of it does." Seller, verbatim. HN commenter, thread and date not confirmed (T19 §4).

Not counted, paraphrase only: an app that works in preview but fails when deployed (seller lists, T21 #12); a founder who needed about 300 Lovable messages instead of the 100 expected (buyer, r/lovable via a mirror, T03 B2); an Indie Hackers founder who gave up after about 20 breaks with little or no budget (buyer, T22 #13).

## 15. Threads, ads and sources read, with links, dates and counts

Counts (approximate where marked; all from search-result text; no page opened):

| item | count | note |
|---|---|---|
| track files | 22 (16 round 1, 5 round 2, 1 round 3) | tracks/ |
| searches run | about 460 (STATUS.md; the phase 1 summary's own tally is about 420) | round 1 tracks got 7 to 20 each under the 200-call quota; rounds 2 and 3 got 33 to 45 each |
| pages opened | 0 | WebFetch and curl blocked for every public host |
| verification | about 2,980 items checked, about 2,813 passed, 34 failed, 53 downgraded to paraphrase, about 246 labelled assumptions | verification-log.md |
| buyer voices | about 60: about 41 buyer-written job posts (about 31 Upwork, 8 Freelancer.com, 2 PeoplePerHour), 12 reviewers or commenters with quoted words (9 fragments plus 3 Clutch reviews), about 10 paraphrased | 0 say they paid a human $1,500 or more |
| buyer posts at $1,000 or more | 9: two at $2,000 (2025), $2,500 and $1,500 not stated AI-built (2026), $1,200, $1,250, $1,000 x2, and an $18,000 product build excluded as not rescue | T17, T21, T22 |
| seller voices | 65 competitor rows (55 agencies or productized sellers, 10 marketplace sellers); about 60 Fiverr gigs with a starting price; about 15 Upwork productized listings and profiles; about 12 vendor guide publishers; about 8 HN and Indie Hackers seller commenters | competitors.md, pricing-map.md |
| advertisers evidenced | 0 in 47 searches (14 plus 33) | ads-library.md |
| HN threads confirmed to exist | 48823359, 48458586, 47386636, 45320431 (the brief's four, points unverified); 44511770, 44739556, 47599303, 44832986, 45235458 (95 points), 50151036 (391 points, 538 comments) | T10, T02, T03, T17, T19 |
| Reddit threads read | 0 | domain filter returns error 400; mirrors returned nothing in rounds 2 and 3 |
| security data points | CVE-2025-48757 (NVD, 2025-05-30); 170 of 1,645 (2025); Reeve 57% of 3,680 (2026-08, vendor); Symbiotic 1,046 of 1,072 (2026-04, vendor); UpGuard 16,326 Supabase databases (TechCrunch 2026-09-25); arXiv 2606.23130 (2026, unopened) | T11, T20 |

Key links (all read as search results only):
- HN: news.ycombinator.com/item?id=48823359 (Slopfix, about 2026-07); =48458586 (about 2026-06); =47386636 (100-hour gap); =45320431 (cleanup as a service); =44511770 (about 2025-07); =44739556 (about 2025-07).
- Upwork buyer posts: upwork.com/freelance-jobs/apply/Twilio-and-Stripe-Integration-for-Lovable-App_~021983230450209748146/ (2025-10-28); .../Full-Stack-Base44-Engineer-for-App-and-Website-Launch_~022006253167123187840/ (2025-12-31); .../Senior-Backend-Engineer-Marketplace-Launch-Supabase-Stripe-Checkr_~022109480430597569648/ (2026-10-12); .../Refine-and-Deploy-Lovable-App-with-Supabase_~022040075709636871527/ (2026-04-03); .../Senior-Full-Stack-Developer-Build-Powered-SaaS-Web-Platform-MVP-Next-React-Node-Supabase_~022110751046086488779/ (2026-10-15); .../call-Supabase-developer-flat-120-month-live-caf-loyalty-app-Edge-Functions-RLS_~022110520330326581289/ (2026-10-14).
- Clutch reviews: clutch.co/profile/geekyants ; clutch.co/profile/connectish ; clutch.co/profile/cleveroad (T22).
- Security: nvd.nist.gov/vuln/detail/CVE-2025-48757 ; superblocks.com/blog/lovable-vulnerabilities ; techcrunch.com/2026/09/25/some-supabase-customers-are-publicly-exposing-reams-of-peoples-data-to-the-web/ ; vibe-eval.com/updates/vibe-coding-security-monthly-aug-2026/ ; symbioticsec.ai/blog/we-scanned-1-072-vibe-coded-apps-98-had-security-flaws.
- Platforms: lovable.dev/blog/a-first-look-at-the-build-economy (2026-06-09); techcrunch.com/2026/06/09/lovable-says-it-has-hit-500m-in-annualized-revenue-with-1-million-new-projects-a-week/ ; lovable.dev/partners/experts ; lovable.dev/experts ; contra.com/replit/jobs ; base44.com/hire-a-partner ; docs.lovable.dev/tips-tricks/self-hosting ; supabase.com/docs/guides/database/postgres/row-level-security.
- Sellers and practitioners: tomshardware.com (Slopfix, 2026-07); indiehackers.com/post/how-quicklaunch-made-120k-fixing-vibe-coded-apps-in-2025-y05kJ7G9VG4wdJplBIb8 ; developers.slashdot.org/story/25/09/13/054206/the-software-engineers-paid-to-fix-vibe-coded-messes ; justinmckelvey.com/vibe-code-rescue ; wavect.io/services/vibe-coding-rescue/ ; gaincafe.com/hire-lovable-expert ; teyrex.com/fix-vibe-coded-app ; arkroot.com/ai-codebase-rescue/ ; xconssolutions.pk/blog/vibe-coding-expert-in-lahore/.
- Channels and law: trends.builtwith.com/websitelist/Lovable ; wordstream.com/blog/facebook-ads-benchmarks-2025 ; ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business ; crtc.gc.ca/eng/com500/guide.htm ; ico.org.uk (PECR guidance on direct marketing by email).

## 16. Caveats and gaps

The network constraint. WebFetch was blocked for every public host (DNS failure on 18 of 18 probes; reddit.com refused by policy) and shell curl was blocked too (STATUS.md, NETWORK-NOTES.md). Only WebSearch worked, under a shared quota of 200 calls per turn across all agents; round 1 tracks got 7 to 20 searches each against plans of 35 to 45, and 13 of 16 reported PARTIAL. The reddit.com domain filter returned error 400, and in rounds 2 and 3 about 20 Reddit-targeted queries returned zero Reddit or mirror pages (T17). So "verified" means faithfully copied from search output, never checked on the page (verification-log.md). Quotes are snippet-sourced; usernames, dates and upvotes are mostly unknown; counts are "from search results, partial".

What could not be checked at all: Reddit threads; HN comment trees and point counts; the Meta Ad Library, Google Ads Transparency Center, Google Trends, autocomplete and People also ask; Fiverr and Upwork pages (review counts, seller countries, proposal counts, hire status); the Clutch review fields "Project size" and "Project length"; vendor pricing pages (every price is a snippet); the TNW article behind the 80% claim; Lovable's live terms and the current state of its Expert track; Supabase, Stripe and Vercel partner fees; any audit-to-project conversion rate, refund rate, overrun rate, rescue-to-rebuild share or retainer attach rate (none exists in the evidence); practitioner hours per fix; whether Wanile can staff a UK or US overlap window; Wanile's own Clutch and Upwork record. The prior findings in the brief were re-checked in section 3; the HN point counts (304, 501, 262, 250) and the three Reddit voices remain unverified.

Items tagged [UNVERIFIED] by the verifiers and kept out of sections 1 and 2: the round-2 Fiverr means ($51.2 and $40.8) and the "30 priced" and "50 gigs" counts (the medians stand); several process counts of searches run; "11 of 18" AI-built posts (supported count 10); an Indie Hackers post title about a token bill; a "5 of 9" Fiverr SERP count (the cache shows 6 of 9); one Fiverr gig URL slug and one gig title; the "hire a verified expert" label for the Lovable directory; "30,998 apps scanned" for Reeve; a certificate-transparency URL; 10Pearls "founded 2008"; a 2017 date on an HN thread; $8,000 to $35,000 "Lovable to production" bands attributed to RapidDevelopers (the figures exist as "one vendor"); the phase 1 summary's "5 to 10% with any revenue" (the source says 7.6%) and its "independent" label on Reeve (it is vendor); Fiverr sellers Kamran Asif and Ahmed Javed used as proof of Pakistani supply (their countries were not shown) and the spelling of an Islamabad Upwork title; GeekyAnts "Bengaluru" and Connectish staff size; two Clutch URLs; a $14.19 CPM attribution; dates on the Cryptosaurus post and one HN seller quote; a model/offers pointer for the $297 TechPotions price (the figure is in T20). The name Slopfix covers two vendors, Odra at $10,000 a week and slopfix.ptolemay.com at $30 to $100 per fix; this report never merges them.

The five fastest manual checks that would most change the verdict (need a browser or open network):
1. Open the three Clutch review pages (clutch.co/profile/geekyants, /connectish, /cleveroad) and read "Project size" and "Project length" on the Lovable, Bolt and AI-audit reviews. About 10 minutes. Three bands at $10,000 or more moves gate 1 toward pass for the agency-buyer segment; bands under $5,000 or stale dates move it toward fail (T22 §6).
2. Open the Meta Ad Library for UK and EU (any ad type, past year) with the full term list (lovable, vibe coded, vibe coding, fix your app, AI built app, bolt.new, replit app, MVP rescue, finish your app, app stuck, lovable developer, launch your app, security audit), filter out the platforms' own ads, and check the Google Ads Transparency Center for the 18 named sellers. Zero rescue advertisers is a real negative for the "they close well" claim; three or more sellers with an ad running 60 days or more and 5 or more variants is a moderate positive (ads-library.md, channels.md §5).
3. Read r/lovable thread 1kvcmfg ("How much to hire a dev"), search r/lovable and r/vibecoding for "hire a developer", "paid a developer" and "quoted me" over the last 90 days, and find the r/vibecoding posts behind the "$600 for a 2-day fix" and "$3,000" anecdotes (T10 §3, T20 §3). Any first-person "I paid $X" at $1,500 or more changes gate 1; a run of $200 to $600 figures confirms the floor.
4. Open the two $2,000 Upwork posts and the $2,500 post in an Upwork account and read proposal counts, hire status, client spend history and payment-verified status; search Upwork directly for "Lovable" fixed-price jobs at $1,500 or more in the last 90 days. This sizes the only channel with buyer-written budgets (T21 #1, channels.md §3.4).
5. Open lovable.dev/partners/experts, lovable.dev/experts and lovable.dev/work-with-a-partner to settle whether the Expert track still exists, its team-size rule and expert count, and whether a Wanile-run small brand may apply; open contra.com/replit/jobs and base44.com/hire-a-partner for live hire counts and the Base44 fee. This settles whether the cheapest modelled channel is real (T20 #7, #8, T09 #6).

Also worth doing before any spend: ask three existing Wanile clients for introductions (the cheapest channel of all, unmodelled); open the QuickLaunch Indie Hackers post and the four HN threads in full for prices, channels and client counts; confirm Fiverr seller countries and review counts for the two best-reviewed rescue sellers and Hamid Siddiqi's gig price; get a lawyer's review quote on the three clauses in risk.md §7; confirm with Wanile's finance lead how card payments and chargebacks work for the company today.

## 17. Red team and final call

Written by the orchestrator after reading red-team.md in full and the synthesis above. The red team did not see the synthesis.

### Where the two agree
Both read the same verified files and reach the same facts: no buyer was found paying a human $1,500 or more to rescue an AI-built app; the two $2,000 Upwork budgets are old, feature-scoped and seen by title only; zero Meta advertisers were evidenced; the Meta mid case is about six times over the $600 line; $2,000 sits at the median of the studio tier; the only sourced repeatable work is the security and data-access core; fix times are unproven. They differ on the label. The synthesis says GO WITH CHANGES because no gate was shown to fail. The red team says NO-GO because no gate was shown to pass, and GO needs all five.

### Answers to the five red-team points

**1. Name one buyer who paid $1,500 or more for an AI-built app in the last 12 months.** None exists in the cache. We do not claim gate 1 passes. The honest state is "not met on available evidence", with the two strongest settling sources (Reddit threads, Clutch cost bands) never opened. The red team is right that a posted budget is not a payment. It is also right that the J9 $2,500 post (2026-10-12) is not stated as AI-built. That cuts both ways: it means the buyer with money is a "launch-hardening on Supabase and Stripe" buyer, whether or not the app was vibe-coded. The offer should follow that buyer, not the "vibe-code rescue" label. Point accepted; the call is narrowed, see below.

**2. Show one channel under $600 on a sourced input.** We cannot. Every cheap-channel figure rests on assumed inquiry and win rates, and the only sourced Meta inputs come from other niches. The consequence is not "spend $2,500 on Meta to find out". The consequence is "spend $0 on ads until a sourced input exists". So the Meta test is removed from the 30-day plan. It moves to a conditional month two, only if (a) a browser check of the Meta Ad Library for the UK and EU, where all ad types are covered, shows at least one advertiser running this offer for 60 days or more, and (b) the probe has already closed three paid audits through free channels. Point accepted.

**3. Reconcile the $2,000 week with 46 to 66 hours, and say why it wins against EU studios and Pakistani sellers.** The $2,000-a-week unit is dropped. Pricing is sized from the audit: a Hardening Week at $2,500 holds about 32 hours of checklist work; a typical Lovable app with Stripe is about 66 hours, so it is a two-week engagement at $4,500 to $5,000. These are our estimates, not published data. Against EU studios at EUR 1,999 to $2,500 we are not cheaper and should not pretend to be; the only visible gap in that tier is a public price, written acceptance tests, a warranty and named case studies, which almost no seller shows. Against Pakistani sellers at $17 an hour we do not compete at all; that is a different buyer. If audited leads will not pay $1,950 or more, the probe fails gate 4 by day 30 and stops. Point accepted; the test now measures this directly.

**4. Show that ten rescue clients out-earn one dedicated-engineer or AI-operations sale on the same contacts.** We cannot, and the arithmetic favours the red team: one $3,800-a-month dedicated engineer placement equals roughly 23 sprint sales a year in gross profit. So the probe must not spend AI-operations introductions. Rules: no existing Wanile client who is an AI-operations prospect is approached with this offer; the probe sources from Upwork proposals, platform directories, inbound and Wanile's existing Clutch and Upwork history; founder time is capped at four hours a week; one engineer at half load plus the lead. The real prize is the dedicated-engineer upsell at the end of a rescue, and the probe logs whether anyone takes it. Point accepted.

**5. What repeatable, defensible work survives the gate 3 and gate 5 collision by October 2027, and who pays for it?** Not scanning. Scanners from Lovable and Replit will own basic RLS and exposed keys within the year. What survives is finishing payments in live mode, repairing data models, migrating off Lovable Cloud to a client-owned Supabase (manual today), and a human accountable for production before a launch, an investor or an acquirer. In the cache the people who posted money for exactly that are J9 at $2,500 (2026-10-12), J10 at $1,500, the two $2,000 posts (2025), and the Clutch clients of GeekyAnts and Connectish (cost bands unread, profile floors $5,000 to $10,000). That is thin, and we say so. It is also why the offer is reframed from "we fix vibe-coded apps" to "launch hardening for Supabase and Stripe apps", which does not depend on AI-built apps staying broken. Point partly accepted; it changes the positioning.

### Final call

**GO WITH CHANGES, narrowed further by the red team. NO-GO on the idea as originally written: a $2,000-a-week vibe-code rescue sold through Meta ads under a new brand.**

The red team changed the call in substance, not in label. The changes, final:

1. **Offer.** A $495 Launch-Readiness Audit, credited in full, then a Hardening Week at $2,500 list ($1,950 for the first three, in return for a named case study) sized from the audit, with written acceptance tests, an itemised refund if an in-scope test fails after one fix round, and a 30-day warranty. Two-week engagements at $4,500 to $5,000 when the audit says so. Never "finish my app" at $2,000. Rebuilds quoted separately. Positioning: launch hardening for Supabase and Stripe apps, AI-built or not.
2. **Brand.** No new brand and no landing-page build in the probe. Sell under the Wanile name with Lahore shown plainly. Decide on the endorsed sub-brand only after three paid engagements.
3. **Channels and cash.** Zero ad spend for 30 days. Twenty counted Upwork proposals to posts at $1,000 or more, applications to the Lovable partner directory, Contra (Replit) and Base44 marketplace where a 20-person firm is eligible, inbound from Wanile's Clutch and Upwork history, and communities. Cash budget about $500 (directory fees, Upwork Connects, tooling). Meta only in month two under the two conditions in point 2 above, capped at $2,500.
4. **Week-one manual checks, before anything else.** Open the three Clutch review pages (GeekyAnts, Cleveroad, Connectish) and read "Project size". Open the Meta Ad Library for the UK and EU with the full term list in ads-library.md. Read r/lovable thread 1kvcmfg and the two $2,000 Upwork posts for hire status. If the Clutch bands are under $1,500 and the advertiser count is zero, downgrade to NO-GO unless inbound appears on its own.
5. **Kill criteria, any one ends the probe.** Fewer than 3 paid audits from 20 qualified conversations by day 30 (gate 1 and 2 fail). Fewer than 2 of the first 5 audited leads accept $1,950 or more (gates 1 and 4 fail). Engineer hours above 1.5 times the audit estimate on 2 of the first 3 jobs (gate 3 fails). Any refund dispute or chargeback. Any rebuild sold as a sprint. Any AI-operations introduction diverted.
6. **Success means a second decision, not a launch.** Three paid audits, two sprints delivered inside estimate, one buyer at $1,950 or more, and one client asking about ongoing work. Then, and only then, the sub-brand, the landing page and the conditional Meta test.

Why not a plain NO-GO: the downside of this probe is about $500 of cash, one engineer at half load for a month and four founder hours a week, against a market whose buyer-side evidence could not be read because the network was blocked, not because it was looked for and found absent. Why not the synthesis's wider plan: every input that made Meta or a sub-brand look sensible is an assumption, and the red team showed the opportunity cost of founder attention is the real price. Spend evidence first, money second.

