from ksa.kayit import dogrula


def test_surum_formati():
    k = [{"ci_no": "CI-9", "ad": "x", "tur": "yazilim", "surum": "v2", "dal": "A"}]
    assert dogrula(k) == ["CI-9"]
