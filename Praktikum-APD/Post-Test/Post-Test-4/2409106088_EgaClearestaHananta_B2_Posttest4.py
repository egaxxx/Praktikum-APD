<<<<<<< HEAD
kesempatan = 3
print("Masukkan username dan password anda dengan benar")
print("Anda hanya memiliki 3 kesempatan login")
nama = input ("Masukkan nama anda :" )
pw = int(input("Masukkan password anda,NIM 3 digit terakhir :" ))

while kesempatan > 0:
    if nama == "ega" and pw == 88:
        break
    else:
        kesempatan -=1
        print(f"kesempatan anda sisa {kesempatan} kali lagi")

        if kesempatan > 0:
            username = input("Masukkan username anda :" )
            password = input("Masukkan password anda, NIM 3 digit terakhir :" )

if kesempatan == 0 :
    print("Anda gagal login")
else:


    while True :
        #input
        berat = (float(input("Masukkan berat badan anda dalam satuan miligram :")))
        tinggi = (float(input("Masukkan tinggi badan anda dalam satuan kilometer :")))

        #proses
        tinggim = tinggi * 1000
        tinggicm = tinggim * 100
        beratkg = berat *0.000001
        beratideal = beratkg / (tinggim * tinggim)

        #output
        if beratideal < 18.5 :
            print (beratideal)
            print ("Tinggi Badan = ",tinggicm," cm")
            print ("Berat Badan = ",beratkg," kg")
            print ("Anda kekurangan berat badan")
        elif beratideal < 24.9 :
            print (beratideal)
            print ("Tinggi Badan = ",tinggicm," cm")
            print ("Berat Badan = ",beratkg," kg")
            print("Berat badan anda normal")
        elif beratideal < 29.9 :
            print (beratideal)
            print ("Tinggi Badan = ",tinggicm," cm")
            print ("Berat Badan = ",beratkg," kg")
            print("Berat badan anda berlebih (Overwight)")
        else:
            print (beratideal)
            print ("Tinggi Badan = ",tinggicm," cm")
            print ("Berat Badan = ",beratkg," kg")
            print("Anda terkena penyakit obesitas")

        pilihan = input("Apakah anda ingin mengulang lagi? (ya/tidak) :")
        if pilihan != "ya":
            print ("program selesai")
=======
kesempatan = 3
print("Masukkan username dan password anda dengan benar")
print("Anda hanya memiliki 3 kesempatan login")
nama = input ("Masukkan nama anda :" )
pw = int(input("Masukkan password anda,NIM 3 digit terakhir :" ))

while kesempatan > 0:
    if nama == "ega" and pw == 88:
        break
    else:
        kesempatan -=1
        print(f"kesempatan anda sisa {kesempatan} kali lagi")

        if kesempatan > 0:
            username = input("Masukkan username anda :" )
            password = input("Masukkan password anda, NIM 3 digit terakhir :" )

if kesempatan == 0 :
    print("Anda gagal login")
else:


    while True :
        #input
        berat = (float(input("Masukkan berat badan anda dalam satuan miligram :")))
        tinggi = (float(input("Masukkan tinggi badan anda dalam satuan kilometer :")))

        #proses
        tinggim = tinggi * 1000
        tinggicm = tinggim * 100
        beratkg = berat *0.000001
        beratideal = beratkg / (tinggim * tinggim)

        #output
        if beratideal < 18.5 :
            print (beratideal)
            print ("Tinggi Badan = ",tinggicm," cm")
            print ("Berat Badan = ",beratkg," kg")
            print ("Anda kekurangan berat badan")
        elif beratideal < 24.9 :
            print (beratideal)
            print ("Tinggi Badan = ",tinggicm," cm")
            print ("Berat Badan = ",beratkg," kg")
            print("Berat badan anda normal")
        elif beratideal < 29.9 :
            print (beratideal)
            print ("Tinggi Badan = ",tinggicm," cm")
            print ("Berat Badan = ",beratkg," kg")
            print("Berat badan anda berlebih (Overwight)")
        else:
            print (beratideal)
            print ("Tinggi Badan = ",tinggicm," cm")
            print ("Berat Badan = ",beratkg," kg")
            print("Anda terkena penyakit obesitas")

        pilihan = input("Apakah anda ingin mengulang lagi? (ya/tidak) :")
        if pilihan != "ya":
            print ("program selesai")
>>>>>>> 49226045668a316d892c04a5758fd98db44f7be7
            break