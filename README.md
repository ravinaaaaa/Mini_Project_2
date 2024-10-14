# Mini_Project_2
Ravina Eka Adiya 2409116078 Sistem Informasi B

## mengimpor kelas Prettytable dari modul prettytable. digunakan untuk membuat tabel yang terformat dengan baik saat menampilkan data
from prettytable import PrettyTable

## untuk mendefinisikan fungsi login
def login():
## untuk mengambil input dari pengguna untuk username dan disimpan di variabel "user"
    user = input("Masukan Username: ")
## untuk mengambil input dari pengguna untuk password dan disimpan di variabel "pw"    
    pw = input("Masukan Password: ")
## untuk memeriksa apakah username dan password yang dimasukan cocok dengan data admin yang telah dibuat
    if user == "admin" and pw == "admin012" :
        return "admin"
## untuk memeriksa apakah username dan password yang dimasukan cocok dengan data pelanggan yang telah dibuat
    elif user == "pelanggan" and pw == "pelanggan123" :
## jika tidak ada yang cocok maka akan mencetak pesan bahwa username dan password yang dimasukan salah
        return "pelanggan"
    else:
        print("Username atau Password salah!")
        return None

## mendefinisikan tabel layanan
def tabel_layanan():
## membuat objek Prettytable dengan tiga kolom (id, jenis treatment, harga)
    table = PrettyTable(['ID', 'Jenis Treatment','Harga'])
## loop melalui layanan : untuk melakukan iterasi melalui list layanan untuk menambahkan setiap layanan ke tabel
    for service in layanan:
## untuk menambahkan baris baru yang berisi ID, nama dan harga dari layanan saat ini.
        table.add_row([service['id'], service['name'], service['price']])
## menampilkan tabel layanan di konsol
    print(table)

## memulai list yang akan mennyimpan informasi layanan
layanan = [
## menambahkan layanan sebagai dictionary dengan ID, nama, dan harga
    {'id': 1, 'name': 'Potong Rambut', 'price': 50000},
    {'id': 2, 'name': 'Potong Cuci Rambut', 'price': 80000},
    {'id': 3, 'name': 'Cuci Catok', 'price': 75000},
    {'id': 4, 'name': 'Cuci Blow', 'price': 95000},
    {'id': 5, 'name': 'Smoothing', 'price': 150000},
    {'id': 6, 'name': 'Hair Colouring', 'price': 250000},
    {'id': 7, 'name': 'Hair Spa', 'price': 150000},
    {'id': 8, 'name': 'Creambath', 'price': 200000},
]

## mendefinisikan list kosong untuk menyimpan data reservasi yang akan dibuat
reservasi = []

## mendefinisikan tabel reservasi
def tabel_reservasi():
## membuat objek PrettyTable dengan kolom yang sesuai untuk informasi reservasi
    table = PrettyTable(['ID', 'Nama', 'Tanggal', 'Jumlah Orang', 'Jenis Treatment', 'Total Harga'])
## mengatur variabell index untuk digunakan dalam penomoran ID reservasi
    index = 1
## melakukan iterasi melalui list reservasi untuk menambahkan setiap reservasi ke tabel
    for res in reservasi:
## untuk menambahkan baris baru dengan informasi dari reservasi saat ini, termasuk index yang mewakili ID
        table.add_row([index, res['name'], res['date'], res['jumlah_orang'], res['service_name'], res['total_price']])
## menambahkan nilai index untuk ID berikutnya
        index += 1
    print(table)

## mendefinisikan menu admin
def menu_admin():
## mengizinkan fungsi untuk mengakses dan memodifikasi list layanan yang didefinisikan secara global
    global layanan
## memulai loop yang akan terus berjalan hingga admin memilih untuk keluar
    while True:
## mencetak opsi yang dapat dipilih admin
        print("\nMenu Admin:")
        print("1. Tampilkan Layanan")
        print("2. Tambah Layanan")
        print("3. Edit Layanan")
        print("4. Hapus Layanan")
        print("5. Keluar")

## mengambil input dari admin untuk memilih salah satu opsi menu
        pilih = input("Pilih menu: ")
## jika admin pilih '1', maka akan memanggil fungsi tabel layanan untuk menunjukkan semua layanan
        if pilih == '1':
           tabel_layanan()
## jika admin memilih '2' untuk menambah layanan
        elif pilih == '2':
## meminta admin untuk memasukan nama jenis treatment baru
            name = input("Jenis Treatment : ")
## meminta admin untuk memasukan harga treatment baru
            price = int(input("Harga Treatment : "))
## menghitung ID untuk layanan baru berdasarkan panjang list layanan
            id_baru = len(layanan) + 1
## menambah dictionary baru ke list layanan dengan ID, nama, hrga yang baru saja dimasukan
            layanan.append({'id' : id_baru, 'name': name, 'price': price})
## mencetak layanan berhasil ditambah
            print("Layanan berhasil ditambah!!!")
## menampilkan tabel layanan
            tabel_layanan()

## jika admin memilih untuk mengedit layanan
        elif pilih == '3':
## menminta admin untuk memilih id yang ingin di edit
            id_layanan = int(input("Pilih ID layanan yang ingin di edit : "))
## untuk mengiterasi setiap elemen 's' dalam 'layanan'
            service = next((s for s in layanan if s['id'] == id_layanan), None)
## jika service tidak none
            if service:
## meminta pengguna untuk memasukan nama baru untuk jenis treatment
                name = input("Nama jenis treatment baru : ")
## meminta pengguna untuk memasukan harga baru untuk jenis treatment
                price = int(input("Harga treatment baru : "))
## memperbarui nama service dengan nama baru yang dimasukan pengguna
                service['name'] = name
## memperbarui harga service dengan harga baru yang dimasukan pengguna
                service['price'] = price
## mencetak jenis treatment berhasil di ubah
                print("Jenis Treatment berhasil diubah!!!")
## menampilkan tabel layanan
                tabel_layanan()
## jika service adalah None maka pesan eror akan ditampilkan
            else:
                print("Maaf, Jenis Treatment tidak ditemukan :(")

## jika admin memilih '4' untuk menghapus layanan
        elif pilih == '4':
## meminta pengguna untuk memasukan ID layanan yang ingin dihapus
            id_layanan = int(input("Pilih ID layanan yang ingin dihapus : "))
## menghapus service dari daftar layanan yang memiliki id sama dengan id_layanan
            layanan = [s for s in layanan if s['id'] != id_layanan]
## menampilkan pesan bahwa jenis treatment berhasil dihapus
            print("Jenis Treatment berhasil dihapus!!!")
## menampilkan tabel layanan
            tabel_layanan()

## jika admin pilih '5' maka admin keluar dari program
        elif pilih == '5':    
## menampilkan pesan terima kasih kepada pengguna
            print("Terima kasih Love <33333")
## menghentikan loop yang sedang berjalan
            break
## jika input pengguna tidak cocok dengan pilihan yang valid, maka akan ditampilakn pesan kesalahan
        else:
            print("Pilihan tidak valid!")

## mendefinisikan fungsi menu pelanggan
def menu_pelanggan():
## memulai loop yang akan terus berjalan hingga pelanggan memilih untuk keluar
    while True:
## mencetak opsi yang dapat dipilih pelanggan
        print("\nMenu Pembeli:")
        print("1. Lihat Layanan")
        print("2. Lihat Reservasi")
        print("3. Buat Reservasi")
        print("4. Keluar")
## mengambil input dari pelanggan untuk memilih salah satu opsi
        pilih = input("Pilih menu: ")
## jika pelanggan pilih '1' untuk melihat layanan
        if pilih == '1':
## memanggil fungsi tabel layanan
            tabel_layanan()
## jika pelanggan pilih '2' untuk melihat reservasi 
        elif pilih == '2':
## memanggil fungsi tabel reservasi
            tabel_reservasi()
## jika pelanggan pilih '3' untuk membuat reservasi
        elif pilih == '3':
## memanggil fungsi tabel layanan
            tabel_layanan()
## meminta pelanggan memasukan nama mereka
            nama = input("Masukkan nama Anda: ")
## meminta pelanggan memasukan tanggal reservasi
            tanggal = input("Masukkan tanggal reservasi (DD/MM/YYYY): ")
## meminta pelanggan memasukan jumlah orang untuk reservasi
            jumlah_orang = input("Masukkan jumlah orang: ")
## meminta pelanggan memasukan ID layanan yang ingin dipesan, dipisahkan dengan koma
            service_ids = input("Masukkan ID layanan yang ingin dipesan (pisahkan dengan koma): ")

## memecah string service_ids menjadi list, menghapus spasi, dan mengonversinya ke integer
            service_ids = [int(id.strip()) for id in service_ids.split(',')]
## membuat list kosong untuk menyimpan layanan yang dipesan
            reservasi_treatment = []
## mengatur variabel total_harga untuk menghitung total harga layanan yang di pesan
            total_harga = 0

## melakukan iterasi melalui setiap ID layanan yang dimasukan
            for service_id in service_ids:
## untuk mencari layanan berdasarkan ID yang dimasukan. jika tidak ditemukan, akan menghasilkan None
                service = next((s for s in layanan if s['id'] == service_id), None)
## jika layanan ada dalam list
                if service:
## menambahkan layanan yang ditemukan ke list reservasi_treatment
                    reservasi_treatment.append(service)
## menambahkan harga layanan ke total harga
                    total_harga += service['price']
## jika ID layanan tidak ditemukan, maka akan mencetak pesan kesalahan
                else:
                    print(f"ID layanan {service_id} tidak valid!")
## memeriksa apakah ada layanan yang berhasil dipesan
            if reservasi_treatment:
## menambahkan dictionary baru ke list reservasi
                reservasi.append({
## mengisi informasi reservasi, termasuk nama, tanggal, jumlah orang, nama layanan, dan total harga
                    'name': nama,
                    'date': tanggal,
                    'jumlah_orang': jumlah_orang,
                    'service_name': ', '.join(service['name'] for service in reservasi_treatment),  # Gabungkan nama layanan
                    'total_price': total_harga
                })
## mencetak pesan bahwa reservasi berhasil dan menunjukan layanan yang dipesan
                print(f"Reservasi berhasil untuk layanan: {', '.join(service['name'] for service in reservasi_treatment)}.")
## mencetak nama dan tanggal reservasi
                print(f"Atas nama: '{nama}', pada tanggal: '{tanggal}'.")
## mencetak total harga layanan yang berhasil di pesan
                print(f"Total harga: {total_harga}.")
## memanggil fungsi tabel_reservasi untuk menunjukan daftar reservasi yang telat dibuat
                tabel_reservasi()
## mencetak pesan jika tidak ada layanan yang berhasil dipesan
            else:
                print("Tidak ada layanan yang berhasil dipesan.")

## jika pelanggan memilih keluar
        elif pilih == '4':
## meminta pelanggan untuk memili apakah ingin melakukan reservasi lagi atau tidak
            lanjut = input("Apakah Anda ingin melakukan reservasi lagi? (ya/tidak): ")
            if lanjut.lower() != 'ya':
## jika tidak ingin login lagi, maka mencetak pesan terimakasih kepada pelanggan
                print("Terima kasih Love <33333")
## menghentikan loop dan keluar dari menu pelanggan
                break
## jika input tidak cocok dengan pilihan yang ada, maka akan menampilkan pesan kesalahan
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

## mengecek apakah file ini dijalankan sebagai program utama
if __name__ == "__main__":
## memulai loop yang akan terus berjalan hingga pengguna memilih untuk keluar 
    while True:
  ## memanggil fungsi login() untuk mendapatkan peran pengguna (admin atau pelanggan)
        role = login()
  ## jika role admin
        if role == "admin":
  ## maka akan memanggil fungsi menu_admin untuk menampilkan menu admin
            menu_admin()
  ## jika role pelanggan
        elif role == "pelanggan":
  ## maka akan memanggil fungsi menu_pelanggan untuk menampilkan menu pelanggan
            menu_pelanggan()
  ## jika tidak dari keduanya maka akan menampilkan pesan login gagal
        else:
            print("Gagal login!")
  ## meminta pelanggan untuk memilih apakah ingin login lagi atau tidak
        lanjut = input("Apakah Anda ingin login lagi? (ya/tidak): ")
  ## jika tidak ingin login lagi, maka akan menampilkan pesan terima kasih kepada pelanggan
        if lanjut.lower() != 'ya':
            print("Terima kasih! Sampai jumpa lagi!")
            break
