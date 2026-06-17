# Przykład użycia operatorów informacyjnych FIELDCORE
# examples/cosmos/informacja_demo.py

import math
from src.cosmos.informacja import analiza_informacji

def demo():
    print("=== DEMO INFORMACJI I ENTROPII — FIELDCORE ===")

    # Przykład: punkt w rezonansie ρ
    u = 0.75 * math.pi
    v = 0.1

    wynik = analiza_informacji(u, v)

    print(f"\nAnaliza informacyjna dla u={u}, v={v}:")

    for k, val in wynik.items():
        print(f"{k}: {val}")

    # Przykład 2: punkt J (maksymalna entropia)
    u2 = math.pi
    v2 = -0.2

    wynik2 = analiza_informacji(u2, v2)

    print(f"\nAnaliza informacyjna dla punktu J (u={u2}, v={v2}):")

    for k, val in wynik2.items():
        print(f"{k}: {val}")

if __name__ == "__main__":
    demo()
