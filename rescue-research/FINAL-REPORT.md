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
- Payments: none. No source in 22 tracks shows a buyer paying a human $1,500 or more to rescue, finish or harden an AI-built app (T17 #1, T22 #1, T07 #4, T10 #3, T03 #9, T04 #3).
- Posted budgets (buyer-written, not payments): $2,000 "Twilio and Stripe Integration for Lovable App" (2025-10-28) and $2,000 "Full-Stack Base44 & QA Engineer for App and Website Launch" (2025-12-31) (T21 #1). Both are over 9 months old, seen by title only, with no proposal count or hire status (T21 #2). The verifiers add that one is "add Twilio and Stripe to an app whose UI is done" and the other is QA plus a WordPress migration: feature-scoped finish jobs, weaker than a pure fix (verification-log.md).
- Posted budgets at or above $1,500 where AI-built is not stated: $2,500 "Senior Backend Engineer — Marketplace Launch (Supabase / Stripe / Checkr)" (2026-10-12, solo founder, pre-launch hardening, T17 J9) and $1,500 on Freelancer.com split as $1,000 audit plus $500 stabilisation (T17 J10).
- Top confirmed AI-built fix or finish post: $1,200 (2026-10-15, review a Lovable prototype and build the rest, T17 J7); then $1,000 (2026-04-03, refine and deploy a Lovable and Supabase app, T07, T17 J6).
- Reviews: three Clutch reviews describe the right job (Lovable prototype to production at GeekyAnts; Bolt prototype rebuilt with a Supabase backend at Connectish; audit of two AI-built codebases at Cleveroad), but the search tool never showed the review's "Project size" field (T22 R1 to R3). Profile-level floors are suggestive, not proof: GeekyAnts minimum $10,000 or more; Connectish minimum $5,000 with 6 of 7 projects under $10,000 (T22 #3, #4).
- Secondhand only: a founder paid $600 for a 2-day fix and another spent $3,000 to make an MVP shippable, both relayed by a vendor blog from Reddit (T10 #3, T20 §3, weak). An HN commenter says of a non-technical friend with paying customers: "Now he's hiring a developer to shore it up." (buyer side, secondhand, verbatim, about 2025-07, T17 3B). No figure.
- Seller prices are not proof: Slopfix $10,000 a week with no named client (T08 #5, T17 #11, vendor); McKelvey $25,000 to $50,000 (T18 #8, vendor); at least 8 studios "from" $1,400 to $2,500 (T21 #7, vendor).
- Why unclear rather than fail: Reddit, where most buyer voices would be, returned zero pages in rounds 2 and 3 (T17, T22); the Clutch bands are unread. The single piece of evidence that settles it: open the three Clutch review pages and read "Project size" (about 10 minutes with a browser, T22 §6).

### Gate 2: a channel under 30% of first-project value (under about $600 on $2,000). UNCLEAR, leaning against for Meta, leaning pass only for low-volume channels on assumed inputs.
- Meta: 0 advertisers evidenced in 47 searches (14 in T05, 33 in T18). The Ad Library was never opened, so this is weak absence. Every funnel benchmark is vendor data from another niche: WordStream Facebook lead CPL $27.66 (2025-09), B2B Meta CPL $50 to $380, Metadata Facebook $145, cost per booked call $80 to $150, show rate 75 to 85%, B2B close 20 to 29% (T18 §5, all vendor).
- The model (channels.md §1): cost per paid audit $338 High / $1,450 Mid / $4,167 Low; cost per sprint client net of audit margin $419 / $3,666 / $19,806. Only the High case approaches $600. Track 18's own simpler stack gives $400 to $1,000 per thing sold on a call (T18 §7). A $2,000 ticket passes only in the High case; the Mid case needs a first project of about $12,220 (channels.md §1.4), which is why Meta may work for $10,000-plus sellers and not for a $2,000 sprint.
- Cheap channels: platform directories $425 at Mid and Upwork $470 at Mid pass on paper, but their inquiry volumes and win rates are assumptions, and they give about 0.4 to 0.6 clients a month each (channels.md §3). Sourced anchors are thin: Contra's Replit page shows 171 experts and 234 hires (vendor, 2026-10, T20 #1); the most-hired Lovable directory expert is also the cheapest (Weekend Inc, 100 hires, $50 an hour, stale listing, T20 #8); Lovable's own pages conflict on whether the Expert track still exists (T20 #7); Base44's 15% fee is contradicted inside its own docs (T09 #6).
- Settling evidence: open the Ad Library for UK and EU, where any ad type is covered for the past year (T05 #6); then our own $2,500 test's cost per booked call (section 13).

### Gate 3: repeatable work. PARTIAL PASS for the security and data-access hardening list; UNPROVEN for fix time and for the whole-rescue list.
- Sourced and repeated: RLS missing or weak and the public anon key as the only control (CVE-2025-48757, published 2025-05-30, disputed by Lovable, NVD, T11 #1; Supabase docs, T11 #3, #14). A researcher found about 170 of 1,645 Lovable showcase apps open with the anon key (2025, relayed by a vendor blog, T11 #2). Reeve: 57% of 3,680 reachable Supabase-backed apps allowed unauthenticated reads (Aug 2026, security vendor, T11 #4). Symbiotic: 1,046 of 1,072 sites had at least one flaw (Apr 2026, vendor, T11 #4). Nine seller lists compared: secrets 5 of 9, access control 5 of 9, payments 3 of 9, error handling 3 of 9, tests or CI 2, fake auth 2 (T19 5b). Marketplace fix lists repeat the same items (T07 #6, T21 #12) and so do the buyer posts J9, J13, J14 and J2 (T17 §7).
- Not sourced: 29 of the 38 draft checklist items in T11 §6b are engineering judgment; in delivery.md, 37 of 58 items are [E]. No published hours-per-task table exists (T19 #1, T11 #15). Only fragments: "take 2-4 hours to fix if you know what you're looking for" for the five commonest patterns (seller, verbatim, T19 §4), about 2 hours for a key exposure (vendor), 1 to 2 days per fix (vendor), 2 to 8 weeks for whole apps (vendor, T19 #2).
- Our own estimate (an assumption, not data): the week-one core is about 46 engineer hours with AI help, range 25 to 70; a typical Lovable app with Stripe is 2 sprint-weeks (delivery.md §3). A fixed 40-hour week fits only a small, clean app, so the sprint is sized from the audit (section 8).
- Rebuild share: unknown. Two HN freelancers both ended in a rewrite (T19 #5).
- Settling evidence: the hours log on the first 3 paid audits (delivery.md §8 pass marks: at least 75% of week-one items needed in 2 of 3; actual hours within 1.5x of estimate).

### Gate 4: a credible position above the low-cost floor. UNCLEAR, weak support. The position exists; it is not unique.
- The floor: Fiverr starting prices min $5, median $25 to $30, max $250 for vibe-specific gigs (about 60 gigs across two rounds, 2026-10-20, T07, T21 #9, verified medians only); Upwork fix posts $20 to $300 (T17 #2); Upwork productized tiers $49 to $750 (T21 #3); Pakistani sellers at $17 an hour and $40 to $100 gigs (T21 #5); Base44 partner rates $10 to $100 an hour (T09 #6, self-declared); audits from $199 to $399 (Valletta, MobiDev, Arkroot, T16 #6, vendor).
- The tier we would join: Teyrex from $1,400, Base44Devs $1,500, Vibe Code Rescue $1,500, AfterBuild $1,999, Arkroot EUR 1,999, GainCafe $2,500, Forasoft $2,500 (T21 #7, #8, T19 #13, T08 #4, vendor). Median of 11 fixed-rescue "from" prices: $2,500 (T21 §5).
- What is rare in that tier: a public price (about 7 of 29 agency rows showed any, T08 #2), a guarantee (Slopfix two-week warranty; Wavect last-week refund; GainCafe's vague "100% success guarantee", T08 #7, T21 #7), named case studies (none seen, T08 #8, T21 §D). That is the opening: price, scope and tests in writing, warranty, security sign-off.
- Against: buyers who name Lovable on job boards budget near the floor (T17 §7 contradicts); advice blogs say clients expect a Pakistan discount (old, weak, T15 #3); one PeoplePerHour buyer wants engineers, not prompt operators (verbatim, T21 §3).
- Settling evidence: whether audited leads accept $1,950 to $2,500 at 30% or better (offers.md §11), and whether prospects drop at "are you in Pakistan?" (brand.md §7).

### Gate 5: platform improvements unlikely to erase demand within 12 months. UNCLEAR, leaning pass.
- Shrink: Lovable ships baseline scanners and a Wiz integration (2026-05-07), but the Wiz step is for teams already on Wiz (T12 #11, vendor). Lovable Cloud is on by default since 2025-09-29 (T20 #3). Replit shipped a Security Agent (2026-04-21) and black-box pen tests (2026-08-17) (T12 #13, vendor). Clients now patch small bugs with AI and call a developer only for hard problems (HN commenter, paraphrase, T14 #10).
- Grow: about 1M new Lovable projects a week and 50M total (vendor, unaudited, no count of live projects, T12 #3); 57% open reads in Aug 2026, 15 months after the CVE (vendor, T11 #4); Replit's own black-box scan found an admin dashboard its code scanner missed (T12 #13); Lovable Cloud to own-Supabase migration is manual (T20 #4); Supabase deprecates anon and service_role keys by end 2026 (T11 #14); no in-house done-for-you rescue service found at Lovable, Replit, Bolt or Base44 (two negative searches, weak, T20 #2).
- Platforms are intermediating, not delivering: Replit routes experts to Contra (T20 #1); Lovable runs a partner directory (T20 #7); Base44 has an in-product hire marketplace (T09 #6). The risk is lead capture and a fee, not the demand vanishing.
- Net: the cheapest faults (basic RLS, exposed keys) get commoditised first; finishing, payments, data-model repair, migration and a human accountable for production persist. Settling evidence: log, in each audit, what the platform scan already flagged versus what we found (delivery.md §8).

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
| XCONS Solutions | Pakistan (Lahore) | not shown | rescue page | none | none | none found (T21 #5) |
| Ahmad M. (Upwork) | Pakistan (Bahawalnagar, weak match) | $17 an hour | audit first, written report | none | self-reported Top Rated Plus | none (T21 #5) |
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

Source: model/delivery.md, built from T11 §6b (38 items) and T19 §5b (9 seller lists). Hours are Wanile estimates, not published data: no hours-per-task table exists anywhere (T19 #1, T11 #15).

The playbook, one engineer plus a lead who reviews (engineer hours 3, 8, 8, 8, 8, 5 = 40; lead 1, 2, 1, 1.5, 1, 1.5 = 8):
- Day 0, intake: fit call; ethics screen; client-owned access to GitHub, Supabase, Stripe test mode, hosting and domain; database and storage snapshot before anything changes (the Replit agent deleted a live database in a code freeze, T11 #11); code freeze starts; contract and written test authorisation.
- Day 1, audit: build locally; secret scan, dependency audit, Supabase Security and Performance Advisors; RLS probe with two test users and the anon key on a staging copy only; checklist filled with severity and hours; triage signals; acceptance-test list and parked list; 2 to 4 page report. No fix work until the client signs the acceptance list.
- Day 2, secrets and database: rotate exposed keys, move secrets server-side; create staging; RLS on every table, user-data and money tables first; migrations in git.
- Day 3, auth and functions: server-side route guards and ownership checks (the BOLA pattern from Lovable's own 2026 bug, T11 #9); roles not user-editable; edge functions check JWT, validate input, set CORS; RLS test harness in CI; Stripe webhooks in test mode; hours checkpoint at 1.25x plan.
- Day 4, payments, deploy, tests: Stripe live-mode checklist with signature verification and idempotency; smoke tests on the signed journeys; CI with build, lint, tests, secret scan; domain, HTTPS, email DNS, security headers; CLAUDE.md or AGENTS.md guardrails in the repo (Slopfix hands over the same, vendor, T19 #8).
- Day 5, verify and hand over: full acceptance list passes on staging; release with rollback in a low-traffic window; runbook; 15 to 20 minute handover video; security sign-off list with the plain disclaimer that we find and fix what we find and do not certify the app as secure (T11 §6); parked list; keys rotated and our access removed.

The checklist: 58 items in 11 groups (intake, auth, RLS and database, secrets, payments, edge functions, deploy, performance, code structure, tests and CI, monitoring, handover). 21 items are sourced, 37 are judgment. Tiers: W1 week-one core (37 items, about 46 engineer hours with AI help, range 25 to 70), IF items only if the feature exists (8 items, about 20 hours, mostly payments and LLM calls), W2 second week (11 items, about 36 hours), X separate quote (Lovable Cloud exit 12 to 30 hours; tax and invoicing). AI is used for inventory, scans, policy drafts, types, docs, CI and test scaffolding; humans own RLS design, auth, ownership checks, payments and sign-off; no AI agent ever holds production credentials (delivery.md §2). The one finding that shapes everything: a 40-hour week safely holds about 32 hours of checklist work, so a small clean app fits one week and a typical Lovable app with Stripe is two weeks (delivery.md §0).

The rescue-or-rebuild rule (delivery.md §5; thresholds are judgment [E] except the vendor 60% line [V]):
- Hours rule from the audit, AI-adjusted mid: 32 or less, one-week sprint; 33 to 64, two weeks; 65 to 128, extended rescue with a go or no-go after each week; over 128, rebuild quote.
- Signals rule: rebuild quote if the data model cannot take owner-based RLS without a schema change on more than 30% of tables or on any core table; or auth is home-made or spread across most components; or the backend is Base44 (export is frontend only, T02 #5); or fix cost is 60% or more of rebuild cost (a vendor heuristic, T19 #5); or deploy failure rate is over 40% and more than half the files are touched. Lovable Cloud is amber and adds the migration job (T20 #4). Live paying users plus a red signal still gets a "stabilise first" sprint (RLS lockdown, key rotation, backup) while the rebuild is planned.
- Take the more severe of the two rules. Published evidence on this is almost nil: two HN freelancers both ended in rewrites; one vendor says rewrites are almost always wrong when the app has users (T19 #5, vendor).

Scope-creep controls (delivery.md §6; all judgment, the evidence on client re-prompting is thin, T19 #7): a code freeze on the client's Lovable project from day 0 to day 5, with a sandbox copy for new ideas; branch protection so our pull request is the only way into main; a daily drift check for outside commits and dashboard schema changes; written change requests with three outcomes only (swap, add at $500 an engineer-day, park); an 8-hour free overrun absorb limit, never silently past 2x; a numbered acceptance list of 15 to 30 tests signed before day 2; a parked-items list that becomes the next-sprint menu; a day-3 checkpoint. If the client keeps prompting the AI: first time we rebase and absorb an hour, second time a change request and the clock pauses, third time we pause work and offer a re-audit fee or partial delivery with a pro-rata refund.

## 9. Unit economics for each offer shape

Inputs (offers.md §1): engineer $1,050 a month, $6.06 an hour; lead reviewer $2,400 a month, an assumption; loaded multiplier 1.75 on labour, an assumption (channels.md and delivery.md use 1.5, also assumed); payment fees 3.5%; expected case adds 20% hours and 5% refunds; stress case doubles hours and uses 10% refunds. No overrun, refund or conversion data exists in the evidence (T16 #11, T19 #12), so every margin below is arithmetic on assumptions.

| offer | price | labour (engineer h + lead h) | gross margin: salary-only / loaded / expected / stress | main risk |
|---|---|---|---|---|
| A. Audit | $495 (large app $950) | 16 + 5 | 63% / 35% / 23% / -24% | free competitors; no conversion data; it is a filter, not a profit line |
| B. Hardening Week | $2,500 (founding $1,950) | 40 + 8 | 82% / 71% / 61% / 36% | price above confirmed AI-built budgets; overrun on a bad codebase |
| C. Finish-and-Launch | $4,500 (founding $3,900) | 100 + 16 | 78% / 63% / 52% / 21% | scope creep; 2.25x the $2,000 posts |
| E. Cloud Exit | $1,500 add-on, $2,000 alone | 32 + 6 | 78% / 63% / 51% / 21% | cutover data issues |
| D1. Care | $450 a month | about 20 + 2 | 87% / 75% / 66% / 58% | no attach data |
| D2. Support | $1,500 a month | 15-hour pool | 88% / 79% / 71% / 64% | no attach data |
| D3. Dedicated | $3,800 a month | 160 + 4 | 70% / 57% / 45% / 19% | few buyers; no overrun lever |

Why $2,500 and not $2,000 for B (offers.md §4): at $2,000 the 30% acquisition cap is $600 and profit after a capped acquisition is $459; at $2,500 the cap is $750 and the profit $766; $2,500 is the median seller "from" price (T21); and $2,000 would sit in the middle of 8 studios where price does not differentiate. The founding price of $1,950 and a price-down trigger (list drops to $2,000 if more than 60% of audited leads reject on price) cover the gap to the two $2,000 posts.

Break-even and acquisition caps (channels.md §2, placeholder prices): on a $2,000 sprint the gate-2 cap is $600, break-even acquisition is $1,322 and 30% net margin allows $722; so gate 2 is a strict test, not a survival test. Blended view (offers.md §9): 10 audits at an assumed 40% audit-to-sprint rate give revenue $12,970, loaded cost $6,170, gross margin 52%; the 30% rule then caps acquisition at about $390 per paid audit, about $300 at 25% conversion. Capacity (delivery.md §4): two engineers can deliver 8 sprint-weeks a month at full load, plan on 6; fixed cost about $3,200 to $3,400 a month, so break-even is about 2 sprint-weeks a month before acquisition cost. The real cost of a 3x overrun is capacity, about $4,000 of unsold weeks, not cash.

## 10. Retention: the path from rescue to maintenance or a dedicated engineer

Evidence: none on the buyer side. Two rounds found zero buyer voices on keeping a developer after a fix and zero conversion, churn or retainer-length figures (T14 #8, T20 #11). Seller claims only: "many clients choose to keep us as their maintenance team after the launch." (seller, verbatim, Akveo, T14 §4); an Indie Hackers commenter: "the regression problem is your recurring revenue. A one-time audit is a project." (seller, verbatim, T14 §4). Against: an HN commenter says clients now fix small bugs with AI and call a developer only for harder problems (paraphrase, T14 #10). Adjacent benchmarks of 25 to 40% attach and 70 to 85% 90-day retention come from non-code Upwork agency guides (vendor, T20 #13).

Prices (all vendor asking prices unless marked): small-app maintenance $500 to $3,000 a month in Western markets (T14 #1); rescue-shop retainers $500 to $2,000 (scopenine), $1,500 to $3,000 (McKelvey), $2,000 to $6,000 (Frenchy), $4,500 plus GST (one Australian shop), $5,000 to $25,000 with a 3-month minimum (Indianic) (T20 #12); dedicated mid-level React developer in South Asia $3,040 to $4,960 a month (Secondtalent, 2026-09, T14 #5) and $4,000 to $6,400 in Pakistan remote-hiring guides (T20 #15). Buyer side: one live cafe app offers a flat $120 a month for on-call RLS fixes (2026-10-14, T17 J11); a Lovable builder's whole stack costs $91 to $131 a month (third-party, T14 #7), so a $450 plan is 3 to 5 times their tool bill. Maintainers often refuse code they did not write: "limited to projects we have built ONLY" (seller, verbatim, Gumroad care plan, T20 #14), a gap a rescue shop can fill.

The path (offers.md §8): 30-day warranty on every sprint; Care $450 a month offered at handover, only for apps we hardened; Support $1,500 a month (15-hour pool, one request at a time) when the app earns; Dedicated engineer $3,800 a month, 3-month minimum, when the client is funded. Planning assumption, not evidence: 15% of sprint clients take Care for 6 months, worth about $405 revenue per sprint client, 16% of one sprint. Do not build the model on it; measure take-up on the first 8 sprint clients and drop Care as a product if under 10%.
