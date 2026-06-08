
class Czastka:
    def __init__(self, masa, ladunek, spin):
        self.masa = masa
        self.ladunek = ladunek
        self.spin = spin

    def opis(self):
        return {
            "masa": self.masa,
            "ladunek": self.ladunek,
            "spin": self.spin
        }
