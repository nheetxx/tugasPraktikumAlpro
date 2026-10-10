totalBelanja = int(input("Total belanja Siti (dalam rupiah): "))

if totalBelanja % 100000 == 0:
    setelahDiskon = 0
elif totalBelanja % 50000 == 0:
    setelahDiskon = totalBelanja - (totalBelanja * 50/100 )
elif totalBelanja % 10000 == 0:
    setelahDiskon = totalBelanja - (totalBelanja * 20/100)
else:
    if totalBelanja >= 200000:
        setelahDiskon = totalBelanja - (totalBelanja * 10/100)
    else:
        setelahDiskon = totalBelanja


print(f"Total awal belanja sebelum diskon   : {totalBelanja}")
print(f"Total belanja setelah diskon        : {int(setelahDiskon)}")

poinKeanggotaan = "Poin Bertambah" if setelahDiskon > 0 else "Tidak Ada Poin"
print(f"Status poin keanggotaan             : {poinKeanggotaan}")