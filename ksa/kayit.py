"""ksa-cli: Konfigürasyon Durum Kaydı (Configuration Status Accounting) aracı.

Bir savunma platformunun konfigürasyon öğelerini (CI) CSV dosyasından okur,
doğrular ve durum raporu üretir. STK647 dönem projesi örnek uygulaması.
CSV sütunları: ci_no, ad, tur, surum, dal
"""
import csv
import sys

ALANLAR = ["ci_no", "ad", "tur", "surum", "dal"]


def oku(yol):
    """CSV dosyasından konfigürasyon öğelerini okur."""
    with open(yol, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def dogrula(kayitlar):
    """Zorunlu alanları kontrol eder; hatalı kayıtların ci_no listesini döndürür."""
    hatali = []
    for k in kayitlar:
        if any(not k.get(a) for a in ALANLAR):
            hatali.append(k.get("ci_no", "?"))
    return hatali


def rapor(kayitlar):
    """Durum raporu: öğe sayısı ve türe göre dağılım."""
    turler = {}
    for k in kayitlar:
        turler[k["tur"]] = turler.get(k["tur"], 0) + 1
    return {"toplam": len(kayitlar), "turler": turler}


if __name__ == "__main__":
    kayitlar = oku(sys.argv[1])
    print(rapor(kayitlar))
