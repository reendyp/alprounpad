#Tugas 1

fibonaci = []
n = int(input('masukkan angka : '))
a = int(input( "Masukkan angka : "))
b = int(input("masukkan angka : "))

fibonaci.append(a)
fibonaci.append(b)
for i in range(n) :
    x = a + b
    a = b
    b = x
    fibonaci.append(x)
print(fibonaci)

A = [[2, 3], [9,1]]

k = 100

hasil = [[x * k for x in baris] for baris in A]
print(hasil)
