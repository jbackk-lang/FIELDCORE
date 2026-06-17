# Nowe Ziemie — Algorytm przewidywania stabilnych planet (FIELDCORE)

## 1. Wprowadzenie

Celem modułu „Nowe Ziemie” jest określenie, w których obszarach kosmosu
powstają stabilne planety typu ziemskiego. FIELDCORE zakłada, że stabilność
planet wynika z lokalnej konfiguracji pola Λ–τ–ρ–J oraz pozycji galaktyki
w cyklu toruso‑Möbiusa.

Model łączy:
- fazę skrętu galaktyki,
- lokalny rezonans pola,
- gradient ρ,
- stabilność Λ,
- punkt przejścia J.

---

## 2. Założenia modelu

1. Stabilne planety powstają w galaktykach w fazie ρ (rezonans).
2. W fazie τ mogą powstawać, ale są niestabilne.
3. W fazie Λ powstają rzadko (brak skrętu pola).
4. W fazie J powstają, ale często ulegają destabilizacji (aktywne jądra).

---

## 3. Kryteria stabilności planety

### 3.1. Kryterium galaktyczne
- Faza ρ → wysoka stabilność
- Faza τ → średnia stabilność
- Faza Λ → niska stabilność
- Faza J → niestabilność

### 3.2. Kryterium lokalnego pola
Planeta jest stabilna, jeśli:
- gradient ρ jest dodatni,
- lokalny skręt nie przekracza 95°,
- rezonans nie jest zakłócony przez punkt J.

### 3.3. Kryterium orbitalne
Orbita stabilna, jeśli:
- ekscentryczność < 0.3,
- odległość od gwiazdy mieści się w strefie rezonansu,
- gwiazda nie znajduje się w obszarze J.

---

## 4. Algorytm „Nowe Ziemie”

1. Ustal fazę skrętu galaktyki (Λ–τ–ρ–J).
2. Jeśli faza ≠ ρ → stabilność niska.
3. Oblicz lokalny gradient pola ρ.
4. Jeśli gradient < 0 → planeta niestabilna.
5. Oblicz lokalny skręt (kąt).
6. Jeśli kąt > 95° → planeta niestabilna.
7. Sprawdź odległość od punktu J.
8. Jeśli < 0.2R → planeta niestabilna.
9. Sprawdź parametry orbity.
10. Jeśli spełnione → planeta stabilna.

---

## 5. Wynik

Algorytm zwraca:

- „Stabilna Nowa Ziemia”
- „Potencjalnie stabilna”
- „Niestabilna”

---

## 6. Zgodność z FIELDCORE

Moduł opiera się na:
- toruso‑Möbius (ANALIZA_KOSMOSU.md),
- klasyfikatorze Λ–τ–ρ–J,
- mapie faz,
- zasadzie samopodobieństwa pola.

