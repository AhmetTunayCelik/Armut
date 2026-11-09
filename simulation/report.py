import json;d=json.load(open('results.json'))
f=lambda x:f"{x:,}"
print("| Solution | P10 | P50 | P90 | P50 vs base | Weeks to detect | Rank score |\n|---|---|---|---|---|---|---|")
for r in d['rows']: print(f"| {r['name']} | {f(r['p10'])} | {f(r['p50'])} | {f(r['p90'])} | +{r['share_of_event_base']}% | {r['weeks_to_detect'] if r['weeks_to_detect'] is not None else 'n/a'} | {r['rank_score']} |")
print("\n| Program | P10 | P50 | P90 | P50 vs base |\n|---|---|---|---|---|")
for r in d['programs']: print(f"| {r['name']} | {f(r['p10'])} | {f(r['p50'])} | {f(r['p90'])} | +{r['share']}% |")
print("\nA1 sensitivity (middle case "+str(d['a1_base'])+"):",d['a1_sensitivity'])
print("Pro cost TL/yr:",d['pro_cost_TL'])
