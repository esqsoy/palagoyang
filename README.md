# 빨라고양 (palagoyang)

고양 시리즈의 스페인어판 빨라고양(palabra + 고양) 저장소다. 판 작업은 26.11.09에 시작했다(26.11.06 영신: 스페인어 일반 학습자판을 탄고고양 일반판보다 먼저). 첫 과정은 소리·글자 단계다.

지금은 **고양공유**(모든 제2외국어 고양 시리즈가 같이 쓰는 것)를 이 저장소에 둔다(26.11.04 영신).

## 게임 (Palabra Goyang)

- [index.html](index.html): 교재 선택, 다른 기기로 기록 옮기기
- [palagoyangsonidos.html](palagoyangsonidos.html): **Sonidos y letras**(소리·글자 단계, 5강·184낱말). 소리를 듣고 철자를 친다. 생성물이고, 원본과 만드는 법은 [pipeline/sonidos/](pipeline/sonidos/README.md)에 있다
- 같이 쓰는 기능(기록 옮기기)은 [SHARED.md](SHARED.md)
- 공개 주소: https://esqsoy.github.io/palagoyang/ (GitHub Pages, main / root, 26.11.09에 켬. [DEPLOYMENT.md](DEPLOYMENT.md))

## 고양공유와 설계

- [goyang-common/](goyang-common/README.md): 언어불문 필수 표현 원장(초안 0.5, 272항목 585칸, 한국어 문장 검수 끝)과 원문 대조표, 합집합 풀
- [goyang-common/word-pool.md](goyang-common/word-pool.md): 고양공유 단어 풀 짜임(끝점 C2, 네 층, HSK 3.0 개념 목록·약 11,000 수준, 26.11.09 영신)
- [goyang-common/spanish-pcic-sources.md](goyang-common/spanish-pcic-sources.md): 빨라고양을 시작할 때 쓸 PCIC 자료 안내
- [PRINCIPLES.md](PRINCIPLES.md): 빨라고양 원칙과 이유. 0-1이 기본 설계(26.11.08 확정)
- [es/expressions-es.json](es/expressions-es.json): 스페인어 판 원장(0.1, F1 시범 60칸 / 585칸). 검사 `python3 -I es/ledger-check.py`, 직검수 페이지 `python3 -I es/ledger-page.py <out.html>`
- [es/topics.md](es/topics.md): 빨라고양 한정 소재 목록(영신 부부의 에스파냐 신혼여행, 사그라다 파밀리아는 늘 "사그리아가 아니라고양!"과 함께). 규칙은 [PRINCIPLES 0-2](PRINCIPLES.md#0-2-빨라고양-한정-사항-2026-11-09)
- [es/grammar-map.md](es/grammar-map.md): 문법 지도(0세트~C2 141항목, 원본 `es/grammar-map.json`). md와 검토 페이지는 `python3 -I es/grammar-page.py es/grammar-map.json --md es/grammar-map.md --html <out.html>`로 그린다
- [design-20261107.md](design-20261107.md): 기본 설계 안의 근거·출처 전문. 결정 페이지는 `python3 design-page.py design-20261107.md <out.html>`로 그린다
- 현재 상태는 [HANDOFF.md](HANDOFF.md), 작업 기록은 [WORK_LOG.md](WORK_LOG.md), 작업 지침은 [AGENTS.md](AGENTS.md)

다른 판: 보카고양(영어) [esqsoy/vocagoyang](https://github.com/esqsoy/vocagoyang), 탄고고양(일본어) [esqsoy/tangogoyang](https://github.com/esqsoy/tangogoyang).
