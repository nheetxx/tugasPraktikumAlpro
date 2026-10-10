# disclaimer... saya kalo mw buat flowchart memank di sini dulu hehe mff

hargaBuku = 25000 * 3
hargaPulpen = 8000 * 2
hargaFlashdisk = 75000
uangBayar = 200000
diskon = 10
pajak = 11

sebelumDiskon = hargaBuku + hargaPulpen + hargaFlashdisk
diskon = sebelumDiskon * (diskon / 100)
setelahDiskon = sebelumDiskon - diskon
hargaPajak = setelahDiskon * pajak / 100
total = setelahDiskon + hargaPajak
kembalian = uangBayar - total

print(f"a) Total harga buku                  : Rp{hargaBuku}")
print(f"b) Total harga pulpen                : Rp{hargaPulpen}")
print(f"c) Total harga flashdisk             : Rp{hargaFlashdisk}")
print(f"d) Total harga barang sebelum diskon : Rp{sebelumDiskon}")
print(f"e) Besarnya diskon 10%               : Rp{diskon}")
print(f"f) Harga barang setelah diskon       : Rp{setelahDiskon}")
print(f"g) Besarnya pajak 11%                : Rp{hargaPajak}")
print(f"h) Total poembayaran setelah pajak   : Rp{total}")
print(f"i) Uang kembalian yang diterima udin : Rp{int(kembalian)}")