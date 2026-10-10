# if (kondisi):
#     statemen
    
#Program Printah if
nama = "python"
if nama == "python":
    print("Halo " + nama)
    
# if (kondisi):
#     statemen 1
# else:
#     statemen 2

#Program perintah if-else    
Kunci = "Python"
password = input("Masukkan password: ")
if password == Kunci:
    print("Password benar")
else:
    print("Password salah")
    
# if (kondisi 1):
#     statemen
# elif (kondisi 2):
#     statemen
# else:
#     statemen

#Program perintah if-elif-else
angka = int(input("Masukkan sebuah bilangan: "))
if angka > 0:
    print("Angka merupakan bilangan positif")
elif angka < 0:
    print("Angka merupakan bilangan negatif")
else:
    print("Angkar merupakan 0")
    
#Program if bersarang
x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))
if x == y :
    print("nilai", x ,"dan", y , "mempunyai nilai yang sama")
else:
    if x > y :
        print(x, "lebih besar daripada", y)
    if x < y:
        print(x, "lebih kecil daripada", y)


#Contoh mengembalikan nilai pada ternary
a = 20
b = 20
opet = "opet harus belajar" if a < b else opet = "opet tidak perlu belajar"
print(opet) 
    
a = 10
b= 20
print("Doni anak baik") if a == b else print("Doni bukan anak baik")