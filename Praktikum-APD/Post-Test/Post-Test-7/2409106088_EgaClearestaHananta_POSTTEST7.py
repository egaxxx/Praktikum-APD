users = {
    "admin": {"password": "88", "status": "admin"}
}
furniture = {
    1: {"nama_barang": "Meja Jati", "stok": 10, "harga": 3500000},
    2: {"nama_barang": "Meja Mahoni", "stok": 5, "harga": 2500000},
    3: {"nama_barang": "Kursi Jati", "stok": 2, "harga": 2500000},
    4: {"nama_barang": "Kursi Mahoni", "stok": 2, "harga": 1500000},
    5: {"nama_barang": "Divan Jati", "stok": 2, "harga": 5000000},
    6: {"nama_barang": "Divan Mahoni", "stok": 2, "harga": 4500000},
    7: {"nama_barang": "Lemari Jati", "stok": 2, "harga": 3500000},
    8: {"nama_barang": "Lemari Mahoni", "stok": 2, "harga": 2500000},
}
running = True

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in users and users[username]['password'] == password:
        print(f"Login berhasil! Selamat datang {username}.\n")
        return users[username]['status'], True
    else:
        print("Login gagal, username atau password salah.\n")
        return None, False

def tambah_barang(furniture):
    try:
        id_barang = int(input("Masukkan ID barang: "))
        if id_barang in furniture:
            print("Error: ID barang sudah ada.\n")
            return
        nama_barang = input("Masukkan nama barang: ")
        stok = int(input("Masukkan jumlah stok: "))
        harga = int(input("Masukkan harga barang: "))
        furniture[id_barang] = {'nama_barang': nama_barang, 'stok': stok, 'harga': harga}
        print("Barang berhasil ditambahkan!\n")
    except ValueError:
        print("Error: Masukkan data yang valid.\n")

def hitung_total_harga(diskon, total_harga):
    if diskon == 0:
        return total_harga
    else:
        return hitung_total_harga(diskon - 1, total_harga - (total_harga * 0.01))

def tampilkan_barang(furniture):
    print("\nDaftar Barang Toko Mebel:")
    print("ID\tNama Barang\tStok\tHarga")
    for id_barang, item in furniture.items():
        print(f"{id_barang}\t{item['nama_barang']}\t{item['stok']}\tRp {item['harga']:,}")
    print()

def beli_barang(furniture):
    try:
        id_barang = int(input("Masukkan ID barang yang ingin dibeli: "))
        jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))
        if id_barang in furniture:
            item = furniture[id_barang]
            if item['stok'] >= jumlah_beli:
                item['stok'] -= jumlah_beli
                total_harga = jumlah_beli * item['harga']
                total_harga_diskon = hitung_total_harga(5, total_harga)  # Diskon 5%
                print(f"Anda membeli {jumlah_beli} {item['nama_barang']} dengan total harga Rp {total_harga_diskon:,}. Stok tersisa: {item['stok']}\n")
            else:
                print(f"Stok tidak mencukupi. Stok tersedia: {item['stok']}\n")
        else:
            print("Barang tidak ditemukan.\n")
    except ValueError:
        print("Error: Masukkan data yang valid.\n")

while running:
    print("=== SISTEM MANAJEMEN TOKO MEBEL ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    milih = input("Pilih menu: ")

    if milih == "2":
        username = input("Masukkan username baru: ")
        password = input("Masukkan password: ")
        users[username] = {"password": password, "status": "user"}
        print(f"Pengguna {username} berhasil terdaftar sebagai pengguna biasa.\n")

    elif milih == '1':
        status, logged_in = login()
        
        if logged_in:
            if status == "admin":
                program_jalan = True
                while program_jalan:
                    print("=== MENU ADMIN ===")
                    print("1. Lihat Barang")
                    print("2. Tambah Barang")
                    print("3. Ubah Barang")
                    print("4. Hapus Barang")
                    print("5. Logout")
                    pilihan = input("Pilih menu: ")

                    if pilihan == '1':
                        tampilkan_barang(furniture)

                    elif pilihan == '2':
                        tambah_barang(furniture)

                    elif pilihan == '3':
                        try:
                            id_barang = int(input("Masukkan ID barang yang akan diubah: "))
                            if id_barang in furniture:
                                item = furniture[id_barang]
                                print(f"Barang ditemukan: {item['nama_barang']} - Stok: {item['stok']} - Harga: Rp {item['harga']:,}")
                                item['nama_barang'] = input("Masukkan nama barang baru: ")
                                item['stok'] = int(input("Masukkan stok baru: "))
                                item['harga'] = int(input("Masukkan harga baru: "))
                                print("Barang berhasil diupdate!\n")
                            else:
                                print("Barang tidak ditemukan.\n")
                        except ValueError:
                            print("Error: Masukkan data yang valid.\n")

                    elif pilihan == '4':
                        try:
                            id_barang = int(input("Masukkan ID barang yang ingin dihapus: "))
                            if id_barang in furniture:
                                del furniture[id_barang]
                                print("Barang berhasil dihapus!\n")
                            else:
                                print("Barang tidak ditemukan.\n")
                        except ValueError:
                            print("Error: Masukkan data yang valid.\n")

                    elif pilihan == '5':
                        print("Logout berhasil.\n")
                        program_jalan = False

                    else:
                        print("Pilihan tidak valid.\n")

            elif status == 'user':
                user_running = True
                while user_running:
                    print("=== MENU PENGGUNA ===")
                    print("1. Lihat Barang")
                    print("2. Beli Barang")
                    print("3. Logout")
                    user_milih = input("Pilih menu: ")

                    if user_milih == '1':
                        tampilkan_barang(furniture)

                    elif user_milih == '2':
                        beli_barang(furniture)

                    elif user_milih == '3':
                        print("Logout berhasil.\n")
                        user_running = False

                    else:
                        print("Pilihan tidak valid.\n")

    elif milih == '3':
        print("Terima kasih telah menggunakan sistem.\n")
        running = False

    else:
        print("Pilihan tidak valid.\n")