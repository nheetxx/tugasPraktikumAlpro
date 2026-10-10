# digit1 = int(input("Masukkan digit pertama: "))
# digit2 = int(input("Masukkan digit kedua: "))
# digit3 = int(input("Masukkan digit ketiga: "))

password = int(input("Masukkan Password 3 digit: "))

digit1 = password // 100
digit2 = (password // 10) % 10
digit3 = password % 10

pelacak = digit1 * digit3

if digit2 % 2 == 0:
    pelacak = pelacak - digit2
else:
    pelacak1 = pelacak + 25

if pelacak1 % 3 == 0:
    pelacak2 = pelacak1 // 3
else:
    pelacak2 = pelacak1 * 2

if pelacak2 > 50:
    kategori = "Kategori A"
elif pelacak2 > 20:
    kategori = "Kategori B"
else:
    kategori = "Password Ditolak"
        
if pelacak2 % 2 == 0:
    siklus = "Genap"
else:
    siklus = "Ganjil"

print(f"Digit anda                              : {digit1}, {digit2}, {digit3}")
print(f"Nilai pelacak awal                      : {pelacak}")
print(f"Nilai pelacak setelah perubahan pertama : {pelacak1}")
print(f"Nilai pelacak setelah perubahan kedua   : {pelacak2}")
print(f"Status Password                         : {kategori}")
print(f"Siklus pelacak                          : {siklus}")