#TP no 3
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
#TP no 5
n = int(input("Jumlah baris: "))
for i in range(1, n + 1):
    baris = ""
    for j in range(1, i + 1):
        baris = baris + str(j) + " "
    print(baris)


# ini punya zay
#TP no 3
for i in range(1, 4):
    print(f"Loop luar i = {i}")
    for j in range(1, 4):
        print(f"Loop dalam j = {j}")

#TP no 5
n = 5
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end=' ')
    for k in range(1, i + 1):
        print(k, end=' ')
    print()