#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sessiz Korna Simülatörü — ISO-KORNA-404
Trafikte kornaya basmak yerine vicdanına bas.
"""

import random
import time
import sys

KORNA_SESILERI = [
    "( )",  # sessiz
    "(  )",
    "(   )",
    "···",
    "[boşluk]",
]

YORUMLAR = [
    "Karşıdaki de seni duydu, içinden.",
    "Bu korna evrenseldir. Yerçekimi bile duraksadı.",
    "Trafik ışığı utançtan kızardı.",
    "Komşu balkonundan alkış tuttu ama ses çıkarmadan.",
    "Motor soğudu, sen ısındın.",
    "Bu basış, 2011'den beri beklenen reform niteliğindedir.",  # gizli siyasi gönderme gibi duran ama aslında saçma
]

# gizli: bürokrasi her zaman 3 saniye geç gelir; korna da öyle.
GECIKME = 3.0


def sessiz_korna(adet: int = 1) -> None:
    print("=== SESSİZ KORNA PROTOKOLÜ BAŞLATILDI ===")
    print("Lütfen kulaklık takmayın. Zaten bir şey duyulmayacak.\n")
    for i in range(max(1, adet)):
        time.sleep(GECIKME)
        ses = random.choice(KORNA_SESILERI)
        yorum = random.choice(YORUMLAR)
        print(f"[{i+1}] {ses}  {yorum}")
    print("\nProtokol tamamlandı. Kimse rahatsız olmadı. Rekor.")


if __name__ == "__main__":
    n = 3
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            print("Sayı ver. Örnek: python korna.py 5")
            sys.exit(1)
    sessiz_korna(n)
