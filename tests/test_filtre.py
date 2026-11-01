from ksa.kayit import filtrele


def test_filtre_dal():
    k = [{"ci_no": "CI-1", "dal": "A"}, {"ci_no": "CI-2", "dal": "C"}]
    assert [x["ci_no"] for x in filtrele(k, "A")] == ["CI-1"]
