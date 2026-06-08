from src.fieldcore import FieldCore
from models.model_pola import ModelPola
from models.model_rezonansow import Rezonans

fc = FieldCore()

# pole z harmonicznymi
pole = ModelPola(intensywnosc=2.5)
pole.dodaj_harmonike(0.3)
pole.dodaj_harmonike(0.7)

fc.init_pole(pole)

# rezonanse
fc.add_rezonans(Rezonans(8, 4))
fc.add_rezonans(Rezonans(15, 6))

# topologia
fc.ustaw_topologie(promien=12, skret=2)

# aktualizacja topologii
fc.aktualizuj_topologie(dR=1, dS=-0.5)

# generacja cząstek
czastki = fc.generuj_czastki()

for c in czastki:
    print(c.opis())
