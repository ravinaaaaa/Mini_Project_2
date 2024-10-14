from prettytable import PrettyTable

def login():
    user = input("Masukan Username: ")
    pw = input("Masukan Password: ")

    if user == "admin" and pw == "admin012" :
        return "admin"
    elif user == "pelanggan" and pw == "pelanggan123" :
        return "pelanggan"
    else:
        print("Username atau Password salah!")
        return None
    
def tabel_layanan():
    table = PrettyTable(['ID', 'Jenis Treatment','Harga'])
    for service in layanan:
        table.add_row([service['id'], service['name'], service['price']])
    print(table)

layanan = [
    {'id': 1, 'name': 'Potong Rambut', 'price': 50000},
    {'id': 2, 'name': 'Potong Cuci Rambut', 'price': 80000},
    {'id': 3, 'name': 'Cuci Catok', 'price': 75000},
    {'id': 4, 'name': 'Cuci Blow', 'price': 95000},
    {'id': 5, 'name': 'Smoothing', 'price': 150000},
    {'id': 6, 'name': 'Hair Colouring', 'price': 250000},
    {'id': 7, 'name': 'Hair Spa', 'price': 150000},
    {'id': 8, 'name': 'Creambath', 'price': 200000},
]

reservasi = []
def tabel_reservasi():
    table = PrettyTable(['ID', 'Nama', 'Tanggal', 'Jumlah Orang', 'Jenis Treatment', 'Total Harga'])
    
    index = 1  # Mulai indeks dari 1
    for res in reservasi:
        table.add_row([index, res['name'], res['date'], res['jumlah_orang'], res['service_name'], res['total_price']])
        index += 1
    print(table)

def menu_admin():
    global layanan
    while True:
        print("\nMenu Admin:")
        print("1. Tampilkan Layanan")
        print("2. Tambah Layanan")
        print("3. Edit Layanan")
        print("4. Hapus Layanan")
        print("5. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == '1':
           tabel_layanan()
        elif pilih == '2':
            name = input("Jenis Treatment : ")
            price = int(input("Harga Treatment : "))
            id_baru = len(layanan) + 1
            layanan.append({'id' : id_baru, 'name': name, 'price': price})
            print("Layanan berhasil ditambah!!!")
            tabel_layanan()
        elif pilih == '3':
            id_layanan = int(input("Pilih ID layanan yang ingin di edit : "))
            service = next((s for s in layanan if s['id'] == id_layanan), None)
            if service:
                name = input("Nama jenis treatment baru : ")
                price = int(input("Harga treatment baru : "))
                service['name'] = name
                service['price'] = price
                print("Jenis Treatment berhasil diubah!!!")
                tabel_layanan()
            else:
                print("Maaf, Jenis Treatment tidak ditemukan :(")
        elif pilih == '4':
            id_layanan = int(input("Pilih ID layanan yang ingin dihapus : "))
            layanan = [s for s in layanan if s['id'] != id_layanan]
            print("Jenis Treatment berhasil dihapus!!!")
            tabel_layanan()
        elif pilih == '5':    
            print("Terima kasih Love <33333")
            break
        else:
            print("Pilihan tidak valid!")


def menu_pelanggan():
    while True:
        print("\nMenu Pembeli:")
        print("1. Lihat Layanan")
        print("2. Lihat Reservasi")
        print("3. Buat Reservasi")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == '1':
            tabel_layanan()
        elif pilih == '2':
            tabel_reservasi()
        elif pilih == '3':
            tabel_layanan()
            nama = input("Masukkan nama Anda: ")
            tanggal = input("Masukkan tanggal reservasi (DD/MM/YYYY): ")
            jumlah_orang = input("Masukkan jumlah orang: ")
            service_ids = input("Masukkan ID layanan yang ingin dipesan (pisahkan dengan koma): ")

            service_ids = [int(id.strip()) for id in service_ids.split(',')]
            reservasi_treatment = []
            total_harga = 0

            for service_id in service_ids:
                service = next((s for s in layanan if s['id'] == service_id), None)
                if service:
                    reservasi_treatment.append(service)
                    total_harga += service['price']
                else:
                    print(f"ID layanan {service_id} tidak valid!")
            
            if reservasi_treatment:
                reservasi.append({
                    'name': nama,
                    'date': tanggal,
                    'jumlah_orang': jumlah_orang,
                    'service_name': ', '.join(service['name'] for service in reservasi_treatment),  # Gabungkan nama layanan
                    'total_price': total_harga
                })
                print(f"Reservasi berhasil untuk layanan: {', '.join(service['name'] for service in reservasi_treatment)}.")
                print(f"Atas nama: '{nama}', pada tanggal: '{tanggal}'.")
                print(f"Total harga: {total_harga}.")

                tabel_reservasi()
            else:
                print("Tidak ada layanan yang berhasil dipesan.")
        elif pilih == '4':
            lanjut = input("Apakah Anda ingin melakukan reservasi lagi? (ya/tidak): ")
            if lanjut.lower() != 'ya':
                print("Terima kasih Love <33333")
                break
        else:
            print("Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    while True:
        role = login()
        if role == "admin":
            menu_admin()
        elif role == "pelanggan":
            menu_pelanggan()
        else:
            print("Gagal login!")
        lanjut = input("Apakah Anda ingin login lagi? (ya/tidak): ")
        if lanjut.lower() != 'ya':
            print("Terima kasih! Sampai jumpa lagi!")
            break