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

def main():
    while True:
        angkaSatu = int(input("Masukkan angka pertama: "))
        sistem = input("Masukkan sistem operasi\n(+, -, x, :): ")
        angkaDua = int(input("Masukkan angka kedua: "))
        print("-" * 30)

        if sistem != "+" and sistem != "-" and sistem != "x" and sistem != ":":
            print("Operasi nguawor!")
            continue

        output(angkaSatu, angkaDua, sistem)
        break

main()