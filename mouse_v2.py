# https://stackoverflow.com/questions/15882665/how-to-read-out-scroll-wheel-info-from-dev-input-mice
from threading import Thread
import time


def listen(onClick, delayBeforeActionInSeconds=0.5):
  listenner = LastMouseActionListenner()
  listenner.start()
  while True:
    if listenner.lastMouseEventAt != None and listenner.lastMouseEventAt < time.time() - delayBeforeActionInSeconds:
      listenner.lastMouseEventAt = None
      time.sleep(0.2)
      onClick()
  listenner.join()

class LastMouseActionListenner(Thread):
    def __init__(self):
      Thread.__init__(self)
      self.lastMouseEventAt = None
      self.file = open( "/dev/input/mice", "rb")
    def run(self):
      while True:
        self.file.read(3)
        self.lastMouseEventAt = time.time()
        print(self.lastMouseEventAt)
      self.file.close()

listen()
