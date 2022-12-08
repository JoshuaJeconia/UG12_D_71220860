print('~~~~~ Table Matematika Nich ~~~~~')
print("Pilihan Model Matematika")
print(' 1. perkalian')
print(' 2. pembagian')
operasi = input('Masukan Model matematika yang diinginkan 1/2 : ')
if operasi == '1':
  print('perkalian')
  sum= int(input("Menampilkan table matematika dari angka: "))
for i in range (1, 11):
   (sum, "x", i, "=", sum*i)
if operasi == '2':
     print('pembagian')
sum= int(input("Menampilkan table matematika dari angka: "))
for i in range (1, 11):
    print(sum, "x", i, "=", sum//i)

