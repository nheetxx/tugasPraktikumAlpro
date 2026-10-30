jumlahBaris = int(input("Jumlah baris: ")) #input 5
jumlahLampu = int(input("Jumlah lampu pada setiap baris: "))

nomorLampu = 4

for baris in range(1, jumlahBaris+1):
    print("Baris")
    for lampu in range(1, jumlahLampu+1):
        if nomorLampu % 3 == 0:
            print("Lampu", nomorLampu, "mengalami gangguan")
        else:
            print("Lampu", nomorLampu, "normal")
        nomorLampu += 1