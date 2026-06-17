# Przykład użycia rezonansów globalnych FIELDCORE
# examples/cosmos/rezonanse_demo.py

import math
from src.cosmos.rezonanse import analiza_rezonansu

def demo():
    print("=== DEMO REZONANSÓW GLOBALNYCH — FIELDCORE ===")

    # Przykład 1: idealny rezonans (u ≈ 0.75π)
    u1 = 0.75 * math.pi
    v1 = 0.2
    wynik1 = analiza_rezonansu(u1, v1)

    print("\nPrzykład 1 — Idealny rezonans ρ:")
    print("u =", u1)
    print("v =", v1)
    print("Rezonans globalny:", wynik1["rezonans_globalny"])
    print("Poziom rezonansu:", wynik1["poziom_rezonansu"])
    print("Gradient ρ:", wynik1["gradient_rho"])

    # Przykład 2: obszar przejściowy (τ)
    u2 = 0.6 * math.pi
    v2 = -0.3
    wynik2 = analiza_rezonansu(u2, v2)

    print("\nPrzykład 2 — Obszar przejściowy τ:")
    print("u =", u2)
    print("v =", v2)
    print("Rezonans globalny:", wynik2["rezonans_globalny"])
    print("Poziom rezonansu:", wynik2["poziom_rezonansu"])
    print("Gradient ρ:", wynik2["gradient_rho"])

    # Przykład 3: punkt J (niestabilny)
    u3 = math.pi
    v3 = 0.1
    wynik3 = analiza_rezonansu(u3, v3)

    print("\nPrzykład 3 — Punkt J (niestabilny):")
    print("u =", u3)
    print("v =", v3)
    print("Rezonans globalny:", wynik3["rezonans_globalny"])
    print("Poziom rezonansu:", wynik3["poziom_rezonansu"])
    print("Gradient ρ:", wynik3["gradient_rho"])

if __name__ == "__main__":
    demo()
