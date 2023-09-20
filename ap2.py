
''' 
# Percobaan 1: Operator aritmetika
# alpro201.py

m = 86.0
n = 26.0

print("%.f + %.f = %.f" % (m, n, m+n))
print("%.2f - %.2f = %.4f" % (m, n, m-n))
print("%f x %f = %f" % (m, n, m*n))
print("%f / %f = %f"% (m/n))
print("%f / %f = %f (dibulatkan ke bawah)" % (m, n, m//n))
print("%f / %f sisa hasil bagi %f " % (m, n, m%n))
print("(-)%f = %f" % (m,-m))
print("%f^2 = %f" % (m,m**2))

print ("%.f + %.f = %.f" % (m, n, m + n))
print ("%.2f - %.2f = %.4f" % (m, n, m - n))
print ("%f x %f = %f" % (m, n, m * n))
print ("%f / %f = %f" % (m, n, m / n))
print ("%f / %f = %f (dibulatkan ke bawah)" % (m, n, m // n))
print ("%f / %f sisa hasil bagi %f" % (m, n, m % n))
print ("(-)%f = %f" % (m, -m))
print ("%f^2 = %f" % (m, m**2))

1. operator penjumlahan pengurangan merupakan operasi perhitungan matematika pada umumnya. Sehingga dapat dipahami bahwa
sistem python memiliki logika yang berkesesuaian dengan matematika.
2. pembulatan dari python dinotasikan dengan perintah // sehingga hasil dari pembagian yang memiliki angka desimal akan dibulatkan kebawah
3. perbedaan %.f dengan %.2f adalah sebuah perintah untuk mendeklarasikan ada berapa angka dibelakang koma yang ingin dihasilkan
'''


# Percobaan 2: Operator pembanding
# alpro202.py
'''
m = 5.0 
n = 5.0

print("m = n :" + str(m==n))
print("m != n :" + str(m!=n))
print("m > n :" + str(m>n))
print("m < n :" + str(m<n))
print("m >= n :" + str(m>=n))
print("m <= n :" + str(m<=n))
'''
'''
1. ketika nilai m = n maka fungsi pada print("m = n :" + str(m==n)) akan memberikan output true sesuai dengan kaidah sama dengan pada matematika
dan pada fungsi lebih atau kecil dari sama dengan akan memberikan output berupa true karena nilai m dan n adalah lebih dari atau kurang dari sama dengan.
untuk fungsi yang tidak mendeklarasikan konsep sama dengan akan memberikan output berupa false

2. ketika m > n maka setiap fungsi yang memberikan deklarasi berupa m lebih besar dari n maka akan memberikan output berupa true. Hal tersebut berlaku pada fungsi lebih dari atau sama dengan dan kecil dari atau sama dengan.\
karena konsep atau adalah jika salah satu memenuhi maka pernyataan adalah benar

3. fungsi str() untuk memberikan deklarasi bahwa data yang ada berupa karakter atau string
'''
''' 
# percobaan 3 bitwise
m = 10
n = 4

print("m and n " + str(m & n))
print("m or n = "+ str(m|n))
print("m xor n = " + str(m ^ n))
print(" ~n = " +str(~n))
print(" geser ke kiri 2 bit = " + str(n<<2))
print(" geser ke kanan 1 bit = " + str(n>>1))
'''





''' 
percobaan 4 Operator logika 
l = 80
m = 90
n = 0 

print("(m>=1) and (m<=n) : "+str(m>=1) and (m<=n))
print("(m>=1) or (m<=n) : "+str(m>=1) or (m<=n))
print ("not((m >= l) and (m <= n)) : " + str(not((m >= l) and (m <= n))))
'''
'''
#percobaan 5 Statement I/O
x = "tinggi Anda?"
print("Nama Anda?")
nama = input()
umur = input("Umur anda?")
tinggi = input(x)
print("Berat Anda? ")
berat = input()

print("Nama Anda adalah %s dan Anda berumur %s serta memiliki tinggi %s dan berat %s." % (nama, umur, x, berat))

#TA 1

b = int(input("Masukkan besar alas :"))
a = int(input("Masukkan besar sisi atas : "))
t = int(input("Masukkan besar tinggi : "))

l = (a+b)*t/2

print(l)

TA 2

name = input("Masukkan nama : ")
address = str(input("Masukkan alamat : "))
gaji = int(input("Masukkan gaji perbulan : "))

pajak = 0.1*gaji

print("pajak pertahun Anda sebesar : " , pajak)
'''


''' 
m = 5.0
n = 7.0
if(m == n):
    print (str(m) + " sama dengan " + str(n))
else:
    print (str(m) + " tidak sama dengan " + str(n))

    dokumentasi ap 2 :
    https://docs.python.org/3/library/stdtypes.html
'''
