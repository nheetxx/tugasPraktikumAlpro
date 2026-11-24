todolist = {

}

while True:
    print("-" * 30)
    print("1. Tambah tugas")
    print("2. Tampilkan tugas")
    print("3. Tandai tugas selesai")
    print("4. Hapus tugas")
    print("5. Statistik tugas")
    print("0. Keluar")
    # userInput = int(input(": "))
    # try:
    #     userInput = int(userInput)
    # except ValueError:
    #     continue
    try: 
        userInput = int(input(": "))
    except ValueError:
        continue

    if userInput == 1:
        while True:
            print("-" * 30)
            taskUserInput = input("Nama tugass: ")
            if taskUserInput != "":
                if taskUserInput in todolist:
                    print(f"{taskUserInput} sudah ada")
                    break
                else:
                    # todolist[taskUserInput] = False
                    todolist[taskUserInput] = "Belum"
                    print(f"{taskUserInput} ditambahkan")
                    break

    elif userInput == 2:
        print("-" * 30)
        if todolist == {}:
            print("Tugas kosong")
        else:
            for i in todolist.items():
                task = i[0]
                status = i[1]
                print(f"{task} = {status}")
                # if status == True:
                #     statusTask = "Selesai"
                # else:
                #     statusTask = "Belum selesai"
                # print(f"{task} = {statusTask}")

    elif userInput == 3:
        print("-" * 30)
        taskUserInput = input("Tugas yang selesai: ")
        if taskUserInput in todolist:
            # todolist[taskUserInput] = True
            todolist[taskUserInput] = "Sudah"
            print(f"{taskUserInput} ditandai selesai")
        else:
            print(f"{taskUserInput} tidak ada")

    elif userInput == 4:
        print("-" * 30)
        taskUserInput = input("Tugas yang mau dihapus: ")
        if taskUserInput in todolist:
            del todolist[taskUserInput]
            print(f"{taskUserInput} dihapus")
        else:
            print(f"{taskUserInput} tidak ada")

    elif userInput == 5:
        print("-" * 30)
        tugasSelesai = 0
        tugasBelumS = 0
        for i in todolist.items():
            status = i[1]
            # if status == True:
            #     tugasSelesai += 1
            # else:
            #     tugasBelumS += 1
            if status == "Sudah":
                tugasSelesai += 1
            else:
                tugasBelumS += 1
        print(f"Selesai: {tugasSelesai}")
        print(f"Belum selesai: {tugasBelumS}")

    elif userInput == 0:
        break

    else:
        continue