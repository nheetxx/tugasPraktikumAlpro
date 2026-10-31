def test(kurung):
    print(f"Ini test, ini kurung {kurung}")
    
            
    
test("nopal\n")

def kali(a, b):
    return a * b

hasil = kali(5, 2)
print(f"ini hasil kali dari variabel hasil {hasil}\n")

def tambah(a, b):
    return a + b

tambah2 = lambda a, b: a + b

print(tambah(3, 4))
print(f"{tambah2(3, 4)}\n")

def kurang(x, y):
    return x - y
print(kurang(5, 2))

kurang = lambda x, y: x - y
print(f"{kurang(5, 2)}\n")

