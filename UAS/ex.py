#MODUL 6 TUPLE
DAFTAR_EKSKUL = (
    ("Basket", 50000, 5, "Senin"),
    ("Futsal", 45000, 5, "Selasa"),
    ("Paduan Suara", 30000, 4, "Rabu"),
    ("Pramuka", 25000, 6, "Jumat"),
    ("Robotik", 75000, 4, "Kamis"),
    ("PMR", 20000, 5, "Sabtu"),
    ("Tari Tradisional", 35000, 4, "Rabu"),
    ("Jurnalistik", 30000, 5, "Kamis"),
)

MAKS_EKSKUL = 3         
BIAYA_ADMIN = 10000

#MODUL 7 : DICTIONARY
database_ekskul = {}     # {"Basket": {"biaya":..., "kuota":..., "hari":..., "peserta":[nis,...]}}
data_siswa = {}          # {"12345": {"nama":..., "kelas":..., "jurusan":..., "ekskul": set()}}
riwayat_transaksi = []   # list berisi dictionary transaksi


# ===============================================================
# MODUL 5 : FUNCTION - TAMPILAN DASAR
# ===============================================================
def garis(panjang=60, simbol="="):
    """Mencetak garis pembatas."""
    print(simbol * panjang)


def judul(teks):
    """Mencetak judul dengan bingkai."""
    garis()
    print(teks.center(60))
    garis()


def format_rupiah(angka):
    """Mengubah angka menjadi format rupiah, contoh 50000 -> Rp 50.000"""
    return "Rp " + f"{angka:,}".replace(",", ".")


# ===============================================================
# MODUL 7 : TRY-EXCEPT - VALIDASI INPUT
# ===============================================================
def input_angka(pesan, minimal, maksimal):
    """Meminta angka bulat dalam rentang tertentu sampai valid."""
    while True:
        try:
            nilai = int(input(pesan))
            if nilai < minimal or nilai > maksimal:
                print(f"  [!] Angka harus antara {minimal} - {maksimal}.")
                continue
            return nilai
        except ValueError:
            print("  [!] Input harus berupa angka bulat.")


def input_nis():
    """Meminta NIS (hanya angka, 5-10 digit)."""
    while True:
        nis = input("Masukkan NIS (5-10 digit)  : ").strip()
        if not nis.isdigit():
            print("  [!] NIS hanya boleh berisi angka.")
        elif len(nis) < 5 or len(nis) > 10:
            print("  [!] Panjang NIS harus 5 sampai 10 digit.")
        else:
            return nis


def input_teks(pesan):
    """Meminta teks yang tidak boleh kosong."""
    while True:
        teks = input(pesan).strip()
        if teks != "":
            return teks
        print("  [!] Input tidak boleh kosong.")


# ===============================================================
# MODUL 1 : OPERATOR ARITMATIKA - PERHITUNGAN BIAYA
# ===============================================================
def hitung_diskon(jumlah_ekskul):
    """Diskon persen berdasarkan jumlah ekskul yang diikuti."""
    if jumlah_ekskul == 1:
        return 0
    elif jumlah_ekskul == 2:
        return 10
    else:
        return 15


def hitung_total(daftar_biaya):
    """
    Menghitung subtotal, potongan, dan total bayar.
    Mengembalikan tuple (subtotal, diskon_persen, potongan, total).
    """
    subtotal = sum(daftar_biaya)                          # penjumlahan
    diskon_persen = hitung_diskon(len(daftar_biaya))
    potongan = subtotal * diskon_persen // 100            # perkalian & pembagian bulat
    total = subtotal - potongan + BIAYA_ADMIN             # pengurangan & penjumlahan
    return subtotal, diskon_persen, potongan, total


def hitung_biaya_semester(biaya_bulanan, jumlah_bulan=6):
    """Contoh operator pangkat dan perkalian: proyeksi biaya semester."""
    return biaya_bulanan * jumlah_bulan


def pembagian_kelompok(jumlah_peserta, ukuran=3):
    """Membagi peserta menjadi kelompok memakai // dan %."""
    jumlah_kelompok = jumlah_peserta // ukuran
    sisa = jumlah_peserta % ukuran
    return jumlah_kelompok, sisa


# ===============================================================
# MODUL 5 & 7 : FUNCTION PENGELOLA DATA
# ===============================================================
def inisialisasi_ekskul():
    """Mengisi dictionary database_ekskul dari tuple DAFTAR_EKSKUL."""
    for nama, biaya, kuota, hari in DAFTAR_EKSKUL:     # tuple unpacking
        database_ekskul[nama] = {
            "biaya": biaya,
            "kuota": kuota,
            "hari": hari,
            "peserta": [],                              # list NIS peserta
        }


def sisa_kuota(nama_ekskul):
    """Mengembalikan sisa kuota sebuah ekskul."""
    data = database_ekskul[nama_ekskul]
    return data["kuota"] - len(data["peserta"])


def daftarkan_ke_ekskul(nis, nama_ekskul):
    """Menyimpan relasi siswa-ekskul pada dua struktur data sekaligus."""
    data_siswa[nis]["ekskul"].add(nama_ekskul)          # set
    database_ekskul[nama_ekskul]["peserta"].append(nis) # list


def tambah_siswa(nis, nama, kelas, jurusan):
    """Menambah siswa baru ke dictionary data_siswa."""
    data_siswa[nis] = {
        "nama": nama,
        "kelas": kelas,
        "jurusan": jurusan,
        "ekskul": set(),
    }


def daftar_nama_ekskul():
    """Mengembalikan list nama ekskul sesuai urutan tuple."""
    return [item[0] for item in DAFTAR_EKSKUL]         # list comprehension


def isi_data_contoh():
    """Data awal agar program langsung bisa didemokan."""
    contoh = [
        ("10001", "Andi Pratama", 10, "IPA", ["Basket", "Robotik"]),
        ("10002", "Siti Aminah", 11, "IPS", ["Paduan Suara", "Tari Tradisional", "PMR"]),
        ("10003", "Budi Santoso", 12, "IPA", ["Basket", "Futsal"]),
        ("10004", "Dewi Lestari", 10, "BAHASA", ["Jurnalistik", "Paduan Suara"]),
    ]
    for nis, nama, kelas, jurusan, pilihan in contoh:
        tambah_siswa(nis, nama, kelas, jurusan)
        biaya_list = []
        for ekskul in pilihan:
            daftarkan_ke_ekskul(nis, ekskul)
            biaya_list.append(database_ekskul[ekskul]["biaya"])
        subtotal, diskon, potongan, total = hitung_total(biaya_list)
        riwayat_transaksi.append({
            "nis": nis, "ekskul": list(pilihan),
            "subtotal": subtotal, "diskon": diskon, "total": total,
        })


# ===============================================================
# MENU 1 : LIHAT DAFTAR EKSKUL  (MODUL 3 : PERULANGAN FOR)
# ===============================================================
def tampil_ekskul():
    judul("DAFTAR EKSTRAKURIKULER")
    print(f"{'No':<4}{'Nama Ekskul':<20}{'Biaya':<13}{'Hari':<10}{'Sisa Kuota'}")
    garis(60, "-")
    nomor = 1
    for nama in daftar_nama_ekskul():
        data = database_ekskul[nama]
        sisa = sisa_kuota(nama)
        status = "PENUH" if sisa == 0 else str(sisa)
        print(f"{nomor:<4}{nama:<20}{format_rupiah(data['biaya']):<13}"
              f"{data['hari']:<10}{status}")
        nomor += 1
    garis(60, "-")
    print(f"Biaya admin per transaksi : {format_rupiah(BIAYA_ADMIN)}")
    print(f"Maksimal ekskul per siswa : {MAKS_EKSKUL}")
    print("Diskon: 2 ekskul = 10%, 3 ekskul = 15%")


# ===============================================================
# MENU 2 : PENDAFTARAN  (MODUL 2 : KONDISI, MODUL 4 : BREAK/CONTINUE)
# ===============================================================
def pilih_jurusan():
    """Memilih jurusan memakai if/elif/else."""
    print("Pilih jurusan: 1. IPA   2. IPS   3. BAHASA")
    pilihan = input_angka("Jurusan (1-3)               : ", 1, 3)
    if pilihan == 1:
        return "IPA"
    elif pilihan == 2:
        return "IPS"
    else:
        return "BAHASA"


def pilih_ekskul(sudah_ikut):
    """
    Meminta siswa memilih ekskul (maks MAKS_EKSKUL).
    sudah_ikut : set ekskul yang sudah diikuti siswa.
    Mengembalikan list ekskul baru yang dipilih.
    """
    nama_list = daftar_nama_ekskul()
    terpilih = []

    while len(sudah_ikut) + len(terpilih) < MAKS_EKSKUL:
        sisa_slot = MAKS_EKSKUL - len(sudah_ikut) - len(terpilih)
        print(f"\nSisa slot pilihan: {sisa_slot}  (ketik 0 untuk selesai)")
        nomor = input_angka("Nomor ekskul (1-8)          : ", 0, len(nama_list))

        if nomor == 0:
            break                                       # berhenti memilih

        nama = nama_list[nomor - 1]
        if nama in sudah_ikut or nama in terpilih:
            print(f"  [!] Anda sudah memilih {nama}.")
            continue                                    # ulangi pilihan
        if sisa_kuota(nama) <= 0:
            print(f"  [!] Kuota {nama} sudah penuh.")
            continue

        terpilih.append(nama)
        print(f"  [+] {nama} ditambahkan.")

    return terpilih


def cetak_bukti(nis, daftar_ekskul_baru, rincian):
    """Mencetak bukti pendaftaran (MODUL 6: unpack tuple hasil hitung_total)."""
    subtotal, diskon, potongan, total = rincian
    siswa = data_siswa[nis]
    print()
    garis(60, "*")
    print("BUKTI PENDAFTARAN EKSKUL".center(60))
    garis(60, "*")
    print(f"NIS       : {nis}")
    print(f"Nama      : {siswa['nama']}")
    print(f"Kelas     : {siswa['kelas']} {siswa['jurusan']}")
    print("Ekskul baru yang didaftar:")
    for urutan, nama in enumerate(daftar_ekskul_baru, start=1):
        biaya = database_ekskul[nama]["biaya"]
        print(f"  {urutan}. {nama:<18}{format_rupiah(biaya):>12}")
    garis(60, "-")
    print(f"{'Subtotal':<30}{format_rupiah(subtotal):>20}")
    print(f"{'Diskon ' + str(diskon) + '%':<30}{'- ' + format_rupiah(potongan):>20}")
    print(f"{'Biaya administrasi':<30}{format_rupiah(BIAYA_ADMIN):>20}")
    garis(60, "-")
    print(f"{'TOTAL BAYAR':<30}{format_rupiah(total):>20}")
    garis(60, "*")


def proses_pendaftaran():
    judul("FORM PENDAFTARAN EKSKUL")
    nis = input_nis()

    # --- Penyeleksian kondisi: siswa lama atau baru ---
    if nis in data_siswa:
        siswa = data_siswa[nis]
        print(f"Siswa terdaftar: {siswa['nama']} (kelas {siswa['kelas']} {siswa['jurusan']})")
        if len(siswa["ekskul"]) >= MAKS_EKSKUL:
            print(f"[!] Anda sudah mengikuti {MAKS_EKSKUL} ekskul (batas maksimum).")
            return
    else:
        nama = input_teks("Nama lengkap                : ").title()
        kelas = input_angka("Kelas (10/11/12)           : ", 10, 12)
        jurusan = pilih_jurusan()
        tambah_siswa(nis, nama, kelas, jurusan)
        print("[+] Data siswa baru berhasil dibuat.")

    tampil_ekskul()
    pilihan_baru = pilih_ekskul(data_siswa[nis]["ekskul"])

    if len(pilihan_baru) == 0:
        print("\nTidak ada ekskul yang dipilih. Pendaftaran dibatalkan.")
        if len(data_siswa[nis]["ekskul"]) == 0:
            del data_siswa[nis]                         # hapus siswa kosong
        return

    # --- Hitung biaya (modul 1) ---
    biaya_list = [database_ekskul[n]["biaya"] for n in pilihan_baru]
    rincian = hitung_total(biaya_list)

    for nama_ekskul in pilihan_baru:
        daftarkan_ke_ekskul(nis, nama_ekskul)

    riwayat_transaksi.append({
        "nis": nis, "ekskul": pilihan_baru,
        "subtotal": rincian[0], "diskon": rincian[1], "total": rincian[3],
    })
    cetak_bukti(nis, pilihan_baru, rincian)


# ===============================================================
# MENU 3 : LIHAT PESERTA PER EKSKUL
# ===============================================================
def lihat_peserta():
    judul("DAFTAR PESERTA PER EKSKUL")
    for nama in daftar_nama_ekskul():
        peserta = database_ekskul[nama]["peserta"]
        print(f"\n> {nama} ({len(peserta)}/{database_ekskul[nama]['kuota']})")
        if len(peserta) == 0:
            print("    (belum ada peserta)")
        for nis in sorted(peserta):                     # list diurutkan
            siswa = data_siswa[nis]
            print(f"    - {nis}  {siswa['nama']:<18} {siswa['kelas']} {siswa['jurusan']}")


# ===============================================================
# MENU 4 : CARI SISWA  (MODUL 7 : KEYERROR / TRY-EXCEPT)
# ===============================================================
def cari_siswa():
    judul("CARI DATA SISWA")
    nis = input_nis()
    try:
        siswa = data_siswa[nis]                         # bisa memicu KeyError
        print(f"\nNama   : {siswa['nama']}")
        print(f"Kelas  : {siswa['kelas']} {siswa['jurusan']}")
        print("Ekskul :", ", ".join(sorted(siswa["ekskul"])))
    except KeyError:
        print("\n[!] Siswa dengan NIS tersebut tidak ditemukan.")
    finally:
        print("(pencarian selesai)")


# ===============================================================
# MENU 5 : BATALKAN PENDAFTARAN
# ===============================================================
def batalkan_pendaftaran():
    judul("BATALKAN PENDAFTARAN EKSKUL")
    nis = input_nis()
    if nis not in data_siswa:
        print("[!] NIS tidak ditemukan.")
        return

    ekskul_siswa = sorted(data_siswa[nis]["ekskul"])    # set -> list
    if not ekskul_siswa:
        print("[!] Siswa belum mengikuti ekskul apa pun.")
        return

    print(f"Ekskul milik {data_siswa[nis]['nama']}:")
    for i, nama in enumerate(ekskul_siswa, start=1):
        print(f"  {i}. {nama}")

    pilihan = input_angka("Nomor yang dibatalkan (0=batal): ", 0, len(ekskul_siswa))
    if pilihan == 0:
        print("Tidak ada yang dibatalkan.")
        return

    nama_ekskul = ekskul_siswa[pilihan - 1]
    data_siswa[nis]["ekskul"].discard(nama_ekskul)
    database_ekskul[nama_ekskul]["peserta"].remove(nis)
    print(f"[+] Pendaftaran {nama_ekskul} berhasil dibatalkan.")


# ===============================================================
# MENU 6 : STATISTIK & GRAFIK  (MODUL 1, 3, 4)
# ===============================================================
def grafik_batang():
    """Grafik batang teks memakai nested loop (MODUL 4)."""
    print("\nGrafik jumlah peserta:")
    for nama in daftar_nama_ekskul():
        jumlah = len(database_ekskul[nama]["peserta"])
        print(f"{nama:<18}|", end=" ")
        for _ in range(jumlah):
            print("#", end="")
        print(f" {jumlah}")


def statistik():
    judul("STATISTIK PENDAFTARAN")
    total_peserta = 0
    total_kuota = 0
    for nama in database_ekskul:
        total_peserta += len(database_ekskul[nama]["peserta"])
        total_kuota += database_ekskul[nama]["kuota"]

    print(f"Jumlah siswa terdaftar : {len(data_siswa)}")
    print(f"Total pendaftaran      : {total_peserta}")
    print(f"Total kuota tersedia   : {total_kuota}")
    print(f"Sisa kuota keseluruhan : {total_kuota - total_peserta}")

    # Penanganan pembagian dengan nol (MODUL 7)
    try:
        persen = total_peserta / total_kuota * 100
        rata = total_peserta / len(data_siswa)
        print(f"Persentase terisi      : {persen:.1f}%")
        print(f"Rata-rata ekskul/siswa : {rata:.2f}")
    except ZeroDivisionError:
        print("Belum ada data untuk dihitung rata-ratanya.")

    pendapatan = sum(t["total"] for t in riwayat_transaksi)
    print(f"Total pendapatan       : {format_rupiah(pendapatan)}")
    print(f"Jumlah transaksi       : {len(riwayat_transaksi)}")

    # Ekskul terpopuler memakai perulangan dan kondisi
    terpopuler, maksimum = "-", -1
    for nama, data in database_ekskul.items():
        if len(data["peserta"]) > maksimum:
            maksimum = len(data["peserta"])
            terpopuler = nama
    print(f"Ekskul terpopuler      : {terpopuler} ({maksimum} peserta)")

    # Statistik per kelas memakai dictionary penghitung
    per_kelas = {10: 0, 11: 0, 12: 0}
    for siswa in data_siswa.values():
        per_kelas[siswa["kelas"]] += 1
    print("\nSiswa per kelas:")
    for kelas, jumlah in per_kelas.items():
        print(f"  Kelas {kelas} : {jumlah} siswa")

    grafik_batang()

    # Pembagian kelompok memakai // dan %
    print("\nPembagian kelompok latihan (3 orang/kelompok):")
    for nama in daftar_nama_ekskul():
        jumlah = len(database_ekskul[nama]["peserta"])
        kelompok, sisa = pembagian_kelompok(jumlah, 3)
        print(f"  {nama:<18}: {kelompok} kelompok, sisa {sisa} orang")


# ===============================================================
# MENU 7 : ANALISIS HIMPUNAN (MODUL 7 : SET)
# ===============================================================
def analisis_himpunan():
    judul("ANALISIS HIMPUNAN PESERTA")
    nama_list = daftar_nama_ekskul()
    for i, nama in enumerate(nama_list, start=1):
        print(f"  {i}. {nama}")

    a = input_angka("Pilih ekskul pertama (1-8) : ", 1, len(nama_list))
    b = input_angka("Pilih ekskul kedua   (1-8) : ", 1, len(nama_list))
    if a == b:
        print("[!] Pilih dua ekskul yang berbeda.")
        return

    nama_a, nama_b = nama_list[a - 1], nama_list[b - 1]
    himpunan_a = set(database_ekskul[nama_a]["peserta"])
    himpunan_b = set(database_ekskul[nama_b]["peserta"])

    def tampil(label, himpunan):
        nama_siswa = sorted(data_siswa[n]["nama"] for n in himpunan)
        isi = ", ".join(nama_siswa) if nama_siswa else "(kosong)"
        print(f"{label:<34}: {isi}")

    print()
    tampil(f"Peserta {nama_a}", himpunan_a)
    tampil(f"Peserta {nama_b}", himpunan_b)
    tampil("Irisan (ikut keduanya)", himpunan_a & himpunan_b)
    tampil("Gabungan (ikut salah satu/keduanya)", himpunan_a | himpunan_b)
    tampil(f"Hanya {nama_a}", himpunan_a - himpunan_b)
    tampil(f"Hanya {nama_b}", himpunan_b - himpunan_a)
    tampil("Selisih simetris", himpunan_a ^ himpunan_b)

    # Siswa yang belum ikut ekskul sama sekali
    semua_siswa = set(data_siswa.keys())
    ikut_ekskul = set()
    for data in database_ekskul.values():
        ikut_ekskul.update(data["peserta"])
    tampil("Siswa belum ikut ekskul", semua_siswa - ikut_ekskul)

    print("\nA subset B ?", himpunan_a.issubset(himpunan_b))
    print("A dan B saling lepas ?", himpunan_a.isdisjoint(himpunan_b))


# ===============================================================
# MENU 8 : KALKULATOR BIAYA (MODUL 1 : OPERATOR ARITMATIKA)
# ===============================================================
def kalkulator_biaya():
    judul("KALKULATOR BIAYA EKSKUL")
    tampil_ekskul()
    nama_list = daftar_nama_ekskul()
    jumlah = input_angka("\nBerapa ekskul yang ingin dihitung (1-3)? ", 1, MAKS_EKSKUL)

    biaya_list = []
    for ke in range(1, jumlah + 1):
        nomor = input_angka(f"Nomor ekskul ke-{ke}: ", 1, len(nama_list))
        biaya_list.append(database_ekskul[nama_list[nomor - 1]]["biaya"])

    subtotal, diskon, potongan, total = hitung_total(biaya_list)
    print(f"\nSubtotal          : {format_rupiah(subtotal)}")
    print(f"Diskon {diskon}%         : {format_rupiah(potongan)}")
    print(f"Biaya admin       : {format_rupiah(BIAYA_ADMIN)}")
    print(f"Total bayar       : {format_rupiah(total)}")
    print(f"Estimasi 6 bulan  : {format_rupiah(hitung_biaya_semester(total))}")
    print(f"Rata-rata/ekskul  : {format_rupiah(total // jumlah)}")
    print(f"Sisa uang dari Rp 200.000 : {format_rupiah(200000 - total)}")
    print(f"Biaya admin dikuadratkan (demo pangkat): {BIAYA_ADMIN ** 2}")


# ===============================================================
# MENU 9 : POLA PERULANGAN (MODUL 4)
# ===============================================================
def pola_segitiga(tinggi):
    for baris in range(1, tinggi + 1):
        print("*" * baris)


def pola_piramida(tinggi):
    for baris in range(1, tinggi + 1):
        spasi = " " * (tinggi - baris)
        bintang = "*" * (2 * baris - 1)
        print(spasi + bintang)


def pola_angka(tinggi):
    for baris in range(1, tinggi + 1):
        for kolom in range(1, baris + 1):
            print(kolom, end=" ")
        print()


def pola_persegi(sisi):
    for baris in range(sisi):
        for kolom in range(sisi):
            if baris == 0 or baris == sisi - 1 or kolom == 0 or kolom == sisi - 1:
                print("#", end=" ")
            else:
                print(" ", end=" ")
        print()


def cari_dengan_for_else(kata):
    """Contoh for-else: mencari ekskul berdasarkan nama."""
    for nama in daftar_nama_ekskul():
        if kata.lower() in nama.lower():
            print(f"Ditemukan : {nama}")
            break
    else:
        print("Ekskul tidak ditemukan.")


def demo_pola():
    judul("DEMO POLA PERULANGAN")
    tinggi = input_angka("Tinggi pola (3-9): ", 3, 9)
    print("\nSegitiga:");  pola_segitiga(tinggi)
    print("\nPiramida:");  pola_piramida(tinggi)
    print("\nPola Angka:"); pola_angka(tinggi)
    print("\nPersegi Berongga:"); pola_persegi(tinggi)
    print("\nPencarian ekskul (for-else):")
    cari_dengan_for_else(input_teks("Kata kunci: "))


# ===============================================================
# MENU UTAMA  (MODUL 3 : WHILE)
# ===============================================================
def tampil_menu():
    judul("SISTEM PENDAFTARAN EKSKUL SMA")
    print(" 1. Lihat daftar ekskul")
    print(" 2. Daftar ekskul")
    print(" 3. Lihat peserta per ekskul")
    print(" 4. Cari data siswa")
    print(" 5. Batalkan pendaftaran")
    print(" 6. Statistik dan grafik")
    print(" 7. Analisis himpunan peserta")
    print(" 8. Kalkulator biaya")
    print(" 9. Demo pola perulangan")
    print(" 0. Keluar")
    garis()


def main():
    inisialisasi_ekskul()
    isi_data_contoh()
    aktif = True
    while aktif:
        try:
            tampil_menu()
            pilihan = input_angka("Pilih menu (1-9): ", 0, 9)
            print()
            if pilihan == 1:
                tampil_ekskul()
            elif pilihan == 2:
                proses_pendaftaran()
            elif pilihan == 3:
                lihat_peserta()
            elif pilihan == 4:
                cari_siswa()
            elif pilihan == 5:
                batalkan_pendaftaran()
            elif pilihan == 6:
                statistik()
            elif pilihan == 7:
                analisis_himpunan()
            elif pilihan == 8:
                kalkulator_biaya()
            elif pilihan == 9:
                demo_pola()
            else:
                print("Terima kasih telah menggunakan program ini. Sampai jumpa!")
                aktif = False
            if aktif:
                input("\nTekan ENTER untuk kembali ke menu...")
        except (KeyboardInterrupt, EOFError):
            print("\nProgram dihentikan oleh pengguna.")
            aktif = False


if __name__ == "__main__":
    main()
