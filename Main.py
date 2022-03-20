
from Functions import *
from os import system


while True:
    clear()
    print('\nApa yang kamu ingin lakukan?\na. Buat Data\nb. Buka Data')
    opsi = str.lower(input('\n>> '))
    clear()
    
    if opsi == 'a' or opsi == 'b':
        break
    
if opsi == 'a':
    system('python FileCreate.py')
    
    
elif opsi == 'b':
    system('python FileOpen.py')
    
