# Globalna topologia kosmosu — implementacja FIELDCORE
# src/cosmos/topologia.py

import math

def faza_globalna(u):
    """
    Zwraca fazę globalną Λ–τ–ρ–J na podstawie parametru u.
    Zakresy zgodne z topologią toruso‑Möbiusa.
    """
    if 0 <= u < math.pi * 0.5:
        return "Λ"
    if math.pi * 0.5 <= u < math.pi * 0.75:
        return "τ"
    if math.pi * 0.75 <= u < math.pi:
        return "ρ"
    if abs(u - math.pi) < 1e-6:
        return "J"
    if math.pi < u <= math.pi * 1.25:
        return "Λ"
    if math.pi * 1.25 < u <= math.pi * 1.5:
        return "τ"
    if math.pi * 1.5 < u < math.pi * 2:
        return "ρ"
    return "Λ"


def orientacja_globalna(u):
    """
    Zwraca globalną orientację powierzchni:
    - 'L' — lewostronna
    - 'P' — prawostronna
    Zmiana następuje w punkcie J.
    """
    if u < math.pi:
        return "L"
    return "P"


def punkt_J(u):
    """
    Zwraca True, jeśli u odpowiada punktowi J.
    """
    return abs(u - math.pi) < 1e-6


def gradient_globalny(u, v, R=2.0, a=0.5):
    """
    Oblicza globalny gradient pola ρ.
    Gradient rośnie w pobliżu punktu J.
    """
    return abs(math.sin(u / 2)) * (1 + abs(v)) * (a / R)


def analiza_topologii(u, v):
    """
    Zwraca pełną analizę globalnej topologii:
    - fazę Λ–τ–ρ–J
    - orientację
    - punkt J
    - gradient pola
    """
    return {
        "faza": faza_globalna(u),
        "orientacja": orientacja_globalna(u),
        "punkt_J": punkt_J(u),
        "gradient_rho": gradient_globalny(u, v)
    }


if __name__ == "__main__":
    # Przykład działania
    u = math.pi * 0.8
    v = 0.2

    wynik = analiza_topologii(u, v)

    print("Analiza topologii globalnej:")
    print("Faza:", wynik["faza"])
    print("Orientacja:", wynik["orientacja"])
    print("Punkt J:", wynik["punkt_J"])
    print("Gradient ρ:", wynik["gradient_rho"])
