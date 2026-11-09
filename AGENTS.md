# 빨라고양 · 고양공유 작업 지침

## 시작할 때

1. `git status --short`로 진행 중인 변경을 확인한다. 기존 변경을 덮어쓰지 않는다. 고치기 전에 pull 한다.
2. [HANDOFF.md](HANDOFF.md)에서 최신 상태와 열린 질문을 확인한다.
3. 빨라고양 일을 하면 [PRINCIPLES.md](PRINCIPLES.md)를 읽는다(0-1 기본 설계, 0-2 빨라고양 한정 사항). 예문이나 고양이 대사를 쓰면 소재 목록 [es/topics.md](es/topics.md)도 본다. 공통 원장을 다루면 [goyang-common/README.md](goyang-common/README.md)를 읽는다.
4. 고양공유 원칙 전문은 아직 탄고고양 저장소 [PRINCIPLES 0절](https://github.com/esqsoy/tangogoyang/blob/main/PRINCIPLES.md#0-목적)에 있다. 예문 원칙(단어 통제 2-1, 소재 2-10, 빈칸 중의성 3절)도 그 문서를 따른다. 공통 원장의 사람 이름만은 따로 정했다: 영신초이·이소연·최혁 셋(영신은 늘 영신초이, 부를 때 "초이!"·"영신 쪼이!"), 가족관계 그대로(영신 26.11.06, [goyang-common README](goyang-common/README.md#예문-원칙과의-관계)).

## 이 저장소의 일

- 고양공유(공통) 일과 빨라고양(스페인어판) 일을 한다. 스페인어 일반 학습자판이 다음 차례다(26.11.06 영신). 탄고고양 일은 탄고고양 세션에서, 보카고양 일은 보카고양 세션에서 한다(26.11.03~04 영신).
- 공통 원장의 원본은 이 저장소의 `goyang-common/`이다. 탄고고양 저장소의 `goyang-common/`은 여기를 가리키는 안내만 남아 있다.
- 단어·항목을 더하거나 빼는 것, 원장 짜임을 바꾸는 것은 먼저 영신에게 의견을 낸다. 승인된 범위의 수정은 다시 묻지 않는다.

## 게임 파일을 고칠 때 (26.11.09~)

- 게임 HTML(`palagoyang*.html`)은 생성물이다. 직접 고치지 않고 `pipeline/<과정>/`의 원본(template.html, 데이터 스크립트)을 고친 뒤 다시 만든다. 만드는 법은 과정마다 README에 있다(지금은 [pipeline/sonidos/](pipeline/sonidos/README.md)).
- 화면·입력·발음 표준은 보카고양 [UI_STANDARD](https://github.com/esqsoy/vocagoyang/blob/main/UI_STANDARD.md)와 탄고고양 五十音 기록을 따른다. 빨라고양에서 달리한 것은 [PRINCIPLES 0-1](PRINCIPLES.md#0-1-빨라고양-기본-설계-2026-11-08)과 과정 README에 이유와 함께 적는다.
- 같이 쓰는 기능은 [SHARED.md](SHARED.md)를 따른다. 같이 쓰는 파일은 여기서 고치지 않는다.
- 맥미니에는 node가 없다. 검사는 파이썬 스크립트와 Claude 내장 브라우저(로컬 서버 `python3 -I -m http.server`)로 한다.
- 미리보기·로컬 수정·커밋·푸시·공개 배포를 구분해서 보고한다. GitHub Pages는 main / root로 켜져 있다(26.11.09 영신 "권한을 줄테니 열어줘"). main에 푸시하면 1~2분 뒤 공개된다. 공개를 확인했을 때만 [DEPLOYMENT.md](DEPLOYMENT.md)를 고친다.
- 과정을 만들거나 낱말을 고치면 영신 직검수 페이지(`review-page.py`)를 같은 Artifact 주소에 다시 올린다(`capabilities: {comments: {composer_only: true}}`).

## 공개 저장소다

- 이 저장소는 공개다. **저작권이 있는 원문(PCIC·Threshold·JF 등의 본문, 보기 문장, Can-do 문장)은 넣지 않는다.** 목차 번호와 짧은 제목, 출처 주소만 적는다.
- 원문 파일은 영신의 비공개 보관처인 **맥미니 지정 폴더**에 둔다: 맥미니 iCloud Drive `10 언어/고양/비공개/`(이 저장소 옆 폴더, git 밖). 저장소 안으로 복사하지 않는다. 작업 환경은 [HANDOFF.md](HANDOFF.md) '작업 환경'.

## 작업을 마칠 때

- 의미 있는 변경이나 결정은 [WORK_LOG.md](WORK_LOG.md)에 날짜, 요청·결정, 변경 파일, 실제 검증, 남은 일을 적는다.
- [HANDOFF.md](HANDOFF.md)는 현재 상태로 고친다. 대기 중인 일을 완료로 적지 않는다.
- 원장을 고치면 `python3 goyang-common/review-page.py --out <파일>`로 영신 직검수 페이지를 다시 만들어 같은 Artifact 주소에 올린다(`capabilities: {comments: {}}`).
- 영신에게는 한국어 반말로, 주요 결과는 대화 안에서도 알려 준다.
