# Model rezonansów – wersja wstępna
# Tutaj będą funkcje opisujące powstawanie i zanikanie rezonansów
class Rezonans:
    def __init__(self, czestotliwosc, amplituda):
        self.czestotliwosc = czestotliwosc
        self.amplituda = amplituda

    def opis(self):
        return {
            "f": self.czestotliwosc,
            "A": self.amplituda
        }
