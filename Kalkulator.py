numb1 = int(input("Masukan Angka-1 : "))
numb2 = int(input("Masukan Angka-2 : "))
print(""" 1. Pertambahan
 2. Pengurangan
 3. Perkalian
 4. Pembagian""")

n = int(input(" Masukan Pilihan : "))
if n == 1 :
    c = numb1 + numb2
    print(" Hasilnya : ",c)
elif n == 2 :
    c = numb1 - numb2
    print(" Hasilnya : ", c)
elif n == 3 :
    c = numb1 * numb2
    print(" Hasilnya : ", c)
elif n == 4 :
    c = numb1 / numb2
    print(" Hasilnya : ", c)
else :
    print("Eror ")