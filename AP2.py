#percobaan 1 : membandingkan

m = 5.0
n = 7.0
'''
if (m==n):
    print(str(m) +' sama dengan ' + str(n))
else:
    print(str(m) + " tidak sama dengan" + str(n))
'''
#percobaan 2
''' 
if(m==n):
    print(str(m) +' sama dengan ' + str(n))
elif(m != n):
    print (str(m) + " tidak sama dengan " + str(n))
elif(m > n):
    print (str(m) + " lebih besar " + str(n))
elif(m < n):
    print (str(m) + " lebih kecil " + str(n))
'''
'''
n = int(input('Masukkan nilai : '))
if(n <= 100):
    if(n>85):
        print('Huruf mutu anda adalah A')
    elif(n>75):
        print('Huruf mutu anda adalah B')
    elif(n>65):
        print('Huruf mutu anda adalah C')
    elif(n>55):
        print('Huruf mutu anda adalah D')
    elif(n<=55):
        print('Huruf mutu anda adalah E')
else: 
    print('Nilai diluar jangkauan')
'''


'''
# tugas akhir pengondisian 1
n  = int(input("Masukkan angka : "))
if(n%2 == 0 and n>=0):
    print("Angka %d adalah bilangan genap" % n)
else:
    a = n%2
    print('Angka %d adalah bilangan ganjil. Dengan sisa pembagian %d' % (n, a))
'''

jm = int(input('Jumlah mata kuliah : '))
sks = int(input('Total SKS : '))

matkul1 = float(input('Masukkan SKS Matkul 1 :'))
matkul2 = float(input('Masukkan SKS Matkul 2 :'))
matkul3 = float(input('Masukkan SKS Matkul 3 :'))

nm1 = float(input('Masukkan nilai Matkul 1 :'))
nm2 = float(input('Masukkan nilai Matkul 2 :'))
nm3 = float(input('Masukkan nilai Matkul 3 :'))

x = float(matkul1*nm1)
y = float(matkul2*nm2)
z = float(matkul3*nm3)

tot = float((x+y+z)/sks)

if(tot==4):
    print("IP Anda adalah %.2f dengan mutu A" % tot)
elif(2.5<tot<=3.5):
    print('IP Anda adalah %.2f dengan mutu B' % tot)
elif(1.5<tot<=2.5):
    print('IP Anda adalah %.2f dengan mutu C' % tot)
elif(1<tot<=1.5):
    print("IP Anda adalah %.2f dengan mutu D" % tot)
elif(tot<=1):
    print("IP Anda adalah %.2f dengan mutu E" % tot)
else:
    print("Mohon maaf IP Anda tidak terdefinisi")

#yang bener : permatkul
nm1 = int(input('Masukkan nilai matkul 1 : '))
sks = int(input('Masukkan jumlah SKS : '))


if (total1<=100) : 
    if (total1 > 85):
        HM1 = 'A'
        print("Matkul satu memiliki nilai %.2f dengan huruf mutu %s" % (total1, HM1))
