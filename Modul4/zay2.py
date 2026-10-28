gajiPokok = 100000
uangShiftMalam = 0
totalGaji = 0

for hari in range(1, 8):
    gajiHarian = 0
    upahLembur = 0

    jamLembur = int(input("Masukkan jam lembur: "))

    shiftMalam = input("Apakah pekerja shift malam?(Y/N): ")
    if shiftMalam == "Y" or shiftMalam == "y":
        gajiHarian += 50000
            
    if jamLembur <= 3:
        upahLembur = 25000 * jamLembur
    elif jamLembur <= 5:
        upahLembur = 100000
    elif jamLembur <= 7:
        upahLembur = 200000
    elif jamLembur == 8:
        upahLembur = 300000
    else:
        print("Jumlah lembur melebihi batas yang ditentukan.")
        upahLembur = 0
    
    gajiHarian = gajiPokok
    gajiHarian += upahLembur
    totalGaji += gajiHarian
    
    print("Total gaji hari ke", hari, "Rp", gajiHarian)
    
print("Total gaji dalam seminggu: Rp", totalGaji)