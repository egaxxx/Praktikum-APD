#input
Nama = str(input('Masukkan Nama Barang = '))
Harga = float(input('Masukkan Harga Barang = Rp. '))
Jumlah_Barang = int(input('Masukkan Jumlah Barang = '))
Diskon = float(input('Masukkan Diskon (2 Digit Belakang NIM) = '))

#pra-proses
Diskon_Persen = Diskon /100

#proses
Harga_Sebelum_Diskon = Jumlah_Barang * Harga
Total_Diskon = Diskon_Persen * Harga_Sebelum_Diskon
Harga_Setelah_Diskon = Harga_Sebelum_Diskon - Total_Diskon
Sisa = Diskon%3

#output
print ('Anda membeli',Jumlah_Barang,Nama,'dengan harga satuan Rp.',Harga,', total sebelum diskon adalah Rp.',Harga_Sebelum_Diskon,', total diskon adalah Rp.',Total_Diskon,'dan total yang harus dibayar adalah Rp.', Harga_Setelah_Diskon)
print (Diskon, 'dibagi dengan 3 sisanya',Sisa)
