asisten_awal = []
while True:
    nama = input("Masukkan nama asisten awal (ketik 'cukup' untuk berhenti): ")
    if nama == "cukup":
        break
    asisten_awal.append(nama)

# tuple = data terkunci, tidak bisa diubah lagi
asisten_awal = tuple(asisten_awal)

asisten_tambahan = input("Masukkan nama asisten tambahan: ")
asisten_akhir = list(asisten_awal) + [asisten_tambahan]

hari_list = []
while True:
    hari = input("Masukkan nama hari tugas (ketik 'cukup' untuk berhenti): ")
    if hari == "cukup":
        break
    hari_list.append(hari)

hari_list = tuple(hari_list)

pengecualian_asisten = input("Nama asisten pengecualian: ")
pengecualian_hari = input("Hari pengecualian: ")

for nama in asisten_akhir:
    for hari in hari_list:
        # kombinasi asisten + hari yang dikecualikan dilewati
        if nama == pengecualian_asisten and hari == pengecualian_hari:
            continue
        print(f"{nama} bertugas pada hari {hari}")
