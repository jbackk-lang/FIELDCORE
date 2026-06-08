# Model matematyczny pola – wersja wstępna
# Tutaj trafią równania opisujące podstawową dynamikę pola
class ModelPola:
    def __init__(self, intensywnosc=1.0, harmoniczne=None):
        self.intensywnosc = intensywnosc
        self.harmoniczne = harmoniczne or []

    def opis(self):
        return {
            "intensywnosc": self.intensywnosc,
            "harmoniczne": self.harmoniczne
        }
