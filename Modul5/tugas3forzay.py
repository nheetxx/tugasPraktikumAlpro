def nilai(nama, tugas, uts, uas):
    nilaiAkhir = tugas * 30/100 + uts * 30/100 + uas * 40/100

    if nilaiAkhir >= 85:
        grade = "A"
    elif nilaiAkhir >= 70:
        grade = "B"
    elif nilaiAkhir >= 55:
        grade = "C"
    else:
        grade = "D"

    status = "Tidak Lulus" if grade == "D" else "Lulus"

    print(f"Nama        : {nama}")
    print(f"Nilai       : {nilaiAkhir}")
    print(f"Grade       : {grade}")
    print(f"Status      : {status}")
    print("-" * 30)

nama = input("Masukkan nama : ")
tugas = float(input("Nilai tugas   : "))
uts = float(input("Nilai UTS     : "))
uas = float(input("Nilai UAS     : "))
print("-" * 30)

nilai(nama, tugas, uts, uas)