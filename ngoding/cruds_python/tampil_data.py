isi=[]
data_input=0


#mengisi data
masuk_data = int(input("Masukkan jumlah data : "))
for i in range (masuk_data):
    tampung=input("Masukkan angka :".format(data_input))
    isi.append(tampung)
    n = len(isi)//2
    print([isi[:i] for i in range(0, n, 1)])

