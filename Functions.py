from pygame import mixer

def clear():
    from os import system
    system('cls')
    
def wait(x):
    from time import sleep
    sleep(x)
    
class musik:
    
    mixer.init()
    def play(lokasi):
        mixer.music.load(lokasi)
        mixer.music.play()
        
    def stop():
        mixer.music.stop()