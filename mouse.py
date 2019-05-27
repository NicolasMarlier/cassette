# https://stackoverflow.com/questions/15882665/how-to-read-out-scroll-wheel-info-from-dev-input-mice
import struct

def getMouseEvent(onClick, bLeftDown):
  buf = file.read(3)
  button = ord( buf[0] )
  bLeft = button & 0x1
  if(bLeft != bLeftDown):
      onClick(bLeft)
  else:
      onClick(bLeft)
 return bLeft


def listen(onClick):
  file = open( "/dev/input/mice", "rb" )
  bLeftDown = false
  while True:
    bLeftDown = getMouseEvent(onClick, bLeftDown)
  file.close()
