# Informacja i entropia w cyklu kosmicznym — implementacja FIELDCORE
# src/cosmos/informacja.py

import math
from src.cosmos.cykl import faza
from src.cosmos.rezonanse import poziom_rezonansu

def entropia(u, v):
    """
    Oblicza entropię pola w zależności od fazy cyklu.
    Zakres: 0 (minimum) — 1 (maksimum).
    """
    f = faza(u)

    if f == "Λ":
        return 0.2  # stabilność, niska entropia
    if f == "τ":
        return 0.6  # wzrost nieuporządkowania
    if f == "ρ":
        return 0.1  # rezonans = minimum entropii
    if f == "J":
        return 1.0  # reset informacji = maksimum entropii

    return 0.5


def koherencja(u, v):
    """
    Koherencja pola informacyjnego.
    Najwyższa w rezonansie ρ, najniższa w punkcie J.
    """
    f = faza(u)

    if f == "ρ":
        return 1.0
    if f == "Λ":
        return 0.7
    if f == "τ":
        return 0.4
    if f == "J":
        return 0.0

    return 0.5


def przeplyw_informacji(u, v):
    """
    Przepływ informacji wzdłuż toruso‑Möbiusa.
    Wartość dodatnia = przepływ uporządkowany.
    Wartość ujemna = przepływ chaotyczny (punkt J).
    """
    f = faza(u)

    if f == "Λ":
        return 0.5
    if f == "τ":
        return 0.8
    if f == "ρ":
        return 1.0
    if f == "J":
        return -1.0  # reset, chaos lokalny

    return 0.0


def analiza_informacji(u, v):
    """
    Zwraca pełną analizę informacyjną:
    - entropię
    - koherencję
    - przepływ informacji
    - poziom rezonansu
    """
    return {
        "entropia": entropia(u, v),
        "koherencja": koherencja(u, v),
        "przeplyw": przeplyw_informacji(u, v),
        "rezonans": poziom_rezonansu(u, v)
    }


if __name__ == "__main__":
    # Przykład działania
    u = 0.75 * math.pi
    v = 0.1

    wynik = analiza_informacji(u, v)

    print("Analiza informacji:")
    for k, val in wynik.items():
        print(f"{k}: {val}")
