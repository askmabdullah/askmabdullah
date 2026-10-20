# Phase 2: Risk and contracts (model/risk.md)

Author: Phase 2 risk and contracts agent. Date: 2026-10-20.
Inputs: BRIEF sections 1 to 8, phase1-summary.md, all 21 track files.

## 0. Read this first
- This is NOT legal advice. It is a working draft of terms and risks. A qualified lawyer must review the contract template before first use. See section 7.
- Evidence tags: [T4] means track 4, [T19] means track 19, and so on. [GK] means general knowledge from the author, NOT from Phase 1. Every [GK] item needs checking by a lawyer or a payment provider before we rely on it.
- One web search was used (limit was 3). Label: [WS1]. Question: does Lovable's own terms say who owns generated code. Result is in section 1.5.
- Big evidence gap: no track found a single chargeback, refund fight, lawsuit or fixed-price overrun story in this niche [T19 #6, T16 #11]. Reddit was not reachable, so absence is weak. Treat all refund and dispute rates below as assumptions to test, not facts.
- Track 22 (buyer reviews on Clutch, G2, Trustpilot) was not in the folder when this was written.
- Track 20 covers outbound marketing law (CAN-SPAM, PECR, CASL, Spam Act), not data protection law. Data protection notes below are [GK].

---

## 1. Contract terms for a fixed-price rescue

Use two documents.
- Document A: Audit order (short, 1 to 2 pages).
- Document B: Master services agreement plus a Statement of Work (SOW) for the sprint.
The audit report becomes Schedule A of the SOW. That ties scope to the audit.

### 1.1 Scope tied to the audit checklist
Why: vendors say "fixed price requires airtight scope" [T16 #10]. Wavect and others start with a signed SOW after an audit [T16 #10, T19 #6]. Every serious seller audits first [T19 sec 6].

Terms:
- Scope = the list of checklist items in Schedule A. Nothing else.
- Each item has an ID from the standard checklist (the 38 items in track 11 section 6b: auth, RLS, secrets, payments, edge functions, deploy, performance, structure, tests, monitoring).
- Each item has: status found, severity, planned fix, acceptance test, and the fee share for that item.
- The audit report is dated. It records the state of the app at start (git tag, screenshots, Supabase advisor output). This is our proof of what was already broken.
- A rescue-or-rebuild gate is written in the audit. If the app fails the gate, we do not sell a sprint. We quote a rebuild or a longer sprint separately [T19 sec 6, T11 6b triage].
- Size limit for the fixed price: one stack, one repo, under about 20 to 30k lines, Supabase plus Stripe [T19 Appendix A]. Above that: re-quote.
- Stop-loss: if we find, after start, that the app is materially worse than the audit showed, either side can pause and re-scope. We do not eat a 3x overrun for free [T19 Appendix A].
- Stated exclusions (put in the SOW, not hidden):
  - New features, redesign, "finish the app".
  - Migration between platforms (for example Lovable Cloud to own Supabase). This is a separate fixed job [T20 #4].
  - App Store or Play Store submission.
  - Load testing beyond named targets.
  - Third-party outages and platform bugs (Lovable, Supabase, Stripe, Vercel).
  - Legal or compliance certification (SOC 2, ISO, PCI, HIPAA).
  - Content, copy, and fixes to code added by anyone after the audit date.

### 1.2 Acceptance criteria and sign-off
- Acceptance tests are written in Schedule A before work starts. Each is a pass or fail check. Example: "user A cannot read user B's rows" (RLS test) [T11 6b #35]. "Stripe test payment ends in correct entitlement" [T11 6b #18 to 20].
- Delivery notice: we send a written delivery note with test results and a Loom walkthrough.
- Client has 5 business days to test and either accept or list failed tests.
- We fix failed in-scope tests once, free, inside 5 business days. Then a second review round.
- Deemed acceptance: no reply in 5 business days, or use of the work in production, counts as acceptance.
- A "defect" is a failed acceptance test. A "change" is anything not in Schedule A. Defects are free. Changes go to change control.
- Sign-off is by email or e-signature. Keep it. It is our main evidence in any dispute (section 2).
- Warranty after acceptance: 30 days on in-scope fixes only. Not on new code. Benchmarks: Slopfix 2 weeks [T19 #9], aibrify 90 days free repair on what it fixed [T16 #4]. 30 days is a middle point. [Assumption, not tested.]

### 1.3 Change control
- Any change is a written Change Request: what, price, days. No work starts until approved in writing (email is fine).
- Hourly or day-rate for changes, set in the SOW.
- Why this matters: the AI tool regression loop and client re-prompting are the likely scope-creep source [T19 #7]. Evidence is thin, so treat this as a risk to test in the first 30 days.
- Small free allowance: tiny tweaks under 30 minutes, to keep goodwill. Optional.

### 1.4 Client obligations
- Access within 1 business day of signing: repo, Lovable or Replit project invite, Supabase, Stripe (test mode first), hosting, domain. Accounts stay in the client's name [T11 6b #26, #28].
- Use invites and roles, not shared passwords. Least privilege. Time-limited. [GK] Platform terms on account sharing were not found in the tracks. Check each platform before we ask for a login.
- Backup before we start. Client confirms a backup exists, or we take one first. Reason: Replit agent deleted a live database [T11 #11, #12].
- Code freeze: during the sprint the client does not prompt the AI tool on the main branch. Client may work on a separate branch that we review. Reason: re-prompting breaks fixes [T19 #7, sec 6].
- Timely answers: reply within 2 business days. Delay pauses the clock. If the client is silent for 10 business days we may close the SOW and bill work done.
- One named decision maker.
- Client pays platform fees, API costs and credits (Lovable, Replit, Supabase, Stripe). Credit burn is already a top pain [T1 #2, T3 #3].
- Client warrants it has the right to give us the code and data, and that the app does not break the law.
- Client takes responsibility for security decisions we advise on but they decline (section 3, risk acceptance form).
- Time zone: state our overlap window in the SOW. Buyers screen for overlap [T15 #5]. Lahore is UTC+5.

### 1.5 Intellectual property
Terms:
- Client owns the deliverables (code we write or change) on payment in full. We assign the rights.
- Client keeps what it already owned: its app, data, brand, and the AI output it generated.
- We keep our tooling: checklists, scripts, test templates, scanners, playbooks, internal docs. We give the client a perpetual, non-exclusive licence to any of these that sit inside the delivered repo (for example CI config, lint rules, test files, README). Slopfix hands over a CLAUDE.md, lint rules and CI checks [T19 #8]. This is normal.
- We may reuse general know-how, but never client code or data.
- No client code or data goes into any public model, public repo or public tool. Disclose which AI assistants we use. Prefer tools with no-training terms. [GK: check each vendor's terms.]
- Portfolio and name use only with the client's written consent (ask at signing). Reason: Pakistani firms often work under NDAs and cannot show work [T20 #17], and proof is what wins trust [T15 sec 6, T20 #18]. Ask early for "may we name you and quote you".

Platform terms found:
- [WS1] Lovable product terms: customer owns the apps and projects built, and owns "AI Output" generated for them, "subject to any third-party rights in the underlying models, training data, or outputs". Nothing transfers ownership of Customer Data or AI Output to Lovable. Lovable's Terms of Service say it claims no ownership of code generated with its services. The same terms say Lovable analyses generated code and prompts to improve its AI. Sources: https://lovable.dev/product-terms ; https://lovable.dev/terms . Read via search snippets only, not opened. Terms may have changed. Check live pages before launch.
- [T9 #2] Lovable Expert programme terms page dated August 2026, and Lovable "may change criteria any time". This is platform-terms dependence (section 5).
- [T11 #1] The CVE-2025-48757 record says Lovable disputes it: "each individual customer of the Lovable platform accepts a responsibility over protecting the data of their application". So the platform puts security responsibility on the customer. Our contract must say the same: the client stays responsible.
- [T21 section 7, gate 5 note] Replit agent charges cited as non-refundable by agency posts (vendor source, weak).
- [T1 #3] Trustpilot reviewers say Lovable denies refunds for glitches (anecdote, weak).
- Not found in the tracks: Replit, Bolt, Base44 and v0 ownership terms. Base44 exports frontend only and keeps backend [T2]. Replit database, hosting and auth are tied to Replit [T2 sec 6]. So "client owns the code" is only partly useful on those platforms. Say so in the SOW.

AI-generated code and licence risk:
- AI output can copy open-source code with its licence. Copyright in purely AI-made code is uncertain in some countries. The vp0 commentary says human edits help [WS1, weak, general info]. [GK]
- Terms: we make no promise that AI-generated code written before we arrived is free of third-party rights. For code we write, we run a dependency licence check and report it. Client warrants rights in what it gives us.
- Lawyer item (section 7).

### 1.6 Security disclaimer
Plain-language intent (lawyer to turn into clause):
- We fix and test the items in Schedule A.
- We do not certify the app as secure.
- We do not promise the app cannot be breached, now or in future.
- New code, new dependencies, new settings, and platform bugs can add new holes after we leave. Lovable's own backend had a 48-day exposure in 2026 [T11 #9]. Supabase is changing key types by end of 2026 [T11 #14].
- Many headline "x% of apps are vulnerable" numbers are vendor marketing [T11 #6]. Do not use them in the contract or the sales page as promises.
- Never use words like "guarantee secure", "hack-proof", "fully secured", "audit-passed" in sales or contract. Use "hardened against the listed risks".
- Secrets: we list every secret found in code, history, build output and (where visible) chat history. Chat history and source may already have been exposed [T11 #9, #10]. We recommend rotating all. Rotation is done by the client, or by us with the client present. Rotation is the client's duty, and unrotated secrets are excluded from our liability.
- We do not hold production credentials longer than needed. Terms:
  - Credentials go through a password manager or the platform's secure invite. Never email or chat.
  - Least privilege and time-limited.
  - We prefer staging, a test Stripe mode, and a read-only role.
  - On delivery, we delete our copies and the client revokes our access. A written "access revoked" checklist is part of sign-off.
  - Our staff laptops hold no production secrets. [GK] Process to be set by Wanile ops.

### 1.7 Data protection
Plan: avoid touching real user data. Work on staging with synthetic or seeded data. That removes most of this section. When we cannot avoid it:

- Roles: client is controller (GDPR), we are processor. Sign a Data Processing Agreement (DPA) before access. [GK]
- DPA basics (GDPR Art 28 / UK GDPR): act only on client instructions; staff confidentiality; security measures; list of sub-processors (including AI tools and cloud tools); help with data subject requests; breach notice to the client without undue delay (propose 24 hours); delete or return data at end; allow audit. [GK]
- Cross-border transfer: our team is in Pakistan. As far as the author knows, Pakistan has no EU or UK adequacy decision, so EU clients need Standard Contractual Clauses, UK clients need the UK IDTA or Addendum, plus a transfer risk assessment. [GK, verify]
- Australia: Privacy Act 1988 and the Australian Privacy Principles. APP 8 (sending data overseas) means the Australian client stays accountable for what an overseas processor does, so AU clients may ask for contract protections. The Notifiable Data Breaches scheme applies to eligible breaches. [GK, verify]
- Canada: PIPEDA makes the client accountable for data sent to a processor and expects contract protection. Quebec Law 25 adds a privacy impact assessment before data leaves Quebec. [GK, verify]
- US: state laws (for example California) need service-provider terms in contracts. [GK]
- Never accept: health data (HIPAA), children's data (COPPA), card numbers (PCI). Put these in the ethics and intake screen as amber/red (section 4). We never see raw card data; Stripe holds it.
- Marketing law (from track 20, outbound only): CAN-SPAM has no B2B exemption [T20 #21]; UK PECR treats sole traders as individuals [T20 #22]; CASL needs role-relevant messages and has no blanket B2B exemption [T20 #23]; Australia Spam Act needs consent, inference rules and unsubscribe [T20 #24]. Not part of the contract, but part of the channel risk. Track 20 flags these as secondary sources and needing a lawyer check.

### 1.8 Confidentiality
- Mutual NDA built into the MSA. Covers code, data, credentials, business plans, audit findings.
- Term: 3 years after end. Trade secrets and personal data: as long as they stay secret or protected. [GK, typical]
- Audit findings are confidential to the client. We never publish anything about a client's flaws, even anonymised, without consent. Reason: a public leak of a client's hole is both an ethics and a liability problem, and "I found a vulnerability" outreach is already seen as a nuisance or extortion [T20 #26].
- Staff and any subcontractor bound by written confidentiality. No subcontractor without notice and client consent.
- Exceptions: law, court order, regulator. We tell the client first where legal.

### 1.9 Limitation of liability
Intent:
- Cap on our total liability: the fees paid for the SOW in question (some clients will ask for 12 months of fees).
- No liability for indirect or consequential loss, lost profit, lost revenue, lost data, loss of goodwill.
- Exclusions from our liability: pre-existing defects and breaches; client changes after the audit date; unrotated secrets; declined recommendations; third-party and platform failures; client's failure to keep backups.
- Carve-outs the law will not let us exclude: fraud, wilful misconduct, death or personal injury from negligence in some countries, and in some places consumer or small-business protections. [GK] Australian Consumer Law and unfair contract terms rules can bite on small-business clients. Quebec has its own rules. A lawyer must check each target market.
- Why the cap is "fees paid": our fee is small ($2,000 range) but a data breach claim can be far bigger. Without a cap, one bad day ends the business.
- Expect pushback from funded clients. Offer a higher cap only with insurance (section 3.3).

### 1.10 Refund policy: recommended shape
What the evidence shows:
- Wavect: weekly billing, "Cancel any week. Last week refunded if we didn't blow you away" [T16 #3, T19 #6, T20 #19]. No weekly price seen. No evidence on how often it is claimed.
- aibrify: "If we cannot deliver a quoted fix, you do not pay for it". Tickets are $100 or $300, diagnosis $100 credited, 90-day free repair [T16 #4]. Small ticket. No evidence it works at $2,000.
- Slopfix: pay in proportion to lines deleted, two-week warranty, free repo review, rejects jobs with too little dead weight [T19 #9]. Press coverage; no named clients.
- Most others show no guarantee [T8 #7]. MetaCTO and Agence Scroll give a free 48-hour audit [T20 #19].
- No dispute stories anywhere [T19 #6].

Reading:
- "Blow you away" is subjective. At $2,000 it invites a refund claim any time the buyer feels low. With a buyer base that is non-technical, budget-tight and already angry at platform charges [T1 #2, #3, T17 #8], a subjective clause is the likeliest route to a dispute.
- "Pay only if fixed" works at $100 to $300 where volume and automation absorb losses. At $2,000 the risk per job is too large unless the test is objective.
- A trust gap exists for a Lahore vendor [T15, T20 #16 to #18]. Some guarantee helps. It should be objective.

Recommended shape:
1. Audit: paid up front, not refundable once the report is delivered. Credited in full against a sprint ordered within 14 days (shape seen at 3 vendors [T16 #1]). Refund only if we miss the stated delivery date by more than 5 business days.
2. Sprint: objective guarantee. If an in-scope acceptance test still fails after our fix round, the fee share for that item is refunded. Item fee shares are written in Schedule A. Total refund cannot exceed the sprint fee.
3. Full refund trigger: written rescue-or-rebuild gate found wrong in the first 2 working days (the app is in fact a rebuild), and either side stops. Refund of unused work, less time spent. This protects both sides.
4. 30-day warranty on accepted in-scope fixes (free repair, not refund).
5. No refund for: change requests, client edits after the audit date, platform or third-party failure, unrotated secrets, "I changed my mind", or a result different from what the client imagined but within Schedule A.
6. Optional later test: "last-week refund" in the Wavect style on multi-week retainers only. Not for the first 30 days.

Cost view [assumptions]:
- Delivery cost for a week is about $300 to $600 even with a 2x overrun [T19 Appendix A, derived from $1,000 to $1,100 monthly engineer cost in BRIEF section 1].
- Acquisition cost is larger: $400 to $1,000 per client on vendor benchmarks [phase1-summary gate 2, T18].
- Expected refund cost per sprint = refund rate x refunded amount. If 5%, 10%, 15% of sprints are refunded in full ($2,000): $100, $200, $300 per sprint. If only per-item refunds, expect less. This is arithmetic, not data.

### 1.11 Payment terms and chargeback exposure by method
Recommended terms:
- Audit: 100% up front.
- Sprint: 50% at signing, 50% on delivery note, due on acceptance or deemed acceptance. Reasons: lowers cash at risk, matches buyer advice to use milestones and small paid first steps [T15 sec 6, T20 #18], and reduces the "paid and got nothing" fear [T4 sec 6]. 100% up front only for repeat clients or for bank transfer/Wise payers who accept the terms.
- Retainers: monthly in advance, cancel on 30 days notice.
- Late fees: simple, 1.5% a month. [GK]
- Invoice shows: legal entity name, scope summary, SOW number. Statement descriptor on card must be recognisable ("WANILE ..."). [GK]

Payment methods [GK, none of this was researched in Phase 1, check with each provider]:
| method | chargeback or reversal exposure | notes |
|---|---|---|
| Card via Stripe | High. Cardholder can dispute for roughly 120 days (varies by network). Dispute fee and lost amount. High dispute rates can put the account at risk | Easiest for buyers. Whether Wanile can receive card payments depends on its entity and account; confirm what it already uses |
| PayPal | High. Buyer protection and disputes. Funds can be held | Avoid for sprint-size invoices if possible |
| ACH / direct debit (US) | Medium. Unauthorised-debit returns possible for weeks | Needs US entity or provider |
| Bank wire / SWIFT | Low. Hard to reverse once settled | Slow, fees, buyer friction |
| Wise (bank-detail transfer) | Low. A push payment, no card chargeback | Good for AU, UK, EU, US clients |
| Escrow / milestone platform | Low, platform rules apply | Fee; fits trust gap; Upwork/Contra route has fees and platform control |
| Crypto | Not recommended | Brand and compliance risk |

Policy:
- Card allowed for the audit and for any single sprint invoice up to a threshold. Suggested threshold: $2,500 per invoice, paid only after the signed SOW. Above it: bank or Wise. [Assumption: set after talking to the payment provider.]
- Keep dispute rate far below any card-network warning level. The author recalls warning levels around 0.75% to 1% of transactions for common processors [GK, verify]. At our volume of a few payments a month, one dispute is a large rate. That is why the threshold and evidence pack matter.
- Evidence pack saved per client: signed SOW, Schedule A, daily progress notes, Loom links, delivery note, acceptance email or deemed-acceptance notice, access logs, repo commit history.

---

## 2. Chargeback and refund risk

### 2.1 Who the buyers are (what the evidence says)
- About 80% of Lovable users say they are non-technical (Lovable's own report, vendor data, unaudited) [T12 #4]. "Non-technical" means role, not seniority or budget (CEO: 55% have 11+ years of work experience).
- Only some have revenue. Sources conflict: 35% earn, about 1 in 10 earn directly [T12 #5].
- Small budgets. Buyer-posted budgets for confirmed AI-built apps are $20 to $1,250. Two $2,000 posts in Oct and Dec 2025. Two hardening posts at $1,500 and $2,500 in Oct 2026 where AI-built is not stated. Seller prices are 3 to 10 times higher [T17 #2, #3, #7; T21 sec 3].
- Burned before. Trustpilot reviewers say Lovable's AI repeated the same errors and cost them "thousands of dollars" in credits; refunds denied for glitches; support slow [T1 #2, #3]. A Replit reviewer reported about $500 a week [T2]. Another reviewer $607.70 in 3.5 days [T17 #8]. All weak, anecdotal, platform spend.
- Burned by freelancers: small-ticket stories of $500 to $1,000 lost, freelancer vanished [T4 #1].
- Distrust of offshore exists in old and scattered evidence [T15 #1, #4; T20 #17].
- Tag: these are mostly small-business owners, not funded teams [T4 sec 6].

Read (inference): buyers who have already lost money to platform credits and freelancers, and learned that refunds are denied, are more likely to use their card issuer as the refund channel. There is NO evidence in the tracks of rescue chargebacks. This is a plausible risk, not a measured one.

### 2.2 What triggers disputes
1. "I paid and nothing changed that I can see." Hardening work is invisible (RLS, secrets). Founders see no new screen.
2. Expectation gap: "fix my app" heard as "finish my app". Sellers who finish quote $15K to $50K over 4 to 8 weeks [T19 #2, Appendix A].
3. Regression: a new bug appears, caused by the client re-prompting, and is blamed on us [T19 #7].
4. Silence. Time zone gap, no progress notes.
5. Scope surprise: audit finds a rebuild-grade app.
6. A security event after we leave, blamed on us.
7. Credit fatigue: the client is already out of money and wants it back.
8. Trust: Lahore vendor, no known brand [T15, T20].
9. Unclear billing name on the card statement. [GK]
10. Fixed-price overrun on our side leading us to cut corners.

### 2.3 How to reduce them
- Written scope and acceptance tests before payment (section 1.1, 1.2).
- Daily written progress note: what was done, what was tested, what is next, what we need. Short. Same time each day.
- Loom walkthroughs at audit and at delivery. Make hidden work visible: show the RLS test failing before, passing after. Demoable checks are the best persuasion [T11 #6 sec 6].
- Before/after evidence pack: advisor output, test results, screenshots.
- Milestone invoices (50/50). No big up-front card payment.
- No card payment above the threshold (section 1.11).
- Recognisable statement descriptor and invoice name.
- Contract sent and signed before payment. Terms visible at checkout.
- A clear expectation call: "this is hardening, not finishing" in plain words; sales page says the same.
- Fast, friendly refund path for real failures (per-item refund). Winning a dispute costs more than a clean refund in goodwill. Rule of thumb: refund small, fight large with the evidence pack. [GK]
- Early warning: 48-hour check-in after delivery.
- Do not start work on weak-fit clients: if budget or expectations are wrong, say no in the audit.
- Collect a testimonial and permission to use their name at acceptance, while they are happy.
- Test in the first 30 days: track refund requests, disputes, and "expectation gap" notes per client.

---

## 3. Liability for apps we touch

### 3.1 Realistic exposures
1. We break something live. Example: a migration or RLS change locks users out or hides data; an auth change breaks logins; a Stripe change double-charges. Source of fear: AI agents deleting prod data [T11 #11]; Stripe misconfigs [T19 #13, $15,000 double-charge rescue case].
2. We miss a vulnerability. We fixed 20 items and the 21st is exploited. The client says "you audited it". Scanner-era platforms still miss runtime holes [T12 #13; T11 6b #7].
3. An existing breach is found mid-engagement. Example: open Supabase tables already read by others; keys exposed for weeks [T11 #9, #10]. Risk: we are blamed or asked to run the response. Legal clocks may start for the client (for example GDPR 72-hour notice to regulators for the controller) [GK].
4. Client data exposure during our work: our staff or tools touch real user data; a laptop or chat leaks it; secrets pasted in an AI tool.
5. Our own AI tools leak client code or secrets to a third party. [GK]
6. Our changes break a licence or cause an IP claim (section 1.5).
7. Reputational blame: breach stories spread fast (Tea, Moltbook, Lovable BOLA) [T11 #8, #9, #13].

### 3.2 Mitigations
Before work:
- Audit first. Dated baseline: git tag, advisor output, screenshots. This proves what was broken at start.
- Staging first. All changes go to a copy of the database and app. Production only after tests pass, in a planned window.
- Backup first. Restore tested once [T11 6b #13].
- Separate dev and prod databases. No AI agent holds production credentials [T11 #12].
- Written risk acceptance form: if the client declines a recommended fix (for example "do not rotate keys", "do not fix X in this sprint"), they sign that they accept the risk.
- Scope exclusions in the SOW (section 1.1).

During work:
- Two-person rule: one engineer, one lead reviewer on every production change [BRIEF section 2, T19].
- Change log and rollback plan per production change.
- Read-only or least-privilege access. Synthetic data on staging.
- No secrets in chat, tickets or AI prompts. Use a vault.

Contract:
- Security disclaimer wording (section 1.6). No "security guarantee" anywhere, including ads and landing page.
- Incident clause: if we find signs of an existing or new breach: stop, tell the client in writing within 24 hours, preserve evidence (logs, snapshots), recommend containment, client decides on any legal notifications. Helping with incident response is out of scope and billed separately. We are not liable for the pre-existing breach or its effects. [Lawyer item]
- Liability cap at fees paid (section 1.9).
- Client owns decisions about notifying users and regulators.
- Exclusion: no liability for loss caused by client not following our written recommendations.

Wrap-up:
- Handover pack: what changed, what is not fixed, residual risk list, monitoring set up [T11 6b #37, #38], "access revoked" checklist.
- Residual-risk letter: a plain list of known open issues and out-of-scope risks, signed or acknowledged. Pairs with the security disclaimer.

### 3.3 Insurance note
- Consider technology errors and omissions (professional indemnity) cover and cyber liability cover. [GK]
- Larger and funded clients often ask for a certificate. Having it also supports a higher liability cap.
- No premium or availability data for a Pakistan-based firm was found in the tracks. Ask a broker. Check whether the policy covers claims brought in the US, UK, AU and CA, and claims arising from AI-assisted work.
- Do not claim insurance in marketing unless it exists.

---

## 4. Ethics screen (intake rule)

BRIEF rule: we do not rescue apps for gambling or betting, interest-based lending, adult content, alcohol-centric businesses, tobacco and vaping. Flag crypto and borderline cases.

### 4.1 Rule
Exclude (RED, auto-decline):
- Gambling and betting: casinos, sportsbooks, poker, lotteries, paid-entry sweepstakes, fantasy sports with cash prizes, skill-game cash tournaments.
- Interest-based lending: payday, personal loans, credit cards, BNPL with interest or late fees, loan marketplaces and lead-gen for them.
- Adult content: pornography, erotic services, adult chat, adult creator platforms.
- Alcohol-centric: producers, sellers, delivery, alcohol-focused marketplaces or bars as the product.
- Tobacco and vaping: sellers, brands, delivery, marketplaces.

Flag for director review (AMBER, decline by default unless cleared):
- Crypto: exchanges, token launches or sales, leveraged trading, custody, staking or yield schemes, memecoin tools: decline. Wallet or analytics tools with no custody of user funds, tax tools, blockchain infrastructure: review. Reasons: fraud and sanctions risk, plus security stakes if funds are held, plus payment-processor restrictions.
- Interest-free or Islamic finance, earned wage access, fee-only financial tools: review (is the money product interest-based).
- Dating apps, social apps with adult content risk, user-generated content with weak moderation: review.
- Cannabis and CBD, kratom, supplements making medical claims: decline by default (not in the brief list; our suggestion).
- Apps for health data (PHI), children's data, or financial account access: review, because of data law (section 1.7).
- Alcohol or tobacco as a side feature (for example a restaurant app that lists beer): review. Rule: the product's main purpose decides.
- Political persuasion, surveillance or stalkerware, weapons, scams or multi-level schemes: decline (our suggestion).
- Anything illegal where the client is based.

Allowed (GREEN): everything else, subject to normal checks.

### 4.2 How to check at intake
1. Intake form (Tally or similar) has a required question: "What does your app do and who is it for?" plus a checkbox list: "Does your app involve any of: gambling or betting, loans with interest, adult content, alcohol, tobacco or vaping, crypto, health records, children under 13, other restricted?" Plus a signed statement.
2. Staff read the public site, app store pages and public marketing. Public pages only. No probing, no login, no vulnerability tests before engagement [BRIEF section 8 spirit].
3. Check company name, domain, social pages and payment descriptions (Stripe product names are visible on public checkout pages).
4. Keyword flag on the form text: bet, wager, casino, odds, loan, APR, payday, credit, adult, NSFW, escort, vape, cigar, liquor, wine, beer, crypto, token, coin, DeFi, CBD. A hit means manual review, not auto-decline.
5. RED = decline politely with a fixed template. AMBER = director decision within 2 business days. Log every decision.
6. Contract clause: client warrants its business is lawful and does not fall in the excluded list; we may stop and refund unused work if we learn otherwise mid-engagement (the audit also reads the code and data model, so this is a second check). Prefer a "no fault, pro-rata" exit to avoid disputes.
7. Re-check at audit: the code and tables often reveal products the intake form missed.
8. Payment processors have their own restricted lists. [GK] Declining these clients also protects our own payment account.

---

## 5. Other risks, one paragraph each

### 5.1 Buyer budgets (tracks 7, 17, 21)
The biggest commercial risk. Confirmed buyer budgets for AI-built apps sit at $20 to $1,250 on Upwork and Freelancer.com [T17 #2]. Two $2,000 posts exist (Twilio+Stripe for a Lovable app, 2025-10-28; Base44 launch and QA, 2025-12-31) [T21 sec 3]. Two Oct 2026 hardening posts at $2,500 and $1,500 do not say AI-built [T17 #3]. Fiverr floor: 50 gigs, median $25 to $30, max $250 [T21 #9]. Sellers list $1,400 to $2,500 "from" [T21 #7]. No named buyer paying $1,500+ was found anywhere [phase1-summary gate 1]. Reddit was unreachable, so this is partly a tool limit. Risk to us: the paying pool may be thin and refund-sensitive. Mitigation: qualify on revenue and users at intake; start with the paid audit as a filter; test price in the first 30 days; accept that most inbound is below price.

### 5.2 Reputation and brand risk
The category has a thin-advertorial image: an HN commenter called a cleanup article "a thin advertorial for their services" [T19 sec 4]; Slopfix drew pushback ("$200 subscription gets similar value") [T21 #13]; one outlet called a cleanup vendor an extortion site (unreliable, uncorroborated) [T19 #9]. Cold "I found a vulnerability" outreach is seen as a nuisance and any ask for money looks like extortion [T20 #26]. Search results for rescue terms are already crowded with agency pages [T6 #11]. A failed or disputed rescue could appear as a public review. Wanile's main brand is moving upmarket to AI operations [BRIEF Q10]. Mitigation: decide the brand split in model/brand.md; keep case studies consent-based; no extortion-like outreach; objective guarantee; respond to every public complaint politely and fast. No evidence on reputational harm from this niche was found.

### 5.3 Platform risk (tracks 12, 20)
Two directions. Shrink: Lovable ships scanners, RLS checks and a Wiz integration (2026-05-07) [T12 #11]; Replit ships a Security Agent (2026-04-21) and black-box pen tests (2026-08-17) [T12 #13]; Lovable Cloud is a built-in backend on by default since 2025-09-29 [T12 #12, T20 #3]. These erase the cheapest faults. Grow: scanners miss runtime holes (Replit's own admin dashboard example) [T12 #13]; volume is about 1M new Lovable projects a week (vendor) [T12 #3]; Cloud to own-Supabase migration is manual [T20 #4]; Supabase key deprecation by end of 2026 [T11 #14]; no in-house done-for-you rescue service at Lovable, Replit, Bolt or Base44 (weak, negative) [T20 #2]. Replit routes experts to Contra [T20 #1]. Lovable has a partner directory and its own pages conflict about the old Experts programme [T20 #7]. Risk: a platform launches its own expert service or the directory captures lead flow. Mitigation: do not build the business on one platform's programme; keep offers platform-neutral (hardening, payments, migration); watch platform announcements monthly.

### 5.4 Trust in a Lahore vendor (tracks 15, 20)
Evidence is old and thin. A 2024 job post barred Indian and Pakistani applicants [T15 #1]; advice blogs say buyers expect a Pakistan discount [T15 #3]; one relayed BusinessWeek-style buyer comment about bad Pakistani outsourcing experience (about 2 years old, relayed by a vendor) [T20 #17]; a Pakistani outlet calls the scammer stereotype a myth and notes NDAs stop firms showing work [T20 #17]. No 2025-26 buyer voice about Pakistan for rescue work was found [T20 #16]. Pakistani sellers already advertise this exact service at floor prices ($17/hr, Fiverr $40 to $100) [T21 #5], which anchors perception. Pakistani agencies that sell abroad lead with a US address and show Pakistan second [T15 #8]. Proof that wins trust per sources (untested): referrals, verifiable reviews, Western-style contract, small paid first step, client owns repo and accounts, reachable references [T20 #18]. Mitigation: paid audit as a trial; client-owned accounts; objective guarantee; named overlap hours; consent-based references; Clutch profile (small Lahore agencies have 16 to 61 reviews [T20 #20]); do not hide Lahore but do not lead with it. Contract points: governing law and a neutral venue to reassure clients (lawyer item).

### 5.5 AI tools shrinking the gap
Three forces. (1) Platform scanners and agents fix basic issues [T12 #11, #13]. (2) Builders can use general AI coding tools to fix their own apps; an HN commenter said a $200 subscription gives similar value to Slopfix's $10k week [T21 #13]. (3) Rescue vendors themselves use AI, so price falls: Slopfix claims cuts "by up to 65%" with AI agents [T19 #8]; feature work 60 to 90 minutes becoming 10 to 15 [T19 #8, seller claim]. Counter: AI agents also cause damage (Replit database deletion [T11 #11]; three different error-handling patterns in one agent run [T19 #8]); auth, data model and payment logic still need a human [T19 #8]. Risk: the audit gets commoditised first. Mitigation: sell outcomes with proof (acceptance tests, sign-off), not hours; use AI inside our delivery to protect margin (cost is already low at about $300 to $600 a week); keep a cost-down path; revisit pricing every quarter.

### 5.6 Dependence on one platform's terms
Lovable dominates the stack we target (ARR about $500M to $600M reported, vendor) [T12 #1]. Its terms can change: the Expert programme terms say criteria can change any time [T9 #2]; the old Experts page said the programme "is no longer active" and was replaced by the Solution Partner Program [T20 #7]; the Solution Partner track is built to sell Lovable Enterprise licences and gives rescue shops no leads [T9, phase 1 table]. Platform output ownership currently favours the customer [WS1]. Lovable disputes platform responsibility for RLS [T11 #1]. Replit and Base44 lock in backends [T2]. Risks: terms change on ownership, export, account sharing, or partner status; a platform bug (Lovable BOLA, 48 days [T11 #9]) hits clients on our watch. Mitigation: re-read key platform terms every quarter; contract says platform failures are excluded; client-owned accounts; record platform and version in the audit; offer migration to client-owned Supabase and GitHub as a standard product [T20 #4].

### 5.7 Delivery overrun and scope creep (adds to the brief's list)
Fixed price on an unknown code base can lose money if a job is rebuild-grade. HN freelancers report at least two assessments that ended in a rewrite [T19 #5]. No published share of rescues that became rebuilds [T19 #5]. Mitigation: audit gate; stop-loss; change control; explicit size limit (section 1.1).

### 5.8 Payment and account risk
A high dispute rate could cost the payment account. Pakistan-based collection may have its own limits. [GK] Not researched in Phase 1. Mitigation: confirm payment method with the company's finance lead before launch; prefer Wise or bank for larger invoices.

### 5.9 Legal and marketing-law risk
Cold outbound has real limits: no B2B exemption in CAN-SPAM, CASL friction in Canada, Australia consent rules, UK sole-trader consent [T20 #21 to #24]. Mitigation: US-first, role-relevant messages, working opt-out and address; lawyer check. Reply rate planning: 3 to 6% at best, before any booked call [T20 #25].

---

## 6. Risk register

Likelihood and impact are the author's judgment. L = low, M = medium, H = high.

| # | risk | likelihood | impact | mitigation | evidence pointer |
|---|---|---|---|---|---|
| 1 | Buyer budgets too small for $2,000 work; most inbound below price | H | H | Intake filter on revenue/users; paid audit as filter; price test in 30 days | T17 #2, #3, #7; T21 #9; phase1 gate 1 |
| 2 | Refund claims after "I can't see what changed" | M | M | Loom, before/after tests, acceptance sign-off, objective guarantee | T1 #3; T19 #6 (no stories found); sec 2 |
| 3 | Card chargeback on a large invoice | M | M | 50/50 milestones, card threshold, evidence pack, bank/Wise for larger | sec 1.11, 2 [GK]; no tracks evidence |
| 4 | Scope creep: "fix" becomes "finish" | H | H | Schedule A tied to audit, exclusions list, change control | T19 #2, #7; T21 #8 |
| 5 | Client re-prompts the AI tool and breaks fixes | M | M | Code freeze clause, branch review, regression tests | T19 #7, sec 6 |
| 6 | App is rebuild-grade after audit | M | M | Rescue-or-rebuild gate, separate quote, stop-loss | T19 #5, Appendix A; T11 6b |
| 7 | We break something live | M | H | Staging first, backup, restore test, two-person review, rollback plan | T11 #11, #12; T19 #13 |
| 8 | We miss a vulnerability that is later exploited | M | H | Scope list, no "secure" wording, disclaimer, residual-risk letter, liability cap | T11 #6, 6b; T12 #13 |
| 9 | Existing breach found mid-engagement | M | H | Dated baseline, incident clause, 24-hour written notice, client decides on notifications | T11 #8, #9, #10; T3 #2 |
| 10 | Client data exposed during our work | L | H | Synthetic data on staging, least privilege, vault, DPA, no data on laptops | sec 1.7, 3.2 [GK] |
| 11 | Secrets not rotated, later abused, we get blamed | M | M | Rotation duty on client, signed risk acceptance, exclusion | T11 #9, #10 |
| 12 | Cross-border data law (GDPR, Privacy Act, PIPEDA) non-compliance | M | M | DPA, SCC/IDTA, avoid production data, lawyer review | sec 1.7 [GK]; T20 #22 to #24 (marketing only) |
| 13 | Liability claim larger than fee | L | H | Cap at fees paid, exclusions, insurance, written scope | sec 1.9, 3.3 [GK] |
| 14 | Platform ships built-in fixes; basic security demand shrinks | M | M | Sell migration, payments, hardening, finishing; track announcements | T12 #11, #13; T20 #2 |
| 15 | Platform launches own expert service or directory takes leads | M | M | Platform-neutral offer; multiple channels; join directories as a bonus only | T20 #1, #7; T9 |
| 16 | Platform terms change (ownership, export, accounts, partner rules) | L | M | Quarterly terms review; client-owned accounts; contract excludes platform failure | WS1; T9 #2; T20 #7 |
| 17 | Lahore trust gap lowers conversion | M | M | Paid audit trial, references, Clutch, overlap hours, objective guarantee, neutral law | T15 #1, #3, #8; T20 #16 to #18 |
| 18 | AI tools shrink the gap; price pressure | H | M | Outcome pricing with acceptance tests; AI inside our delivery; re-price quarterly | T12 #13; T19 #8; T21 #13 |
| 19 | Reputation hit from a public complaint or breach story | L | H | Consent-based case studies, fast response, no extortion-style outreach, objective refund | T20 #26; T11 #13 |
| 20 | Brand damage to Wanile's upmarket move | M | M | Brand decision in model/brand.md; separate brand option | BRIEF Q10 |
| 21 | Ethics breach: take on a barred client | L | H | Intake screen, keyword flags, RED/AMBER log, mid-engagement exit clause | sec 4 |
| 22 | Payment account frozen from disputes or country limits | L | H | Confirm methods with finance lead; Wise/bank for large invoices; dispute rate watch | sec 1.11, 5.8 [GK] |
| 23 | Outbound marketing law breach | M | M | US-first, compliant sender details, opt-out, lawyer check | T20 #21 to #25 |
| 24 | AI-generated code carries third-party licence or copyright issues | L | M | Dependency licence check, no provenance warranty, client warranty | WS1; sec 1.5 [GK] |
| 25 | Retainer conversion lower than planned (revenue, not risk to safety) | H | M | Do not rely on retainers; test in first 5 rescues | T20 #11, #12; T14 |

---

## 7. Not legal advice. What a lawyer must review.

- This document is a planning draft. It is not legal advice. Nothing here has been checked by a lawyer.
- Every [GK] item is the author's general knowledge and may be wrong or out of date.
- Platform terms in [WS1] were read from search snippets, not the live pages.
- A lawyer with software services experience in at least the UK or US, plus input for Pakistan, Australia and Canada, should review the template before first use.

The three clauses most worth a lawyer's time:
1. Limitation of liability plus security disclaimer plus incident clause. Check enforceability across the UK, US, Australia, Canada (unfair contract terms, consumer and small-business rules, carve-outs), whether a cap at "fees paid" holds, and how to word "no guarantee" without sounding evasive. This is the clause that decides whether one breach can end the company.
2. Data protection and cross-border terms. Controller and processor roles, DPA content, transfer mechanism from the EU, UK, Australia and Canada to Pakistan, sub-processors including AI tools, breach notification timing, and what we may do with client data on staging. Also the rule on health, children's and financial data.
3. IP assignment, AI-generated code and refund/guarantee wording, together with governing law and dispute resolution. Check the assignment on full payment, the carve-out for our tooling, licence and provenance warranty for AI-generated code, whether the per-item refund and the 30-day warranty create consumer-style rights, and which court or arbitration venue is acceptable to clients and enforceable against a Pakistan entity.
(Honourable mention: payment terms and late fees by jurisdiction.)

---

## 8. Open items for the orchestrator
- Confirm how Wanile receives payments today, and whether card payment is available. Then set the card threshold.
- Confirm audit price and sprint price from model/offers.md and align the refund shape and the fee-share table.
- Ask a lawyer for a first review quote before Day 1 of the 30-day test.
- Check the platform terms pages directly when network access is available (Lovable product terms and terms of service; Replit, Base44, Bolt, v0).
- Add a track 22 pointer (buyer reviews) when it lands.
- Phase 3 verification: [WS1] result and all [GK] items need a source or a lawyer sign-off. They were not in the Phase 1 cache.
