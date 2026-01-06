FILE_NAME = "mahasiswa.txt"

def tambah_mahasiswa():
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    prodi = input("Masukkan Program Studi: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{nim},{nama},{prodi}\n")

    print("Data mahasiswa berhasil ditambahkan.")

def tampilkan_mahasiswa():
    try:
        with open(FILE_NAME, "r") as file:
            data = file.readlines()
            if not data:
                print("Belum ada data mahasiswa.")
            else:
                for mhs in data:
                    nim, nama, prodi = mhs.strip().split(",")
                    print("NIM:", nim)
                    print("Nama:", nama)
                    print("Program Studi:", prodi)
                    print("-" * 30)
    except FileNotFoundError:
        print("File database belum tersedia.")

def cari_mahasiswa():
    cari_nim = input("Masukkan NIM yang dicari: ")
    ditemukan = False

    try:
        with open(FILE_NAME, "r") as file:
            for mhs in file:
                nim, nama, prodi = mhs.strip().split(",")
                if nim == cari_nim:
                    print("Data ditemukan:")
                    print("NIM:", nim)
                    print("Nama:", nama)
                    print("Program Studi:", prodi)
                    ditemukan = True
                    break
        if not ditemukan:
            print("Data mahasiswa tidak ditemukan.")
    except FileNotFoundError:
        print("File database belum tersedia.")

def hapus_mahasiswa():
    hapus_nim = input("Masukkan NIM yang akan dihapus: ")
    ditemukan = False
    data_baru = []

    try:
        with open(FILE_NAME, "r") as file:
            for mhs in file:
                nim, nama, prodi = mhs.strip().split(",")
                if nim != hapus_nim:
                    data_baru.append(mhs)
                else:
                    ditemukan = True

        with open(FILE_NAME, "w") as file:
            file.writelines(data_baru)

        if ditemukan:
            print("Data mahasiswa berhasil dihapus.")
        else:
            print("NIM tidak ditemukan.")

    except FileNotFoundError:
        print("File database belum tersedia.")

# ===== PROGRAM UTAMA =====
while True:
    print("\n===== MENU PENGELOLAAN MAHASISWA =====")
    print("1. Tambah Mahasiswa")
    print("2. Tampilkan Semua Mahasiswa")
    print("3. Cari Mahasiswa (NIM)")
    print("4. Hapus Mahasiswa")
    print("5. Keluar")

    menu = input("Pilih menu (1-5): ")

    if menu == "1":
        tambah_mahasiswa()
    elif menu == "2":
        tampilkan_mahasiswa()
    elif menu == "3":
        cari_mahasiswa()
    elif menu == "4":
        hapus_mahasiswa()
    elif menu == "5":
        print("Program selesai.")
        break
    else:
        print("Menu tidak valid.")