# Struktury wieloskalowe kosmosu — implementacja FIELDCORE
# src/cosmos/struktury.py

import math
from src.cosmos.cykl import faza
from src.cosmos.rezonanse import poziom_rezonansu, czy_rezonans_globalny

def skala_czastki(u, v):
    """
    Analiza struktury na poziomie cząstki.
    """
    return {
        "faza": faza(u),
        "rezonans": poziom_rezonansu(u, v),
        "stabilna": poziom_rezonansu(u, v) > 0.3
    }


def skala_atomu(u, v):
    """
    Analiza struktury na poziomie atomu.
    """
    return {
        "powłoka": faza(u),
        "rezonans": poziom_rezonansu(u, v),
        "jonizacja": (faza(u) == "J")
    }


def skala_gwiazdy(u, v):
    """
    Analiza struktury na poziomie gwiazdy.
    """
    return {
        "etap": faza(u),
        "stabilna": (faza(u) == "ρ"),
        "ryzyko_zapadania": (faza(u) == "J")
    }


def skala_galaktyki(u, v):
    """
    Analiza struktury na poziomie galaktyki.
    """
    return {
        "typ": faza(u),  # Λ=eliptyczna, τ=nieregularna, ρ=spiralna, J=AGN
        "rezonans_globalny": czy_rezonans_globalny(u, v),
        "stabilna": (faza(u) == "ρ")
    }


def skala_kosmosu(u, v):
    """
    Analiza struktury na poziomie całego kosmosu.
    """
    return {
        "faza_globalna": faza(u),
        "rezonans": poziom_rezonansu(u, v),
        "punkt_J": (faza(u) == "J")
    }


def analiza_wieloskalowa(u, v):
    """
    Zwraca analizę na wszystkich poziomach jednocześnie.
    """
    return {
        "czastka": skala_czastki(u, v),
        "atom": skala_atomu(u, v),
        "gwiazda": skala_gwiazdy(u, v),
        "galaktyka": skala_galaktyki(u, v),
        "kosmos": skala_kosmosu(u, v)
    }


if __name__ == "__main__":
    # Przykład działania
    u = 0.8 * math.pi
    v = 0.15

    wynik = analiza_wieloskalowa(u, v)

    print("Analiza wieloskalowa:")
    for skala, dane in wynik.items():
        print(f"\n[{skala.upper()}]")
        for k, v in dane.items():
            print(f"{k}: {v}")
