#!/usr/bin/env python3
"""공통 원장에 PCIC 수준 분포를 얹어 '기능×수준 사다리' 칸 수 초안을 낸다.

사용: python3 -I goyang-common/ladder.py [--pcic <PCIC 폴더>] [--out <html>]
  --pcic 기본값: 저장소 옆 맥미니 지정 폴더 ../비공개/pcic (원문은 이 저장소에 없다)
  결과: goyang-common/ladder-draft-20261104.json (칸 초안, 숫자와 번호만) + 영신 검토 페이지 HTML
  페이지는 항목마다 한 블록이라 댓글이 그 항목에 붙는다. 올릴 때 capabilities: {comments: {}}.

PCIC 원문(보기 표현)은 읽기만 하고 옮기지 않는다. JSON과 페이지에는 기능 번호, 수준별 유무, 칸 수만 적는다.
"""
import html
import json
import re
import sys
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
LEVELS = ["a1", "a2", "b1", "b2", "c1", "c2"]
BAND = {"a1": "A", "a2": "A", "b1": "B", "b2": "B", "c1": "C", "c2": "C"}
BANDS = "ABC"
OWN = {"A1": "A", "A2": "A", "B1": "B", "B2": "B", "C1": "C"}
BAND_LABEL = {"A": "A1~A2 기본꼴", "B": "B1~B2", "C": "C1 다듬은 꼴"}
OUT_JSON = HERE / "ladder-draft-20261104.json"

# 영신 결정(26.11.06 "추천대로 해"): PCIC 규칙으로 낸 칸을 항목별로 고친다
_B12 = "1.2 정보 묻기 묶음: B·C 칸은 대표(어디·이유·방법)에만"
_B13 = "1.3 정보 주기 묶음: B·C 칸은 대표(하는 일)에만"
OWN_ONLY = {**{i: _B12 for i in ["F1-06", "F1-08", "F1-09", "F1-10", "F1-11", "F1-12"]},
            **{i: _B13 for i in ["F1-01", "F1-02", "F1-03", "F1-05"]}}
REPRESENTATIVE = {**{i: "1.2 정보 묻기 묶음 대표" for i in ["F1-07", "F1-13", "F1-14"]},
                  "F1-04": "1.3 정보 주기 묶음 대표"}
ADD = {i: ["B"] for i in ["F6-01", "F6-02", "F6-04", "F6-08", "F6-11", "F6-13"]}
ADD_NOTE = "말이 막혔을 때: B 칸 더함(PCIC 5·6장에 없는 기능)"


def numkey(no):
    return [int(x) for x in no.split(".")]


def lvl_of(attr):
    m = re.search(r"(a1|a2|b1|b2|c1|c2)$", attr or "")
    return m.group(1) if m else None


class Funciones(HTMLParser):
    """5장: 기능마다 표 하나, 수준마다 칸 하나. 칸의 최상위 li = 표현 꼴 하나."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.funcs, self.cur, self.cap, self.in_cap = [], None, "", False
        self.lvl, self.ul, self.depth = None, 0, 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "table":
            self.depth += 1
            if self.depth == 1:
                self.cur, self.cap = {}, ""
        elif tag == "caption" and self.cur is not None:
            self.in_cap = True
        elif tag == "td" and self.cur is not None:
            self.lvl, self.ul = lvl_of(a.get("headers")), 0
            if self.lvl:
                self.cur.setdefault(self.lvl, 0)
        elif tag == "ul" and self.lvl:
            self.ul += 1
        elif tag == "li" and self.lvl and self.ul == 1:
            self.cur[self.lvl] += 1

    def handle_endtag(self, tag):
        if tag == "table":
            if self.depth == 1 and self.cur is not None:
                m = re.match(r"\s*([\d.]+?)\.?\s+(.*)", self.cap.strip())
                if m:
                    self.funcs.append((m.group(1).rstrip("."), self.cur))
                self.cur = None
            self.depth -= 1
        elif tag == "caption":
            self.in_cap = False
        elif tag == "td":
            self.lvl = None
        elif tag == "ul" and self.lvl:
            self.ul -= 1

    def handle_data(self, d):
        if self.in_cap:
            self.cap += d


class Tacticas(HTMLParser):
    """6장: 갈래마다 표 하나, 하위 번호는 수준 칸 안의 소제목(id 끝이 수준)."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.present = defaultdict(set)
        self.cap, self.in_cap, self.lvl, self.li, self.h, self.ht = None, False, None, 0, None, ""

    def mark(self, no, lvl):
        no = no.strip().rstrip(".")
        if re.fullmatch(r"\d+(\.\d+)*", no):
            self.present[no].add(lvl)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "caption":
            self.in_cap, self.cap = True, ""
        elif tag == "td":
            self.lvl, self.li = lvl_of(a.get("headers")), 0
        elif tag == "li" and self.lvl:
            self.li += 1
        elif tag in ("h3", "h4", "h5"):
            self.h, self.ht = lvl_of(a.get("id")), ""

    def handle_endtag(self, tag):
        if tag == "caption":
            self.in_cap = False
        elif tag == "td":
            if self.lvl and self.li and self.cap and "[-]" not in self.cap:
                m = re.match(r"\s*([\d.]+)", self.cap)
                if m:
                    self.mark(m.group(1), self.lvl)
            self.lvl = None
        elif tag in ("h3", "h4", "h5") and self.h:
            m = re.match(r"\s*([\d.]+)", self.ht)
            if m:
                self.mark(m.group(1), self.h)
            self.h = None

    def handle_data(self, d):
        if self.in_cap:
            self.cap += d
        if self.h:
            self.ht += d


def read_pcic(folder):
    f5 = {}
    t6 = defaultdict(set)
    for band in ["a1-a2", "b1-b2", "c1-c2"]:
        p = Funciones()
        p.feed((folder / f"05_funciones_inventario_{band}.htm").read_text(encoding="utf-8"))
        for no, cells in p.funcs:
            f5.setdefault(no, {l: 0 for l in LEVELS}).update(cells)
        q = Tacticas()
        q.feed((folder / f"06_tacticas_pragmaticas_inventario_{band}.htm").read_text(encoding="utf-8"))
        for no, s in q.present.items():
            t6[no] |= s
    # 6장 2.2(누그러뜨리기)는 빈 표에 'v. 3.1'만 있다 → 3.1의 수준을 쓴다
    t6["2.2"] = set(t6["3.1"])
    return f5, t6


def build(f5, t6):
    led = json.loads((HERE / "expressions.json").read_text())
    sc = json.loads((HERE / "source-check-20261103.json").read_text())

    def f5_levels(no):  # 표가 없는 하위 항목(1.2.1 등)은 부모 표의 수준
        r = f5.get(no) or f5.get(no.rsplit(".", 1)[0])
        return {l for l in LEVELS if r and r[l] > 0}

    def t6_levels(no):  # 상위 번호(2, 3 등)는 하위 전체
        s = set(t6.get(no, ()))
        for k, v in t6.items():
            if k.startswith(no + "."):
                s |= v
        return s

    refs = defaultdict(list)
    share = Counter()
    for f in sc["pcic_functions"]:
        for i in f["ledger"]:
            refs[i].append(("5", f["no"]))
            share[f["no"]] += 1
    for f in sc["pcic_tactics"]:
        for i in f["ledger"]:
            refs[i].append(("6", f["no"]))

    rows = []
    for it in led["items"]:
        lv, used = set(), []
        for ch, no in refs.get(it["id"], []):
            s = f5_levels(no) if ch == "5" else t6_levels(no)
            if s:
                lv |= s
                used.append(f"{ch}-{no}")
        own = OWN[it["level"]]
        bands = {BAND[l] for l in lv}
        rec = sorted(bands | {own}, key=BANDS.index)
        alt = [b for b in rec if BANDS.index(b) >= BANDS.index(own)]
        final, note = rec, REPRESENTATIVE.get(it["id"])
        if it["id"] in OWN_ONLY:
            final, note = [own], OWN_ONLY[it["id"]]
        if it["id"] in ADD:
            final, note = sorted(set(rec) | set(ADD[it["id"]]), key=BANDS.index), ADD_NOTE
        row = {
            "id": it["id"], "group": it["group"], "level": it["level"], "task": it["task"], "ko": it["ko"],
            "pcic": used, "pcic_levels": [l for l in LEVELS if l in lv], "own": own,
            "rungs": final, "rungs_pcic": rec, "rungs_from_own": alt,
        }
        if note:
            row["decision"] = note
        rows.append(row)

    levels_stat = {l: {"functions": sum(1 for r in f5.values() if r[l] > 0), "forms": sum(r[l] for r in f5.values())} for l in LEVELS}
    big = []
    for no, n in share.most_common():
        if n < 3:
            break
        f = next(x for x in sc["pcic_functions"] if x["no"] == no)
        big.append({"no": no, "heading": f["heading"], "items": f["ledger"]})
    return led, rows, levels_stat, big, len(f5)


def write_json(led, rows, levels_stat, big, n_func):
    doc = {
        "title": "공통 원장 기능×수준 사다리 칸 초안",
        "date": "2026-11-04",
        "ledger_version": led["version"],
        "status": "칸 수 확정(영신 26.11.06): 낮은 칸도 두고, 묶음 1.2·1.3은 B·C 칸을 대표에만, F6 6항목에 B 칸. 문장은 아직 없다.",
        "bands": BAND_LABEL,
        "rule": [
            "칸은 A(A1~A2 기본꼴)·B(B1~B2)·C(C1 다듬은 꼴) 셋. PCIC의 C2는 C에 합친다(원장은 C1까지).",
            "rungs_pcic: PCIC가 그 기능에 표현 꼴을 둔 띠마다 한 칸 + 지금 문장의 띠. 지금 수준보다 낮은 띠도 둔다(영신 26.11.06).",
            "rungs(확정): rungs_pcic에 영신 결정(26.11.06)을 얹은 것. 고친 항목은 decision에 까닭을 적었다.",
            "  - 묶음 1.2 정보 묻기(9항목): B·C 칸은 대표 F1-07·F1-13·F1-14에만. 묶음 1.3 정보 주기(5항목): 대표 F1-04에만. 4.7·5.17 묶음은 항목마다 행동·상황이 달라 그대로.",
            "  - F6 말이 막혔을 때: F6-01·02·04·08·11·13에 B 칸을 더함. C 수준 고쳐 말하기·끼어들기는 C 갈래가 맡는다.",
            "rungs_from_own(채택 안 함, 비교용): PCIC 규칙에서 지금 수준보다 낮은 띠는 뺀 것.",
            "PCIC 근거가 없는 항목은 지금 문장 한 칸.",
            "표가 따로 없는 PCIC 5장 하위 항목(1.2.1 등)은 부모 기능의 수준, 6장 2.2는 3.1의 수준을 썼다.",
        ],
        "pcic_levels": {"functions_with_tables": n_func, "per_level": levels_stat},
        "shared_functions": big,
        "totals": {"rungs": sum(len(r["rungs"]) for r in rows), "rungs_pcic": sum(len(r["rungs_pcic"]) for r in rows),
                   "rungs_from_own": sum(len(r["rungs_from_own"]) for r in rows)},
        "items": rows,
    }
    OUT_JSON.write_text(json.dumps(doc, ensure_ascii=False, indent=1) + "\n")
    return doc


CSS = """
/* 사다리 표: 위에 합계와 규칙, 아래는 원장 갈래별 한 줄 한 항목. 검수 페이지(review-page.py)와 같은 색과 글꼴 */
:root{--bg:#f6f7f4;--fg:#1d2420;--mute:#5d6a62;--line:#d7ddd6;--card:#ffffff;--accent:#2f6b4f;--accent2:#b7d6c4;--warn:#9a5b12;--warnbg:#fbf1e2;--cell:#e6ebe5;
--display:"Gowun Batang",Georgia,serif;--body:"Pretendard","Apple SD Gothic Neo","Noto Sans KR",system-ui,sans-serif;--mono:ui-monospace,"SF Mono",Menlo,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#151a17;--fg:#e4ebe6;--mute:#9aa8a0;--line:#2c352f;--card:#1c2320;--accent:#7cc4a0;--accent2:#2f5a45;--warn:#e3b46e;--warnbg:#2b2418;--cell:#25302a;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#151a17;--fg:#e4ebe6;--mute:#9aa8a0;--line:#2c352f;--card:#1c2320;--accent:#7cc4a0;--accent2:#2f5a45;--warn:#e3b46e;--warnbg:#2b2418;--cell:#25302a;color-scheme:dark}
body{background:var(--bg);color:var(--fg);font-family:var(--body);line-height:1.55}
.wrap{max-width:860px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 64px}
h1{font-family:var(--display);font-size:1.7rem;margin:0 0 6px;text-wrap:balance}
h2{font-family:var(--display);font-size:1.2rem;margin:34px 0 8px;padding-bottom:6px;border-bottom:1px solid var(--line);text-wrap:balance}
h2 small{font-family:var(--body);color:var(--mute);font-size:.8rem;font-weight:400;margin-left:6px}
.lead{color:var(--mute);margin:0 0 14px;font-size:.95rem;max-width:68ch}
.nums{display:flex;flex-wrap:wrap;gap:10px 28px;margin:18px 0 8px}
.nums div{display:flex;flex-direction:column}
.nums b{font-family:var(--display);font-size:2rem;line-height:1.1;font-variant-numeric:tabular-nums}
.nums span{font-size:.82rem;color:var(--mute)}
.tbl{overflow-x:auto;margin:10px 0 4px}
table{border-collapse:collapse;font-size:.88rem;font-variant-numeric:tabular-nums;min-width:100%}
th,td{padding:6px 10px;border-bottom:1px solid var(--line);text-align:right;white-space:nowrap}
th:first-child,td:first-child{text-align:left}
th{font-weight:600;color:var(--mute);font-size:.8rem}
tfoot td{font-weight:700;border-bottom:none}
ol.rules{padding-left:1.3em;margin:8px 0;max-width:68ch}
ol.rules li{margin:4px 0}
.ask{border:1px solid var(--line);background:var(--card);border-radius:8px;padding:12px 14px;margin:10px 0;max-width:68ch}
.ask b{display:block;margin-bottom:2px}
.ask p{margin:4px 0;font-size:.92rem}
.ask.done{background:transparent;border-style:dashed}
.ask .tag{display:inline-block;margin-left:6px;font-size:.75rem;font-weight:600;color:var(--accent);border:1px solid var(--accent);border-radius:4px;padding:0 6px;vertical-align:middle}
.bars{display:grid;grid-template-columns:2.4em 1fr auto;gap:5px 10px;align-items:center;max-width:520px;margin:10px 0;font-size:.82rem;font-variant-numeric:tabular-nums}
.bars .lab{font-family:var(--mono);color:var(--mute)}
.bars .bar{height:12px;background:var(--cell);border-radius:2px;position:relative}
.bars .bar i{position:absolute;inset:0 auto 0 0;background:var(--accent);border-radius:2px}
.bars .val{color:var(--mute)}
.legend{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:.82rem;color:var(--mute);margin:8px 0 0}
.legend span{display:inline-flex;align-items:center;gap:5px}
.row{display:grid;grid-template-columns:58px 30px minmax(0,1fr) auto auto 26px;gap:4px 12px;align-items:center;padding:8px 4px;border-bottom:1px dashed var(--line)}
.id{font-family:var(--mono);font-size:.76rem;color:var(--mute)}
.lv{font-family:var(--mono);font-size:.74rem;color:var(--accent);font-weight:600}
.task{font-size:.8rem;color:var(--mute)}
.ko{font-size:1rem}
.refs{font-family:var(--mono);font-size:.7rem;color:var(--mute);overflow-wrap:anywhere}
.none{font-size:.72rem;color:var(--warn);background:var(--warnbg);border-radius:4px;padding:0 5px}
.strip{display:grid;grid-template-columns:repeat(6,10px);gap:2px}
.strip i{height:14px;background:var(--cell);border-radius:1px}
.strip i.on{background:var(--accent2)}
.strip i:nth-child(2n){margin-right:3px}
.rungs{display:flex;gap:3px}
.rung{width:22px;height:22px;display:grid;place-items:center;font-family:var(--mono);font-size:.72rem;font-weight:700;border-radius:4px;border:1.5px solid transparent;color:var(--mute)}
.rung.own{background:var(--accent);color:var(--bg)}
.rung.up{border-color:var(--accent);color:var(--accent)}
.rung.down{border-color:var(--accent);border-style:dashed;color:var(--accent)}
.rung.off{color:var(--line)}
.rung.cut{color:var(--mute);border-color:var(--line);text-decoration:line-through}
.dec{display:inline-block;margin-top:2px;font-size:.72rem;color:var(--accent);border:1px solid var(--accent2);border-radius:4px;padding:0 5px}
.cnt{font-family:var(--display);font-size:1.15rem;text-align:right;font-variant-numeric:tabular-nums}
@media (max-width:560px){.row{grid-template-columns:52px 28px minmax(0,1fr) 26px}.row .strip{grid-column:3}.row .rungs{grid-column:3}.row .cnt{grid-row:1;grid-column:4}}
"""


def render(doc):
    e = html.escape
    rows = doc["items"]
    groups = json.loads((HERE / "expressions.json").read_text())["groups"]
    tot = doc["totals"]
    n_items = len(rows)
    no_ref = sum(1 for r in rows if not r["pcic"])
    P = ['<title>공통 원장 사다리 칸표</title><meta name="claude:viewport-fit-sides" content="cover">',
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Gowun+Batang:wght@700&display=swap">',
         f"<style>{CSS}</style><div class=\"wrap\">",
         "<h1>공통 원장 기능×수준 사다리 칸표</h1>",
         f'<p class="lead">원장 초안 {e(doc["ledger_version"])}의 {n_items}항목마다, 같은 일을 수준별로 몇 번 말하게 할지(칸 수)를 PCIC 5·6장의 수준 분포로 정한 초안입니다. 문장은 아직 없어요. 줄을 눌러 댓글로 칸을 고쳐 주세요(예: “B 칸 빼자”, “C 칸 더”).</p>',
         '<div class="nums">'
         f'<div><b>{tot["rungs"]}</b><span>전체 문장 수</span></div>'
         f'<div><b>{tot["rungs"] - n_items}</b><span>그중 새로 쓸 문장</span></div>'
         f'<div><b>{no_ref}</b><span>PCIC 근거 없는 항목</span></div></div>']

    # 갈래별 합계
    P.append('<div class="tbl"><table><thead><tr><th>갈래</th><th>항목</th><th>PCIC 근거</th><th>1칸</th><th>2칸</th><th>3칸</th><th>문장</th></tr></thead><tbody>')
    for g, name in groups.items():
        rs = [r for r in rows if r["group"] == g]
        c = Counter(len(r["rungs"]) for r in rs)
        P.append(f'<tr><td>{e(g)} {e(name)}</td><td>{len(rs)}</td><td>{sum(1 for r in rs if r["pcic"])}</td>'
                 f'<td>{c[1]}</td><td>{c[2]}</td><td>{c[3]}</td><td>{sum(len(r["rungs"]) for r in rs)}</td></tr>')
    c = Counter(len(r["rungs"]) for r in rows)
    P.append(f'</tbody><tfoot><tr><td>합계</td><td>{n_items}</td><td>{n_items - no_ref}</td><td>{c[1]}</td><td>{c[2]}</td><td>{c[3]}</td><td>{tot["rungs"]}</td></tr></tfoot></table></div>')

    # 규칙
    P.append("<h2>칸을 정한 규칙</h2><ol class=\"rules\">"
             "<li>칸은 셋입니다. <b>A</b> A1~A2 기본꼴, <b>B</b> B1~B2, <b>C</b> C1 다듬은 꼴. PCIC의 C2는 C에 합쳤어요(원장은 C1까지).</li>"
             "<li>PCIC 근거가 있는 항목은 PCIC가 그 기능에 표현 꼴을 둔 띠마다 한 칸, 그리고 지금 문장이 있는 띠는 늘 한 칸입니다.</li>"
             "<li>지금 수준보다 낮은 띠도 PCIC에 있으면 칸을 둡니다(점선 칸). 같은 일을 처음부터 쉽게 말해 보게 하려는 것이에요(영신 26.11.06 결정).</li>"
             "<li>PCIC 근거가 없는 항목(주제 상황, 한국어 쪽 사교 표현 등)은 지금 문장 한 칸 그대로입니다.</li>"
             "<li>영신 결정(26.11.06)으로 고친 항목: 한 기능을 여러 항목이 나눠 쓰는 묶음(1.2 정보 묻기, 1.3 정보 주기)은 B·C 칸을 대표 항목에만 두고, 말이 막혔을 때(F6) 여섯 항목에 B 칸을 더했어요. 줄 아래 초록 글씨가 그 표시입니다.</li>"
             "<li>PCIC 5장에서 표가 따로 없는 하위 항목(1.2.1 등 25개)은 부모 기능의 수준을, 6장 2.2(누그러뜨리기)는 3.1을 보라고만 되어 있어 3.1의 수준을 썼어요.</li></ol>")

    # 정할 것
    big = doc["shared_functions"]
    big_txt = ", ".join(f'{e(b["no"])} {e(b["heading"])} {len(b["items"])}항목' for b in big)
    P.append("<h2>정한 것</h2>"
             '<div class="ask done"><b>1. 낮은 칸을 둘까 <span class="tag">정함 · 둔다</span></b><p>영신 26.11.06. 지금 B1인 항목이라도 PCIC가 A2에 꼴을 두면 A 칸을 만듭니다. 이 칸이 '
             f'{tot["rungs_pcic"] - tot["rungs_from_own"]}문장이에요.</p></div>'
             f'<div class="ask done"><b>2. 한 기능을 여러 항목이 나눠 쓰는 묶음 <span class="tag">정함 · 대표에만</span></b><p>영신 26.11.06. 묶음은 {big_txt}. 정보 묻기는 B·C 칸을 어디·이유·방법에만, 정보 주기는 하는 일에만 둡니다(B·C 꼴이 항목마다 같은 간접 질문·정정이 되어서). 부탁에 답하기(4.7)와 좋은 일 빌기(5.17)는 항목마다 행동·상황이 달라 그대로예요. 20문장 줄었어요.</p></div>'
             f'<div class="ask done"><b>3. 근거 없는 {no_ref}항목 <span class="tag">정함 · F6에 B 칸 6</span></b><p>영신 26.11.06. 대부분 주제 상황(T)이라 수준이 올라가면 문장보다 단어와 문법이 늘어서 한 칸 그대로입니다. 말이 막혔을 때(F6)는 PCIC 5·6장에 해당 기능이 없을 뿐이라, 다시 말해 달라기·천천히·뜻 묻기·말이 막힐 때·못 알아들었다기·에둘러 말하기에 B 칸을 더했어요. C 칸은 C 갈래가 맡습니다.</p></div>')

    # PCIC 분포
    ls = doc["pcic_levels"]["per_level"]
    nf = doc["pcic_levels"]["functions_with_tables"]
    P.append(f'<h2>PCIC 5장 수준 분포<small>기능 표 {nf}개</small></h2>'
             f'<p class="lead">수준마다 표현 꼴이 하나라도 있는 기능의 수입니다. 전체 칸 {nf}×6 = {nf * 6} 가운데 {sum(v["functions"] for v in ls.values())}칸이 차 있어요. 오른쪽 숫자는 그 수준의 표현 꼴 수.</p><div class="bars">')
    for l in LEVELS:
        v = ls[l]
        P.append(f'<span class="lab">{l.upper()}</span><span class="bar"><i style="width:{100 * v["functions"] / nf:.1f}%"></i></span><span class="val">{v["functions"]} · {v["forms"]}</span>')
    P.append("</div>")

    # 범례
    P.append('<div class="legend"><span><span class="strip"><i class="on"></i><i></i><i class="on"></i><i class="on"></i><i></i><i></i></span>PCIC에 꼴이 있는 수준(A1 A2 · B1 B2 · C1 C2)</span>'
             '<span><span class="rung own">A</span>지금 문장</span><span><span class="rung up">B</span>새 칸</span><span><span class="rung down">A</span>새 칸(지금보다 낮음)</span><span><span class="rung cut">C</span>묶음이라 뺀 칸</span></div>')

    for g, name in groups.items():
        rs = [r for r in rows if r["group"] == g]
        P.append(f"<h2>{e(name)}<small>{e(g)} · {len(rs)}항목 · {sum(len(r['rungs']) for r in rs)}문장</small></h2>")
        for r in rs:
            strip = "".join(f'<i class="on" title="{l.upper()}"></i>' if l in r["pcic_levels"] else f'<i title="{l.upper()}"></i>' for l in LEVELS)
            chips = []
            for b in BANDS:
                if b == r["own"]:
                    chips.append(f'<span class="rung own" title="{BAND_LABEL[b]} · 지금 문장">{b}</span>')
                elif b in r["rungs"] and BANDS.index(b) > BANDS.index(r["own"]):
                    chips.append(f'<span class="rung up" title="{BAND_LABEL[b]} · 새 칸">{b}</span>')
                elif b in r["rungs"]:
                    chips.append(f'<span class="rung down" title="{BAND_LABEL[b]} · 새 칸(낮음)">{b}</span>')
                elif b in r["rungs_pcic"]:
                    chips.append(f'<span class="rung cut" title="{BAND_LABEL[b]} · 묶음이라 뺌">{b}</span>')
                else:
                    chips.append(f'<span class="rung off">{b}</span>')
            ref = (f'<div class="refs">PCIC {e(" · ".join(r["pcic"]))}</div>' if r["pcic"]
                   else '<div><span class="none">PCIC 근거 없음</span></div>')
            if r.get("decision"):
                ref += f'<div><span class="dec">{e(r["decision"])}</span></div>'
            P.append(f'<div class="row" id="{e(r["id"])}"><span class="id">{e(r["id"])}</span><span class="lv">{e(r["level"])}</span>'
                     f'<div><div class="task">{e(r["task"])}</div><div class="ko">{e(r["ko"])}</div>{ref}</div>'
                     f'<span class="strip">{strip}</span><span class="rungs">{"".join(chips)}</span><span class="cnt">{len(r["rungs"])}</span></div>')
    P.append("</div>")
    return "\n".join(P)


def main():
    args = sys.argv[1:]
    pcic = Path(args[args.index("--pcic") + 1]) if "--pcic" in args else HERE.parent.parent / "비공개" / "pcic"
    out = Path(args[args.index("--out") + 1]) if "--out" in args else HERE / "out" / "ladder.html"
    f5, t6 = read_pcic(pcic)
    led, rows, levels_stat, big, n_func = build(f5, t6)
    doc = write_json(led, rows, levels_stat, big, n_func)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(doc))
    print(OUT_JSON)
    print(out)
    print("totals", doc["totals"], "functions", n_func)


if __name__ == "__main__":
    main()
