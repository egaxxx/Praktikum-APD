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