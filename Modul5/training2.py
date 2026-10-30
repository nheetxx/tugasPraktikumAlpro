# nilaiTugas = 80
# nilaiUts = 70
# nilaiUas = 90

def hitungAkhir(tugas, uts, uas):
    tugas *= 30/100
    uts *= 30/100
    uas *= 40/100
    return tugas + uts + uas

def tentukanGrade(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 60:
        return "C"
    else:
        return "D"

def lulus(grade):
    return grade != "D"
    
data = [("Budi", 80, 70, 90), ("Ani", 60, 50, 55), ("Fall", 95, 90, 100)]

for nama, tugas, uts, uas in data:
    akhir = hitungAkhir(tugas, uts, uas)
    grade = tentukanGrade(akhir)
    status = "Lulus" if lulus(grade) else "Tidak Lulus"    
    
    print(f"Nama       : {nama}")
    print(f"Nilai akhir: {akhir}")
    print(f"Grade      : {grade}")
    print(f"Status     : {status}\n")
    



    