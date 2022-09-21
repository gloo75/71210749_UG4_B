import json

with open('karyawan.json','r') as datafile:
    data = json.load(datafile)

x = int(input("Masukkan jumlah karyawan : "))

list_hobi = []
nama = []


for i in range(x):
    a = input("Masukkan nama : ")
    nama.append(a)
    b = int(input("Masukkan alamat : "))
    c = int(input("Masukan jumlah kolega"))
    d = int(input("Masukan nama kolega ke- : "))
    for j in range (1,b+1):
        c = input("Masukkan hobi ke-{}: ".format(j))
        list_hobi.append(c)
    print('=== Data berhasil ditambahkan ===')


nama = {}
nama['Audy'] = list
nama['Banu'] = d


data = [nama]

with open('karyawan.json','a+') as datafile:
    json.dump(data, datafile)
