# 고양공유 인수인계

갱신: 2026-11-04. 이 문서는 최신 상태로 교체하고, 경위는 [WORK_LOG.md](WORK_LOG.md)에 남긴다.

## 지금 상태

- **언어불문 필수 표현 원장 초안 0.3** (258항목, [goyang-common/](goyang-common/README.md)). **영신 검수 대기.** 직검수 페이지 https://claude.ai/artifact/TDwB3yZf3sAwqooZS38zXA (0.3, 새 항목에 '0.2 추가'·'0.3 추가' 표시, 줄마다 댓글).
  - 0.1(141항목)을 원문과 대조해 0.2에서 85항목(Threshold 1990·Vantage·JF Can-do), 0.3에서 32항목(PCIC)을 더했다. 네 원문 대조는 끝났다. 대조표는 [source-check-20261103.json](goyang-common/source-check-20261103.json).
  - 각 판은 항목마다 `same`/`counterpart`/`none`을 단다. 원장에 없는 그 언어 고유 표현은 판 고유 원장에 둔다.
- **PCIC 원문은 빨라고양 판 고유 원장용으로 남김**(영신 26.11.03). 주소와 쓰는 법은 [spanish-pcic-sources.md](goyang-common/spanish-pcic-sources.md). 원문 8쪽(5·6장 목록 6쪽, 소개 2쪽)은 26.11.04 맥미니 세션이 Internet Archive에서 다시 받아 아래 비공개 폴더 `pcic/`에 두었다.

## 작업 환경 (26.11.04~)

- 작업은 늘 켜 두는 **맥미니**의 Claude 데스크톱 앱(Code 탭)에서 한다. 클라우드 세션은 쓰지 않는다.
- 저장소: 맥미니 iCloud Drive `10 언어/고양/palagoyang/`(영신 결정, "저기가 안전해").
- **맥미니 지정 폴더**(공개하면 안 되는 자료): 저장소 옆 `10 언어/고양/비공개/`. git 밖이고 어디에도 올리지 않는다. 지금은 `pcic/` 8쪽과 README.
- 맥미니 세션은 web.archive.org에 들어갈 수 있다(26.11.04 확인).
- iCloud 안의 git 저장소다. ` 2`가 붙은 사본처럼 이상한 파일이 `.git` 안에 생기면 손으로 고치지 말고, 커밋 안 된 변경을 빼 둔 뒤 GitHub에서 다시 받는다. 원본은 GitHub다.
- GitHub CLI는 `~/.local/bin/gh`(PATH에 없음, 전체 경로로 부른다). 이 저장소의 커밋 작성자는 `esqsoy` noreply 주소로 설정돼 있다(`git config` 저장소 범위).
- 26.11.03에 만든 Google Drive `빨라고양 자료 · PCIC 보관본` 폴더('읽어 두기' 문서)는 맥미니 폴더를 정하기 전 것이다. 둘지 지울지는 영신이 정한다.

## 열린 질문 (영신 결정 대기)

- 공통 원장을 **기능×수준 사다리**로 키울지. **칸 수 초안이 나왔다(26.11.04, 영신 검토 대기).** 검토 페이지 https://claude.ai/artifact/5v9b3inZWWQU1jvLEVigMb (줄마다 댓글), 데이터 [ladder-draft-20261104.json](goyang-common/ladder-draft-20261104.json), 만드는 스크립트 [ladder.py](goyang-common/ladder.py).
  - 칸은 A(A1~A2 기본꼴)·B(B1~B2)·C(C1 다듬은 꼴). PCIC가 그 기능에 꼴을 둔 띠마다 한 칸, 지금 문장의 띠는 늘 한 칸. 근거 없는 89항목(대부분 주제 T)은 한 칸.
  - 추천(지금보다 낮은 띠도 둠) 570문장(새로 312), 대안(지금 수준부터) 516문장.
  - 영신이 정할 것: 낮은 칸을 둘지, 한 PCIC 기능을 여러 항목이 나눠 쓰는 묶음(1.2 정보 묻기 9항목, 1.3 정보 주기 5항목 등)에서 B·C 칸을 줄일지, 근거 없는 F6(말이 막혔을 때)에 B 칸을 더할지.
  - PCIC 5장 실측: 기능 표 140개, 기능×수준 840칸 가운데 643칸에 표현 꼴이 있다(예전 '약 860칸'은 어림).
- 고양공유 원칙 전문(지금은 tangogoyang PRINCIPLES 0절)을 이 저장소로 옮길지.

## 그 밖의 고양공유 후보 (tangogoyang HANDOFF에서 넘겨받음)

다리 언어, 소리, 학습자 폭, 이정표, 읽기량, 시험 과정 위상. 영신과 함께 짜는 중인 '제2외국어 학습용 기본 틀'의 남은 칸이다. 정한 것(문자 학습 단계 맨 처음, 그 언어 자판+알파벳 입력, 예문 내용 공통, 문법 지도 먼저, 기초·회화 비중 크게, 고전어판은 따로)은 tangogoyang PRINCIPLES 0절에 있다.
