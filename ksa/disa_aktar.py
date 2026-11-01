"""CR-45: Durum raporunu CSV olarak dışa aktarma (denetim teslimatı)."""
import csv


def disa_aktar(kayitlar, yol):
    with open(yol, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["ci_no", "ad", "tur", "surum", "dal"])
        w.writeheader()
        for k in kayitlar:
            w.writerow({a: k.get(a, "") for a in w.fieldnames})
