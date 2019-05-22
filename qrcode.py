import pyzbar.pyzbar as pyzbar
import cv2

def inteprete_picture(image2):
  image = cv2.imread('opencv.png')
  decodedObjects = pyzbar.decode(image)
  qrCodes = [ decodedObject for decodedObject in decodedObjects if decodedObject.type == 'QRCODE']
  print(decodedObjects)
  if len(qrCodes) > 0:
    return qrCodes[0].data
  else:
    return None
