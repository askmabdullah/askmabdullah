# Deep 04: Healthcare problem cards. (1) Fax and email referral/order intake at independent outpatient providers; (2) Denied and underpaid claims at independent physician and therapy practices and small billing companies

Research conditions (read first):
- Research date: 27 Oct 2026. US only, USD.
- One page fetch was tried early (hhs.gov HIPAA business-associate FAQ) and failed with "getaddrinfo ENOTFOUND". So every finding below comes from search-engine summaries of the cited pages, not from reading the full pages. Re-check numbers on the page before publishing.
- This researcher used exactly 30 web searches (the cap). It did not repeat searches from lens01, lens02, lens03 or lens09. Facts reused from those notes keep their original URLs and are marked "(first-round)".
- Labels: "vendor claim" = number from a company that sells a fix. "Estimate" = my math, shown, with assumptions marked. "Prior knowledge, not verified" = from model background knowledge, not checked this session. "Not found" = searched and not found.
- Problem 1 is called P1 (referral and order intake). Problem 2 is called P2 (denials, underpayments, eligibility and prior-auth follow-up).

**At a glance (details and sources in Q1–Q14)**

| | P1 Referral/order intake | P2 Denials and underpayments |
|---|---|---|
| Verdict | Weakened. Platforms (Brightree, WellSky) now bundle AI fax intake, and Medsender sells AI referral automation at $549/month. What is left is exception handling and missing-document chasing for practices not on those platforms | Still strong as a contingency or white-label wedge (aged denials plus underpayments). Weakened as a full-service billing offer, because Commure/Athelas, athenahealth and WebPT are moving into the same small-practice segment |
| Example labour (estimate) | $3.2K–$9.0K/month per site | $3.4K–$5.8K/month per 5-physician practice |
| Example money leak (estimate) | Lost referrals of $10K–$21K/month (weak, unverified per-referral value) | $9.6K–$22K/month (unworked denials plus underpayments) |
| Price anchors | $549/month for 200 referrals (software); $15–27/hour US intake staff; $5–12/hour offshore | 4–10% of collections; 25% contingency; $3–8 per claim; $10 per appeal |
| Biggest risk | Platform bundling, plus real-time US-hours work | Crowding, plus payer and Medicaid contract limits on offshore PHI |

---

## Q1. The exact task, in plain words

### Takeaway
P1: an intake coordinator opens a multi-page fax, finds the order, demographics, insurance and clinical notes, creates the patient and order in the EHR or billing system, checks eligibility and prior-auth needs, then phones or faxes the referring office for missing pieces. P2: a biller pulls each denial or short payment from the remittance, works out why, fixes and resubmits or writes an appeal, checks eligibility or auth status, chases the payer until paid, and compares payments against the contract to catch underpayments.

### Cited Findings
**P1**
- Home health and DME intake postings describe "collecting demographic and clinical information from clients, physicians office and other referral sources to compile referrals". Some DME roles add verifying insurance eligibility and following up on prior authorization requests (search summary of postings) — [ZipRecruiter DME intake](https://www.ziprecruiter.com/Jobs/Dme-Intake-Coordinator); [ZipRecruiter home health intake](https://www.ziprecruiter.com/Jobs/Home-Health-Intake-Coordinator/2)
- An HME intake specialist posting requires that "medical documentation that is required to establish medical necessity or to meet payer criteria is printed and readily available in the patient's medical record prior to billing" — [DCH Health System job post](https://careers-dchsystem.icims.com/jobs/10793/hme-intake-specialist/job)
- A home health documentation article says intake staff are responsible for "training referral sources regarding the level of documentation your agency needs" — [AAPC article](https://aapc.com/codes/scc_articles/article_pdf/72/documentation-does-your-intake-process-need-updating-140580)
- A vendor-style page lists the intake loop: review faxed documents, enter data into several systems, call referral sources, verify insurance, track missing paperwork (search summary; page not tied) — [HME News intake tag](https://www.hmenews.com/tag/intake)
- Brightree's own description of what its AI automates: read and classify referral faxes, extract data, create patient records and sales orders, match patients, check eligibility automatically — [Brightree IDA](https://www.brightree.com/brightree-intelligent-document-automation/)
- Tennr describes referrals arriving by fax, email or e-portal, "often requir[ing] hours of manual review and back-and-forth communication" (first-round) — [HIT Consultant](https://hitconsultant.net/2025/06/18/tennr-raises-101m-to-solve-healthcares-patient-referral-black-hole/)

**P2**
- First-round task description (lens02): pull the denial or underpayment from the ERA/835, read the reason code, check eligibility, auth and coding, compare the paid amount against the contract fee schedule, fix and resubmit or appeal with records, track to payment — [lens02 notes, sourced to Experian and Premier](https://www.businesswire.com/news/home/20250922969006/en/Experian-Health%E2%80%99s-3rd-Annual-State-of-Claims-Survey-Finds-Denials-Still-on-the-Rise-Amid-Escalating-Challenges)
- About 90% of denials are reworked with at least some human review (Experian Health State of Claims 2025) — [Fierce Healthcare](https://www.fiercehealthcare.com/providers/experian-study-providers-say-claims-denials-continue-rise); [HMP Global](https://www.hmpgloballearningnetwork.com/site/ihe/news/claim-denials-increasing-providers-struggle-staffing-and-data-issues-survey-finds)
- Underpayments "hide inside zero-balance claims", meaning they look paid and closed (vendor) — [PayerPrice](https://payerprice.com/blog/underpayment-detection)
- Underpayment software works this way: load payer contracts into a contract library, then check each payment against the fee schedule by procedure and diagnosis code — [RevFind on GetApp](https://www.getapp.com/all-software/a/revfind/)

### Inferences
- P1 card wording: "An intake coordinator reads a 10–40 page fax. They find the order or prescription, face sheet, insurance card and clinical notes. They create the patient and order in Brightree, WellSky or the EHR, run eligibility, check the payer's documentation rules (for example face-to-face notes or a signed order), fax or call the referring office for the missing signature or notes, and then hand the case to scheduling or delivery."
- P2 card wording: "A denial specialist opens today's ERAs. They sort denials by reason (eligibility, auth, coding, medical necessity, timely filing), correct and resubmit the easy ones, pull records and write appeals for the rest, call or check portals for status, and once a month compare paid amounts with each payer's contracted rate to find short payments."

### Gaps
- No time-and-motion study for either task was found. Minutes per step are estimates (see Q3).

---

## Q2. Who feels it (job title) and who approves the money (job title)

### Takeaway
P1: felt by intake coordinators, intake specialists and referral coordinators; approved by the DME owner or general manager, the home health administrator or director of operations, or the practice administrator. P2: felt by billing managers, denial specialists and AR follow-up reps; approved by the practice administrator, owner physician or CFO, or by the owner of the billing company.

### Cited Findings
- Job titles found in live postings: "Home Health Intake Coordinator", "DME Intake Coordinator", "Senior Intake Coordinator", "HME Intake Specialist" — [ZipRecruiter](https://www.ziprecruiter.com/Jobs/Home-Health-Intake-Coordinator/2); [Virtual Vocations](https://www.virtualvocations.com/job/senior-intake-coordinator-3143120-i.html); [DCH](https://careers-dchsystem.icims.com/jobs/10793/hme-intake-specialist/job)
- P2 job titles found: "Denial Management Specialist" (BrightSpring/Amerita), "Accounts Receivable Denials Specialist" (AnswersNow), "Accounts Receivable (AR) Caller" (AllCare Therapies) — [BrightSpring](https://careers-brightspring.icims.com/jobs/192000/denial-management-specialist---remote/job); [AnswersNow via Techstars jobs](https://jobs.techstars.com/companies/getanswersnow-com/jobs/65416447-accounts-receivable-denials-specialist); [SmartRecruiters AllCare](https://www.smartrecruiters.com/AllCareTherapies/744000052723834-accounts-receivable-ar-caller)
- In DME, billing companies also run intake. ACU-Serve (an HME billing company) hired a director of intake who "already manages a staff of about 50 intake and document management staff" (2019) — [HME News intake tag](https://www.hmenews.com/tag/intake)
- MGMA Stat polls are answered by "medical group leaders", meaning practice administrators and executives (first-round) — [MGMA](https://mgma.com/mgma-stat/strategic-improvements-in-your-rcm-to-reduce-your-practices-claim-denials)

### Inferences
- Approver titles are inferred from org structure. No source states who signs these purchases.
- In P2, the billing company is both a competitor and a channel: its owner or COO buys white-label denial and underpayment capacity.
- In DME, the intake budget can sit at a billing company (ACU-Serve shows intake is already bought as an outsourced service).

### Gaps
- No buyer-side survey of who approves intake or denial-recovery purchases was found.

---

## Q3. How often it happens and how many hours it eats (math shown)

### Takeaway
Both tasks happen every business day. A mid-size independent DME supplier handling about 150 orders a week needs about 1.9 FTE of intake. A 4-physician specialty practice with about 60 referrals a week needs about 0.9 FTE. A 5-physician practice submitting about 500 claims a week sees about 40–50 denials a week, which with status follow-up takes about 0.85 FTE. All volumes are estimates built on the few sourced throughput figures.

### Cited Findings
- Manual intake throughput is under 100 orders per FTE per week, versus about 300 with Tennr (vendor claim, first-round) — [Tennr benchmark via finanzen.net](https://www.finanzen.net/nachricht/aktien/independent-healthcare-providers-already-operate-on-thin-margins-where-every-dollar-counts-tennr-s-benchmark-report-reveals-they-lose-10-of-their-revenue-every-year-to-preventable-paperwork-mistakes-14933837)
- 52% of faxes need staff intervention and manual processing; 35% of inbound documents are still faxes (vendor survey, Oct 2025, first-round) — [Documo via BusinessWire](https://www.businesswire.com/news/home/20251015114710/en/88-of-Healthcare-Practitioners-Say-Fax-Related-Delays-Impact-Patient-Care-New-Survey-Finds)
- A manual eligibility verification takes up to 24.36 minutes and $14.32 for specialists and behavioural health (2023 CAQH Index, secondary, first-round) — [ASP RCM white paper](https://asprcmsolutions.com/whitepapers/eligibility-first-revenue-defense/)
- First-submission denial rate for single-specialty groups: 8% (MGMA DataDive 2023, older, first-round) — [MGMA](https://mgma.com/mgma-stat/strategic-improvements-in-your-rcm-to-reduce-your-practices-claim-denials); 41% of providers have denial rates of 10% or more (Experian 2025) — [Business Wire](https://www.businesswire.com/news/home/20250922969006/en/Experian-Health%E2%80%99s-3rd-Annual-State-of-Claims-Survey-Finds-Denials-Still-on-the-Rise-Amid-Escalating-Challenges)
- A successful appeal can take 30 to 90 days even after the denial is overturned (CorroHealth executive at a Becker's event; the summary did not tie the quote to one of these Becker's pages) — [Becker's A](https://www.beckershospitalreview.com/finance/denials-to-dollars-how-health-systems-can-fight-back-and-protect-revenue); [Becker's B](https://www.beckershospitalreview.com/finance/less-frustration-more-revenue-how-hospital-leaders-are-confronting-denials-with-technology)
- Rework cost per denied claim is $25–$118 (attributed to MGMA by a vendor blog; not verified). The same blog says only 35–50% of denials get appealed at small practices (vendor claim) — [BAM AI blog](https://bam-ai-site.pages.dev/blog/ai-denial-management-small-practices.html)

### Inferences (estimates, math shown)
**P1-A, independent DME/HME supplier (assumption: 150 new orders a week)**
- Keying at 24 minutes per order (40 hours × 60 ÷ 100 orders, from the Tennr manual benchmark): 150 × 24 min = 60 hours a week.
- Missing-document chase (assumption: 40% of orders incomplete, a figure set below Documo's 52% "need manual processing"; 15 minutes of calls and faxes each): 150 × 0.4 × 15 = 15 hours a week.
- Total: about 75 hours a week ≈ 1.9 FTE ≈ 325 hours a month (× 4.33).

**P1-B, independent 4-physician specialty practice (assumption: 60 referrals a week)**
- 30–45 minutes per referral, including eligibility and benefits (CAQH puts manual verification alone at up to 24 minutes). At the midpoint of 37.5 minutes: 60 × 37.5 = 37.5 hours a week ≈ 0.94 FTE ≈ 162 hours a month.

**P2, independent 5-physician practice (assumptions: 20 encounters per physician per day, 1 claim per encounter, 5 days a week)**
- Claims: 5 × 20 × 5 = 500 a week ≈ 2,167 a month.
- Denials at 8–10%: 40–50 a week ≈ 173–217 a month.
- Work time (assumption: 30 minutes per denial to research, correct or appeal): 217 × 0.5 = 108 hours a month.
- Status follow-up (assumption: 10% of claims need a status check at 10 minutes): 217 × 10 min ≈ 36 hours a month.
- Total ≈ 145 hours a month ≈ 0.85 FTE (at 173 hours per FTE-month).
- **Small billing company (assumption: 30 such clients): about 25 FTE-months of denial and AR work.** This is why billing companies are a channel.

### Gaps
- No sourced minutes-per-denial or minutes-per-referral figure from an independent study. Referral volumes per practice type were not found.

---

## Q4. What it costs a typical practice in dollars per month (math shown)

### Takeaway
P1: labour is about $3K–$9K a month per site. The larger but weaker-evidenced cost is lost referrals ($10K–$21K a month for a specialty practice, if one accepts an unverified $800-per-lost-referral figure) and intake-driven denials. P2: labour is about $3.4K–$5.8K a month, and the money left on the table is about $9.6K–$22K a month for a 5-physician practice (unworked denials plus underpayments).

### Cited Findings
- Home health intake coordinator pay averages $21.23/hour (most $17.31–$23.56), as of 15 Jun 2026 — [ZipRecruiter](https://www.ziprecruiter.com/Jobs/Home-Health-Intake-Coordinator/2); Payscale gives a $15.00 average (about $13–$17), undated — [Payscale](https://www.payscale.com/research/US/Job=Home_Health_Intake_Coordinator/Hourly_Rate)
- Remote denial specialist pay: $18–$22/hour (BrightSpring/Amerita); $25–$28/hour contract (AnswersNow, posted 17 Jan 2026); ZipRecruiter averages range from $20.97 to $30.69 depending on the search term — [BrightSpring](https://careers-brightspring.icims.com/jobs/192000/denial-management-specialist---remote/job); [AnswersNow](https://jobs.techstars.com/companies/getanswersnow-com/jobs/65416447-accounts-receivable-denials-specialist); [ZipRecruiter remote denial management](https://www.ziprecruiter.com/Jobs/Remote-Denial-Management); [ZipRecruiter remote denials management](https://www.ziprecruiter.com/n/Remote-Denials-Management-Jobs-Near-Me)
- Lost-referral value: $800–$3,000 per dropped patient (attributed to HFMA) and $800–$1,500 (attributed to MGMA). Neither attribution could be traced to a primary report; these are vendor blogs — [BD Emerson](https://www.bdemerson.com/article/referral-leakage-statistics); [ScribeEMR](https://www.scribeemr.com/what-is-referral-leakage-revenue-loss/). Leakage of 20–65% by service line (vendor summary) — [Documo](https://www.documo.com/?p=10193)
- Tennr's benchmark says independent providers lose over 10% of revenue, "or $2.2M", every year to claim denials tied to referral intake (vendor claim) — [HIT Consultant](https://hitconsultant.net/?p=91617)
- Top denial causes: missing or inaccurate data 50%, authorizations 35%, registration errors 32% (Experian 2025, first-round) — [Business Wire](https://www.businesswire.com/news/home/20250922969006/en/Experian-Health%E2%80%99s-3rd-Annual-State-of-Claims-Survey-Finds-Denials-Still-on-the-Rise-Amid-Escalating-Challenges)
- 54.3% of hospital denials were eventually overturned (Premier, 2022 claims, published 2024, first-round) — [Fierce Healthcare](https://www.fiercehealthcare.com/providers/providers-wasted-106b-2022-overturning-claims-denials-survey-finds); an AI appeals vendor's calculator assumes a 57% overturn rate (vendor) — [NoNos](https://nonos.pages.dev/)
- Underpayments: 1–11% of net revenue (vendor, first-round) — [HelpSquad](https://helpsquad.com/blog/beyond-denials-how-outsourced-payer-underpayment-recovery-finds-revenue-your-denial-reports-miss/); 5–7% of net revenue for physician groups (vendor, attributed to MGMA, not verified) — [PayerPrice](https://payerprice.com/blog/underpayment-detection)
- 24% of denied claims are never recovered and 95% are preventable (vendor claim) — [Knack RCM](https://knackrcm.com/?p=2731)

### Inferences (estimates, math shown)
**P1 labour** (loaded rate = wage × 1.3 for taxes and benefits; the 1.3 is an assumption)
- P1-A DME: 325 hours a month × $19.50 (Payscale $15 × 1.3) to $27.60 (ZipRecruiter $21.23 × 1.3) = **$6.3K–$9.0K a month**.
- P1-B specialty: 162 hours a month × $19.50–$27.60 = **$3.2K–$4.5K a month**.
- Labour per referral: 24 minutes × $19.50–$27.60 per hour ≈ **$7.80–$11.04 per referral** before chasing.

**P1 lost referrals (weak evidence)**
- P1-B: 60 × 4.33 = 260 referrals a month. If 5–10% are lost to slow or incomplete intake (assumption), that is 13–26 lost × $800 (low end of the unverified figure) = **$10.4K–$20.8K a month** in lost visit revenue. For DME, revenue per order was not found, so no DME figure is given.

**P1 intake-driven denials**
- Taking Tennr's 10% at face value for a $4M-revenue supplier (assumption) gives $400K a year ≈ $33K a month. This is a vendor claim and likely overstated. At 3% (assumption) it is about $10K a month.
- Tennr's "10% = $2.2M" implies its benchmark population averages about $22M a year in revenue (inference). Those are larger independents than the small shops in scope here.

**P2 (same 5-physician practice as Q3; assumption: average paid per claim of $120, giving 26,000 claims × $120 ≈ $3.1M a year ≈ $260K a month in collections)**
- Denied value: 217 × $120 ≈ $26K a month (at 10%); $20.8K a month (at 8%).
- Left on the table: if 50–65% of denials are never worked (from the vendor's "35–50% appealed") and 54% of those were winnable: $26K × 0.50–0.65 × 0.54 = **$7.0K–$9.1K a month** (about $84K–$110K a year).
- Underpayments at 1–5% of collections: **$2.6K–$13K a month**.
- **Total leak ≈ $9.6K–$22K a month.** Labour to work everything: 145 hours × $23.40–$40.30 (the $18–$31/hour range × 1.3) ≈ **$3.4K–$5.8K a month**.
- Comparison: the practice already pays a full-service billing company 4–10% of collections, which is $10.4K–$26K a month (see Q5).
- Service revenue at 25% contingency: 25% × $9.6K–$22K = **$2.4K–$5.5K a month per practice**, if all of it is recovered (upper bound).

### Gaps
- No independent per-referral revenue value for DME, PT, sleep or imaging. Average paid per professional claim was not searched; $120 is an assumption.

---

## Q5. How practices handle it today and what they pay

### Takeaway
P1 is mostly in-house intake staff ($15–$27/hour in the US), sometimes a DME billing company's intake team, offshore VAs at $5–12/hour, or software (Medsender, Brightree, WellSky, Tennr). P2 is mostly a full-service billing company at about 4–10% of collections (most small practices pay 5–8%; complex specialties 10–12%), in-house billers, offshore India or Philippines teams at about $5–12/hour, or contingency denial firms at about 25% of what they recover.

### Cited Findings
**P2 pricing**
- Billing company fees across 2026 pricing guides: 4–10% of net collections; most small and mid-size quotes are 5–8%; cardiology, oncology and orthopedic surgery reach 10–12%. Per-claim pricing is $3–$8. Flat monthly fees run $500–$2,500 for small to mid-size practices. Hidden fees can add 10–30% to the effective rate. Some vendors charge on gross charges rather than net collections. These are vendor or lead-gen guides; the summary did not tie each number to one page — [Neolytix](https://neolytix.com/articles/what-is-the-going-rate-for-medical-billing-services/); [Carepatron](https://www.carepatron.com/blog/how-much-do-medical-billing-services-cost/); [Helpware](https://helpware.com/blog/medical-billing-outsourcing); [NuGenera](https://nugenera-health.lovable.app/blog/medical-billing-outsourcing-cost-2026); [RCM Intel](https://rcmintel.pages.dev/blog/how-much-does-medical-billing-service-cost/)
- Other ranges: 4–9% of collections — [Outsource Accelerator](https://www.outsourceaccelerator.com/?p=164021); budget providers 2–5% versus premium 6–14%, with premium firms offering dedicated denial teams and appeals — [RCM Intel](https://rcmintel.pages.dev/blog/are-cheap-medical-billing-services-worth-it/)
- Contingency denial recovery: 25% of recovered revenue, nothing owed if nothing is recovered (PT and mental health focus, vendor) — [Relvio](https://relvio-health.pages.dev/); 25% with no setup fees or contracts (vendor) — [NoNos](https://nonos.pages.dev/)
- Medicare recovery audit contractors earn about 8–9% of what they recover — [AAPC newsletter](https://aapc.com/codes/coding-newsletters/my-homecare-week-alert/audits-racs-get-8-of-every-denial-they-make-156734-article); older RAC base fees were 9–12.5% (14–17.5% for DME) (first-round) — [CPBJ](https://www.cpbj.com/cms-we-have-a-recovery-audit-contractor-problem)
- Offshore India: one vendor's billers start "from $7 per hour", with hourly, FTE, % of collections or % of invoice pricing. Indian BPO coding runs $3–$7 per claim. An Upwork listing offers 40 hours for $200 (about $5/hour). The summary did not tie the $7 and $3–$7 figures to a specific page among these — [Upwork listing](https://www.upwork.com/services/product/admin-customer-support-complete-medical-billing-accounts-receivables-and-payment-posting-services-1604985890695888896); [4D Global](https://4dglobalinc.com/?p=27389); [SunTec India](https://www.suntecindia.com/accounts-receivable-follow-up-services.html); [Virtual Employee](https://www.virtualemployee.com/services/medical-process-outsourcing/outsource-revenue-cycle-management)
- Philippines: medical billing VA $5–$12/hour; full-time benefits-verification and prior-auth role PHP 30,000–33,000 a month (first-round) — [HireTalent.ph](https://hiretalent.ph/skill/medical-billing-support); [Remotive/SuperStaff](https://remotive.com/remote/jobs/medical/medical-billing-assistant-4677268)
- US billing staff turnover is 20–30% a year, at $24K–$36K per replacement (vendor estimate; the summary did not confirm which offshore vendor page) — [4D Global](https://4dglobalinc.com/?p=27389)

**P1**
- US intake pay: $15–$27/hour (see Q4). Postings: Oklahoma City $16.75–$22.75; Concord, CA $19.75–$27; DME in Salida, CA $21–$26; Vestavia Hills, AL $17.75–$23.75 (search summary of ZipRecruiter postings) — [ZipRecruiter DME intake](https://www.ziprecruiter.com/Jobs/Dme-Intake-Coordinator); [ZipRecruiter home health intake](https://www.ziprecruiter.com/Jobs/Home-Health-Intake-Coordinator/2)
- Medsender software: AI Fax Automation $299/month, AI Referral Automation $549/month, AI Call Automation $2,249/month, flat monthly — [Capterra](https://www.capterra.com/p/215989/Medsender/pricing/); the $549 tier includes 200 referrals a month plus about 3,000 fax pages — [Xpay index](https://www.xpay.sh/agent-ready-index/medsender/)
- DME billing companies sell intake (ACU-Serve, about 50 intake staff, 2019) — [HME News](https://www.hmenews.com/tag/intake)
- Darby launched "Smart Intake", which pulls data points from scanned medical documentation so intake staff can move them into billing software; two providers were live (date not visible) — [HME News](https://www.hmenews.com/article/darby-fuels-referrals)

### Inferences
- Medsender at $549 for 200 referrals ≈ **$2.75 per referral** (estimate) for software that a practice still has to supervise. In-house labour is about $7.80–$11.04 per referral (Q4). A human-in-the-loop service priced at roughly $4–$8 per referral would sit between the two (inference, untested).
- In P2, buyers already pay for denial work inside the 4–10% fee. A new service must either be priced as recovery the billing company is not achieving (contingency on aged or unworked items and underpayments) or sold white-label to the billing company.

### Gaps
- Per-referral pricing from outsourced intake firms was not found. Tebra and AdvancedMD bundled billing-service prices were not found.

---

## Q6. Proof: quotes, surveys and job posts

### Takeaway
Survey evidence is strong for P2: the January 2026 MGMA Stat poll ranks denials and appeals as the biggest revenue leak (48%). Direct practice-manager quotes are scarce in search results for both problems. Job posts confirm the work is paid and recurring: intake $15–$27/hour, denial specialists $18–$46/hour.

### Cited Findings
**Surveys and polls**
- MGMA Stat poll, 6 Jan 2026, 288 responses: 48% said "denials and appeals" was the biggest leak in their revenue cycle; front-end issues such as eligibility came next at 23% — [Physicians Practice, 20 Jan 2026](https://www.physicianspractice.com/view/mgma-poll-denials-are-biggest-revenue-cycle-leak-for-medical-practices)
- MGMA regulatory survey: 89% rate prior authorization very or extremely burdensome; 97% say patients have had delays or denials of medically necessary care because of prior auth (report year unclear in the summary) — [Becker's](https://www.beckershospitalreview.com/finance/prior-authorizations-are-top-burden-for-medical-groups-mgma.html); [Becker's ASC](https://www.beckersasc.com/asc-news/the-regulatory-burdens-crushing-physicians/)
- MGMA Stat (Dec 2020, older): 42% named prior authorization as the top denial reason — [MGMA Stat](https://www.mgma.com/stat-120120)
- Experian 2025: 54% say claim errors are rising; 68% say clean claims are harder than a year ago; 43% are understaffed; about 90% of denials get human rework; 67% think AI can help — [Fierce Healthcare](https://www.fiercehealthcare.com/providers/experian-study-providers-say-claims-denials-continue-rise); [Experian newsroom](https://experianplc.com/newsroom/press-releases/2025/experian-health-s-3rd-annual-state-of-claims-survey-finds-denial). **No 2026 State of Claims edition was found** as of this search. Experian's Dec 2025 outlook says denials stay a top 2026 challenge — [Business Wire, 15 Dec 2025](https://www.businesswire.com/news/home/20251215116962/en/Outlook-for-2026-Experian-Health-Releases-Revenue-Cycle-Management-Predictions)
- Fax: 88% of practitioners say fax delays affect patient care (vendor survey, Oct 2025, first-round) — [Documo via BusinessWire](https://www.businesswire.com/news/home/20251015114710/en/88-of-Healthcare-Practitioners-Say-Fax-Related-Delays-Impact-Patient-Care-New-Survey-Finds)

**Quotes and close paraphrases (none from small-practice managers)**
- CorroHealth denial executive: "Even when you do get that denial overturned, a successful appeal can take 30 to 90 days." (Becker's event; page not pinned) — [Becker's](https://www.beckershospitalreview.com/finance/denials-to-dollars-how-health-systems-can-fight-back-and-protect-revenue)
- Five ASC executives told Becker's that payer behaviour has become "more aggressive, automated and less collaborative". One CEO reported about a 60% increase in down-coding, denials and delayed payments, mostly from Medicare Advantage plans (paraphrase) — [Becker's ASC](https://www.beckersasc.com/?p=98908)
- Sponsored Becker's piece (2026): denials were "a downstream problem handled by appeals teams that are armed with spreadsheets and overtime hours" (sponsored content) — [Becker's](https://www.beckershospitalreview.com/hospital-management-administration/2026-wake-up-call-denials-prevention-is-now-a-c-suite-responsibility/)
- A congressional critic of the WISeR AI prior-auth model said the administration "decided to use big tech and give them a contract to deny claims to seniors" (speaker not named in the summary) — [Medical Economics, 21 Jan 2026](https://www.medicaleconomics.com/view/wiser-spending-or-unneeded-delays-in-health-care-prior-authorizations-ai-in-medicare-prompt-concerns)
- Darby's CEO described Smart Intake as a way to speed up existing intake workflows rather than change them (paraphrase) — [HME News](https://www.hmenews.com/article/darby-fuels-referrals)

**Job posts with pay (see Q4 and Q5 for full lists)**
- Remote Senior Intake Coordinator, Mon–Fri 12:00 PM–8:30 PM EST, hourly (pay not shown) — [Virtual Vocations](https://www.virtualvocations.com/job/senior-intake-coordinator-3143120-i.html)
- Denial Management Specialist, remote, $18–$22/hour — [BrightSpring](https://careers-brightspring.icims.com/jobs/192000/denial-management-specialist---remote/job); AR Denials Specialist, $25–$28/hour, 17 Jan 2026 — [AnswersNow](https://jobs.techstars.com/companies/getanswersnow-com/jobs/65416447-accounts-receivable-denials-specialist); Kirkland, WA $28.83–$46.14/hour (Washington-only remote, 5 years' experience) and Quincy, MA $60K–$65K (search summary of ZipRecruiter) — [ZipRecruiter](https://www.ziprecruiter.com/Jobs/Remote-Denials-Management/2)

### Inferences
- The best P2 proof is the MGMA January 2026 poll plus Experian's "90% human rework". For P1, the proof is mainly job posts and vendor surveys.

### Gaps
- No Reddit (r/medicalbilling), AAPC forum, Facebook-group or podcast quotes from small-practice managers or DME intake leads were retrieved. Reddit and full pages could not be opened, and the search budget was spent on pricing and compliance. Next step: manually collect 10 quotes from the AAPC forums, r/medicalbilling, r/physicaltherapy and the HME News comment sections.

---

## Q7. Who else sells a fix, at what price, for what customer size, and how crowded

### Takeaway
P1 is now crowded at the platform layer. Brightree (DME) and WellSky (home health) ship AI fax intake inside their systems, Medsender sells $299–$549/month AI fax and referral tiers to small practices, and Tennr sells enterprise contracts to specialty clinics and ambulatory groups. P2 is very crowded: about 2,000 billing companies, offshore firms, Commure/Athelas (which does serve independent physician and therapy practices), athenahealth and WebPT native denial AI, AKASA (health systems), and small AI appeal tools at $10 per appeal or 25% contingency. No vendor published minimum contract sizes.

### Cited Findings
**P1 sellers**
| Seller | What | Price | Customer size | Source |
|---|---|---|---|---|
| Tennr | AI referral and order intake; DME/HME product | Quote-only, "enterprise pricing"; G2 shows no price | Core customers are specialty clinics and ambulatory provider groups; benchmark implies about $22M-revenue providers (inference) | [G2](https://www.g2.com/products/tennr/pricing); [AI for Medical, May 2026](https://aiformedical.pages.dev/products/tennr/); [ToolDirectory, May 2026](https://tooldirectory.ai/tools/tennr); [Tennr DME](https://tennr.com/lp/for-dme-hme) |
| Medsender | AI fax, referral and call automation | $299 / $549 (200 referrals) / $2,249 per month, flat | Small practices; FitGap says practices without IT may need vendor services | [Capterra](https://www.capterra.com/p/215989/Medsender/pricing/); [Xpay](https://www.xpay.sh/agent-ready-index/medsender/); [FitGap](https://us.fitgap.com/products/044989/medsender) |
| Brightree Intelligent Document Automation | AI classifies referral faxes, extracts data, creates patients and sales orders, auto-eligibility | Not found | Brightree DME/HME customers | [Brightree](https://www.brightree.com/brightree-intelligent-document-automation/); [Brightree handout](https://info.brightree.com/rs/963-ASR-132/images/BT-Intelligent-Document-Automation-hndt.pdf) |
| WellSky CarePort Referral Intake / Enterprise Referral Manager | AI summaries of referral packets including eFax (late 2025); AI completeness scoring with human oversight (Jan 2026) | Not found | Home health, hospice, post-acute | [HomeCare Magazine](https://www.homecaremag.com/news/wellsky-launches-ai-powered-careport-referral-intake-solution); [HME News](https://www.hmenews.com/article/wellsky-launches-next-generation-intake-solution-enhanced-with-ai); [Business Wire, Jan 2026](https://www.businesswire.com/news/home/20260127232204/en/WellSky-Launches-New-AI-Capabilities-to-Automate-and-Scale-Referral-Intake) |
| Darby Smart Intake | Pulls data from scanned documents into billing software | Not found | HME; 2 providers live (date unknown) | [HME News](https://www.hmenews.com/article/darby-fuels-referrals) |
| Assort Health | Voice, text and web agents incl. referrals; $76M Series B, Sep 2025 | Not found | Specialty practices | [Fierce Healthcare](https://www.fiercehealthcare.com/ai-and-machine-learning/assort-health-brings-total-funding-102m-four-months) (first-round) |
| DME billing companies (e.g., ACU-Serve) | Outsourced intake staff | Not found | DME/HME | [HME News](https://www.hmenews.com/tag/intake) |

**P2 sellers**
| Seller | What | Price | Customer size | Source |
|---|---|---|---|---|
| AKASA | AI RCM | Not found | Health systems and academic centres (Cleveland Clinic, Duke, Stanford, Johns Hopkins); customers total $120B+ net patient revenue | [Built In LA](https://www.builtinla.com/company/akasa); [Village](https://village.ai/company/akasahealth) |
| Infinitus | AI voice agents for benefits and payer calls | Not found | ASCs, health systems, labs, pharma patient support, specialty pharmacy | [CB Insights](https://www.cbinsights.com/company/infinitus-systems/customers) |
| Commure (merged with Athelas, Oct 2023, $6B) | Full RCM service | Not published | **Independent physician and therapy practices**: case studies include an orthopedics group (1.9% denial rate), South Valley ENT, Hillside Foot & Ankle (+$3.6M/year) and Meier Marsh Professional Therapies (vendor claims) | [Athelas merger](https://athelas.com/insights/athelas-commure-merging-to-create-a-6b-healthcare-infrastructure-company); [Ortho case](https://www.athelas.com/case-studies/ortho-plus-athelas-case-study); [South Valley ENT](https://www.athelas.com/case-studies/south-valley-ent); [Hillside](https://athelas.com/case-studies/rcm-case-study-podiatry-clinic-collections-growth); [Meier Marsh](https://athelas.com/case-studies/meier-marsh-professional-therapies-shhkn) |
| athenahealth (June 2026) | 80+ AI features; Denial Resolution Automation generates corrections for coding denials and claims a 30% increase in recovered payments (vendor claim); expanding through 2026 to automated resubmission, payer-portal appeals, and appeal-vs-resubmit advice | In athenaOne | athenaOne practices | [Business Wire, 3 Jun 2026](https://www.businesswire.com/news/home/20260603429867/en/); [TechTarget](https://www.techtarget.com/revcyclemanagement/news/366643899/Athenahealth-unveils-over-80-revenue-cycle-AI-features) |
| WebPT (July 2026) | "Next generation of AI-powered RCM for rehab therapy"; RCM services claim 80% fewer denials and rejections (vendor claim) | Not found | PT/OT/SLP practices | [Webull/press release](https://www.webull.com/news/15225550655022080); [WebPT denials guide](https://www.webpt.com/downloads/a-practical-guide-to-denials-prevention-and-management-in-rehab-therapy) |
| MD Clarity RevFind | Underpayment detection against loaded contracts; integrates athenahealth, ModMed, eClinicalWorks, NextGen | Not found | Specialty groups and MSOs up to hospitals | [GetApp](https://www.getapp.com/all-software/a/revfind/); [Software Advice AU](https://www.softwareadvice.com.au/software/560420/RevFind) |
| Fight Paperwork | AI appeals | $25/month per practice + $10 per appeal (after a 30-day trial) | Small practices | [Journal of Cyber Policy](https://journalofcyberpolicy.com/?p=310643) |
| NoNos AI / Relvio | Denial recovery | 25% contingency, no setup or contract | Small practices; PT and mental health (Relvio) | [NoNos](https://nonos.pages.dev/); [Relvio](https://relvio-health.pages.dev/) |
| Undenied | AI appeal pipeline | $49–$299 per appeal (search summary; page attribution not confirmed, and it may target patients) | Not clear | [PYMNTS 2026](https://www.pymnts.com/artificial-intelligence-2/2026/insurance-denials-meet-their-match-in-ai-powered-appeals/) |
| Billing companies | Full-service | 4–10% of collections | All sizes; HBMA typical member firm has 40–50 staff | See Q5; [HBMA](https://www.hbma.org/downloads/HBMA_Membership11.pdf) |

### Inferences
- **The "underserved by funded startups" claim holds for AKASA and Infinitus (enterprise and pharma), Tennr (larger ambulatory groups), and probably SmarterDx (hospital coding, prior knowledge, not verified). It does not hold for Commure/Athelas.** Athelas publicly sells full RCM to independent orthopedics, ENT, podiatry and therapy practices.
- EHR-native features hit the "easy" half. Athena covers coding denials first, and Brightree and WellSky cover clean fax extraction. What is left is medical necessity, auth and timely-filing appeals, contract underpayments, missing-document chasing, and practices on smaller or older systems.
- Crowding: P1 is high at the platform layer and medium for services. P2 is very high for services and medium for contingency underpayment audits at small practices.

### Gaps
- Thoughtful AI, SmarterDx and Hello Patient target customers and prices: not found (searched once, no results).
- No minimum contract size was found for any vendor.
- AdvancedMD's Waystar-powered denial prioritisation and appeal templates appeared in one undated result without a citable URL. Tebra's AI denial features: not found. eClinicalWorks and ModMed fax and denial AI: not searched (budget).

---

## Q8. Will the problem grow or shrink as AI improves over 24 months?

### Takeaway
P1: the basic data entry will shrink fast, because extraction is being bundled into Brightree and WellSky and sold for $299–$549/month. Fax itself will persist, since CMS-0057-F targets payer prior-auth APIs, not provider-to-provider referrals. Work that remains: exceptions, missing documents and payer documentation rules, which WISeR's new prior auth in six states increases for some DME items. P2: volume grows as payers automate (WISeR, MA plans), while EHRs absorb coding-type denials. Complex appeals and underpayment recovery should grow.

### Cited Findings
- CMS-0057-F: prior-auth decision times (7 calendar days standard, 72 hours expedited), specific denial reasons and annual metrics apply from 1 Jan 2026. The Prior Authorization, Patient Access, Provider Access and Payer-to-Payer APIs are due 1 Jan 2027. It covers MA, Medicaid/CHIP FFS and managed care, and FFE QHP issuers, not traditional Medicare or most commercial group plans. Providers have no direct compliance obligation — [CMS fact sheet](https://cms.gov/newsroom/fact-sheets/cms-interoperability-prior-authorization-final-rule-cms-0057-f); [Innovaccer](https://innovaccer.com/resources/blogs/cms-0057-prior-authorization-rule-requirements-deadlines-apis-and-operational-impact)
- WISeR: a six-year CMS Innovation Center model started January 2026. It adds AI-assisted prior auth to traditional Medicare in Arizona, New Jersey, Ohio, Oklahoma, Texas and Washington, for services such as skin substitutes, electrical nerve stimulators and knee arthroscopy. A licensed clinician must sign off before a denial. H.R. 6361 ("Ban AI Denials in Medicare Act", 2 Dec 2025) seeks to stop it (status not confirmed) — [Georgetown CHIR](https://medicare.chir.georgetown.edu/new-cms-wiser-model-revives-concerns-of-prior-authorization-and-artificial-intelligence/); [DLA Piper, 14 Jan 2026](https://www.dlapiper.com/en-at/insights/publications/2026/01/cms-wiser-model); [PYMNTS](https://www.pymnts.com/?p=3889376)
- ASC leaders say payer behaviour is "more aggressive, automated" — [Becker's ASC](https://www.beckersasc.com/?p=98908). Headline: "AI is making claim denials worse for physician practices" (19 Jun 2026, body not read, first-round) — [Healthcare Guys](https://healthcareguys.com/2026/06/19/ai-is-making-claim-denials-worse-for-physician-practices-heres-why/)
- Fax persistence: about 75% of US medical institutions still rely on fax (2025, first-round) — [JMIR Med Inform](https://medinform.jmir.org/2025/1/e62983)
- Vendors are productising the work: athenahealth Denial Resolution Automation (Jun 2026), WebPT AI RCM (Jul 2026), Brightree IDA, WellSky AI intake (Jan 2026) — sources in Q7.
- A six-month CMS moratorium on new Medicare enrollment of certain DMEPOS "medical supply companies" was announced 25 Feb 2026. An HME trade page reports it expired 27 Aug 2026 — [Greenberg Traurig](https://www.gtlaw.com/en/insights/2026/2/cms-announces-medicare-dmepos-supplier-enrollment-moratorium); [Federal Register, 27 Feb 2026](https://www.govinfo.gov/content/pkg/FR-2026-02-27/pdf/2026-03971.pdf); [HME News tag page](https://www.hmenews.com/tag/part-a)

### Inferences
- P1: by late 2028, pure "fax to fields" work will be close to free inside the main DME and home health platforms. A services business must own outcomes: complete, payer-ready orders within X hours, missing documents chased, and patients contacted. Otherwise it competes with $2.75-per-referral software.
- P2: CMS-0057-F's "specific reason for each denial" makes appeals easier to triage and draft (inference). Payer AI raises volume. EHR AI handles coding corrections first. The net effect is more complex appeals per practice, which favours AI drafting plus a human reviewer.
- WISeR's inclusion of electrical nerve stimulators means DME suppliers in those six states now need prior-auth documentation packages for some traditional Medicare orders. That is new intake and auth work for both problems (inference).

### Gaps
- WISeR outcome data: a summary mentioned a 62% first-submission approval rate in Texas rising to 84% after review, but this could not be verified, so it is excluded. Payer-side adoption of AI denial tools beyond WISeR was not measured.

---

## Q9. How to reach these buyers

### Takeaway
P1: through HME News, Medtrade, AAHomecare, NAHC and state home care associations, Brightree and WellSky partner ecosystems, and DME billing companies (which already sell intake). P2: through HBMA (about 500 member RCM firms, the best white-label channel), AAPC (forums plus local chapters), MGMA state chapters, APTA Private Practice, athenahealth and WebPT marketplaces, and Physicians Practice, Medical Economics and Becker's newsletters.

### Cited Findings
- HBMA: "more than 47,000 employees at nearly 500 revenue cycle management firms and professional billing departments" (undated About page). Typical member firm has 40–50 employees (older document) — [HBMA About](https://hbma.org/content/about/about-hbma); [HBMA membership PDF](https://www.hbma.org/downloads/HBMA_Membership11.pdf). HBMA runs an annual RCM conference with an exhibitor prospectus — [HBMA RCM2022 prospectus](https://www.hbma.org/uploads/content_files/files/event/HBMA_RCM2022_ConferenceProspectus_D2.pdf)
- AAPC runs active discussion forums, including threads on offshore PHI — [AAPC forum](https://www.aapc.com/discuss/threads/offshore-resources-cannot-access-phi.199990/)
- DME trade media and events: HME News — [HME News](https://www.hmenews.com/tag/patient-intake); Medtrade — [Medtrade](https://medtrade.com/news/subcontracting-with-offshore-company/144741/)
- Home care: HomeCare Magazine — [HomeCare](https://www.homecaremag.com/news/wellsky-debuts-new-referral-intake-solution); state associations active on MedPAC issues: Home Care Association of Florida, Home Care Alliance of Massachusetts, LeadingAge Ohio — [HCAF](https://homecareassociationoffloridainc.growthzoneapp.com/provider-updates/Details/medpac-s-march-2026-report-raises-concerns-for-home-health-providers-319525); [HCA Mass](https://homecareallianceofmassachusetts.growthzoneapp.com/member-news/Details/medpac-march-2026-report-summary-320431); [LeadingAge Ohio](https://leadingageohio.org/aws/LAO/pt/sd/news_article/615458/_PARENT/layout_details/false)
- PT owners: WebPT's Heidi Jannenga appears on practice podcasts (e.g., The Practice Marketing Podcast on the 2025 State of Rehab) — [Buzzsprout](https://www.buzzsprout.com/1155128/episodes/18559061-2025-state-of-rehab-w-heidi-jannenga-webpt); PT Pintcast — [Podpage](https://www.podpage.com/ptpintcast/videos/pts-bigger-problem-than-burnout-2025-state-of-rehab-report)
- Practice-leader media: Physicians Practice (MGMA poll coverage) — [Physicians Practice](https://www.physicianspractice.com/view/mgma-poll-denials-are-biggest-revenue-cycle-leak-for-medical-practices); Medical Economics — [Medical Economics](https://www.medicaleconomics.com/view/wiser-spending-or-unneeded-delays-in-health-care-prior-authorizations-ai-in-medicare-prompt-concerns); Becker's ASC — [Becker's ASC](https://www.beckersasc.com/?p=98908)
- EHR marketplaces with integrations to underpayment tools: athenahealth, ModMed, eClinicalWorks, NextGen (RevFind integrations) — [GetApp](https://www.getapp.com/all-software/a/revfind/)

### Inferences
- The fastest P2 route is white-label through HBMA-size billing firms (40–50 staff). Each one gives access to dozens of practices, and they already sell offshore-style delivery.
- For P1, DME billing companies with intake teams are both a channel and a competitor.

### Gaps
- Not verified this session (prior knowledge only): MGMA state chapter lists, AAPC HEALTHCON, MGMA Leaders Conference, APTA Private Practice annual conference, AAHomecare and NAHC events and membership counts, Home Health Care News, the athenahealth Marketplace partner programme terms, and Brightree and WellSky partner programmes.

---

## Q10. Roughly how many US practices or providers have this problem

### Takeaway
Hard counts are thin. 42.2% of US physicians were in physician-owned private practice in 2024 (AMA), down from 60.1% in 2012. Ophthalmology (70.4%) and orthopedics (54%) have the highest independent shares. There were roughly 2,000 billing companies (HBMA, 2011 estimate), with about 500 HBMA member firms. DME supplier, home health agency and PT practice counts were not found this session.

### Cited Findings
- AMA Physician Practice Benchmark 2024: 42.2% of physicians in private practice (wholly physician-owned), down from 60.1% (2012) and 46.7% (2022). Shares: cardiology 30.7%, radiology about 47%, surgical subspecialties 51.2%, orthopedics 54%, ophthalmology 70.4%. In 2022, 18.3% of physicians were in practices with 50+ physicians — [AMA](https://www.ama-assn.org/about/research/physician-practice-benchmark-survey); [Radiology Business](https://radiologybusiness.com/topics/healthcare-management/medical-practice-management/percentage-radiologists-private-practice-continues-plummet-ama-says); [Drugs.com/HealthDay](https://drugs.com/news/fewer-physicians-working-private-practice-113891.html)
- Billing companies: HBMA's 2011 annual report estimated nearly 2,000 billing companies nationwide, with over 700 members then. Today's About page says nearly 500 firms. A 2019 prospectus says 400+ firms; a 2022 prospectus says 250+ firms (inconsistent) — [HBMA 2011](https://www.hbma.org/downloads/HBMA_AnnualReport_11_FNweb.pdf); [HBMA About](https://hbma.org/content/about/about-hbma); [HBMA 2019](https://www.hbma.org/uploads/content_files/files/event/2019%20HBMA%20Prospectus-online.pdf)
- Home health: 8.6% of Medicare FFS beneficiaries used home health in 2023. MedPAC (March 2026) recommends a 7% base-rate cut for CY2027, citing freestanding agency margins of 21.2% (2024) — [HCAF summary](https://homecareassociationoffloridainc.growthzoneapp.com/provider-updates/Details/medpac-s-march-2026-report-raises-concerns-for-home-health-providers-319525)
- DMEPOS: the CMS dataset "Medicare Durable Medical Equipment, Devices & Supplies – by Supplier" lists suppliers by NPI (it can be used to count suppliers, but the count was not retrieved) — [data.gov catalog](https://catalog.data.gov/dataset/medicare-durable-medical-equipment-devices-supplies-by-supplier)

### Inferences (estimate math)
- Physicians in private practice: if the AMA survey base is about 800,000 patient-care physicians (**prior knowledge, not verified**), then 42.2% ≈ 340,000 physicians in physician-owned practices. At an assumed average of about 5 physicians per independent practice, that is roughly 60,000–70,000 independent practices. Treat this as an order-of-magnitude figure only.
- Billing companies: about 2,000 (2011 estimate). Small firms with fewer than 50 staff are likely the majority (inference from HBMA's typical member size).
- Home health agencies: roughly 11,000–12,000 Medicare-certified agencies (**prior knowledge, not verified**).

### Gaps
- Not found: NPPES counts by taxonomy (DME supplier, PT clinic, sleep lab, imaging centre), Census CBP counts (NAICS 621610 home health, 532283 home health equipment rental, 621340 PT offices), AAHomecare and APTA counts, and a current Medicare-enrolled DMEPOS supplier count.

---

## Q11. The strongest argument against each opportunity

### Takeaway
P1: the work is being turned into a cheap software feature by the platforms the buyers already use (Brightree, WellSky) and by $549/month tools. The remaining exception work is time-critical in US hours, and per-referral value is low for DME. P2: every target already pays someone (a billing company at 4–10% or in-house billers) to do denials. Commure/Athelas, athenahealth and WebPT now sell AI RCM to exactly this small-practice segment, and payer and Medicaid contracts can block offshore PHI access.

### Cited Findings
- Bundling in P1: [Brightree IDA](https://www.brightree.com/brightree-intelligent-document-automation/); [WellSky Jan 2026](https://www.businesswire.com/news/home/20260127232204/en/WellSky-Launches-New-AI-Capabilities-to-Automate-and-Scale-Referral-Intake); cheap software [Medsender on Capterra](https://www.capterra.com/p/215989/Medsender/pricing/); funded rival Tennr ($101M Series C, $605M valuation, Jun 2025, first-round) — [Fortune](https://fortune.com/2025/06/18/tennr-health-tech-ai-patient-referral-ivp-a16z-lightspeed-iconiq-series-c/)
- Crowding in P2: [Athelas case studies](https://www.athelas.com/case-studies/south-valley-ent); [athenahealth Jun 2026](https://www.businesswire.com/news/home/20260603429867/en/); [WebPT Jul 2026](https://www.webull.com/news/15225550655022080); 25% contingency competitors [Relvio](https://relvio-health.pages.dev/), [NoNos](https://nonos.pages.dev/)
- Offshore limits: see Q12 ([Shumaker](https://www.shumaker.com/insight/offshoring-patient-data-what-health-care-providers-need-to-know-now/); [Medical Mutual provider offshore attestation](https://www.medmutual.com/-/media/MedMutual/Files/Providers/Updated-Provider-Offshore-Attestation-Form.pdf))

### Inferences
- P2 counter-counter: the contingency underpayment audit is a "second look" that billing companies paid on collections have weak reasons to do on their own posted payments (first-round inference). Selling it white-label to billing companies turns a competitor into a channel.
- P1 counter-counter: shops on older or smaller DME and specialty systems, and specialty practices whose EHR lacks fax AI, still need people. But proving which shops those are takes prospect-level research.

**Shariah flag (no ruling given).** Both services work for healthcare providers, but their output (claims, eligibility checks, appeals) runs through conventional health insurance payers, which some scholars question. Points that may matter to the end client's advisor:
- P1 is mainly document processing for a provider. Insurance touches only the eligibility step, so the question may be lighter.
- P2's revenue comes from collecting insurer payments, and contingency pricing ties the fee to recovered insurer money.
- Segments where the question may differ: Medicare-only or Medicaid-heavy providers (government programmes, not commercial insurers); cash-pay practices (no payer claims, so P2 does not apply, but P1 intake still does); and any work on patient balances that touches medical credit or interest-bearing payment plans, which should be avoided.

### Gaps
- No churn or win-rate data on outsourced denial services was found, so the counter-arguments are not quantified.

---

## Q12. Delivery constraints for an offshore (non-US) team

### Takeaway
HIPAA itself does not ban offshore business associates (prior knowledge; the hhs.gov page could not be fetched). The real limits come from contracts and programmes:
- Medicare Advantage plans require offshore attestations, which some push down to providers.
- Some state Medicaid programmes and MCO contracts ban PHI leaving the US (Texas; Tennessee without consent; older OIG list: Wisconsin, Alaska, Ohio, Arizona).
- Availity's agreement bans scraping and web-emulation bots.
- The DOJ bulk-data rule blocks only six "countries of concern", so India, Pakistan and the Philippines are not among them.

P1 intake needs same-day response in US business hours. P2 denials work can mostly run asynchronously.

### Cited Findings
**Medicaid and state rules**
- ACA §6505 bars state Medicaid from paying for items or services furnished by entities outside the US. CMS clarified this targets benefits and services, not administrative support. States are "tightening the reins" through policy manuals, procurement terms and managed-care contracts. The Texas Medicaid Uniform Managed Care Contract bars MCOs and all subcontractors from moving state Confidential Information outside the US. A Tennessee Medicaid (TennCare) BAA requires express written consent before PHI is viewed or used beyond US borders — [Shumaker](https://www.shumaker.com/insight/offshoring-patient-data-what-health-care-providers-need-to-know-now/)
- An older OIG survey found four state Medicaid programmes (Wisconsin, Alaska, Ohio, Arizona) prohibit offshore subcontractors (year not shown in the summary; a secondary summary gives different counts) — [OIG OEI-09-12-00530](https://www.oig.hhs.gov/documents/evaluation/3120/OEI-09-12-00530-Complete%20Report.pdf); [Fierce Healthcare](https://www.fiercehealthcare.com/it/offshore-outsourcing-a-risk-to-personal-health-information-oig-report-warns)
- Law-firm guidance on US healthcare offshoring — [McDermott Will & Emery](https://www.mwe.com/?p=322505)
- An AAPC forum thread claims a broad ban on offshore PHI, but the poster could not find a primary source. Commenters pointed to an executive order limited to "countries of concern" and a proposed rule that is not law (treat as unreliable) — [AAPC forum](https://www.aapc.com/discuss/threads/offshore-resources-cannot-access-phi.199990/)

**Medicare Advantage**
- CMS requires an MA organisation to submit an offshore attestation if it, or any first-tier, downstream or related entity, does offshore work involving MA beneficiaries' PHI. Plan forms ask for PHI safeguards, a bar on accessing unrelated Medicare data, termination on a serious breach, an annual audit of the offshore subcontractor, and sharing audit results with CMS on request. Some plans require written notice and/or approval before an offshore subcontract starts. Several are **provider** attestation forms — [Medical Mutual provider form](https://www.medmutual.com/-/media/MedMutual/Files/Providers/Updated-Provider-Offshore-Attestation-Form.pdf); [Moda Medicare provider attestation](https://modahealth.com/pdfs/comp/Moda_Medicare_2020-21_Provider_Attestation.pdf); [Johns Hopkins Health Plans, 2016](https://www.hopkinsmedicine.org:443/-/media/johns-hopkins-health-plans/documents/offshoring-of-phi-attestation_final-070816.pdf); [CHRISTUS](https://chppayment.christushealth.org/documents/CHRISTUSHealth/Evergreen/Providers/Provider%20Relations/Offshore%20Subcontractor%20Compliance%20Attestation_H1189_PC2610.pdf); [Delta Dental MA](https://www1.deltadentalins.com/content/dam/ddins/en/pdf/dentists/medicare-advantage-attestation.pdf)
- DME trade press has covered subcontracting with offshore companies (content not read) — [Medtrade](https://medtrade.com/news/subcontracting-with-offshore-company/144741/)

**DOJ Data Security Program (bulk sensitive data rule)**
- Covers six countries of concern: China (incl. Hong Kong and Macau), Cuba, Iran, North Korea, Russia and Venezuela, plus "covered persons" with significant ties to them. Personal health data is a covered category. The rule applies even if data is de-identified or encrypted. It took effect 8 Apr 2025; enforcement started 9 Jul 2025; further requirements from 6 Oct 2025 — [Foley Hoag](https://foleyhoag.com/news-and-insights/blogs/security-privacy-and-the-law/2025/june/doj-s-bulk-sensitive-data-rule%E2%80%9D-is-in-effect-and-may-require-significant-compliance-obligations-as); [Jones Day](https://www.jonesday.com/en/insights/2025/01/doj-issues-final-rule-on-bulk-transfers-of-sensitive-personal-data)

**Payer portals and bots**
- Availity's agreement (version V2024.0718) prohibits "Scraping Methods" (screen scraping, data scraping, web scraping, web emulation) used outside the services' intended purpose, and lets Availity take technical measures. It also bars eligibility transactions used for insurance discovery — [Availity OAA](https://essentials.availity.com/availity/documents/Availity_OAA.pdf). RPA bots that log into Availity for claim status are nonetheless marketed — [UiPath Marketplace](https://marketplace.uipath.com/listings/epic-availity-claim-statusing-bot)

**Hours**
- A remote US intake role runs Mon–Fri 12:00 PM–8:30 PM EST — [Virtual Vocations](https://www.virtualvocations.com/job/senior-intake-coordinator-3143120-i.html)

### Inferences
- HIPAA (prior knowledge, not verified this session): no offshore prohibition. A BAA is required between the provider and the vendor, and the vendor must sign BAAs with its own subcontractors. The offshore team carries the same Security Rule duties.
- Practical rules for a non-US team:
  - (1) Do not take Texas or Tennessee Medicaid managed-care PHI offshore without written consent. Screen each client's payer mix and MA plan contracts.
  - (2) Expect MA plans to ask providers about offshore vendors. Have an attestation pack ready: safeguards, audit, breach termination.
  - (3) Do not use Chinese-owned tools or subcontractors (DOJ rule). Pakistan, India and the Philippines are not countries of concern.
  - (4) Use clearinghouse X12 276/277 and 270/271 transactions or approved APIs for status and eligibility, and keep portal work human-driven unless a payer approves automation.
  - (5) Keep PHI in a US-hosted environment (VDI) with no local storage. This is the common mitigation (inference).
- Time zones: 9 AM–5 PM US Eastern is 6 PM–2 AM in Pakistan (UTC+5) until US daylight time ends on 1 Nov 2026, then 7 PM–3 AM. In the Philippines (UTC+8) it is 10 PM–6 AM after 1 Nov. P1 (new-referral response and calls to referring offices) and payer phone calls need night shifts or a US-hours human. P2 appeal drafting, underpayment audits and portal work can run off-hours.

### Gaps
- HHS OCR's own guidance text on offshore business associates could not be fetched. Current statutes for all 50 state Medicaid programmes were not compiled. Terms for other payer portals (UHC, Aetna, Cigna, BCBS plans) were not checked.

---

## Q13. Where to find 15 named prospects within 14 days

### Takeaway
Use public CMS datasets to build lists:
- P1: the DMEPOS "by Supplier" and "by Supplier and Service" datasets, filtered to independent suppliers in WISeR states and to HCPCS codes that now need auth. Home health agency lists can come from Care Compare (not verified).
- P2: HBMA-size billing companies and independent groups in high-independence specialties (ophthalmology, orthopedics, ENT, podiatry, PT).

No named prospects were compiled in this pass (search budget).

### Cited Findings
- CMS "Medicare DME, Devices & Supplies – by Supplier and Service" gives supplier NPI, HCPCS code, payments and charges. The catalog was updated 7 Oct 2025 and the latest version is titled 2023 — [data.gov](https://catalog-beta.data.gov/dataset/medicare-durable-medical-equipment-devices-supplies-by-supplier-and-service). "By Supplier" — [data.gov](https://catalog.data.gov/dataset/medicare-durable-medical-equipment-devices-supplies-by-supplier). "By Referring Provider" shows which physicians generate DME orders — [data.gov](https://catalog.data.gov/dataset/medicare-durable-medical-equipment-devices-supplies-by-referring-provider-1eb67). Licence: US government works.
- A legacy Medicare Supplier Directory existed (2011 archive) — [UNT web archive](https://webarchive.library.unt.edu/web/20110504095507/http://data.medicare.gov/dataset/Supplier-Directory-Data/g4vg-8tt9)
- WISeR states (AZ, NJ, OH, OK, TX, WA) and items (e.g., electrical nerve stimulators) — [Georgetown CHIR](https://medicare.chir.georgetown.edu/new-cms-wiser-model-revives-concerns-of-prior-authorization-and-artificial-intelligence/)
- HBMA membership (about 500 firms) — [HBMA About](https://hbma.org/content/about/about-hbma)
- AMA high-independence specialties: ophthalmology 70.4%, orthopedics 54% — [Radiology Business](https://radiologybusiness.com/topics/healthcare-management/medical-practice-management/percentage-radiologists-private-practice-continues-plummet-ama-says)
- Competitor case studies show the type of practice that buys: an orthopedics group, South Valley ENT, Hillside Foot & Ankle, Meier Marsh Professional Therapies (already Athelas customers, so not prospects) — [Athelas](https://www.athelas.com/case-studies/south-valley-ent)

### Inferences (14-day plan)
- **P1 (8 prospects):** download the DMEPOS by-Supplier file. Keep suppliers in WISeR states with mid-range Medicare payments (e.g., $0.5M–$10M, assumption), and remove national chains. Cross-check the website for "fax referrals to" (a sign of manual intake). Contact titles: Owner/President, Director of Intake, Revenue Cycle or Billing Manager. For home health: Administrator, Director of Intake, or Executive Director.
- **P2 (7 prospects):** 4 small billing companies (HBMA-size; contact Owner/CEO or COO) and 3 independent ortho, ophthalmology, ENT or PT groups not on athenaOne or WebPT (contact Practice Administrator or Billing Manager).
- Other list sources (prior knowledge, not verified this session): the NPPES NPI Registry and downloadable file (filter by taxonomy, e.g., DME supplier, PT clinic), Care Compare home health agency data on data.cms.gov, the CMS "Medicare Physician & Other Practitioners – by Provider" dataset, state DME and home care association member directories, and Medtrade exhibitor lists.

### Gaps
- No named prospects were collected. The HBMA directory's public availability was not verified. No way of identifying a supplier's software platform (Brightree versus others) from public data was found.

---

## Q14. Pricing shapes buyers already accept

### Takeaway
Buyers already accept these pricing shapes:
- % of collections (4–10%; 5–8% typical small practice)
- contingency on recovered money (25% for small-practice denial firms; about 8–12.5% for Medicare RACs)
- per claim ($3–$8)
- per appeal ($10 to $49–$299)
- flat monthly software ($299–$2,249)
- offshore hourly or FTE ($5–12/hour)

Enterprise AI vendors stay quote-only.

### Cited Findings
| Shape | Rate | Problem | Source |
|---|---|---|---|
| % of collections (full billing) | 4–10%; most small/mid 5–8%; complex specialties 10–12% | P2 | [Neolytix](https://neolytix.com/articles/what-is-the-going-rate-for-medical-billing-services/); [Carepatron](https://www.carepatron.com/blog/how-much-do-medical-billing-services-cost/); [Helpware](https://helpware.com/blog/medical-billing-outsourcing) (vendor guides) |
| Premium vs budget % | 6–14% vs 2–5% | P2 | [RCM Intel](https://rcmintel.pages.dev/blog/are-cheap-medical-billing-services-worth-it/) |
| Contingency on recovered denials | 25%, no recovery no fee | P2 | [Relvio](https://relvio-health.pages.dev/); [NoNos](https://nonos.pages.dev/) |
| Government recovery audit | about 8–9%; older 9–12.5% (DME 14–17.5%) | P2 benchmark | [AAPC](https://aapc.com/codes/coding-newsletters/my-homecare-week-alert/audits-racs-get-8-of-every-denial-they-make-156734-article); [CPBJ](https://www.cpbj.com/cms-we-have-a-recovery-audit-contractor-problem) |
| Per claim | $3–$8 (billing); $3–$7 (India coding) | P2 | Q5 sources |
| Flat monthly billing | $500–$2,500 | P2 | Q5 sources |
| Per appeal + subscription | $10 per appeal + $25/month | P2 | [Journal of Cyber Policy](https://journalofcyberpolicy.com/?p=310643) |
| Flat monthly software with volume cap | $299 (3,000 pages); $549 (200 referrals); $2,249 | P1 | [Capterra](https://www.capterra.com/p/215989/Medsender/pricing/); [Xpay](https://www.xpay.sh/agent-ready-index/medsender/) |
| Per verification + per-location tier (dental analogue) | $2.75–$12.50 per verification; $250–$825 per location per month; $299 setup | P1/P2 eligibility | [eAssist](https://dentalbilling.com/pricing-dental-insurance-verification/) (first-round) |
| Offshore hourly or FTE | $5–$12/hour PH; from $7/hour India (vendor) | Both | [HireTalent.ph](https://hiretalent.ph/skill/medical-billing-support); [Upwork](https://www.upwork.com/services/product/admin-customer-support-complete-medical-billing-accounts-receivables-and-payment-posting-services-1604985890695888896) |
| Enterprise quote-only | Not published | P1 (Tennr), P2 (AKASA, Commure) | [G2](https://www.g2.com/products/tennr/pricing) |

### Inferences
- P1 offer shape: a per-referral fee (about $4–$8, inference) or a monthly retainer by volume band (for example, up to 300 referrals a month), with a turnaround guarantee. Sell it as cheaper than 1 FTE ($3.2K–$9.0K a month, Q4) and better than $549 software because exceptions and missing documents are handled.
- P2 offer shapes: (a) 20–25% contingency on aged or unworked denials and underpayments, with no minimum (matches the market anchor); (b) for billing companies, white-label at a lower share (e.g., 10–15%, assumption) or per-appeal pricing; (c) a monthly retainer plus a smaller success fee for larger groups.
- Contingency on recovered insurer money is the shape most exposed to the Shariah question in Q11 (flag only).

### Gaps
- No published per-referral prices from outsourced intake services. No published contingency rate specifically for underpayment recovery at physician practices. Commure/Athelas pricing not published.
