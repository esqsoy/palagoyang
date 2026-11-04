# 고양공유 작업 기록

의미 있는 작업과 영신 결정을 날짜별로 더한다. 현재 상태는 [HANDOFF.md](HANDOFF.md). 26.11.03까지의 기록은 [tangogoyang WORK_LOG](https://github.com/esqsoy/tangogoyang/blob/main/WORK_LOG.md)의 고양공유 절들(원장 0.1 → 0.2 Threshold·Vantage·JF 대조 → 0.3 PCIC 대조 → PCIC 자료를 빨라고양용으로 남김).

## 2026-11-04 · 고양공유를 palagoyang으로 옮김

- **결정(영신):** 방금 만든 palagoyang(스페인어판, 당장은 고양공통용)에 공통 작업을 두고, 공개가 문제되는 자료는 맥미니 지정 폴더를 쓴다. palagoyang은 공개 저장소, tangogoyang의 공통 원장은 옮겨도 된다.
- **한 일:** tangogoyang `goyang-common/`(README·expressions.json·source-check-20261103.json·review-page.py·spanish-pcic-sources.md, tangogoyang `91d5ce8` 기준)을 그대로 옮김. README의 PRINCIPLES 상대 링크를 tangogoyang 절대 주소로 바꾸고 옮긴 경위를 적음. 저장소 README·AGENTS·HANDOFF·WORK_LOG·.gitignore를 새로 씀. tangogoyang `goyang-common/`은 이 저장소를 가리키는 안내만 남김.
- **검증:** 옮긴 원장 JSON을 다시 읽어 258항목·id 중복 없음 확인, review-page.py가 새 위치에서 페이지를 만드는지 확인.
- **남은 일:** HANDOFF '열린 질문'.

## 2026-11-04 · 맥미니로 작업 자리를 옮김

- **결정(영신):** 클라우드 세션 대신 늘 켜 두는 맥미니에서 작업한다. 고양 작업은 맥미니 iCloud Drive `10 언어/고양/`에 둔다("저기가 안전해"). 맥미니 지정 폴더는 그 안의 `비공개/`.
- **한 일:**
  - palagoyang을 `10 언어/고양/palagoyang/`에 받음.
  - `10 언어/고양/비공개/`를 만들고, PCIC 5·6장 목록 6쪽과 소개 2쪽을 Internet Archive 보관본에서 원래 HTML 그대로 받아 `pcic/`에 둠. 출처는 그 폴더 README에 적음.
  - GitHub CLI 2.103.3을 공식 릴리스에서 받아 체크섬을 확인하고 `~/.local/bin/gh`에 깜. 이 저장소의 커밋 작성자를 `esqsoy` noreply 주소로 설정.
  - HANDOFF('작업 환경' 절 새로 둠, 열린 질문에서 맥미니 폴더 위치 뺌)·AGENTS·goyang-common README·spanish-pcic-sources에 위치를 적음.
  - 맥미니 git은 Xcode 라이선스를 수락해야 돌아간다(영신이 `sudo xcodebuild -license accept` 실행).
- **검증:** 8쪽 모두 HTTP 200. gzip을 풀어 UTF-8 HTML임을 확인. 제목이 PCIC 5·6장의 해당 쪽이고, 끝(`</html>`)까지 들어옴.
- **남은 일:** HANDOFF '열린 질문'. Google Drive 폴더를 둘지는 영신이 정한다.

## 2026-11-04 · 기능×수준 사다리 칸 수 초안

- **요청(영신):** "표 만들어 줘". 공통 원장을 사다리로 키울지 정하기 전에, PCIC 수준 분포로 항목마다 몇 칸을 둘지 표부터.
- **한 일:**
  - `goyang-common/ladder.py`를 새로 씀. 맥미니 지정 폴더의 PCIC 5·6장 목록 6쪽에서 기능·전술 번호별로 어느 수준에 표현 꼴이 있는지만 읽는다. 대조표(source-check)의 대응을 거쳐 원장 항목마다 A·B·C 칸을 정한다.
  - 결과를 `ladder-draft-20261104.json`(번호·수준 유무·칸 수만, PCIC 본문 없음)으로 냄. 검토 페이지 https://claude.ai/artifact/5v9b3inZWWQU1jvLEVigMb (comments)를 올림.
  - HANDOFF 열린 질문에 결과와 정할 것을 적음.
- **결과:** 추천 570문장(258 + 새로 312), 대안(지금 수준부터) 516문장. 3칸 144항목, 2칸 24, 1칸 90. PCIC 근거 없는 항목 89(T 45, F4 12, F6 12 등).
  - PCIC 5장 실측: 기능 표 140개. 수준별로 꼴이 있는 기능 수는 A1 53, A2 91, B1 125, B2 128, C1 126, C2 120(840칸 중 643칸).
- **검증:** 스크래치 계산과 저장소 스크립트의 합계가 같음(570/516).
  - 표본 항목(F1-06·F2-22·C-01·C-23·F6-01·T-01)의 PCIC 번호와 수준을 원문 표와 대조함.
  - F6 대부분이 근거 없음으로 나오는 것은 PCIC 5·6장에 해당 기능이 없어서임을 대조표에서 확인함(F6은 Threshold 6·12장 출처).
  - 페이지를 올린 뒤 화면은 보지 못함(내장 브라우저가 claude.ai에 로그인 안 됨).
- **어림과 한계:**
  - 표가 따로 없는 PCIC 5장 하위 항목 25개는 부모 기능의 수준을 썼다. 6장 2.2는 빈 표라 3.1의 수준을 썼다.
  - 6장 상위 번호(2·3)에 걸린 항목은 하위 전체의 수준을 합쳐서, 칸이 넉넉하게 잡혔을 수 있다.
- **남은 일:** 영신 검토. 정해지면 규칙을 고쳐 다시 셈 → 원장 짜임에 칸을 넣는 방식은 그때 영신에게 의견을 낸다.
