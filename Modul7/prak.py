# contoh = {"nama": "shiroko", "umur": 16, "kota": "Abydos"}

# contoh.clear()

# print(contoh)

#union
# x = {1, 2, 3, 4, 4}
# y = {3, 4, 5, 6, 7, 8}
# 
# z = y.difference(x)
# 
# print(z)
# 
# 

x = {}

try:
    x.pop()
    print("berhasil")
except TypeError as e:
    print("Error: ", e)