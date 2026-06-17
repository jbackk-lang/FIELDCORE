# Mapa cyklu kosmicznego Λ–τ–ρ–J — implementacja FIELDCORE
# src/cosmos/mapa.py

import math
from src.cosmos.cykl import faza

# Zakresy faz na toruso‑Möbiusie
ZAKRESY = {
    "Λ": [
        (0, 0.5 * math.pi),
        (math.pi, 1.25 * math.pi)
    ],
    "τ": [
        (0.5 * math.pi, 0.75 * math.pi),
        (1.25 * math.pi, 1.5 * math.pi)
    ],
    "ρ": [
        (0.75 * math.pi, math.pi),
        (1.5 * math.pi, 2 * math.pi)
    ],
    "J": [
        (math.pi, math.pi)  # punkt
    ]
}

def segment(u):
    """
    Zwraca segment cyklu, w którym znajduje się parametr u.
    """
    f = faza(u)
    return {
        "faza": f,
        "u": u,
        "segmenty": ZAKRESY[f]
    }

def mapa_faz(kroki=100):
    """
    Generuje uproszczoną mapę faz na przestrzeni 0 → 2π.
    Zwraca listę faz dla kolejnych kroków.
    """
    wynik = []
    for i in range(kroki):
        u = (2 * math.pi) * (i / kroki)
        wynik.append(faza(u))
    return wynik

def opis_zakresow():
    """
    Zwraca pełny opis zakresów faz.
    """
    return ZAKRESY

if __name__ == "__main__":
    print("Mapa faz (20 kroków):")
    print(mapa_faz(20))

    print("\nSegment dla u = 0.8π:")
    print(segment(0.8 * math.pi))

    print("\nZakresy faz:")
    for f, z in ZAKRESY.items():
        print(f"{f}: {z}")
