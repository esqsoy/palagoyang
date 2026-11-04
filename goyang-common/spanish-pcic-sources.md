# 빨라고양(스페인어판)용 자료 · PCIC 보관본

결정(영신, 26.11.03): "이 데이터 자체는 스페인어판용으로 남기자". 공통 원장 대조에 쓴 PCIC 원문 여섯 쪽을 빨라고양을 시작할 때 다시 쓴다.

## 무엇인가

Instituto Cervantes, *Plan curricular del Instituto Cervantes. Niveles de referencia para el español*(2006)의 두 장이다.

- 5장 기능(Funciones): 기능 약 140개, 수준마다 스페인어 보기 표현이 달려 있다. 보기 표현 줄은 약 5,000줄이다(26.11.03 대충 셈). 26.11.04 실측: 기능 표 140개, 기능×수준 840칸 가운데 643칸에 표현 꼴이 있다(꼴 2,444개). 수준 분포를 쓴 사다리 칸 초안은 [ladder.py](ladder.py)·[ladder-draft-20261104.json](ladder-draft-20261104.json).
- 6장 화용 전술·전략(Tácticas y estrategias pragmáticas): 담화 짜기·양태(강조·누그러뜨리기)·공손 전략.

공통 원장은 이 중 **목차(할 일)만** 받았다. 목차 번호와 원장 id의 대응은 [source-check-20261103.json](source-check-20261103.json)의 `pcic_functions`·`pcic_tactics`에 있다. 보기 표현은 스페인어로 말하는 여러 방식이라 공통 원장(한국어 공통 내용)에는 맞지 않고, 빨라고양의 판 고유 원장 몫이다.

## 어디에 있나

원래 주소 cvc.cervantes.es는 26.11.03 현재 서버가 모든 주소에 404를 돌려준다. Internet Archive 보관본을 받아 맥미니 지정 폴더에 두었다(아래). 다시 받을 주소:

| 쪽 | 보관본 |
|---|---|
| 5장 A1-A2 | https://web.archive.org/web/20260624131458/https://cvc.cervantes.es/ensenanza/biblioteca_ele/plan_curricular/niveles/05_funciones_inventario_a1-a2.htm |
| 5장 B1-B2 | https://web.archive.org/web/20260624131458/https://cvc.cervantes.es/ensenanza/biblioteca_ele/plan_curricular/niveles/05_funciones_inventario_b1-b2.htm |
| 5장 C1-C2 | https://web.archive.org/web/20260624131458/https://cvc.cervantes.es/ensenanza/biblioteca_ele/plan_curricular/niveles/05_funciones_inventario_c1-c2.htm |
| 6장 A1-A2 | https://web.archive.org/web/20260725113425/https://cvc.cervantes.es/ensenanza/biblioteca_ele/plan_curricular/niveles/06_tacticas_pragmaticas_inventario_a1-a2.htm |
| 6장 B1-B2 | https://web.archive.org/web/20260725113438/https://cvc.cervantes.es/ensenanza/biblioteca_ele/plan_curricular/niveles/06_tacticas_pragmaticas_inventario_b1-b2.htm |
| 6장 C1-C2 | https://web.archive.org/web/20260725113440/https://cvc.cervantes.es/ensenanza/biblioteca_ele/plan_curricular/niveles/06_tacticas_pragmaticas_inventario_c1-c2.htm |

소개 쪽: `05_funciones_introduccion.htm`, `06_tacticas_pragmaticas_introduccion.htm`(같은 보관본, 20260624131351). 같은 책의 다른 장(문법·발음·개념·문화 등)도 같은 `niveles/` 아래에 있다.

**원문 파일은 이 저장소에 넣지 않는다.** 이 저장소는 공개이고 PCIC는 세르반테스 문화원의 저작물이라, 올리면 재배포가 된다. 파일은 맥미니 iCloud Drive `10 언어/고양/비공개/pcic/`에 둔다. 26.11.04 맥미니 세션이 위 주소의 보관 시점에서 보관본 툴바 없는 원래 HTML(`/web/<시점>id_/…`)로 8쪽(목록 6쪽, 소개 2쪽)을 받았다. 맥미니 세션은 web.archive.org에 들어갈 수 있고, 클라우드 세션은 막힐 수 있다(26.11.03 막힘). 26.11.03에 만든 Google Drive `빨라고양 자료 · PCIC 보관본` 폴더('읽어 두기' 문서)는 맥미니 폴더를 정하기 전 것이다.

## 빨라고양에서 쓰는 법

- 공통 원장 id마다 `same`/`counterpart`/`none`을 판정할 때, 그 기능의 PCIC 보기 표현을 보고 스페인어가 실제로 쓰는 꼴을 고른다.
- 판 고유 원장: 공통 원장에 없는 스페인어 고유 기능과 수준별 꼴(접속법을 쓰는 공손·바람 표현 등)을 PCIC 목차와 수준에 맞춰 짠다.
- 문장은 직접 쓴다. 짧은 관용 표현은 그 언어의 일반 표현이라 겹칠 수 있지만, PCIC 보기 표현 목록을 통째로 옮기지 않는다(0절 고양공유, 공통 원장과 같은 원칙).
