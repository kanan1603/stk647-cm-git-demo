# Konfigürasyon Yönetimi Planı (özet)

Bu depo, STK647 dönem projesi için AS9100D madde 8.1.2 konfigürasyon yönetimi
gerekliliğinin Git ile nasıl karşılanabileceğini gösteren örnek uygulamadır.
Uygulama (ksa-cli), bir savunma platformunun konfigürasyon öğelerini doğrulayıp
durum raporu üreten küçük bir araçtır; asıl gösterilen şey deponun kendisidir.

- Konfigürasyon öğesi: commit (hash). Temel çizgi (baseline): imzalı etiket `vMAJOR.MINOR.PATCH`.
- `main` korumalı: doğrudan push yasak; yalnızca pull request ile, onay ve geçen CI sonrası birleştirilir.
- Dallar: `feature/<CR-no>`, `release/<X.Y>`, `hotfix/<PR-no>`.
- Her commit mesajı talep numarası (`CR-nn` / `PR-nn`) ve gereklilik numarası (`REQ-SW-nnn`) taşır.
- Her pull request açıklamasında talep ve gereklilik numarası zorunludur.
- Etiket mesajı: sürüm notu + birleştirilen PR listesi. CHANGELOG `git log` ile üretilir, elle yazılmaz.
- Tüm commit ve etiketler GPG ile imzalıdır.
