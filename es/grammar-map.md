# 빨라고양 문법 지도 0.1

갱신: 2026-11-08. 원본은 [grammar-map.json](grammar-map.json)이고, 이 문서는 `python3 -I es/grammar-page.py es/grammar-map.json --md es/grammar-map.md`로 다시 만든다(손으로 고치지 않는다).

FÁBULA 예문을 놓는 문법 차례(PRINCIPLES 0-1 5번). Claude가 PCIC 2장 문법(2006)의 수준 배치를 참고해 중남미 기준으로 짰다. PCIC 문구는 옮기지 않고 절 번호만 적는다. 보기 문장은 Claude가 쓴 것이다.

## 쓰는 규칙

- **차례.** 띠(0세트 → A1 → A2 → B1 → B2 → C1) 안의 번호 차례로 처음 소개한다. 처음 소개하는 카드의 해설에 규칙 한 줄을 쓰고, 뒤 예문에서 다시 만나게 한다(보카고양 12절).
- **예문 통제.** 예문에는 그 세트까지 소개한 항목과 아래 덩어리만 쓴다. 아직 나오지 않은 문법은 쓰지 않는다(고양공유 0절).
- **덩어리 먼저.** 회화에 꼭 필요한 정해진 말은 문법보다 먼저 통째로 쓴다. 해설에 '통째로 외우는 말'이라 하고, 그 문법이 나오는 항목에서 다시 짚는다. 목록 밖의 덩어리는 쓰지 않는다. 덩어리를 더할 때는 이 목록에 먼저 적는다.
- **첫 소개와 반복.** 첫 소개는 전형적인 낱말 하나로 하고, 반복은 매번 다른 낱말 · 새 문장으로 고르게 한다(보카고양 12절, Year & Gordon 2009).
- **중남미 기본값.** PRINCIPLES 0-1 3번을 따른다: vosotros 없음, ustedes 하나, 단순과거 먼저, 미래는 ir a 먼저, 접속법 과거는 -ra, 작게 말하기(-ito) 일찍. 에스파냐 꼴(vosotros, 현재완료로 말하는 오늘 일, leísmo)은 해설 표시로만 둔다.
- **한국어 비교.** 도움이 될 때만 해설 한 줄로 쓴다(보카고양 4절): gustar의 방향, 목적 대명사의 자리, 이중 부정, 주어 빼기.
- **세트 번호.** 세트 번호와 이정표(A1~B2 상당) 위치는 FÁBULA 후보를 뽑을 때 정한다(PRINCIPLES 0-1 12번 3단계). 지금은 띠와 차례만 정한다.
- **원장 문장과 잇기.** 다음 일(원장 585칸 스페인어 문장)에서 문장마다 쓴 문법 항목 id를 단다(`grammar`). 그 문장은 그 항목이 모두 소개된 세트부터 놓는다. A 칸이라도 단순과거를 쓰면 A2-09 뒤다.

## PCIC와 다르게 둔 것

- **단순과거를 현재완료보다 먼저 (A2-09 → A2-16).** PCIC는 세 과거를 모두 A2에 둔다. 중남미 기본값(PRINCIPLES 0-1 3번).
- **para que + 접속법을 B1로 (B1-14).** PCIC는 B2. quiero que와 같은 짜임이라 함께 익힌다.
- **tú 명령 · usted 명령 · 접속법 인사를 덩어리로 먼저.** PCIC는 명령을 A2, 접속법을 B1에 둔다. 길 묻기 · 헤어질 때 인사 같은 원장 A 칸에 필요하다.
- **vosotros 전부, leísmo.** 에스파냐 꼴이라 가르치지 않는다. 해설 표시로만 둔다.
- **접속법 과거는 -ra 꼴 (B2-01).** PCIC는 -ra · -se 두 꼴을 함께 둔다. 중남미는 -ra가 훨씬 많다.
- **작게 말하기 -ito (A2-30).** PCIC 2장에는 따로 칸이 없다. 중남미 입말에 아주 잦다.
- **vos 알아듣기 (B1-28).** PCIC는 중남미 꼴로 표시만 한다. 쓰지 않고 알아보게만 한다.

## 0세트 (17항목)

기초 중의 기초. FABLE 0세트처럼 가장 기초 문법의 초석이다. 동사는 나 · 너 · 그 꼴과 원형 자리만 쓴다.

- **0-01 sí · no, 동사 앞 부정 no** — Sí. / No, gracias. / No sé.
  - 한국어: no는 동사 바로 앞에 온다. 한국어 '안'과 자리가 같다(No como carne = 고기 안 먹어).
  - PCIC 2장 8.2, 13.3
- **0-02 나 · 너: yo, tú (주어는 흔히 뺀다)** — Yo soy Youngsin Choi. / ¿Y tú?
  - 한국어: 주어를 자주 빼는 것은 한국어와 같다. 동사 끝이 누구인지 알려 준다.
  - PCIC 2장 7.1.1
- **0-03 ser 1: soy · eres · es (이름 · 출신 · 직업)** — Soy de Corea. / ¿Eres de México? / Es profesora.
  - 한국어: '~이다'에 가깝다.
  - PCIC 2장 12.1, 12.2.1
- **0-04 명사의 성과 관사: el / la, un / una** — el gato, la casa / un libro, una mesa / el día, la mano, el problema
  - 덧붙임: -o는 남성, -a는 여성이 기본이고 예외는 만날 때마다 짚는다. 모든 명사에 따라붙어 맨 처음부터 매번 본다. 정답 화면에 el/la를 늘 보인다(PRINCIPLES 0-1 4번).
  - PCIC 2장 1.2, 3.1, 3.2
- **0-05 복수: -s / -es, los / las, unos / unas** — los gatos / las ciudades / unos amigos
  - PCIC 2장 1.3, 2.3
- **0-06 형용사: 명사 뒤에, 성 · 수를 맞춘다** — un perro grande / una casa blanca / los zapatos negros / Choi Hyuk es coreano. / Lee Soyeon es coreana.
  - 한국어: 한국어와 반대로 꾸미는 말이 뒤에 온다.
  - PCIC 2장 2.2, 2.4, 10.3
- **0-07 estar 1: 있는 곳** — Estoy en casa. / ¿Dónde está el baño?
  - 한국어: '(어디에) 있다'.
  - 덧붙임: estar는 장소부터 연다. 학습자는 estar를 장소에 먼저, 상태 형용사에 나중에 바르게 쓴다(VanPatten 1987).
  - PCIC 2장 12.1
- **0-08 hay: 있다 · 없다 (존재)** — Hay un gato en la mesa. / No hay agua.
  - 덧붙임: hay는 꼴이 하나다. 하나여도 여럿이어도 hay.
  - PCIC 2장 3.3, 13.3
- **0-09 묻는 말: ¿?, qué · quién · dónde · cómo · cuándo · cuánto** — ¿Qué es esto? / ¿Quién es? / ¿Cómo estás?
  - 덧붙임: 물음표를 앞에도 거꾸로 쓴다(¿). 묻는 말에는 악센트를 찍는다(qué / que).
  - PCIC 2장 7.3, 8.8, 13.3
- **0-10 por qué · porque** — ¿Por qué? —Porque sí.
  - 덧붙임: 띄어 쓰고 악센트를 찍으면 '왜', 붙여 쓰고 악센트가 없으면 '왜냐하면'.
  - PCIC 2장 8.9, 15.3.4
- **0-11 y · o · pero** — ¿Café o té? / Es pequeño, pero bonito.
  - PCIC 2장 14.1, 14.2, 14.3
- **0-12 이것 · 여기: este / esta / esto, aquí · acá, allí · allá** — Esta es mi casa. / Estoy aquí. / ¿Qué es eso?
  - 중남미: acá · allá를 aquí · allí만큼, 곳에 따라 더 많이 쓴다. 둘 다 표제어로 둔다.
  - 덧붙임: PCIC 4장(지시사).
  - PCIC 2장 8.2
- **0-13 내 · 네 · 그의: mi / tu / su (복수 mis / tus / sus)** — mi mamá / tu casa / sus hijos
  - 덧붙임: PCIC 5장(소유사).
- **0-14 기초 전치사: de · en · a · con · para (al · del)** — Soy de Corea. / Estoy en Goyang. / café con leche / Es para mi mamá. / la casa del profesor
  - 덧붙임: de는 출신 · 소유, a + el = al, de + el = del. PCIC 2장에는 전치사 장이 따로 없다.
- **0-15 원형 자리: quiero · puedo · tengo que · voy a + 원형 (나 · 너 꼴)** — Quiero comer. / ¿Puedes venir? / Tengo que trabajar. / Voy a dormir.
  - 덧붙임: PRINCIPLES 0-1 4번: 활용을 배우기 전에도 자연스러운 문장을 쓰려고 맨 앞에 둔다. 빈칸은 원형에 둔다. 동사 꼴(quiero · puedes)은 A2-01에서 체계가 된다.
  - PCIC 2장 12.1, 15.1.1
- **0-16 gustar 1: me gusta / te gusta + 단수 명사 · 원형** — Me gusta el café. / ¿Te gusta bailar?
  - 한국어: "나는 커피가 좋아"와 같은 방향이다(커피가 주어). 영어 I like coffee보다 한국어가 가깝다.
  - 덧붙임: gustar 뒤 명사에는 관사를 붙인다(Me gusta el café, 관사 없이는 틀림).
  - PCIC 2장 7.1.3, 12.1, 12.2.3, 3.3
- **0-17 muy · mucho · un poco, también · tampoco** — Muy bien. / Mucho gusto. / Yo también. / Yo tampoco.
  - PCIC 2장 6.1, 6.2, 11.2

## A1 (22항목)

현재 시제와 사람별 꼴, ser · estar · hay, gustar, 관사.

- **A1-01 규칙 현재 -ar: 나 · 너 · 그 (hablo, hablas, habla)** — Hablo un poco de español. / ¿Hablas coreano?
  - 덧붙임: 사람별 꼴을 한꺼번에 주지 않고 나 · 너 · 그 셋부터 연다. 회화 대부분이 이 셋이다.
  - PCIC 2장 9.1.1
- **A1-02 규칙 현재 -er · -ir (como, vives, escribe)** — Como arroz. / ¿Dónde vives?
  - PCIC 2장 9.1.1
- **A1-03 usted: 높임 '당신 · 선생님', 꼴은 그(él)와 같다** — ¿Usted es la profesora? / ¿Cómo está usted?
  - 중남미: 콜롬비아 등에서는 가까운 사이에도 usted를 쓴다(해설).
  - 한국어: 높임말 자리지만 동사 꼴 하나로 높인다.
  - PCIC 2장 7.1.1, 13.1
- **A1-04 우리 · 그들 · 여러분: nosotros, ellos / ellas, ustedes** — Hablamos coreano. / ¿Ustedes hablan inglés?
  - 중남미: vosotros는 쓰지 않는다. ustedes가 '너희'와 '여러분'을 함께 맡는다.
  - PCIC 2장 7.1.1, 9.1.1
- **A1-05 자주 쓰는 불규칙 1: ser · estar · ir · tener 모든 사람 꼴** — somos, son / vamos, van / tenemos, tienen
  - PCIC 2장 9.1.1
- **A1-06 tener: 가지다 · 나이 · 배고픔** — Tengo dos hermanos. / Tengo treinta años. / Tengo hambre.
  - 한국어: '배고프다'를 '배고픔을 가지다'로 말한다.
  - PCIC 2장 12.2.2
- **A1-07 estar 2: 지금 어떤 상태** — Estoy cansado. / La tienda está cerrada.
  - PCIC 2장 9.4.3, 12.2.1
- **A1-08 ser · estar 가르기: 어떤 사람 · 것(ser) / 지금 상태(estar)** — Mi papá es alto. / Hoy mi papá está cansado.
  - 한국어: ser는 '~이다', estar는 '(어디) 있다 · (지금) ~하다'로 잡으면 대부분 맞는다.
  - PCIC 2장 12.1
- **A1-09 hay · estar 가르기** — Hay un banco cerca. / El banco está cerca.
  - 덧붙임: 처음 말하는 것은 hay + un, 이미 아는 것은 el + está.
  - PCIC 2장 3.3, 13.3
- **A1-10 관사 쓰임: 처음 말하는 것 un, 아는 것 el, 물질 · 복수는 관사 없이** — Tengo un perro. El perro es negro. / Hay agua. / Quiero café.
  - 한국어: 한국어에 없는 표시라 예문에서 매번 본다(보카고양 12절 '꼭 표시하게 하는 것'과 같은 무게).
  - PCIC 2장 3.1, 3.2, 3.3
- **A1-11 gustar 2: me / te / le / nos / les + gusta · gustan** — Me gustan los perros. / A mi hermano le gusta el fútbol. / A mí también.
  - 한국어: 좋아하는 대상이 여럿이면 gustan이다. 대상이 주어라서다.
  - PCIC 2장 7.1.3, 12.2.3
- **A1-12 시각 · 요일: es la una, son las dos, el lunes / los lunes** — Son las dos. / La clase es a las tres. / Los lunes trabajo.
  - 덧붙임: 시각은 ser. 요일 앞 el은 그 요일에, los는 그 요일마다.
  - PCIC 2장 3.1, 12.1
- **A1-13 재귀동사 1: me llamo, levantarse, ducharse** — Me llamo Lee Soyeon. / Me levanto a las siete.
  - 중남미: PCIC는 중남미가 재귀꼴을 더 쓰는 경향을 적는다(regresarse, enfermarse).
  - 한국어: '스스로를'이 붙는 동사로 본다.
  - PCIC 2장 7.1.4, 13.3
- **A1-14 묻는 말 2: cuál, cuántos / cuántas, de dónde, a qué hora** — ¿Cuál es tu nombre? / ¿Cuántos años tienes? / ¿De dónde eres?
  - PCIC 2장 7.3, 8.8
- **A1-15 que 관계절 1: 명사 + que + 현재** — el libro que leo / la chica que canta
  - 한국어: 한국어(내가 읽는 책)와 반대로 꾸미는 절이 뒤에 온다.
  - PCIC 2장 7.2, 15.2
- **A1-16 creo que + 직설법** — Creo que es caro.
  - PCIC 2장 15.1.2
- **A1-17 para + 원형(목적), porque(이유)** — Estudio español para viajar. / No voy porque estoy cansado.
  - PCIC 2장 15.3.4, 15.3.5
- **A1-18 원형 자리 2: querer · poder · tener que · ir a · necesitar, 모든 사람 꼴** — ¿Quieren venir? / Vamos a comer. / Necesito dormir.
  - 중남미: 미래는 ir a + 원형이 기본이다. PCIC도 미래형 칸에 중남미는 다른 짜임을 더 쓴다고 적었다.
  - PCIC 2장 12.1, 15.1.1
- **A1-19 목적어 me · te (나를 · 나에게 · 너를)** — ¿Me ayudas? / Te quiero.
  - 한국어: 한국어처럼 동사 앞에 온다.
  - PCIC 2장 7.1.2, 7.1.3
- **A1-20 수와 일치: uno → un / una, 21~100** — un café / veintiún años / cien pesos
  - PCIC 2장 6.1
- **A1-21 mucho · poco · bastante (양)과 muy (정도)** — Tengo mucho trabajo. / Es muy bueno. / Hay poca gente.
  - PCIC 2장 6.1, 11.2
- **A1-22 ni: no ... ni** — No como carne ni pescado.
  - PCIC 2장 14.1

## A2 (33항목)

과거(단순과거 → 불완료과거 → 현재완료), 목적 대명사, tú 명령, 비교, 조건 1.

- **A2-01 모음이 바뀌는 현재: e → ie, o → ue, e → i** — quiero, queremos / puedo, duermo / pido
  - 덧붙임: 0-15의 quiero · puedo가 여기서 체계가 된다. 우리 꼴(queremos)은 바뀌지 않는다.
  - PCIC 2장 9.1.1
- **A2-02 나 꼴만 다른 동사: hago, pongo, salgo, traigo, conozco, sé, doy, veo** — Hago la tarea. / No sé. / Salgo a las ocho.
  - PCIC 2장 9.1.1
- **A2-03 날씨: hace calor · frío, llueve** — Hace calor. / Hoy llueve mucho.
  - PCIC 2장 13.3
- **A2-04 estar + 현재분사 (진행)** — Estoy comiendo. / ¿Qué estás haciendo?
  - PCIC 2장 9.4.2, 12.1
- **A2-05 사람 목적어 앞 a** — Veo a Lucía. / Conozco a tu hermano.
  - PCIC 2장 12.2.2
- **A2-06 목적 대명사 lo · la · los · las, 원형 · 현재분사 뒤에 붙이기** — ¿El libro? Lo tengo. / Quiero verlo.
  - 한국어: 동사 앞 자리가 한국어 어순(그걸 가지고 있어)과 같다.
  - PCIC 2장 7.1.2, 12.2.2
- **A2-07 간접 목적 le · les, a + 사람과 겹쳐 쓰기** — Le doy el libro a mi mamá.
  - 덧붙임: a mi mamá가 있어도 le를 쓴다.
  - PCIC 2장 7.1.3, 12.2.3
- **A2-08 gustar처럼 쓰는 동사: encantar, interesar, doler, parecer, importar** — Me duele la cabeza. / Me encanta. / ¿Qué te parece?
  - PCIC 2장 7.1.3, 12.2.3
- **A2-09 단순과거 1: 규칙 (llegué, comí, viviste)** — Ayer llegué tarde. / Hoy comí tacos.
  - 중남미: 과거 가운데 맨 먼저 연다(PRINCIPLES 0-1 3번). 오늘 일도 단순과거로 말한다.
  - 덧붙임: 첫 예문은 끝이 있는 동사(llegar, terminar, comprar)로 쓴다. 학습자는 단순과거를 이런 동사에서 먼저 쓴다(상 가설, Andersen & Shirai 1994).
  - PCIC 2장 9.1.3
- **A2-10 단순과거 2: 불규칙 fui(ser · ir 같음), tuve, estuve, hice, pude, dije, vine** — Fui a México. / No pude dormir.
  - PCIC 2장 9.1.3
- **A2-11 hace + 기간(~ 전), desde** — Llegué hace dos años. / Vivo aquí desde 2020.
  - PCIC 2장 15.3.1
- **A2-12 비교: más / menos ... que, tan ... como, mejor · peor · mayor · menor** — Es más alto que yo. / Es tan caro como el otro.
  - PCIC 2장 2.5, 15.3.8
- **A2-13 가장: el / la más ..., -ísimo** — Es el más alto. / Está riquísimo.
  - PCIC 2장 2.5
- **A2-14 불완료과거: 지난날의 습관 · 모습 (era, iba, había)** — Cuando era niño, vivía en el campo. / Había mucha gente.
  - 한국어: '~곤 했다 · ~였다'.
  - 덧붙임: 첫 예문은 상태 동사(ser, estar, tener, haber)로 쓴다(상 가설).
  - PCIC 2장 9.1.2
- **A2-15 단순과거와 불완료과거: 장면과 사건** — Llovía cuando llegué.
  - PCIC 2장 9.1.2, 9.1.3
- **A2-16 현재완료: 경험 · 아직 · 벌써** — ¿Has estado en México? / Todavía no he comido.
  - 중남미: 좁게 쓴다. 오늘 · 조금 전 일은 단순과거(Hoy comí)이고, 현재완료는 경험(alguna vez, nunca)과 '아직 · 벌써'에 둔다.
  - PCIC 2장 9.1.6
- **A2-17 과거분사 불규칙: hecho, dicho, visto, escrito, puesto, vuelto, abierto, roto** — ¿Lo has visto? / La puerta está abierta.
  - PCIC 2장 9.4.3
- **A2-18 tú 명령: habla, come, ven, ten, pon, sal, haz, di, ve, sé + 대명사 붙이기** — Habla más despacio. / Ven acá. / Dime. / Ayúdame.
  - 덧붙임: ven · mira · espera · dime는 A1부터 덩어리로 쓰고, 여기서 체계가 된다.
  - PCIC 2장 9.3
- **A2-19 cuando + 직설법, antes de / después de + 원형** — Cuando llego a casa, como. / Antes de comer, me lavo las manos.
  - PCIC 2장 15.3.1
- **A2-20 si + 현재 → 현재 · ir a · 명령 (조건 1)** — Si llueve, no voy. / Si quieres, te llamo.
  - 덧붙임: si(만약)와 sí(응)는 악센트로 가른다(PRINCIPLES 0-1 4번).
  - PCIC 2장 15.3.6
- **A2-21 순서 · 결과의 말: primero, después, luego, por eso, entonces** — Primero como y después salgo. / Estaba cansado, por eso no fui.
  - PCIC 2장 8.4, 15.3.7
- **A2-22 -mente 부사** — rápidamente / normalmente
  - 덧붙임: 여성꼴에 붙인다(rápida + mente).
  - PCIC 2장 8.1
- **A2-23 소유 강세형: mío, tuyo, suyo, nuestro** — ¿Es tuyo? —Sí, es mío.
  - 덧붙임: PCIC 5장(소유사).
- **A2-24 지시 셋과 시간: este · ese · aquel, esta tarde** — Esta tarde voy al cine. / Ese día llovía.
  - 덧붙임: PCIC 4장(지시사).
- **A2-25 감탄: ¡Qué ...!** — ¡Qué bonito! / ¡Qué bien! / ¡Qué frío!
  - PCIC 2장 7.4
- **A2-26 없음의 말과 이중 부정: nada, nadie, nunca, ningún** — No veo a nadie. / No quiero nada.
  - 한국어: 한국어 '아무도 안 봐'처럼 부정을 두 번 쓴다. 영어(I don't see anybody)보다 한국어가 가깝다.
  - PCIC 2장 6.1
- **A2-27 todo · otro · cada** — todos los días / otra vez / cada semana
  - PCIC 2장 6.1
- **A2-28 hay que + 원형** — Hay que pagar aquí.
  - PCIC 2장 9.4.1
- **A2-29 원형과 짝짓는 동사: empezar a, volver a, acabar de, dejar de, tener ganas de** — Acabo de llegar. / Dejé de fumar. / Tengo ganas de dormir.
  - PCIC 2장 12.1
- **A2-30 작게 · 귀엽게: -ito / -ita** — un cafecito / un momentito / ahorita
  - 중남미: 중남미에서 아주 자주 쓴다. ahorita는 멕시코 등에서 '지금 바로'와 '조금 있다가'로 갈린다(해설).
- **A2-31 ser de (재료 · 출신 · 주인), ser para** — La mesa es de madera. / Este regalo es para Lucía.
  - PCIC 2장 12.1
- **A2-32 전치사 뒤 대명사: mí, ti, conmigo, contigo** — para mí / ¿Vienes conmigo?
  - PCIC 2장 7.1.6
- **A2-33 por 1: 시간대 · 지나는 곳 · 수단** — por la mañana / por el parque / por teléfono
  - 덧붙임: por / para 정리는 B1-23.

## B1 (28항목)

미래형 · 조건형, 접속법 현재와 그 쓰임, 대명사 둘, se.

- **B1-01 미래형: 규칙과 불규칙(tendré, podré, haré, diré, saldré, vendré)** — Mañana lloverá. / Te llamaré.
  - 중남미: 일상 계획은 ir a(A1-18)가 기본이고, 미래형은 예측 · 약속 · 글말에 많다.
  - PCIC 2장 9.1.4
- **B1-02 미래형으로 짐작하기** — ¿Dónde estará? / Tendrá treinta años.
  - PCIC 2장 9.1.4
- **B1-03 조건형: 공손 · 바람 · 조언** — ¿Podrías ayudarme? / Me gustaría ir. / Deberías descansar.
  - 덧붙임: 덩어리로 먼저 쓴 me gustaría · ¿podría?가 여기서 체계가 된다.
  - PCIC 2장 9.1.5
- **B1-04 과거완료: había + 과거분사** — Cuando llegué, ya se había ido.
  - PCIC 2장 9.1.8
- **B1-05 접속법 현재 꼴: 규칙, 나 꼴에서 오는 불규칙, 아주 불규칙(sea, vaya, esté, sepa, haya, dé)** — hable, coma, viva / tenga, haga, diga / sea, vaya, esté
  - 덧붙임: 꼴을 한 항목으로 먼저 두고, 쓰임(B1-06~14)을 하나씩 연다.
  - PCIC 2장 9.2.1
- **B1-06 접속법 1: 바람 (quiero que, ojalá) — 주어가 다르면 접속법, 같으면 원형** — Quiero que vengas. / Quiero venir. / Ojalá llueva.
  - 한국어: '네가 오기를 바라'의 '-기를' 자리로 보면 쉽다.
  - PCIC 2장 9.2.1, 15.1.2
- **B1-07 접속법 2: 부탁 · 권고 (te pido que, es importante que)** — Te pido que me llames. / Es importante que descanses.
  - PCIC 2장 15.1.2
- **B1-08 접속법 3: 감정 (me alegra que, siento que)** — Me alegra que estés bien. / Siento que no puedas venir.
  - PCIC 2장 15.1.2
- **B1-09 접속법 4: 의심 (no creo que) / creo que + 직설법** — No creo que sea verdad. / Creo que es verdad.
  - PCIC 2장 15.1.2
- **B1-10 부정 명령: no + 접속법** — No hables. / No te preocupes.
  - 덧붙임: 덩어리 ¡No te preocupes!가 여기서 체계가 된다.
  - PCIC 2장 9.3
- **B1-11 usted · ustedes 명령 (접속법 꼴)** — Pase, por favor. / Siga derecho. / Disculpe.
  - 덧붙임: 덩어리 disculpe · pase · siga가 여기서 체계가 된다.
  - PCIC 2장 9.3
- **B1-12 대명사 둘: me lo, te la, se lo (le · les → se), 명령 · 원형 뒤에 붙이기** — Te lo doy. / Se lo di a mi mamá. / Dámelo.
  - 중남미: 중남미 입말은 '그들에게'를 se los로 나타내기도 한다(Se los dije). 알아보기만 한다.
  - PCIC 2장 7.1.4, 7.1.5
- **B1-13 cuando · hasta que + 접속법 (아직 일어나지 않은 때)** — Cuando llegues, llámame. / Espera hasta que vuelva.
  - PCIC 2장 15.3.1
- **B1-14 para que + 접속법** — Te lo digo para que lo sepas.
  - 덧붙임: PCIC는 B2에 둔다. quiero que(B1-06)와 같은 짜임(주어가 다르면 접속법)이라 앞당긴다.
  - PCIC 2장 15.3.5
- **B1-15 aunque + 직설법(사실), como(이유, 문장 앞)** — Aunque estoy cansado, voy. / Como no venías, empecé a comer.
  - PCIC 2장 15.3.4, 15.3.9
- **B1-16 al + 원형 (~할 때)** — Al llegar, te llamo.
  - PCIC 2장 15.3.1
- **B1-17 se 무인칭 · 수동** — Aquí se habla español. / Se venden carros.
  - PCIC 2장 7.1.4
- **B1-18 se 서로** — Nos conocimos en 2020. / Se quieren mucho.
  - PCIC 2장 7.1.4
- **B1-19 뜻하지 않은 일의 se: se me olvidó** — Se me olvidó. / Se me cayó el celular.
  - 한국어: '깜빡했다'처럼 일이 저절로 일어난 듯 말한다.
- **B1-20 관계사 2: lo que, donde, quien, el que / la que** — Lo que quiero es dormir. / la ciudad donde vivo
  - PCIC 2장 7.2, 15.2
- **B1-21 전하는 말 1: dice que + 직설법** — Dice que viene mañana. / Dicen que es bueno.
  - PCIC 2장 15.1.2
- **B1-22 ser · estar 2: 뜻이 갈리는 형용사** — ser listo / estar listo / ser aburrido / estar aburrido / ser rico / estar rico
  - PCIC 2장 12.1
- **B1-23 por · para 정리** — Gracias por todo. / Es para mañana. / Lo hago por ti.
  - 덧붙임: por는 이유 · 맞바꿈 · 대신 · 지나는 곳, para는 목적 · 받는 사람 · 기한 · 가는 곳.
  - PCIC 2장 15.3.4, 15.3.5
- **B1-24 현재분사와 짝짓는 동사: seguir, llevar + 기간** — Sigo estudiando. / Llevo dos años viviendo aquí.
  - 중남미: '여기 산 지 2년'은 현재완료보다 llevar나 hace ... que로 말하는 일이 많다.
  - PCIC 2장 12.1
- **B1-25 lo + 형용사: lo bueno, lo mejor** — Lo bueno es que no llueve. / Lo mejor es descansar.
  - PCIC 2장 2.6
- **B1-26 mientras, hasta que + 직설법(지난 일)** — Mientras como, veo la tele. / Esperé hasta que llegó.
  - PCIC 2장 15.3.1
- **B1-27 o sea, así que (결과)** — O sea, no puedes. / Estaba cansado, así que me fui a dormir.
  - PCIC 2장 15.3.7
- **B1-28 vos 알아듣기: vos sos, vos tenés, vení** — ¿Vos sos de acá?
  - 중남미: 아르헨티나 · 우루과이 등의 꼴이다. 쓰지 않고 알아보기만 한다(변종 표시).
  - PCIC 2장 9.1.1

## B2 (19항목)

접속법 과거 · 완료, 가정, 전하는 말 시제, 수동, 이음말.

- **B2-01 접속법 과거 꼴: -ra (fuera, tuviera, pudiera), -se는 알아보기만** — fuera, tuviera, pudiera, hiciera
  - 중남미: 중남미는 -ra 꼴이 훨씬 많다. 덩어리 quisiera가 여기서 체계가 된다.
  - PCIC 2장 9.2.2
- **B2-02 접속법 과거 쓰임: 지난 일 속 바람 · 부탁** — Quería que vinieras. / Me pidió que lo llamara.
  - PCIC 2장 9.2.2, 15.1.2
- **B2-03 si + 접속법 과거, 조건형 (지금 아닌 가정)** — Si tuviera tiempo, viajaría.
  - PCIC 2장 15.3.6
- **B2-04 ojalá + 접속법 과거, como si** — Ojalá pudiera. / Habla como si lo supiera todo.
  - PCIC 2장 9.2.2
- **B2-05 접속법 현재완료** — Espero que hayas descansado.
  - PCIC 2장 9.2.3
- **B2-06 미래완료 · 조건완료와 짐작** — Ya habrá llegado. / Yo lo habría hecho.
  - PCIC 2장 9.1.9, 9.1.10
- **B2-07 조건형으로 지난 일 짐작하기** — Serían las diez.
  - PCIC 2장 9.1.5
- **B2-08 접속법 과거완료: 지난 일의 가정 (si hubiera ..., habría ...)** — Si lo hubiera sabido, habría venido.
  - PCIC 2장 9.2.4, 15.3.6
- **B2-09 관계절 + 접속법 (정해지지 않은 대상)** — Busco a alguien que hable coreano. / No hay nadie que lo sepa.
  - PCIC 2장 15.2
- **B2-10 양보: aunque + 접속법, a pesar de que** — Aunque llueva, voy. / A pesar de que estaba cansado, vino.
  - PCIC 2장 15.3.9
- **B2-11 접속법을 부르는 이음말: antes de que, sin que, en cuanto, con tal de que, a menos que, en caso de que** — Llámame en cuanto llegues. / Salí sin que me vieran.
  - PCIC 2장 15.3.1, 15.3.6
- **B2-12 전하는 말 2: 시제 바꾸기** — Dijo que vendría. / Me preguntó si tenía tiempo.
  - PCIC 2장 15.1.2
- **B2-13 수동: ser + 과거분사(글말), estar + 과거분사(결과)** — La casa fue construida en 1990. / La puerta está cerrada.
  - PCIC 2장 12.1, 13.3
- **B2-14 강조: es ... donde, lo que más ... es** — Es aquí donde vivo. / Lo que más me gusta es leer.
  - PCIC 2장 7.2, 15.2
- **B2-15 이음말: sin embargo, además, en cambio, por lo tanto, es decir, de hecho** — Es caro; sin embargo, lo compro.
  - PCIC 2장 8.4, 8.5
- **B2-16 짝짓는 동사 3: llegar a, terminar + 현재분사, andar + 현재분사** — Llegué a pensar que no venías. / Anda buscando trabajo.
  - PCIC 2장 12.1
- **B2-17 동사가 정하는 전치사: pensar en, soñar con, depender de, acordarse de, casarse con** — Pienso en ti. / Depende de ti.
  - PCIC 2장 12.2.5
- **B2-18 서술 보어: Llegó cansado** — Llegó cansado. / La encontré dormida.
  - PCIC 2장 12.2.6
- **B2-19 다 해 버림의 se: comerse, tomarse** — Se comió toda la pizza. / Me tomé un café.
  - PCIC 2장 7.1.4

## C1 (10항목)

섞인 가정, 굳은 접속법, 분사 구문, 글말 이음말, 어순.

- **C1-01 섞인 가정: si hubiera ..., ahora sería ...** — Si hubiera estudiado, ahora sería médico.
  - PCIC 2장 15.3.6
- **C1-02 접속법 굳은 꼴: digan lo que digan, que yo sepa, sea como sea** — Que yo sepa, no viene. / Sea como sea, voy.
  - PCIC 2장 9.2.1
- **C1-03 분사 구문** — Terminada la reunión, salimos. / Siendo así, acepto.
  - PCIC 2장 9.4.2, 9.4.3
- **C1-04 글말 이음말: no obstante, por consiguiente, dado que, puesto que, siempre que + 접속법** — Te ayudo siempre que me lo pidas.
  - PCIC 2장 15.3.4, 15.3.6
- **C1-05 미래 · 조건형으로 맞서기: Será muy listo, pero ...** — Será muy listo, pero no escucha.
  - PCIC 2장 9.1.4, 9.1.5
- **C1-06 앞으로 꺼낸 말과 대명사 되받기** — A Mateo no lo conozco. / El café lo tomo sin azúcar.
  - PCIC 2장 13.2, 7.1.2
- **C1-07 lo + 형용사 + que (정도 강조)** — No sabes lo difícil que es.
  - PCIC 2장 2.6
- **C1-08 de + 원형완료 (조건)** — De haberlo sabido, habría venido.
  - PCIC 2장 15.3.6
- **C1-09 cuyo (글말 관계사)** — el autor cuyo libro leí
  - PCIC 2장 2.1.3
- **C1-10 el hecho de que + 접속법** — El hecho de que no llame me preocupa.
  - PCIC 2장 15.1.2

## 덩어리 (먼저 통째로 쓰는 말, 15개)

| 덩어리 | 처음 쓰는 띠 | 체계가 되는 항목 |
|---|---|---|
| Me llamo ... / ¿Cómo te llamas? | 0세트 | A1-13 |
| ¿Cómo estás? / ¿Cómo está? / ¿Qué tal? | 0세트 | A1-03 |
| Mucho gusto. / Encantado. · Encantada. | 0세트 | 0-06 |
| Por favor. / Gracias. / De nada. / Perdón. / Lo siento. | 0세트 | 굳은 말 |
| ¡Buen provecho! / ¡Salud! / ¡Felicidades! | 0세트 | 굳은 말 |
| ¿Aló? | 0세트 | 굳은 말 |
| No sé. / No entiendo. | 0세트 | A2-02 |
| ¿Me das ...? / ¿Me da ...? | A1 | A2-02 |
| Mira. / Oye. / Ven. / Espera. / Dime. | A1 | A2-18 |
| Disculpe. / Perdone. / Pase. / Siga derecho. | A1 | B1-11 |
| ¡Vamos! / ¡Vámonos! | A1 | B1-12 |
| No pasa nada. / ¡No te preocupes! | A2 | B1-10 |
| ¡Que te vaya bien! / ¡Que te mejores! / ¡Que descanses! / ¡Que tengas un buen día! | A2 | B1-06 |
| Me gustaría ... / ¿Podría ...? / ¿Podrías ...? | A2 | B1-03 |
| Quisiera ... | B1 | B2-01 |

## 출처

- PCIC 2장 문법 목록 A1-A2 · B1-B2 · C1-C2: https://cvc.cervantes.es/ensenanza/biblioteca_ele/plan_curricular/niveles/02_gramatica_inventario_a1-a2.htm (수준 배치 참고(비공개 사본))
