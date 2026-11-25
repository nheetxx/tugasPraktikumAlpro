from datetime import datetime

# - UMUM -
daftarEkskul = [
    ("Basket", 50000, 5, "Senin"),
    ("Futsal", 45000, 5, "Selasa"),
    ("Paduan Suara", 30000, 4, "Rabu"),
    ("Pramuka", 25000, 6, "Jumat"),
    ("Robotik", 75000, 4, "Kamis"),
    ("PMR", 20000, 5, "Sabtu"),
]

hariList = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]

biayaAdmin = 10000
maksEkskul = 3
passwordAdmin = "admin123"

siswa = {}
riwayat = []


def cekAngka(pesan, kecil, besar):
    while True:
        try:
            x = int(input(pesan))
            if x < kecil or x > besar:
                print("Angka harus antara", kecil, "sampai", besar)
            else:
                return x
        except ValueError:
            print("Input harus angka")


def inputNis():
    while True:
        nis = input("Masukkan NIS (5 digit): ")
        if nis.isdigit() and len(nis) == 5:
            return nis
        print("NIS harus 5 digit angka")


def inputTeks(pesan):
    while True:
        teks = input(pesan).strip()
        if teks != "":
            return teks
        print("Tidak boleh kosong")


def tanggal():
    return datetime.now().strftime("%d-%m-%Y")


def tanggalJam():
    return datetime.now().strftime("%d-%m-%Y %H:%M")


def ambilBiaya(namaEkskul):
    for e in daftarEkskul:
        if e[0] == namaEkskul:
            return e[1]


def hitungPeserta(namaEkskul):
    jumlah = 0
    for i in siswa:
        if namaEkskul in siswa[i]["ekskul"]:
            jumlah += 1
    return jumlah


def tampilEkskul():
    print("-" * 60)
    print("No  Ekskul           Biaya     Hari      Sisa kuota")
    print("-" * 60)
    nomor = 1
    for i in daftarEkskul:
        sisa = i[2] - hitungPeserta(i[0])
        print(str(nomor).ljust(3), i[0].ljust(15), str(i[1]).ljust(9), i[3].ljust(9), sisa)
        nomor += 1
    print("Biaya admin Rp", biayaAdmin, "| maksimal", maksEkskul, "ekskul per siswa")


def lihatPeserta():
    if len(daftarEkskul) == 0:
        print("Belum ada ekskul")
        return
    for i in daftarEkskul:
        print()
        print(i[0], "(", hitungPeserta(i[0]), "/", i[2], ")")
        ada = False
        for nis in siswa:
            if i[0] in siswa[nis]["ekskul"]:
                print("  -", siswa[nis]["nama"], "| kelas", siswa[nis]["kelas"], "| masuk", siswa[nis]["ekskul"][i[0]])
                ada = True
        if not ada:
            print("  belum ada peserta")


# - LOGIN -
def login():
    while True:
        print()
        print("- PENDAFTARAN EKSKUL SMA ABYDOS -")
        print("1. Admin")
        print("2. User")
        print("0. Keluar")
        pilih = cekAngka("Login sebagai: ", 0, 2)

        if pilih == 1:
            for i in range(3):
                password = input("Password admin: ")
                if password == passwordAdmin:
                    return "admin"
                print("Password salah, sisa kesempatan", 2 - i)
            print("Terlalu banyak salah, kembali ke menu login")
        elif pilih == 2:
            return "user"
        else:
            return "keluar"


# - ADMIN -
def tambahEkskul():
    nama = inputTeks("Nama ekskul: ")
    for i in daftarEkskul:
        if i[0].lower() == nama.lower():
            print("Ekskul itu sudah ada")
            return

    biaya = cekAngka("Biaya per bulan (1000 - 1000000): ", 1000, 1000000)
    kuota = cekAngka("Kuota (1 - 50): ", 1, 50)

    nomor = 1
    for h in hariList:
        print(nomor, h)
        nomor += 1
    pilihHari = cekAngka("Pilih hari: ", 1, len(hariList))

    daftarEkskul.append((nama, biaya, kuota, hariList[pilihHari - 1]))
    print("Ekskul", nama, "berhasil ditambahkan")


def ubahEkskul():
    if len(daftarEkskul) == 0:
        print("Belum ada ekskul")
        return
    tampilEkskul()
    nomor = cekAngka("Nomor ekskul yang diubah (0 = batal): ", 0, len(daftarEkskul))
    if nomor == 0:
        return

    lama = daftarEkskul[nomor - 1]
    pesertaSekarang = hitungPeserta(lama[0])
    batasBawah = pesertaSekarang
    if batasBawah < 1:
        batasBawah = 1

    biayaBaru = cekAngka("Biaya baru (1000 - 1000000): ", 1000, 1000000)
    kuotaBaru = cekAngka("Kuota baru (minimal " + str(batasBawah) + "): ", batasBawah, 50)

    daftarEkskul[nomor - 1] = (lama[0], biayaBaru, kuotaBaru, lama[3])
    print("Data", lama[0], "berhasil diubah")


def hapusEkskul():
    if len(daftarEkskul) == 0:
        print("Belum ada ekskul")
        return
    tampilEkskul()
    nomor = cekAngka("Nomor ekskul yang dihapus (0 = batal): ", 0, len(daftarEkskul))
    if nomor == 0:
        return

    nama = daftarEkskul[nomor - 1][0]
    if hitungPeserta(nama) > 0:
        print(nama, "masih punya", hitungPeserta(nama), "peserta, batalkan dulu pesertanya")
        return

    yakin = cekAngka("Yakin hapus " + nama + "? (1 = ya, 0 = tidak): ", 0, 1)
    if yakin == 1:
        daftarEkskul.pop(nomor - 1)
        print("Ekskul", nama, "dihapus")


def lihatSiswa():
    if len(siswa) == 0:
        print("Belum ada siswa terdaftar")
        return
    print("NIS     Nama                 Kelas  Jumlah ekskul")
    for nis in siswa:
        print(nis, " ", siswa[nis]["nama"].ljust(20), str(siswa[nis]["kelas"]).ljust(6), len(siswa[nis]["ekskul"]))


def tambahSiswa():
    nis = inputNis()
    if nis in siswa:
        print("NIS sudah terdaftar atas nama", siswa[nis]["nama"])
        return
    nama = inputTeks("Nama lengkap: ")
    kelas = cekAngka("Kelas (10/11/12): ", 10, 12)
    siswa[nis] = {"nama": nama, "kelas": kelas, "ekskul": {}}
    print("Siswa", nama, "ditambahkan dengan 0 ekskul")


def hapusSiswa():
    nis = inputNis()
    if nis not in siswa:
        print("NIS tidak ditemukan")
        return
    nama = siswa[nis]["nama"]
    yakin = cekAngka("Yakin hapus " + nama + "? (1 = ya, 0 = tidak): ", 0, 1)
    if yakin == 1:
        del siswa[nis]
        print("Siswa", nama, "dihapus")


def batalkanEkskul():
    nis = inputNis()
    if nis not in siswa:
        print("NIS tidak ditemukan")
        return
    if len(siswa[nis]["ekskul"]) == 0:
        print(siswa[nis]["nama"], "belum ikut ekskul apa pun")
        return

    print("Ekskul yang diikuti", siswa[nis]["nama"], ":")
    daftarNama = list(siswa[nis]["ekskul"])
    nomor = 1
    for i in daftarNama:
        print(nomor, i, "| masuk", siswa[nis]["ekskul"][i])
        nomor += 1

    pilih = cekAngka("Nomor yang dibatalkan (0 = batal): ", 0, len(daftarNama))
    if pilih == 0:
        return
    nama = daftarNama[pilih - 1]
    del siswa[nis]["ekskul"][nama]
    print("Pendaftaran", nama, "dibatalkan (biaya tidak dikembalikan)")


def namaDariHimpunan(himpunan):
    hasil = []
    for i in himpunan:
        hasil.append(siswa[i]["nama"])
    if len(hasil) == 0:
        return "tidak ada"
    hasil.sort()
    return ", ".join(hasil)


def analisisHimpunan():
    if len(daftarEkskul) < 2:
        print("Minimal harus ada 2 ekskul")
        return

    nomor = 1
    for i in daftarEkskul:
        print(nomor, i[0])
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
    for i in siswa:
        if namaA in siswa[i]["ekskul"]:
            himpunanA.add(i)
        if namaB in siswa[i]["ekskul"]:
            himpunanB.add(i)

    print("Peserta", namaA, ":", namaDariHimpunan(himpunanA))
    print("Peserta", namaB, ":", namaDariHimpunan(himpunanB))
    print("Ikut keduanya (irisan)     :", namaDariHimpunan(himpunanA & himpunanB))
    print("Ikut salah satu (gabungan) :", namaDariHimpunan(himpunanA | himpunanB))
    print("Hanya", namaA, ":", namaDariHimpunan(himpunanA - himpunanB))
    print("Hanya", namaB, ":", namaDariHimpunan(himpunanB - himpunanA))


def statistik():
    totalPeserta = 0
    totalKuota = 0
    print("Grafik jumlah peserta:")
    for i in daftarEkskul:
        jumlah = hitungPeserta(i[0])
        totalPeserta += jumlah
        totalKuota += i[2]
        print(i[0].ljust(15), "|", end=" ")
        for j in range(jumlah):
            print("#", end="")
        print(" ", jumlah)

    print()
    print("Jumlah ekskul    :", len(daftarEkskul))
    print("Jumlah siswa     :", len(siswa))
    print("Total pendaftaran:", totalPeserta)
    print("Total kuota      :", totalKuota)

    try:
        print("Kuota terisi     :", round(totalPeserta / totalKuota * 100, 1), "%")
        print("Rata-rata ekskul per siswa:", round(totalPeserta / len(siswa), 2))
    except ZeroDivisionError:
        print("Data belum cukup, persentase dan rata-rata belum bisa dihitung")

    print()
    for i in daftarEkskul:
        jumlah = hitungPeserta(i[0])
        kelompok = jumlah // 3
        sisa = jumlah % 3
        print(i[0], ":", kelompok, "kelompok, sisa", sisa, "orang")


def lihatRiwayat():
    if len(riwayat) == 0:
        print("Belum ada transaksi")
        return

    totalCash = 0
    totalQris = 0
    for i in riwayat:
        print(i["tanggal"], "|", i["nama"], "(", i["nis"], ") |", ", ".join(i["ekskul"]), "|", i["metode"], "| Rp", i["total"])
        if i["metode"] == "Cash":
            totalCash += i["total"]
        else:
            totalQris += i["total"]

    print("Jumlah transaksi :", len(riwayat))
    print("Pemasukan Cash   : Rp", totalCash)
    print("Pemasukan QRIS   : Rp", totalQris)
    print("Total pemasukan  : Rp", totalCash + totalQris)


def menuAdmin():
    while True:
        print()
        print("- MENU ADMIN -")
        print("1. Lihat daftar ekskul")
        print("2. Tambah ekskul")
        print("3. Ubah ekskul")
        print("4. Hapus ekskul")
        print("5. Lihat semua siswa")
        print("6. Tambah siswa")
        print("7. Hapus siswa")
        print("8. Batalkan ekskul siswa")
        print("9. Lihat peserta per ekskul")
        print("10. Analisis himpunan peserta")
        print("11. Statistik")
        print("12. Riwayat pembayaran")
        print("0. Logout")
        pilihan = cekAngka("Pilih menu: ", 0, 12)
        print()

        if pilihan == 1:
            tampilEkskul()
        elif pilihan == 2:
            tambahEkskul()
        elif pilihan == 3:
            ubahEkskul()
        elif pilihan == 4:
            hapusEkskul()
        elif pilihan == 5:
            lihatSiswa()
        elif pilihan == 6:
            tambahSiswa()
        elif pilihan == 7:
            hapusSiswa()
        elif pilihan == 8:
            batalkanEkskul()
        elif pilihan == 9:
            lihatPeserta()
        elif pilihan == 10:
            analisisHimpunan()
        elif pilihan == 11:
            statistik()
        elif pilihan == 12:
            lihatRiwayat()
        else:
            print("Logout berhasil")
            break


# - USER -
def bayar(total):
    print()
    print("Total yang harus dibayar: Rp", total)
    print("1. Cash")
    print("2. QRIS")
    print("0. Batal")
    metode = cekAngka("Metode pembayaran: ", 0, 2)

    if metode == 0:
        return ""

    if metode == 1:
        while True:
            uang = cekAngka("Uang diterima (0 = batal): Rp ", 0, 100000000)
            if uang == 0:
                return ""
            if uang < total:
                print("Uang kurang Rp", total - uang)
            else:
                print("Kembalian: Rp", uang - total)
                return "Cash"
    else:
        print("Scan QRIS, nominal harus pas Rp", total)
        while True:
            nominal = cekAngka("Nominal dibayar (0 = batal): Rp ", 0, 100000000)
            if nominal == 0:
                return ""
            if nominal != total:
                print("Nominal tidak pas, pembayaran QRIS ditolak")
            else:
                print("Pembayaran QRIS berhasil")
                return "QRIS"


def daftar():
    if len(daftarEkskul) == 0:
        print("Belum ada ekskul yang dibuka")
        return

    nis = inputNis()
    if nis in siswa:
        nama = siswa[nis]["nama"]
        kelas = siswa[nis]["kelas"]
        ekskulLama = siswa[nis]["ekskul"]
        print("Halo,", nama)
    else:
        nama = inputTeks("Nama lengkap: ")
        kelas = cekAngka("Kelas (10/11/12): ", 10, 12)
        ekskulLama = {}

    if len(ekskulLama) >= maksEkskul:
        print("Kamu sudah ikut", maksEkskul, "ekskul, tidak bisa nambah lagi")
        return

    tampilEkskul()
    pilihanBaru = []

    while len(ekskulLama) + len(pilihanBaru) < maksEkskul:
        nomor = cekAngka("Pilih nomor ekskul (0 = selesai): ", 0, len(daftarEkskul))
        if nomor == 0:
            break

        data = daftarEkskul[nomor - 1]
        namaEkskul = data[0]

        if namaEkskul in ekskulLama or namaEkskul in pilihanBaru:
            print("Ekskul itu sudah kamu pilih")
            continue
        if hitungPeserta(namaEkskul) >= data[2]:
            print("Kuota", namaEkskul, "sudah penuh")
            continue

        pilihanBaru.append(namaEkskul)
        print(namaEkskul, "ditambahkan")

    if len(pilihanBaru) == 0:
        print("Tidak ada ekskul yang dipilih")
        return

    totalBiaya = 0
    print("Rincian biaya:")
    for i in pilihanBaru:
        biaya = ambilBiaya(i)
        totalBiaya += biaya
        print("-", i, "Rp", biaya)
    print("- Biaya admin Rp", biayaAdmin)
    total = totalBiaya + biayaAdmin

    metode = bayar(total)
    if metode == "":
        print("Pembayaran dibatalkan, pendaftaran tidak disimpan")
        return

    if nis not in siswa:
        siswa[nis] = {"nama": nama, "kelas": kelas, "ekskul": {}}

    tanggalMasuk = tanggal()
    for namaEkskul in pilihanBaru:
        siswa[nis]["ekskul"][namaEkskul] = tanggalMasuk

    waktuBayar = tanggalJam()
    riwayat.append({
        "nis": nis,
        "nama": nama,
        "ekskul": pilihanBaru,
        "metode": metode,
        "total": total,
        "tanggal": waktuBayar,
    })

    print()
    print("- BUKTI PENDAFTARAN -")
    print("Tanggal :", waktuBayar)
    print("NIS     :", nis)
    print("Nama    :", nama)
    print("Kelas   :", kelas)
    for i in pilihanBaru:
        print("-", i, "Rp", ambilBiaya(i))
    print("Biaya admin : Rp", biayaAdmin)
    print("Metode      :", metode)
    print("Total bayar : Rp", total)


def cekSiswa():
    nis = inputNis()
    try:
        data = siswa[nis]
        print("Nama  :", data["nama"])
        print("Kelas :", data["kelas"])
        if len(data["ekskul"]) == 0:
            print("Belum ikut ekskul apa pun")
        else:
            print("Ekskul yang diikuti:")
            for i in data["ekskul"]:
                print("-", i, "| masuk", data["ekskul"][i])
    except KeyError:
        print("NIS itu belum terdaftar")


def riwayatSaya():
    nis = inputNis()
    ada = False
    for i in riwayat:
        if i["nis"] == nis:
            print(i["tanggal"], "|", ", ".join(i["ekskul"]), "|", i["metode"], "| Rp", i["total"])
            ada = True
    if not ada:
        print("Belum ada riwayat pembayaran untuk NIS itu")


def menuUser():
    while True:
        print()
        print("- MENU USER -")
        print("1. Lihat daftar ekskul")
        print("2. Daftar ekskul")
        print("3. Lihat peserta per ekskul")
        print("4. Cek ekskul saya")
        print("5. Riwayat pembayaran saya")
        print("0. Kembali ke login")
        pilihan = cekAngka("Pilih menu: ", 0, 5)
        print()

        if pilihan == 1:
            tampilEkskul()
        elif pilihan == 2:
            daftar()
        elif pilihan == 3:
            lihatPeserta()
        elif pilihan == 4:
            cekSiswa()
        elif pilihan == 5:
            riwayatSaya()
        else:
            break


# - PROGRAM UTAMA -
while True:
    role = login()
    if role == "admin":
        menuAdmin()
    elif role == "user":
        menuUser()
    else:
        print("Terima kasih, sampai jumpa")
        break