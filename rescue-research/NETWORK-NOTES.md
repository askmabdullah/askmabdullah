# NETWORK NOTES: read before you start (applies to every agent)

## What works and what does not
- WebFetch is BLOCKED for every public host in this environment (DNS fails: reddit, HN, Algolia, Arctic Shift, Fiverr, Upwork, Facebook Ad Library, Google Trends, vendor sites, all of them). Do not spend more than one attempt on WebFetch. Shell curl is also blocked.
- WebSearch WORKS. It is your only source. Use mode "standard" first, and "extended" when results are thin or when you need recent or niche material (ad library pages, Reddit threads, prices).
- Use the allowed_domains parameter to target a site, for example allowed_domains ["reddit.com"] or ["news.ycombinator.com"] or ["fiverr.com"] or ["upwork.com"] or ["indiehackers.com"] or ["facebook.com"] or ["x.com","twitter.com"]. Run many narrow, site-targeted searches rather than a few broad ones.
- Plan on 25 to 45 searches in your 60-minute budget. If the search tool returns an error or rate limit, wait and try a different query. Do not hammer it.

## Evidence rule under this constraint
- You can only quote text that appears in the search result output (snippets, summaries, titles). Copy quotes verbatim from that output. Never extend, complete or "clean up" a quote.
- Mark every quote and number with "Source text: search snippet" so verifiers know the full page was not opened.
- Upvote counts, dates and usernames: record them only if they appear in the result text. Otherwise write "unknown". Do not guess.
- A search result summary written by the search tool is NOT a quote. Only text that is clearly quoted from the page counts as a quote. If unsure, label it "paraphrase from search summary" and do not put it in quotation marks.

## Caching rule (mandatory, verifiers depend on it)
- After EVERY search you rely on, append the full raw result text to a cache file: rescue-research/cache/<track-slug>-searches.md
- Format per entry:
  ---
  QUERY: <exact query> | MODE: standard|extended | DOMAINS: <list or none> | DATE: 2026-10-21
  <paste the full result text exactly as returned, including links>
  ---
- Use the Bash tool with a heredoc (cat >> file <<'EOF' ... EOF) to append. Do this as you go, not at the end.
- In your track file, every quote and number must name the cache file and the QUERY it came from.

## Things that cannot be done here, so say so plainly in your file
- Opening Meta Ad Library, Google Trends, Google autocomplete, Fiverr or Upwork search pages directly. You can only find what search engines have indexed or what third parties have written about them.
- Reading full Reddit or HN threads. You get snippets only.
- Counting things precisely. Give what the snippets show and label counts as "from search results, partial".

## UPDATE (round 2, 22:20 UTC): hard search quota
- WebSearch has a shared quota of 200 calls per turn across ALL agents. Your brief gives you a hard cap. Do not exceed it. Count your searches. When you hit your cap, stop and write up.
- allowed_domains ["reddit.com"] returns API error 400. Do NOT use it. Instead put "site:reddit.com" or "reddit" in the query text. Results come back from Reddit mirrors (reddit.birdcat.cafe, redlib.hackliberty.org, etc.). Those count as Reddit evidence; record the mirror URL and the subreddit and thread slug.
- For HN use "site:news.ycombinator.com" in the query text, or search the thread title plus "hacker news".
- WebSearch returns a tool-written summary plus links. Only text inside quotation marks in the summary may be recorded as a quote, with the label "search snippet". Everything else is a paraphrase and must be labelled so.
- Use mode "extended" for Reddit and HN queries; it returns more and fresher material. Use "standard" for vendor pages.
