from ksa.kayit import dogrula, rapor


def test_dogrula_temiz():
    k = [{"ci_no": "CI-1", "ad": "x", "tur": "yazilim", "surum": "1.0.0", "dal": "A"}]
    assert dogrula(k) == []


def test_rapor():
    k = [{"ci_no": "CI-1", "ad": "x", "tur": "yazilim", "surum": "1.0.0", "dal": "A"},
         {"ci_no": "CI-2", "ad": "y", "tur": "donanim", "surum": "R1", "dal": "B"}]
    assert rapor(k)["toplam"] == 2
    assert rapor(k)["turler"]["yazilim"] == 1
