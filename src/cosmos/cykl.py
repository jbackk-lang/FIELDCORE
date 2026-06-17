# Operator cyklu kosmicznego Λ–τ–ρ–J — implementacja FIELDCORE
# src/cosmos/cykl.py

import math

def faza(u):
    """
    Zwraca fazę cyklu kosmicznego Λ–τ–ρ–J na podstawie parametru u.
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


def nastepna_faza(f):
    """
    Zwraca kolejną fazę cyklu.
    """
    if f == "Λ":
        return "τ"
    if f == "τ":
        return "ρ"
    if f == "ρ":
        return "J"
    if f == "J":
        return "Λ"
    return "Λ"


def operator_cyklu(u):
    """
    Zwraca:
    - aktualną fazę
    - kolejną fazę
    - informację, czy jesteśmy w punkcie J
    """
    f = faza(u)
    return {
        "faza": f,
        "nastepna": nastepna_faza(f),
        "punkt_J": (f == "J")
    }


def ewolucja(u, krok=0.1, n=10):
    """
    Generuje n kroków ewolucji cyklu kosmicznego.
    """
    wyniki = []
    x = u
    for _ in range(n):
        wyniki.append(operator_cyklu(x))
        x += krok
        if x > 2 * math.pi:
            x -= 2 * math.pi
    return wyniki


if __name__ == "__main__":
    # Przykład działania
    start = 0.6 * math.pi
    wynik = operator_cyklu(start)

    print("Operator cyklu kosmicznego:")
    print("Faza:", wynik["faza"])
    print("Następna faza:", wynik["nastepna"])
    print("Punkt J:", wynik["punkt_J"])
