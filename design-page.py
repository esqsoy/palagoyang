"""palagoyang/design-*.md(빨라고양 설계 안)를 영신 결정 페이지(Artifact용 HTML)로 그린다.
사용: python3 -I design-page.py <design.md> <out.html>
번호(##)마다 한 칸이고 칸마다 '댓글 달기' 단추가 있다(comments composer_only)."""
import html, re, sys
from pathlib import Path

src = Path(sys.argv[1]).read_text()
out = Path(sys.argv[2])
e = html.escape


def inline(t):
    t = e(t, quote=False)
    t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
    t = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', t)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"<span class=\"file\">\1</span>", t)
    t = re.sub(r"(?<![\"'>])(https?://[^\s<]+)", r'<a href="\1">\1</a>', t)
    return t


def choices(line):
    """'**고를 것:** A(추천) / B / C' → 고르기 알약"""
    body = line.split("</b>", 1)[1] if "</b>" in line else line
    opts = [o.strip().rstrip(".") for o in re.split(r"\s/\s", body)]
    pills = []
    for o in opts:
        rec = "(추천)" in o
        label = o.replace("(추천)", "").strip()
        pills.append(f'<span class="pill{" rec" if rec else ""}">{label}{"<small>추천</small>" if rec else ""}</span>')
    return '<div class="choose"><span class="choose-h">고를 것</span>' + "".join(pills) + "</div>"


lines = src.splitlines()
title = lines[0].lstrip("# ").strip()
intro, sections, cur = [], [], None
for ln in lines[1:]:
    m = re.match(r"^## (.+)$", ln)
    if m:
        cur = {"head": m.group(1), "lines": []}
        sections.append(cur)
        continue
    (cur["lines"] if cur else intro).append(ln)


def render_lines(ls):
    """줄 목록 → 중첩 목록 HTML. 들여쓰기 2칸이 한 단계. '고를 것' 줄은 알약 상자로."""
    nodes = []  # (level, kind, html) ; level 0 = 문단
    for ln in ls:
        if not ln.strip():
            continue
        m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)$", ln)
        if not m:
            nodes.append((0, "p", inline(ln.strip())))
            continue
        text = inline(m.group(3))
        kind = "choose" if text.startswith("<b>고를 것:</b>") else ("ol" if m.group(2)[0].isdigit() else "ul")
        nodes.append((len(m.group(1)) // 2 + 1, kind, text))

    def block(i, level):
        """level 단계의 형제들을 그린다. (html, 다음 i)"""
        out, lst = [], None
        while i < len(nodes):
            lv, kind, text = nodes[i]
            if lv < level or (lv == 0 and level > 0):
                break
            if lv == 0:
                out.append(f"<p>{text}</p>"); i += 1; continue
            if kind == "choose":
                if lst: out.append(f"</{lst}>"); lst = None
                out.append(choices(text)); i += 1; continue
            if lst is None:
                lst = kind; out.append(f"<{kind}>")
            i += 1
            inner, i = block(i, lv + 1) if i < len(nodes) and nodes[i][0] > lv else ("", i)
            out.append(f"<li>{text}{inner}</li>")
        if lst: out.append(f"</{lst}>")
        return "".join(out), i

    html_out, i, res = "", 0, []
    while i < len(nodes):
        h, j = block(i, 1 if nodes[i][0] else 0)
        if j == i:  # 문단
            res.append(f"<p>{nodes[i][2]}</p>"); i += 1
        else:
            res.append(h); i = j
    return "\n".join(res)


KEYS = '<div class="keys" aria-label="빈칸 아래 글자 단추 예">' + "".join(
    f'<kbd lang="es">{k}</kbd>' for k in "á é í ó ú ü ñ".split()) + "</div>"

css = """
/* 결정 페이지: 왼쪽 번호 띠 + 본문. 고를 것은 알약, 추천은 금잔화 색 */
:root{--bg:#f4f6f7;--card:#ffffff;--fg:#17212b;--mute:#566370;--line:#d5dce1;--accent:#b5650a;--accent-bg:#fdf0df;--teal:#1d6f6c;--teal-bg:#e3f1f0;
--display:"Gowun Batang",Georgia,serif;--body:"Pretendard","Apple SD Gothic Neo","Noto Sans KR",system-ui,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#11171c;--card:#182027;--fg:#e3e9ee;--mute:#97a5b1;--line:#2a343d;--accent:#f0a646;--accent-bg:#2c2214;--teal:#6cc5bf;--teal-bg:#15292a;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#11171c;--card:#182027;--fg:#e3e9ee;--mute:#97a5b1;--line:#2a343d;--accent:#f0a646;--accent-bg:#2c2214;--teal:#6cc5bf;--teal-bg:#15292a;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.6}
.wrap{max-width:780px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}
h1{font-family:var(--display);font-size:1.85rem;line-height:1.25;margin:0 0 4px;text-wrap:balance}
.sub{color:var(--mute);font-size:.88rem;margin:0 0 18px;letter-spacing:.02em}
.intro{max-width:66ch}.intro ul{padding-left:20px;margin:6px 0 0}.intro li{margin:2px 0}
.index{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:6px 14px;margin:26px 0 30px;padding:14px 16px;border:1px solid var(--line);border-radius:10px;background:var(--card)}
.index a{display:flex;gap:8px;align-items:baseline;color:var(--fg);text-decoration:none;font-size:.9rem;min-width:0}
.index a:hover span.t{text-decoration:underline}
.index .n{font-family:var(--mono);font-size:.78rem;color:var(--mute);font-variant-numeric:tabular-nums;width:1.6em;flex:none;text-align:right}
.index .dot{width:7px;height:7px;border-radius:50%;background:var(--accent);flex:none;align-self:center}
.index .dot.no{background:transparent;border:1px solid var(--line)}
.legend{font-size:.8rem;color:var(--mute);display:flex;gap:16px;flex-wrap:wrap;margin:-18px 0 26px}
.legend span{display:inline-flex;gap:6px;align-items:center}
section.item{display:grid;grid-template-columns:44px minmax(0,1fr);gap:0 14px;padding:18px 0 20px;border-top:1px solid var(--line)}
section.item .num{font-family:var(--display);font-size:1.6rem;color:var(--teal);line-height:1.1;text-align:right;font-variant-numeric:tabular-nums}
section.item h2{font-family:var(--display);font-size:1.15rem;line-height:1.35;margin:2px 0 8px;text-wrap:balance}
section.item ul,section.item ol{padding-left:20px;margin:4px 0}section.item li{margin:3px 0}
section.item ul ul{margin:2px 0 4px;color:var(--mute);font-size:.94em}
section.item b{font-weight:650}
code{font-family:var(--mono);font-size:.86em;background:var(--teal-bg);color:var(--teal);padding:0 4px;border-radius:4px;overflow-wrap:anywhere}
.file{font-family:var(--mono);font-size:.86em;color:var(--teal)}
a{color:var(--teal);overflow-wrap:anywhere}
.choose{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin:12px 0 4px;padding:10px 12px;background:var(--accent-bg);border-radius:8px}
.choose-h{font-size:.74rem;font-weight:700;letter-spacing:.06em;color:var(--accent);margin-right:4px}
.pill{font-size:.88rem;border:1px solid var(--line);background:var(--card);border-radius:999px;padding:2px 11px}
.pill.rec{border-color:var(--accent);color:var(--fg);font-weight:600}
.pill small{font-size:.68rem;color:var(--accent);margin-left:6px;font-weight:700}
.keys{display:flex;gap:6px;flex-wrap:wrap;margin:8px 0 6px}
kbd{font-family:var(--display);font-size:1.05rem;min-width:2.1em;text-align:center;padding:3px 6px;border:1px solid var(--line);border-bottom-width:3px;border-radius:7px;background:var(--card)}
.act{margin-top:10px}
.act button{font:inherit;font-size:.82rem;color:var(--teal);background:transparent;border:1px solid var(--teal);border-radius:6px;padding:3px 10px;cursor:pointer}
.act button:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.act button[hidden]{display:none}
section.done{opacity:.92}section.done .num{color:var(--mute)}
@media (max-width:480px){section.item{grid-template-columns:30px minmax(0,1fr);gap:0 10px}section.item .num{font-size:1.25rem}}
"""

SUBT = title[title.find('(')+1:-1] if '(' in title else ''
N_ITEMS = len([x for x in sections if re.match(r'\d+\.', x['head'])])
parts = ['<title>빨라고양 설계 안</title><meta name="claude:viewport-fit-sides" content="cover">',
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&display=swap">',
         f"<style>{css}</style><div class=\"wrap\">",
         f"<h1>{e(title.split(' (')[0])}</h1>",
         f'<p class="sub">{e(SUBT)} · 항목 {N_ITEMS}개</p>',
         f'<div class="intro">{render_lines(intro)}</div>']

idx = ['<nav class="index" aria-label="항목">']
for s in sections:
    m = re.match(r"(\d+)\.\s*(.+)", s["head"])
    sid = f"s{m.group(1)}" if m else "s-" + re.sub(r"\W+", "-", s["head"])[:20]
    s["id"] = sid
    has = any("**고를 것:**" in l for l in s["lines"])
    n = m.group(1) if m else "·"
    t = m.group(2) if m else s["head"]
    idx.append(f'<a href="#{sid}"><span class="n">{e(n)}</span><span class="dot{"" if has else " no"}"></span><span class="t">{e(t)}</span></a>')
idx.append("</nav>")
parts += idx
parts.append('<div class="legend"><span><span class="index"><span class="dot"></span></span>고를 것이 있는 항목</span></div>'.replace('<span class="index"><span class="dot"></span></span>', '<span style="width:7px;height:7px;border-radius:50%;background:var(--accent);display:inline-block"></span>'))

for s in sections:
    m = re.match(r"(\d+)\.\s*(.+)", s["head"])
    num = m.group(1) if m else ""
    head = m.group(2) if m else s["head"]
    body = render_lines(s["lines"])
    if num == "4":  # 입력: 글자 단추 모양을 실제로 보인다
        body = body.replace("<li>③ 빈칸 아래 글자 단추를 한 번 누른다.</li>", "<li>③ 빈칸 아래 글자 단추를 한 번 누른다." + KEYS + "</li>")
    cls = "item" if num else "item done"
    parts.append(f'<section class="{cls}" id="{s["id"]}"><div class="num">{e(num) if num else "·"}</div><div>'
                 f"<h2>{inline(head)}</h2>{body}"
                 f'<div class="act"><button type="button" class="cbtn" id="c-{s["id"]}" hidden>이 항목에 댓글 달기</button></div></div></section>')

parts.append("</div>")
parts.append("""<script>
(async () => {
  let c = null;
  try { c = window.claude && await window.claude.use("comments"); } catch (_) { c = null; }
  if (!c) return;
  document.querySelectorAll(".cbtn").forEach(b => {
    b.hidden = false;
    b.addEventListener("click", async () => {
      try { await c.openComposer({ element: b.closest("section") }); } catch (_) { b.hidden = true; }
    });
  });
})();
</script>""")
out.write_text("\n".join(parts))
print(out, len(sections), "sections")
