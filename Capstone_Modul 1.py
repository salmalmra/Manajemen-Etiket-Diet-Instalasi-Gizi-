print("""
============================================================
            SISTEM DATA PASIEN INSTALASI GIZI
============================================================
Program ini digunakan untuk mencatat, melihat, memperbarui,
dan menghapus data pasien beserta status gizinya.
============================================================

""")



data_pasien = [
    {
        "No RM": "RM001",
        "Nama": "Andi Pratama",
        "Umur": 28,
        "Jenis Kelamin": "Laki-laki",
        "Tinggi": 170,
        "Berat": 65,
        "IMT": 22.49,
        "Status Gizi": "Normal"
    },
    {
        "No RM": "RM002",
        "Nama": "Budi Santoso",
        "Umur": 35,
        "Jenis Kelamin": "Laki-laki",
        "Tinggi": 165,
        "Berat": 80,
        "IMT": 29.38,
        "Status Gizi": "Overweight"
    },
    {
        "No RM": "RM003",
        "Nama": "Citra Dewi",
        "Umur": 24,
        "Jenis Kelamin": "Perempuan",
        "Tinggi": 160,
        "Berat": 45,
        "IMT": 17.58,
        "Status Gizi": "Underweight"
    },
    {
        "No RM": "RM004",
        "Nama": "Diana Putri",
        "Umur": 31,
        "Jenis Kelamin": "Perempuan",
        "Tinggi": 155,
        "Berat": 60,
        "IMT": 24.97,
        "Status Gizi": "Normal"
    },
    {
        "No RM": "RM005",
        "Nama": "Eko Saputra",
        "Umur": 40,
        "Jenis Kelamin": "Laki-laki",
        "Tinggi": 172,
        "Berat": 95,
        "IMT": 32.09,
        "Status Gizi": "Obesitas"
    }
]



def hitung_imt(berat, tinggi):
    IMT = round(berat / ((tinggi / 100) ** 2), 2)
    if IMT < 18.5:
        status = "Underweight"
    elif 18.5 <= IMT <= 24.9:
        status = "Normal"
    elif 25 <= IMT <= 29.9:
        status = "Overweight"
    else:
        status = "Obesitas"
    return IMT, status



def data_seluruh():
    if len(data_pasien) == 0:
        print("\n===================================================")
        print("\t\tTidak Ada Data Pasien")
        print("===================================================")
        return

    print("\n\t\t\tDATA SELURUH PASIEN")
    print("--------------------------------------------------------------------------------------------------")
    print("INDEX | NO RM  | NAMA             | JK         | UMUR | TINGGI | BERAT  | IMT   | STATUS GIZI")
    print("--------------------------------------------------------------------------------------------------")

    i = 0
    for p in data_pasien:
        print(f"  {i}\t| {p['No RM']}\t| {p['Nama']}\t| {p['Jenis Kelamin']}\t| {p['Umur']}\t| {p['Tinggi']}\t| {p['Berat']}\t| {p['IMT']}\t| {p['Status Gizi']}")
        i += 1

    print("--------------------------------------------------------------------------------------------------")



def baca_Data():
    while True:
        bacaData = input('''\n
        ---------------Menampilkan Data Pasien---------------

        Pilihan Menu :
        1. Data Seluruh Pasien
        2. Data Pasien Tertentu
        3. Kembali ke Menu Utama

        Masukkan angka sub menu yang ingin dijalankan : ''')

        if bacaData == '1':
            data_seluruh()

        elif bacaData == '2':
            if len(data_pasien) == 0:
                print('\tTidak Ada Data Pasien.')
                continue
            try:
                inputBaca = int(input('\nMasukkan index data pasien yang ingin ditampilkan: '))
            except ValueError:
                print('\tHarap masukkan angka index, bukan teks.\n')
                continue

            if 0 <= inputBaca < len(data_pasien):
                data = data_pasien[inputBaca]
                print('\nData pasien dengan index', inputBaca)
                print("------------------------------------------------------------")
                for key, value in data.items():
                    print(f"{key}: {value}")
                print("------------------------------------------------------------")
            else:
                print('\tIndex tidak ditemukan. Silakan masukkan angka antara 0 dan', len(data_pasien)-1)

        elif bacaData == '3':
            break
        else:
            print('\tPilihan tidak valid. Silakan masukkan angka 1-3.')



def tambah_Data():
    while True:
        tambahData = input('''\n
        ---------------Menambah Data Pasien---------------

        Pilihan Menu :
        1. Tambah Data Pasien
        2. Kembali ke Menu Utama

        Masukkan angka sub menu yang ingin dijalankan : ''')

        if tambahData == '1':
            no_rm = input('\nMasukkan Nomor RM Pasien : ').upper()
            namaPasien = input('Masukkan Nama Pasien : ').title()

            while True:
                jenisKelamin = input('Masukkan Jenis Kelamin (L/P atau Laki-laki/Perempuan) : ').strip().upper()

                if jenisKelamin == 'L':
                    jenisKelamin = 'Laki-laki'
                    break
                elif jenisKelamin == 'P':
                    jenisKelamin = 'Perempuan'
                    break
                elif jenisKelamin in ['LAKI-LAKI', 'PEREMPUAN']:
                    jenisKelamin = jenisKelamin.title()
                    break
                else:
                    print("Input tidak valid. Masukkan hanya 'L', 'P', 'Laki-laki', atau 'Perempuan'.")

            try:
                umurPasien = int(input('Masukkan Umur Pasien : '))
                tinggiPasien = float(input('Masukkan Tinggi Badan (cm) : '))
                beratPasien = float(input('Masukkan Berat Badan (kg) : '))
            except ValueError:
                print('Input umur, tinggi, dan berat harus berupa angka.\n')
                continue

            IMT, status = hitung_imt(beratPasien, tinggiPasien)

            choice = input('\nApakah Anda yakin data ingin ditambahkan? (Y/N) : ').upper()
            if choice == 'Y':
                data_pasien.append({
                    'No RM': no_rm,
                    'Nama': namaPasien,
                    'Umur': umurPasien,
                    'Jenis Kelamin': jenisKelamin,
                    'Tinggi': tinggiPasien,
                    'Berat': beratPasien,
                    'IMT': IMT,
                    'Status Gizi': status
                })
                print('============================================================')
                print('\t\t      Data Tersimpan')
                print('============================================================')
            else:
                print('============================================================')
                print('\t\t     Data Dibatalkan')
                print('============================================================')

        elif tambahData == '2':
            break
        else:
            print('Pilihan tidak valid. Coba lagi.')



def perbarui_Data():
    while True:
        perbaruiData = input('''\n
        ---------------Memperbarui Data Pasien---------------

        Pilihan Menu :
        1. Perbarui Data Pasien
        2. Kembali ke Menu Utama

        Masukkan angka sub menu yang ingin dijalankan : ''')

        if perbaruiData == '1':
            try:
                index = int(input('\nMasukkan index data pasien yang ingin diperbarui: '))
            except ValueError:
                print('Masukkan angka index yang valid.')
                continue

            if 0 <= index < len(data_pasien):
                kolom = input('Masukkan kolom yang ingin diperbarui (Nama/Umur/Jenis Kelamin/Tinggi/Berat): ').title()
                if kolom not in ['Nama', 'Umur', 'Jenis Kelamin', 'Tinggi', 'Berat']:
                    print('\nKolom tidak valid.')
                    continue

                nilaiBaru = input(f'Masukkan nilai baru untuk {kolom}: ')
                if kolom in ['Umur', 'Tinggi', 'Berat']:
                    try:
                        nilaiBaru = float(nilaiBaru) if kolom != 'Umur' else int(nilaiBaru)
                    except ValueError:
                        print('Input harus berupa angka untuk kolom tersebut.')
                        continue

                konfirmasi = input('\nApakah Anda yakin ingin memperbarui data ini? (Y/N): ').upper()
                if konfirmasi == 'Y':
                    data_pasien[index][kolom] = nilaiBaru
                    if kolom in ['Tinggi', 'Berat']:
                        berat = float(data_pasien[index]['Berat'])
                        tinggi = float(data_pasien[index]['Tinggi'])
                        IMT, status = hitung_imt(berat, tinggi)
                        data_pasien[index]['IMT'] = IMT
                        data_pasien[index]['Status Gizi'] = status
                    print('\n============================================================')
                    print('\t\t      Data Berhasil Diperbarui')
                    print('============================================================')
                else:
                    print('\nData tidak diperbarui.')
            else:
                print('\nIndex tidak ditemukan.')

        elif perbaruiData == '2':
            break
        else:
            print('Pilihan tidak valid. Coba lagi.')



def hapus_Data():
    while True:
        hapusData = input('''\n
        ---------------Menghapus Data Pasien---------------

        Pilihan Menu :
        1. Hapus Data Pasien
        2. Kembali ke Menu Utama

        Masukkan angka sub menu yang ingin dijalankan : ''')

        if hapusData == '1':
            if len(data_pasien) == 0:
                print('\nTidak ada data untuk dihapus.')
                continue
            try:
                index = int(input('\nMasukkan index data pasien yang ingin dihapus: '))
            except ValueError:
                print('Masukkan angka index yang valid.')
                continue

            if 0 <= index < len(data_pasien):
                konfirmasi = input('\nApakah Anda yakin ingin menghapus data ini? (Y/N): ').upper()
                if konfirmasi == 'Y':
                    pasien_dihapus = data_pasien.pop(index)
                    print('\n============================================================')
                    print(f"\tData pasien '{pasien_dihapus['Nama']}' berhasil dihapus")
                    print('============================================================')
                else:
                    print('\nData tidak dihapus.')
            else:
                print('\nIndex tidak ditemukan.')

        elif hapusData == '2':
            break
        else:
            print('Pilihan tidak valid. Coba lagi.')



while True:
    menu = input('''\n
    ================================
           MENU UTAMA PROGRAM
    ================================
    1. Lihat Data Pasien
    2. Tambah Data Pasien
    3. Perbarui Data Pasien
    4. Hapus Data Pasien
    5. Keluar Program

    Masukkan pilihan Anda: ''')

    if menu == '1':
        baca_Data()
    elif menu == '2':
        tambah_Data()
    elif menu == '3':
        perbarui_Data()
    elif menu == '4':
        hapus_Data()
    elif menu == '5':
        print('\nTerima kasih! Program selesai.\n')
        break
    else:
        print('\nPilihan tidak valid, coba lagi.\n')
