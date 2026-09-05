# Stav zkoušení vzorců (04-vzorce.pdf) — po restartu kontextu pokračovat odtud

Poslední aktualizace: 31. 8. 2026 (druhá session, checkpoint po dokončení všech netestovaných).

## Protokol (vyžádaný uživatelem)

- Náhodně po **jednom vzorci** z `04-vzorce.pdf` — vypsat **jen název** vzorce, nic víc.
  Uživatel si vzorec napíše a sám zkontroluje v PDF.
- Odpověď **„ok"** = umí → vyřadit z poolu. **Cokoliv jiného** = neumí → vrátit do poolu, +1 miss.
- U každého vzorce držet počet missů; slabiny se zapisují do `zkouseni/slabiny.md`.
- Zdroj: názvy `\fml{...}` v `04-vzorce.tex` — celkem **139 vzorců**.
- Samplovat **náhodně** (ne po pořadě dokumentu!), missnuté občas vracet.
- **DŮLEŽITÉ: otázku vypsat právě JEDNOU, čistý text, žádné tool cally mezi otázkami.**
  (Opakovaný problém první session: no-op tool cally duplikovaly výpis otázky až 10×.)
- Zapisování stavu bufferovat (ne po každé otázce) — rychlost odpovědí má prioritu.

## Skóre

- **Hotovo (ok): 115/139.** Všech 19 dříve netestovaných už bylo vyzkoušeno.
- **V poolu zbývá 24** — samé missnuté.
- Session 2 (31. 8.): 49 otázek, 30 ok / 19 idk (t-weight vypsaná, ale nezodpovězená — uživatel přepnul na netestované; zůstává ×1).

## Pool — missnuté (24)

### ×3 missnuto (propadly i napotřetí, 31. 8.)

- Metropolisovo kritérium (simulované žíhání)
- Kernelový trik a měkký okraj (SVM)
- Modularita Q
- Bellmanova rovnice pro evaluaci politiky
- ACO — pravidlo přechodu (Ant System)

### ×2 missnuto

- REINFORCE (policy gradient)
- Mutace — dárcovský vektor (DE)
- Binární kódování reálného čísla
- NEAT — míra podobnosti genomů (speciace)
- Lineární SVM — rozhodovací funkce a okraj
- Rozhodovací hranice a testování (SVM)
- Lineární regrese jedné proměnné (metoda nejmenších čtverců)
- Vícerozměrná lineární regrese — normální rovnice
- ELM — extrémní učicí stroj

### ×1 missnuto

- t-weight a kvantitativní charakteristické pravidlo (nezodpovězená, vypsat znovu)
- Střední hodnota ceny (různá cena různých chyb)
- HITS — huby a autority
- Finální PageRank s tlumicím faktorem
- Sousedské míry predikce vazeb
- Kuhn–Tuckerovy podmínky a vznik duálu
- Wolfeho duální úloha a rekonstrukce w, b
- LVQ — adaptace vah
- Náhodné lesy — rozptyl při korelovaných komponentách
- Poměrový a normalizovaný řez

## Zajímavé kontrasty (zvládnuté vs. nezvládnuté dvojice)

- Bellmanova rovnice **optimality ok**, ale rovnice **pro evaluaci politiky ne**.
- ACO **aktualizace feromonu ok**, ale **pravidlo přechodu ne** (×3).
- Učení logistické regrese (věrohodnost, cross-entropy) **ok**, primární SVM + Lagrangián **ok**,
  ale **KT podmínky a Wolfeho duál ne** — duální část SVM chybí celá.

## Missnuté klastry (kam se dívat při doučování)

1. **Celý SVM blok** (DM kap. 3.2.4) — kernel trik ×3, rozhodovací funkce, hranice+testování, KT podmínky, Wolfeho duál. Nejhorší klastr.
2. **Regrese** (DM) — nejmenší čtverce ×2, normální rovnice ×2; logistická už ok.
3. **RL rovnice** (MAS kap. 6) — Bellman evaluace ×3, REINFORCE ×2; optimalita a cíl v MDP už ok.
4. **SNA globální míry** — modularita ×3, PageRank, HITS huby/autority, predikce vazeb, řezy (poměrový/normalizovaný).
5. **NIC operátory** — dárcovský vektor DE, binární kódování reálného čísla, NEAT podobnost, ACO přechod ×3, Metropolis ×3.
6. Drobné: ELM, LVQ, náhodné lesy (korelované komponenty), střední hodnota ceny, t-weight.
