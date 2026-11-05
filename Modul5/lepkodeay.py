def hitungHasil(angkaSatu, angkaDua, sistem):
    if sistem == "+":
        return angkaSatu + angkaDua
    elif sistem == "-":
        return angkaSatu - angkaDua
    elif sistem == "x":
        return angkaSatu * angkaDua
    else:
        return angkaSatu / angkaDua


def output(angkaSatu, angkaDua, sistem):
    hasilAkhir = hitungHasil(angkaSatu, angkaDua, sistem)
    print(f"Hasil dari {angkaSatu} {sistem} {angkaDua} = {hasilAkhir}")
    print("-" * 30)


def inputAman(prompt):
    # biar Ctrl+C / Ctrl+D nggak ngeluarin traceback
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        print("\nProgram dihentikan. Arigatouuuuu, sampai jumpa lagi! >///<")
        raise SystemExit(0)


def bacaAngka(prompt):
    teks = inputAman(prompt).strip().replace(",", ".")
    if teks == "":
        return None
    try:
        return int(teks)
    except ValueError:
        pass
    try:
        return float(teks)
    except ValueError:
        return None


def bacaSistem(prompt):
    # "X", "/", "*" dan spasi tetap diterima
    teks = inputAman(prompt).strip().lower()
    if teks == "*":
        return "x"
    elif teks == "/":
        return ":"
    return teks


def main():
    print("-" * 30)
    print("Selamat datang di kalkulator sederhana")
    print("-" * 30)

    while True:
        angkaSatu = bacaAngka("Masukkan angka pertama                  : ")
        if angkaSatu is None:
            print("Input harus berupa angka! silahkan masukkan angka yang benar\n")
            continue

        sistem = bacaSistem("Masukkan sistem operasi (+, -, x, :)    : ")
        if sistem not in ("+", "-", "x", ":"):
            print("Operasi nguawor! silahkan masukkan operasi yang benar\n")
            continue

        angkaDua = bacaAngka("Masukkan angka kedua                    : ")
        if angkaDua is None:
            print("Input harus berupa angka! silahkan masukkan angka yang benar\n")
            continue

        print("-" * 30)

        if sistem == ":" and angkaDua == 0:
            print("Tidak bisa membagi dengan nol!\n")
            continue

        output(angkaSatu, angkaDua, sistem)

        while True:
            continueKalkulator = inputAman("Apakah anda ingin melanjutkan kalkulator? (y/n) ")
            jawaban = continueKalkulator.strip().lower()
            if jawaban == "y":
                print("-" * 30)
                break
            elif jawaban == "n":
                print("Arigatouuuuu, sampai jumpa lagi! >///<")
                raise SystemExit(0)
            else:
                print(f"Input {continueKalkulator} nguawor! silahkan masukkan 'y' atau 'n'")


if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        pass
