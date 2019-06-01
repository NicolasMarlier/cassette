from pygame import mixer
from camera import take_picture
from qrcode import inteprete_picture
from mouse_v2 import listen
import mutagen.mp3
import json
import os

currentMusicPlaying = None

def initialize_music():
    mixer.init()
    playSound(fullFilename("effects/ready.mp3"))

def fullFilename(filename):
     dirname = os.path.dirname(__file__)
     return os.path.join(dirname, filename)

def getMusicFromPicture(token):
    if token == None:
        return None
    print("music", token)
    if token == b'8fad1fc5-203c-4027-916b-07f670d6114a':
        return fullFilename("music/johnny_b_goode.mp3")
    elif token == b'68d26688-907d-4dcb-88c4-47b432fa7e5a':
        return fullFilename("music/hit_the_road_jack.mp3")
    else:
        return None

def playSound(filename):
    mp3 = mutagen.mp3.MP3(filename)
    mixer.init(frequency=mp3.info.sample_rate)
    mixer.music.load(filename)
    mixer.music.play()

def getCurrentMusic():
    picture = take_picture()
    data = inteprete_picture(picture)
    getMusicFromPicture(data)

def stopMusic():
    mixer.music.fadeout(1000)
    currentMusicPlaying = None

def onClick():
    music = getCurrentMusic()
    if(currentMusicPlaying == None):
        if(music == None):
            playSound("effects/unrecognized.mp3")
        else:
            currentMusicPlaying = music
            playSound(music)
    else:
        if(music == None):
            stopMusic()
        else:
            currentMusicPlaying = music
            playSound(music)

print("Cassette initialized. Please insert a cassette.")

initialize_music()
listen(onClick=onClick)
