#!/usr/bin/env python3
"""언어불문 필수 표현 원장을 영신 직검수 페이지(Artifact용 HTML)로 뽑는다.

사용: python3 goyang-common/review-page.py [--out 파일]
항목마다 한 블록, 칸(A·B·C)마다 한 줄이라 댓글이 그 칸에 붙는다. 올릴 때 capabilities: {comments: {}}.
원장 0.4부터 문장은 항목의 rungs(칸)에 있다. ko가 null인 칸은 '쓸 차례'로 보인다.
"""
import html, json, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
doc = json.loads((HERE / 'expressions.json').read_text())
out = Path(sys.argv[sys.argv.index('--out') + 1]) if '--out' in sys.argv else HERE / 'out' / 'expressions-review.html'
e = html.escape
items = doc['items']
n_by = Counter(i['added'] for i in items if i.get('added'))
SRC = {'0.2': 'Threshold 1990·Vantage·JF Can-do', '0.3': 'PCIC'}
rungs = [r for i in items for r in i['rungs']]
n_new = sum(1 for r in rungs if not r.get('base'))
n_new_done = sum(1 for r in rungs if not r.get('base') and r['ko'])
done_groups = [g for g in doc['groups'] if all(r['ko'] for i in items if i['group'] == g for r in i['rungs'])]

css = """
:root{--bg:#f6f7f4;--fg:#1d2420;--mute:#5d6a62;--line:#d7ddd6;--card:#ffffff;--accent:#2f6b4f;--warn:#9a5b12;--warnbg:#fbf1e2;--newbg:#eef6f0;
--display:"Gowun Batang",Georgia,serif;--body:"Pretendard","Apple SD Gothic Neo","Noto Sans KR",system-ui,sans-serif}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#151a17;--fg:#e4ebe6;--mute:#9aa8a0;--line:#2c352f;--card:#1c2320;--accent:#7cc4a0;--warn:#e3b46e;--warnbg:#2b2418;--newbg:#18261e;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#151a17;--fg:#e4ebe6;--mute:#9aa8a0;--line:#2c352f;--card:#1c2320;--accent:#7cc4a0;--warn:#e3b46e;--warnbg:#2b2418;--newbg:#18261e;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font-family:var(--body);line-height:1.55}
.wrap{max-width:760px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 64px}
h1{font-family:var(--display);font-size:1.7rem;margin:0 0 6px;text-wrap:balance}
.lead{color:var(--mute);margin:0 0 14px;font-size:.95rem;max-width:68ch}
.kinds{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:8px;margin:0 0 26px}
.kinds div{border:1px solid var(--line);border-radius:8px;padding:10px 12px;background:var(--card);font-size:.88rem}
.kinds b{display:block;color:var(--accent);font-family:ui-monospace,monospace;font-size:.82rem}
h2{font-family:var(--display);font-size:1.2rem;margin:30px 0 8px;padding-bottom:6px;border-bottom:1px solid var(--line)}
h2 small{font-family:var(--body);color:var(--mute);font-size:.8rem;font-weight:400;margin-left:6px}
.item{padding:10px 4px 8px;border-bottom:1px dashed var(--line)}
.head{display:flex;flex-wrap:wrap;gap:4px 10px;align-items:baseline;margin-bottom:4px}
.id{font-family:ui-monospace,monospace;font-size:.78rem;color:var(--mute);font-variant-numeric:tabular-nums}
.task{font-size:.85rem;color:var(--mute)}
.rung{display:grid;grid-template-columns:44px 1fr;gap:10px;align-items:baseline;padding:3px 6px;border-radius:4px}
.rung.new{background:var(--newbg)}
.lv{font-family:ui-monospace,monospace;font-size:.75rem;color:var(--accent);font-weight:600}
.ko{font-size:1.05rem}
.todo{font-size:.85rem;color:var(--mute);font-style:italic}
.hint{font-size:.78rem;color:var(--warn);background:var(--warnbg);border-radius:4px;padding:1px 6px}
.new-tag{font-size:.75rem;font-weight:600;color:var(--accent);border:1px solid var(--accent);border-radius:4px;padding:0 5px}
.ref{font-size:.74rem;color:var(--mute);font-family:ui-monospace,monospace;overflow-wrap:anywhere}
.legend{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:.82rem;color:var(--mute);margin:0 0 8px}
.legend span{display:inline-flex;align-items:center;gap:6px}
.sw{display:inline-block;width:18px;height:12px;border-radius:3px;border:1px solid var(--line)}
.sw.new{background:var(--newbg)}
"""
parts = ['<title>언어불문 필수 표현</title><meta name="claude:viewport-fit-sides" content="cover">',
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@700&display=swap">',
         f'<style>{css}</style><div class="wrap">',
         '<h1>언어불문 필수 표현 원장</h1>',
         f'<p class="lead">초안 {e(doc["version"])} · {e(doc["date"])} · {len(items)}항목 {len(rungs)}칸. 항목마다 같은 일을 수준별로 말하는 칸(A1~A2 기본꼴 · B1~B2 · C1 다듬은 꼴)이 있어요. '
         f'새 칸 {n_new}개 가운데 {n_new_done}개를 썼습니다'
         + (f'(다 쓴 갈래: {", ".join(e(g) for g in done_groups)})' if done_groups else '')
         + '. 칸을 눌러 댓글을 달아 주세요. 문장 고칠 것, 수준이 어긋난 것, 칸끼리 상황이 달라진 것.</p>',
         ('<p class="lead">원문과 대조해 더한 항목에는 판 표시가 붙어 있습니다: '
          + ', '.join(f'<span class="new-tag">{e(v)} 추가</span> {n}항목({e(SRC.get(v, "원문"))})' for v, n in sorted(n_by.items()))
          + '. 회색 글씨가 근거 위치예요.</p>' if n_by else ''),
         '<div class="legend"><span><span class="sw"></span>0.3까지의 문장</span><span><span class="sw new"></span>0.4에서 새로 쓴 칸</span></div>',
         '<div class="kinds"><div><b>same</b>거의 번역으로 통한다</div><div><b>counterpart</b>같은 상황, 다른 표현</div><div><b>none</b>그 언어에 해당 표현 없음</div></div>']
for g, name in doc['groups'].items():
    rows = [i for i in items if i['group'] == g]
    rs = [r for i in rows for r in i['rungs']]
    todo = sum(1 for r in rs if not r['ko'])
    parts.append(f'<h2>{e(name)}<small>{e(g)} · {len(rows)}항목 · {len(rs)}칸' + (f' · 쓸 칸 {todo}' if todo else '') + '</small></h2>')
    for i in rows:
        tags = []
        if i.get('added'):
            tags.append(f'<span class="new-tag">{e(i["added"])} 추가</span>')
        if i.get('hint'):
            tags.append('<span class="hint">대응 가능성 큼</span>')
        if i.get('ref'):
            tags.append(f'<span class="ref">{e(" · ".join(i["ref"]))}</span>')
        parts.append(f'<div class="item" id="{e(i["id"])}"><div class="head"><span class="id">{e(i["id"])}</span><span class="task">{e(i["task"])}</span>{"".join(tags)}</div>')
        for r in i['rungs']:
            cls = 'rung' if r.get('base') else 'rung new'
            text = f'<span class="ko">{e(r["ko"])}</span>' if r['ko'] else '<span class="todo">쓸 차례</span>'
            parts.append(f'<div class="{cls}" id="{e(r["id"])}"><span class="lv">{e(r["level"])}</span>{text}</div>')
        parts.append('</div>')
parts.append('</div>')
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text('\n'.join(parts))
print(out)
