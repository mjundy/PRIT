list_angka = []
input_angka = int(input("Masukkan jumlah data :"))
for i in range (input_angka) :
    angka = input("Masukkan angka yang mau diinput :")
    list_angka.append(angka)

a = len(list_angka)
x = len(list_angka)//2
if a % 2 == 0 :
    y = list_angka[:x]
else :
    y = list_angka[:x+1]
z = list_angka[-x:]
print (y,z)