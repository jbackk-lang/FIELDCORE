from src.fieldcore import FieldCore
from models.model_pola import ModelPola
from models.model_rezonansow import Rezonans

fc = FieldCore()

# pole + filtr λ
pole = ModelPola(intensywnosc=3.0)
pole.filtr_lambda(0.7)

fc.init_pole(pole)

# rezonanse
fc.add_rezonans(Rezonans(12, 4))
fc.add_rezonans(Rezonans(5, 2))

# topologia torus–Möbius
fc.ustaw_topologie(promien=10, skret=1)

# generacja cząstek
czastki = fc.generuj_czastki()

for c in czastki:
    print(c.opis())
