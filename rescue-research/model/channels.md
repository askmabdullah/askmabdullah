# Channel economics (Phase 2, Channel Economist)

Run: 2026-10-20. Inputs: BRIEF sections 1 to 8, phase1-summary.md, all 22 track files, ads-library.md, model/delivery.md and model/risk.md (read for hours and refund assumptions). model/offers.md did not exist when I started, so I used the placeholder prices from the task.

## How to read this file

- Plain truth first: **nothing here is a measured cost per client.** No track found a published cost per call or cost per client for vibe-code rescue (T5, T18). Every funnel number below is either a vendor benchmark from another niche or my own assumption. I label each one.
- Source tags: **[T18]** etc. = track file. **[V]** = vendor number (marketing blog or ad-software company). **[A]** = my assumption, no source. **[X]** = outside Phase 1 (one WebSearch, see section 3).
- "High", "Mid" and "Low" describe the **outcome**, not the input. High = good result (cheap leads, high close). Low = bad result.
- Arithmetic is shown in tables so you can redo it. A script check was run on every figure.
- Gate 2 test used throughout: cost per paying client is at most 30% of first-project value. For the $2,000 sprint that is **$600**. For a client who buys the $500 audit and then the sprint, I count the first project as the credited $2,000 (the audit is credited in full, the shape seen at 3 vendors, T16 #1, and recommended in model/risk.md 1.10).

---

## 1. Meta ads funnel model

### 1.1 Which benchmarks are vendor numbers

All of them. Track 18 found no independent data (no regulator, no academic, no platform statement). Grading from T18:

| benchmark | value | source | vendor? | T18 grade |
|---|---|---|---|---|
| Facebook lead-campaign CPL, all industries | $27.66 (+21% YoY) | WordStream/LocaliQ 2025 | vendor, own account data | moderate (all-industry) |
| Lead CTR / lead CPC | 2.59% / $1.92 | same | vendor | moderate |
| Traffic CTR / CPC | 1.71% / $0.70 | same | vendor | moderate |
| B2B Meta CPL | $50 to $380 | many blogs | vendor | weak |
| B2B CPL Instagram / Facebook | $138 / $145 | Metadata benchmark, 153 advertisers (lead definition unpublished) | vendor | weak |
| B2B CPL LinkedIn / Google | $202 / $524 | same | vendor | weak |
| B2B SaaS CPL, landing page | $120 to $380 | GrowthSpree | vendor | weak |
| Meta CPM | $9 to $15 ($9.31 AdKit median; $14.19; $15.20 B2B tech) | several | vendor | weak |
| B2B Meta CTR | 0.92% to 1.37% (Focus Digital); 0.78% (B2B tech) | several | vendor | weak |
| Cost per booked call | $80 to $150 | one agency playbook; one restaurant case | vendor, other niche | weak |
| Show rate | 75 to 85% | vendor list | vendor | weak |
| B2B close rate | 20 to 29% | two vendor sources | vendor | weak |
| Warm vs cold win rate | 30 to 50% vs 10 to 20% | pitchsite, gigradar | vendor | weak |
| Software development cost per lead | $510 organic, $680 paid, $591 blended | First Page Sage via T18 | vendor | weak |
| Software/IT services cost per sales-qualified lead | $1,680 to $3,080 | Belkins via Zephra | vendor | weak |

Two honest flags on these numbers:

1. **Metadata's "$138 to $202" mixes platforms.** $138 is Instagram, $145 is Facebook, $202 is LinkedIn. Only $138 and $145 are Meta. I use $145 for the mid case.
2. **The track 18 benchmarks do not reconcile with each other.** CPM $9 to $15 and CTR 0.78% to 1.37% give a click cost of $0.66 to $1.92. WordStream's own $1.92 CPC with a 2.59% CTR would imply a CPM near $50, not $9 to $15. And if you take a normal landing-page rate of 2 to 5% on those clicks, you get a cost per lead of $13 to $96, far below the sourced B2B figures of $50 to $380. The B2B CPL figures include lead quality filters. So I **anchor cost per lead on the sourced CPL points** and back-solve what landing-page conversion that implies. If the real landing page converts at 3%, the model is conservative.

### 1.2 Inputs by case

| step | High | Mid | Low | basis |
|---|---|---|---|---|
| CPM | $9 | $12 | $15 | [T18 V] range $9 to $15; mid is the midpoint [A] |
| Link CTR | 1.37% | 1.15% | 0.78% | [T18 V] B2B 0.92 to 1.37%; 0.78% B2B tech; mid is the midpoint of 0.92 to 1.37 [A]. WordStream's 2.59% is NOT used: with a $9 CPM it gives a $0.35 click, below every CPC in T18 |
| CPC (calc) | $0.66 | $1.04 | $1.92 | CPM / (CTR x 1000). Low case equals WordStream's $1.92 lead CPC. |
| Cost per lead (CPL) | $50 | $145 | $250 | [T18 V] $50 = low end of B2B $50 to $380; $145 = Metadata Facebook; $250 = middle of GrowthSpree landing-page range $120 to $380 |
| Implied click-to-lead rate | 1.31% | 0.72% | 0.77% | CPC / CPL. Low versus typical web rates, see 1.1. |
| Lead to booked call | 60% | 50% | 40% | [A] No source. A lead is a form submit; a booked call is a chosen slot. |
| Call show rate | 85% | 80% | 75% | [T18 V] 75 to 85% |
| Held call to paid audit | 29% | 25% | 20% | [T18 V] B2B close 20 to 29%. Different ticket ($500, not a full project) and cold ad leads: no adjustment possible. |
| Paid audit to sprint | 50% | 35% | 20% | **[A] No source at all.** T16 #11: zero audit-to-project data points in 8 searches. T20 #13 gives 25 to 40% "attach" but for retainers in non-code fields. |

Funnel shape used: ad, landing page, application/lead, booked call, held call, **paid $500 audit (credited)**, sprint. A direct-purchase variant is in 1.5.

### 1.3 Arithmetic and outputs

| line | High | Mid | Low | formula |
|---|---|---|---|---|
| Cost per click | $0.66 | $1.04 | $1.92 | CPM / (CTR x 1000) |
| **Cost per lead** | **$50** | **$145** | **$250** | anchored on benchmark |
| Cost per booked call | $83 | $290 | $625 | CPL / booking rate (50/0.6; 145/0.5; 250/0.4) |
| **Cost per held call** | **$98** | **$362** | **$833** | booked / show rate |
| **Cost per paid audit** | **$338** | **$1,450** | **$4,167** | held call / close rate |
| **Cost per sprint client (ad spend only)** | **$676** | **$4,143** | **$20,833** | paid audit / audit-to-sprint rate |
| Audit margin recovered | $257 x 1 | $257 x 1.86 | $257 x 4 | non-converting audits per sprint client = 1/rate - 1; audit gross profit $257 (section 2) |
| **Cost per sprint client, net of audit margin** | **$419** | **$3,666** | **$19,806** | ad spend per client minus recovered audit margin |
| Gate 2 test ($600) | net passes, gross fails by 13% | fails 6x | fails 33x | |

Cross-check with track 18's own stitched estimate: $80 to $150 per booked call, 75 to 85% show, 20 to 29% close gives $400 to $1,000 per **paid thing sold on the call** (T18 section 7). That lines up with my **cost per paid audit** in the High case ($338) and falls between High and Mid. My Mid case is more cautious than T18 because it uses a B2B CPL ($145) and a 50% booking step instead of an $80 to $150 booked-call price that comes from one agency blog and one restaurant case. Adding the audit-to-sprint step multiplies every number again, which T18 did not do. T18 called its range "could pass or fail". With the extra step, only the High case gets near the line.

### 1.4 What first-project value would make Meta pass gate 2

Ticket needed = cost per client / 0.30.

| case | gross | net of audit margin |
|---|---|---|
| High | $2,253 | $1,397 |
| Mid | $13,810 | $12,220 |
| Low | $69,444 | $66,020 |

Read: at a $2,000 ticket only the High case is near a pass. At $10,000 to $15,000 (the price of Slopfix and McKelvey's lighter rescues, T10, T18, vendor asking prices) the Mid case would pass. This matters for the "agencies close well on Meta" claim (section 5).

### 1.5 Sensitivity: cost per sprint client (ad spend only), Mid inputs except the two weakest

| CPL | audit-to-sprint 20% | 35% | 50% | 70% |
|---|---|---|---|---|
| $50 | $2,500 | $1,429 | $1,000 | $714 |
| $100 | $5,000 | $2,857 | $2,000 | $1,429 |
| $145 | $7,250 | $4,143 | $2,900 | $2,071 |
| $250 | $12,500 | $7,143 | $5,000 | $3,571 |

Only a CPL near $50 combined with a 70% audit-to-sprint rate gets near $600 (gross $714). Both are unsupported by any source. For a net-of-audit view subtract roughly $250 to $500.

**Direct-purchase variant (landing page sells the $500 audit with a card).** No data. The useful number is the break-even: with a Mid click cost of $1.04, to reach $600 per sprint client at 35% audit-to-sprint, the page must turn **at least 0.50% of clicks into paid audits** (1.04 / (600 x 0.35)). The call funnel's Mid yield is about 0.07% of clicks (0.72% click-to-lead x 50% booked x 80% show x 25% close = 0.072% of clicks become paid audits). A $500 cold purchase from an unknown Lahore vendor is a trust problem (T15, T20 #16 to #18: no buyer data either way). Treat 0.5% as an untested hope, not a base case.

---

## 2. Break-even cost per client by offer

### 2.1 Delivery cost assumptions

| input | value | basis |
|---|---|---|
| Engineer salary | $1,050 / month | [BRIEF 1] midpoint of $1,000 to $1,100 |
| Loading factor | x1.5 = $1,575 / month, $71.6 per day, $8.95 per hour (22 days, 8 hours) | [A] covers seat, tools, management, bench time. Salary-only would make margins about 10 points higher. |
| Lead reviewer | $20 per hour loaded | [A] about $2,500 per month x1.5 over 176 hours, rounded |
| Payment fee | 3% of price | [A] general knowledge, not from Phase 1 |
| Refund / warranty reserve | 5% of price on audit and sprints | [A] model/risk.md 1.10 says refund rates are assumptions (5%, 10%, 15% examples), no data |
| Sprint hours | 40 engineer hours + 8 lead hours per week | [model/delivery.md] day plan 3, 8, 8, 8, 8, 5 and lead 8 hours. The same file warns a safe week is about 32 checklist hours |
| Audit hours | 16 engineer hours + 3 lead hours | [A] sellers quote 2 to 5 days for audits (T5, T16 vibecoding.app); Teyrex "report from 3 days" (T21) |
| Care plan hours | 20 engineer hours + 2 lead hours per month | [A] |
| Dedicated engineer | 176 engineer hours + 8 lead hours per month | [A] one full-time engineer |
| Target gross margin | 60% | [A] |
| Target net margin after acquisition | 30% | [A] used for the third threshold column |

### 2.2 Offer economics (placeholder prices)

| offer | price | engineer | lead | fee + reserve | **delivery cost** | gross profit | gross margin | meets 60%? |
|---|---|---|---|---|---|---|---|---|
| Audit | $500 | $143 | $60 | $40 | **$243** | $257 | 51% | no |
| 1-week sprint | $2,000 | $358 | $160 | $160 | **$678** | $1,322 | 66% | yes |
| 2-week sprint | $4,000 | $716 | $280 | $320 | **$1,316** | $2,684 | 67% | yes |
| Care plan (per month) | $500 | $179 | $40 | $15 | **$234** | $266 | 53% | no |
| Dedicated engineer (per month) | $3,500 | $1,575 | $160 | $105 | **$1,840** | $1,660 | 47% | no |

Notes:
- The dedicated engineer margin is 62% on a salary-only basis ($1,050 + $160 + $105 = $1,315). At the loaded 1.5x it needs about $4,600 a month to reach 60%. The market anchor for a Pakistan-based mid-level dedicated developer is $4,000 to $6,400 a month (T20 #15, vendor guides), so $3,500 is below the anchor.
- Stress case for the 1-week sprint (engineer and lead hours x1.5, scope creep): cost $937, gross profit $1,063, margin 53%. At 1.5x the sprint still makes money; model/delivery.md sets a 1.25x checkpoint.

### 2.3 Maximum allowed acquisition cost per client

| offer | **Gate 2 max (30% of first-project value)** | **Break-even (first-project gross profit)** | Max cost that still leaves 30% net margin | Price needed for 60% gross margin |
|---|---|---|---|---|
| Audit | **$150** | $257 | $107 | $608 |
| 1-week sprint | **$600** | $1,322 | $722 | $1,695 |
| 2-week sprint | **$1,200** | $2,684 | $1,484 | $3,290 |
| Care plan (month 1) | **$150** | $266 | $116 | $585 |
| Dedicated engineer (month 1) | **$1,050** | $1,660 | $610 | $4,600 |

Formulas: gate 2 = 0.30 x price. Break-even = price - delivery cost. 30% net = 0.70 x price - delivery cost.

Read: the gate 2 limit ($600) is well under the break-even ($1,322), so a client acquired at $1,000 still earns cash on the first sprint. Gate 2 is a strict test, not a survival test. Break-even matters for risk; gate 2 matters for the GO call.

### 2.4 Lifetime value at 0%, 20% and 40% attach

"Attach" = share of sprint clients who later buy a monthly plan. **No source gives any attach number.** T14 and T20 #11: zero buyer voices, zero conversion figures, only seller anecdotes ("many clients keep us", Akveo; "most clients stay on a monthly retainer", unnamed). T20 #13's 25 to 40% attach and 70 to 85% 90-day retention are from Upwork-agency guides in non-code fields. An HN commenter says clients now fix small bugs with AI (T14 #10). So 0% is the planning case; 20% and 40% are what-if upside.

Additional assumptions [A]: attached clients stay 6 months on the care plan (monthly gross profit $266), or 4 months on a dedicated engineer (monthly gross profit $1,660). LTV here = gross profit only, not revenue.

| first project | gross profit at 0% | care plan 20% | care plan 40% | dedicated 20% | dedicated 40% |
|---|---|---|---|---|---|
| Audit | $257 | $576 | $895 | $1,585 | $2,913 |
| 1-week sprint | $1,322 | $1,641 | $1,960 | $2,650 | $3,978 |
| 2-week sprint | $2,684 | $3,003 | $3,323 | $4,012 | $5,340 |

Formula example (sprint, care plan, 20%): 1,322 + 0.20 x 6 x 266 = 1,641. Dedicated: 1,322 + 0.20 x 4 x 1,660 = 2,650.

LTV divided by 3 (a common "3 to 1" rule, [A]) as a ceiling on acquisition cost for the 1-week sprint: **$441 at 0% attach**, $547 (care 20%) to $883 (dedicated 20%), $654 (care 40%) to $1,326 (dedicated 40%). At 0% attach the 3-to-1 rule ($441) is stricter than gate 2 ($600). Retention evidence cannot be used to relax gate 2.

---

## 3. The next-best channels

### 3.1 Evidence scan for each candidate

| channel | what Phase 1 found | volume evidence | price level evidence | main problem |
|---|---|---|---|---|
| (a) Upwork / marketplaces | 18 buyer posts, budgets $5 to $2,000+; 6 posts at $1,000+, only 2 at $2,000 (both over 9 months old); Supabase hardening posts $1,500 and $2,500, AI-built not stated [T7, T21] | No proposal counts, no hire status [T21] | Most posts $20 to $1,000; floor $17/hr Pakistani sellers, Fiverr median $25 [T21] | few $1,500+ jobs; no reviews on a new account; low trust for Lahore vendors (weak, T15/T20) |
| (b) SEO and content | RapidDev 509-page hub [T18 S22]; agency SERP dominance, 7 agency pages in 9 results for "vibe code cleanup service" [T6]; "vibe coding" 95k to 110k US searches/month (head term, flat since March 2026) [T6, T18 vendor]; no volume for any rescue term [T6] | none for buyer terms | n/a | slow; seller says SEO "has stopped being a useful avenue" (HN, seller, unconfirmed thread, T18) |
| (c) Platform directories | Lovable Expert/Partner directory with hire counts: Weekend Inc 100 hires at $50/hr, Creme Digital 50 at $100, Neo Carbone 28 at $130, Zeroqode 21 at $75 (stale, possibly old) [T20 #8]. Expert track free, paid Lovable plan needed, 5 working days to answer, 10% commission is for referring Lovable plans, not a fee on our work [T9]. Contra's Replit page: 171 experts, 234 hires, jobs $50 to $75/hr [T20 #1]. Base44 marketplace 15% fee unconfirmed, rates $10 to $180/hr [T9]. | Real but small: 234 hires across 171 experts is 1.4 per expert; hire counts per time unknown | $50 to $130/hr; 40 hours at $50 = $2,000, so a $2,000 week sits at the cheapest end of top-hired experts | Lovable's own pages conflict on whether the Expert program is still active [T20 #7]; the lead flow is unproven; most-hired expert is the cheapest |
| (d) Outbound to live apps | ~101k BuiltWith Lovable sites, 3,937 on .ai; 5 to 10% with any revenue (weak, T13); cold email reply 3 to 6% (vendor, T20 #25); CAN-SPAM no B2B exemption, up to $53,088 per email; UK PECR skip sole traders; CASL and Spam Act need role-relevance (T20 #21 to #24) | list is findable, quality low | n/a | legal friction; list quality; "I found a vulnerability" hook is a reputation and legal risk (T20 #26) and we must not probe apps (BRIEF 8) |
| (e) Communities and word of mouth | Sellers say referrals and word of mouth (HN seller comment; QuickLaunch "$120k+ in 2025, referrals, no ads" is UNCONFIRMED per T18 S9 vs S11) [T10, T18]; VibeCodeFixers matched only 30 to 40 projects [T10] | none | n/a | cannot be bought; needs delivered work and proof first; Reddit coverage zero in Phase 1 |

### 3.2 The two I picked, and why

1. **Platform directories and expert marketplaces (c)**: near-zero cash cost; buyers are already looking to hire; hire counts show money is moving; hourly rates ($50 to $130) bracket our $2,000-per-week price.
2. **Upwork-type job marketplaces (a)**: the only channel with real buyer-written posts at our ticket (two at $2,000, T21), a small known cost (Connects), and fast to test.

Why not the others as the "two best": SEO takes 6 to 12 months and the SERP is owned by agencies. Outbound has legal drag and the weakest arithmetic (section 4). Communities and referrals are probably the cheapest long-run channel, but they cannot produce a first client on demand; I rank them third and model them in section 4. Honest caveat: the two picked channels are volume-capped (about 0.4 to 0.6 clients a month in the Mid case). They are cheap per client but cannot fill a business alone.

### 3.3 Channel A: platform directories (Lovable, Contra/Replit, Base44)

[X] none needed. Inputs:

| input | High | Mid | Low | basis |
|---|---|---|---|---|
| Qualified inquiries per month | 8 | 3 | 1 | [A]. Anchor: Contra 234 hires / 171 experts (T20 #1); Lovable top experts 21 to 100 hires with unknown time (T20 #8). A new listing with no reviews gets few. |
| Inquiry to paying client ($2,000 first project) | 30% | 20% | 10% | [A]; warm inbound vs cold win rates 30 to 50% vs 10 to 20% [T18 V], haircut for no reviews and Lahore |
| Platform fee on our work | 0% | 10% | 15% | [T9] Lovable: no fee found; Base44 15% unconfirmed; Contra unknown. [A] |
| Set-up cost, per month over 6 months | $75 | $75 | $75 | [A] about 3 engineer-days ($215) for demo projects Lovable's review looks at (published projects, traffic, build quality, T9) + $25/month Pro plan (T14) = $450 / 6 |
| Lead time per inquiry | 1 hour at $20 | same | same | [A] |

| result | High | Mid | Low |
|---|---|---|---|
| Clients per month | 2.4 | 0.6 | 0.1 |
| Cost per month | $75 + 8 x $20 + 0 = $235 | $75 + 3 x $20 + 10% x $2,000 x 0.6 = $255 | $75 + 1 x $20 + 15% x $2,000 x 0.1 = $125 |
| **Cost per client** | **$98** | **$425** | **$1,250** |
| Time to first client | 4 weeks | 4 to 8 weeks | 3+ months |
| Gate 2 ($600) | pass | pass | fail |

Risk: directory buyers are often hourly. A $2,000 fixed sprint has to be sold as a productised week; otherwise clients pay $50/hr for small tasks.

### 3.4 Channel B: Upwork job marketplace

[X] One WebSearch (1 of 3 allowed) on Upwork pricing, third-party blogs summarising it: Connects cost **$0.15 each**; a proposal costs about **2 to 16 Connects** depending on the job (other sources: 2 to 6 on standard jobs); free Basic account gets 10 Connects a month; Upwork's own pricing page lists freelancer service fees at **0% to 15%** (sources conflict on the exact structure). Upwork's own page is more reliable than the blogs, but I did not open it. Verify in an account.

| input | High | Mid | Low | basis |
|---|---|---|---|---|
| Relevant jobs at $1,500+ per month we can propose to | 15 | 6 | 2 | [A]. Anchor: only 2 Lovable/Base44 posts at $2,000 and 2 Supabase hardening posts at $1,500 and $2,500 found in a partial search of a year (T21). The true volume is unknown and larger than what a snippet search shows. |
| Win rate per proposal | 12% | 6% | 2% | [A]. T18 vendor figures: 43% agency proposal win rate, 28 to 35% for web dev, 10 to 20% cold. Heavy haircut: new account, no reviews, $17/hr competitors (T21). |
| Cost per proposal | 8 Connects ($1.20) + 30 min ($10) = $11.20 | $1.20 + 45 min ($15) = $16.20 | $1.20 + 60 min ($20) = $21.20 | [X] Connects; [A] time at $20/hour |
| Service fee | 10% | 10% | 15% | [X] range 0 to 15%; applied to a $2,000 job |

| result | High | Mid | Low |
|---|---|---|---|
| Proposals per client | 8.3 | 16.7 | 50 |
| Proposal cost per client | $93 | $270 | $1,060 |
| Fee per client | $200 | $200 | $300 |
| **Cost per client** | **$293** | **$470** | **$1,360** |
| Clients per month (jobs x win rate) | 1.8 | 0.36 | 0.04 |
| Time to first client | 2 to 4 weeks | 4 to 8 weeks | 6+ months |
| Gate 2 ($600) | pass | pass | fail |

Risk: the budgets T7/T21 saw are mostly under $1,000. Taking those jobs at $500 to $1,000 means a different product (the $500 audit fits). The channel's problem is volume and trust, not cost.

---

## 4. All channels ranked by expected cost per paying client

Basis: cost per paying client for a first project (about $2,000). Meta and outbound include the paid audit step, so their number is per sprint client; the others are per $2,000 client directly. Mid case is used for rank. Lower is better. **Confidence is LOW for every row.** Why "low" differs: Meta and outbound use vendor benchmarks stitched across niches; the cheap channels use mostly unsourced assumptions, so their low cost partly reflects optimism in my inputs, not strong evidence.

Extra channel inputs, all [A] unless noted:
- Communities: 6 hours a week at $20 = $520 a month (cash cost near zero; founder time at $100 an hour would be 5x). Qualified inbound per month 8 / 3 / 0.5; warm win rate 40% / 30% / 15% [T18 V warm 30 to 50%].
- SEO: build $5,000 (about 25 pages at $200) over 12 months = $417 plus $600 a month upkeep. Visits per month at maturity 1,000 / 400 / 100; visit-to-lead 4% / 2.5% / 1%; lead-to-client 25% / 20% / 10%. Starts to pay in month 4 to 6 at the earliest.
- Outbound: 1,000 contacts a month; reply 6% / 4.5% / 3% [T20 #25 V: 3 to 6%]; positive share of replies 40% / 30% / 25% [A]; booking 80% / 70% / 60% [A]; show 85 / 80 / 75% [T18]; audit close 20 / 15 / 10% [T18 cold 10 to 20%]; audit-to-sprint 50 / 35 / 20% [A]; monthly cost = one researcher/SDR $1,575 + tools $300 = $1,875 [A].

| rank | channel | cost per client High / **Mid** / Low | clients per month (Mid) | time to first client | confidence | gate 2 at Mid? |
|---|---|---|---|---|---|---|
| 1 | Platform directories (Lovable, Contra/Replit, Base44) | $98 / **$425** / $1,250 | 0.6 | 4 to 8 weeks | Low | yes |
| 2 | Upwork / job marketplaces | $293 / **$470** / $1,360 | 0.36 | 2 to 8 weeks | Low | yes |
| 3 | Communities and word of mouth | $162 / **$577** / $6,928 | 0.9 | 6 to 12 weeks | Low | yes (barely) |
| 4 | SEO and content | $102 / **$508 steady-state** / $10,167; year-one about $1,200 to $2,000 per client (ramp [A]) | 2.0 after month 6 | 4 to 12 months | Low | not in year one |
| 5 | Meta ads (paid audit then sprint) | $419 net / **$3,666 net** ($4,143 gross) / $19,806 net | 0.6 per $2,500 spent | 3 to 6 weeks to first paid audit, 5 to 8 to first sprint | Low | no; High case only |
| 6 | Cold outbound to live apps | $1,149 / **$4,724** / $27,778 | 0.4 per 1,000 contacts | 4 to 8 weeks | Low | no |

How to read it:
- Four channels pass gate 2 at Mid on paper, but they are **volume-capped** (about 0.4 to 2 clients a month combined) and rest on unsourced inputs. None is proven.
- Meta and outbound are the only channels that scale with money or effort, and both fail gate 2 at Mid by 6x to 8x.
- A realistic plan runs the cheap channels in parallel from week one (they cost almost no cash), and uses Meta only as a bounded $2,500 test (section 6).
- Existing Wanile relationships (UK, US, Europe, Australia and the Middle East clients, BRIEF 1) are not modelled because Phase 1 has no evidence on them. Asking existing clients for introductions is the most likely cheapest channel of all, and the cheapest to test.

---

## 5. The claim "agencies spend heavily on Meta ads and close well"

**Verdict: unsupported by any evidence found. Not refuted either.**

What the evidence says:
- **0 advertisers evidenced in 47 searches** (14 in T5, 33 in T18). No Ad Library listing, no ad screenshot, no buyer saying "I saw an ad" (T5, T18). Zero buyer quotes in both tracks.
- **The Ad Library was never opened.** WebFetch was blocked (STATUS.md, NETWORK-NOTES). So this is absence of search hits, not a clean negative. Weak.
- The Ad Library shows no spend for normal commercial ads and no results. Its API covers political ads plus UK/EU ads of any type for the past year, not US/CA/AU commercial ads (T5 #6, Meta help text). So even when opened, "ran 60+ days with many variants" is a weak proxy for profit.
- Lovable is itself a heavy Meta advertiser (1,079 ads, 304 active in one vendor snapshot, T18 #5). Platform ads compete for the same people. That is a point against cheap clicks, not for rescue ads.
- Sellers who talk about acquisition cite **word of mouth, networking, referrals and SEO content** (HN seller comment; QuickLaunch claim unconfirmed; RapidDev's 509-page hub) (T10, T18). One HN seller says SEO no longer works for pipeline. Both are anecdotes.
- Free audits are the common front door (MetaCTO 48 hours, McKelvey 20 minutes, ULAM, Chudovo, Agence Scroll) (T18 #7, T20 #19). That funnel shape suits paid lead gen, but nothing shows ads feed it.
- Nothing found about "close well". No close-rate figure exists for this niche. Vendor B2B close rates of 20 to 29% are from other fields.

What the arithmetic adds (section 1.4): Meta could work for sellers with a **bigger ticket**. A $10,000 to $15,000 project (Slopfix, McKelvey's $15,000 and up) can carry $3,000 to $4,000 of acquisition cost. At a $2,000 ticket the Mid case cannot. So the claim may be true for premium agencies and false for a $2,000 sprint. We cannot tell from Phase 1 which is behind the rumour.

What evidence would change the read:
1. **Open the Meta Ad Library in a browser** for UK and EU, where coverage is complete for any ad type over the past year. Zero rescue advertisers after the full term list (lovable, vibe coded, fix your app, MVP rescue, finish your app and so on) is a real negative. Three or more advertisers with the same ad running 60+ days and 5+ variants would be a moderate positive.
2. A rescue seller **naming a cost per lead, cost per call or close rate** from their own ads (a post-mortem, podcast or Indie Hackers post). The unopened QuickLaunch post is the nearest lead.
3. A **buyer** saying they found a rescue vendor through an ad.
4. Google Ads Transparency Center check for the same advertiser names (T6 did not run it).
5. Our own $2,500 test result (section 6). A booked-call cost at or below about $100 for 10 days would move the read toward supported.

---

## 6. $2,500 Meta test budget plan

### 6.1 Setup [A unless noted]

- **Market:** one country first, the US, so CPM stays stable. UK, AU and CA only after a pass. (CASL and Spam Act are not issues for ads, but keep one variable at a time.)
- **Campaign:** one campaign, one ad set per angle (2 ad sets), 4 ad variants. Ad copy uses buyer language from model/brand.md; angles to the paid audit, not "rescue" (T6 #14: "rescue" is a poor keyword; sellers use "fix", "cleanup", "audit").
- **Landing page:** one page, a calendar booking with three qualifying questions: which platform, is it live with users or revenue, budget range. This lowers lead count and lifts quality. Offer: $500 audit credited against the sprint, with a refund shape from model/risk.md.
- **Spend:** days 1 to 5 at **$100 a day** ($500), days 6 to 20 at **$133 a day** ($2,000). Total **$2,500 over 20 days**. Measure sprint conversions for 15 more days after spending stops (audits take about a week to deliver; sprint decisions come after).
- Cost not in the $2,500: landing page and creative build, lead-reviewer time on calls (7 to 25 calls at 45 minutes, about $15 each at $20/hour).

### 6.2 What to measure daily

| metric | why | green / amber / red |
|---|---|---|
| Spend, impressions, CPM | matches the $9 to $15 benchmark | CPM above $20 = amber |
| Link CTR | creative quality | below 0.5% = swap the ad |
| CPC | checks 1.1 flag | above $3 = swap the ad |
| Landing page views and bounce | page quality | 150+ clicks and 0 leads = fix page or tracking |
| Leads and **cost per lead** | the benchmark anchor | green at or below $60, amber to $110, red above $110 |
| Booked calls and **cost per booked call** | main kill metric | green at or below $100, amber $100 to $160, red above $160 |
| Quality of each lead (live app? users or revenue? budget at or above $1,500?) | right buyer, not just cheap | a lead only counts as "qualified" if all three |
| Show rate (calls held / booked) | benchmark 75 to 85% | below 60% = tighten reminders |
| Paid audits and cost per paid audit | the first revenue event | note each one by hand |
| Frequency | audience size too small | above 2.5 in week 1 = widen |

Where the booked-call thresholds come from (my arithmetic, section 1): from a booked call, show x close x audit-to-sprint is 0.123 in the High case and 0.070 in Mid. To keep a sprint client at or below $600 you need a booked call at or below **$74** (High) or $42 (Mid). To merely break even on the sprint's $1,322 gross profit you need at or below **$163** (High) or $93 (Mid). So above about **$160** per booked call, even the best case downstream cannot break even. Below about $100 starts to pass gate 2 on a net-of-audit basis if audit-to-sprint holds at 50%.

### 6.3 Expected results from $2,500 by case

| line | High | Mid | Low |
|---|---|---|---|
| Impressions | 277,778 | 208,333 | 166,667 |
| Clicks | 3,806 | 2,396 | 1,300 |
| Leads | 50 | 17.2 | 10 |
| Booked calls | 30 | 8.6 | 4 |
| Held calls | 25.5 | 6.9 | 3 |
| Paid audits | 7.4 | 1.7 | 0.6 |
| Audit revenue ($500 each) | $3,700 | $860 | $300 |
| Sprint clients | 3.7 | 0.6 | 0.12 |
| Chance of zero paid audits (Poisson) | 0.1% | 18% | 55% |

Formula: leads = 2,500 / CPL; each later line multiplies by that stage rate.

Important honesty: **$2,500 cannot prove a cost per sprint client.** Even in the High case it buys 3 to 4 sprint clients; in Mid, fewer than one. What it can do is tell you the cost per lead and per booked call within about plus or minus 30% (needs at least 10 to 15 leads), and whether any held call turns into a paid audit.

### 6.4 Kill and continue rules

| # | rule | trigger | reasoning |
|---|---|---|---|
| K1 | Pause an ad, not the test | by day 3 (about $300), CTR below 0.5% or CPC above $3 | creative problem, swap |
| K2 | **Stop** if cost per booked call is above **$160** over 10 days | measured at day 10 (about $1,170 spent) | above $160 even High-case downstream rates cannot break even on the sprint ($163) |
| K3 | **Stop** if leads are at least 8 and none is qualified | any time after 8 leads | wrong audience; cheap leads are worthless |
| K4 | **Stop** if there are fewer than 3 leads at $1,000 spent | day 10 | CPL above $330, worse than the Low case |
| K5 | Stop spending and rework the offer, not the ads | no paid audit after **$1,500** and at least 6 held calls | the problem is price, trust or offer, not traffic |
| K6 | Meta fails as modelled | zero paid audits at **$2,500** | still 18% likely if Mid is true, 0.1% if High is true, so it rules out High, not Mid |
| C1 | **Continue and scale** (second $2,500 at the same settings) | cost per booked call at or below **$100** for 10 days **and** at least 2 paid audits by day 20 | the only path to gate 2 on a net basis |
| C2 | Hold, no extra spend | booked call $100 to $160 | finish the 20 days, review audit-to-sprint, decide at day 35 |

Before spending: set the K-rules in the ad account and write the date and spend limit into a note. A dull test with fixed rules beats an exciting test that runs on hope.

---

## 7. Assumption register (what to test first)

| # | assumption | where used | source | test |
|---|---|---|---|---|
| 1 | Audit-to-sprint 20 / 35 / 50% | Meta, outbound | none (T16 #11: zero data) | first 10 paid audits |
| 2 | Lead-to-booked-call 40 / 50 / 60% | Meta | none | Meta test, day 1 |
| 3 | Click-to-lead back-solved to CPL | Meta | contradicts raw CPM x CTR x normal conv | Meta test |
| 4 | Sourced B2B CPL $50 / $145 / $250 | Meta | T18 vendors | Meta test |
| 5 | Show 75 to 85%, close 20 to 29% | Meta, outbound | T18 vendors, other niches | first 10 calls |
| 6 | Delivery hours and loading 1.5x | offer table | delivery.md; loading is mine | first 3 audits and sprints |
| 7 | Refund reserve 5% | offer table | none (risk.md: no data) | first 10 clients |
| 8 | Attach 0 / 20 / 40%, 6 months, 4 months | LTV | none (T14, T20: zero data) | first 5 rescues |
| 9 | Directory inquiries 1 / 3 / 8 a month | channel A | loosely Contra 234 hires / 171 experts | apply to Lovable, Contra and Base44 this week |
| 10 | Upwork win rate 2 / 6 / 12%, jobs 2 / 6 / 15 a month | channel B | none; vendor 43% win rate haircut | run 20 proposals, count |
| 11 | Upwork Connects $0.15 and fee 0 to 15% | channel B | [X] third-party blogs | check in an Upwork account |
| 12 | SEO, communities, outbound inputs | ranking | mostly none | do not rely on these until measured |

## 8. Gate 2 read from this file

**UNCLEAR, leaning against for Meta, leaning pass only for low-volume buyer-intent channels.**
- Meta at $2,000: only the High case ($419 net, $676 gross) approaches $600. Mid is 6x over, Low 33x.
- Directories and Upwork pass on paper at $425 to $470, but they depend on unsourced inputs and give about one client a month.
- Nothing has been measured. The fastest cheap tests are: apply to the three directories, send 20 Upwork proposals, ask existing Wanile clients for introductions, and open the Ad Library for UK/EU.

## 9. What I could not do

- Open the Meta Ad Library, Google Trends, Upwork or any listing page (tools blocked in Phase 1). Used 1 of 3 allowed WebSearch calls, for Upwork Connects and fee; third-party blogs only.
- model/offers.md was missing at start, so offer prices are the placeholders. If offers.md changes prices or hours, re-run section 2; sections 1 and 3 depend on price only through the $2,000 first project.
