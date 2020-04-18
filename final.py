rom PIL import Image, ImageOps
from picamera import PiCamera
import RPi.GPIO as GPIO

class myCamera():
        def __init__(self):
                self.camera = PiCamera()

        #method takes a still image
        def takeImage(self):
                self.camera.capture("originalPic.jpg")

        #method gray scales and compresses the image
        def modifyImage(self, imageName):
                newPic = Image.open(imageName).convert("L")
                newPic = newPic.resize((28,28))
                newPic.save("modifiedImage.jpg")


def main():
        #setup button and camera
        GPIO.setmode(GPIO.BCM)
        buttonPin = 20
        GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        cam = myCamera()
        #run forever until button is pushed, then take an image and modify it
        while True:
                if GPIO.input(buttonPin) == 1:
                        cam.takeImage()
                        cam.modifyImage("originalPic.jpg")
                        break
 
main()

