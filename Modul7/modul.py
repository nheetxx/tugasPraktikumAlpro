# # Contoh cara membuat Dictionary pada Python

# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print("dict['Name']: ", dict['Name'])
# print("dict['Age']: ", dict['Age'])



# #Update dictionary Python

# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dict['Age'] = 8                 #Mengubah entri baru yang sudah ada
# dict['School'] = "DPS School"   #Menambah entri baru

# print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])



# #Contoh cara menghapus pada Dictionary Python

# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

# del dict['Name'] #Hapus entri dengan key 'Name'
# dict.clear()     #Hapus semua entri di dict
# del dict         #Hapus dictionary yang sudah ada

# print("dict['Age']: ", dict['Age'])
# print("dict['School']: ", dict['School'])




# set1 = set() #deklarasi set kosong
# set1.add(1)  #menambahkan isi set1



# >>> A = {1, 2, 3, 4, 5} >>> B = {4, 5, 6, 7, 8}



# #use union function
# >>> A.union(B)
# {1, 2, 3, 4, 5, 6, 7, 8}
# #user union function on B
# # >>> B.union(A)
# {1, 2, 3, 4, 5, 6, 7, 8}



# #use intersection function on A
# >>> A.intersection(B)
# {4, 5}
# #use intersection function on  B
# >>> B.intersection(A)
# {4, 5}




# #use difference  function on A
# >>> A.difference(B)
# {1, 2, 3}
# #use - operator on (B)
# >>> B - A
# {8, 6, 7}
# #use difference function on B
# >>> B.difference(A)
# {8, 6, 7}




# #use symmetric_difference function on A
# >>> A.symmetric_difference(B)
# {1, 2, 3, 6, 7, 8}
# #use symmetric_difference function on B
# >>> B.symmetric_difference(A)
# {1, 2, 3, 6, 7, 8} 




# try:
#     #kode yang berpotensi menimbulkan error
# except NamaEror:
#     #kode yang dijalankan jika error terjadi
    
    
    

# angka = int('abc')
# print("Program selesai")



# try:
#     angka = int('abc')
#     print(angka)
# except ValueError:
#     print("Input harus berupa angka")

# print("Program selesai")






# mahasiswa = {"Andi": 85,"Budi": 90}

# try:
#     print(mahasiswa["Citra"])
# except  KeyError:
#     print("Nama tidak ditemukan")
    
    
    
# hobi = {"membaca", "menulis"}

# try:
#     hobi.remove("berenang")
# except KeyError:
#     print("Elemen tidak ada di himpunan")
    
    
    

# kosong = set()

# try:
#     kosong.pop()
# except KeyError as e:
#     print("Error:", e)
    



