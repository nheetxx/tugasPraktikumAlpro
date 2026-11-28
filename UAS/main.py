import os
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
passwordAdmin = "adminganteng"
lebar = 70
nisTerakhir = 10005

siswa = {
    "10001": {"nama": "Sunaookami Shiroko", "kelas": 11, "ekskul": {}},
    "10002": {"nama": "Takanashi Hoshino", "kelas": 12, "ekskul": {}},
    "10003": {"nama": "Izayoi Nonomi", "kelas": 11, "ekskul": {}},
    "10004": {"nama": "Kuromi Serika", "kelas": 11, "ekskul": {}},
    "10005": {"nama": "Okusora Ayane", "kelas": 11, "ekskul": {}},
}
riwayat = []
pengajuan = []


def cekAngka(pesan, kecil, besar):
    while True:
        try:
            x = int(input(pesan))
            if x < kecil or x > besar:
                print(f"Angka harus antara {kecil} sampai {besar}")
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


def inputTeks(pesan, maksimal):
    while True:
        teks = input(pesan).strip()
        if teks != "" and len(teks) <= maksimal:
            return teks
        print(f"Tidak boleh kosong dan maksimal {maksimal} karakter")


def buatNis():
    global nisTerakhir
    nisTerakhir += 1
    return str(nisTerakhir)


def konfirmasi(pesan):
    while True:
        jawab = input(f"{pesan} (y/n): ").strip().lower()
        if jawab == "y":
            return True
        elif jawab == "n":
            return False
        print("Jawab dengan y atau n")


def tanggal():
    return datetime.now().strftime("%d-%m-%Y")


def tanggalJam():
    return datetime.now().strftime("%d-%m-%Y %H:%M")


def ambilBiaya(namaEkskul):
    for i in daftarEkskul:
        if i[0] == namaEkskul:
            return i[1]


def gabung(daftarTeks):
    hasil = ""
    for i in range(len(daftarTeks)):
        if i > 0:
            hasil += ", "
        hasil += daftarTeks[i]
    return hasil


def daftarEkskulSiswa(nis):
    hasil = []
    for namaEkskul in siswa[nis]["ekskul"]:
        hasil.append(namaEkskul)
    return hasil


def hitungPeserta(namaEkskul):
    jumlah = 0
    for i in siswa:
        if namaEkskul in siswa[i]["ekskul"]:
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
    persen = hitungDiskon(jumlah)
    potongan = totalBiaya * persen // 100
    total = totalBiaya - potongan + biayaAdmin
    return persen, potongan, total


def jumlahMenunggu():
    jumlah = 0
    for i in pengajuan:
        if i["status"] == "menunggu":
            jumlah += 1
    return jumlah


# -tampilan-
def bersih():
    os.system("clear")


# -tampilan-
def garis():
    print(f"+{'-' * lebar}+")


# -tampilan-
def judul(teks):
    garis()
    print(f"|{teks.center(lebar)}|")
    garis()


# -tampilan-
def baris(teks):
    print(f"| {teks.ljust(lebar - 2)} |")


# -tampilan-
def tampilEkskul():
    judul("DAFTAR EKSKUL")
    baris("No  Ekskul          Biaya     Hari      Sisa")
    garis()
    nomor = 1
    for i in daftarEkskul:
        sisa = i[2] - hitungPeserta(i[0])
        baris(f"{str(nomor).ljust(4)}{i[0].ljust(16)}{str(i[1]).ljust(10)}{i[3].ljust(10)}{sisa}")
        nomor += 1
    garis()
    baris(f"Biaya admin Rp {biayaAdmin} | maks {maksEkskul} ekskul")
    baris("Diskon: 2 ekskul = 10%, 3 ekskul = 15%")
    garis()


# -tampilan-
def lihatPeserta():
    if len(daftarEkskul) == 0:
        print("Belum ada ekskul")
        return

    judul("PESERTA PER EKSKUL")
    for i in daftarEkskul:
        baris(f"{i[0]} ({hitungPeserta(i[0])}/{i[2]})")
        ada = False
        for j in siswa:
            if i[0] in siswa[j]["ekskul"]:
                baris(f"  - {siswa[j]['nama'].ljust(20)} kelas {siswa[j]['kelas']}  {siswa[j]['ekskul'][i[0]]}")
                ada = True
        if not ada:
            baris("  belum ada peserta")
        baris("")
    garis()


# - LOGIN -
# -tampilan-
logo = [
    "",
    r"   _____ __  __                              ",
    r"  / ____|  \/  |   /\                        ",
    r" | (___ | \  / |  /  \                       ",
    r"  \___ \| |\/| | / /\ \                      ",
    r"  ____) | |  | |/ ____ \                     ",
    r" |_____/|_|__|_/_/    \_\____   ____   _____ ",
    r"     /\   |  _ \ \   / /  __ \ / __ \ / ____|",
    r"    /  \  | |_) \ \_/ /| |  | | |  | | (___  ",
    r"   / /\ \ |  _ < \   / | |  | | |  | |\___ \ ",
    r"  / ____ \| |_) | | |  | |__| | |__| |____) |",
    r" /_/    \_\____/  |_|  |_____/ \____/|_____/ ",
    "",
]


# -tampilan-
def tampilLogo():
    garis()
    for i in logo:
        baris(i.center(lebar - 2))
    baris("Sistem Pendaftaran Ekstrakurikuler".center(lebar - 2))
    garis()


def login():
    while True:
        bersih()
        tampilLogo()
        baris("1. Admin")
        baris("2. User")
        baris("0. Keluar")
        garis()
        pilih = cekAngka("Login sebagai: ", 0, 2)

        if pilih == 1:
            for i in range(3):
                password = input("Password admin: ")
                if password == passwordAdmin:
                    return "admin"
                print(f"Password salah, sisa kesempatan {2 - i}")
            print("Terlalu banyak salah, kembali ke menu login")
            input("Tekan Enter untuk lanjut...")
        elif pilih == 2:
            return "user"
        else:
            return "keluar"


# - ADMIN -
def tambahEkskul():
    nama = inputTeks("Nama ekskul: ", 15)
    for i in daftarEkskul:
        if i[0].lower() == nama.lower():
            print("Ekskul itu sudah ada")
            return

    biaya = cekAngka("Biaya per bulan (1000 - 1000000): ", 1000, 1000000)
    kuota = cekAngka("Kuota (1 - 30): ", 1, 30)

    nomor = 1
    for i in hariList:
        print(f"{nomor} {i}")
        nomor += 1
    pilihHari = cekAngka("Pilih hari: ", 1, len(hariList))

    daftarEkskul.append((nama, biaya, kuota, hariList[pilihHari - 1]))
    print(f"Ekskul {nama} berhasil ditambahkan")


def ubahEkskul():
    if len(daftarEkskul) == 0:
        print("Belum ada ekskul")
        return

    tampilEkskul()
    nomor = cekAngka("Nomor ekskul yang diubah (0 = batal): ", 0, len(daftarEkskul))
    if nomor == 0:
        return

    while True:
        data = daftarEkskul[nomor - 1]
        pesertaSekarang = hitungPeserta(data[0])

        # -tampilan-
        print()
        judul(f"UBAH EKSKUL: {data[0]}")
        baris(f"1. Nama  : {data[0]}")
        baris(f"2. Biaya : Rp {data[1]}")
        baris(f"3. Kuota : {data[2]} (peserta sekarang {pesertaSekarang})")
        baris(f"4. Hari  : {data[3]}")
        baris("0. Selesai")
        garis()
        pilih = cekAngka("Pilih yang mau diubah: ", 0, 4)

        if pilih == 0:
            break

        elif pilih == 1:
            namaBaru = inputTeks("Nama baru: ", 15)
            kembar = False
            for i in daftarEkskul:
                if i[0].lower() == namaBaru.lower() and i[0] != data[0]:
                    kembar = True

            if namaBaru == data[0]:
                print("Nama sama, tidak ada perubahan")
            elif kembar:
                print("Nama itu sudah dipakai ekskul lain")
            else:
                namaLama = data[0]
                for nis in siswa:
                    if namaLama in siswa[nis]["ekskul"]:
                        siswa[nis]["ekskul"][namaBaru] = siswa[nis]["ekskul"][namaLama]
                        del siswa[nis]["ekskul"][namaLama]
                for i in riwayat:
                    for j in range(len(i["ekskul"])):
                        if i["ekskul"][j] == namaLama:
                            i["ekskul"][j] = namaBaru
                for i in pengajuan:
                    if i["ekskul"] == namaLama:
                        i["ekskul"] = namaBaru
                daftarEkskul[nomor - 1] = (namaBaru, data[1], data[2], data[3])
                print("Nama berhasil diubah")

        elif pilih == 2:
            biayaBaru = cekAngka("Biaya baru (1000 - 1000000): ", 1000, 1000000)
            daftarEkskul[nomor - 1] = (data[0], biayaBaru, data[2], data[3])
            print("Biaya berhasil diubah")

        elif pilih == 3:
            batasBawah = pesertaSekarang
            if batasBawah < 1:
                batasBawah = 1
            kuotaBaru = cekAngka(f"Kuota baru ({batasBawah} - 30): ", batasBawah, 30)
            daftarEkskul[nomor - 1] = (data[0], data[1], kuotaBaru, data[3])
            print("Kuota berhasil diubah")

        else:
            nomorHari = 1
            for i in hariList:
                print(f"{nomorHari} {i}")
                nomorHari += 1
            pilihHari = cekAngka("Pilih hari: ", 1, len(hariList))
            daftarEkskul[nomor - 1] = (data[0], data[1], data[2], hariList[pilihHari - 1])
            print("Hari berhasil diubah")


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
        print(f"{nama} masih punya {hitungPeserta(nama)} peserta, batalkan dulu pesertanya")
        return

    if konfirmasi(f"Yakin hapus {nama}?"):
        daftarEkskul.pop(nomor - 1)
        print(f"Ekskul {nama} dihapus")


# -tampilan-
def lihatSiswa():
    if len(siswa) == 0:
        print("Belum ada siswa terdaftar")
        return

    judul("DAFTAR SISWA")
    baris("NIS    Nama                  Kelas  Ekskul")
    garis()
    for i in siswa:
        baris(f"{i.ljust(7)}{siswa[i]['nama'].ljust(22)}{str(siswa[i]['kelas']).ljust(7)}{len(siswa[i]['ekskul'])}")
    garis()


def tambahSiswa():
    nama = inputTeks("Nama lengkap: ", 20)
    kelas = cekAngka("Kelas (10/11/12): ", 10, 12)
    nis = buatNis()
    siswa[nis] = {"nama": nama, "kelas": kelas, "ekskul": {}}
    print(f"Siswa {nama} ditambahkan dengan NIS {nis} dan 0 ekskul")


def hapusSiswa():
    nis = inputNis()
    if nis not in siswa:
        print("NIS tidak ditemukan")
        return

    nama = siswa[nis]["nama"]
    if konfirmasi(f"Yakin hapus {nama}?"):
        del siswa[nis]
        print(f"Siswa {nama} dihapus")


def batalkanEkskul():
    nis = inputNis()
    if nis not in siswa:
        print("NIS tidak ditemukan")
        return
    if len(siswa[nis]["ekskul"]) == 0:
        print(f"{siswa[nis]['nama']} belum ikut ekskul apa pun")
        return

    print(f"Ekskul yang diikuti {siswa[nis]['nama']} :")
    daftarNama = daftarEkskulSiswa(nis)
    nomor = 1
    for i in daftarNama:
        print(f"{nomor} {i} | masuk {siswa[nis]['ekskul'][i]}")
        nomor += 1

    pilih = cekAngka("Nomor yang dibatalkan (0 = batal): ", 0, len(daftarNama))
    if pilih == 0:
        return
    nama = daftarNama[pilih - 1]
    del siswa[nis]["ekskul"][nama]
    print(f"Pendaftaran {nama} dibatalkan (biaya tidak dikembalikan)")


def namaDariHimpunan(himpunan):
    hasil = []
    for i in himpunan:
        hasil.append(siswa[i]["nama"])
    if len(hasil) == 0:
        return "tidak ada"
    hasil.sort()
    return gabung(hasil)


def analisisHimpunan():
    if len(daftarEkskul) < 2:
        print("Minimal harus ada 2 ekskul")
        return

    # -tampilan-
    judul("ANALISIS HIMPUNAN PESERTA")
    nomor = 1
    for i in daftarEkskul:
        baris(f"{nomor}. {i[0]}")
        nomor += 1
    garis()

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

    print()
    print(f"Peserta {namaA} : {namaDariHimpunan(himpunanA)}")
    print(f"Peserta {namaB} : {namaDariHimpunan(himpunanB)}")
    print(f"Ikut keduanya (irisan)     : {namaDariHimpunan(himpunanA & himpunanB)}")
    print(f"Ikut salah satu (gabungan) : {namaDariHimpunan(himpunanA | himpunanB)}")
    print(f"Hanya {namaA} : {namaDariHimpunan(himpunanA - himpunanB)}")
    print(f"Hanya {namaB} : {namaDariHimpunan(himpunanB - himpunanA)}")


def statistik():
    totalPeserta = 0
    totalKuota = 0

    # -tampilan-
    judul("GRAFIK JUMLAH PESERTA")
    for i in daftarEkskul:
        jumlah = hitungPeserta(i[0])
        totalPeserta += jumlah
        totalKuota += i[2]
        batang = ""
        for j in range(jumlah):
            batang += "#"
        baris(f"{i[0].ljust(16)}| {batang} {jumlah}")
    garis()

    # -tampilan-
    print()
    judul("STATISTIK")
    baris(f"Jumlah ekskul     : {len(daftarEkskul)}")
    baris(f"Jumlah siswa      : {len(siswa)}")
    baris(f"Total pendaftaran : {totalPeserta}")
    baris(f"Total kuota       : {totalKuota}")
    try:
        baris(f"Kuota terisi      : {round(totalPeserta / totalKuota * 100, 1)} %")
        baris(f"Rata-rata ekskul per siswa : {round(totalPeserta / len(siswa), 2)}")
    except ZeroDivisionError:
        baris("Data belum cukup untuk persentase dan rata-rata")
    garis()


def lihatRiwayat():
    if len(riwayat) == 0:
        print("Belum ada transaksi")
        return

    totalCash = 0
    totalQris = 0

    # -tampilan-
    judul("RIWAYAT PEMBAYARAN")
    for i in riwayat:
        baris(f"{i['tanggal']} | {i['metode']} | Rp {i['total']}")
        baris(f"  {i['nama']} ({i['nis']})")
        baris(f"  {gabung(i['ekskul'])}")
        baris("")
        if i["metode"] == "Cash":
            totalCash += i["total"]
        else:
            totalQris += i["total"]
    garis()
    baris(f"Jumlah transaksi : {len(riwayat)}")
    baris(f"Pemasukan Cash   : Rp {totalCash}")
    baris(f"Pemasukan QRIS   : Rp {totalQris}")
    baris(f"Total pemasukan  : Rp {totalCash + totalQris}")
    garis()


def notifikasiPembatalan():
    while True:
        daftarMenunggu = []
        for i in pengajuan:
            if i["status"] == "menunggu":
                daftarMenunggu.append(i)

        if len(daftarMenunggu) == 0:
            print("Tidak ada pengajuan pembatalan yang menunggu")
            return

        # -tampilan-
        judul("PENGAJUAN PEMBATALAN EKSKUL")
        nomor = 1
        for i in daftarMenunggu:
            baris(f"{nomor}. {i['nama']} ({i['nis']})")
            baris(f"   ingin batal : {i['ekskul']}")
            baris(f"   diajukan    : {i['tanggal']}")
            baris("")
            nomor += 1
        garis()

        pilih = cekAngka("Pilih nomor pengajuan (0 = kembali): ", 0, len(daftarMenunggu))
        if pilih == 0:
            return

        data = daftarMenunggu[pilih - 1]
        print("1. Setujui")
        print("2. Tolak")
        print("0. Kembali")
        aksi = cekAngka("Pilihan: ", 0, 2)

        if aksi == 1:
            if data["nis"] in siswa and data["ekskul"] in siswa[data["nis"]]["ekskul"]:
                del siswa[data["nis"]]["ekskul"][data["ekskul"]]
                data["status"] = "disetujui"
                print(f"Pembatalan {data['ekskul']} untuk {data['nama']} disetujui")
            else:
                data["status"] = "ditutup"
                print("Data siswa atau ekskul sudah tidak ada, pengajuan ditutup")
        elif aksi == 2:
            data["status"] = "ditolak"
            print("Pengajuan ditolak")


def menuAdmin():
    while True:
        menunggu = jumlahMenunggu()
        batas = 12
        if menunggu > 0:
            batas = 13

        # -tampilan-
        bersih()
        daftarMenu = [
            "1. Lihat daftar ekskul",
            "2. Tambah ekskul",
            "3. Ubah ekskul",
            "4. Hapus ekskul",
            "5. Lihat semua siswa",
            "6. Tambah siswa",
            "7. Hapus siswa",
            "8. Batalkan ekskul siswa",
            "9. Lihat peserta per ekskul",
            "10. Analisis himpunan peserta",
            "11. Grafik dan statistik",
            "12. Riwayat pembayaran",
        ]
        if menunggu > 0:
            daftarMenu.append("13. Notifikasi pembatalan (" + str(menunggu) + ")")
            daftarMenu.append("0. Logout")

        separuh = (len(daftarMenu) + 1) // 2
        judul("MENU ADMIN")
        for i in range(separuh):
            kiri = daftarMenu[i]
            kanan = ""
            if i + separuh < len(daftarMenu):
                kanan = daftarMenu[i + separuh]
            baris(kiri.ljust(28) + kanan)
        if menunggu == 0:
            baris("0. Logout")
        garis()
        pilihan = cekAngka("Pilih menu: ", 0, batas)
        bersih()

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
        elif pilihan == 13:
            notifikasiPembatalan()
        else:
            break

        print()
        input("Tekan Enter untuk kembali ke menu...")


# - USER -
def bayar(total):
    # -tampilan-
    print()
    judul("PEMBAYARAN")
    baris(f"Total yang harus dibayar: Rp {total}")
    baris("1. Cash")
    baris("2. QRIS (nominal harus pas)")
    baris("0. Batal")
    garis()
    metode = cekAngka("Metode pembayaran: ", 0, 2)

    if metode == 0:
        return ""

    if metode == 1:
        while True:
            uang = cekAngka("Uang diterima (0 = batal): Rp ", 0, 100000000)
            if uang == 0:
                return ""
            if uang < total:
                print(f"Uang kurang Rp {total - uang}")
            else:
                print(f"Kembalian: Rp {uang - total}")
                return "Cash"
    else:
        print(f"Scan QRIS, nominal harus pas Rp {total}")
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

    # -tampilan-
    judul("PENDAFTARAN EKSKUL")
    baris("1. Siswa baru")
    baris("2. Sudah punya NIS")
    baris("0. Batal")
    garis()
    jenis = cekAngka("Pilih: ", 0, 2)
    if jenis == 0:
        return

    if jenis == 2:
        nis = inputNis()
        if nis not in siswa:
            print("NIS belum terdaftar, pilih siswa baru kalau belum punya NIS")
            return
        nama = siswa[nis]["nama"]
        kelas = siswa[nis]["kelas"]
        ekskulLama = siswa[nis]["ekskul"]
        print(f"Halo, {nama}")
    else:
        nama = inputTeks("Nama lengkap: ", 20)
        kelas = cekAngka("Kelas (10/11/12): ", 10, 12)
        nis = buatNis()
        siswa[nis] = {"nama": nama, "kelas": kelas, "ekskul": {}}
        ekskulLama = siswa[nis]["ekskul"]
        print(f"Siswa baru berhasil terdaftar, NIS kamu: {nis}")

    if len(ekskulLama) >= maksEkskul:
        print(f"Kamu sudah ikut {maksEkskul} ekskul, tidak bisa nambah lagi")
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
            print(f"Kuota {namaEkskul} sudah penuh")
            continue

        pilihanBaru.append(namaEkskul)
        print(f"{namaEkskul} ditambahkan")

    if len(pilihanBaru) == 0:
        print(f"Tidak ada ekskul yang dipilih, NIS kamu {nis} tetap tersimpan")
        return

    totalBiaya = 0
    for i in pilihanBaru:
        totalBiaya += ambilBiaya(i)
    persen, potongan, total = hitungBayar(totalBiaya, len(pilihanBaru))

    # -tampilan-
    print()
    judul("RINCIAN BIAYA")
    for i in pilihanBaru:
        baris(f"- {i.ljust(18)}Rp {ambilBiaya(i)}")
    baris(f"Subtotal            Rp {totalBiaya}")
    teksDiskon = f"Diskon {persen}%"
    baris(f"{teksDiskon.ljust(20)}Rp -{potongan}")
    baris(f"Biaya admin         Rp {biayaAdmin}")
    baris(f"Total               Rp {total}")
    garis()

    metode = bayar(total)
    if metode == "":
        print(f"Pembayaran dibatalkan, ekskul tidak disimpan, NIS kamu {nis} tetap tersimpan")
        return

    tanggalMasuk = tanggal()
    for i in pilihanBaru:
        siswa[nis]["ekskul"][i] = tanggalMasuk

    waktuBayar = tanggalJam()
    transaksi = {"nis": nis, "nama": nama, "ekskul": pilihanBaru, "metode": metode, "total": total, "tanggal": waktuBayar}
    riwayat.append(transaksi)

    # -tampilan-
    print()
    judul("BUKTI PENDAFTARAN")
    baris(f"Tanggal : {waktuBayar}")
    baris(f"NIS     : {nis}")
    baris(f"Nama    : {nama}")
    baris(f"Kelas   : {kelas}")
    garis()
    for i in pilihanBaru:
        baris(f"- {i.ljust(18)}Rp {ambilBiaya(i)}")
    baris(f"Subtotal            Rp {totalBiaya}")
    teksDiskon = f"Diskon {persen}%"
    baris(f"{teksDiskon.ljust(20)}Rp -{potongan}")
    baris(f"Biaya admin         Rp {biayaAdmin}")
    baris("Metode".ljust(20) + metode)
    baris(f"Total bayar         Rp {total}")
    garis()
    baris("Simpan NIS kamu untuk pendaftaran berikutnya")
    garis()


def cekSiswa():
    nis = inputNis()
    try:
        data = siswa[nis]

        # -tampilan-
        judul("DATA SISWA")
        baris(f"NIS   : {nis}")
        baris(f"Nama  : {data['nama']}")
        baris(f"Kelas : {data['kelas']}")
        if len(data["ekskul"]) == 0:
            baris("Belum ikut ekskul apa pun")
        else:
            baris("Ekskul yang diikuti:")
            for i in data["ekskul"]:
                baris(f"- {i.ljust(16)}masuk {data['ekskul'][i]}")

        adaPengajuan = False
        for i in pengajuan:
            if i["nis"] == nis:
                if not adaPengajuan:
                    baris("Pengajuan pembatalan:")
                    adaPengajuan = True
                baris(f"- {i['ekskul'].ljust(16)}{i['status']}")
        garis()
    except KeyError:
        print("NIS itu belum terdaftar")


def riwayatSaya():
    nis = inputNis()

    # -tampilan-
    judul(f"RIWAYAT PEMBAYARAN {nis}")
    ada = False
    for i in riwayat:
        if i["nis"] == nis:
            baris(f"{i['tanggal']} | {i['metode']} | Rp {i['total']}")
            baris(f"  {gabung(i['ekskul'])}")
            ada = True
    if not ada:
        baris("Belum ada riwayat pembayaran")
    garis()


def ajukanPembatalan():
    nis = inputNis()
    if nis not in siswa:
        print("NIS belum terdaftar")
        return
    if len(siswa[nis]["ekskul"]) == 0:
        print("Kamu belum ikut ekskul apa pun")
        return

    # -tampilan-
    judul("AJUKAN PEMBATALAN EKSKUL")
    daftarNama = daftarEkskulSiswa(nis)
    nomor = 1
    for i in daftarNama:
        baris(f"{nomor}. {i}")
        nomor += 1
    garis()

    pilih = cekAngka("Nomor yang mau dibatalkan (0 = batal): ", 0, len(daftarNama))
    if pilih == 0:
        return
    namaEkskul = daftarNama[pilih - 1]

    for i in pengajuan:
        if i["nis"] == nis and i["ekskul"] == namaEkskul and i["status"] == "menunggu":
            print("Pengajuan itu sudah ada dan masih menunggu persetujuan admin")
            return

    dataBaru = {"nis": nis, "nama": siswa[nis]["nama"], "ekskul": namaEkskul, "tanggal": tanggalJam(), "status": "menunggu"}
    pengajuan.append(dataBaru)
    print(f"Pengajuan pembatalan {namaEkskul} terkirim, tunggu persetujuan admin")


def menuUser():
    while True:
        # -tampilan-
        bersih()
        judul("MENU USER")
        baris("1. Lihat daftar ekskul          4. Cek ekskul saya")
        baris("2. Daftar ekskul                5. Riwayat pembayaran saya")
        baris("3. Lihat peserta per ekskul     6. Ajukan pembatalan ekskul")
        baris("0. Kembali ke login")
        garis()
        pilihan = cekAngka("Pilih menu: ", 0, 6)
        bersih()

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
        elif pilihan == 6:
            ajukanPembatalan()
        else:
            break

        print()
        input("Tekan Enter untuk kembali ke menu...")


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