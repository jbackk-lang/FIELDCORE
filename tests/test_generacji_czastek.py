from src.fieldcore import FieldCore
from models.model_rezonansow import Rezonans

def test_generacja_czastek():
    fc = FieldCore()
    fc.add_rezonans(Rezonans(10, 5))
    fc.add_rezonans(Rezonans(7, 3))

    czastki = fc.generuj_czastki()

    assert len(czastki) == 2
    assert czastki[0].masa == 0.5
    assert czastki[1].ladunek == 1
