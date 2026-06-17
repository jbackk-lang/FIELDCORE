# Przykład użycia mapy cyklu kosmicznego FIELDCORE
# examples/cosmos/mapa_demo.py

import math
from src.cosmos.mapa import segment, mapa_faz, opis_zakresow

def demo():
    print("=== DEMO MAPY CYKLU Λ–τ–ρ–J — FIELDCORE ===")

    # Przykład 1: segment dla konkretnego u
    u = 0.8 * math.pi
    seg = segment(u)

    print(f"\nSegment dla u={u}:")
    print("Faza:", seg["faza"])
    print("Zakresy fazy:", seg["segmenty"])

    # Przykład 2: mapa faz (20 kroków)
    print("\nMapa faz (20 kroków):")
    fazy = mapa_faz(20)
    print(fazy)

    # Przykład 3: pełny opis zakresów
    print("\nOpis zakresów faz:")
    zakresy = opis_zakresow()
    for f, z in zakresy.items():
        print(f"{f}: {z}")

if __name__ == "__main__":
    demo()
