# https://stackoverflow.com/questions/15882665/how-to-read-out-scroll-wheel-info-from-dev-input-mice
import struct

def getMouseEvent(file, onClick, bLeftDown):
  buf = file.read(3)
  button = buf[0]
  bLeft = button & 0x1 == 1
  if(bLeft != bLeftDown):
      onClick(bLeft)
  return bLeft


def listen(onClick):
  file = open( "/dev/input/mice", "rb" )
  bLeftDown = False
  while True:
    bLeftDown = getMouseEvent(file=file, onClick=onClick, bLeftDown=bLeftDown)
  file.close()
