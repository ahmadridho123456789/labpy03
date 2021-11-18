#Program Menentukan Bilangan Terbersar

#Input Bilangan
num1 = input("Masukan angka ke-1: ")
num2 = input("Masukan angka ke-2: ")

#Proses dan Output
if num1 > num2:
    print(num1, "Adalah Bilangan Terbesar")
elif num2 > num1:
    print(num2, "Adalah Bilangan Terbesar")
else:
    print("Diluar dari pernyataan IF")
