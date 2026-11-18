undangan = set()
webinarA = set()
webinarB = set()

jumlah = int(input("jumlah undangan: "))
for i in range(jumlah):
    nama = input("nama undangan: ")
    undangan.add(nama)
print("-" * 30)

jumlah = int(input("jumlah peserta webinar A: "))
for i in range(jumlah):
    nama = input("nama peserta A: ")
    webinarA.add(nama)
print("-" * 30)

jumlah = int(input("jumlah peserta webinar B: "))
for i in range(jumlah):
    nama = input("nama peserta B: ")
    webinarB.add(nama)
print("-" * 30)

print("Total peserta    :", webinarA | webinarB)
print("hadir keduanya   :", webinarA & webinarB)
print("hadir salah satu :", webinarA ^ webinarB)
print("tidak hadir      :", undangan - (webinarA | webinarB))