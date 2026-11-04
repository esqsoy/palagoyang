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
