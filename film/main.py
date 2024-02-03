import function
ulang = "y"

while ulang.lower() == "y":
    print()
    print("-"*80)
    print("🎬  ** Welcome to the Movie Management System! **  🎬".center(80, ' '))
    print("-"*80)
    print()
    print("   1. ➕  Tambah Film Baru")
    print("   2. ️👁️  Tampilkan Seluruh Film")
    print("   3. 🔍  Cari Film (Searching)")
    print("   4. ❌  Hapus Film")
    print("   5. 🔢  Urutkan Film (Sorting)")
    print("   0. 🚪  Exit the system\n")

    pilih = int(input("\nEnter your choice: "))

    if pilih == 1:
        function.tambah_movie()
    elif pilih == 2:
        print("\n** Daftar Semua Film **".center(50))
        function.all_movie()
    elif pilih == 3:
        print("\n** Cari Film **".center(50))
        function.cari_film()
    elif pilih == 4:
        print("\n** Hapus a Movie **".center(50))
        function.hapus_film()
    elif pilih == 5:
        print("\n** Urutkan Film (Sorting) **".center(50))
        function.sorting_movie()
    elif pilih == 0:
        print("\n** Exit the System **".center(50))
        print("\nProgram selesai.")
        ulang = "n"
        break
    else:
        print()
        print('!!! Inputan Tidak Valid!!!')

    print()
    ulang = input("Apakah Anda Akan Kembali Ke Menu Aplikasi ? (y/n) : ")

    while ulang.lower() not in ["y", "n"]:
        print()
        print('!!! Inputan Tidak Valid!!!')
        print()
        ulang = input("Apakah Anda Akan Kembali Ke Menu Aplikasi ? (y/n) : ")

print()
print("="*50)
print("Terimakasih Telah Menggunakan Program Kami".center(50))
print("="*50)

profile = [
    ["10123395", "Muhammad Raihan Nur Aziz", "IF-10"],
    ["10123391", "Rizky Fathurohman", "IF-10"],
    ["10123395", "Raditya Rizqullah Anwar", "IF-10"],
    ["10123401", "Lutfi Pramudya", "IF-10"],
    ["10123404", "Gilang Aldiano", "IF-10"],
    ["10123404", "Farhan", "IF-10"],
]
print("Profile Kelompok".center(50))
print("="*50)
print()
function.tampilkan_tabel("nama", profile)
