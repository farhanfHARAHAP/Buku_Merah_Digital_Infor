
from Functions import *


while True:
    try:
        print('='*5)
        filename = str(input('Nama file yang ingin dibuka: '))
        clear()
        file = open(f'{filename}.txt','r')
    except:
        clear()
        print('\n Incorrect Filename!')
        wait(2)
        clear()
    else:
        clear()
        print(f'\n File {filename}.txt ditemukan!')
        wait(2)
        clear()
        break

# Proccess Data
baca = file.read()
baca = baca.split('\n')
listNama = []
listKota = []
listTanggal = []

for i in range(len(baca)-1):
    cache = baca[i]
    cache = cache.split('#')
    listNama.append(cache[0])
    listKota.append(cache[1])
    listTanggal.append(cache[2])
file.close()

# Show Data
opsi = str(input('Data diproses! Ingin melihat(y) atau skip(n)?\n>> '))
if opsi == 'y':
    clear()
    class my_dictionary(dict):
    
        def __init__(self):
            self = dict()
    
        def add(self, key, value):
            self[key] = value
            
    data = my_dictionary()
    data.add('Nama',listNama)
    data.add('Kota',listKota)
    data.add('Tanggal',listTanggal)
    
    from pandas import DataFrame
    
    hasil = DataFrame(data)
    print(f'\nExported from {filename}.txt\n',hasil)
    input('\nPRESS ENTER untuk melanjutkan!')
    

    


    
    