from pygame import mixer
from camera import take_picture
from qrcode import inteprete_picture
from mouse import listen
import mutagen.mp3
import json
import os

def initialize_music():
    mixer.init()

def fullFilename(filename):
     dirname = os.path.dirname(__file__)
     return os.path.join(dirname, filename)

def play_music(token):
    if token == None:
        playSound(fullFilename("effects/unrecognized.mp3"))
        print("No music to play")
        return
    print("playing music", token)
    if token == b'8fad1fc5-203c-4027-916b-07f670d6114a':
        playSound(fullFilename("music/johnny_b_goode.mp3"))
    elif token == b'68d26688-907d-4dcb-88c4-47b432fa7e5a':
        playSound(fullFilename("music/hit_the_road_jack.mp3"))
    else:
        print("Unrecognized music")
        playSound(fullFilename("effects/unrecognized.mp3"))
        return

def playSound(filename):
    mp3 = mutagen.mp3.MP3(filename)
    mixer.init(frequency=mp3.info.sample_rate)
    mixer.music.load(filename)
    mixer.music.play()

def activation():
    picture = take_picture()
    data = inteprete_picture(picture)
    play_music(data)

def stopMusic():
    mixer.music.fadeout(1000)

def onClick(pressed):
    if(pressed):
        playSound(fullFilename("effects/clicked.mp3"))
        activation()
    else:
        stopMusic()

print("Cassette initialized. Please insert a cassette.")

initialize_music()
listen(onClick=onClick)
