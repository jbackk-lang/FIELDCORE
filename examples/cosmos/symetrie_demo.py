# Przykład użycia modułu symetrii FIELDCORE
# examples/cosmos/symetrie_demo.py

import math
from src.cosmos.symetrie import analiza_symetrii

def demo():
    print("=== DEMO SYMETRII I PUNKTÓW J — FIELDCORE ===")

    # Przykład 1: punkt J (u = π)
    u1 = math.pi
    v1 = 0.3
    wynik1 = analiza_symetrii(u1, v1)

    print("\nPrzykład 1 — Punkt J:")
    print("u =", u1)
    print("v =", v1)
    print("Punkt J:", wynik1["punkt_J"])
    print("Orientacja:", wynik1["orientacja"])
    print("Gradient ρ:", wynik1["gradient_rho"])

    # Przykład 2: skręt lewostronny (u < π)
    u2 = math.pi / 2
    v2 = -0.4
    wynik2 = analiza_symetrii(u2, v2)

    print("\nPrzykład 2 — Skręt lewostronny:")
    print("u =", u2)
    print("v =", v2)
    print("Punkt J:", wynik2["punkt_J"])
    print("Orientacja:", wynik2["orientacja"])
    print("Gradient ρ:", wynik2["gradient_rho"])

    # Przykład 3: skręt prawostronny (u > π)
    u3 = math.pi * 1.5
    v3 = 0.1
    wynik3 = analiza_symetrii(u3, v3)

    print("\nPrzykład 3 — Skręt prawostronny:")
    print("u =", u3)
    print("v =", v3)
    print("Punkt J:", wynik3["punkt_J"])
    print("Orientacja:", wynik3["orientacja"])
    print("Gradient ρ:", wynik3["gradient_rho"])

if __name__ == "__main__":
    demo()
