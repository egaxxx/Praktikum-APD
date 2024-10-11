# daftar_buku = { 
# "Buku1" : "Harry Potter", 
# "Buku2" : "Percy Jackson", 
# "Buku3" : "Twillight" 
# } 
# print(daftar_buku["Buku1"]) 
# print(daftar_buku["Buku2"]) 
# print(daftar_buku["Buku3"])

# daftar_buku = {}

# daftar_buku["novel 1"] = "senyum pertama di pagi hari Airin"
# daftar_buku[1] = "matahari"
# print(daftar_buku)

# daftar_buku = dict(buku1 = "harry potter", buku2 = "percy jackson",)
# print(daftar_buku)

# Biodata = { 
# "Nama" : "Aldy Ramadhan Syahputra", 
# "NIM" : 2109106079, 
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"], "Mahasiswa_Aktif" :True, 
# "Social Media" : { 
# "Instagram" : "@aldyrmdhns_", 
# "Discord" : "\'Izanami#6848" 
# } 
# }
# print(Biodata)

# print(daftar_buku.get("buku2"))


# Nilai = { 
# "Matematika" : 80, 
# "B. Indonesia" : 90, 
# "B. Inggris" : 81, 
# "Kimia" : 78, 
# "Fisika" : 80 
# }

# for i in Nilai:
#     print(i)

# for i, j in Nilai.items():
#     print(f"nilai dari {i} itu valuenya adalah : {j}")


# nilai = { 
# "Matematika" : 80, 
# "B. Indonesia" : 90, 
# "B. Inggris" : 81, 
# "Kimia" : 78, 
# "Fisika" : 80 
# }

# # nilai["strukutur data"] = 99
# nilai.update({"struktur data" : 99})
# nilai.update({"Matematika" : 100})
# print(nilai)

# nilai = { 
# "Matematika" : 80, 
# "B. Indonesia" : 90, 
# "B. Inggris" : 81, 
# "Kimia" : 78, 
# "Fisika" : 80 
# }

# trashbin = nilai.pop("Matematika")

# print(nilai)
# print()
# print(trashbin)

# del nilai["Fisika"]
# print(nilai)

# nilai.clear()
# print(nilai)

# nilai = { 
# "Matematika" : 80, 
# "B. Indonesia" : 90, 
# "B. Inggris" : 81, 
# "Kimia" : 78, 
# "Fisika" : 80 
# }

# # print(f"jumlah elemen dari variabel di dict nilai adalah {len(nilai)}")

# daftar_nilai = nilai.copy()
# print(daftar_nilai)

# import os

# os.system("cls")
# key = "motor", "mobil", "sepeda" 
# value = 2 
# daftar_kendaraan = dict.fromkeys(key, value)

# print(daftar_kendaraan)

# Nilai = { 
# "Matematika" : 80, 
# "B. Indonesia" : 90, 
# "B. Inggris" : 81, 
# "Kimia" : 78, 
# "Fisika" : 80 
# } 

# for i in Nilai.keys(): 
# print(i) 

# print("")

# for i in Nilai.values(): 
# print(i)


# Musik = { 
# "The Chainsmoker" : ["All we Know", "The Paris"], 
# "Alan Walker" : ["Alone", "Lily"], 
# "Neffex" : ["Best of Me", "Memories"] 
# } 
# # Mengakses key dan value dari dictionary
# for i, j in Musik.items(): 
#     print(f"Musik milik {i} adalah : ") 
#     #mengambil nilai dari list
#     for song in j: 
#         print(song) 
#         print("")

# mahasiswa = { 
# 101 : {"Nama" : "Aldy", "Umur" : 19}, 
# 111 : {"Nama" : "Abdul", "Umur" : 18, "Hobi" : ["Membaca", "menulis", "ngoding"]} 
# } 
# for key, value in mahasiswa.items(): 
#     print("ID Mahasiswa : ", key) 
#     # for key_a, value_a in value.items(): 
#     #     print (key_a, " : ", value_a) 
#     #     print("")
# print (mahasiswa[111]["Hobi"][-1])