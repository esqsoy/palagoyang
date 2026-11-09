#!/usr/bin/env python3
"""스페인어 판 원장(es/expressions-es.json) 기계 검사.

- 칸 id가 공통 원장(goyang-common/expressions.json)에 있고 겹치지 않는가
- 갈래(kind)가 다섯 가운데 하나인가
- 빈칸 낱말이 문장(es, es_f)에 낱말째로 있는가(대소문자는 가리지 않고 악센트는 가린다)
- 문법 id·덩어리가 문법 지도(es/grammar-map.json)에 있는가
- 칸 수준과 쓴 문법의 띠가 맞는가: A 칸은 A2까지, B 칸은 B2까지 (넘으면 경고. 판단은 사람이 한다)
사용: python3 -I es/ledger-check.py
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
led = json.loads((ROOT / 'goyang-common' / 'expressions.json').read_text(encoding='utf-8'))
es = json.loads((ROOT / 'es' / 'expressions-es.json').read_text(encoding='utf-8'))
gm = json.loads((ROOT / 'es' / 'grammar-map.json').read_text(encoding='utf-8'))

KINDS = {'same', 'counterpart', 'paraphrase', 'none-situation', 'none-silence'}
ORDER = ['0', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2']
CEIL = {'A': 'A2', 'B': 'B2', 'C': 'C2'}
rung_ko = {r['id']: (r['level'], r['ko']) for it in led['items'] for r in it['rungs']}
gram = {g['id']: g['band'] for g in gm['items']}
chunks = {c['chunk'] for c in gm['chunks']}
WORD = re.compile(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+")

err, warn = [], []


def words(s):
    return [w.lower() for w in WORD.findall(s)]


def check_entry(where, x):
    for f in ('es', 'es_f'):
        if f in x and x['blank'].lower() not in words(x[f]):
            err.append(f'{where}: 빈칸 "{x["blank"]}"이 {f}에 낱말째로 없다')
    if 'es_f' in x and x['es_f'] == x['es']:
        err.append(f'{where}: es_f가 es와 같다')
    for a in x.get('alt', []):
        if a.lower() == x['blank'].lower():
            err.append(f'{where}: alt에 빈칸과 같은 말')
    if len(x.get('alt', [])) > 3:
        warn.append(f'{where}: alt가 셋보다 많다. 빈칸을 옮길 것')
    for g in x.get('grammar', []):
        if g not in gram:
            err.append(f'{where}: 문법 지도에 없는 id {g}')
    for c in x.get('chunks', []):
        if c not in chunks:
            err.append(f'{where}: 덩어리 목록에 없는 것 {c}')


seen = set()
for r in es['rungs']:
    i = r['id']
    if i not in rung_ko:
        err.append(f'{i}: 공통 원장에 없는 칸')
        continue
    if i in seen:
        err.append(f'{i}: 두 번 나온다')
    seen.add(i)
    if r.get('kind') not in KINDS:
        err.append(f'{i}: 갈래 {r.get("kind")}')
    check_entry(i, r)
    top = max((gram.get(g, '0') for g in r.get('grammar', [])), key=ORDER.index, default='0')
    ceil = CEIL[i[-1]]
    if ORDER.index(top) > ORDER.index(ceil):
        warn.append(f'{i}: {rung_ko[i][0]} 칸인데 {top} 문법을 쓴다({", ".join(g for g in r["grammar"] if gram.get(g) == top)})'
                    + (' · map 제안 있음' if r.get('map') else ''))
for o in es.get('own', []):
    if o['of'] not in seen:
        err.append(f'own {o["of"]}: 그 칸이 판 원장에 없다')
    check_entry(f'own({o["of"]})', o)

groups = {}
for i in rung_ko:
    g = i.split('-')[0]
    groups.setdefault(g, [0, 0])[0] += 1
    if i in seen:
        groups[g][1] += 1
kinds = {}
for r in es['rungs']:
    kinds[r['kind']] = kinds.get(r['kind'], 0) + 1
print('칸', len(seen), '/', len(rung_ko), '·', ' '.join(f'{g} {b}/{a}' for g, (a, b) in groups.items()))
print('갈래', kinds, '· 고유 층', len(es.get('own', [])), '· 성 두 꼴', sum('es_f' in r for r in es['rungs']),
      '· 대체 정답 든 칸', sum(bool(r.get('alt')) for r in es['rungs']))
gaps = [(r['id'], g) for r in es['rungs'] for g in r.get('gap', [])]
for i, g in gaps:
    print('지도에 없음', i, g)
for r in es['rungs']:
    if r.get('map'):
        print('지도 제안', r['id'], r['map'])
for w in warn:
    print('경고', w)
for e in err:
    print('오류', e)
sys.exit(1 if err else 0)
