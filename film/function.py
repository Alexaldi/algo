movies = [
    ["8", "The Shawshank Redemption", "DRAMA"],
    ["4", "The Godfather", "CRIME"],
    ["6", "The Dark Knight", "ACTION"],
    ["9", "12 Angry Men", "CRIME"],
    ["3", "The Lord of the Rings: The Fellowship of the Ring", "FANTASY"],
    ["5", "The Silence of the Lambs", "THRILLER"],
    ["2", "Schindler's List", "DRAMA"],
    ["1", "Pulp Fiction", "CRIME"],
    ["7", "The Good, the Bad and the Ugly", "WESTERN"],
    ["10", "Forrest Gump", "DRAMA"],
]


# Fungsi Pertama
def tambah_movie():
    print("\n** Tambah Film Baru**\n".center(50))
    kode_film = input(
        "Masukkan Kode Film (Harap masukkan angka tunggal, contoh: 2, 3, 10, dll.) : ")
    for movie in movies:
        if int(movie[0]) == int(kode_film) and kode_film.isdigit() == True:
            print("\nKode Film sudah ada. Silakan masukkan kode yang berbeda.\n")
            return tambah_movie()  # Restart the entire function

    judul_film = input("Masukkan Judul Film: ")
    genre_film = input("Masukkan Genre Film: ")

    new_movie = [kode_film, judul_film.capitalize(), genre_film.upper()]
    movies.append(new_movie)

    print("\nMovie berhasil ditambahkan!\n")
    all_movie()

# Fungsi Kedua


def all_movie():
    tampilkan_tabel("proses", movies)

# fungsi ketiga


def tampilkan_tabel(rows, data):
    if rows == "proses":
        judul_kolom = ['Kode Film', 'Judul Film', 'Genre']
    elif rows == "nama":
        judul_kolom = ['NIM', 'Nama', 'Kelas']

    column_widths = [max(len(str(row[i])) for row in [judul_kolom] + data)
                     for i in range(len(judul_kolom))]

    print("+" + "+".join("-" * (width + 2) for width in column_widths) + "+")

    print("|" + "|".join(f" {judul.center(width)} " for judul,
          width in zip(judul_kolom, column_widths)) + "|")

    print("+" + "+".join("-" * (width + 2) for width in column_widths) + "+")

    for row in data:
        print("|" + "|".join(f" {data.center(width)} " for data,
              width in zip(row, column_widths)) + "|")

    print("+" + "+".join("-" * (width + 2) for width in column_widths) + "+")


def cari_film():
    def sequence_search(data, dicari_kode):
        i = 0
        banyak_data = len(data)
        while (i < banyak_data) and (data[i][0] != dicari_kode):
            i = i + 1
        if i < banyak_data:
            return i
        else:
            return -1

    all_movie()
    print()
    dicari_kode = input("Masukkan kode film yang ingin dicari: ")
    posisi = sequence_search(movies, dicari_kode)

    if posisi >= 0:
        print(
            f"\nFilm dengan kode '{dicari_kode}' ditemukan di posisi {posisi + 1}:\n")
        tampilkan_tabel("proses", [movies[posisi]])
    else:
        print(f"Tidak ada film dengan kode '{dicari_kode}'")
        return cari_film()

# fungsi ke empat


def followup(x):
    if x == 'Y':
        print()
    elif x == 'T':
        print()
        print('!!! Aktifitas dibatalkan !!!')
        print()
    else:
        print()
        print('!!! Masukan keyword yang benar !!!')
        print()
        return hapus_film()


def hapus_film():
    all_movie()
    hapus_movie = input("\n Masukkan kode film yang ingin dihapus: ")
    var_tem = 1
    while var_tem <= len(movies):
        print(var_tem)
        if hapus_movie == movies[var_tem-1][0]:
            tampilkan_tabel("proses", [movies[var_tem-1]])
            simpan_data_3 = input(
                f'Apakah Anda ingin menghapus Film {movies[var_tem-1][1]} ini? (Y/T):').upper()
            followup(simpan_data_3)
            if simpan_data_3 == 'Y':
                movies.pop(var_tem-1)
                all_movie()
                print()
                break
            else:
                break
        else:
            var_tem += 1
    else:
        print()
        print('!!! Kode Film yang di input tidak tersedia !!!')
        print()
        return hapus_film()

# fungsi sorting


def bubble_sort_naik(data):
    n = len(data)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if int(data[i][0]) > int(data[j][0]):
                temp = data[i]
                data[i] = data[j]
                data[j] = temp


def bubble_sort_turun(data):
    n = len(data)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if int(data[i][0]) < int(data[j][0]):
                temp = data[i]
                data[i] = data[j]
                data[j] = temp


def sorting_movie():
    posisi = input(
        "Inputkan Urutan Yang Ingin Anda Lakukan ? (Naik / Turun) : ")
    if posisi.upper() == "NAIK":
        bubble_sort_naik(movies)
        all_movie()
    elif posisi.upper() == "TURUN":
        bubble_sort_turun(movies)
        all_movie()
    else:
        print()
        print('!!! Inputan Tidak Valid!!!')
        print()
        return sorting_movie()
