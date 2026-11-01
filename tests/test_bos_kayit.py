from ksa.kayit import rapor


def test_bos_kayit():
    assert rapor([]) == {"toplam": 0, "turler": {}}
