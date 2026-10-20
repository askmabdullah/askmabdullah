# Track output template (every Phase 1 agent must follow this exactly)

Save to: rescue-research/tracks/<track>.md
Write to the file as you go. Update it after every 3 to 5 sources. Do not wait for the end.

## 1. Track name and scope
One paragraph. What you looked at, what you skipped, time spent, sources tried, sources blocked.

## 2. Key findings
Numbered. Each finding: one or two short lines, then "Grade: strong | moderate | weak", then "Type: independent data | vendor marketing | first-person anecdote", then the link and date.

## 3. Buyer quotes
Exact text only, in quotation marks. No paraphrase inside quotes. For each:
- Quote: "..."
- Username: ...
- Site: ... (subreddit, HN, IH, X, forum)
- Date: YYYY-MM-DD (or month if that's all that's known)
- Upvotes or likes: ... (or "unknown")
- Link: ...
- Buyer tag: what is known about them: product stage, paying users or revenue, funding, what they've already spent, country. Write "unknown" for each field you cannot verify.
- Cache file: cache/<file>

## 4. Seller quotes
Same fields as buyer quotes. Keep in a separate section. Flag the bias: sellers benefit from saying demand is huge.

## 5. Numbers found
A table: number | what it measures | source link | date | type (independent / vendor / anecdote) | grade.
Prices, counts, budgets, growth figures, gig counts, review counts, ad counts, upvotes.

## 6. What this means for the offer
Exactly 3 bullets.

## 7. What this means for the GO gates
One line per gate your track touches (gates 1 to 5 from BRIEF.md section 5). Say "supports", "contradicts" or "unclear", then why, in one line.

## 8. Machine-readable block
Last thing in the file. Valid JSON on its own lines, fenced with ```json:
{"track": "...", "demand_signal": "strong|moderate|weak|none", "buyer_price_points_usd": [], "seller_price_points_usd": [], "gates_supported": [], "gates_contradicted": [], "evidence_grade": "strong|moderate|weak", "sources_read": 0, "buyer_quotes": 0, "seller_quotes": 0}

## Caching rule
For every page you use as evidence, save the relevant text to rescue-research/cache/<short-slug>.md with this header:
URL: ...
Fetched: 2026-10-21
Title: ...
---
<the text you relied on: the quote and its surrounding context, or the table or numbers>

Check the cache folder before fetching. Reuse what is there.

## Network notes
See rescue-research/NETWORK-NOTES.md. WebFetch and curl are blocked. WebSearch only. Cache every search result you rely on.
