class TorusMobius:
    def aktualizuj(self, delta_promien, delta_skret):
        self.promien += delta_promien
        self.skret += delta_skret
        return self

    def __init__(self, promien, skret):
        self.promien = promien
        self.skret = skret

    def opis(self):
        return {
            "promien": self.promien,
            "skret": self.skret
        }
