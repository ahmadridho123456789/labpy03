print("membuat program sederhana dengan tiga buah input bilangan")
a =int(input("masukan bilangan pertama :"))
b =int(input("masukan bilangan kedua: "))
c =int(input("masukan bilangan ketiga: "))

if a > b and a > c:
    print(a,"bilangan terbesar dari tiga buah input bilangan")
if b > a and b > c:
    print(b,"bilangan terbesar dari tiga buah input bilangan")
else:
    print(c,"bilangan terbesar dari tiga buah input bilangan")
