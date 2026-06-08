from src.fieldcore import FieldCore
from models.model_pola import ModelPola
from models.model_rezonansow import Rezonans

fc = FieldCore()
fc.init_pole(ModelPola(intensywnosc=2.0))

fc.add_rezonans(Rezonans(10, 5))
fc.add_rezonans(Rezonans(7, 3))

czastki = fc.generuj_czastki()

for c in czastki:
    print(c.opis())
