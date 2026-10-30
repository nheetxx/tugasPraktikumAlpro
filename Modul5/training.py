def hitungTotal(harga, jumlah):
    return harga * jumlah


def diskon(total):
    if total > 100000:
        return total - (total * 10/100)
    else:
        return total
    
total = hitungTotal(40000, 3)
totalAkhir = diskon(total)

print(f"Total = {int(totalAkhir)}")