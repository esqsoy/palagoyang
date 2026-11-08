#!/usr/bin/env python3
"""스페인어 낱말 → 발음기호(중남미)·음절·발음 설명. sonidos.py가 쓴다. 26.11.09 Claude.

- 발음은 중남미 기본값이다(palagoyang PRINCIPLES 0-1 3번): c(e·i)·z = [s](seseo), ll = y = [ʝ](yeísmo).
- 기호는 소리 그대로(좁은 표기)다. b·d·g는 첫머리와 m·n 뒤(d는 l 뒤도)에서 [b d ɡ], 그 밖에서는 [β ð ɣ].
  n은 [k ɡ x] 앞에서 [ŋ], b·p·m 앞에서 [m].
- 발음 설명은 탄고고양 五十音의 판정 넷을 따른다(PRINCIPLES 0-1 9번):
  한국어와 같으면 뺀다 / 한국어식으로 해도 통하면 그렇게 알리고 차이를 짚는다 /
  한국어식으로 하면 다른 소리가 되면 "하면 안 된다"와 주의 / 한국어에 없는 소리는 따로.
  기호 표시는 소리가 같아도 기호를 익히게 짧게 남긴다(五十音과 같다). 조음 용어에는 영어를 함께 적는다.
- 해설의 영어는 거짓 짝만(10번)이라, 발음 설명에서 영어 낱말에 빗대지 않는다.
사용: python3 -I es_sound.py  (아래 TESTS로 발음기호를 검사한다)
"""
import re

ACC = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
VOW = set('aeiouáéíóúü')
STRONG = set('aeoáéíóú')          # 악센트가 붙은 i·u도 센 모음처럼 음절을 가른다
FRONT = set('eiéí')
ONSET2 = {'pl', 'pr', 'bl', 'br', 'fl', 'fr', 'tr', 'dr', 'cl', 'cr', 'gl', 'gr', 'kl', 'kr'}


def _units(word):
    """철자 → [(글자, 'C'|'V')]. h는 읽지 않아 뺀다. qu·gu(e·i 앞)는 자음 하나, gü는 g + 반모음."""
    w, out, i = word.lower(), [], 0
    while i < len(w):
        c, two, nx = w[i], w[i:i + 2], w[i + 2:i + 3]
        if two in ('ch', 'll', 'rr'):
            out.append((two, 'C')); i += 2; continue
        if two in ('qu', 'gu') and nx in FRONT:
            out.append((two, 'C')); i += 2; continue
        if c == 'h':
            i += 1; continue
        if c == 'y':
            out.append(('y', 'C' if nx_vowel(w, i) else 'V')); i += 1; continue
        out.append((c, 'V' if c in VOW else 'C')); i += 1
    return out


def nx_vowel(w, i):
    return i + 1 < len(w) and w[i + 1] in VOW


def syllables(word):
    """[[(글자, 종류), …], …] 음절마다. 센 모음 둘은 가르고(hiatus), 약한 모음(i·u·ü·y)은 붙인다."""
    u = _units(word)
    # 모음 덩어리를 음절 핵으로 나눈다
    nuclei, cur, strong = [], [], False   # nuclei: [(시작, 끝)] u 안의 자리
    k = 0
    groups = []
    while k < len(u):
        if u[k][1] == 'V':
            j = k
            while j < len(u) and u[j][1] == 'V':
                j += 1
            groups.append((k, j)); k = j
        else:
            k += 1
    for a, b in groups:
        start, has = a, False
        for k in range(a, b):
            s = u[k][0] in STRONG
            if s and has:
                nuclei.append((start, k)); start, has = k, True
            else:
                has = has or s
        nuclei.append((start, b))
    if not nuclei:
        return [u]
    # 자음을 앞뒤 음절로 나눈다
    bounds = [0]
    for (a1, b1), (a2, b2) in zip(nuclei, nuclei[1:]):
        cons = list(range(b1, a2))
        n = len(cons)
        if n == 0:
            cut = a2
        elif n == 1:
            cut = cons[0]
        else:
            last2 = u[cons[-2]][0] + u[cons[-1]][0]
            cut = cons[-2] if last2 in ONSET2 else cons[-1]
        bounds.append(cut)
    bounds.append(len(u))
    return [u[bounds[i]:bounds[i + 1]] for i in range(len(bounds) - 1)]


def stress_index(word, syls):
    for i, s in enumerate(syls):
        if any(g in ACC for g, _ in s):
            return i
    if len(syls) < 2:
        return 0
    last = word.lower()[-1]
    return len(syls) - 2 if last in 'aeiouns' else len(syls) - 1


def _cons(g, nxt, prev, initial):
    """자음 글자 → 소리. nxt: 다음 글자(없으면 ''), prev: 앞 소리, initial: 낱말 첫머리."""
    if g in ('b', 'v'):
        return 'b' if initial or prev in ('m', 'n') else 'β'
    if g == 'd':
        return 'd' if initial or prev in ('n', 'l') else 'ð'
    if g == 'gu' or (g == 'g' and nxt not in FRONT):
        return 'ɡ' if initial or prev in ('n', 'ŋ') else 'ɣ'
    if g == 'g':
        return 'x'
    if g == 'c':
        return 's' if nxt in FRONT else 'k'
    if g in ('qu', 'k'):
        return 'k'
    if g in ('z', 's'):
        return 's'
    if g == 'j':
        return 'x'
    if g == 'x':
        return 'ks'
    if g == 'ch':
        return 'tʃ'
    if g in ('ll', 'y'):
        return 'ʝ'
    if g == 'ñ':
        return 'ɲ'
    if g == 'rr':
        return 'r'
    if g == 'r':
        return 'r' if initial or prev in ('n', 'l', 's') else 'ɾ'
    return g


VELAR = {'k', 'ɡ', 'ɣ', 'x'}


def analyse(word):
    """→ {'syl': ['ca','sa'], 'stress': i, 'ipa': 'ˈkasa', 'phones': [(소리, 음절 번호, 자리, 앞 소리, 다음 소리)]}
    자리: onset(음절 첫 자음) / cluster(자음 뒤 자음, 음절 첫머리) / nucleus / glide / coda"""
    syls = syllables(word)
    st = stress_index(word, syls)
    flat = [(g, kind, si) for si, s in enumerate(syls) for g, kind in s]
    phones, prev = [], ''
    for idx, (g, kind, si) in enumerate(flat):
        nxt = flat[idx + 1][0][0] if idx + 1 < len(flat) else ''
        initial = idx == 0
        if kind == 'C':
            p = _cons(g, nxt, prev, initial)
            if g == 'n':
                ng = flat[idx + 1] if idx + 1 < len(flat) else None
                if ng and ng[1] == 'C':
                    q = _cons(ng[0], flat[idx + 2][0][0] if idx + 2 < len(flat) else '', 'n', False)
                    if q in VELAR:
                        p = 'ŋ'
                    elif q in ('b', 'p', 'm'):
                        p = 'm'
            # 음절 안 자리
            syl = syls[si]
            pos_in = [k for k, (gg, kk) in enumerate(syl) if kk == 'C']
            first_v = next((k for k, (gg, kk) in enumerate(syl) if kk == 'V'), len(syl))
            here = idx - sum(len(s) for s in syls[:si])
            if here > first_v:
                place = 'coda'
            elif here > 0 and syl[here - 1][1] == 'C':
                place = 'cluster'
            else:
                place = 'onset'
            for ph in (['k', 's'] if p == 'ks' else [p]):
                phones.append([ph, si, place, prev, ''])
                prev = ph
        else:
            phones.append([g, si, 'V', prev, ''])
            prev = g
    # 모음: 핵 하나에 모음이 여럿이면 센 모음(약한 둘이면 뒤)이 핵, 나머지는 반모음
    by_syl = {}
    for i, ph in enumerate(phones):
        if ph[2] == 'V':
            by_syl.setdefault(ph[1], []).append(i)
    for si, idxs in by_syl.items():
        letters = [phones[i][0] for i in idxs]
        strong = [k for k, l in enumerate(letters) if l in STRONG]
        core = strong[0] if strong else len(letters) - 1
        for k, i in enumerate(idxs):
            l = letters[k]
            if k == core:
                phones[i][0] = ACC.get(l, 'i' if l == 'y' else l)
                phones[i][2] = 'nucleus'
            else:
                phones[i][0] = 'j' if l in ('i', 'y') else 'w'
                phones[i][2] = 'glide'
    for i in range(len(phones)):
        phones[i][3] = phones[i - 1][0] if i else ''
        phones[i][4] = phones[i + 1][0] if i + 1 < len(phones) else ''
    # 발음기호
    parts = [''] * len(syls)
    for ph in phones:
        parts[ph[1]] += ph[0]
    ipa = ''.join(('ˈ' if i == st and len(syls) > 1 else '') + p for i, p in enumerate(parts))
    # 음절 철자(h도 넣어서 보인다)
    return {'syl': spell_syllables(word, syls), 'stress': st, 'ipa': ipa, 'phones': [tuple(p) for p in phones], 'n': len(syls)}


def spell_syllables(word, syls):
    """음절 나누기를 원래 철자로(h 포함): hermano → her·ma·no"""
    w = word.lower()
    sizes = [sum(len(g) for g, _ in s) for s in syls]
    out, i = [], 0
    for n in sizes:
        piece = ''
        while n > 0 and i < len(w):
            if w[i] == 'h' and not (i > 0 and w[i - 1] == 'c'):
                piece += w[i]; i += 1; continue
            piece += w[i]; i += 1; n -= 1
        out.append(piece)
    if i < len(w):
        out[-1] += w[i:]
    # 낱말 첫 h는 첫 음절에, 음절 사이 h는 뒤 음절에 붙인다
    for k in range(len(out) - 1):
        if out[k].endswith('h') and not out[k].endswith('ch'):
            out[k], out[k + 1] = out[k][:-1], 'h' + out[k + 1]
    return out


# ---------- 발음 설명 (판정 넷) ----------
N = {
    'p': '[p] 한국어 ‘ㅍ’식으로 해도 된다 (무성 양순 파열음, voiceless bilabial plosive) — 차이: 바람을 거의 내지 않는다. ‘ㅃ’에 가깝다',
    't': '[t] 한국어 ‘ㅌ’식으로 해도 된다 (무성 치 파열음, voiceless dental plosive) — 차이: 혀끝을 윗니 뒤에 대고, 바람을 거의 내지 않는다. ‘ㄸ’에 가깝다',
    'k': '[k] 한국어 ‘ㅋ’식으로 해도 된다 (무성 연구개 파열음, voiceless velar plosive) — 차이: 바람을 거의 내지 않는다. ‘ㄲ’에 가깝다',
    'b0': '[b] 한국어 ‘ㅂ’식으로 하면 안 된다 (유성 양순 파열음, voiced bilabial plosive) — 목을 울리며 입술을 뗀다. 목에 손을 대고 떨리는지 본다 · 주의: 한국어 첫머리 ‘ㅂ’은 목이 안 울려 [p]로 들린다(vino 포도주 → pino 소나무)',
    'β': '[β] 한국어 ‘ㅂ’식으로 해도 된다 (유성 양순 접근음, voiced bilabial approximant) — 차이: 입술을 다 닫지 않고 살짝 띄운 채 부드럽게 낸다',
    'd0': '[d] 한국어 ‘ㄷ’식으로 하면 안 된다 (유성 치 파열음, voiced dental plosive) — 혀끝을 윗니 뒤에 대고 목을 울리며 낸다 · 주의: 한국어 첫머리 ‘ㄷ’은 목이 안 울려 [t]로 들린다(dos 둘 → tos 기침)',
    'ð': '[ð] 한국어 ‘ㄷ’식으로 해도 된다 (유성 치 접근음, voiced dental approximant) — 차이: 혀끝을 윗니에 살짝만 대고 소리를 흘린다. 낱말 끝에서는 아주 약하다',
    'ɡ0': '[ɡ] 한국어 ‘ㄱ’식으로 하면 안 된다 (유성 연구개 파열음, voiced velar plosive) — 목을 울리며 낸다 · 주의: 한국어 첫머리 ‘ㄱ’은 목이 안 울려 [k]로 들린다(goma 고무 → coma 쉼표)',
    'ɣ': '[ɣ] 한국어 ‘ㄱ’식으로 해도 된다 (유성 연구개 접근음, voiced velar approximant) — 차이: 혀뒤를 입천장에 붙이지 않고 가까이만 대서 부드럽게 흘린다',
    'x': '[x] 한국어 ‘ㅎ’식으로 해도 된다 (무성 연구개 마찰음, voiceless velar fricative) — 차이: 목 안쪽에서 혀뒤와 입천장 사이로 긁듯이 낸다. 멕시코는 이 소리, 카리브·중미·콜롬비아는 ‘ㅎ’에 가깝다',
    's': '[s] 한국어 ‘ㅅ’식으로 해도 된다 (무성 치경 마찰음, voiceless alveolar fricative) — 차이: 혀끝으로 좁게, ‘ㅆ’에 가깝게 낸다',
    'si': '[s] 한국어 ‘ㅅ’식으로 해도 된다 (무성 치경 마찰음, voiceless alveolar fricative) — 차이: 혀끝으로 좁게, ‘ㅆ’에 가깝게 낸다 · 주의: i 앞에서 한국어 ‘시’처럼 혀를 넓게 대면 [ʃ](‘쉬’)로 들린다',
    'f': '[f] 한국어 ‘ㅍ’식으로 하면 안 된다 (무성 순치 마찰음, voiceless labiodental fricative) — 윗니를 아랫입술에 가볍게 대고 그 틈으로 바람을 낸다 · 주의: ‘ㅍ’로 내면 [p]로 들린다(fila 줄 → pila 건전지)',
    'l': '[l] 한국어 ‘ㄹ’식으로 하면 안 된다 (치경 설측 접근음, alveolar lateral approximant) — 혀끝을 윗잇몸에 붙인 채 소리를 낸다. ‘ㄹㄹ’처럼(pelo ‘펠로’) · 주의: 혀끝을 [ɾ]처럼 튕기면 다른 말이 된다(pelo 머리카락 → pero 그러나)',
    'ɾ': '[ɾ] = 한국어 모음 사이 ‘ㄹ’ (치경 탄음, alveolar tap): 혀끝을 한 번 튕긴다',
    'ɾc': '[ɾ] 받침 ‘ㄹ’로 하면 안 된다 (치경 탄음, alveolar tap) — 혀끝을 윗잇몸에 한 번 튕긴다. 뒤에 ‘으’를 붙이지 않는다 · 주의: 받침 ‘ㄹ’은 [l]이라 다른 말이 된다(mar 바다 → mal 나쁘게)',
    'ɾk': '[ɾ] 한국어 ‘ㄹ’식으로 해도 된다 (치경 탄음, alveolar tap) — 차이: 앞 자음과 사이에 ‘으’를 넣지 않고 바로 튕긴다(tres는 한 음절)',
    'r': '[r] 한국어에 없는 소리 (치경 전동음, alveolar trill) — 혀끝을 윗잇몸 가까이 두고 바람으로 여러 번 떨게 한다 · 주의: 한 번만 튕기면 [ɾ]라 다른 말이 된다(perro 개 → pero 그러나)',
    'tʃ': '[tʃ] 한국어 ‘ㅊ’식으로 해도 된다 (무성 후치경 파찰음, voiceless postalveolar affricate) — 차이: 바람을 덜 낸다',
    'ʝ': '[ʝ] 한국어 ‘야·요’식으로 해도 된다 (유성 경구개 마찰음, voiced palatal fricative) — 차이: 혀를 입천장에 더 붙여 살짝 마찰을 낸다(‘쟈’ 쪽으로 조금). 아르헨티나·우루과이는 ‘샤’·‘쟈’처럼 낸다',
    'ɲ': '[ɲ] = 한국어 ‘냐·뇨’의 ‘ㄴ’ (경구개 비음, palatal nasal)',
    'ŋ': '[ŋ] = 한국어 받침 ‘ㅇ’ (연구개 비음, velar nasal): n이 [k]·[ɡ]·[x] 앞에서 이렇게 된다',
    'j': '[j] = 한국어 ‘야·예’의 반모음 (경구개 접근음, palatal approximant)',
    'w': '[w] = 한국어 ‘와·웨’의 반모음 (양순 연구개 접근음, labial-velar approximant)',
    'o': '[o] 한국어 ‘오’식으로 해도 된다 — 차이: 입술을 덜 오므리고 입을 조금 더 연다',
    'ˈ': '[ˈ] 바로 뒤 음절에 강세 — 그 음절을 더 세고 조금 길게 낸다. 강세 자리가 바뀌면 다른 말이 된다(papa 감자 / papá 아빠)',
}


def notes(word, stress_note=False):
    """그 낱말에 나오는 소리 차례로 설명(같은 것은 한 번)."""
    a = analyse(word)
    out, seen = [], set()

    def add(key, text=None):
        if key not in seen:
            seen.add(key); out.append(text or N[key])
    for ph, si, place, prev, nxt in a['phones']:
        first = prev == ''
        if ph in ('p', 't', 'k', 'β', 'ð', 'ɣ', 'x', 'f', 'tʃ', 'ʝ', 'ɲ', 'ŋ', 'j', 'w', 'o', 'r'):
            add(ph)
        elif ph == 'b' and first:
            add('b0')
        elif ph == 'd' and first:
            add('d0')
        elif ph == 'ɡ' and first:
            add('ɡ0')
        elif ph == 's':
            # i 앞의 s가 하나라도 있으면 '주의'가 붙은 설명 하나로 둔다
            if nxt in ('i', 'j') and 's' in seen and 'si' not in seen:
                out[out.index(N['s'])] = N['si']; seen.add('si')
            elif not ({'s', 'si'} & seen):
                add('si' if nxt in ('i', 'j') else 's')
        elif ph == 'l' and place == 'onset':
            add('l')
        elif ph == 'ɾ':
            add('ɾc' if place == 'coda' else 'ɾk' if place == 'cluster' else 'ɾ')
    if stress_note and a['n'] > 1:
        add('ˈ')
    # 음절: 자음만 있는 자리(음절 끝 s·ð, 자음 둘로 여는 음절)
    if any((place == 'coda' and ph in ('s', 'ð', 'k')) or place == 'cluster' for ph, si, place, *_ in a['phones']):
        add('syl', f"음절 {a['n']}개: {'·'.join(a['syl'])} — 자음만 있는 자리에 ‘으’를 넣지 않는다. 음절이 늘면 다른 말처럼 들린다")
    return out


TESTS = {
    'mesa': 'ˈmesa', 'luna': 'ˈluna', 'sol': 'sol', 'pan': 'pan', 'pelo': 'ˈpelo', 'fiesta': 'ˈfjesta', 'tomate': 'toˈmate',
    'nada': 'ˈnaða', 'dedo': 'ˈdeðo', 'tres': 'tɾes', 'siete': 'ˈsjete', 'planta': 'ˈplanta', 'semana': 'seˈmana',
    'casa': 'ˈkasa', 'queso': 'ˈkeso', 'clase': 'ˈklase', 'cuatro': 'ˈkwatɾo', 'parque': 'ˈpaɾke',
    'gato': 'ˈɡato', 'amigo': 'aˈmiɣo', 'tengo': 'ˈteŋɡo', 'grande': 'ˈɡɾande', 'seguir': 'seˈɣiɾ', 'juguete': 'xuˈɣete',
    'guitarra': 'ɡiˈtara', 'agua': 'ˈaɣwa', 'paraguas': 'paˈɾaɣwas', 'pingüino': 'piŋˈɡwino', 'bilingüe': 'biˈliŋɡwe',
    'jugo': 'ˈxuɣo', 'viejo': 'ˈbjexo', 'mujer': 'muˈxeɾ', 'joven': 'ˈxoβen', 'gente': 'ˈxente', 'gigante': 'xiˈɣante',
    'colegio': 'koˈlexjo', 'girasol': 'xiɾaˈsol',
    'cena': 'ˈsena', 'cielo': 'ˈsjelo', 'ciudad': 'sjuˈðað', 'cinco': 'ˈsiŋko', 'once': 'ˈonse', 'zapato': 'saˈpato',
    'azul': 'aˈsul', 'plaza': 'ˈplasa', 'cerveza': 'seɾˈβesa', 'diez': 'djes', 'vez': 'bes',
    'vaca': 'ˈbaka', 'bueno': 'ˈbweno', 'beber': 'beˈβeɾ', 'nueve': 'ˈnweβe', 'verde': 'ˈbeɾðe', 'ventana': 'benˈtana',
    'hola': 'ˈola', 'hijo': 'ˈixo', 'hermano': 'eɾˈmano', 'huevo': 'ˈweβo', 'ahora': 'aˈoɾa', 'hoy': 'oj', 'hambre': 'ˈambɾe',
    'historia': 'isˈtoɾja',
    'pero': 'ˈpeɾo', 'perro': 'ˈpero', 'carro': 'ˈkaro', 'tierra': 'ˈtjera', 'arroz': 'aˈros', 'rosa': 'ˈrosa',
    'sonrisa': 'sonˈrisa', 'rubio': 'ˈruβjo', 'ruido': 'ˈrwiðo', 'mar': 'maɾ', 'flor': 'floɾ', 'calor': 'kaˈloɾ',
    'llave': 'ˈʝaβe', 'lluvia': 'ˈʝuβja', 'calle': 'ˈkaʝe', 'yo': 'ʝo', 'ayer': 'aˈʝeɾ', 'playa': 'ˈplaʝa',
    'niño': 'ˈniɲo', 'mañana': 'maˈɲana', 'señor': 'seˈɲoɾ', 'español': 'espaˈɲol', 'noche': 'ˈnotʃe',
    'camisa': 'kaˈmisa', 'martes': 'ˈmaɾtes', 'naranja': 'naˈɾaŋxa', 'imagen': 'iˈmaxen', 'volumen': 'boˈlumen',
    'papel': 'paˈpel', 'hablar': 'aˈβlaɾ', 'feliz': 'feˈlis', 'verdad': 'beɾˈðað', 'pared': 'paˈɾeð',
    'café': 'kaˈfe', 'también': 'tamˈbjen', 'canción': 'kanˈsjon', 'avión': 'aˈβjon', 'inglés': 'iŋˈɡles',
    'adiós': 'aˈðjos', 'jamón': 'xaˈmon', 'ratón': 'raˈton', 'francés': 'fɾanˈses',
    'lápiz': 'ˈlapis', 'árbol': 'ˈaɾβol', 'fácil': 'ˈfasil', 'difícil': 'diˈfisil', 'azúcar': 'aˈsukaɾ',
    'música': 'ˈmusika', 'sábado': 'ˈsaβaðo', 'teléfono': 'teˈlefono', 'médico': 'ˈmeðiko', 'pájaro': 'ˈpaxaɾo',
    'plátano': 'ˈplatano', 'miércoles': 'ˈmjeɾkoles',
    'día': 'ˈdia', 'país': 'paˈis', 'río': 'ˈrio', 'qué': 'ke', 'cómo': 'ˈkomo', 'dónde': 'ˈdonde', 'cuándo': 'ˈkwando',
    'quién': 'kjen', 'cuánto': 'ˈkwanto', 'tú': 'tu', 'él': 'el', 'mí': 'mi',
}

if __name__ == '__main__':
    bad = 0
    for w, want in TESTS.items():
        got = analyse(w)['ipa']
        if got != want:
            bad += 1
            print('다름', w, got, '← 기대', want)
    print('발음기호 검사', len(TESTS), '개 중 다름', bad)
    for w in ('hermano', 'ahora', 'historia', 'fiesta', 'tres', 'dos', 'perro', 'cine', 'pelo', 'bilingüe', 'mar'):
        a = analyse(w)
        print(w, '·'.join(a['syl']), a['ipa'])
        for n in notes(w, True):
            print('   ', n[:70])
