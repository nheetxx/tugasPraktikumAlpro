daftar = []
while True:
    nama = input("Masukkan nama calon anggota (ketik 'selesai' untuk berhenti): ")
    if nama == "selesai":
        break
    daftar.append(nama)

# evaluasi tiap nama: "admin" atau panjang kurang dari 4 ditandai tidak valid
for nama in daftar:
    if nama == "admin" or len(nama) < 4:
        print(f"Nama '{nama}' tidak valid")

suspect = input("Masukkan nama penyusup yang ingin dihapus: ")
# cek dulu sebelum remove, supaya tidak error kalau nama tidak ada di daftar
if suspect in daftar:
    daftar.remove(suspect)
    print(f"{suspect} telah dihapus dari daftar")
else:
    print(f"{suspect} tidak ditemukan dalam daftar")

print(f"Daftar anggota akhir: {daftar}")
