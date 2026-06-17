# Klasyfikator galaktyk Λ–τ–ρ–J — FIELDCORE
# src/cosmos/klasyfikator.py

import math

def klasyfikuj_galaktyke(kat_stopnie):
    """
    Klasyfikuje galaktykę według fazy skrętu Λ–τ–ρ–J.
    kat_stopnie — kąt skrętu galaktyki w stopniach.
    """

    if kat_stopnie < 0:
        raise ValueError("Kąt nie może być ujemny.")

    if kat_stopnie <= 50:
        return "Λ — faza liniowa (galaktyki eliptyczne / soczewkowate)"

    if 50 < kat_stopnie <= 70:
        return "τ — faza przejściowa (spiralne luźne, nieregularne)"

    if 70 < kat_stopnie <= 95:
        return "ρ — faza rezonansu (spiralne wyraźne, stabilne)"

    return "J — punkt skrętu (aktywne jądra, zmiana orientacji)"

def kat_z_ramion(liczba_ramion, skret_na_ramie):
    """
    Szacuje kąt skrętu na podstawie:
    - liczby ramion spiralnych,
    - skrętu jednego ramienia (w stopniach).
    """

    return liczba_ramion * skret_na_ramie

if __name__ == "__main__":
    # Przykład użycia
    kat = kat_z_ramion(2, 35)  # 2 ramiona, każde skręcone o 35°
    print("Kąt:", kat)
    print("Klasyfikacja:", klasyfikuj_galaktyke(kat))
