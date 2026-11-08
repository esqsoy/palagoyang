#!/usr/bin/env python3
"""Sonidos y letras 조립: template.html + sonidos-data.json → palagoyangsonidos.html, 그리고 index.html의 낱말 수·기록 옮기기.

- 원본: template.html(화면, derive-template.py로 한 번 뽑은 뒤 손으로 고친다), sonidos-data.json(sonidos.py가 만든다).
- 저장 키는 palagoyang-sonidos-(탄고고양 五十音의 tangogoyang-kana-와 같은 자리). palagoyang- 바로 뒤는 FÁBULA 몫으로 남긴다.
- 생성물 palagoyangsonidos.html은 직접 고치지 않는다.
사용: python3 -I pipeline/sonidos/sonidos.py && python3 -I pipeline/sonidos/build.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / 'pipeline'))
from record_transfer_build import build as record_transfer  # noqa: E402

OUT = ROOT / 'palagoyangsonidos.html'
tpl = (HERE / 'template.html').read_text(encoding='utf-8')
data = json.loads((HERE / 'sonidos-data.json').read_text(encoding='utf-8'))
marker = 'const DATA = /*__DATA__*/[];'
assert tpl.count(marker) == 1
html = tpl.replace(marker, 'const DATA = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';')
html = re.sub(r'(["\'`])palagoyang-', r'\1palagoyang-sonidos-', html)
OUT.write_text(html, encoding='utf-8')

words = sum(len(e['words']) for L in data for e in L['exercises'] if not e.get('rnd'))
cards = sum(len(e['words']) for L in data for e in L['exercises'])
idx = ROOT / 'index.html'
it = idx.read_text(encoding='utf-8')
it, n = re.subn(r'<!-- VOCAB_STATS:sonidos:START -->.*?<!-- VOCAB_STATS:sonidos:END -->',
                f'<!-- VOCAB_STATS:sonidos:START --><b>{words}낱말</b> · 소리를 듣고 철자를 친다<!-- VOCAB_STATS:sonidos:END -->', it, flags=re.S)
assert n == 1, 'index.html VOCAB_STATS:sonidos'
idx.write_text(record_transfer(it), encoding='utf-8')
print(OUT.name, f'{len(data)}강 · {sum(len(L["exercises"]) for L in data)}연습 · {words}낱말 · {cards}카드', '| index.html 낱말 수·기록 옮기기')
