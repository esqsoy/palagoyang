#!/usr/bin/env python3
"""스페인어 판 원장 영신 직검수 페이지(Artifact용 HTML). 칸마다 '댓글' 단추(comments composer_only).
짜임과 겉모습은 es/grammar-page.py 검토 페이지와 같다.
사용: python3 -I es/ledger-page.py <out.html>"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
led = json.loads((ROOT / 'goyang-common' / 'expressions.json').read_text(encoding='utf-8'))
es = json.loads((ROOT / 'es' / 'expressions-es.json').read_text(encoding='utf-8'))
gm = json.loads((ROOT / 'es' / 'grammar-map.json').read_text(encoding='utf-8'))
out = Path(sys.argv[1])
e = html.escape

css = (ROOT / 'es' / 'grammar-page.py').read_text(encoding='utf-8').split('css = """', 1)[1].split('"""', 1)[0]
css += """
.it{grid-template-columns:72px minmax(0,1fr)}
.lv{display:block;font-size:.72rem;color:var(--mute)}
.ko{font-weight:650;line-height:1.45}
.sp{font-family:var(--display);font-size:1.08rem;line-height:1.5;margin:2px 0 0}
.sp mark{background:var(--accent-bg);color:var(--accent);font-weight:700;border-radius:4px;padding:0 3px}
.sp small{font-family:var(--body);font-size:.72rem;color:var(--mute);margin-right:6px}
.meta{font-size:.76rem;color:var(--mute);margin-top:3px}
.meta code{font-size:.74rem}
.tag.kd{background:var(--teal-bg);color:var(--teal)}
.own{margin:6px 0 0;padding:4px 0 0 10px;border-left:3px solid var(--line)}
h3{font-size:1rem;margin:18px 0 0}
h3 small{font-family:var(--mono);color:var(--teal);font-weight:400;margin-right:8px}
@media (max-width:480px){.it{grid-template-columns:minmax(0,1fr)}.lv{display:inline;margin-left:8px}}
"""
band_of = {g['id']: g['band'] for g in gm['items']}
title_of = {g['id']: g['title'] for g in gm['items']}
mine = {r['id']: r for r in es['rungs']}
own = {}
for o in es.get('own', []):
    own.setdefault(o['of'], []).append(o)
KIND = {'same': '같음', 'counterpart': '대응', 'paraphrase': '풀어 말함', 'none-situation': '상황 없음', 'none-silence': '말 안 함'}


def mark(s, w):
    m = re.search(r'(?<![A-Za-zÁÉÍÓÚÜÑáéíóúüñ])' + re.escape(w) + r'(?![A-Za-zÁÉÍÓÚÜÑáéíóúüñ])', s, re.I)
    if not m:
        return e(s)
    return e(s[:m.start()]) + '<mark>' + e(m.group(0)) + '</mark>' + e(s[m.end():])


def meta(x):
    bits = []
    if x.get('alt'):
        bits.append('대체 정답 ' + ', '.join(f'<b lang="es">{e(a)}</b>' for a in x['alt']))
    if x.get('grammar'):
        bits.append('문법 ' + ' '.join(f'<code title="{e(title_of[g])}">{e(g)}</code>' for g in x['grammar']))
    if x.get('chunks'):
        bits.append('덩어리 ' + ' · '.join(f'<span lang="es">{e(c)}</span>' for c in x['chunks']))
    return f'<div class="meta">{" · ".join(bits)}</div>' if bits else ''


def notes(x):
    P = []
    for k, lab, cls in (('note', '해설', 'no'), ('gap', '지도에 없음', 'ko'), ('map', '지도 제안', 'la'), ('conf', '확신', 'ko')):
        v = x.get(k)
        if not v:
            continue
        for t in (v if isinstance(v, list) else [v]):
            P.append(f'<p class="nt"><span class="tag {cls}">{lab}</span>{e(t)}</p>')
    return ''.join(P)


groups = [it for it in led['items'] if any(r['id'] in mine for r in it['rungs'])]
n = sum(1 for it in groups for r in it['rungs'] if r['id'] in mine)
P = ['<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>스페인어 판 원장 직검수</title><meta name="claude:viewport-fit-sides" content="cover">',
     '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&display=swap">',
     f'<style>{css}</style><div class="wrap">',
     f'<h1>{e(es["name"])} · F1 시범</h1>',
     f'<p class="sub">{e(es["version"])} · {e(es["date"])} · Claude 초안 · {len(groups)}항목 {n}칸 / 원장 585칸 · 고유 층 {len(es.get("own", []))}</p>',
     f'<p class="about">{e(es["about"])}</p>',
     '<details class="rules" open><summary>봐 줄 것</summary><ul>'
     '<li><b>문장이 자연스러운지.</b> A → B → C로 갈수록 정중하고 길어지는지도 본다. 귤빛 칸이 빈칸 낱말이다.</li>'
     '<li><b>빈칸과 대체 정답.</b> 빈칸에 같은 뜻으로 들어가는 다른 말은 정답으로 받는다(F1-02A Soy / Vengo).</li>'
     '<li><b>높임.</b> 한국어에 -시-·-세요·성함이 있으면 usted, 해요체면 tú로 썼다(F1-27A ¿Cómo te llamas? / F1-27B ¿cómo se llama usted?).</li>'
     '<li><b>성이 드러나는 \'나\'.</b> F1-20B Estoy seguro / segura처럼 두 꼴을 다 적고 둘 다 정답으로 받는다. 화면에는 기기마다 처음 시작할 때 고른 \'남자 / 여자\'의 꼴이 보인다(영신 26.11.09).</li>'
     '<li>고칠 문장은 그 줄 댓글로.</li></ul></details>',
     '<details class="rules"><summary>쓰는 규칙</summary><ul>' + ''.join(f'<li>{e(r)}</li>' for r in es['rules']) + '</ul></details>']
for it in groups:
    P.append(f'<h3><small>{e(it["id"])}</small>{e(it["task"])}</h3>')
    for r in it['rungs']:
        x = mine.get(r['id'])
        if not x:
            continue
        sp = f'<p class="sp" lang="es">{mark(x["es"], x["blank"])}</p>'
        if x.get('es_f'):
            sp = (f'<p class="sp" lang="es"><small>남성</small>{mark(x["es"], x["blank"])}</p>'
                  f'<p class="sp" lang="es"><small>여성</small>{mark(x["es_f"], x["blank"])}</p>')
        ow = ''.join(f'<div class="own"><p class="nt"><span class="tag la">고유 층 둘째 꼴</span>따로 카드</p>'
                     f'<p class="sp" lang="es">{mark(o["es"], o["blank"])}</p>{meta(o)}{notes(o)}</div>' for o in own.get(r['id'], []))
        P.append(f'<div class="it" id="{e(r["id"])}"><div class="id">{e(r["id"])}<span class="lv">{e(r["level"])}</span></div><div>'
                 f'<div class="ko"><span class="tag kd">{e(KIND[x["kind"]])}</span>{e(r["ko"])}</div>{sp}{meta(x)}{notes(x)}{ow}'
                 f'<button type="button" class="cb" hidden>댓글</button></div></div>')
P.append('</div>')
P.append("""<script>
(async () => {
  let c = null;
  try { c = window.claude && await window.claude.use("comments"); } catch (_) { c = null; }
  if (!c) return;
  document.querySelectorAll(".cb").forEach(b => {
    b.hidden = false;
    b.addEventListener("click", async () => {
      try { await c.openComposer({ element: b.closest(".it") }); } catch (_) { b.hidden = true; }
    });
  });
})();
</script>""")
out.write_text('\n'.join(P), encoding='utf-8')
print(out)
