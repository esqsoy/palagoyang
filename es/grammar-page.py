"""es/grammar-map.json(빨라고양 문법 지도)을 읽기용 md와 검토 페이지(Artifact용 HTML)로 그린다.
사용: python3 -I es/grammar-page.py es/grammar-map.json --md es/grammar-map.md --html <out.html>
페이지는 항목마다 '댓글' 단추가 있다(comments composer_only)."""
import argparse, html, json, re
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("src")
ap.add_argument("--md")
ap.add_argument("--html")
a = ap.parse_args()
d = json.loads(Path(a.src).read_text(encoding="utf-8"))
e = html.escape
items = d["items"]
by_band = {b["band"]: [x for x in items if x["band"] == b["band"]] for b in d["bands"]}
band_name = {b["band"]: b["name"] for b in d["bands"]}


def code(t):
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", e(t, quote=False))


# ── md ──
if a.md:
    L = [f"# {d['name']} {d['version']}", "",
         f"갱신: {d['date']}. 원본은 [grammar-map.json](grammar-map.json)이고, 이 문서는 `python3 -I es/grammar-page.py es/grammar-map.json --md es/grammar-map.md`로 다시 만든다(손으로 고치지 않는다).", "",
         d["about"], "", "## 쓰는 규칙", ""]
    for r in d["rules"]:
        L.append(f"- **{r['title']}.** {r['body']}")
    L += ["", "## PCIC와 다르게 둔 것", ""]
    for v in d["deviations"]:
        L.append(f"- **{v['what']}.** {v['why']}")
    for b in d["bands"]:
        xs = by_band[b["band"]]
        L += ["", f"## {b['name']} ({len(xs)}항목)", "", b["about"], ""]
        for x in xs:
            L.append(f"- **{x['id']} {x['title']}** — {' / '.join(x['es'])}")
            for k, lab in (("latam", "중남미"), ("ko", "한국어"), ("note", "덧붙임")):
                if x.get(k):
                    L.append(f"  - {lab}: {x[k]}")
            if x["pcic"]:
                L.append(f"  - PCIC 2장 {', '.join(x['pcic'])}")
    L += ["", f"## 덩어리 (먼저 통째로 쓰는 말, {len(d['chunks'])}개)", "",
          "| 덩어리 | 처음 쓰는 띠 | 체계가 되는 항목 |", "|---|---|---|"]
    for c in d["chunks"]:
        L.append(f"| {c['chunk']} | {band_name[c['from']]} | {c['explained'] or '굳은 말'} |")
    L += ["", "## 출처", ""]
    for s in d["sources"]:
        L.append(f"- {s['name']}: {s['url']} ({s['use']})")
    Path(a.md).write_text("\n".join(L) + "\n", encoding="utf-8")
    print(a.md)

# ── html ──
if a.html:
    css = """
:root{--bg:#f4f6f7;--card:#ffffff;--fg:#17212b;--mute:#566370;--line:#d5dce1;--accent:#b5650a;--accent-bg:#fdf0df;--teal:#1d6f6c;--teal-bg:#e3f1f0;--rose:#9b3d55;--rose-bg:#f8e8ec;
--display:"Gowun Batang",Georgia,serif;--body:"Pretendard","Apple SD Gothic Neo","Noto Sans KR",system-ui,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#11171c;--card:#182027;--fg:#e3e9ee;--mute:#97a5b1;--line:#2a343d;--accent:#f0a646;--accent-bg:#2c2214;--teal:#6cc5bf;--teal-bg:#15292a;--rose:#e58ea4;--rose-bg:#2d1a20;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#11171c;--card:#182027;--fg:#e3e9ee;--mute:#97a5b1;--line:#2a343d;--accent:#f0a646;--accent-bg:#2c2214;--teal:#6cc5bf;--teal-bg:#15292a;--rose:#e58ea4;--rose-bg:#2d1a20;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font-family:var(--body);font-size:15px;line-height:1.6}
.wrap{max-width:820px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:32px 72px}
h1{font-family:var(--display);font-size:1.85rem;line-height:1.25;margin:0 0 4px;text-wrap:balance}
h2{font-family:var(--display);font-size:1.3rem;line-height:1.3;margin:0 0 6px}
.sub{color:var(--mute);font-size:.88rem;margin:0 0 18px}
.about{max-width:68ch;margin:0 0 14px}
details.rules{border:1px solid var(--line);border-radius:10px;background:var(--card);padding:10px 16px;margin:0 0 12px}
details.rules summary{cursor:pointer;font-weight:650}
details.rules ul{padding-left:20px;margin:8px 0 4px}details.rules li{margin:4px 0}
nav.bands{display:flex;flex-wrap:wrap;gap:6px;margin:22px 0 8px;position:sticky;top:0;background:var(--bg);padding:8px 0;z-index:2}
nav.bands a{font-size:.88rem;text-decoration:none;color:var(--fg);border:1px solid var(--line);background:var(--card);border-radius:999px;padding:3px 12px;font-variant-numeric:tabular-nums}
nav.bands a small{color:var(--mute);margin-left:5px}
section.band{padding:22px 0 6px;border-top:2px solid var(--line);margin-top:18px;scroll-margin-top:52px}
section.band>p{color:var(--mute);margin:0 0 10px;max-width:68ch}
.it{display:grid;grid-template-columns:62px minmax(0,1fr);gap:0 12px;padding:10px 0;border-top:1px solid var(--line)}
.it:first-of-type{border-top:0}
.id{font-family:var(--mono);font-size:.8rem;color:var(--teal);padding-top:3px;font-variant-numeric:tabular-nums}
.t{font-weight:650;line-height:1.45}
.es{margin:3px 0 2px;display:flex;flex-wrap:wrap;gap:4px 8px}
.es span{font-family:var(--display);font-size:1.02rem;background:var(--teal-bg);border-radius:6px;padding:0 7px}
.nt{font-size:.9rem;margin:3px 0 0;color:var(--fg)}
.tag{display:inline-block;font-size:.7rem;font-weight:700;letter-spacing:.04em;border-radius:4px;padding:0 5px;margin-right:6px;vertical-align:1px}
.tag.la{background:var(--accent-bg);color:var(--accent)}.tag.ko{background:var(--rose-bg);color:var(--rose)}.tag.no{background:var(--teal-bg);color:var(--teal)}
.pc{font-size:.76rem;color:var(--mute);margin-top:3px;font-family:var(--mono)}
.cb{font:inherit;font-size:.74rem;color:var(--teal);background:transparent;border:1px solid var(--line);border-radius:5px;padding:0 7px;margin-top:5px;cursor:pointer}
.cb:focus-visible{outline:2px solid var(--accent);outline-offset:2px}.cb[hidden]{display:none}
table{border-collapse:collapse;width:100%;font-size:.9rem;margin:6px 0}
th,td{text-align:left;padding:6px 8px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:.76rem;color:var(--mute);font-weight:650}
td.c{font-family:var(--display);font-size:1rem}
td.r{font-family:var(--mono);font-size:.8rem;color:var(--teal);white-space:nowrap}
.tw{overflow-x:auto}
code{font-family:var(--mono);font-size:.86em;background:var(--teal-bg);color:var(--teal);padding:0 4px;border-radius:4px}
a{color:var(--teal);overflow-wrap:anywhere}
@media (max-width:480px){.it{grid-template-columns:minmax(0,1fr)}.id{padding:0}}
"""
    P = ['<title>빨라고양 문법 지도</title><meta name="claude:viewport-fit-sides" content="cover">',
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&display=swap">',
         f"<style>{css}</style><div class=\"wrap\">",
         f"<h1>{e(d['name'])}</h1>",
         f'<p class="sub">{e(d["version"])} · {e(d["date"])} · 항목 {len(items)}개 · 덩어리 {len(d["chunks"])}개</p>',
         f'<p class="about">{e(d["about"])}</p>',
         '<details class="rules" open><summary>쓰는 규칙</summary><ul>' +
         "".join(f"<li><b>{e(r['title'])}.</b> {code(r['body'])}</li>" for r in d["rules"]) + "</ul></details>",
         '<details class="rules"><summary>PCIC와 다르게 둔 것</summary><ul>' +
         "".join(f"<li><b>{e(v['what'])}.</b> {e(v['why'])}</li>" for v in d["deviations"]) + "</ul></details>"]
    P.append('<nav class="bands" aria-label="띠">' + "".join(
        f'<a href="#b-{b["band"]}">{e(b["name"])}<small>{len(by_band[b["band"]])}</small></a>' for b in d["bands"]) +
        '<a href="#chunks">덩어리<small>' + str(len(d["chunks"])) + "</small></a></nav>")
    for b in d["bands"]:
        P.append(f'<section class="band" id="b-{b["band"]}"><h2>{e(b["name"])}</h2><p>{e(b["about"])}</p>')
        for x in by_band[b["band"]]:
            notes = "".join(
                f'<p class="nt"><span class="tag {cls}">{lab}</span>{e(x[k])}</p>'
                for k, lab, cls in (("latam", "중남미", "la"), ("ko", "한국어", "ko"), ("note", "덧붙임", "no")) if x.get(k))
            pc = f'<div class="pc">PCIC 2장 {e(", ".join(x["pcic"]))}</div>' if x["pcic"] else ""
            es = "".join(f"<span>{e(s)}</span>" for s in x["es"])
            P.append(f'<div class="it" id="{e(x["id"])}"><div class="id">{e(x["id"])}</div><div>'
                     f'<div class="t">{e(x["title"])}</div><div class="es" lang="es">{es}</div>{notes}{pc}'
                     f'<button type="button" class="cb" hidden>댓글</button></div></div>')
        P.append("</section>")
    P.append('<section class="band" id="chunks"><h2>덩어리</h2><p>회화에 꼭 필요해서 문법보다 먼저 통째로 쓰는 말이다. 오른쪽 항목에서 체계가 된다.</p>'
             '<div class="tw"><table><thead><tr><th>덩어리</th><th>처음 쓰는 띠</th><th>체계가 되는 항목</th></tr></thead><tbody>')
    for c in d["chunks"]:
        ex = f'<a href="#{e(c["explained"])}">{e(c["explained"])}</a>' if c["explained"] else "굳은 말"
        P.append(f'<tr><td class="c" lang="es">{e(c["chunk"])}</td><td>{e(band_name[c["from"]])}</td><td class="r">{ex}</td></tr>')
    P.append("</tbody></table></div></section>")
    P.append('<section class="band"><h2>출처</h2><ul>' + "".join(
        f'<li>{e(s["name"])}: <a href="{e(s["url"])}">{e(s["url"])}</a> ({e(s["use"])})</li>' for s in d["sources"]) + "</ul></section>")
    P.append("</div>")
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
    Path(a.html).write_text("\n".join(P), encoding="utf-8")
    print(a.html)
