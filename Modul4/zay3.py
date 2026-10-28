n = int(input("Masukkan n: "))
    
for i in range(1, n + 1):
    baris = ""
    for a in range(1, i + 1):
        baris = baris + str(a % 10)
    for s in range(2 * (n - i) + 1):
        baris = baris + " "
    for a in range(i, 0, -1):
        baris = baris + str(a % 10)
    print(baris)