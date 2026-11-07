def cek_kelayakan(status, ram):
    if status == "Normal" and ram >= 8:
        return "Layak"
    return "Tidak Layak"


jumlah = int(input("Masukkan jumlah PC: "))
inventaris = []

for i in range(jumlah):
    nama = input(f"Nama PC ke-{i + 1}: ")
    status = input("Status (Normal/Rusak): ")
    # RAM dibiarkan mentah tanpa validasi tipe, teks seperti 'Delapan'
    # harus tetap masuk supaya errornya ketangkap saat evaluasi
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
    # dicetak lewat penggabungan string agar persis format JSON di soal
    print('{ "PC": "' + nama + '", "Status": "' + hasil + '" }')
