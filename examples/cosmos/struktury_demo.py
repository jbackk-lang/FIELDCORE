# Przykład użycia wieloskalowych struktur FIELDCORE
# examples/cosmos/struktury_demo.py

import math
from src.cosmos.struktury import analiza_wieloskalowa

def demo():
    print("=== DEMO STRUKTUR WIELOSKALOWYCH — FIELDCORE ===")

    # Przykład: punkt w rezonansie globalnym
    u = 0.8 * math.pi
    v = 0.15

    wynik = analiza_wieloskalowa(u, v)

    print(f"\nAnaliza dla u={u}, v={v}:")

    for skala, dane in wynik.items():
        print(f"\n[{skala.upper()}]")
        for k, val in dane.items():
            print(f"{k}: {val}")

if __name__ == "__main__":
    demo()
