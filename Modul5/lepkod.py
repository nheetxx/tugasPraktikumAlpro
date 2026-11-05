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
        try:
            angkaSatu = int(input("Masukkan angka pertama                  : "))
        except ValueError:
            print("Input harus berupa angka! silahkan masukkan angka yang benar\n")
            continue
        
        sistem = input("Masukkan sistem operasi (+, -, x, :)    : ")
        
        try:
            angkaDua = int(input("Masukkan angka kedua                    : "))
        except ValueError:
            print("Input harus berupa angka! silahkan masukkan angka yang benar\n")
            continue
        
        print("-" * 30)

        if sistem != "+" and sistem != "-" and sistem != "x" and sistem != ":":
            print("Operasi nguawor! silahkan masukkan operasi yang benar\n")
            continue

        if sistem == ":" and angkaDua == 0:
            print("Tidak bisa membagi dengan nol!\n")
            continue

        output(angkaSatu, angkaDua, sistem)
        
        while True:
            continueKalkulator = input("Apakah anda ingin melanjutkan kalkulator? (y/n) ").lower()
            if continueKalkulator == "y":
                break
            elif continueKalkulator == "n":
                print(f"Arigatouuuuu, sampai jumpa lagi! >///<")
                exit()
            else:
                print(f"Input {continueKalkulator} nguawor! silahkan masukkan 'y' atau 'n'")
                continue

main()