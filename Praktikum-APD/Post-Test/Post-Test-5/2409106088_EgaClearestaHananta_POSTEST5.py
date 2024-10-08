# Data Users [username, password, role]
users = [
    ['admin', 'admin123', 'admin'],  # Admin default
]

# Data Barang Toko Mebel [id_barang, nama_barang, stok, harga]
furniture = [
    [1, 'Meja Jati', 10, 3500000],
    [2, 'Meja Mahoni', 5, 2500000],
    [3, 'Kursi Jati', 2, 2500000],
    [4, 'Kursi Mahoni', 2, 1500000],
    [5, 'Divan Jati', 2, 5000000],
    [6, 'Divan Mahoni', 2, 4500000],
    [7, 'Lemari Jati', 2, 3500000],
    [8, 'Lemari Mahoni', 2, 2500000],
]

# Variabel loop program utama
running = True

# Program Utama
while running:
    print("=== SISTEM MANAJEMEN TOKO MEBEL ===")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    choice = input("Pilih menu: ")

    
    if choice == '2':
        username = input("Masukkan username baru: ")
        password = input("Masukkan password: ")
        users.append([username, password, 'user'])  
        print(f"Pengguna {username} berhasil terdaftar sebagai pengguna biasa.\n")
    
    
    elif choice == '1':
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        logged_in = False
        role = None
        for user in users:
            if user[0] == username and user[1] == password:
                logged_in = True
                role = user[2]
                print(f"Login berhasil! Selamat datang {username}.\n")
                break
        
        if not logged_in:
            print("Login gagal, username atau password salah.\n")
            continue

        
        if role == 'admin':
            admin_running = True
            while admin_running:
                print("=== MENU ADMIN ===")
                print("1. Lihat Barang")
                print("2. Tambah Barang")
                print("3. Ubah Barang")
                print("4. Hapus Barang")
                print("5. Logout")
                pilihan = input("Pilih menu: ")

                if pilihan == '1':
                    
                    print("\nDaftar Barang Toko Mebel:")
                    print("ID\tNama Barang\tStok\tHarga")
                    for item in furniture:
                        print(f"{item[0]}\t{item[1]}\t{item[2]}\tRp {item[3]:,}")
                    print()

                elif pilihan == '2':
                    
                    try:
                        id_barang = int(input("Masukkan ID barang: "))
                        nama_barang = input("Masukkan nama barang: ")
                        stok = int(input("Masukkan jumlah stok: "))
                        harga = int(input("Masukkan harga barang: "))
                        furniture.append([id_barang, nama_barang, stok, harga])
                        print("Barang berhasil ditambahkan!\n")
                    except ValueError:
                        print("Error: Masukkan data yang valid.\n")

                elif pilihan == '3':
                    
                    try:
                        id_barang = int(input("Masukkan ID barang yang ingin diubah: "))
                        penemuan = False
                        for item in furniture:
                            if item[0] == id_barang:
                                penemuan = True
                                print(f"Barang ditemukan: {item[1]} - Stok: {item[2]} - Harga: Rp {item[3]:,}")
                                item[1] = input("Masukkan nama barang baru: ")
                                item[2] = int(input("Masukkan stok baru: "))
                                item[3] = int(input("Masukkan harga baru: "))
                                print("Barang berhasil diupdate!\n")
                                break
                        if not penemuan:
                            print("Barang tidak ditemukan.\n")
                    except ValueError:
                        print("Error: Masukkan data yang valid.\n")

                elif pilihan == '4':
                    
                    try:
                        id_barang = int(input("Masukkan ID barang yang ingin dihapus: "))
                        penemuan = False
                        for item in furniture:
                            if item[0] == id_barang:
                                penemuan = True
                                furniture.remove(item)
                                print("Barang berhasil dihapus!\n")
                                break
                        if not penemuan:
                            print("Barang tidak ditemukan.\n")
                    except ValueError:
                        print("Error: Masukkan data yang valid.\n")

                elif pilihan == '5':
                    print("Logout berhasil.\n")
                    admin_running = False

                else:
                    print("Pilihan tidak valid.\n")

        
        elif role == 'user':
            user_running = True
            while user_running:
                print("=== MENU PENGGUNA ===")
                print("1. Lihat Barang")
                print("2. Beli Barang")
                print("3. Logout")
                user_choice = input("Pilih menu: ")

                if user_choice == '1':  
                    print("\nDaftar Barang Toko Mebel:")
                    print("ID\tNama Barang\tStok\tHarga")
                    for item in furniture:
                        print(f"{item[0]}\t{item[1]}\t{item[2]}\tRp {item[3]:,}")
                    print()

                elif user_choice == '2':  
                    try:
                        id_barang = int(input("Masukkan ID barang yang ingin dibeli: "))
                        jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))
                        barang_ditemukan = False
                        for item in furniture:
                            if item[0] == id_barang:
                                barang_ditemukan = True
                                if item[2] >= jumlah_beli:
                                    item[2] -= jumlah_beli  
                                    total_harga = jumlah_beli * item[3]
                                    print(f"Anda membeli {jumlah_beli} {item[1]} dengan total harga Rp {total_harga:,}. Stok tersisa: {item[2]}\n")
                                else:
                                    print(f"Stok tidak mencukupi. Stok tersedia: {item[2]}\n")
                                break
                        if not barang_ditemukan:
                            print("Barang tidak ditemukan.\n")
                    except ValueError:
                        print("Error: Masukkan data yang valid.\n")

                elif user_choice == '3':  
                    print("Logout berhasil.\n")
                    user_running = False

                else:
                    print("Pilihan tidak valid.\n")

    elif choice == '3':  
        print("Terima kasih telah menggunakan sistem.\n")
        running = False

    else:
        print("Pilihan tidak valid.\n")
