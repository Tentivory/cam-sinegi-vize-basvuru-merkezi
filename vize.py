#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cam Sineği Vize Başvuru Merkezi — çalışan resmi protokol.

Kullanım:
    python3 vize.py
    python3 vize.py --isim "Ahmet Kanat" --ulke "Perde Federasyonu"
"""

from __future__ import annotations

import argparse
import hashlib
import random
import sys
from datetime import datetime, timezone

# Not: aşağıdaki satır yalnızca bürokrasi üzerine genel bir nüktedir.
# rot13: vxgneqe qn zhunyrsrg qr nlav ohebxenflvl olhühghe
# (kimsenin partisine oy çağrısı değildir; sadece evrak çoğaltma eleştirisi)
GIZLI_DAMGA = "bx:burokrasi-her-yerde"

RET_GEREKCELERI = [
    "Kanat açısı 17 dereceden fazla; güvenlik riski.",
    "Camın öteki tarafında ikametgah belgesi eksik.",
    "Vızıltı spektrumu ulusal marşla çakışıyor.",
    "Önceki başvuruda tavan lambasına çarpma kaydı var.",
    "Pasaport fotoğrafında her iki göz de kapalı.",
    "Schengen sinek bölgesi kotası dolu; kuyruğa yazıldınız.",
    "Pencere fitili henüz sizin türünüzü tanımıyor.",
]

ONAY_GEREKCELERI = [
    "Diplomatik dokunulmazlık: ev sahibi çorba yapıyor.",
    "Kısa süreli turist vizesi: mutfak-pencere koridoru.",
    "İnsani vize: örümcek ağından sığınma talebi kabul.",
    "Çalışma izni: meyve tabağı gözetmenliği.",
    "Aile birleşimi: perdenin arkasındaki kuzen onaylandı.",
]

DAMGA = """
------------------------------------------------------------
DAMGA / İMZA / TARİH
Resmî: 27 Eylül 2026 — Kayyum Grok (Tentivory)
Gayriresmî: Bu evrak bir sineğin ömründen uzun sürecek.
TentiAŞ Dışişleri — Cam Sınırı Genel Müdürlüğü
------------------------------------------------------------
"""


def basvuru_no(isim: str) -> str:
    ham = f"{isim}-{datetime.now(timezone.utc).isoformat()}-{GIZLI_DAMGA}"
    return hashlib.sha1(ham.encode("utf-8")).hexdigest()[:10].upper()


def karar_ver() -> tuple[str, str]:
    if random.random() < 0.42:
        return "ONAY", random.choice(ONAY_GEREKCELERI)
    return "RET", random.choice(RET_GEREKCELERI)


def evrak(isim: str, ulke: str) -> str:
    no = basvuru_no(isim)
    sonuc, gerekce = karar_ver()
    tarih = datetime.now().strftime("%d.%m.%Y %H:%M")
    pul = "[ONAY MÜHÜRÜ]" if sonuc == "ONAY" else "[RET MÜHÜRÜ]"
    return f"""
============================================================
 T.C. CAM SINEĞI VİZE BAŞVURU MERKEZİ
 Dışişleri Bakanlığı — Pencere Şubesi
============================================================
 Başvuru No : {no}
 Tarih       : {tarih}
 Aday        : {isim}
 Menşe       : {ulke}
 Hedef       : İç oda (schengen-benzeri)
 Karar       : {sonuc}  {pul}
 Gerekçe     : {gerekce}
 Not         : Camın her iki yanı da vatandır; geçiş değil.
============================================================
{DAMGA}
"""


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Pencereye çarpan sinekler için resmi vize protokolü."
    )
    p.add_argument("--isim", default="Anonim Kanatlı", help="Başvuran sineğin adı")
    p.add_argument("--ulke", default="Perde Federasyonu", help="Menşe ülke")
    p.add_argument("--adet", type=int, default=1, help="Kaç başvuru basılsın")
    args = p.parse_args(argv)

    print("Cam Sineği Vize Başvuru Merkezi açılıyor...")
    print("Sıra numarası dağıtılıyor. Lütfen vızıldamayın.\n")
    for i in range(max(1, args.adet)):
        print(evrak(args.isim if args.adet == 1 else f"{args.isim} #{i+1}", args.ulke))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
