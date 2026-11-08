"""Sonidos y letras 영신 직검수 페이지(Artifact용 HTML). 카드마다 '댓글' 단추(comments composer_only).
짜임은 es/grammar-page.py 검토 페이지와 같다.
사용: python3 -I pipeline/sonidos/review-page.py <out.html>"""
import html
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
d = json.loads((HERE / 'sonidos-data.json').read_text(encoding='utf-8'))
e = html.escape
out = Path(sys.argv[1])

css = (HERE.parents[1] / 'es' / 'grammar-page.py').read_text(encoding='utf-8').split('css = """', 1)[1].split('"""', 1)[0]
css += """
.it{grid-template-columns:118px minmax(0,1fr)}
.w{font-family:var(--display);font-size:1.32rem;font-weight:700;line-height:1.2;color:var(--fg)}
.ipa{font-family:"Doulos SIL","Charis SIL","Gentium Plus","Noto Sans",system-ui,sans-serif;color:var(--teal);font-size:.95rem}
.ko{font-weight:650}
details.pn{margin:4px 0 0;font-size:.88rem}
details.pn summary{cursor:pointer;color:var(--mute);font-size:.8rem}
details.pn ul{padding-left:18px;margin:4px 0}
details.pn li{margin:3px 0}
details.pn b{font-weight:650}
h3{font-size:1rem;margin:16px 0 2px}
h3 small{color:var(--mute);font-weight:400;margin-left:6px}
@media (max-width:480px){.it{grid-template-columns:minmax(0,1fr)}}
"""
words = sum(len(x['words']) for L in d for x in L['exercises'] if not x.get('rnd'))
P = ['<title>Sonidos y letras 직검수</title><meta name="claude:viewport-fit-sides" content="cover">',
     '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@400;700&display=swap">',
     f'<style>{css}</style><div class="wrap">',
     '<h1>Sonidos y letras · 소리·글자 단계</h1>',
     f'<p class="sub">빨라고양 첫 과정 · 26.11.09 Claude 초안 · {len(d)}강 · {words}낱말(강마다 전체 무작위 복습이 더 붙는다)</p>',
     '<p class="about">낱말 소리를 듣고 철자를 친다(PRINCIPLES 0-1 9번). 문제 칸에는 🔊 단추와 한국어 뜻, 글자 수만큼의 칸이 보인다. '
     '맞히거나 따라쓰기를 마치면 발음기호, 그 카드의 철자 규칙 한 줄, 발음 설명(판정 넷)이 나온다.</p>',
     '<details class="rules" open><summary>봐 줄 것</summary><ul>'
     '<li><b>낱말과 뜻.</b> 모두 Claude가 골랐다. 기초 낱말이면서 그 강의 소리·철자 규칙이 드러나는 말로 골랐다. 빼거나 바꿀 말은 그 줄에 댓글로.</li>'
     '<li><b>뜻을 같이 보이는 것.</b> casa 집 / caza 사냥, hola 안녕 / ola 파도처럼 소리가 같은 말을 뜻으로 가른다. 기초 낱말도 함께 익힌다.</li>'
     '<li><b>악센트는 ⑤강부터.</b> ①~④강 낱말에는 악센트가 없다. 강세 규칙을 배우기 전에 "악센트가 빠지면 틀림"을 겪지 않게 했다.</li>'
     '<li><b>과정 이름 Sonidos y letras</b>(소리와 글자). 고양공유 원칙대로 스페인어 이름이다. 다른 이름이 좋으면 말해 줘.</li>'
     '</ul></details>',
     '<details class="rules"><summary>화면에서 되는 것</summary><ul>'
     '<li>카드가 뜨면 낱말을 읽는다. 🔊 단추나 Space로 다시 듣는다. 음성은 es-MX → es-US → 그 밖의 스페인어 차례로 고른다.</li>'
     "<li>악센트·ñ·ü: 휴대폰은 길게 누르기나 입력칸 아래 글자 단추, PC는 a' → á, n~ → ñ, u: → ü.</li>"
     '<li>틀리면 고양이가 짚는다. 악센트·ñ·ü만 틀리면 그 자리를, s/z/c·b/v·h·ll/y·j/g·qu/k처럼 소리는 맞는데 글자가 다르면 "소리는 맞다고양!"이라고.</li>'
     '<li>강마다 순서대로 배운 뒤 강 전체를 섞어 한 판 더(五十音과 같다).</li>'
     '</ul></details>']
P.append('<nav class="bands" aria-label="강">' + ''.join(
    f'<a href="#L{L["lesson"]}">{e(L["id"])}<small>{sum(len(x["words"]) for x in L["exercises"] if not x.get("rnd"))}</small></a>' for L in d) + '</nav>')
for L in d:
    P.append(f'<section class="band" id="L{L["lesson"]}"><h2>{e(L["id"])} · {e(L["name"])}</h2>')
    for x in L['exercises']:
        if x.get('rnd'):
            P.append(f'<p class="sub">끝에 「{e(x["title"])}」: 위 낱말을 모두 섞어 한 판.</p>')
            continue
        P.append(f'<h3>{e(x["title"])}<small>{len(x["words"])}낱말</small></h3>')
        for w in x['words']:
            pn = ''
            if w['pn']:
                items = []
                for t in w['pn']:
                    i = t.find(' — ')
                    items.append(f'<li><b>{e(t[:i])}</b> — {e(t[i + 3:])}</li>' if i > 0 else f'<li>{e(t)}</li>')
                pn = f'<details class="pn"><summary>발음 설명 {len(w["pn"])}줄</summary><ul>{"".join(items)}</ul></details>'
            rule = f'<p class="nt"><span class="tag no">철자</span>{e(w["c"])}</p>' if w['c'] else ''
            P.append(f'<div class="it" id="{e(w["id"])}"><div><div class="w" lang="es">{e(w["en"])}</div><div class="ipa">[{e(w["ipa"])}]</div></div>'
                     f'<div><div class="ko">{e(w["ko"])}</div>{rule}{pn}<button type="button" class="cb" hidden>댓글</button></div></div>')
    P.append('</section>')
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
