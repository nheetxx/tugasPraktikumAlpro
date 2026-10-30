# def waifu():
#     nama = input("Masukkan nama waifu: ")
#     return nama
    
# print(f"Aku cinta {waifu()} >///<")


mA = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
mB = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

def penjumlahan():
    for baris in range(len(mA)):
                for kolom in range(len(mA[baris])):
                    print(mA[baris][kolom] + mB[baris][kolom], end=" ")
                print()

penjumlahan()