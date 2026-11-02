def hitungHasil(angkaSatu, angkaDua, sistem):
    if sistem == "+":
        return angkaSatu + angkaDua
    elif sistem == "-":
        return angkaSatu - angkaDua
    elif sistem == "x":
        return angkaSatu * angkaDua
    elif sistem == ":":
        return angkaSatu / angkaDua

def output(angkaSatu, angkaDua, sistem):
    hasilAkhir = hitungHasil(angkaSatu, angkaDua, sistem)
    print(f"Hasil dari {angkaSatu} {sistem} {angkaDua} = {hasilAkhir}")
    print("-" * 30)

print("-" * 30)
print("Selamat datang di kalkulator sederhana")
print("-" * 30)

def main():
    while True:
        angkaSatu = int(input("Masukkan angka pertama                  : "))
        sistem = input("Masukkan sistem operasi (+, -, x, :)    : ")
        angkaDua = int(input("Masukkan angka kedua                    : "))
        print("-" * 30)

        if sistem != "+" and sistem != "-" and sistem != "x" and sistem != ":":
            print("Operasi nguawor! silahkan masukkan operasi yang benar\n")
            continue

        output(angkaSatu, angkaDua, sistem)
        continueKalkulator = input("Apakah anda ingin melanjutkan kalkulator? (y/n) ")
        if continueKalkulator.lower() != "y":
            break
main()