
from Functions import *

clear()

print()
print('='*20)
filename = str(input('\nCreate your filename: '))
clear()

file = open(f'{filename}.txt','w')

print('\n'+'='*20)
print(f'Now {filename}.txt is created!')

wait(2)

clear()

listNama = []
listTTL = []

def inputData():
    clear()
    print('EDITING MODE'+'='*5+'[x]')
    print('Ketik exit untuk keluar')
    nama = str.upper(input('\nNama: '))
    if nama == 'EXIT':
        return 0
    try:
        ttl = str(input('TTL (co: Jakarta 01-01-2003)\n>> '))
        ttl = ttl.split(' ')
        tempat = str.upper(ttl[0])
        tanggal = str(ttl[1])
        tgl = tanggal.split('-')
        if len(tgl[0]) == 2 and len(tgl[1]) == 2:
            listNama.append(nama)
            listTTL.append([tempat,tanggal])
            clear()
    except:
        clear()
        musik.play('wrong.mp3')
        print('\n INVALID INPUT! USE FORMAT!')
        wait(2)
        musik.stop()
        clear()
    else:
        clear()
        musik.play('right.mp3')
        print('\n SAVED...')
        wait(0.5)
        musik.stop()
        clear()
        pass
    
while True:
    register = inputData()
    if register == 0:
        break

for i in range(len(listNama)):
    file.write(listNama[i]+'#'+listTTL[i][0]+'#'+listTTL[i][1]+'\n')
    
clear()
print('\n SAVED...')
wait(0.5)
clear()

file.close()

