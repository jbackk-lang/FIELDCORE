# Przykład użycia operatora cyklu kosmicznego FIELDCORE
# examples/cosmos/cykl_demo.py

import math
from src.cosmos.cykl import operator_cyklu, ewolucja

def demo():
    print("=== DEMO CYKLU KOSMICZNEGO Λ–τ–ρ–J — FIELDCORE ===")

    # Przykład 1: punkt startowy w fazie τ
    u1 = 0.6 * math.pi
    wynik1 = operator_cyklu(u1)

    print("\nPrzykład 1 — Faza τ:")
    print("u =", u1)
    print("Faza:", wynik1["faza"])
    print("Następna faza:", wynik1["nastepna"])
    print("Punkt J:", wynik1["punkt_J"])

    # Przykład 2: punkt J
    u2 = math.pi
    wynik2 = operator_cyklu(u2)

    print("\nPrzykład 2 — Punkt J:")
    print("u =", u2)
    print("Faza:", wynik2["faza"])
    print("Następna faza:", wynik2["nastepna"])
    print("Punkt J:", wynik2["punkt_J"])

    # Przykład 3: ewolucja cyklu
    print("\nPrzykład 3 — Ewolucja cyklu (10 kroków):")
    start = 0.4 * math.pi
    kroki = ewolucja(start, krok=0.2, n=10)

    for i, k in enumerate(kroki):
        print(f"Krok {i+1}: Faza={k['faza']}, Następna={k['nastepna']}, J={k['punkt_J']}")

if __name__ == "__main__":
    demo()
