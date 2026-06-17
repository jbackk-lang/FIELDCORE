# Algorytm "Nowe Ziemie" — implementacja FIELDCORE
# src/cosmos/nowe_ziemie.py

def stabilnosc_galaktyczna(faza):
    """
    Zwraca bazową stabilność na podstawie fazy Λ–τ–ρ–J.
    """
    if faza == "Λ":
        return 0.2
    if faza == "τ":
        return 0.5
    if faza == "ρ":
        return 0.9
    if faza == "J":
        return 0.1
    raise ValueError("Nieznana faza galaktyki.")


def stabilnosc_lokalna(gradient_rho, kat_skretu, odleglosc_od_J):
    """
    Ocena lokalnej stabilności planety.
    """
    if gradient_rho < 0:
        return 0.0

    if kat_skretu > 95:
        return 0.1

    if odleglosc_od_J < 0.2:
        return 0.2

    # stabilny lokalnie
    return 0.8


def ocen_planete(faza, gradient_rho, kat_skretu, odleglosc_od_J):
    """
    Główna funkcja oceniająca stabilność planety.
    Zwraca:
    - 'Stabilna Nowa Ziemia'
    - 'Potencjalnie stabilna'
    - 'Niestabilna'
    """

    Sg = stabilnosc_galaktyczna(faza)
    Sl = stabilnosc_lokalna(gradient_rho, kat_skretu, odleglosc_od_J)

    wynik = (Sg + Sl) / 2

    if wynik >= 0.75:
        return "Stabilna Nowa Ziemia"

    if wynik >= 0.4:
        return "Potencjalnie stabilna"

    return "Niestabilna"


if __name__ == "__main__":
    # Przykład działania
    faza = "ρ"
    gradient = 0.3
    kat = 70
    odleglosc = 0.4

    print("Ocena planety:")
    print(ocen_planete(faza, gradient, kat, odleglosc))
