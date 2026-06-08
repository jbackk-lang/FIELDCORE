# Główny moduł logiki FIELDCORE – w przygotowaniu
from models.model_pola import *
from models.model_rezonansow import *
from models.model_czastek import *
class FieldCore:
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
        # placeholder – logika pojawi się później
        return self.czastki
