# Symetrie skrętu i punkty J — implementacja FIELDCORE
# src/cosmos/symetrie.py

import math

def punkt_J(u):
    """
    Zwraca True, jeśli parametr u odpowiada punktowi J.
    Punkt J występuje przy u = π (180°).
    """
    return abs(u - math.pi) < 1e-6


def orientacja(u):
    """
    Zwraca orientację powierzchni toruso‑Möbiusa:
    - 'L' — skręt lewostronny
    - 'P' — skręt prawostronny
    Zmiana orientacji następuje w punkcie J.
    """
    if u < math.pi:
        return "L"
    return "P"


def gradient_rho(u, v, R=2.0, a=0.5):
    """
    Oblicza lokalny gradient pola ρ dla toruso‑Möbiusa.
    Gradient rośnie w pobliżu punktu J.
    """
    # uproszczony model gradientu
    return abs(math.sin(u / 2)) * (1 + abs(v)) * (a / R)


def analiza_symetrii(u, v):
    """
    Zwraca pełną analizę lokalnej symetrii:
    - czy punkt J
    - orientacja
    - gradient ρ
    """
    return {
        "punkt_J": punkt_J(u),
        "orientacja": orientacja(u),
        "gradient_rho": gradient_rho(u, v)
    }


if __name__ == "__main__":
    # Przykład działania
    u = math.pi
    v = 0.3

    wynik = analiza_symetrii(u, v)

    print("Analiza symetrii:")
    print("Punkt J:", wynik["punkt_J"])
    print("Orientacja:", wynik["orientacja"])
    print("Gradient ρ:", wynik["gradient_rho"])
