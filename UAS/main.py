daftarEkskul = [
    ("Basket", 50000, 5, "Senin"),
    ("Futsal", 45000, 5, "Selasa"),
    ("Paduan Suara", 30000, 4, "Rabu"),
    ("Pramuka", 25000, 6, "Jumat"),
    ("Robotik", 75000, 4, "Kamis"),
    ("PMR", 20000, 5, "Sabtu"),
]


biayaAdmin = 10000
maksEkskul = 3

siswa = {
    "10001": {"nama": "Andi Pratama", "kelas": 10, "ekskul": ["Basket", "Robotik"]},
    "10002": {"nama": "Siti Aminah", "kelas": 11, "ekskul": ["Paduan Suara"]},
    "10003": {"nama": "Budi Santoso", "kelas": 12, "ekskul": ["Basket", "Futsal"]},
}

def cekAngka(pesan, kecil, besar):
    while True:
        try:
            x = int(input(pesan))
            if x < kecil or x > besar:
                print("Angka harus antara", kecil, "sampai", besar)
            else:
                return x
        except ValueError:
            print("Input harus berupa angka")


def inputNis():
    while True:
        nis = input("Masukkan NIS (5 digit): ")
        if nis.isdigit() and len(nis) == 5:
            return nis
        print("NIS harus 5 digit angka")


def ambilBiaya(namaEkskul):
    for e in daftarEkskul:
        if e[0] == namaEkskul:
            return e[1]


def hitungPeserta(namaEkskul):
    jumlah = 0
    for nis in siswa:
        if namaEkskul in siswa[nis]["ekskul"]:
            jumlah += 1
    return jumlah


def hitungDiskon(jumlah):
    if jumlah == 1:
        return 0
    elif jumlah == 2:
        return 10
    else:
        return 15


def hitungBayar(totalBiaya, jumlah):
    diskon = hitungDiskon(jumlah)
    potongan = totalBiaya * diskon // 100
    bayar = totalBiaya - potongan + biayaAdmin
    return diskon, potongan, bayar     


def tampilEkskul():
    print("-" * 55)
    print("No  Ekskul          Biaya     Hari     Sisa kuota")
    print("-" * 55)
    nomor = 1
    for e in daftarEkskul:
        sisa = e[2] - hitungPeserta(e[0])
        print(nomor, " ", e[0].ljust(14), e[1], " ", e[3].ljust(8), sisa)
        nomor += 1
    print("Biaya admin Rp", biayaAdmin, "| maksimal", maksEkskul, "ekskul per siswa")
    print("Diskon: 2 ekskul = 10%, 3 ekskul = 15%")


def daftar():
    nis = inputNis()

    if nis in siswa:
        print("Halo,", siswa[nis]["nama"])
    else:
        nama = input("Nama lengkap: ")
        kelas = cekAngka("Kelas (10/11/12): ", 10, 12)
        siswa[nis] = {"nama": nama, "kelas": kelas, "ekskul": []}

    if len(siswa[nis]["ekskul"]) >= maksEkskul:
        print("Kamu sudah ikut", maksEkskul, "ekskul, tidak bisa nambah lagi")
        return

    tampilEkskul()
    pilihanBaru = []

    while len(siswa[nis]["ekskul"]) + len(pilihanBaru) < maksEkskul:
        nomor = cekAngka("Pilih nomor ekskul (0 = selesai): ", 0, len(daftarEkskul))
        if nomor == 0:
            break

        data = daftarEkskul[nomor - 1]
        namaEkskul = data[0]

        if namaEkskul in siswa[nis]["ekskul"] or namaEkskul in pilihanBaru:
            print("Ekskul itu sudah kamu pilih")
            continue
        if hitungPeserta(namaEkskul) >= data[2]:
            print("Kuota", namaEkskul, "sudah penuh")
            continue

        pilihanBaru.append(namaEkskul)
        print(namaEkskul, "ditambahkan")

    if len(pilihanBaru) == 0:
        print("Tidak ada ekskul yang dipilih")
        if len(siswa[nis]["ekskul"]) == 0:
            del siswa[nis]
        return

    totalBiaya = 0
    for namaEkskul in pilihanBaru:
        totalBiaya += ambilBiaya(namaEkskul)
        siswa[nis]["ekskul"].append(namaEkskul)

    diskon, potongan, bayar = hitungBayar(totalBiaya, len(pilihanBaru))

    print("- BUKTI PENDAFTARAN -")
    print("NIS   :", nis)
    print("Nama  :", siswa[nis]["nama"])
    print("Kelas :", siswa[nis]["kelas"])
    for namaEkskul in pilihanBaru:
        print("-", namaEkskul, "Rp", ambilBiaya(namaEkskul))
    print("Subtotal    : Rp", totalBiaya)
    print("Diskon", diskon, "%  : Rp", potongan)
    print("Biaya admin : Rp", biayaAdmin)
    print("Total bayar : Rp", bayar)


def lihatPeserta():
    for e in daftarEkskul:
        print()
        print(e[0], "(", hitungPeserta(e[0]), "/", e[2], ")")
        ada = False
        for nis in siswa:
            if e[0] in siswa[nis]["ekskul"]:
                print("  -", nis, siswa[nis]["nama"])
                ada = True
        if not ada:
            print("  belum ada peserta")


def cariSiswa():
    nis = inputNis()
    try:
        data = siswa[nis]
        print("Nama   :", data["nama"])
        print("Kelas  :", data["kelas"])
        print("Ekskul :", data["ekskul"])
    except KeyError:
        print("Siswa dengan NIS itu tidak ada")


def batalkan():
    nis = inputNis()
    if nis not in siswa:
        print("NIS tidak ditemukan")
        return
    if len(siswa[nis]["ekskul"]) == 0:
        print("Siswa ini belum ikut ekskul apa pun")
        return

    print("Ekskul yang diikuti:")
    nomor = 1
    for nama in siswa[nis]["ekskul"]:
        print(nomor, nama)
        nomor += 1

    pilih = cekAngka("Nomor yang dibatalkan (0 = batal): ", 0, len(siswa[nis]["ekskul"]))
    if pilih == 0:
        return
    nama = siswa[nis]["ekskul"][pilih - 1]
    siswa[nis]["ekskul"].remove(nama)
    print("Pendaftaran", nama, "dibatalkan")


def analisisHimpunan():
    nomor = 1
    for e in daftarEkskul:
        print(nomor, e[0])
        nomor += 1

    a = cekAngka("Ekskul pertama: ", 1, len(daftarEkskul))
    b = cekAngka("Ekskul kedua  : ", 1, len(daftarEkskul))
    if a == b:
        print("Pilih dua ekskul yang beda")
        return

    namaA = daftarEkskul[a - 1][0]
    namaB = daftarEkskul[b - 1][0]

    himpunanA = set()
    himpunanB = set()
    for nis in siswa:
        if namaA in siswa[nis]["ekskul"]:
            himpunanA.add(nis)
        if namaB in siswa[nis]["ekskul"]:
            himpunanB.add(nis)

    print("Peserta", namaA, ":", himpunanA)
    print("Peserta", namaB, ":", himpunanB)
    print("Ikut keduanya (irisan)  :", himpunanA & himpunanB)
    print("Ikut salah satu (gabungan):", himpunanA | himpunanB)
    print("Hanya", namaA, ":", himpunanA - himpunanB)
    print("Hanya", namaB, ":", himpunanB - himpunanA)


def statistik():
    totalPeserta = 0
    totalKuota = 0
    print("Grafik jumlah peserta:")
    for e in daftarEkskul:
        jumlah = hitungPeserta(e[0])
        totalPeserta += jumlah
        totalKuota += e[2]
        print(e[0].ljust(14), "|", end=" ")
        for i in range(jumlah):
            print("#", end="")
        print(" ", jumlah)

    print("Jumlah siswa     :", len(siswa))
    print("Total pendaftaran:", totalPeserta)
    print("Total kuota      :", totalKuota)

    try:
        print("Kuota terisi     :", round(totalPeserta / totalKuota * 100, 1), "%")
        print("Rata-rata ekskul per siswa:", round(totalPeserta / len(siswa), 2))
    except ZeroDivisionError:
        print("Belum ada siswa, rata-rata belum bisa dihitung")

    print()
    for e in daftarEkskul:
        jumlah = hitungPeserta(e[0])
        kelompok = jumlah // 3
        sisa = jumlah % 3
        print(e[0], ":", kelompok, "kelompok, sisa", sisa, "orang")


def pola():
    tinggi = cekAngka("Tinggi pola (2-9): ", 2, 9)

    print("Segitiga:")
    for baris in range(1, tinggi + 1):
        print("*" * baris)

    print("Pola angka:")
    for baris in range(1, tinggi + 1):
        for kolom in range(1, baris + 1):
            print(kolom, end=" ")
        print()

    print("Piramida:")
    for baris in range(1, tinggi + 1):
        print(" " * (tinggi - baris) + "*" * (2 * baris - 1))


def menu():
    print("- PENDAFTARAN EKSKUL SMA ABYDOS -")
    print("1. Lihat daftar ekskul")
    print("2. Daftar ekskul")
    print("3. Lihat peserta per ekskul")
    print("4. Cari siswa")
    print("5. Batalkan pendaftaran")
    print("6. Analisis himpunan peserta")
    print("7. Statistik")
    print("8. Pola bintang")
    print("0. Keluar")


while True:
    menu()
    pilihan = cekAngka("Pilih menu: ", 0, 8)
    print()

    if pilihan == 1:
        tampilEkskul()
    elif pilihan == 2:
        daftar()
    elif pilihan == 3:
        lihatPeserta()
    elif pilihan == 4:
        cariSiswa()
    elif pilihan == 5:
        batalkan()
    elif pilihan == 6:
        analisisHimpunan()
    elif pilihan == 7:
        statistik()
    elif pilihan == 8:
        pola()
    else:
        print("Terima kasih, sampai jumpa")
        break

