from src.fieldcore import FieldCore
from models.model_pola import ModelPola
from models.model_rezonansow import Rezonans
from config.global_config import CONFIG

# włączamy logi
CONFIG.wlacz_logi()

fc = FieldCore()

# pole + harmoniczne + filtr λ
pole = ModelPola(intensywnosc=4.0)
pole.dodaj_harmonike(0.2)
pole.dodaj_harmonike(0.5)
pole.filtr_lambda(0.8)

fc.init_pole(pole)

# rezonanse
fc.add_rezonans(Rezonans(6, 3))
fc.add_rezonans(Rezonans(14, 7))

# topologia torus–Möbius
fc.ustaw_topologie(promien=15, skret=3)
fc.aktualizuj_topologie(dR=-2, dS=1)

# generacja cząstek
czastki = fc.generuj_czastki()

for c in czastki:
    print(c.opis())
