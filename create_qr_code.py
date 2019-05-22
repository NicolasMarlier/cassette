import pyqrcode
import json

# 8fad1fc5-203c-4027-916b-07f670d6114a > johnny
# 68d26688-907d-4dcb-88c4-47b432fa7e5a > hit the road

qr = pyqrcode.create("68d26688-907d-4dcb-88c4-47b432fa7e5a")
qr.svg("hit_the_road_jack.svg", scale=6)
