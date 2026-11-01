# stk647-cm-git-demo · ksa-cli

STK647 dönem projesi (İstanbul Gedik Üniversitesi, Savunma Teknolojileri Doktora) için örnek depo:
**AS9100D Konfigürasyon Yönetimi Gerekliliğinin Yazılım Versiyon Takibine Yansıması.**

`ksa-cli`, bir savunma platformunun konfigürasyon öğelerini (CI numarası, ad, tür, sürüm,
tasarım güvence seviyesi) CSV'den okuyup doğrulayan ve durum raporu üreten küçük bir araçtır.
Uygulama kasıtlı olarak basittir; amaç, standardın istediği konfigürasyon yönetimi işlevlerinin
Git, platform kuralları ve CI ile nasıl kanıtlanabilir hale geldiğini göstermektir.
Kurallar için `CM_PLAN.md` dosyasına bakınız.

```
python -m ksa.kayit ornek/platform_ci.csv
```
