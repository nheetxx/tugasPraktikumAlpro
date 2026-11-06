# # L = ['python', 'java', 'c++', 'css', 'javascript', 'html']
# # print(L[::3])
# # print(L[2])
# # print(L[-2])
# # print(L[1:4])


# nilai = [100, 98, 97, 65, 89, 65, 90]

# nilai.append("nopal")
# nilai2 = [200, 70, 78]
# nilai.insert(1, "nopal")
# print(nilai)
# print(nilai.count("nopal"))
# print(nilai.extend(nilai2))
# nilai[1] = "shiroko"

# nilai[-3] = 100
# print(nilai)buah = ["anggur", "jeruk", "mangga", "pisang"]


# print(f"Buah awalnya adalah      {buah}")
# print(f"Buah saat ini            {buah}")
# hapus = buah.pop(0)
# print(f"Buah yang dihapus adalah {hapus}")
# print(buah)
# buah.append(hapus)
# buah.remove("pisang")
# del buah[1]
# print(buah)


# nilai = [1, 2, 3, 4, 5, 6, 77, 88]
# nilai.reverse()
# print(nilai)
# nilai.sort()
# print(nilai)


# nilai = (1, 2, 3, 4, 5)
# nilai2 = 1, 2, 3, 4, 5
# print(nilai)

# tup = ('cincin', 'anting', 'gelang')
# i = 0
# while i < len(tup):
    # print(tup[i])
    # i += 1

# outfit = ('baju', 'celana', 'rok')
# for i in outfit:
    # for j in outfit:
        # for k in outfit:
            # print(f"kombinasi outfit hari ini: {i}, {j}, {k}")


matriks = [
    [10, 20, 30], #Baris 0
    [40, 60, 89], #Baris 1
    [70, 80, 90]  #Baris 2
]
 
elemen = matriks[1][2]
print("Elemen baris 1 kolom 2:", elemen)

matriks[0][0] = 99
print("Matriks setelah diubah:", matriks[0])