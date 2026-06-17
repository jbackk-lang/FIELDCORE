# Przykład użycia algorytmu "Nowe Ziemie"
# examples/cosmos/nowe_ziemie_demo.py

from src.cosmos.nowe_ziemie import ocen_planete

def demo():
    print("=== DEMO ALGORYTMU NOWE ZIEMIE — FIELDCORE ===")

    # Przykład 1: planeta w galaktyce rezonansowej (ρ)
    faza = "ρ"
    gradient = 0.4
    kat = 70
    odleglosc = 0.5

    print("\nPlaneta 1:")
    print("Faza:", faza)
    print("Gradient ρ:", gradient)
    print("Kąt skrętu:", kat)
    print("Odległość od J:", odleglosc)
    print("Wynik:", ocen_planete(faza, gradient, kat, odleglosc))

    # Przykład 2: planeta w fazie τ (średnia stabilność)
    faza = "τ"
    gradient = 0.2
    kat = 55
    odleglosc = 0.3

    print("\nPlaneta 2:")
    print("Faza:", faza)
    print("Gradient ρ:", gradient)
    print("Kąt skrętu:", kat)
    print("Odległość od J:", odleglosc)
    print("Wynik:", ocen_planete(faza, gradient, kat, odleglosc))

    # Przykład 3: planeta blisko punktu J (niestabilna)
    faza = "ρ"
    gradient = 0.3
    kat = 80
    odleglosc = 0.1

    print("\nPlaneta 3:")
    print("Faza:", faza)
    print("Gradient ρ:", gradient)
    print("Kąt skrętu:", kat)
    print("Odległość od J:", odleglosc)
    print("Wynik:", ocen_planete(faza, gradient, kat, odleglosc))

if __name__ == "__main__":
    demo()
