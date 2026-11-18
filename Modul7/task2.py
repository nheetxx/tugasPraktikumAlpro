playlist = {

}

while True:
    print("1. buat playlist")
    print("2. tambah lagu")
    print("3. lihat semua playlist")
    print("4. cari lagu")
    print("5. hapus lagu")
    print("6. hapus playlist")
    print("0. keluar")
    userPilih = input("pilih: ")

    if userPilih == "1":
        namaPlaylist = input("nama playlist: ")
        playlist[namaPlaylist] = {}
        print("-" * 30)

    elif userPilih == "2":
        namaPlaylist = input("nama playlist: ")
        judulLagu = input("judul lagu: ")
        penyanyi = input("penyanyi: ")
        try:
            playlist[namaPlaylist][judulLagu] = penyanyi
        except KeyError:
            print(f"playlist {namaPlaylist} tidak ada")
        print("-" * 30)

    elif userPilih == "3":
        for i in playlist:
            print(i)
            for k in playlist[i]:
                print(f"-- {k} - {playlist[i][k]}")
        print("-" * 30)
    
    elif userPilih == "4":
        cari = input("judul lagu: ")
        ada = False
        for i in playlist:
            if cari in playlist[i]:
                print(f"{cari} ada di {i}  ({playlist[i][cari]})")
                ada = True
        if ada == False:
            print(f"lagu {cari} tidak ada")
        print("-" * 30)

    elif userPilih == "5":
        namaPlaylist = input("nama playlist: ")
        judulLagu = input("judul lagu: ")
        try:
            del playlist[namaPlaylist][judulLagu]
        except KeyError:
            print("playlist atau lagu tidak ada")
        print("-" * 30)
        
    elif userPilih == "6":
        namaPlaylist = input("nama playlist: ")
        try:
            del playlist[namaPlaylist]
        except KeyError:
            print(f"playlist {namaPlaylist} tidak ada")
        print("-" * 30)
        
    elif userPilih == "0":
        break
    
    else:
        print(f"{userPilih} tidak ada di menu")