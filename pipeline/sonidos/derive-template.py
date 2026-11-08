#!/usr/bin/env python3
"""탄고고양 화면 틀에서 빨라고양 화면 틀(template.html)을 한 번 뽑는다. 26.11.09.

원본: esqsoy/tangogoyang 의 pipeline/jlpt/template.html (그 파일의 마지막 고침 2eb7596, 저장소 main 881e403).
탄고고양 틀은 보카고양 마더텅 화면에서 나왔고(탄고고양 derive-template.py), 五十音(글자 과정) 모드가 들어 있어
제2외국어판의 소리·글자 단계에 가장 가깝다. 영신 26.11.09: "탄고고양이랑 보카고양을 최대한 참조한 후에 작업시작".

바꾸는 것(스페인어, palagoyang PRINCIPLES 0-1 3·4·9·11번):
- 저장 키 접두어 tangogoyang- → palagoyang- (같은 esqsoy.github.io의 보카고양·탄고고양 기록과 겹치지 않게)
- 제목: Palabra Goyang, 과정 이름 Sonidos y letras
- JP_MODE="es": 일본어 입력·후리가나·쓰는 순서 코드는 그대로 두되 돌지 않는다
- 스페인어 판정·입력(a' → á, n~ → ñ, 글자 단추)·음성(es-MX → es-US → 그 밖의 스페인어)·받아쓰기(문제 때 소리를 읽는다)
  스크립트 안의 같은 이름 함수(normalize, isCorrect, jpConvertInput…)를 맨 끝에서 다시 정의한다. 함수 선언은 마지막 것이 이긴다.

뽑은 뒤에는 template.html이 원본이다. 다시 돌리면 template.html의 손 고침이 사라진다.
사용: python3 -I pipeline/sonidos/derive-template.py <tangogoyang 저장소>/pipeline/jlpt/template.html [--force]
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE / 'template.html'
args = [a for a in sys.argv[1:] if not a.startswith('--')]
if len(args) != 1:
    sys.exit(__doc__)
if OUT.exists() and '--force' not in sys.argv:
    sys.exit('template.html이 이미 있다. 손 고침을 지우려면 --force')
s = Path(args[0]).read_text(encoding='utf-8')


def rep(old, new, count=1):
    global s
    n = s.count(old)
    assert n == count, (old[:70], n)
    s = s.replace(old, new)


# 저장 키: 같은 주소의 다른 고양 기록과 절대 겹치지 않게(palagoyang PRINCIPLES 0-1 11번)
s = re.sub(r'(["\'`])tangogoyang-', r'\1palagoyang-', s)
assert not re.search(r'(["\'`])tangogoyang-', s)

rep('<title>日本語能力試験 · 単語高陽</title>', '<title>Sonidos y letras · Palabra Goyang</title>')
rep('<h1 lang="ja"><b>単語高陽</b> · 日本語能力試験</h1>', '<h1 lang="es"><b>Palabra Goyang</b> · Sonidos y letras</h1>')
rep('<h2>日本語能力試験 N5–N1</h2>', '<h2 lang="es">Sonidos y letras</h2>')
rep('aria-label="일본어 정답"', 'aria-label="스페인어 정답"')
rep('const SAVED_COURSE="日本語能力試験";', 'const SAVED_COURSE="Sonidos y letras";')
rep("PACE_COURSE==='ksat'?'日本語能力試験 완주'", "PACE_COURSE==='ksat'?'Sonidos y letras 완주'")
# 출처 줄: 이 과정은 바깥 단어 목록을 쓰지 않는다. FÁBULA 때 위키낱말사전·FrequencyWords 줄을 build.py가 넣는다.
old = re.search(r'      <p class="homeCredit" style="font-size:\.72rem;opacity:\.75;">단어 목록: <a href="https://github\.com/evanclan/OpenJLPT".*?<!--KANA_CREDIT--></p>\n', s)
assert old, 'OpenJLPT 출처 줄'
rep(old.group(0), '      <!--ES_CREDIT-->\n')
rep('const JP_MODE=/*__MODE__*/"meaning";', 'const JP_MODE=/*__MODE__*/"es";')
rep('"ja-JP"', '"es-MX"', count=3)

# 五十音과 같이: '같은 뜻 다른 말' 대사를 쓰지 않는다, 공개 칸 읽을 시간은 설명 길이에 맞춘다
rep('if(JP_MODE==="kana")return false; // 五十音에는', 'if(JP_MODE==="kana"||JP_MODE==="es")return false; // 五十音·Sonidos에는')
rep('function mtRevealDelay(w){if(JP_MODE==="kana"&&w){', 'function mtRevealDelay(w){if((JP_MODE==="kana"||JP_MODE==="es")&&w){')
rep("function mtRevealHtml(term,meaning){\n const w=mtCurrentWord();if(!w)return '';\n",
    "function mtRevealHtml(term,meaning){\n const w=mtCurrentWord();if(!w)return '';\n if(JP_MODE===\"es\")return esRevealHtml(w);\n")
rep('    else $("#meaning").textContent=w.meaning;\n', '    else if(JP_MODE==="es")esQuestion(w);\n    else $("#meaning").textContent=w.meaning;\n')
rep('    if(!opt.timeout&&isSynonymMiss(typed,w))wline=pick(SYNLINES).replace("{w}",typed.trim());\n',
    '    if(!opt.timeout&&isSynonymMiss(typed,w))wline=pick(SYNLINES).replace("{w}",typed.trim());\n'
    '    if(!opt.timeout&&JP_MODE==="es"){const el=esWrongLine(typed,w.term);if(el)wline=el;}\n')

CSS = r'''
/* ===== 빨라고양 Sonidos y letras (26.11.09) ===== */
.es-q{display:flex;align-items:center;justify-content:center;gap:12px;flex-wrap:wrap;}
.es-say{display:inline-flex;align-items:center;justify-content:center;width:48px;height:48px;flex:0 0 auto;border-radius:50%;
  border:2px solid var(--pink2);background:rgba(255,79,163,.14);color:var(--ink);cursor:pointer;padding:0;touch-action:manipulation;}
.es-say .spk{width:24px;height:24px;}
.es-say:active{transform:scale(.94);}
.es-mute{display:block;width:100%;margin-top:4px;font-size:.62em;font-weight:700;color:var(--muted);}
.es-keys{display:flex;justify-content:center;gap:6px;flex-wrap:wrap;margin:10px 0 2px;}
.es-key{min-width:42px;height:42px;padding:0 8px;border-radius:10px;border:1.5px solid var(--line);background:var(--panel2);color:var(--ink);
  font:inherit;font-size:1.2rem;font-weight:800;cursor:pointer;-webkit-user-select:none;user-select:none;touch-action:manipulation;}
.es-key:active{background:rgba(255,79,163,.26);border-color:var(--pink2);}
.es-ipa{font-size:1.4rem;}
'''
rep('</style>\n</head>', CSS + '</style>\n</head>')

KEYS = ('        <div class="es-keys" id="esKeys" role="group" aria-label="스페인어 글자 넣기">'
        + ''.join(f'<button type="button" class="es-key" data-c="{c}" tabindex="-1">{c}</button>' for c in 'áéíóúüñ')
        + '</div>\n')
rep('        <div id="mHint" hidden></div>', KEYS + '        <div id="mHint" hidden></div>')

JS = r'''
/* ===== 빨라고양 스페인어 (26.11.09, palagoyang PRINCIPLES 0-1 3·4·9번) =====
   이 아래 함수들은 위의 같은 이름 함수(일본어)를 덮는다. 스크립트 안 함수 선언은 마지막 것이 이긴다.
   위쪽 코드가 이 함수들을 먼저 부를 수 있으니(GLOSS가 normalize를 부른다) 여기서 쓰는 값은 함수 안에 둔다. */

/* 판정(4번): 대소문자는 가리지 않는다. 악센트·ñ·ü는 철자다(tú 너 / tu 너의). ¿ ¡ 문장부호는 빈칸에 들지 않는다. */
function normalize(v){return String(v||"").normalize("NFC").replace(/[\s¿¡?!.,;:'"´`«»()\-‐–—]/g,"").toLowerCase();}
function esBare(v){return normalize(v).normalize("NFD").replace(/[̀-ͯ]/g,"").normalize("NFC");}
function isCorrect(inp,ans){const g=normalize(inp);if(!g)return false;if(g===normalize(ans))return true;
  const w=jpCardFor(ans);return !!(w&&(w.alt||[]).some(a=>normalize(a)===g));}
function isSpellingVariant(){return false;}
/* 입력(4번): 영어 자판으로 친다. PC는 a' → á, u: → ü, n~ → ñ. 휴대폰은 길게 누르기나 아래 글자 단추. */
function jpConvertInput(){
  const el=document.getElementById("ainput");if(!el||state.composing)return;
  const v=el.value;if(!/['´`:"¨~]/.test(v))return;
  const acc={a:"á",e:"é",i:"í",o:"ó",u:"ú",A:"Á",E:"É",I:"Í",O:"Ó",U:"Ú"};
  const next=v.replace(/([aeiouAEIOU])['´`]/g,(m,c)=>acc[c]).replace(/([uU])[:"¨]/g,(m,c)=>c==="u"?"ü":"Ü").replace(/([nN])~|~([nN])/g,(m,a,b)=>((a||b)==="n"?"ñ":"Ñ"));
  if(next!==v){const fromEnd=Math.max(0,v.length-(el.selectionEnd??v.length));el.value=next;try{const n=Math.max(0,next.length-fromEnd);el.setSelectionRange(n,n);}catch(e){}}
}
/* 칸을 다 채워도 끝 글자가 모음이면 바로 판정하지 않는다: café를 cafe까지 친 뒤 '를 칠 수 있게. 맞으면 바로 받는다. */
function jpPending(v){return /[aeiouAEIOU]$/.test(v||"");}
function jpTentative(raw){return raw;}
/* 받아쓰기라 들을 시간을 더 준다 */
function limitFor(term){const n=[...String(term||"")].filter(c=>/\p{L}/u.test(c)).length;return Math.min(45,Math.max(16,Math.round(10+n*2.6)));}

/* 음성(3번): es-MX → es-US → 그 밖의 중남미 → 에스파냐 차례. */
function pronunciationVoiceScore(v){
  const name=v.name||"",lang=(v.lang||"").replace(/_/g,"-");
  if(!/^es(?:-|$)/i.test(lang))return -1;
  let score=/^es-MX/i.test(lang)?50:/^es-US/i.test(lang)?45:/^es-419/i.test(lang)?44:/^es-(AR|BO|CL|CO|CR|CU|DO|EC|GT|HN|NI|PA|PE|PR|PY|SV|UY|VE)/i.test(lang)?30:/^es-ES/i.test(lang)?15:20;
  const preferred=["Paulina","Angélica","Google español de Estados Unidos","Microsoft Dalia","Microsoft Sabina","Juan","Microsoft Jorge","Microsoft Raul"];
  const i=preferred.findIndex(n=>name.indexOf(n)>=0);if(i>=0)score+=30-i*2;
  if(/compact|eloquence|novelty|Albert|Bells|Boing|Bubbles|Cellos|Jester|Junior|Organ|Ralph|Superstar|Trinoids|Whisper|Wobble|Zarvox|Grandma|Grandpa|Abuel|Rocko|Shelley|Sandy|Flo\b|Reed|Eddy/i.test(name))score-=40;
  if(v.localService)score+=6;return score;
}
function pickPronunciationVoice(){try{
  const es=(window.speechSynthesis.getVoices()||[]).filter(v=>pronunciationVoiceScore(v)>=0);
  if(!es.length)return null;
  if(pronunciationVoiceName){const keep=es.find(v=>v.name===pronunciationVoiceName);if(keep)return keep;}
  let best=null,score=-1;for(const v of es){const x=pronunciationVoiceScore(v);if(x>score){best=v;score=x;}}
  if(best)pronunciationVoiceName=best.name;return best;
}catch(e){return null;}}

/* 받아쓰기(9번): 카드가 뜨면 낱말을 읽고, 한국어 뜻과 칸 수를 보인다. 🔊 단추·Space로 다시 듣는다.
   정답 공개 뒤의 소리·다시 듣기는 원래 코드(speakPronunciation)가 맡는다. */
var esQT=null;
function esQuestion(w){
  const note=state.muted?'<small class="es-mute">소리를 꺼 두면 받아쓸 수 없다고양. 위 ‘무음’을 눌러 켜라고양</small>':!pronunciationSupported()?'<small class="es-mute">이 브라우저는 소리를 못 낸다고양. 사파리·크롬으로 열라고양</small>':'';
  $("#meaning").innerHTML='<span class="es-q"><button type="button" class="es-say" aria-label="소리 다시 듣기" title="다시 듣기 (Space)">'+spkSvg(false)+'</button><span class="es-ko">'+esc(w.meaning)+'</span>'+note+'</span>';
  clearTimeout(esQT);const s=state.session;if(!s)return;
  // 연습 첫 카드는 누른 그 자리에서 읽는다(아이폰은 사람이 누른 때에만 소리를 연다).
  // 그다음 카드는 조금 뒤에: 앞 카드 소리를 끊은 바로 뒤에 읽으면 사파리가 새 소리를 씹는다.
  if(!s.esSpoke){s.esSpoke=true;esSpeakQuestion();}else esQT=setTimeout(esSpeakQuestion,260);
}
function esSpeakQuestion(){
  const s=state.session;if(!s||s.currentId===null||state.muted||!pronunciationSupported()||!screens.game.classList.contains("active"))return;
  const id=s.currentId,w=s.words[id];
  if(s.answered){speakPronunciation(w.term,w.meaning);return;}
  stopPronunciation(false);const seq=pronunciationSeq;
  const live=()=>seq===pronunciationSeq&&state.session===s&&s.currentId===id&&!s.answered&&!state.muted&&screens.game.classList.contains("active");
  try{if(window.speechSynthesis.speaking||window.speechSynthesis.pending)window.speechSynthesis.cancel();}catch(e){}
  const say=()=>{if(!live())return;try{const u=new window.SpeechSynthesisUtterance(w.term);u.lang=pronunciationVoice?.lang||"es-MX";u.rate=.85;if(pronunciationVoice)u.voice=pronunciationVoice;window.speechSynthesis.speak(u);}catch(e){}};
  pronunciationVoice=pickPronunciationVoice();if(pronunciationVoice){say();return;}
  try{const p=new window.SpeechSynthesisUtterance(" ");p.lang="es-MX";p.volume=0;window.speechSynthesis.speak(p);}catch(e){}
  let tries=0;clearInterval(pronunciationWait);pronunciationWait=setInterval(()=>{
    if(!live()){clearInterval(pronunciationWait);pronunciationWait=null;return;}
    pronunciationVoice=pickPronunciationVoice();
    if(pronunciationVoice||++tries>=12){clearInterval(pronunciationWait);pronunciationWait=null;say();}
  },100);
}
document.addEventListener("click",e=>{const b=e.target.closest&&e.target.closest(".es-say");if(!b)return;e.preventDefault();esSpeakQuestion();focusAnswerInput();});
$("#ainput").addEventListener("keydown",e=>{if(composingKey(e)||e.repeat)return;
  if((e.key===" "||e.code==="Space")&&answerInputActive()){e.preventDefault();e.stopPropagation();esSpeakQuestion();}});

/* 글자 단추(4번): 누른 자리에 넣는다. 입력칸 초점을 잃지 않게 누르는 순간 처리한다(휴대폰 자판이 내려가지 않게). */
function esInsert(c){const el=$("#ainput");if(!el||el.disabled||!answerInputActive())return;
  const a=el.selectionStart??el.value.length,b=el.selectionEnd??el.value.length;
  try{el.setRangeText(c,a,b,"end");}catch(e){el.value+=c;}
  el.dispatchEvent(new Event("input",{bubbles:true}));focusAnswerInput();}
(function(){const bar=document.getElementById("esKeys");if(!bar)return;
  const hit=e=>{const b=e.target.closest&&e.target.closest(".es-key");return b&&bar.contains(b)?b:null;};
  bar.addEventListener("touchstart",e=>{const b=hit(e);if(!b)return;e.preventDefault();esInsert(b.dataset.c);},{passive:false});
  bar.addEventListener("mousedown",e=>{const b=hit(e);if(!b)return;e.preventDefault();esInsert(b.dataset.c);});
  bar.addEventListener("click",e=>{const b=hit(e);if(b&&e.detail===0)esInsert(b.dataset.c);});
})();

/* 오답 대사(4번): 악센트·ñ·ü만 틀렸으면 그 자리를, 소리는 맞는데 글자가 다르면(s/z/c, b/v, h, ll/y, j/g, qu/k) 그렇다고 짚는다. */
function esSoundKey(v){return esBare(v).replace(/ch/g,"C").replace(/h/g,"").replace(/ll/g,"y").replace(/y$/,"i").replace(/v/g,"b")
  .replace(/z/g,"s").replace(/c(?=[ei])/g,"s").replace(/qu(?=[ei])/g,"k").replace(/gu(?=[ei])/g,"G").replace(/g(?=[ei])/g,"j")
  .replace(/c/g,"k").replace(/G/g,"g").replace(/rr/g,"R").replace(/^r/,"R").replace(/([nls])r/g,"$1R").replace(/C/g,"ch");}
function esWrongLine(typed,term){
  const t=[...normalize(typed)],a=[...normalize(term)];if(!t.length)return null;
  if(t.length===a.length&&esBare(t.join(""))===esBare(a.join(""))){
    const i=a.findIndex((c,k)=>c!==t[k]),c=a[i]||"";
    if(c==="ñ")return "n이 아니라 ñ라고양! ñ는 다른 글자라고양 ✦";
    if(c==="ü")return "ü 점 두 개까지가 철자라고양! 그래야 u를 읽는다고양 ✦";
    if(/[áéíóú]/.test(c))return "악센트까지가 철자라고양! ‘"+c+"’ 자리를 봐라고양 ✦";
    return "악센트는 거기 찍는 게 아니라고양 ✦";
  }
  if(esSoundKey(t.join(""))===esSoundKey(a.join("")))return "소리는 맞다고양! 근데 글자는 ‘"+term+"’ 이렇게 쓴다고양 ✦";
  return null;
}

/* 정답 공개(9번): 발음기호, 이 카드의 철자 규칙 한 줄, 발음 설명(판정 넷). 뜻은 문제 칸에 그대로 있다. */
function esRevealHtml(w){
  const ipa=w.ipa?'<div class="jp-ipa es-ipa">['+esc(w.ipa)+']</div>':'';
  const note=w.note?'<div class="ov-tr jp-note">'+esc(w.note)+'</div>':'';
  const pn=w.pn&&w.pn.length?'<ul class="jp-pn">'+w.pn.map(x=>{const i=x.indexOf(' — ');return '<li>'+(i>0?'<b>'+esc(x.slice(0,i))+'</b><br>'+esc(x.slice(i+3)).replace(' · 주의: ','<br><i>주의</i> ').replace(/^주의: /,'<i>주의</i> ').replace(/^차이: /,'<i>차이</i> '):esc(x))+'</li>';}).join('')+'</ul>':'';
  return ipa+note+pn;
}
'''
i = s.rfind('\n</script>')
assert i > 0
s = s[:i] + JS + s[i:]
OUT.write_text(s, encoding='utf-8')
print(OUT, len(s))
