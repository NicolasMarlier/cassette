import pyqrcode
import json

# 8fad1fc5-203c-4027-916b-07f670d6114a > johnny
# 68d26688-907d-4dcb-88c4-47b432fa7e5a > hit the road
# 24d26568-677d-4dcb-9rc4-89b4a8fa7e98 > la banana

qr = pyqrcode.create("24d26568-677d-4dcb-9rc4-89b4a8fa7e98")
qr.svg("la_banana.svg", scale=6)
