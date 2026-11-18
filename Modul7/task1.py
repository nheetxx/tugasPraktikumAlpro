todolist = {

}

while True:
    print("1. tambah tugas")
    print("2. lihat tugas")
    print("3. tandai selesai")
    print("4. hapus tugas")
    print("5. jumlah selesai/belum")
    print("0. keluar")
    userPilih = input("---: ")

    if userPilih == "1":
        namaTugas = input("nama tugas: ")
        todolist[namaTugas] = "belum"
        print("-" * 30)
    
    elif userPilih == "2":
        for i in todolist.items():
            indnol = i[0]
            indsat = i[1]
            print(f"{indnol} : {indsat}")
        print("-" * 30)
    
    elif userPilih == "3":
        namaTugas = input("nama tugas: ")
        if namaTugas in todolist:
            todolist[namaTugas] = "selesai"
        else:
            print(f"tugas {namaTugas} tidak ditemukan")
        print("-" * 30)

    elif userPilih == "4":
        namaTugas = input("nama tugas: ")
        try:
            del todolist[namaTugas]
        except KeyError:
            print(f"{namaTugas} tidak ditemukan")
        print("-" * 30)

    elif userPilih == "5":
        tugasSelesai = 0
        tugasBelum = 0
        for i in todolist.values():
            if i == "selesai":
                tugasSelesai += 1
            else:
                tugasBelum += 1 
        print(f"tugas yang selesai: {tugasSelesai}")
        print(f"tugas belum selesai: {tugasBelum}")
        print("-" * 30)

    elif userPilih == "0":
        break

    else:
        print(f"pilihan {userPilih} tidak ada di menu.")
        print("-" * 30)