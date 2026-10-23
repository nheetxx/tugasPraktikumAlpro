for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)


n = int(input("Jumlah baris: "))

for i in range(1, n + 1):
    baris = ""
    for j in range(1, i + 1):
        baris = baris + str(j) + " "
    print(baris)