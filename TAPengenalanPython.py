#(1)
# Buatlah program Python untuk memasukkan tiga buah bilangan integer melalui keyboard. Kemudian program akan menampilkan penjumlahan rata-rata, product (perkalian ketiga bilangan tersebut).
#Amati tampilan keluaran yang dihasilkan serta ambil kesimpulan tentang output yang dihasilkan.

n = input("Masukkan tiga buah bilangan integer: ")
sum=0
for i in n:
    sum=sum+int(i)
print("Penjumlahan tiap digit : ", sum)

#rata-rata dari penjumlahan tiap digit
for i in n:
   mean = sum/len(n)
print("Rata-rata: ", mean)
result=1

#perkalian setiap digit
for i in n:
    result=result* int(i)
print("Perkalian: ", result)
