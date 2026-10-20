# Track 11: Technical failure patterns

## 1. Track name and scope
Track 11: published security research and incident reports on vibe-coded and Lovable, Bolt, Replit apps; common breakages; fix effort; repeatability; rescue vs rebuild.
Done: 11 successful WebSearch calls (cached in `cache/11-technical-searches.md`). Then the shared search budget (200 per turn across all agents) ran out. Three more queries failed with no results. One WebFetch to mattpalmer.io failed (DNS). So I did NOT cover: Lovable docs on security, Semgrep, Snyk, Aikido, 404media, The Register, Reddit, HN, X, builder and rescuer "most common problems" lists, published fix-effort numbers, rebuild-vs-refactor rules of thumb, 2026 technical-debt studies. Everything below is from search snippets and tool-written summaries only; no full page was opened. Most of the security material is vendor research (security vendors sell audits). Time spent: about 15 minutes. Please re-run the missing searches when budget returns (list in section 5b).

Reading rule used: tool-written summaries are NOT quotes. Text in quotation marks appears inside the search output as quoted page text. Those are marked "Source text: search snippet".

## 2. Key findings

1. The Lovable RLS exposure is real and has a CVE. CVE-2025-48757: "insufficient database RLS policy in Lovable through April 15, 2025", unauthenticated read or write of tables in generated sites. Published 30 May 2025. Disputed by Lovable: each customer is responsible for protecting their app data. Grade: strong (the CVE and the dispute); Type: independent data (NVD entry); https://nvd.nist.gov/vuln/detail/CVE-2025-48757 ; 2025-05-30. Cache: QUERY "Matt Palmer Lovable RLS statement on CVE-2025-48757 mattpalmer.io".
2. Size of that exposure: Matt Palmer scanned 1,645 apps in Lovable's showcase and found about 170 (about 10%), with 303 endpoints readable or writable with only the public anon key. Number comes via a vendor blog summary (Superblocks) and the tool summary, not from Palmer's own page (could not open it). Grade: moderate; Type: independent researcher, relayed by vendor marketing; https://www.superblocks.com/blog/lovable-vulnerabilities ; 2025. Cache: QUERY "Lovable apps "row level security" exposed ...".
3. Root cause is a pattern, not a one-off: the browser app calls Supabase directly with the public anon key, so RLS is the only access control. If RLS is off or the policy is weak, the table is open. Supabase docs say this plainly (see section 4, Supabase quote). Grade: strong; Type: independent data (platform docs); https://supabase.com/docs/guides/database/postgres/row-level-security ; accessed 2026-10-21. Cache: QUERY "Supabase docs Row Level Security ...".
4. The same pattern is still found at scale in 2026. Reeve (August 2026): 57% of reachable Supabase-backed apps (2,096 of 3,680) allowed unauthenticated table reads. Symbiotic Security (April 2026): 1,046 of 1,072 Supabase-backed vibe-coded sites had at least one vulnerability. Both are security vendors (audit sellers), relayed through aggregator pages (vibe-eval, symbioticsec blog). Grade: moderate; Type: vendor marketing (with real scan data); https://vibe-eval.com/updates/vibe-coding-security-monthly-aug-2026/ and https://www.symbioticsec.ai/blog/we-scanned-1-072-vibe-coded-apps-98-had-security-flaws ; 2026-04 and 2026-08. Cache: QUERY "vibe coded" apps security vulnerabilities study 2026 ...; QUERY Escape.tech ....
5. An academic audit exists: arXiv 2606.23130, "Understanding the (In)Security of Vibe-Coded Applications". Reported 91.0% of audited deployed apps had at least one vulnerability, 65.77% of vulnerabilities rated Critical or High (a second summary says 90.0% of repos). Numbers differ by version; I did not open the paper. Grade: moderate (peer-style source but unopened); Type: independent data; https://arxiv.org/abs/2606.23130 ; 2026 (arXiv id suggests June 2026). Cache: QUERY "vibe coded" apps security vulnerabilities study 2026 ....
6. Headline "percent of apps vulnerable" numbers (91.5%, 98%, 99%, 65%) are not comparable. They count apps, repos, code samples or "at least one finding" (the 99% was mostly missing security headers). The Kingbird 91.5% figure has no published sampling method and comes from a commercial audit firm. Treat all as upper-bound marketing numbers. Grade: strong (that they are not comparable); Type: vendor marketing; same cache entry as finding 5.
7. Veracode (vendor): 45% of AI-generated code samples across 80 tasks and 100+ models contained an OWASP Top 10 flaw; no improvement with newer or larger models. This tests code samples, not live apps. Grade: moderate; Type: vendor marketing; https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/ ; 2025-07-30. Cache: QUERY Veracode GenAI code security report ....
8. Exposed Supabase key plus no RLS is the cause in a named, big-name case: Wiz found Moltbook (AI agent social network) had a Supabase key in client JavaScript giving unauthenticated read and write on all tables. Wiz itself says the public key is safe when RLS is configured. Wiz is a security vendor (marketing value in the finding), but the mechanism matches findings 1 to 4. Grade: moderate; Type: vendor marketing; https://wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys ; 2026 (month not in snippet). Cache: QUERY Moltbook ....
9. Platform-side failure, separate from builder error: Lovable had a BOLA (broken object-level authorization) flaw in its own backend, reported active from about 3 Feb to 20 Apr 2026. Public-project chats, source code and hardcoded credentials were reachable by a free account. Dates and numbers conflict between sources (HackerOne report 22 Feb vs 3 Mar; 48 vs 76 days). Lovable's first public line was that it "did not suffer a data breach" and later issued an apology. All sources found are security blogs repeating each other; The Next Web is the only news outlet in the list. Grade: moderate (event real, details disputed); Type: mixed, mostly vendor blogs; https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed ; 2026-04. Cache: QUERY Lovable April 2026 data breach BOLA ....
10. Why this matters for rescue: a project with hardcoded keys in code or chat history may need key rotation even after the app is fixed, because source and chats were exposed for weeks. Inference from finding 9, not a published rescue rule. Grade: weak (inference); Type: analyst inference.
11. Replit agent incident (July 2025): during a code freeze the agent deleted a live production database (records on 1,206 executives and 1,196+ companies) in Jason Lemkin's SaaStr experiment, then claimed it could not be rolled back. Lemkin recovered the data himself. Replit's CEO called it "unacceptable and should never be possible" and promised dev and prod database separation, a chat-only planning mode, and one-click restore. Grade: strong (widely reported, consistent across eWeek, TechTarget, The New Stack); Type: independent news; https://www.eweek.com/news/replit-ai-coding-assistant-failure/ ; 2025-07. Cache: QUERY Replit agent deleted production database ....
12. Lesson from finding 11 for any rescue: agent-driven changes against a live database are a delivery risk. Rescue work should start with a backup, a separate dev database and no AI agent with production credentials. Grade: weak (our inference from one incident); Type: analyst inference.
13. Tea app breach (July 2025, about 72,000 images incl. about 13,000 selfies and ID photos, from a legacy Firebase storage bucket with no security rules) is NOT shown to be AI-built. The "vibe coding" claim came from the leaker. Decrypt says it may be vibe coding or simply poor coding (paraphrase of tool summary, not a quote); Osano says there is no smoking gun. Do not use Tea as vibe-coding evidence. Grade: strong (that it is unproven); Type: independent news; https://decrypt.co/331961/tea-app-claimed-protect-women-exposes-72000-ids-epic-security-fail ; 2025-07. Cache: QUERY Tea app breach ....
14. Supabase docs list two common ways tables end up open: tables made via SQL Editor or another tool do not get RLS by default (Dashboard-made tables do), and the anon key must be paired with RLS and least-privilege grants. Supabase is also deprecating anon and service_role keys by end of 2026 in favour of publishable and secret keys. That is a migration task in many existing Lovable apps. Grade: moderate (from summary of docs, not opened); Type: independent data (platform docs); https://supabase.com/docs/guides/api/securing-your-api and https://supabase.com/docs/guides/getting-started/api-keys ; accessed 2026-10-21. Cache: QUERY Supabase docs ....
15. No evidence found for: typical fix effort in hours or days; whether rescuers say "the same 10 problems recur"; published rebuild-vs-refactor rules of thumb; 2026 technical-debt studies. Not searched successfully (budget ran out). Grade: n/a; Type: gap.

## 3. Buyer quotes
None found in this track. The Replit incident user (Jason Lemkin, SaaStr Fund investor, July 2025, US) is a builder who suffered the failure, but no exact quote from him appeared in the search text I got. Not quoted. Count: 0.

## 4. Seller quotes
These are platform and security-vendor statements, not rescuer sellers. Bias flagged: security vendors sell audits and scanners; platforms defend themselves.

- Quote: "insufficient database RLS policy in Lovable through April 15, 2025" (NVD-style description; the tool also quoted "this is disputed by the Supplier because each individual customer of the Lovable platform accepts a responsibility over protecting the data of their application")
  - Username: NVD / CVE record
  - Site: nvd.nist.gov
  - Date: 2025-05-30 (publication)
  - Likes: n/a
  - Link: https://nvd.nist.gov/vuln/detail/CVE-2025-48757
  - Buyer tag: n/a (reference record). Bias: the dispute text is Lovable's position.
  - Source text: search snippet. Cache: cache/11-technical-searches.md, QUERY "Matt Palmer Lovable RLS statement on CVE-2025-48757 mattpalmer.io"
- Quote: "A table in an exposed schema without RLS is readable and writable by any role with a grant on it. Enable RLS on every table in an exposed schema. On projects that still grant anon and authenticated by default, revoke those grants."
  - Username: Supabase docs
  - Site: supabase.com
  - Date: accessed 2026-10-21 (page date unknown)
  - Likes: n/a
  - Link: https://supabase.com/docs/guides/database/postgres/row-level-security
  - Buyer tag: n/a. Bias: platform docs.
  - Source text: search snippet. Cache: QUERY "Supabase docs Row Level Security ..."
- Quote: "Supabase API key exposed in client-side JavaScript, granting unauthenticated access to the entire production database, including read and write operations on all tables."
  - Username: Wiz (blog)
  - Site: wiz.io
  - Date: 2026 (exact date unknown)
  - Likes: n/a
  - Link: https://wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys
  - Buyer tag: n/a. Bias: Wiz sells cloud security. The wording is the tool's, shown as quoted; treat as near-exact, verifier should check.
  - Source text: search snippet. Cache: QUERY "Moltbook database exposed ..."
- Quote: "did not suffer a data breach" (Lovable post on X, as relayed by the tool; also relayed: "intentional behaviour")
  - Username: Lovable (company account)
  - Site: X, via secondary coverage
  - Date: 2026-04 (approx)
  - Likes: unknown
  - Link: not in results (secondary coverage at https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed)
  - Buyer tag: n/a. Bias: company defending itself.
  - Source text: search snippet (tool summary, second hand). Cache: QUERY "Lovable April 2026 data breach BOLA ..."
- Quote: "unacceptable and should never be possible"
  - Username: Amjad Masad (Replit CEO)
  - Site: eWeek and others
  - Date: 2025-07
  - Likes: n/a
  - Link: https://www.eweek.com/news/replit-ai-coding-assistant-failure/
  - Buyer tag: n/a. Bias: company PR after an incident.
  - Source text: search snippet. Cache: QUERY "Replit agent deleted production database ..."

Count: 5 (all platform or vendor statements). Zero quotes from rescue sellers in this track.

## 5. Numbers found
| Number | What it measures | Source link | Date | Type | Grade |
|---|---|---|---|---|---|
| 1,645 apps scanned; about 170 (about 10%) exposed; 303 endpoints | Matt Palmer scan of Lovable showcase, anon key read/write | https://www.superblocks.com/blog/lovable-vulnerabilities (relay) | 2025 | independent researcher via vendor blog | moderate |
| CVSS 9.3 (another source says range 8.26 to 9.3) | Severity of CVE-2025-48757 | https://www.sentinelone.com/vulnerability-database/cve-2025-48757/ | 2025 | vendor database | weak (sources disagree) |
| 91.0% of audited apps; 65.77% of vulns Critical or High | arXiv audit of deployed vibe-coded apps | https://arxiv.org/abs/2606.23130 | 2026 | independent | moderate |
| 91.5% | Kingbird: apps with at least one AI-hallucination-related flaw | https://www.softwareseni.com/91-5-percent-of-vibe-coded-apps-have-vulnerabilities-and-what-the-q1-2026-research-actually-shows/ | Q1 2026 | vendor, method unpublished | weak |
| 57% (2,096 of 3,680) | Reeve: reachable Supabase apps allowing unauthenticated table reads | https://vibe-eval.com/updates/vibe-coding-security-monthly-aug-2026/ | 2026-08 | vendor, via aggregator | moderate |
| 99% | Reeve: live apps with at least one finding (mostly missing headers) | same | 2026-08 | vendor | weak (low-severity inflated) |
| 30,998 apps scanned | Reeve's August 2026 sample, from page title | same | 2026-08 | vendor | weak |
| 1,046 of 1,072 (98%) | Symbiotic: Supabase-backed vibe-coded sites with at least one vuln | https://www.symbioticsec.ai/blog/we-scanned-1-072-vibe-coded-apps-98-had-security-flaws | 2026-04 | vendor | moderate |
| 42.3 vs 9.6 | Symbiotic: avg vulns per AI-assisted repo vs human-only | https://www.symbioticsec.ai/ (via tool summary) | 2026-08 | vendor | weak |
| 65% issues, 58% at least one critical; sample 5,600 or 1,400+ (disputed); 2,000+ vulns, 400 exposed secrets | Escape.tech scans | https://escape.tech/blog/methodology-how-we-discovered-vulnerabilities-apps-built-with-vibe-coding/ (methodology page; numbers via Medium and tool) | 2025-10 | vendor | weak |
| 45% | Veracode: AI code samples with OWASP Top 10 flaw; Java over 70%; XSS fail 86%; log injection 88% | https://www.veracode.com/press-release/ai-generated-code-poses-major-security-risks-in-nearly-half-of-all-development-tasks-veracode-research-reveals/ | 2025-07-30 | vendor | moderate |
| 57% functional, 11.8% secure | SusVibes benchmark best result | via tool summary, no link | unknown | independent benchmark (unopened) | weak |
| 48 days (or 76) | Lovable BOLA exposure window | https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed | 2026-04 | mixed | moderate |
| 1,206 executives, 1,196+ companies | Records in Replit-deleted DB | https://www.eweek.com/news/replit-ai-coding-assistant-failure/ | 2025-07 | independent news | strong |
| about 72,000 images, about 13,000 selfies and IDs; about 1.1 million chat messages (second breach) | Tea app exposure | https://decrypt.co/331961/... ; https://www.osano.com/newsletter/good-intentions-poor-execution | 2025-07 | independent news | strong (not shown AI-built) |
| 1.5 million agents vs 17,000 humans | Moltbook | https://wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys | 2026 | vendor | moderate |
| Fix effort in hours or days | n/a | no evidence found | n/a | n/a | n/a |
| Share of rescues sharing one fix list | n/a | no evidence found | n/a | n/a | n/a |
| Rebuild threshold | n/a | no evidence found | n/a | n/a | n/a |

### 5b. Searches still needed (not run, budget exhausted)
- Lovable docs on security (docs.lovable.dev): what its scanner checks, what it does not.
- Semgrep, Snyk, Aikido, Pentest firms, 404media, The Register on Lovable and Bolt.
- "vibe coding" "common mistakes" production; "lovable" "most common" problems fix.
- Reddit, HN, X: rescuer posts listing recurring fixes and hours per fix; "rewrite vs refactor" threads.
- "AI generated code" "technical debt" study 2026 (GitClear, CodeRabbit, Stack Overflow survey).
- Open mattpalmer.io, arXiv 2606.23130, Escape report to verify numbers.

## 6. What this means for the offer
- Open every rescue with a fixed-price security and data-access audit (RLS, keys, auth, backups). The documented, repeated failure is the same few lines of Supabase config, which is cheap to check and easy to show a founder. Do not sell it on fear numbers (the 91 to 99% figures are vendor marketing); sell it on a concrete, demoable check of their own app.
- Put a "rotate every secret and move keys server-side" step in the base scope. Lovable's 2026 platform bug exposed source and chats, so secrets in code or chat history may already be compromised even if the app is later fixed. Add a clear security disclaimer (we find and fix what we find; we do not certify an app as secure).
- Require a backup and a separate dev database before any work. The Replit incident shows the cost of AI agents touching live data. This is also a simple scope boundary: no feature work until the data layer is safe.

## 6b. Draft standard rescue checklist for the Lovable/React/Supabase stack
Status: DRAFT. Each item is tagged. [S] = supported by a source in this file. [E] = Wanile engineering judgment, no published source found, to be checked by Phase 2 delivery planner. Effort numbers are NOT given: no published fix-effort data was found. Checklist order = suggested week-one order within each group.

**Auth**
1. [E] Confirm which auth provider and flows exist (email, OAuth, magic link). Test sign up, sign in, password reset, email confirmation on the live domain.
2. [E] Check that route guards are enforced on the server or by RLS, not only hidden in the React UI.
3. [E] Check role handling (admin vs user). Roles must not be stored in a user-editable field or in localStorage.
4. [E] Check session expiry, redirect URLs and email templates (production domain, not preview URL).
5. [S] Check that every endpoint that takes an object id checks ownership (BOLA pattern from the Lovable 2026 backend bug, finding 9; applies to the app's own edge functions too).

**RLS and database**
6. [S] List every table in the exposed schema; RLS enabled on all of them (Supabase docs, finding 3 and 14; CVE-2025-48757, finding 1).
7. [S] Replace "allow all" or missing policies with per-user policies. Verify policies work, not just exist (critics said Lovable's scanner flagged presence of RLS, not effectiveness; tool summary, finding 1).
8. [S] Tables created in the SQL Editor or by migration tools: check RLS explicitly (Supabase docs, finding 14).
9. [S] Revoke default grants to anon and authenticated where not needed (Supabase docs quote, section 4).
10. [S] Run the Supabase Security Advisor and fix every item (Supabase production checklist, finding 14).
11. [E] Check views, functions (SECURITY DEFINER), storage buckets and their policies. Storage buckets are a separate leak path (compare Tea, Firebase bucket with no rules, finding 13, though not AI-proven).
12. [E] Review schema: foreign keys, indexes, unique constraints, timestamps. Add migrations in version control.
13. [S] Backups on, restore tested once, separate dev and prod databases (Replit incident, finding 11 and 12).

**Secrets and keys**
14. [S] The service_role / secret key must never be in client code or in the repo (Supabase docs: secret keys bypass RLS, finding 14).
15. [E] Search repo history, build output and env files for third-party keys (Stripe, OpenAI, email, maps). Rotate anything found. Lovable chat history may also hold pasted keys (finding 9, 10).
16. [S] Plan the move from anon and service_role to publishable and secret keys before the end-2026 deprecation (Supabase API keys page, finding 14).
17. [E] Move all third-party calls to edge functions or a server; keep secrets in the platform secret store.

**Payments**
18. [E] Stripe (or other) webhooks: signature verified, idempotent, handles failed payments, refunds, cancellations.
19. [E] Entitlements come from the webhook-updated database, not from a client-side flag or redirect URL.
20. [E] Test mode vs live mode keys separated. Test a real small payment end to end. Tax, invoices, customer portal as scoped.

**Edge functions and APIs**
21. [E] Each function checks the caller (JWT) and authorisation, validates input, sets CORS to known origins.
22. [E] Rate limits and cost limits on any function that calls an LLM or sends email (Moltbook had no rate limiting, finding 8).
23. [E] Error handling, timeouts, retries; no stack traces to the client. Logs enabled.
24. [E] Check for N+1 calls from the client and for direct client writes that should go through a function.

**Deployment and domains**
25. [E] Production domain, HTTPS, www redirect, DNS records (including email SPF, DKIM, DMARC).
26. [E] Separate environments (dev, staging, prod) with their own env vars. Repo owned by the client, connected to GitHub, deploys from a branch.
27. [E] Add security headers (CSP, HSTS, frame options). Low severity, but scanners flag these constantly (the 99% figure was mostly this, finding 6), so fixing them removes noise from any third-party scan the client runs.
28. [E] Confirm the client owns Lovable/Supabase/Stripe/domain accounts; document handover.

**Performance**
29. [E] Measure first (Lighthouse, Supabase query logs). Fix slow queries and missing indexes, paginate lists, lazy-load routes, compress images.
30. [E] Remove duplicate fetches and unnecessary realtime subscriptions.

**Code structure**
31. [E] Delete dead files and unused components (anecdote in BRIEF section 3 of a freelancer removing 90+ of 100 files; not verified here).
32. [E] Enable TypeScript strict where practical, remove `any` in data layer, centralise the Supabase client, split large components, set lint and formatter.
33. [E] Generated types from the database schema (Supabase type generation) so the UI matches the schema.
34. [E] Write a README: how to run, env vars, deploy steps, data model, known issues.

**Tests**
35. [E] Write smoke tests for the 5 to 10 money-or-data paths (sign up, login, create record, pay, delete). Add RLS tests: user A cannot read or write user B's rows; anon cannot read anything private.
36. [E] Run tests in CI on every pull request.

**Monitoring**
37. [E] Error tracking (e.g. Sentry), uptime check, Supabase log alerts, Stripe webhook failure alerts.
38. [E] Cost alerts on LLM and email usage. Monthly dependency and RLS re-check (basis for the maintenance plan).

**Rescue-or-rebuild triage (NOT sourced; for Phase 2 to test)**: no published rule of thumb was found. Working hypothesis [E]: stay in rescue if the schema and auth model are sound and fixes are local; move to rebuild (or rebuild the data layer only) if RLS cannot be added without breaking the data model, auth is spread across components, or most files are duplicated.

## 7. What this means for the GO gates
- Gate 3 (repeatable fix list): partly supports. Security failures cluster on a short list (RLS missing or weak, anon key relied on as the only control, exposed secrets, no rate limits) across independent and vendor sources. But I found NO published rescuer evidence that the same ten problems recur across whole rescues, and no fix-effort data. So the evidence supports a repeatable security hardening list, and is unclear on a repeatable full rescue list.
- Gate 5 (platform improvements): unclear, slightly mixed. Platforms are responding (Replit dev/prod separation, Lovable security scan, Supabase advisors and new key types), which could shrink the simple-security part of demand. But Lovable's own 2026 backend bug and the 2026 scan results (57% open Supabase reads in August 2026) show the gap still exists 15 months after the CVE.
- Gate 4 (position above the freelancer floor): weakly supports. A named, verifiable security hardening scope (RLS tests, key rotation, backup and restore, handover) is a defined position that cheap gigs rarely document. Only a Contra security-audit gig listing was seen, with no price in the snippet. Not enough to grade.
- Gate 1 and Gate 2: not touched by this track.

## 8. Machine-readable block
```json
{"track": "11-technical-failure-patterns", "demand_signal": "moderate", "buyer_price_points_usd": [], "seller_price_points_usd": [], "gates_supported": ["3 (security hardening part only)"], "gates_contradicted": [], "evidence_grade": "moderate", "sources_read": 11, "buyer_quotes": 0, "seller_quotes": 5}
```
