# 공통 기능 표 (분가: 빨라고양)

보카고양이 본가이고, 빨라고양은 분가다. 공통 기능은 본가에서 만들거나 고치고, 분가는 그 기능 폴더를 가져와 자기 설정만 바꾼다. 원칙과 가져가는 법은 본가 [SHARED.md](https://github.com/esqsoy/vocagoyang/blob/main/SHARED.md)에 있다. 업데이트 소식은 AL 장부 이슈(`[빨라고양]`)로 온다.

| 기능 | 폴더 | 게임별 설정 | 본가 버전 | 가져간 버전 |
|---|---|---|---|---|
| 기록 옮기기 | `pipeline/record-transfer/` | `config.json`(빨라고양, `palagoyang-records`, 접두어 `palagoyang-`, Sonidos 키 `palagoyang-sonidos-`) | `69e8d5e` | `69e8d5e` (26.11.09) |

- 같이 쓰는 파일(merge.js·runtime.js·ui.html·style.css·build.cjs·README.md)은 본가 그대로다. 고칠 것이 있으면 여기서 고치지 않고 본가에 요청한다.
- **이 저장소만의 것:** 맥미니에는 node가 없어서, index.html에 넣는 일은 [pipeline/record_transfer_build.py](pipeline/record_transfer_build.py)가 build.cjs와 같은 글자로 한다. node가 있는 곳에서는 `node pipeline/record-transfer/build.cjs --check`로 같은지 본다.
- 본가 검사 `pipeline/tests/record-transfer.test.cjs`는 보카고양 키(`goyang-`)로 짜여 있어 가져오지 않았다.
- 화면 틀(모아둔 카드·돌파 축하·진행 속도 등)은 아직 공유 기능이 아니다. 탄고고양 틀을 통째로 빌려 왔다([pipeline/sonidos/README](pipeline/sonidos/README.md)).
