from src.fieldcore import FieldCore
from models.model_pola import ModelPola
from models.model_rezonansow import Rezonans

def szybka_symulacja(intensywnosc, rezonanse):
    fc = FieldCore()
    pole = ModelPola(intensywnosc=intensywnosc)
    fc.init_pole(pole)

    for f, A in rezonanse:
        fc.add_rezonans(Rezonans(f, A))

    return fc.generuj_czastki()
