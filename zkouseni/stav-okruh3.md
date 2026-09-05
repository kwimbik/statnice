# Stav testovacího zkoušení — okruh 3 (Dobývání znalostí)

Poslední aktualizace: 3. 9. 2026, po kole 14. **Okruh projit na 100 %.**

> Vlastní soubor, protože `stav-zkouseni.md` patří paralelní větvi (okruhy 1 a 2) a přepisuje se
> celý — sekce pro okruh 3 se z něj jednou už ztratila.

## Pravidla

- Zdroj otázek **výhradně `03-dobyvani-znalosti.tex` / `.pdf`** (ENG/03-data-mining je totéž).
  Slidy v `materialy/` nejsou zdroj otázek, jen kontext. Látka značená `\mimo{}` / `\mimoq{}` se **zkouší také** (oprava 26. 8. 2026) — značka
  není vyřazení z rozsahu, jen signál nižší priority. Rozhoduje **rozsah v dokumentu**.
- **Váhu tématu měřit rozsahem podkapitoly.** Skript `secsize.py` (scratchpad) vypíše
  `\subsection`/`\subsubsection` seřazené podle počtu řádků a označí ty s `\mimo{}`.
  Vybírat největší dosud nedrilované bloky + 2–3 povinné retesty.
- **Hodnotit principy, ne názvosloví.** Váha pojmenování je úměrná váze konceptu: pojem s celou
  podsekcí se pojmenovat má, pojem zmíněný jednou větou se nehodnotí. Slití **dvou různých
  mechanismů** do jednoho se jako chyba počítá dál. (Korekce uživatele 25. 8. 2026.)
- Jedna otázka po druhé, počkat na odpověď, nikdy si neodpovídat sám.
- Hodnocení po každé odpovědi **max 3 věty, bez rovnic a LaTeXu** (v terminálu se nezobrazí).
- 5 bodů na otázku, po deseti otázkách tabulka skóre + vzorec chyb.
- Po každém kole zapsat **jen chyby a neznalosti** do `zkouseni/slabiny.md`, sekce „Okruh 3",
  ve formátu `pojem — v čem byla chyba — → kap. X.Y`.
- Otázky si dopředu nacachovat po deseti (scratchpad `kolo-NN.md`).

## Výsledky

| Kolo | Skóre |
|---|---|
| 1 | 35/50 = 70 % |
| 2 | 32,5/50 = 65 % |
| 3 | 35/50 = 70 % |
| 4 | 20/50 = 40 % |
| 5 | 27,5/50 = 55 % |
| 6 | 25/50 = 50 % |
| 7 | 21/50 = 42 % |
| 8 | 29/50 = 58 % |
| 9 | 28/50 = 56 % |
| 10 | 20/50 = 40 % |
| 11 | 26,5/50 = 53 % (konkrétní mechanika na malých příkladech) |
| 12 | 28,5/45 = 63 % (jen retesty; CLARA/CLARANS vyřazeno uživatelem) |
| 13 | 17,5/30 = 58 % (jen retesty; 4 otázky „ok"/vyřazeny) |
| 14 | 17,5/35 = 50 % (jen retesty; 3 vyřazeny) |

Sestupný trend kol 4–7 je z velké části artefakt výběru: od kola 4 jdou otázky systematicky po
dosud neprobrané látce. Skok v kole 8 souvisí s přechodem na hodnocení principů místo pojmů.

## Režim od kola 11

Nová látka došla — **okruh je projit celý**. Kola 11+ tedy skládat jako **náhodný mix napříč
celým dokumentem** (vážený rozsahem podkapitol) **plus povinné retesty**. Cílem už není pokrytí,
ale udržení.

## Povinné retesty do kola 11

1. **Standardizace atributů** (2.5) — nulový výsledek.
2. **Taxonomie metod detekce komunit** (6.16.1) — vymyslel si vlastní dělení.
3. **Osy ROC křivky** (5.2.5) — konstrukci umí, osy ne.
4. **Volba položek a taxonomie v MBA** (3.1.3).
5. **Fuzzy = stupeň pravdivosti, ne pravděpodobnost** (2.6.1 a 4.1) — zaměněno dvakrát v kole 10.
6. **Kritéria hodnocení metod mimo osu přesnosti** (5.2.1).

Splněné retesty (drží, dál nezkoušet): lift analýza (5.2.4), linkage (3.3.4), odhad chyby (5.2.2),
LR vs. LDA (3.2.5–6), matice záměn (5.2.3), modularita a null model (6.16),
Apriori / anti-monotonie (3.1.4), random forest (3.2.9).

**Zákonitost opakování (ověřeno v kolech 6, 8, 9):** první vysvětlení nedrží nikdy, druhé někdy,
třetí spolehlivě. Každý propadlý retest tedy plánovat na tři kola, ne doufat v jedno.

## Nedrilovaná látka

Evoluční konstrukce pravidel (4.4), aplikace spam/malware/doporučování (4.8), reprezentace
znalostí (5.1 — z větší části `\mimoq`), srovnání klasifikačních metod (3.2.10), zbytek taxonomie
detekce komunit (6.16.1), homofilie / výběr / sociální vliv (6.9), praktické nasazení a etika
(7.3), aplikace SNA (7.2), integrace a normalizace dat (2.4–2.5), CURE a k-medians (3.3.8).

## Diagnóza po deseti kolech

**Silné:** mechanika metod a algoritmické postupy (FP-Growth, k-means, Apriori, Louvain,
AdaBoost váhy), úvahové otázky, schopnost popsat princip vlastními slovy.

**Slabé, v pořadí podle ceny:**
1. **Druhá polovina otázky se vynechává** — pět kol v řadě (kola 4–7); v kole 8 slabší, ale
   nezmizelo. Největší jednotlivý zdroj ztrát.
2. **Dosazení sousedního pojmu se stejným povrchem** — „fuzzy" jako pravděpodobnost místo
   stupně pravdivosti, tři roviny vyhodnocení za tři role vizualizace, míry přesnosti místo
   kritérií jiného druhu, prohozené směry dvojic (C u SVM, dangling ↔ spider trap). Odpověď
   strukturně sedí, ale je to jiný pojem — u ústní zkoušky nejdražší, protože zní sebejistě.
3. **Procedura ano, důsledek v prostoru ne** — linkage (míry ano, tvary ne), stromy (extrakce
   ano, kvádry ne), LVQ (mechanika ano, co optimalizuje ne). U každé metody se vyplatí doplnit
   otázku „jak vypadá výsledek geometricky".
3. **Prohozené směry** — zná oba objekty dvojice, přiřadí je obráceně (C u SVM, dangling ↔
   spider trap, blízkostní centralita, věta o balanci). Zní sebejistě, proto drahé.
4. **Kapitola 5.2 (vyhodnocování modelů)** — nejtrvalejší obsahová mezera, padá od kola 1.
   Jedno vysvětlení nedrží, drží až **druhé** opakování téhož retestu (ověřeno v kolech 6 a 8).

## Po kole 11 (3. 9. 2026)

Kolo na žádost uživatele celé z **konkrétní mechaniky na malých číselných příkladech** (ne koncepty).
Splněné retesty: ROC osy (č. 3), fuzzy = stupeň příslušnosti (č. 5). **Propadlé:** standardizace
podle střední absolutní odchylky (č. 1, 2. propadnutí ⇒ plánovat ještě dvě kola), lift v decilu
(dřív „zvládnuto", teď nevěděl ⇒ zpět do retestů). Nové do retestů: Apriori prořezání podle
podmnožin (3.1.4), PageRank krok + dangling (6.14), linkage na číslech (3.3.4), FPR jmenovatel.
Pozorování: u „spočítej krok" odpovídá „nebudu počítat, vím vzorec" — a mechanika pak chybí.
Příště zadávat tak malé příklady, že se odpověď dá říct z hlavy (2–4 čísla).

## Po kole 12 (3. 9. 2026) — nový režim: jen slabiny

Uživatel: **zkoušet už jen slabiny / co nevěděl**; jeho „ok"/„umím" = splněno, přeskočit bez bodů.
Pro CLARA/CLARANS řekl „out of scope" — vyřazeno.

Splněno v kole 12 (dál nezkoušet): SVM C, Apriori prořezání, kritéria hodnocení mimo přesnost
(retest č. 6), taxonomie položek v MBA (retest č. 4), LOO definice (k = n).

**Kartičky (3× propadlé, vysvětlení v kole už nepomáhá):** standardizace přes střední absolutní
odchylku (2.5), dangling vs. spider trap (6.14), blízkostní centralita směr (6.4, 2×).

**Otevřené retesty do kola 13:** lift v decilu (5.2.4), PageRank iterační krok (6.14), linkage na
číslech + tvary klastrů (3.3.4), FPR jmenovatel (5.2.3), AdaBoost konec při ε ≥ 0,5 (3.2.8),
taxonomie metod detekce komunit (retest č. 2), information gain vážení (3.2.2), Laplaceova korekce
tvar (3.2.3); ze starších kol: Girvan–Newman volba počtu komunit, ratio vs. normalized cut,
validační množina, vzájemná informace vada, confounding, FP-strom řazení, Leiden.

## Po kole 13 (3. 9. 2026)

Splněno (dál nezkoušet): lift v decilu, validační množina, linkage (tvary nejsou ve skriptech).
Uživatel označil „ok" / vyřadil: information gain vážení, Laplaceova korekce tvar, **PageRank
iterační krok → patří do drilu vzorců (04-vzorce), ne sem.**

**Kartičky:** standardizace přes střední absolutní odchylku (3×), dangling vs. spider trap (3×),
blízkostní centralita směr (2×), **FPR jmenovatel (2× v řadě, pokaždé jinak)**.

**Otevřené retesty do kola 14:** AdaBoost konec při ε ≥ 0,5 (2×), taxonomie detekce komunit
(zbývá skupinově + hierarchické), Girvan–Newman výběr úrovně podle modularity; ze starších kol:
ratio vs. normalized cut, vzájemná informace vada, confounding (třetí proces), FP-strom řazení,
Leiden vs. Louvain, C4.5 proti ID3, k-medoids důvody, vyhlazování šumu, Milgram slabina, tři
roviny vyhodnocení znalostí, nevyvážené třídy, alternativy ke vzorkování.

## Po kole 14 (3. 9. 2026)

Splněno (dál nezkoušet): ratio vs. normalized cut, FP-strom řazení, Leiden vs. Louvain.
Vyřazeno uživatelem: vyhlazování šumu, Milgram, tři roviny vyhodnocení, C4.5 (uzavřeno po částečné
odpovědi).

**Kartičky (jednovětné, opakovaně nula):** standardizace přes střední absolutní odchylku (3×),
dangling vs. spider trap (3×), blízkostní centralita směr (2×), FPR jmenovatel (2×), vada vzájemné
informace (2×), confounding (2×).

**Zbývající otevřené retesty (poslední kolo):** AdaBoost konec při ε ≥ 0,5, taxonomie detekce
komunit (skupinově + hierarchické), Girvan–Newman výběr úrovně podle modularity, k-medoids druhý
důvod (outliery), nevyvážené třídy, alternativy ke vzorkování. Po nich je seznam slabin okruhu 3
vyčerpán — dál už jen kartičky.
