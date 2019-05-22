import cv2

def take_picture():
    camera = cv2.VideoCapture(0)
    camera.set(3, 1280)
    camera.set(4, 1024)
    camera.set(15, 0.5)
    returnValue, image = camera.read()
    cv2.imwrite('opencv.png', image)
    if returnValue:
        print("image ok")
        return image
    else:
        return None
