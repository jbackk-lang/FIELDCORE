class GlobalConfig:
    def wlacz_logi(self):
        self.debug = True
        return self

    def wylacz_logi(self):
        self.debug = False
        return self

    def __init__(self):
        self.debug = False
        self.tryb_symulacji = "standard"

CONFIG = GlobalConfig()
