from PIL import ImageGrab, ImageOps, Image
import pyautogui, time
import numpy as np
import matplotlib.pyplot as plt

pyautogui.PAUSE = 0.001

class Cordinates():
    replayBtn = (640, 1030)
    dinosaur =  (406, 1028)

#228 = x coord to check for tree
#390 = y coord
#(228, 371)top box
#(319, 403)bottom box
#(180, 390)half dino height


def pressleft():
    pyautogui.press('left')
    print("left")

def pressright():
    pyautogui.press('right')
    print("right")

def pressd():
    pyautogui.press('d')

def pressa():
    pyautogui.press('a')
    print("a")

def imageGrab():
    box = (10, 52, 1000, 545)
    image = ImageGrab.grab(box)
    arr = np.array(image)
    imgplot = plt.imshow(image)
    star = np.where(np.all(arr == [250, 216, 73, 255], axis=-1))
    guy = np.where(np.all(arr == [218, 159, 62, 255], axis=-1))
    starcoords = list(zip(star[0], star[1]))[0]
    guycoords = list(zip(guy[0], guy[1]))
    arr.setflags(write=1)
    #for i in range(240, 260):
        #for k in range(200, 220):
            #arr[k,i] = [0,0,0,255]
            #print(arr[k,i])
    return starcoords
    #img = Image.fromarray(arr)
    #img.show()

#guyX = (imageGrab()[0][1])
#guyY = (imageGrab()[0][0])
starX = (imageGrab()[1])
starY = (imageGrab()[0])


def findguycoords():
    box = (10, 52, 1000, 545)
    image = ImageGrab.grab(box)
    arr = np.array(image)
    trylist = ([170, 119, 41, 255], [243, 183, 78, 255], [180, 127, 45, 255])
    guy = np.where(np.all(arr == trylist[0], axis=-1))
    try:
        guycoords = list(zip(guy[0], guy[1]))[0]
    except IndexError:
        try:
            guy = np.where(np.all(arr == trylist[1], axis=-1))
            guycoords = list(zip(guy[0], guy[1]))[0]
        except IndexError:
            guy = np.where(np.all(arr == trylist[2], axis=-1))
            guycoords = list(zip(guy[0], guy[1]))[0]
    return guycoords




def start():
    pyautogui.click(200, 200)
    guyX = (findguycoords()[1])
    guyY = (findguycoords()[0])
    starX = (imageGrab()[1])
    starY = (imageGrab()[0])
    print([starX, starY])
    try:
        while True:
            findguycoords()
            imageGrab()
            if starX - 10 < guyX < starX + 10 and guyY > starY:
                pressright()
                pressleft()
                pressright()
                pressleft()
                pressright()
                pressleft()
                pressright()
                pressleft()
                pressright()
                pressleft()
                pressright()
                pressleft()
                pressright()
            elif guyX > starX:
                pressleft()
                pressleft()
            elif guyX < starX:
                pressright()
                pressright()

            elif guyX < starX and guyY < starY:
                pressd()
            guyX = (findguycoords()[1])
            guyY = (findguycoords()[0])
            starX = (imageGrab()[1])
            starY = (imageGrab()[0])
            print(list([guyX, guyY]))
    except KeyboardInterrupt:
        pass
    except IndexError:
        findguycoords()
        start()
#imageGrab()
start()