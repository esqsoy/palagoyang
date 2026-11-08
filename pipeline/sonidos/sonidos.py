#!/usr/bin/env python3
"""Sonidos y letras(소리·글자 단계, 0번 과정) 카드 만들기 → sonidos-data.json. build.py가 읽어 palagoyangsonidos.html을 만든다.

설계: palagoyang PRINCIPLES 0-1 9번(영신 26.11.08 "추천대로 가자"). 낱말 소리를 듣고 철자를 친다(받아쓰기).
다루는 것: j와 g(e·i 앞)의 [x], 읽지 않는 h, ll·y, r·rr, c·z(seseo), 같은 소리인 b·v, ñ, qu·gu·gü, 강세 규칙과 악센트.
- 한국어 뜻을 함께 보인다: casa(집)/caza(사냥), hola/ola처럼 소리가 같은 말을 뜻으로 가르고, 기초 낱말도 함께 익힌다.
- ①~④강 낱말에는 악센트가 없다. 악센트는 ⑤강에서 강세 규칙과 함께 배운다(4번 판정 '악센트가 빠지면 틀림'이 억울하지 않게).
- 강마다 순서대로 배운 뒤 강 전체 무작위(五十音 26.11.06 영신 "순서대로 내면 … 무지성으로 칠 수 있어").
- 낱말은 Claude가 골랐다(26.11.09). 영신 직검수 대기.
카드: en=정답 철자, w=화면 표기, ko=뜻, ipa=발음기호(중남미), pn=발음 설명(es_sound.py), c=이 카드의 철자 규칙, lv, id.
사용: python3 -I pipeline/sonidos/sonidos.py
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from es_sound import analyse, notes  # noqa: E402

FRONT = 'eiéí'


def rules(word, focus):
    """그 연습에서 배우는 철자 규칙 가운데 이 낱말에 든 것(많아야 둘)."""
    w, out = word.lower(), []
    a = analyse(word)

    def has(p):
        return re.search(p, w) is not None
    R = []
    if 'k' in focus:
        if has(r'qu'): R.append('que·qui의 u는 읽지 않는다: [ke]·[ki]')
        if has(r'c(?![eiéíh])'): R.append('c는 a·o·u와 자음 앞에서 [k]')
        if has(r'k'): R.append('k는 kilo 같은 바깥말에만 쓴다')
    if 'g' in focus:
        if has(r'gü'): R.append('ü(점 두 개)를 찍으면 güe·güi의 u를 읽는다: [ɡwe]·[ɡwi]')
        if has(r'gu[eiéí]'): R.append('gue·gui의 u는 읽지 않는다: [ɡe]·[ɡi]')
        if has(r'gu[ao]'): R.append('gua·guo의 u는 읽는다: [ɡwa]')
        if has(r'g(?![eiéíuü])'): R.append('g는 a·o·u와 자음 앞에서 [ɡ]')
    if 'x' in focus:
        if has(r'j'): R.append('j는 언제나 [x]')
        if has(r'g[eiéí]'): R.append('g는 e·i 앞에서 [x]: j와 같은 소리')
    if 's' in focus:
        if has(r'c[eiéí]'): R.append('c는 e·i 앞에서 [s] (에스파냐는 [θ])')
        if has(r'z'): R.append('z도 [s] (에스파냐는 [θ])')
        if not R: R.append('s·z·c(e·i 앞)는 같은 소리 [s]: 글자는 낱말마다 외운다')
    if 'b' in focus:
        R.append('b와 v는 같은 소리: 글자는 낱말마다 외운다')
    if 'h' in focus:
        R.append('h는 읽지 않는다')
    if 'r' in focus:
        if has(r'rr'): R.append('rr은 모음 사이에만 쓰고 떤다 [r]')
        if w.startswith('r'): R.append('낱말 첫 r은 rr처럼 떤다 [r]')
        if has(r'[nls]r'): R.append('n·l·s 뒤의 r도 떤다 [r]')
        if has(r'[aeiouáéíóú]r[aeiouáéíóú]') and not has(r'rr'): R.append('모음 사이 r 하나는 한 번 튕긴다 [ɾ]')
        if has(r'r$'): R.append('끝의 r도 한 번 튕긴다 [ɾ]')
    if 'y' in focus:
        R.append('ll과 y는 같은 소리 [ʝ]: 글자는 낱말마다 외운다')
    if 'ñ' in focus:
        if has(r'ñ'): R.append('ñ는 n과 다른 글자다 [ɲ]')
        if has(r'ch'): R.append('ch는 두 글자로 한 소리 [tʃ]')
    if 'plain' in focus:
        if has(r'(?<![nl])d') and 'ð' in a['ipa']: R.append('d는 모음 사이·끝에서 부드럽게 [ð]')
        if re.search(r'[iu][aeo]', w): R.append('i·u와 다른 모음이 만나면 한 음절로 붙는다: ' + '·'.join(a['syl']))
    if 'stress' in focus:
        R.append(stress_rule(word, a))
    return ' · '.join(R[:2])


QUESTION = {'qué': 'que …라는 것', 'cómo': 'como …처럼', 'dónde': 'donde …하는 곳', 'cuándo': 'cuando …할 때',
            'quién': 'quien …하는 사람', 'cuánto': 'cuanto …만큼'}
PAIRS = {'tú': ('tú', '너', 'tu', '너의'), 'tu': ('tú', '너', 'tu', '너의'), 'sí': ('sí', '응', 'si', '만약'), 'si': ('sí', '응', 'si', '만약'),
         'él': ('él', '그', 'el', '관사'), 'el': ('él', '그', 'el', '관사'), 'té': ('té', '차', 'te', '너를'), 'te': ('té', '차', 'te', '너를'),
         'mí': ('mí', '나', 'mi', '나의'), 'mi': ('mí', '나', 'mi', '나의')}


def stress_rule(word, a):
    w, syl, st, n = word.lower(), a['syl'], a['stress'], a['n']
    show = '·'.join(syl)
    acc = any(c in 'áéíóú' for c in w)
    if w in PAIRS:
        x, xk, y, yk = PAIRS[w]
        return f'한 음절 말은 악센트를 안 찍는다. 다만 뜻을 가를 때 찍는다: {x} {xk} / {y} {yk}'
    if w in QUESTION:
        return f'물음말에는 악센트를 찍는다: ¿{w.capitalize()}? / {QUESTION[w]}'
    if acc and re.search(r'[íú][aeo]|[aeo][íú]', w):
        return f'약한 모음 i·u에 강세가 오면 두 모음을 갈라 악센트를 찍는다: {show}'
    end = w[-1]
    vns = end in 'aeiouáéíóúns'
    if not acc:
        return (f'모음·n·s로 끝나면 끝에서 둘째 음절이 세다: {show}' if vns
                else f'n·s 말고 자음으로 끝나면 끝 음절이 세다: {show}')
    if st == n - 1:
        return f'모음·n·s로 끝나는데 끝 음절이 세서 악센트를 찍는다: {show}'
    if st == n - 2:
        return f'자음으로 끝나는데 끝에서 둘째가 세서 악센트를 찍는다: {show}'
    return f'끝에서 셋째 음절이 세면 언제나 악센트를 찍는다: {show}'


# (낱말, 뜻, 덧붙임)
L1 = [
    ('모음 a·e·i·o·u', ['plain'], [('mesa', '책상'), ('luna', '달'), ('sol', '해'), ('pan', '빵'), ('mano', '손'), ('piso', '층, 바닥'),
                                 ('sopa', '수프'), ('uno', '하나'), ('dos', '둘'), ('malo', '나쁜')]),
    ('자음 p·t·m·n·l·s·f·d', ['plain'], [('pelo', '머리카락'), ('foto', '사진'), ('fiesta', '파티'), ('tomate', '토마토'), ('nada', '아무것도'),
                                     ('dedo', '손가락'), ('lunes', '월요일'), ('semana', '주(週)'), ('siete', '일곱'), ('planta', '식물'), ('tres', '셋')]),
]
L2 = [
    ('[k] c·qu·k', ['k'], [('casa', '집'), ('cosa', '것, 물건'), ('cama', '침대'), ('comida', '음식'), ('clase', '수업'), ('cuatro', '넷'),
                          ('poco', '조금'), ('queso', '치즈'), ('parque', '공원'), ('kilo', '킬로')]),
    ('[ɡ] g·gu·gü', ['g'], [('gato', '고양이'), ('amigo', '친구'), ('lago', '호수'), ('tengo', '(나는) 가지고 있다'), ('grande', '큰'),
                           ('seguir', '계속하다, 따라가다'), ('juguete', '장난감'), ('guitarra', '기타'), ('agua', '물'), ('paraguas', '우산'),
                           ('pingüino', '펭귄'), ('bilingüe', '두 언어를 하는')]),
    ('[x] j·ge·gi', ['x'], [('jugo', '주스', '중남미 말이다. 에스파냐는 zumo'), ('ojo', '눈(보는 눈)'), ('ajo', '마늘'), ('rojo', '빨간'),
                          ('viejo', '늙은, 오래된'), ('mujer', '여자'), ('joven', '젊은'), ('gente', '사람들'), ('gigante', '거인'),
                          ('colegio', '학교'), ('girasol', '해바라기')]),
]
L3 = [
    ('[s] s·z·c(e·i)', ['s'], [('cena', '저녁밥'), ('cine', '영화관'), ('cielo', '하늘'), ('ciudad', '도시'), ('cinco', '다섯'), ('once', '열하나'),
                             ('doce', '열둘'), ('zapato', '구두'), ('azul', '파란'), ('plaza', '광장'), ('taza', '찻잔'), ('cerveza', '맥주'),
                             ('diez', '열'), ('vez', '번(횟수)')]),
    ('b·v는 같은 소리', ['b'], [('vaca', '소'), ('vino', '포도주'), ('bueno', '좋은'), ('beber', '마시다'), ('nueve', '아홉'), ('uva', '포도'),
                          ('lobo', '늑대'), ('verde', '초록색의'), ('nube', '구름'), ('ventana', '창문')]),
    ('읽지 않는 h', ['h'], [('hola', '안녕'), ('hora', '시각, 시간'), ('hijo', '아들'), ('hermano', '형제'), ('helado', '아이스크림'),
                        ('huevo', '달걀'), ('ahora', '지금'), ('hoy', '오늘'), ('hambre', '배고픔'), ('historia', '역사')]),
]
L4 = [
    ('[ɾ] r·[r] rr', ['r'], [('pero', '그러나'), ('perro', '개'), ('caro', '비싼'), ('carro', '자동차', '중남미 말이다. 에스파냐는 coche'),
                           ('cara', '얼굴'), ('toro', '황소'), ('torre', '탑'), ('tierra', '땅'), ('arroz', '쌀')]),
    ('첫 r·끝 r', ['r'], [('rosa', '장미'), ('ropa', '옷'), ('rico', '맛있는, 부자인'), ('rubio', '금발의'), ('ruido', '소음'),
                       ('sonrisa', '미소'), ('mar', '바다'), ('flor', '꽃'), ('calor', '더위')]),
    ('[ʝ] ll·y', ['y'], [('llave', '열쇠'), ('lluvia', '비'), ('calle', '거리'), ('pollo', '닭고기'), ('silla', '의자'), ('ella', '그녀'),
                        ('playa', '해변'), ('yo', '나'), ('ayer', '어제'), ('mayo', '5월')]),
    ('ñ·ch', ['ñ'], [('niño', '남자아이'), ('año', '해(年)'), ('mañana', '내일, 아침'), ('señor', '…씨, 아저씨'), ('montaña', '산'),
                    ('baño', '화장실'), ('pequeño', '작은'), ('español', '스페인어'), ('leche', '우유'), ('noche', '밤'), ('ocho', '여덟'),
                    ('mucho', '많이')]),
]
L5 = [
    ('강세 규칙(악센트 없음)', ['stress'], [('camisa', '셔츠'), ('martes', '화요일'), ('naranja', '오렌지'), ('imagen', '그림, 이미지'),
                                     ('volumen', '음량, 부피'), ('papel', '종이'), ('hablar', '말하다'), ('color', '색'), ('feliz', '행복한'),
                                     ('verdad', '진실'), ('pared', '벽'), ('animal', '동물')]),
    ('끝 음절 강세와 악센트', ['stress'], [('café', '커피'), ('sofá', '소파'), ('mamá', '엄마'), ('papá', '아빠'), ('también', '…도, 역시'),
                                   ('canción', '노래'), ('avión', '비행기'), ('inglés', '영어'), ('adiós', '잘 가'), ('jamón', '햄'),
                                   ('ratón', '쥐'), ('francés', '프랑스어')]),
    ('앞쪽 강세와 악센트', ['stress'], [('lápiz', '연필'), ('árbol', '나무'), ('fácil', '쉬운'), ('difícil', '어려운'), ('azúcar', '설탕'),
                                 ('música', '음악'), ('sábado', '토요일'), ('teléfono', '전화'), ('médico', '의사'), ('número', '숫자'),
                                 ('pájaro', '새'), ('plátano', '바나나')]),
    ('두 모음 가르기·물음말', ['stress'], [('día', '날, 하루'), ('país', '나라'), ('río', '강'), ('tía', '이모, 고모'), ('qué', '무엇'),
                                   ('cómo', '어떻게'), ('dónde', '어디'), ('cuándo', '언제'), ('quién', '누구'), ('cuánto', '얼마나')]),
    ('뜻을 가르는 악센트', ['stress'], [('tú', '너'), ('tu', '너의'), ('sí', '응, 그래'), ('si', '만약 …면'), ('él', '그(남자)'),
                                 ('el', '(남성 명사 앞 관사)'), ('té', '차(마시는 차)'), ('te', '너를, 너에게'), ('mí', '나(전치사 뒤: para mí)'),
                                 ('mi', '나의')]),
]
LESSONS = [('Sonidos ①', '모음과 글자대로', L1), ('Sonidos ②', '[k] [ɡ] [x]', L2), ('Sonidos ③', '[s] · b=v · h', L3),
           ('Sonidos ④', 'r·rr · ll·y · ñ·ch', L4), ('Sonidos ⑤', '강세와 악센트', L5)]


def card(entry, focus, lesson_no):
    word, ko, *extra = entry
    a = analyse(word)
    c = rules(word, focus)
    if extra:
        c = (c + ' · ' if c else '') + extra[0]
    return {'id': 'es-snd-' + word, 'en': word, 'w': word, 'ko': ko, 'ipa': a['ipa'],
            'pn': notes(word, stress_note=lesson_no in (1, 5)), 'c': c, 'lv': 'sonidos'}


def ex(title, cards, rnd=False):
    e = {'scope': '2026', 'title': title, 'words': cards}
    if rnd:
        e['rnd'] = 1
    return e


data, seen = [], {}
for no, (lid, name, exs) in enumerate(LESSONS, 1):
    out, all_cards = [], []
    for title, focus, entries in exs:
        cs = [card(e, focus, no) for e in entries]
        for c in cs:
            assert c['en'] not in seen, ('같은 낱말이 두 번', c['en'], seen.get(c['en']))
            seen[c['en']] = lid
            if no < 5:
                assert not re.search(r'[áéíóú]', c['en']), ('⑤강 전에 악센트', c['en'])
        out.append(ex(title, cs))
        all_cards += cs
    out.append(ex(f'{lid[-1]} 전체 무작위 ({len(all_cards)}낱말)', [dict(c) for c in all_cards], rnd=True))
    data.append({'id': lid, 'name': name, 'lesson': no, 'exercises': out})
for L in data:
    for j, e in enumerate(L['exercises']):
        e['ex'] = j + 1

(HERE / 'sonidos-data.json').write_text(json.dumps(data, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
words = sum(len(e['words']) for L in data for e in L['exercises'] if not e.get('rnd'))
cards = sum(len(e['words']) for L in data for e in L['exercises'])
print('Sonidos y letras', len(data), '강', sum(len(L['exercises']) for L in data), '연습', words, '낱말', cards, '카드(무작위 포함)')
