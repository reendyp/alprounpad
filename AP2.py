#operasi aritmetika

m = 82.0
n = 26.0
print("%.f + %.f = %.f" % (m, n, m+n))
print("%.2f - %.2f = %.4f" % (m, n, m-n))
print("%f x %f = %f" % (m, n, m*n))
print("%f/%f = %f" % (m, n, m/n))
print("%f/%f = %f (dibulatkan kebawah)" % (m, n, m//n))
print("%f/%f (sisa hasil bagi) %f" % (m, n, m%n))
print("(-) %f = %f" % (m,-m))
print("%f^2 =%f" % (m,m**2))

#operator pembanding
m = 5.0
n = 7.0
print("m = n :" + str(m==n))
print("m !== n : " +str(m!=n))
print("m > n : "+ str(m>n))
print("m < n : "+ str(m<n))
print("m >= n : " +str(m>=n))
print("m<=n : "+str(m<=n))

# str berfungsi untuk memberikan penekanan bahwa tipe data didalamnya adalah string atau karakter
#operator bitwise
m = 10
n = 5
print("m and n : "+ str(m&n))
print("m or n : "+ str(m|n))
print("m XOR n : "+ str(m^n))
print(" ~ n : " + str(~n))

#operator logika
l = 80
m = 90
n = 0

print(" (m >= 1) and (m <= n) : " + str((m>=1) and (m<=n)))
print(" (m >= 1) or (m <= n) : " + str((m>=1) or (m<=n)))
print("not ((m>=1) and (m<=n)) : " + str(not((m>=1) and (m<=n))))

#statement I/O
'''
tanyaTinggi = "Tinggi Anda?"
print("Nama Anda?")
nama = input()
umur = input("Umur Anda?")
tinggi = input(tanyaTinggi)
print("Berat Anda?")
berat = input()

print("Nama Anda adalah %s dan Anda berumur %s serta memiliki tinggi %s dan berat %s." % (nama, umur, tinggi, berat))
#fungsi print untuk memberikan perintah untuk sistem menampilkan output
#fungsi input untuk memberikan program masukkan dari user
'''
#tugas akhir modul AP-2
'''
1. Buatlah program untuk menghitung luas bangunan geometri trapesium. Ukuran dimensi bangunan didapat dari peranti masukan dan luas bangun ditampilkan sebagai keluaran. Berikan penjelasan!
2. Buatlah program untuk menghitung pajak penghasilan (10%), inputkan nama, alamat, instansi gaji perbulan dan hitung pajak pertahun
'''
#1 menghitung luas trapesium
'''
a = int(input("Masukkan panjang atas : "))
b = int(input("Masukkan panjang bawah :"))
t = int(input("Masukkan tinggi :")) 

l = (a+b)*t/2
print("Luas trapesium :",l)
'''
#2 menghitung pajak penghasilan

n = input("Nama : ")
add = str(input('Alamat :'))
paid = str(input("Gaji perbulan : "))

pajak = 0.1*int(paid)
print("Halo %s , pajak pertahun anda sebesar %s" % (n, pajak))
