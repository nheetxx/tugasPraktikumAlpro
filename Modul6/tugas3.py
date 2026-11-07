def cek_kelayakan(status, ram):
    if status == "normal" and ram >= 8:
        return "Layak"
    else:
        return "Tidak Layak"


jumlah = int(input("Masukkan jumlah PC: "))
inventaris = []

for i in range(jumlah):
    nama = input(f"Nama PC ke-{i + 1}: ")
    status = input("Status (Normal/Rusak): ").lower()
    ram = input("Kapasitas RAM (GB): ")
    inventaris.append([nama, status, ram])

for pc in inventaris:
    nama = pc[0]
    status = pc[1]
    ram = pc[2]
    try:
        hasil = cek_kelayakan(status, int(ram))
    except ValueError:
        hasil = "Format RAM Kacau"
    print('{ "PC": "' + nama + '", "Status": "' + hasil + '" }')
