while True:
    n = int(input("Masukkan n: ")) #misal n 3
    jarak = 1

    if n <= 0:
        continue

    for i in range(1, n + 1):
        baris = ""

        # for s in range(n - i):
        #     baris = baris + " "
        for a in range(i, 0, -1):
            baris = baris + str(a % 10)
        for b in range(2, i + 1):
            baris = baris + str(b % 10)
        # for s in range(n - i):
        for s in range(2 * (n - i)):
            baris = baris + " "

        for g in range(jarak):
            baris = baris + " "

        k = i
        for s in range(2 * (n - i)):
            baris = baris + " "
        for a in range(k, 0, -1):
            baris = baris + str(a % 10)
        for b in range(2, k + 1):
            baris = baris + str(b % 10)
        # k = n - i + 1
        # for s in range(i - 1):
        #     baris = baris + " "
        # for a in range(k, 0, -1):
        #     baris = baris + str(a % 10)
        # for b in range(2, k + 1):
        #     baris = baris + str(b % 10)

        print(baris)

    break