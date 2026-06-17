# Przykład użycia globalnej topologii FIELDCORE
# examples/cosmos/topologia_demo.py

import math
from src.cosmos.topologia import analiza_topologii

def demo():
    print("=== DEMO TOPOLOGII GLOBALNEJ — FIELDCORE ===")

    # Przykład 1: obszar rezonansu (ρ)
    u1 = math.pi * 0.8
    v1 = 0.1
    wynik1 = analiza_topologii(u1, v1)

    print("\nPrzykład 1 — Rezonans ρ:")
    print("u =", u1)
    print("v =", v1)
    print("Faza:", wynik1["faza"])
    print("Orientacja:", wynik1["orientacja"])
    print("Punkt J:", wynik1["punkt_J"])
    print("Gradient ρ:", wynik1["gradient_rho"])

    # Przykład 2: punkt J
    u2 = math.pi
    v2 = -0.3
    wynik2 = analiza_topologii(u2, v2)

    print("\nPrzykład 2 — Punkt J:")
    print("u =", u2)
    print("v =", v2)
    print("Faza:", wynik2["faza"])
    print("Orientacja:", wynik2["orientacja"])
    print("Punkt J:", wynik2["punkt_J"])
    print("Gradient ρ:", wynik2["gradient_rho"])

    # Przykład 3: faza Λ (stabilność globalna)
    u3 = math.pi * 0.2
    v3 = 0.4
    wynik3 = analiza_topologii(u3, v3)

    print("\nPrzykład 3 — Faza Λ:")
    print("u =", u3)
    print("v =", v3)
    print("Faza:", wynik3["faza"])
    print("Orientacja:", wynik3["orientacja"])
    print("Punkt J:", wynik3["punkt_J"])
    print("Gradient ρ:", wynik3["gradient_rho"])

if __name__ == "__main__":
    demo()
