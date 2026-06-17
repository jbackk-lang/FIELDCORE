# Rezonanse globalne pola ρ — implementacja FIELDCORE
# src/cosmos/rezonanse.py

import math

def czy_rezonans_globalny(u, v):
    """
    Sprawdza, czy punkt (u, v) znajduje się w rezonansie globalnym ρ.
    Warunki:
    - u ≈ 0.75π (skręt ~90°)
    - gradient ρ > 0
    - brak punktu J (u != π)
    """
    if abs(u - (0.75 * math.pi)) > 0.3:
        return False

    if abs(u - math.pi) < 1e-6:
        return False

    if gradient_rho(u, v) <= 0:
        return False

    return True


def gradient_rho(u, v, R=2.0, a=0.5):
    """
    Oblicza gradient pola ρ.
    Gradient rośnie w pobliżu punktu J, ale rezonans wymaga stabilnego wzrostu.
    """
    return abs(math.sin(u / 2)) * (1 + abs(v)) * (a / R)


def poziom_rezonansu(u, v):
    """
    Zwraca poziom rezonansu w skali 0–1.
    Maksimum przy u = 0.75π.
    """
    ideal = 0.75 * math.pi
    odleglosc = abs(u - ideal)

    # normalizacja
    poziom = max(0.0, 1.0 - (odleglosc / (0.25 * math.pi)))

    return poziom * gradient_rho(u, v)


def analiza_rezonansu(u, v):
    """
    Zwraca pełną analizę rezonansu:
    - czy rezonans globalny
    - poziom rezonansu
    - gradient pola
    """
    return {
        "rezonans_globalny": czy_rezonans_globalny(u, v),
        "poziom_rezonansu": poziom_rezonansu(u, v),
        "gradient_rho": gradient_rho(u, v)
    }


if __name__ == "__main__":
    # Przykład działania
    u = 0.75 * math.pi
    v = 0.2

    wynik = analiza_rezonansu(u, v)

    print("Analiza rezonansu globalnego:")
    print("Rezonans globalny:", wynik["rezonans_globalny"])
    print("Poziom rezonansu:", wynik["poziom_rezonansu"])
    print("Gradient ρ:", wynik["gradient_rho"])
