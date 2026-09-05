# Stav testovacího zkoušení (po restartu kontextu pokračovat odtud)

Poslední aktualizace: 3. 9. 2026, po kole 23 (cílené zkoušení kapitol dokončeno: MAS 2, 4, 7; NIC 3).

## Jak to má probíhat (pravidla, která si uživatel vyžádal)

- Zkouším z **okruhu 1 (Multiagentní systémy)** a **okruhu 2 (Přírodou inspirované počítání)**, mix.
- **Jedna otázka po druhé**, vždy počkat na odpověď. Nikdy si neodpovídat sám.
- Po každé odpovědi **krátké hodnocení: max 3 věty**, bez rovnic a LaTeXu (v terminálu se nezobrazí).
- Otázky mají být **menší** — ověřují pochopení pojmů, ne eseje.
- Používat **zavedenou anglickou terminologii**, nevymýšlet české kalky.
- Po každých 10 otázkách: **souhrnné hodnocení kola** (tabulka skóre + vzorec chyb).
- Po každém kole zapsat nové mezery do `zkouseni/slabiny.md` — **jen to, co nevěděl nebo řekl špatně**, ve stávajícím formátu `pojem — v čem byla chyba — → kap. X.Y`.
- Otázky si dopředu nacachovat po deseti, aby to šlo rychle.
- **Když uživatel odpoví „umím“, otázka se přeskočí** a zapisuje se jako známá („umím“),
  bez bodování a bez výkladu — kvůli času. Platí **jen** když to napíše sám; nikdy to nepředpokládat
  jen proto, že bych otázku hodnotil plným počtem. Do průměru kola se takové otázky nepočítají.
- **Otázky výhradně ze shrnovacích skript, přednostně z anglické verze** (`ENG/01-multiagent-systems`, `ENG/02-nature-inspired-computing`). Slidy v `materialy/` **nejsou** zdroj otázek. **Vše, co v skriptech je, se zkouší — včetně pasáží označených \mimo{} a \mimoq{}** (rozhodnutí uživatele 25. 8. 2026).
- **Neptat se na jména a niche nálepky.** Otázka se vždy ptá na **princip / mechanismus / trade-off**, nikdy „co je architektura od X“. Pojem popsat slovy a ptat se, jak funguje.
- **Rozhodující a jediný zdroj je PDF skript** (`ENG/01-multiagent-systems.pdf`, `ENG/02-nature-inspired-computing.pdf`). Slidy v `materialy/` už **nehrají roli vůbec** — sloužily jen k sepsaní skript (finální upřesnění 25. 8. 2026: „slidy můžeš ignorovat, jediné rozhodující je to pdf“). Nic ve skriptech se nevylřazuje — ani pasáže označené \mimo{} a \mimoq{}.
- **Váhu témat určuje rozsah v PDF**: jedna věta = okrajové, celá podsekce nebo víc = důležité. Největší podsekce MAS (podle délky textu): Languages and platforms, KQML a FIPA-ACL, Classical games, Four basic types of auction, spreading activation network, Ontology languages, subsumpce, STRIPS, Normal-form games, speech acts, AOSE. NIC: Coevolution, General scheme of an EA, Genetic and evolutionary programming, Schema theory, Representation and genetic operators, Multi-objective optimisation, LCS/expert systems, Evolution strategies, Vose model, Genetic algorithms, Neuroevolution, Combinatorial problems and constraint handling.
## Kde jsme skončili

**Kolo 16 (3. 9. 2026) dokončeno**: rychlý retest chronických slabin MAS+NIC, 27,5/45 = 61 %, JADE
vyřazeno uživatelem. Nový režim od 3. 9.: **jen slabiny**, „ok"/„umím"/„není důležité" = splněno či
vyřazeno bez bodů. Splněno: horizontal vs. vertical layering, Vickrey, NEAT. Kartičky (3–4×
propadlé, dál nezkoušet v kole, jen přečíst): **OWL vs. RDFS** (konkrétní odvození: subsumpce,
konzistence), **LCS: odměna mění p/ε/F, GA mění c/a**, **ES komma selekce kvůli špatnému σ**.
**Kolo 17 (3. 9. 2026)**: 26,5/45 = 59 %, epistemická logika vyřazena. Splněno: fitness sharing.
Obrácené/zaměněné podruhé+: VCG (platba = externalita), Zeuthen (ustoupí nižší Risk), DE F = délka
kroku, parameter control „fixní" = tuning. Neznámý základní pojem: ε-greedy.
**Kolo 18 (3. 9. 2026)**: 20,5/45 = 46 %, epistáze vyřazena. Splněno: STRIPS frame problem, VI vs. PI.
Kartička nově: **winner's curse = common value** (3× mimo). Podruhé nula: deterministic crowding /
clearing, CMA-ES evolution path. **Kolo 19 (3. 9. 2026)**: 34,5/45 = 77 % — nejlepší kolo retestů. Splněno: FIPA-Request, next/action,
chicken, GP sufficiency, hypervolume. UCB vyřazeno. Otevřené: inform FP/RE (2), předčasná konvergence
znak (2× půlka), CCGA credit assignment.
**Režim od 4. 9. 2026 — cílené kapitoly** (na žádost uživatele): MAS kap. 2, 4, 7 a NIC kap. 3,
30 otázek ve třech kolech (cache: scratchpad kola-21-23-kapitoly.md).
**Kolo 21 (MAS kap. 2)**: 20,5/50 = 41 % — nejslabší kapitola; splněn jen commitment. Nula:
arbitráže, aktivační síť (2×), přípustný vs. korektní plán. Doporučeno přečíst shrnutí 2.14 celé.
**Kolo 22 (MAS kap. 4+7)**: 30,5/50 = 61 %. Splněno: neverifikovatelnost, protokoly, AMS/DF, společná
znalost. Kartička: **efekt Inform = H věří, že S věří φ** (2× obráceně). Slabé dvojice: T-Box/A-Box,
liveness/safety, KQML/KIF, RDFS.
**Kolo 23 (NIC kap. 3)**: 28/50 = 56 %. Splněno: ES selekce, rekombinace, DE geometrie. Nula: dynamická
krajina mechanismy, počet strategických parametrů. Doporučeno přečíst shrnutí 3.5 celé.
**Souhrn cílených kapitol:** MAS 2 = 41 % (nejslabší, číst 2.14), MAS 4+7 = 61 %, NIC 3 = 56 %.

**Kolo 20 (3. 9. 2026)**: 36/50 = 72 %. Splněno: utilita nad běhy, FIPA-ACL pole, prostředí, MARL,
Vose, memetický. Otevřené: blackboard arbitr (2×), EP vs. GP (2× záměna), subsumpce omezení,
ruleta druhá půlka.
Zbývá v zásobě MAS: deduktivní agent, AMS vs. DF, Nash/Pareto/dominance, Zeuthen (retest), VCG
(retest), DCOP důvody; NIC: ADF, neutralita vs. ruggedness, zašuměná fitness, implicitní paralelismus,
NSGA-II kritéria, hill climbing first improvement, DE F/CR (retest), parameter control (retest).
Původní seznam: utilita nad běhy, FIPA-ACL pole, subsumpce směr, felicity FP/RE, deduktivní agent, blackboard
arbiter, vlastnosti prostředí, MARL, AMS vs. DF, Nash/Pareto/dominance. NIC: GP sufficiency, ADF,
CCGA, neutralita vs. ruggedness, EP vs. GP, ACO parametry, zašuměná fitness, Vose, memetický,
hypervolume, implicitní paralelismus, předčasná konvergence, NSGA-II kritéria, selekce
roulette/rank/tournament, hill climbing first improvement.
Zásoba dalších retestů: viz scratchpad kolo-17 (MAS ~18, NIC ~20 položek).

Zbývající retesty s posunem: policy gradient (stochastická politika), scatter search
(systematická kombinace + lokální prohledávání), admissible vs. consistent (důsledek).

### Stav před 3. 9.

**Kolo 15 dokončeno** (26,5/45 = 59 %; otázka 1 MAPF přeskočena jako „umím" — bakalářská práce).
Kolo bylo celé z dosud nedotčených podsekcí. Slabiny v `zkouseni/slabiny.md`.
Zbývající nedotčené podsekce po kole 15: IDA a global workspace, A* samostatně, agent a MAS
(definice, vlastnosti inteligentního agenta), implementing a BDI agent, comparison of
architectures, the selfish agent, agent interaction in the environment, další typy aukcí,
why and how agents learn; z NIC: other swarm algorithms.
Chronické retesty na kartičky: **OWL vs. RDFS** (3 propadnutí), **horizontal vs. vertical
layering**, **LCS parametry vs. obsah**, nově **policy gradient** a **scatter search vs. DE**.

## Výsledky kol 1–10

| Kolo | Skóre |
|---|---|
| 1 | 32,5/50 = 65 % |
| 2 | 28/50 = 56 % |
| 3 | 31,5/50 = 63 % |
| 4 | 23/50 = 46 % |
| 5 | 32/50 = 64 % |
| 6 | 24,5/50 = 49 % |
| 7 | 20/50 = 40 % |
| 8 | 13,5/50 = 27 % |
| 9 | 14/45 = 31 % |
| 10 | 17,5/40 = 44 % |
| 11 | 25/50 = 50 % |
| 12 | 25,5/50 = 51 % |
| 13 | 32/50 = 64 % |
| 14 | 27/50 = 54 % |
| 15 | 26,5/45 = 59 % |

## Co uživatel vyřadil jako nepotřebné

- Sociální volba a hlasovací protokoly (Gibbard–Satterthwaite atd.) — v okruhu nejsou.
- Intencionální postoj (Dennett).
- SPEA2 (stačí NSGA-II).
- Obecně: přesné definice drobných parametrů GA nejsou priorita — uživatel si sám rozhodne, co je důležité.
- Pozor: negenerovat otázky mimo okruh (AutoML/NAS byl přešlap).

## Diagnóza po devíti kolech

Silné: úvahové otázky — teorie her, architektury, kompromisy, mechanika „jak to běží".
Slabé: (a) faktografie platformy a jazyků (FIPA, Jason, JADE), (b) přesně pojmenované mechanismy a jejich parametry, (c) **záměny za sousední pojem** (ADF↔CPPN, EP↔GP, PRS↔STRIPS) — nejdražší typ chyby u ústní zkoušky, (d) tendence odpovědět na první část otázky a zbytek vynechat.

Kompletní seznam mezer je v `zkouseni/slabiny.md` (okruh 1 a 2, členěno po kolech).

## Kolo 16 — nacachované otázky (26. 8. 2026)

Zbytek nedotčených podsekcí + pět kartičkových retestů.

1. [MAS] IDA a global workspace — kognitivní architektura, co je ta „soutěž o pozornost" (2.12) *nové*
2. [NIC] Scatter search vs. diferenciální evoluce — rozlišovací rys *(retest)*
3. [MAS] Vlastnosti inteligentního agenta — čtyři vlastnosti a jejich napětí (1.2) *nové*
4. [MAS] Policy gradient / actor–critic — kdy je nutný a jak se pozná směr *(retest)*
5. [MAS] Self-interested agent — proč nepředpokládat benevolenci, co je společné a co ne (5.6) *nové*
6. [NIC] Další rojové algoritmy — bee colony, firefly: co je v nich mechanismem (4.3) *nové*
7. [MAS] OWL vs. RDFS *(retest, čtvrtý pokus)*
8. [MAS] Proč a jak se agenti učí — co se vlastně učí (6.1) *nové*
9. [MAS] Horizontal vs. vertical layering + srovnání architektur *(retest)*
10. [NIC] LCS — co mění reward update a co GA *(retest)*

Zbydou nedotčené jen: A* samostatně, implementing a BDI agent, další typy aukcí.

Průběžné skóre kola 16:
