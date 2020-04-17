from PTL import Image, ImageOps
from picamera import PiCamera
import RPi.GPIO as GPIO

class myCamera():
    def __init__(self):
        self.camera = PiCamera()

    #class method takes an image
    def takeImage(self):
        self.camera.capture("originalPic.jpg")

    #class method grayscales and compresses the image, call with originalPic.jpg
    def modifyImage(self, imageName):
        #grayscales image
        newPic = Image.open(imageName).convert("L")
        #compresses image
        newPic.resize((28,28))
        newPic.save("modifiedImage.jpg")


# #function takes an image and turns it to grayscale
# def grayscaleImage(imageName):
#     grayscaledPic = Image.open(imageName).convert("L")
#     grayscaledPic.save("grayscaledPic.jpg")

# #funciton takes in an image and compresses it to be 28x28 pixels
# def compressImage(imageName):
#     pic = Image.open(imageName)
#     pic = pic.resize((28,28))
#     pic.save("compressedPic.jpg")

# def main():
#     #setup button and camera
#     GPIO.setmode(BCM)
#     buttonPin = 20
#     GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#     camera = PiCamera()
#     #run forever until button is pushed, then take an image, grayscale it, and compress it
#     while True:
#         if GPIO.input(buttonPin):
#             camera.capture("mainPic.jpg")
#             grayscaleImage("mainPic.jpg")
#             compressImage("grayscaledPic.jpg")
#         break
#     print("Picture taken, grayscaled, and compressed!")
