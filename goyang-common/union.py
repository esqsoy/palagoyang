"""합집합 풀 계산: 원장 항목과 풀 후보가 몇 계보(family)에 들었는지 센다.

읽는 것: expressions.json(원장), source-check-20261103.json(TL90·VA·JF·PCIC 대조),
         union-pool.json(26.11.07부터 대조한 출처와 풀 후보)
쓰는 것: union-coverage.json

계보 수가 많을수록 '누가 써도 공통으로 쓰는 상황'(교집합) 쪽이고, 1 이하는 거르기 때 먼저 본다.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
led = json.loads((HERE / "expressions.json").read_text())
sc = json.loads((HERE / "source-check-20261103.json").read_text())
pool = json.loads((HERE / "union-pool.json").read_text())

FAM = {s["id"]: s["family"] for s in pool["sources"]}
SC_KEYS = {  # source-check의 목록 → 출처 id
    "threshold1990_functions": "TL90", "threshold1990_themes": "TL90", "threshold1990_exchange_patterns": "TL90",
    "vantage_additions": "VA", "jf_topics": "JF", "jf_categories": "JF",
    "pcic_functions": "PCIC", "pcic_tactics": "PCIC",
}
REF_PREFIX = {"TL90": "TL90", "VA": "VA", "JF": "JF", "PCIC": "PCIC"}

ALIAS = {old: it["id"] for it in led["items"] for old in it.get("merged", [])}  # 0.5에서 합친 옛 id → 새 자리
hits = defaultdict(set)       # 원장 항목 id → 출처 id
for key, src in SC_KEYS.items():
    for row in sc.get(key, []):
        for lid in row.get("ledger", []):
            hits[ALIAS.get(lid, lid)].add(src)
for it in led["items"]:        # 항목에 직접 단 ref(0.2·0.3에서 더한 근거)
    for r in it.get("ref", []):
        for src, pre in REF_PREFIX.items():
            if r.startswith(pre):
                hits[it["id"]].add(src)
cand_hits = defaultdict(set)
for src, entries in pool["entries"].items():
    for e in entries:
        if e["status"] == "있음":
            for lid in e.get("ledger", []):
                hits[ALIAS.get(lid, lid)].add(src)
        elif e["status"] in ("새", "후보"):
            cand_hits[e["cand"]].add(src)

for it in led["items"]:        # 0.5에서 풀 후보로 들어온 항목은 그 후보의 출처를 받는다
    if it.get("from_pool", "").startswith("N-"):
        hits[it["id"]] |= cand_hits.get(it["from_pool"], set())

def fams(srcs):
    return sorted({FAM[s] for s in srcs})

items = []
for it in led["items"]:
    s = sorted(hits.get(it["id"], set()))
    items.append({"id": it["id"], "task": it["task"], "sources": s, "families": fams(s), "n": len(fams(s))})
cands = []
for c in pool["candidates"]:
    s = sorted(cand_hits.get(c["id"], set()))
    cands.append({**{k: c[k] for k in ("id", "task", "group")}, "sources": s, "families": fams(s), "n": len(fams(s))})

all_fams = sorted(set(FAM.values()))
dist = Counter(x["n"] for x in items)
out = {
    "title": "원장 항목·풀 후보의 계보 수",
    "families": all_fams,
    "how": "계보 수 = 그 항목을 덮는 출처들의 계보(T, E, 독자 목록 하나하나) 수. 출처는 union-pool.json sources. 원장 항목은 source-check의 대조와 항목 ref, 26.11.07 대조의 '있음'을 합쳐 센다.",
    "ledger_distribution": {str(k): dist[k] for k in sorted(dist)},
    "ledger": items,
    "candidates": cands,
}
(HERE / "union-coverage.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
print("계보", all_fams)
print(f"원장 {len(items)}항목의 계보 수 분포", out["ledger_distribution"])
print("풀 후보", [(c["id"], c["n"]) for c in cands])
low = [x for x in items if x["n"] <= 1]
print("계보 1 이하 원장 항목", len(low))
