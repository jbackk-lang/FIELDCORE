# Globalna symulacja kosmosu — implementacja FIELDCORE
# src/cosmos/symulacja.py

import math
from src.cosmos.cykl import operator_cyklu
from src.cosmos.rezonanse import analiza_rezonansu
from src.cosmos.informacja import analiza_informacji
from src.cosmos.struktury import analiza_wieloskalowa

def krok_symulacji(u, v):
    """
    Wykonuje jeden krok symulacji kosmosu.
    Zwraca:
    - fazę cyklu
    - rezonans
    - informację (entropia, koherencja, przepływ)
    - analizę wieloskalową
    """
    return {
        "cykl": operator_cyklu(u),
        "rezonans": analiza_rezonansu(u, v),
        "informacja": analiza_informacji(u, v),
        "struktury": analiza_wieloskalowa(u, v)
    }

def symulacja_globalna(u_start, v_start, krok=0.1, n=20):
    """
    Wykonuje pełną symulację globalną kosmosu.
    Zwraca listę kroków symulacji.
    """
    wyniki = []
    u = u_start
    v = v_start

    for _ in range(n):
        wyniki.append(krok_symulacji(u, v))

        # ewolucja parametru u po toruso‑Möbiusie
        u += krok
        if u > 2 * math.pi:
            u -= 2 * math.pi

        # ewolucja parametru v (oscylacja)
        v = math.sin(u)

    return wyniki

if __name__ == "__main__":
    print("Symulacja globalna kosmosu (10 kroków):")
    wynik = symulacja_globalna(0.4 * math.pi, 0.1, n=10)

    for i, w in enumerate(wynik):
        print(f"\n=== KROK {i+1} ===")
        print("Faza:", w["cykl"]["faza"])
        print("Rezonans:", w["rezonans"]["poziom_rezonansu"])
        print("Entropia:", w["informacja"]["entropia"])
        print("Koherencja:", w["informacja"]["koherencja"])
        print("Punkt J:", w["cykl"]["punkt_J"])
