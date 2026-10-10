# digit1 = int(input("Masukkan digit pertama: "))
# digit2 = int(input("Masukkan digit kedua: "))
# digit3 = int(input("Masukkan digit ketiga: "))

pin = int(input("Masukkan PIN 3 digit: "))
jamDatang = int(input("Jam Kedatangan (dalam format 0-23): "))

digit1 = pin // 100
digit2 = (pin // 10) % 10
digit3 = pin % 10

if (digit1 % 5 == 0) and (digit2 % 5 == 0) and (digit3 % 5 == 0):
    if jamDatang < 12:
        pesan = "Garasi Pagi Terbuka"
    else:
        pesan = "Garasi Malam Terbuka, Lampu Dinyalakan"
elif (digit1 % 2 == 0) and (digit2 % 2 == 0) and (digit3 % 2 == 0):
    if (digit1 + digit3) == digit2:
        pesan = "Garasi VIP Terbuka Khusus Bos"
    else:
        pesan = "Kode Genap Ditolak, Alarm Berbunyi!"
else:
    pesan = "Akses DITOLAK"
    
print(f"PIN                : {digit1} {digit2} {digit3}")
print(f"Pesan Akses Pintu  : {pesan}")
print("Mode Malam Merekam") if jamDatang > 18 else print("Mode Siang Standby")
