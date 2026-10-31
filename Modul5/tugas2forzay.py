def palindrom(kata):
    balik = ""
    for huruf in kata:
        balik = huruf + balik
    return True if kata == balik else False

kata = str(input("Masukkan kata : "))
print(f"{kata} adalah palindrom") if palindrom(kata) else print(f"{kata} bukan palindrom")