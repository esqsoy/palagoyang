# Sonidos y letras (빨라고양 · 소리·글자 단계)

낱말 소리를 듣고 스페인어 철자를 치는 과정이다. 문제 칸에는 🔊 단추, 한국어 뜻, 글자 수만큼의 칸이 보인다. 맞히거나 따라쓰기를 마치면 발음기호(중남미), 그 카드의 철자 규칙, 발음 설명(판정 넷)이 나온다. 결정과 이유는 [PRINCIPLES 0-1 9번](../../PRINCIPLES.md#0-1-빨라고양-기본-설계-2026-11-08).

## 원본과 조립

| 파일 | 무엇 | 원본인가 |
|---|---|---|
| `sonidos.py` | 강·연습·낱말·뜻·철자 규칙 | 원본 |
| `es_sound.py` | 낱말 → 음절·발음기호·발음 설명. `python3 -I es_sound.py`로 발음기호 128개 검사 | 원본 |
| `sonidos-data.json` | sonidos.py가 만든 카드 | 생성물 |
| `template.html` | 화면. 탄고고양 틀(esqsoy/tangogoyang `pipeline/jlpt/template.html`, 2eb7596)에서 [derive-template.py](derive-template.py)로 한 번 뽑은 뒤 손으로 고친다 | 원본 |
| `../../palagoyangsonidos.html` | 조립 결과 | **생성물. 직접 고치지 않는다** |
| `../../index.html` | 교재 선택. 낱말 수(`VOCAB_STATS`)와 기록 옮기기 구간만 build.py가 다시 쓴다 | 원본(그 두 구간 밖) |

```
python3 -I pipeline/sonidos/sonidos.py      # sonidos-data.json
python3 -I pipeline/sonidos/build.py        # palagoyangsonidos.html, index.html 낱말 수·기록 옮기기
python3 -I pipeline/sonidos/review-page.py <out.html>   # 영신 직검수 페이지(Artifact, 카드마다 댓글)
```

## 화면 틀에서 바꾼 것 (template.html 맨 끝 '빨라고양 스페인어' 구간)

탄고고양 틀의 일본어 함수와 같은 이름의 함수를 맨 끝에서 다시 정의한다. 스크립트 안 함수 선언은 마지막 것이 이긴다. 일본어 코드는 `JP_MODE="es"`라 돌지 않는다.

- **판정**(4번): 대소문자는 가리지 않는다. 악센트·ñ·ü가 빠지거나 틀리면 틀림이다. ¿ ¡ 같은 문장부호는 빈칸에 들지 않는다.
- **입력**(4번): 영어 자판으로 친다. PC는 a' → á, u: → ü, n~ → ñ로 친다. 휴대폰은 길게 누르기나 입력칸 아래 글자 단추(á é í ó ú ü ñ)를 쓴다.
  - 글자 단추는 누르는 순간 넣어서 입력칸 초점을 잃지 않는다. 맞힌 뒤에는 숨기고, 따라쓰기 때는 둔다.
  - 칸을 다 채워도 끝 글자가 모음이면 바로 판정하지 않는다. cafe까지 친 뒤 '를 칠 수 있게 하려는 것이다. 맞으면 바로 받는다.
- **음성**(3번): es-MX → es-US → es-419 → 그 밖의 중남미 → 에스파냐 차례로 고른다. 받아쓰기라 문제 때 읽는다(속도 0.85). 🔊 단추와 Space로 다시 듣는다.
  - 연습 첫 카드는 누른 그 자리에서 읽는다(아이폰). 그다음 카드는 0.26초 뒤에 읽는다. 앞 소리를 끊은 바로 뒤에 읽으면 사파리가 새 소리를 씹는다(탄고고양 五十音 경험).
- **오답 대사**: 악센트·ñ·ü만 틀렸으면 그 자리를 짚는다. 소리는 맞는데 글자가 다르면 "소리는 맞다고양! 근데 글자는 ‘…’ 이렇게 쓴다고양"이라고 한다(s/z/c, b/v, h, ll/y, j/g, qu/k).
- **저장 키**: `palagoyang-sonidos-`. `palagoyang-` 바로 뒤는 FÁBULA 몫으로 남긴다. 같은 esqsoy.github.io의 보카고양(`goyang-`)·탄고고양(`tangogoyang-`)과 겹치지 않는다.
- 화면 표준은 보카고양 [UI_STANDARD](https://github.com/esqsoy/vocagoyang/blob/main/UI_STANDARD.md)를 따른다. 예문이 없는 카드라 마더텅 방식이다.

## 확인한 것 (26.11.09, 맥미니 내장 브라우저 375×812, 로컬 서버)

- 함수 검사 26개 통과: 판정, 입력 변환, 오답 대사 9갈래, 끝 모음 대기, 저장 키, 카드 수 368.
- 화면 흐름: cafe → ' → café 정답, 공개 칸(발음기호·규칙·설명), cafe + Enter → 악센트 대사와 따라쓰기, é 단추로 마침(초점 유지).
- 연습 한 판 끝까지(틀린 sol 2회독), 결과 화면, 기록 옮기기가 `palagoyang-sonidos-` 키만 모으는 것, 콘솔 오류 없음.
- **확인 못 한 것:** 실제 소리. 이 브라우저에는 스페인어 음성이 없다. 아이폰·안드로이드·PC 실기기에서 들어 봐야 한다. 짧은 낱말(yo, sol, tú)이 아이폰에서 끊기는지도 본다(탄고고양 가나 한 글자 끊김과 같은 문제일 수 있다).
