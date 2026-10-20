# Delivery plan: the standard rescue (Phase 2, delivery planner)

Date: 2026-10-20. Stack: Lovable / React / Vite / Supabase (+ Stripe where the app takes money).
Method: modelling only, from Phase 1 files. No web searches were used. No facts were added from outside the tracks, except items marked [E].

## How to read this file
- `t11 #14` = track 11, key finding 14. `t11 6b-14` = item 14 of the track 11 checklist (section 6b). `t19 5b` = track 19, section 5b table. `t20`, `t21`, `t12`, `t02` work the same way.
- [S] = a Phase 1 file names it. [E] = Wanile engineering judgment. Nothing else.
- Most [S] items are seller or vendor claims. They are not tested.
- Independent sources behind [S]: Supabase docs (B1, B3, B4, B5, C1, C3), the NVD record for CVE-2025-48757 (B1), and news on the Replit incident (0.2).
- "Our estimate" means we made the number up from experience and the Phase 1 fragments. It is NOT published data.
- Hours are for a small app: under about 20 to 30k lines, one stack, Supabase + Stripe (the size used in t19 appendix A).
- Cost inputs from the brief: $1,000 to $1,100 per engineer-month, USD billing, 20 engineers.

## The one finding that shapes everything
- No published hours-per-task table exists (t19 #1, t11 #15). We checked.
- Our own bottom-up estimate (section 3) says the week-one hardening set costs about 46 engineer-hours with AI help (range 25 to 70).
- A 40-hour week does not fit that safely. A safe week holds about 32 hours of checklist work (80% of 40, 8 hours kept for review fixes, client questions and overrun).
- So "$2,000 a week" fits a small, clean app. A typical Lovable app with Stripe is 2 sprint-weeks.
- Rule: size the sprint from the audit hours, not from a fixed week. Section 5 has the rule.
- This also matches the seller range: 1 to 2 week remediation sprints, 2 to 6 weeks (Red Leg), 4 weeks for a small SaaS (t19 #2). All vendor claims.

---

## 1. The standard playbook: Day 0 to Day 5

Frame:
- Day 0 = intake. Day 1 = audit. Days 2 to 4 = fix. Day 5 = verify and hand over.
- Day 0 and Day 1 can be sold as the paid audit, credited to the sprint (credited audits: Vibe Code Rescue $299 in t19 #6; TopDevz $4,950 in t21 #7; note t20 #19 saw mostly free 48-hour audits instead). Offer design is in offers.md.
- Engineer hours per day: 3, 8, 8, 8, 8, 5 = 40. Lead hours per day: 1, 2, 1, 1.5, 1, 1.5 = 8.
- Client time zone matters. Lahore is UTC+5. Send the daily update before the client's working day starts (UK/EU) or at their end of day (US). [E]

### Day 0: Intake (engineer 3 h, lead 1 h)
Engineer does:
- 20 to 30 minute intake call. Ask: platform, what is broken, users, revenue, payments, what they spent, deadline, who else edits the app.
- Check the ethics list from BRIEF section 5 (no gambling, interest lending, adult, alcohol, tobacco; flag crypto).
- Get access: GitHub repo (client-owned), Supabase invite, Stripe (test mode or read-only), hosting, domain registrar (read-only), Lovable project (view).
- Snapshot database and storage. Do this before touching anything (item 0.2).
- Start the freeze (section 6). Tell the client in writing.
- Sign the contract and the written test authorisation (risk.md has the terms).
Lead reviews:
- Go or no-go on fit: platform (Lovable/Supabase = in; Base44 backend = likely rebuild, see t02 #5), app size, ethics list, red flags.
- Checks that access is client-owned, not ours.
Client receives:
- Welcome note, access checklist, freeze rules, what happens each day.
- Date and time of the Day 1 audit delivery.
Client does: gives access within 24 hours. Stops prompting the AI tool.

### Day 1: Audit (engineer 8 h, lead 2 h)
Engineer does:
- Build locally. Record baseline (item 0.4). Run secret scan, dependency audit, Supabase Security and Performance Advisors.
- Read-only probe of RLS on a staging copy (never production data). Use two test users and the anon key.
- AI-assisted read-only audit pass over the repo (t19 #8: an open-source Claude Code plugin does this).
- Fill the checklist (section 3): present or not, severity, hours.
- Measure triage signals S1 to S6 (section 5).
- Draft the acceptance test list and the parked list.
- Write the audit report (2 to 4 pages).
Lead reviews:
- The audit report line by line for the three high-risk areas: RLS, secrets, auth.
- The triage decision: rescue sprint, extended rescue, or rebuild quote.
- Signs the scope. Cuts anything that does not fit 32 hours.
Client receives (end of Day 1):
- Audit report: findings, severity, what we will fix, what we will not.
- Fixed scope + acceptance test list (for signature) + parked list v1.
- Triage result with price, or a rebuild quote.
Gate: no fix work starts until the client signs the acceptance list. If it is not signed by Day 2 morning, the clock waits.

### Day 2: Secrets and database (engineer 8 h, lead 1 h)
Engineer does:
- Rotate exposed keys with the client. Move secrets server-side (C1 to C4).
- Create staging: second Supabase project or branch, preview deploy, own env vars (F2).
- RLS on every table. Start with the tables that hold user data and money (B1 to B4).
- All database changes as migrations in git (B7 starts, full cleanup is W2).
- Use AI for inventory, policy drafts and migration scaffolding. Engineer writes and checks every policy.
Lead reviews (1 h):
- Every pull request that touches policies, grants or keys.
Client receives:
- Daily update (done, next, decisions needed, hours used vs plan).
- Key rotation steps they must do in their own accounts.
- Staging URL v0.

### Day 3: Auth, functions, RLS tests (engineer 8 h, lead 1.5 h)
Engineer does:
- Server-side route guards and ownership checks (A2, A5). Roles (A3). Redirect URLs (A4).
- Edge functions: JWT check, input validation, CORS (E1).
- Write the RLS test harness (I2). It runs in CI.
- If the app takes money: start Stripe webhook fixes in test mode (D1, D2).
- Checkpoint: compare hours used vs plan. If above 1.25x the plan, tell the lead the same day.
Lead reviews (1.5 h):
- Auth and function pull requests.
- Tries to break the RLS tests: writes two negative cases of his own.
- Decides at the checkpoint: cut to parked, or ask the client for a change request or extended sprint.
Client receives:
- Daily update. Staging URL with the fixes so far.
- Two journeys to test on staging (their own eyes on the app).

### Day 4: Payments, deploy, tests, CI (engineer 8 h, lead 1 h)
Engineer does:
- Finish payments in Stripe test mode (D3). Full test-mode payment on staging.
- Smoke tests for the acceptance journeys (I1). CI: build, lint, tests, secret scan, audit (I3, C5, C6).
- Domain, HTTPS, DNS email records, security headers (F1, F3).
- CLAUDE.md / AGENTS.md and lint rules into the repo (H4). Generated types (H3).
Lead reviews (1 h):
- Runs the signed acceptance list himself on staging. Marks pass or fail.
- Reviews CI config and branch protection.
Client receives:
- Daily update with a table: each acceptance test, pass or fail.
- Short list of what is left for Day 5 and what is parked.

### Day 5: Verify and hand over (engineer 5 h, lead 1.5 h)
Engineer does:
- Re-run the full acceptance list on staging. All must pass.
- Release to production with a rollback ready, in a low-traffic window, before noon client time. Do not release on a Friday evening. If Day 5 is a Friday, release in the morning or move the release to Monday.
- Write the runbook (AI drafts, engineer edits). Record the 15 to 20 minute handover video.
- Security sign-off list. Parked list with estimates. Rotate keys we touched. Remove our access or agree what stays.
Lead reviews (1.5 h):
- Final sign-off: checks every artefact in section 7 exists and opens.
- 30 minute handover call with the client.
Client receives:
- The full artefact pack (section 7).
- Acceptance form to sign. Invoice.
- Menu of next steps: parked items quote, maintenance plan (basis: t11 6b-38).
- Warranty start. Length is set in risk.md. The only published example is Slopfix: 2 weeks (t19 #9, vendor).

### Hours check
| | D0 | D1 | D2 | D3 | D4 | D5 | Total |
|---|---|---|---|---|---|---|---|
| Engineer | 3 | 8 | 8 | 8 | 8 | 5 | 40 |
| Lead | 1 | 2 | 1 | 1.5 | 1 | 1.5 | 8 |

---

## 2. The tools

Principle: tools are cheap for us. The expensive part is engineer attention on RLS, auth and payments. Build the harnesses once. Reuse them on every rescue. [E]

| Tool | What we use it for | Notes | Tag |
|---|---|---|---|
| Repo access | Client-owned GitHub repo. We get write access on a branch. Branch protection on main. Pull request required. | Lovable can sync to GitHub (t01 #6 says builders export to GitHub and hand the repo to a contractor). Check how sync writes to the repo on Day 0. | [E] |
| Supabase Security Advisor and Performance Advisor | Run on Day 1 and again on Day 5. Keep before and after exports. | Security Advisor: t11 6b-10 (Supabase production checklist). Performance Advisor is [E]. | [S]/[E] |
| Supabase CLI | Pull schema into migrations in git. Run local stack. Run DB tests. | Prefer local or staging branch over remote production. | [E] |
| RLS test harness | Two test users + anon client. For each table: A cannot read or write B, anon reads nothing private, owner can do owner actions. Runs in CI. | Build once as a template (pgTAP or a script). This is the main reusable asset. | [E] |
| Secret scanning | Scan full git history, build output, env files. Pre-commit and CI. | Use a scanner such as gitleaks or trufflehog. Also check keys pasted into Lovable chat (inference from t11 #9-10). | [E] |
| Dependency audit | `npm audit` or OSV scanner. Fix criticals. Lockfile committed. | Not a Phase 1 finding. Normal practice. | [E] |
| Stripe test mode | Separate test keys. Stripe CLI forwards webhooks to staging. Trigger failed payment, refund, cancel events. | One small live payment only with client approval (D3). | [E] |
| Staging deploy | Preview deploy from a branch + separate Supabase project. Client-owned hosting. | Gives the client a URL to test. Required artefact. | [E] |
| Monitoring | Error tracking (Sentry is the example in t11 6b-37), uptime check, Supabase log alerts, Stripe webhook failure alert. | W2 item. Often becomes part of the maintenance plan. | [E] |
| Static checks | ESLint, tsc, Prettier, Lighthouse. | Baseline numbers on Day 1. | [E] |
| Time log | Every hour tagged to a checklist item and "AI-assisted yes/no". | This is how we get the missing fix-time data (section 8). | [E] |
| Client channel | One shared channel + one daily written update. Parked list in a shared doc. | Keeps change control visible. | [E] |

### How Claude Code or Cursor is used
Evidence from track 19 (all weak: vendor marketing or one-person anecdotes). No percentage of rescue work automated has been published (t19 #8).

What the evidence says automates:
- Cutting dead code. Slopfix says its team uses AI agents to cut repos "by up to 65%" and its example went from 100,000 to 35,000 lines. It hands over a CLAUDE.md, lint rules and CI checks (t19 #8, #9). Vendor.
- Read-only audits. An open-source Claude Code plugin audits a repo across eight lenses and writes a report without touching code (t19 #8).
- Feature-style edits. McKelvey (a seller) says 60 to 90 minutes by hand became 10 to 15 minutes with Claude Code (t19 #8). Self-reported, and about features, not rescues.
- Rough overall gains. A Substack report says about 30% productivity gain, with big gains on large refactors (t19 #8). HN "100 hour gap" commenters say the AI speedup falls to about 2 to 3x once back-and-forth and review are counted (t19 #3).

What the evidence says does not automate:
- Consistency. A dev.to author says an agent produced three different error-handling patterns and cost a Saturday for an hour of manual work (t19 #8, #32).
- UI and state. The Substack report says the tool floundered on UI and state.
- Auth, data model, payments. The track 19 read is that these still need a human (t19 #8). Agency case: Anish Gandhi closed 73 bugs on a Lovable app with Claude Code, and every commit passes a human gate (t19 #8).
- Self-checking. A Cursor forum post says the session that wrote the fix should not be the one that says it is fixed (t19 N=34 summary).
- Regression loops: fixing one thing breaks another. Freeze known-good behaviour with tests (AppStuck, vendor, t19 #7).
- Production access. The Replit agent deleted a live production database in a code freeze (t11 #11, t02 #1).

Our rules (all [E], built from the above):
1. AI-led items (marked "AI-led" in section 3): inventory, scans and triage of findings, dead-code candidates, types, README and runbook drafts, CI config, test scaffolding, repetitive policy drafts.
2. Human-led items: RLS policy design, auth model, ownership checks, payments, triage decision, sign-off.
3. AI works on a branch and on staging data only. Never on production credentials. Never with the service key in its context.
4. A different person (or a fresh session) reviews every AI change. The lead reviews every pull request that touches policies, keys, auth or payments.
5. Plan mode first. Read the plan before it changes code (a tip seen in t19 #32 summary).
6. Hard rules go in CLAUDE.md in the repo: no full component rewrites when a local patch will do; no public API changes without asking (AppStuck rules, t19 N=34 summary).
7. Our assumption for hours: AI cuts AI-led items by 30% to 50% and human-led items by 0 to 10%. This is our estimate. The first 3 audits test it.

---

## 3. The checklist

### How it was built
- Base: track 11 section 6b (38 items, 1 to 38).
- Merged in: the problem-class table in track 19 section 5b (9 sellers + Wiz via tool summary).
- Added from other tracks: Lovable Cloud migration (t20 #4), AI guardrails files (t19 #8), staging/prod split (t19 5b), secret scan and dependency audit steps (our practice).
- Mapping from track 11 numbers: 1 to A1, 2 to A2, 3 to A3, 4 to A4, 5 to A5, 6 to 9 to B1 to B4, 10 to B5, 11 to B6, 12 to B7, 13 to B8, 14 to C1, 15 to C2, 16 to C3, 17 to C4, 18 to 20 to D1 to D4, 21 to E1, 22 to E2, 23 to E3, 24 to E4, 25 to F1, 26 to F2 and 0.1, 27 to F3, 28 to 0.3, 29 and 30 to G1 to G3, 31 to H1, 32 to H2, 33 to H3, 34 to H5, 35 to I1, I2, I4, 36 to I3, 37 to J1, 38 to J2.
- Tag changes: seven items that track 11 marked [E] are now [S] because track 19 shows at least one seller naming them (A2, C2, D1, E3, F2, H1, I1). That is vendor-grade support only.
- A check on track 19: its finding 4 says several items appear in "at least 5 of 9" sources. Its own table shows: secrets 5, access control 5, payments 3, error handling 3, no tests or CI 2, fake auth 2, staging/prod split 1. Only secrets and access control reach 5. Six of the nine sources name at least one security or data item. We use the table counts.

### Tiers
- W1 = in the 1-week hardening sprint (security, data, staging, tests, handover).
- IF = also in week one, but only if the app has that feature (payments, LLM calls, keys in browser, admin tools).
- W2 = second sprint-week (code quality, performance, monitoring, wider tests).
- X = separate quote.

### Hours column
- "Hours (our est.)" = low to high, one engineer, small app, before AI help. OUR ESTIMATE, NOT PUBLISHED DATA.
- Only published fragments: 2 to 4 hours for the five most common patterns together (vendor, t19 #1), about 2 hours for a key exposure (vendor sample audit), 1 to 2 days per fix (vendor claim). Our per-item bands are higher because they include testing and a review pass.
- "AI" column: AI-led items get a 30% to 50% cut in section 3 totals. Human-led items get 0 to 10%.

### 0. Intake and baseline (Day 0 to 1)

| # | Tag | Item | Tier | Hours (our est.) | AI | Source or note |
|---|---|---|---|---|---|---|
| 0.1 | [E] | Get client-owned GitHub repo access. If Lovable is not synced to GitHub, set it up. Work on a branch we control. | W1 | 0.5 to 1 | Human-led | Check how Lovable writes to the repo before promising a freeze (see section 6). |
| 0.2 | [S] | Snapshot database and storage before any change. No AI agent gets production credentials. | W1 | 0.5 to 1 | Human-led | t11 #11-12 (Replit deleted a live DB). |
| 0.3 | [E] | Account map: Lovable, Supabase, Stripe, domain, DNS, email. Client stays owner. We join as collaborator. | W1 | 0.5 to 1 | Human-led | t11 6b-28 [E]. |
| 0.4 | [E] | Build and run locally. Record baseline: build, lint, type errors, file count, lines, bundle size. | W1 | 1 to 2 | AI-led | Feeds triage signals S1, S6. |
| 0.5 | [E] | Written test authorisation. Draft acceptance test list (5 to 10 user journeys). | W1 | 1 to 2 | Human-led | Contract text is in risk.md. |
| 0.6 | [E] | Inventory: tables, edge functions, third-party services, env vars, cron jobs, who has access. | W1 | 1 to 2 | AI-led | Read-only AI audit pass fits here (t19 #8). |

### A. Auth

| # | Tag | Item | Tier | Hours (our est.) | AI | Source or note |
|---|---|---|---|---|---|---|
| A1 | [E] | Map auth flows. Test sign up, sign in, reset, email confirm on the live domain. | W1 | 0.5 to 1.5 | AI-led | t11 6b-1 [E]. |
| A2 | [S] | Route guards enforced by server or RLS, not only hidden in the React UI. Remove fake or client-side auth. | W1 | 1 to 3 | Human-led | t19 5b: fake auth named by 2 of 9 (McKelvey, Wiz). |
| A3 | [E] | Roles (admin vs user) not stored in a user-editable field or localStorage. | W1 | 0.5 to 1 | Human-led | t11 6b-3 [E]. |
| A4 | [E] | Session expiry, redirect URLs, email templates use the production domain. | W1 | 0.5 to 1 | Human-led | t11 6b-4 [E]. |
| A5 | [S] | Every endpoint that takes an object id checks ownership (BOLA). Includes our own edge functions. | W1 | 1 to 3 | Human-led | t11 finding 9 (Lovable 2026 backend bug). |
| A6 | [S] | Internal or admin tools are not public without auth. | IF | 0.5 to 1.5 | Human-led | t19 5b: Wiz (via tool summary). |

### B. RLS and database

| # | Tag | Item | Tier | Hours (our est.) | AI | Source or note |
|---|---|---|---|---|---|---|
| B1 | [S] | List every table in the exposed schema. RLS on for all. | W1 | 0.5 to 1 | Human-led | t11 #1, #3, #14. CVE-2025-48757. |
| B2 | [S] | Replace allow-all or missing policies with per-user policies. Prove they work, not just exist. | W1 | 3 to 8 | Human-led | t11 #1: scanner checked presence, not effect (tool summary). Biggest single item. |
| B3 | [S] | Tables made in SQL Editor or by migration tools: check RLS by hand. | W1 | 0.5 to 1 | Human-led | t11 #14 (Supabase docs). |
| B4 | [S] | Revoke default grants to anon and authenticated where not needed. | W1 | 0.5 to 1 | Human-led | t11 section 4 (Supabase docs quote). |
| B5 | [S] | Run Supabase Security Advisor. Fix every item. Run Performance Advisor too. | W1 | 1 to 2 | AI-led | t11 6b-10 (cites finding 14). Performance Advisor is [E]. |
| B6 | [E] | Views, SECURITY DEFINER functions, storage buckets and their policies. | W1 | 1 to 3 | AI-led | t11 6b-11 [E]. The Tea case (t11 finding 13) is not AI-proven. |
| B7 | [E] | Schema integrity: foreign keys, indexes, unique constraints, timestamps. Migrations in git. | W2 | 2 to 6 | Human-led | t11 6b-12 [E]. Feeds triage S3. |
| B8 | [S] | Backups on. Restore tested once. Dev and prod databases separate. | W1 | 1 to 2 | Human-led | t11 findings 11-12 (6b-13); t19 5b (Wavect: staging and prod share one DB). |

### C. Secrets, keys and dependencies

| # | Tag | Item | Tier | Hours (our est.) | AI | Source or note |
|---|---|---|---|---|---|---|
| C1 | [S] | service_role / secret key never in client code or repo. | W1 | 0.5 to 1 | Human-led | t11 #14 (Supabase docs). |
| C2 | [S] | Scan repo history, build output, env files for third-party keys. Rotate every hit. Ask about keys pasted in Lovable chat. | W1 | 1 to 3 | AI-led | t19 (vibecoding.app, vendor: most common finding). Chat exposure is inference from t11 #9-10. |
| C3 | [S] | Plan move from anon / service_role keys to publishable / secret keys before the end-2026 deprecation. Check the current date on Supabase's page first. | IF | 1 to 3 | Human-led | t11 #14. Deadline is about 10 weeks from today (2026-10-20). |
| C4 | [E] | Move third-party calls into edge functions. Secrets in the platform secret store. | IF | 2 to 5 | Human-led | t11 6b-17 [E]. Only if keys are in the browser. |
| C5 | [E] | Secret scanning in pre-commit and in CI. | W1 | 0.5 to 1 | AI-led | [E]. New step, not in t11. |
| C6 | [E] | Dependency audit. Fix criticals. Commit the lockfile. | W1 | 0.5 to 1.5 | AI-led | [E]. |

### D. Payments (only if the app takes money)

| # | Tag | Item | Tier | Hours (our est.) | AI | Source or note |
|---|---|---|---|---|---|---|
| D1 | [S] | Stripe webhooks: signature verified, idempotent, handles failed payment, refund, cancel. Check the JWT setting on the webhook function. | IF | 3 to 8 | Human-led | t19 5b: payments named by 3 of 9; systag found JWT off on webhooks. Vendor. |
| D2 | [E] | Entitlements come from the webhook-updated database, not a client flag or redirect URL. | IF | 2 to 4 | Human-led | t11 6b-19 [E]. McKelvey: Stripe 'just a button' case (t19 section 5 table). |
| D3 | [E] | Test and live keys separated. Full test-mode payment on staging. One small live payment, with client approval. | IF | 1 to 3 | Human-led | t11 6b-20 [E]. |
| D4 | [E] | Tax, invoices, customer portal as scoped. | X | 2 to 6 | Human-led | t11 6b-20 [E]. Not in the standard week. |

### E. Edge functions and APIs

| # | Tag | Item | Tier | Hours (our est.) | AI | Source or note |
|---|---|---|---|---|---|---|
| E1 | [E] | Each function checks the caller (JWT) and authorisation, validates input, sets CORS to known origins. | W1 | 1 to 4 | Human-led | t11 6b-21 [E]. |
| E2 | [E] | Rate and cost limits on any function that calls an LLM or sends email. | IF | 1 to 3 | Human-led | t11 6b-22 [E]. Moltbook had none (t11 finding 8). |
| E3 | [S] | Error handling, timeouts, retries. No stack traces to the client. Logs on. | W2 | 2 to 5 | AI-led | t19 5b: named by 3 of 9 (Wavect, Red Leg, McKelvey). |
| E4 | [E] | Client writes that should go through a function. Remove N+1 calls. | W2 | 1 to 4 | Human-led | t11 6b-24 [E]. |

### F. Deployment, environments, domains

| # | Tag | Item | Tier | Hours (our est.) | AI | Source or note |
|---|---|---|---|---|---|---|
| F1 | [E] | Production domain, HTTPS, www redirect, DNS, SPF, DKIM, DMARC. | W1 | 1 to 3 | AI-led | t11 6b-25 [E]. |
| F2 | [S] | Dev, staging, prod with own env vars. Deploy from a branch. Staging URL for the client. | W1 | 2 to 4 | Human-led | t19 5b: Wavect names staging/prod split (1 of 9). t11 6b-26 [E]. |
| F3 | [E] | Security headers (CSP, HSTS, frame options). Removes noise from the client's own scans. | W1 | 0.5 to 1.5 | AI-led | t11 6b-27 and finding 6 (99% figure was mostly headers). |
| F4 | [S] | Deploy smoke: [PARAPHRASE, NOT VERBATIM] 'works in preview, fails when deployed', env vars, CORS and redirect mismatches. | W2 | 1 to 3 | Human-led | t21 #12 (seller lists, round 2). |
| F5 | [S] | Lovable Cloud to own Supabase: schema, data, auth users, storage, password-reset emails, rewire. Separate quote. | X | 12 to 30 | Human-led | t20 #4: manual, needs reset email to every user. Hours are our guess. |

### G. Performance

| # | Tag | Item | Tier | Hours (our est.) | AI | Source or note |
|---|---|---|---|---|---|---|
| G1 | [E] | Measure first: Lighthouse, Supabase query logs. | W2 | 1 to 2 | AI-led | t11 6b-29 [E]. |
| G2 | [E] | Fix slow queries and missing indexes. Paginate. Lazy-load routes. Compress images. | W2 | 3 to 8 | Human-led | t11 6b-29 [E]. |
| G3 | [E] | Remove duplicate fetches and needless realtime subscriptions. | W2 | 1 to 3 | AI-led | t11 6b-30 [E]. |

### H. Code structure and AI guardrails

| # | Tag | Item | Tier | Hours (our est.) | AI | Source or note |
|---|---|---|---|---|---|---|
| H1 | [S] | Delete dead files and unused components. Only safe, test-covered deletions in week one. | W2 | 2 to 6 | AI-led | t19 #8: Slopfix 100,000 to 35,000 lines (vendor). BRIEF '90+ of 100 files' is unverified. |
| H2 | [E] | TypeScript strict where practical. Remove `any` in the data layer. One Supabase client. Split big components. Lint and formatter. | W2 | 3 to 8 | AI-led | t11 6b-32 [E]. |
| H3 | [E] | Generate types from the database schema. | W1 | 0.5 to 1 | AI-led | t11 6b-33 [E]. |
| H4 | [S] | Put CLAUDE.md / AGENTS.md with hard rules, lint rules and CI checks in the repo, so the next AI session does not undo the fixes. | W1 | 1 to 2 | Human-led | t19 #8 (Slopfix hands over CLAUDE.md, lint, CI); #32 (hard rules lifted output quality). Vendor and anecdote. |
| H5 | [E] | README: how to run, env vars, deploy steps, data model, known issues. | W1 | 1 to 2 | AI-led | t11 6b-34 [E]. |

### I. Tests and CI

| # | Tag | Item | Tier | Hours (our est.) | AI | Source or note |
|---|---|---|---|---|---|---|
| I1 | [S] | Smoke tests for the 3 to 5 journeys on the signed acceptance list. Freeze known-good behaviour. | W1 | 2 to 5 | AI-led | t19 #7 (AppStuck regression loop); t11 6b-35 [E]. |
| I2 | [E] | RLS tests: user A cannot read or write user B's rows. Anon reads nothing private. One test group per table. | W1 | 3 to 6 | AI-led | t11 6b-35 [E]. Built once as a template, reused. |
| I3 | [E] | CI on every pull request: build, lint, tests, secret scan, dependency audit. | W1 | 1 to 3 | AI-led | t11 6b-36 [E]. |
| I4 | [E] | Extend smoke tests to all 10 money-or-data paths. | W2 | 2 to 4 | AI-led | t11 6b-35 [E]. |

### J. Monitoring

| # | Tag | Item | Tier | Hours (our est.) | AI | Source or note |
|---|---|---|---|---|---|---|
| J1 | [E] | Error tracking (e.g. Sentry), uptime check, Supabase log alerts, Stripe webhook failure alerts. | W2 | 1 to 3 | Human-led | t11 6b-37 [E]. |
| J2 | [E] | Cost alerts on LLM and email usage. | IF | 0.5 to 1 | Human-led | t11 6b-38 [E]. |

### L. Handover (Day 5)

| # | Tag | Item | Tier | Hours (our est.) | AI | Source or note |
|---|---|---|---|---|---|---|
| L1 | [E] | Runbook (AI drafts, engineer edits). | W1 | 1.5 to 2.5 | AI-led | [E]. |
| L2 | [E] | Handover video, 15 to 20 minutes. | W1 | 1 to 1.5 | Human-led | [E]. |
| L3 | [E] | Security sign-off list with the plain disclaimer: we find and fix what we find. We do not certify an app as secure. | W1 | 1 to 1.5 | Human-led | t11 section 6 (disclaimer advice). |
| L4 | [E] | Parked items list with hour estimates. | W1 | 0.5 | Human-led | [E]. See section 6. |
| L5 | [E] | Rotate any key we touched. Remove our access, or agree what stays. Log it. | W1 | 0.5 to 1 | Human-led | [E]. |

### Totals (our estimate, computed from the table)
- 58 items: 21 [S] and 37 [E]. Of the 37 week-one items, 14 are [S].
- Most of the checklist is still engineering judgment. The sourced part is mainly the security and data core.

| Tier | Items | Manual hours, low to high | Mid |
|---|---|---|---|
| W1 week-one core | 37 | 35.5 to 81.5 | 58.5 |
| W1 with AI help (30-50% off AI-led, 0-10% off human-led) | 37 | 25 to 70 | 46 |
| IF (only if the feature exists) | 8 | 11 to 28.5 | about 20 |
| W2 second sprint-week | 11 | 19 to 52 | 35.5 |
| X separate quote | 2 | 14 to 36 | 25 |

Read:
- A small, clean app lands near the low end: about 25 to 32 hours. It fits one sprint-week.
- A typical Lovable app with Stripe: about 46 h (W1) + about 20 h (IF) = 66 h. That is 2 sprint-weeks.
- The whole list including W2 for an app with payments: about 100 hours, 3 sprint-weeks. This agrees with the vendor 2 to 6 week range (t19 #2), but both are unproven.

### Sizing rule from the Day 1 audit
- Add up W1 + IF items that are present. Use the AI-adjusted mid value.
- 32 hours or less: 1-week sprint.
- 33 to 64 hours: 2-week sprint.
- 65 to 128 hours: extended rescue (section 5).
- Over 128 hours: rebuild quote.
- (32 h = 80% of a 40 h week. The other 20% is the buffer.)

---

## 4. The team and the cost

### Roles and hours per sprint-week
| Role | Hours per week | Does |
|---|---|---|
| Engineer (1 per sprint) | 40 (3, 8, 8, 8, 8, 5) | All hands-on work. Uses Claude Code or Cursor. Writes the daily update. |
| Lead (reviews) | 8 (1, 2, 1, 1.5, 1, 1.5) | Go or no-go. Triage. Signs scope. Reviews pull requests on policies, keys, auth, payments. Runs the acceptance list. Final sign-off. |
| Warranty reserve | 4 engineer hours per sprint-week, spent in the 2 weeks after handover | Fixes for things that fail the acceptance list. Length of warranty is a risk.md decision. |

### Cost per sprint-week (our estimate)
Inputs:
- Engineer salary: $1,000 to $1,100 per month (brief).
- Hours per month: 160 (4 weeks x 40 h). Conservative, since a month is really about 4.33 weeks.
- Engineer per hour: $1,000 / 160 = $6.25. $1,100 / 160 = $6.875.
- Lead salary is NOT in the brief. We assume $2,500 per month: $2,500 / 160 = $15.63 per hour. Sensitivity: $4,000 per month = $25.00 per hour.
- Tools per sprint-week: $50 (assumption: AI coding seats and a staging project; check current plan prices).
- Payment and FX fees: 3% to 5% of $2,000 = $60 to $100 (assumption).
- Reference price: $2,000 per sprint-week (brief). Offer prices live in offers.md.

Arithmetic, 1 sprint-week, lead at $2,500 a month:
| Line | Low | High |
|---|---|---|
| Engineer 40 h | 40 x $6.25 = $250 | 40 x $6.875 = $275 |
| Warranty reserve 4 h | 4 x $6.25 = $25 | 4 x $6.875 = $27.50 |
| Lead 8 h | 8 x $15.63 = $125 | $125 |
| Tools | $50 | $50 |
| Fees | $60 | $100 |
| Total | $510 | $577.50 |
| Margin on $2,000 | $1,490 (74.5%) | $1,422.50 (71%) |

If the lead costs $4,000 a month: lead 8 h x $25 = $200. Total $585 to $652. Margin 67% to 71%.

Overrun cases (hours multiplied; lead and warranty hours scale too, which is cautious):
| Case | Cost, lead at $2,500 | Margin on $2,000 | Cost, lead at $4,000 | Margin |
|---|---|---|---|---|
| 1x plan (40 h) | $510 to $578 | 71% to 74% | $585 to $652 | 67% to 71% |
| 2x plan (80 h) | $910 to $1,005 | 50% to 55% | $1,060 to $1,155 | 42% to 47% |
| 3x plan (120 h) | $1,310 to $1,432 | 28% to 34% | $1,535 to $1,658 | 17% to 23% |

Read:
- Cash cost is small. Even 3x leaves a positive margin. This matches track 19 appendix A: delivery cost is not the risk.
- The real cost of an overrun is capacity. A 3x job holds an engineer for 3 weeks and sells one week. That is about $4,000 of work not sold (2 lost weeks at $2,000). This is the loss to manage.
- Salary is not all cost. The $1,000 to $1,100 figure leaves out rent, equipment, management, sales time and tax. Treat the margin as gross, before acquisition cost (channels.md) and overhead.
- A 2-week sprint costs about 2x the figures above. Scope is checked at the end of week one (section 5).

### Capacity with 2 engineers in parallel
- Each engineer runs one sprint-week at a time.
- 2 engineers x 40 h = 80 h per week. 2 sprint-weeks per week at full load.
- Lead load at full: 2 x 8 = 16 h per week = 40% of a 40 h week. The lead is not the bottleneck at 2 engineers. Past about 4 engineers he is. [E]
- Per month (4 weeks): 8 sprint-weeks at 100%. Planning figure: 6 at 75% (the rest goes to audits that do not convert, overruns, warranty, holidays). The 75% is our assumption.
- New starts: Day 0 + Day 1 take 11 engineer hours. Limit new starts to 2 per week.

Monthly view, price $2,000 per sprint-week, fixed cost = 2 engineers ($2,000 to $2,200) + lead 40% share (assumed $1,000) + tools ($200) = $3,200 to $3,400:
| Sprint-weeks sold per month | Revenue | Fees 3-5% | Gross profit after fixed cost |
|---|---|---|---|
| 2 | $4,000 | $120 to $200 | $400 to $680 |
| 4 | $8,000 | $240 to $400 | $4,200 to $4,560 |
| 6 | $12,000 | $360 to $600 | $8,000 to $8,440 |
| 8 | $16,000 | $480 to $800 | $11,800 to $12,320 |
- Break-even is about 2 sprint-weeks a month: $3,200 / ($2,000 x 0.97) = 1.65, and $3,400 / ($2,000 x 0.95) = 1.79.
- All of this is before the cost of getting a client. The brief's gate is under $600 per paying client (30% of $2,000).
- Engineer pay is fixed. If we sell nothing, the cost is still $2,000 to $2,200 a month.

---

## 5. Rescue or rebuild: the triage rule

### What is published
Almost nothing. Track 19 #5 found no hard rule and no share of rescues that became rebuilds. What exists:
- Vendor heuristic [V]: rebuild may be faster if more than 40% of deployments cause a bug or outage. Refactor works under 15%. If the refactor estimate is 60% or more of the rewrite estimate, rewrite wins. The source says itself that these are "vendor heuristics, not research" (t19 N=17).
- Vendor structural triggers [V]: architecture wrong; data model cannot represent the domain; every change touches ten files (t19 #5).
- Vendor view [V]: "Rewrites are almost always the wrong call when the app already has users" (vibecoding.app, t19 #5). A counterpoint in the same search: "If you're early enough, a rewrite loses you less than you think."
- Anecdote: two HN freelancers both ended in a rewrite after a cleanup brief (t19 #5).
- Vendor audit (axonbuild): 21 AI-built apps, 958 confirmed findings, 58 critical (about 6%). The author argues most other findings would be redone in a new build anyway. Not a triage signal; just context.
- Our own hypothesis from track 11: stay in rescue if schema and auth are sound and fixes are local. Rebuild (or rebuild the data layer only) if RLS cannot be added without breaking the data model, auth is spread across components, or most files are duplicated. [E]

### Signals measured on Day 1
All thresholds marked [E] are our judgment. They are NOT published. The first 3 audits calibrate them.

| # | Signal | How we measure it | Green | Amber | Red | Basis |
|---|---|---|---|---|---|---|
| S1 | Share of files touched by the fix list | Files changed by W1 + IF items / total source files (src, supabase) | under 25% | 25% to 50% | over 50% | [E]. Vendor "every change touches ten files" has no number. |
| S2 | Fix cost vs rebuild cost | AI-adjusted fix hours / our rebuild hours (screens + tables + integrations, from our rebuild template) | under 35% | 35% to 59% | 60% or more | Red line is the vendor 60% [V]. Green and amber lines [E]. |
| S3 | Data model integrity | Share of tables that cannot get an owner-based RLS policy without a schema change (no owner id, no keys, relational data in JSON). Any core table (users, orgs, payments) with no owner link is red on its own. | 10% or less | 11% to 30% | over 30% | [E], from the track 11 hypothesis. |
| S4 | Auth model | Count of distinct auth or role patterns in the code. Check for home-made password or token handling. | One pattern (Supabase Auth only) | 2 to 3 patterns, or role checks in over 10 client files | Home-made auth, or auth logic in over half the components | [E], from the track 11 hypothesis. |
| S5 | Platform lock-in | Where is the backend? | Own Supabase | Lovable Cloud (adds item F5, 12 to 30 h our guess, and a password-reset email to every user: t20 #4) | Base44 backend (export is frontend only: t02 #5) | [S] for facts, [E] for the colours. |
| S6 | Deploy failure rate | Failed / total of the last 20 production deploys. If no history: 10 clean builds + staging deploys. | under 15% | 15% to 40% | over 40% | Vendor heuristic [V] (t19 N=17). |
| S7 | Users and money (modifier, not a colour) | Paying users? Revenue? | | | | Vendor view above [V]. |

### Decision
Take the more severe result of the hours rule (section 3) and the signals rule.

Signals rule:
- REBUILD QUOTE if any of: S3 red, S4 red, S5 red (Base44), S2 red, or two or more reds among S1 and S6.
- EXTENDED RESCUE if no rebuild trigger and any of: one red on S1 or S6, or three or more ambers.
- RESCUE SPRINT otherwise (no red, at most two ambers).

Hours rule (AI-adjusted mid, W1 + IF items present):
| Hours | Outcome |
|---|---|
| 32 or less | Rescue sprint, 1 week |
| 33 to 64 | Rescue sprint, 2 weeks |
| 65 to 128 | Extended rescue, 3 to 4 sprint-weeks, with a go or no-go gate after each week |
| Over 128 | Rebuild quote |

S7 modifier:
- Live app with paying users and S3 or S4 red: still a rebuild quote, but offer a "stabilise first" sprint (RLS lockdown, key rotation, backup) so the users are safe while the rebuild is planned. [E]
- No users yet: any single red tips to rebuild quote. A rewrite is cheap early. [V counterpoint]

Outcome terms:
- Rescue sprint: fixed price, signed acceptance list. This is the standard offer.
- Extended rescue: fixed price per sprint-week. Re-triage at the end of each week. The client can stop after any week. We never sell an open-ended "finish my app" (t19 appendix A: finishing is sold at $15K to $50K and 4 to 8 weeks by those who offer it).
- Rebuild quote: the audit fee is credited to the rebuild if signed within a set period (the credit pattern exists in t19 #6, t21 #7). Rebuild price and terms: offers.md.
- Stop and tell: if the audit finds signs the data was already taken or changed (unknown users, unexpected exports), stop the sprint and tell the client. That is an incident, not a rescue. Legal duties are in risk.md. [E]
- Not done: ethics-list apps (BRIEF section 5).

---

## 6. Scope-creep controls

### Where creep comes from (our list, [E])
1. "While you're in there" feature requests.
2. The client keeps prompting the AI tool during the sprint.
3. Hidden scope found after the audit (payments broken, Cloud migration, data model).
4. UI polish. Cheap sellers sell this at the floor (t19 5b: Siddiqi lists UI and branding). It is not our product.
5. A bad codebase eats more hours than planned.

### What the evidence says
- Thin. No practitioner account of a client overwriting a fix during a rescue was found (t19 #7).
- One HN summary says clients often keep vibe-coding on top of cleaned-up code, so the cycle repeats (t19 #7, paraphrase, no quote).
- AppStuck (vendor) describes the "regression loop": a fix loses a working behaviour elsewhere. Advice: freeze known-good behaviour with tests (t19 #7, N=34).
- The contract ideas (code freeze, change control, no liability for outside edits) came from the search tool's own synthesis, not from a source (t19 #7). So this whole section is [E] and is a risk to test in the first paid jobs.

### Control 1: Code freeze on the client's Lovable project
- From Day 0 to Day 5 the client does not prompt Lovable and does not edit the Supabase dashboard. Written in the contract and the Day 0 note.
- Our work lives on a git branch. Lovable must not write to it. [E] CHECK ON DAY 0: how Lovable's GitHub sync is set up (which branch it writes to, and whether it can be pointed at another one). We have not verified this. If Lovable writes to main, we merge main into our branch each morning.
- Give the client a sandbox: a copy (remix or duplicate) of the Lovable project. New ideas get prompted there. Nothing from the sandbox merges during the sprint. [E] (check the platform's copy feature).
- Branch protection on main. Our pull request is the only way in.
- Daily drift check each morning: new commits we did not make; Supabase migrations in production that are not in git; schema changes in the dashboard. A short script. [E]

### Control 2: Change control
- After the acceptance list is signed, every new request becomes a written change request: what, why, hours (our estimate), price.
- The lead decides. The engineer never says "quick one, yes".
- Three outcomes only: SWAP (replace an item of equal hours), ADD (extra hours at a quoted price, may extend the sprint), PARK (goes on the list).
- Add-on price: set in offers.md. Market anchors seen: Lovable directory experts $50 to $130 an hour (t20 #8), AppStuck $70 an hour with a 5-hour prepaid minimum (t21 #7), Upwork pros $60 to $100 (t21 #4). All seller prices.
- Absorb limit: we take up to 8 hours (20% of 40) of overrun for free. Past that, the lead must approve a change request or a switch to extended. Never absorb silently past 2x.

### Control 3: Fixed acceptance test list, signed at audit
- Written on Day 1. Signed by the client before Day 2.
- Numbered tests. Each has: steps, expected result, where it runs (staging), who runs it, pass or fail.
- Typical size 15 to 30 tests (our guess): 3 to 5 user journeys, one RLS test group per table, secret scan clean, advisor clear, dependency audit clean, deploy works from a clean clone.
- "Done" = every test passes on staging, then smoke test passes on production.
- Nothing off the list is in scope.

### Control 4: Parked items list
- A shared doc. Each item: what, who asked, date, hours (our estimate), price.
- Anything outside the signed list goes here, including things we notice.
- Reviewed at the Day 5 call. This is the menu for the next sprint or the maintenance plan.

### Control 5: Mid-week checkpoint
- Day 3: hours used vs plan. Over 1.25x means the lead decides that day: cut to parked, change request, or switch to extended.

### When the client keeps prompting the AI during the sprint
Ladder:
1. First time. Same-day message. We merge or rebase, re-run the tests. We absorb up to 1 hour.
2. Second time. Written change request for the hours. The sprint clock is paused while we re-check the delta.
3. Third time. We pause work. Options for the client: (a) restore the freeze and pay a re-audit fee for the delta; (b) end the sprint with partial delivery and a pro-rata refund under the refund terms in risk.md.
Technical guards that make this visible:
- CI blocks merges when acceptance tests fail. An AI commit that breaks a test shows up in red.
- The drift check (Control 1) finds outside changes within a day.
- CLAUDE.md / AGENTS.md and lint rules sit in the repo, so a later AI session starts with our rules (H4). Also paste guard rules into the platform's project instructions if it has them. [E] (not verified)
Budget: 4 hours of rebase work per sprint is built in. More is billed.

---

## 7. What a finished rescue delivers

Acceptance rule: the client signs when artefacts 1 to 12 are delivered and every test on the acceptance list passes.

| # | Artefact | Format | Pass test |
|---|---|---|---|
| 1 | Audit report (Day 1) | 2 to 4 pages | Every finding has severity and status. |
| 2 | Signed scope + acceptance test list | One page | Signed by client before fix work. |
| 3 | Security sign-off list | One page, signed by the lead | Each week-one checklist item marked fixed, not applicable, parked or accepted risk, with a link to proof. Carries the disclaimer: we find and fix what we find; we do not certify an app as secure (t11 section 6). |
| 4 | Passing RLS test suite | Folder in the repo + green CI run link | User A cannot read or write user B. Anon reads nothing private. One group per table. |
| 5 | Smoke tests for the acceptance journeys | In the repo, run by CI | Green on staging and after release. |
| 6 | Supabase Security Advisor, before and after | Two exports | No errors left. Warnings listed with a reason. |
| 7 | Secret scan report + rotation log | One page | Full history clean. Log shows which keys rotated and when (never the keys). |
| 8 | Dependency audit report | One page | No critical findings open. |
| 9 | Staging URL | Live link + test accounts | Separate database. Client can log in and test. |
| 10 | Runbook | Markdown in the repo | Covers: run locally, env var names, deploy, rollback, backup and restore, rotate keys, run tests, add a table safely (RLS template), how to use AI tools safely on this repo, known issues. A new engineer can deploy from it. |
| 11 | Handover video | 15 to 20 minute screen recording | Shows architecture, deploy, tests, where secrets live, what not to touch. |
| 12 | Parked items list | Shared doc | Each item has hours and price. |
| 13 | Guardrail files | CLAUDE.md / AGENTS.md, lint and CI config in the repo | CI runs on every pull request. |
| 14 | Account ownership map + access log | One page | Client owns every account. Our access removed or agreed. |
| 15 | Next-step offer | One page | Maintenance plan (monthly dependency and RLS re-check, t11 6b-38) and quote for parked items. |

Note: items 13 to 15 are delivered but are not conditions for the acceptance signature.

---

## 8. What the evidence does not tell us

### The gaps
1. Fix time. No published hours per task. Only vendor fragments (2 to 4 hours for five patterns; about 2 hours for a key exposure; 1 to 2 days per fix). Our bands in section 3 are our estimate. (t19 #1, t11 #15)
2. Rebuild share. No source gives the share of rescues that ended as rebuilds. Two HN freelancers did. (t19 #5)
3. Refund and dispute data. Zero stories of chargebacks, refund fights or fixed-price overruns were found. This is not proof there are none: Reddit could not be searched. Sellers' guarantees exist (Wavect: last week refunded if not impressed; Slopfix: 2-week warranty; GainCafe: "100% success guarantee") but no outcome data. (t19 #6, t20 #19, t21 #7)
4. Repeatability share. Nobody states "X% of our jobs share this list". We have problem classes, not a share. (t19 #4)
5. AI share of work. No percentage published. Our 30% to 50% cut is a guess. (t19 #8)
6. Client re-prompting. No practitioner account. (t19 #7)
7. Scanner effect. Lovable and Replit now run scanners (t12 #11, #13). We do not know how many holes the scanners already close before a client reaches us. Replit's own black-box scan found an admin dashboard its code scanner missed (t12 #13).
8. Cloud share. We do not know what share of prospects are on Lovable Cloud (13 months in, on by default, t20 #3) versus their own Supabase. It changes S5 and the hours.
9. Practitioner voices. No Reddit, so no first-person rescuer lists of recurring fixes with hours. All lists are seller-written.
10. Facts we did not check: how Lovable's GitHub sync and project copy behave (section 6); current prices of Supabase branching and AI coding seats.

### How the first 3 paid audits should measure them
One sheet per audit. One row per checklist item. Filled live, not from memory.

Per app (Day 1):
- Platform, Cloud or own Supabase, lines, file count, tables, edge functions, Stripe yes or no, LLM calls yes or no, paying users, client's earlier spend.
- Did the client bring a platform scan report? If yes, copy what it flagged. After our audit, mark what we found that it missed.
- Signals S1 to S6 raw values and colours. Our decision. Estimated hours (manual and AI-adjusted).

Per checklist item:
- Present: yes or no. Severity. Files touched.
- Estimated hours at audit. Actual hours. Actual hours tagged "AI-assisted" or "manual".
- Items we found that are NOT on the checklist (add them; track their hours).

Per engagement:
- Overrun ratio = actual / estimated, and the cause (bad data model, hidden scope, client re-prompting, our error).
- Change requests: count, hours, accepted or parked.
- Client prompting incidents: count, hours lost.
- Outcome: accepted, partial, refunded, disputed. Days to acceptance.
- Triage outcome and later regret: did a rescue need a rebuild after all?
- Cold read from the client: did they understand the handover video and runbook (ask one question).

Pass marks we propose for Gate 3 (our proposal, [E]):
- Repeatable: at least 75% of W1 items needed in at least 2 of the 3 audits, and unplanned work under 15% of hours.
- Estimate quality: actual hours within 1.5x of estimate on at least 2 of 3.
- If actual hours average over 2x the estimate: re-set the bands and price by audit hours, not by the week.

Caveat:
- Three is a tiny sample. It calibrates; it does not prove. Do not publish a guarantee or a success rate until at least 6 to 10 engagements are logged.

---
End of file. Companion files: offers.md (prices, guarantee, rebuild terms), risk.md (contract, refund, liability), channels.md (cost per client).

## Appendix: unverified items
- Checklist item F4, "works in preview, fails when deployed" [t21 #12]: downgraded to [PARAPHRASE, NOT VERBATIM], propagated from track 21. The cache wording is "App works in preview but not in deployment".
