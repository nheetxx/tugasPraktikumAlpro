#buatlahlist berisi 5 mahasiswa, tampilkan mahasiswa 1
#  dan terkahir, tambahkan 1 nama baru, hapus salah satu n
# ama menggunaka method tadi

mhs = ["Naufal", "Shiroko", "Megumin", "Nezuko", "Ruri"]
print(f"Nama mahasiswa pertama: {mhs[0]}")
print(f"Nama mahasiswa terakhir: {mhs[-1]}")
mhs.append("Nishimiya")
print(mhs)
lonet = mhs.pop(3)
print(f"Mahasiswa yang dihapus: {lonet}")
print(mhs)