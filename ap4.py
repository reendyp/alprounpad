'''
nilai = int(input("Masukkan nilai awal = "))
print ("Pengulangan while dimulai...")
while (nilai > 1):
    nilai = nilai / 2
    print (nilai)
print ("Pengulangan while selesai.")
awal=int(input('Set Nilai Awal = '))
akhir=int(input('Set Nilai Akhir = '))
count=0
summ=0
print ('Bilangan antara %d dan %d' % (awal,akhir))


for i in range(awal,akhir+1):
    print(i, end=' ')
    count=count+1
    summ=summ+i
print('Bilangan di atas ada %d bilangan' %count)
for i in range (2,3,1):
    print (i, end=' ')

'''

# Fibonnaci


'''  
print('Program Deret Fibonaci')
n = int(input('Masukkan jumlah bilangan yang ingin ditampilkan : '))
a = float(input('Masukkan bilangan pertama : '))
b = float(input('Masukkan bilangan kedua : '))

print(a, b, end = " ")
for i in range(n):
    x = a+b
    a = b 
    b = x
    print (x, end=" ")
    
print()

# Menghitung nilai faktorial

n = int(input('Masukkan nilai yang ingin difaktorialkan : '))
c = 1
for i in range(1, n+1):
    c = c*i
print(f'{n}! = %d ' % c)        
'''

# kombinasi

n = int(input('Masukkan nilai yang ingin dikombinasikan : '))
r = int(input('Masukkan nilai yang menjadi kombinator : '))
c = 1
b = 1
a = 1
z = n-r

for i in range(1, n+1):
    c = c*i
for i in range(1, r+1):
    b = b*i
for i in range(1, z+1):
    a=a*i
        
y = c/(b*a)
print(f'kombinasi dari %d dengan %d = %d ' % (n, r, y))
