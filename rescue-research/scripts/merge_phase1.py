import json, re, glob, os, sys
rows=[]
for f in sorted(glob.glob('tracks/*.md')):
    s=open(f,encoding='utf-8',errors='replace').read()
    m=re.findall(r'```json\s*(\{.*?\})\s*```', s, re.S)
    rec=None
    for cand in reversed(m):
        try:
            rec=json.loads(cand); break
        except Exception as e:
            pass
    if rec is None:
        # try last {...} containing "track"
        m2=re.findall(r'(\{[^{}]*"track"[^{}]*\})', s, re.S)
        for cand in reversed(m2):
            try: rec=json.loads(cand); break
            except: pass
    rows.append((os.path.basename(f), rec, len(s.split())))
print("| file | words | demand | buyer $ | seller $ | gates + | gates - | grade | sources | buyer q | seller q |")
print("|---|---|---|---|---|---|---|---|---|---|---|")
for f,r,w in rows:
    if not r:
        print(f"| {f} | {w} | NO JSON | | | | | | | | |"); continue
    g=lambda k: r.get(k,'')
    print(f"| {f} | {w} | {g('demand_signal')} | {g('buyer_price_points_usd')} | {g('seller_price_points_usd')} | {g('gates_supported')} | {g('gates_contradicted')} | {g('evidence_grade')} | {g('sources_read')} | {g('buyer_quotes')} | {g('seller_quotes')} |")
# gate tally
sup={i:[] for i in range(1,6)}; con={i:[] for i in range(1,6)}
for f,r,w in rows:
    if not r: continue
    for gname,d in (('gates_supported',sup),('gates_contradicted',con)):
        for x in r.get(gname,[]) or []:
            try:
                n=int(re.sub(r'\D','',str(x)) or 0)
                if n in d: d[n].append(f)
            except: pass
print("\n## Gate tally\n| gate | supported by | contradicted by |\n|---|---|---|")
for i in range(1,6):
    print(f"| {i} | {', '.join(sup[i]) or 'none'} | {', '.join(con[i]) or 'none'} |")
