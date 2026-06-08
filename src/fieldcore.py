# Główny moduł logiki FIELDCORE – w przygotowaniu
from models.model_pola import *
from models.model_rezonansow import *
from models.model_czastek import *
from models.model_torus_mobius import TorusMobius
class FieldCore:
    def aktualizuj_topologie(self, dR, dS):
        if hasattr(self, "topologia"):
            self.topologia.aktualizuj(dR, dS)
        return self

    def ustaw_topologie(self, promien, skret):
        self.topologia = TorusMobius(promien, skret)
        return self

    def __init__(self):
        self.pole = None
        self.rezonanse = []
        self.czastki = []

    def init_pole(self, model):
        self.pole = model
        return self

    def add_rezonans(self, rezonans):
        self.rezonanse.append(rezonans)
        return self

        def generuj_czastki(self):
        self.czastki = []

        for r in self.rezonanse:
            masa = r.amplituda * 0.1
            ladunek = 0 if r.czestotliwosc % 2 == 0 else 1
            spin = 1/2

            from models.model_czastek import Czastka
            cz = Czastka(masa, ladunek, spin)
            self.czastki.append(cz)

        return self.czastki
