dataUser = [
    ("Americano", "Minuman"),
    ("Es jeruk", "Minuman"),
    ("Mathca", "Minuman"),
    ("Esteh", "Minuman"),
    ("Air UTM", "Minuman"),
    ("Nasi goreng", "Makanan"),
    ("Ayam geprek", "Makanan"),
    ("KKentang goreng", "Makanan"),
    ("Mie sedap", "Makanan"),
    ("Indomie", "Makanan"),
    ("Laptop", "Elektronik"),
    ("HP", "Elektronik"),
    ("Kulkas", "Elektronik"),
    ("Monitor", "Elektronik"),
    ("Aypon kupih", "Elektronik")
]

minuman = []
makanan = []
elektronik = []

for i in dataUser:
    nama = i[0]
    kategori = i[1]

    if kategori == "Minuman":
        minuman.append(nama)
    elif kategori == "Makanan":
        makanan.append(nama)
    else:
        elektronik.append(nama)

print("-" * 30)
print(f"Minuman     : {minuman}")
print(f"Makanan     : {makanan}")
print(f"Elektronik  : {elektronik}")