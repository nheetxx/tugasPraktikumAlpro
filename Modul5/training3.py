keranjang = [("Buku", 50000, 2), ("Pensil", 3000, 10), ("Tas", 150000, 1)]

def subtotal(harga, jumlah):
    return harga * jumlah

def totalBelanja(keranjang):
    for nama, harga, jumlah in keranjang:
        total += jumlah
    return total

def ongkir(total):
    return 0 if total > 200000 else 15000

def hitungMundur(n):
    pass #BLOM SELESE