#import modules

import cv2 as cv
import numpy as np
import time
import threading
from playsound import playsound

'''
Defining function for alert
'''
def alert():
    threading.Thread(target=playsound, args=('Nokia.mp3',), daemon=True).start()

'''
Extracting Region of Interest (ROI) from image for comparison
'''
def extractROI(img):
    upper_left = (952, 584)
    bottom_right = (1100, 650)
    r = cv.rectangle(img, upper_left, bottom_right, (100, 50, 200), 1)
    ROI = img[upper_left[1]: bottom_right[1], upper_left[0]: bottom_right[0]]
    return cv.cvtColor(ROI,cv.COLOR_BGR2HSV)

def extractROI_encStart(img):
    upper_left = (100, 584)
    bottom_right = (300, 650)
    r = cv.rectangle(img, upper_left, bottom_right, (100, 50, 200), 1)
    ROI = img[upper_left[1]: bottom_right[1], upper_left[0]: bottom_right[0]]
    return cv.cvtColor(ROI,cv.COLOR_BGR2HSV)
#textbox
# img = cv.imread('ScreenshotBattle.png')
# upper_left = (952, 584)
# bottom_right = (1100, 650)
# # Rectangle marker indicates region of interest (ROI)
# r = cv.rectangle(img, upper_left, bottom_right, (100, 50, 200), 1)
# # ROI assignment
# ROI = img[upper_left[1]: bottom_right[1], upper_left[0]: bottom_right[0]]
# textBoxActual= cv.cvtColor(ROI,cv.COLOR_BGR2HSV)
textBoxActual = extractROI(cv.imread('ScreenshotBattle.png'))
print(textBoxActual.shape)
#white screen
whiteScreen = extractROI_encStart(cv.imread('ScreenshotBattle.png'))
#blackScreen
blackScreen = extractROI(cv.imread('blackScreen.png'))

'''
Code for stream
'''
stream = cv.VideoCapture(0)

#no stream detected
if not stream.isOpened():
    print("Cannot open stream. Check Hardware")
    exit()

#set stream resolution. 3 is width, 4 is height
stream.set(3,1280)
stream.set(4,720)

#region of interest in the shape of rectangle
#format is (x,-y) where top left is origin
#ie first number is x pixels from left to right. 2nd number is y pixels from the top
upper_left = (952, 584)
bottom_right = (1100, 650)
stateTextBox=False
start = time.time()
stateEncounter = False
encountersCounter = 0

textBoxCounter = 0
while True:
    # Capture frame-by-frame
    ret, frame = stream.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break


    # Rectangle marker indicates region of interest (ROI)
    r = cv.rectangle(frame, upper_left, bottom_right, (100, 50, 200), 1)
    enounter_r = cv.rectangle(frame, (100,584), (300,650), (100, 50, 200), 1)
    #ROI assignment
    ROI = frame[upper_left[1]: bottom_right[1], upper_left[0]: bottom_right[0]]

    #Converts ROI to HSV (apparently better)
    hsvFrame = cv.cvtColor(ROI, cv.COLOR_BGR2HSV)


    encounterROI = frame[584:650, 100:300]
    encounterhsvFrame = cv.cvtColor(encounterROI, cv.COLOR_BGR2HSV)

    #See if the start of encounter
    if (encounterhsvFrame == whiteScreen).all() and stateEncounter == False:
        stateEncounter = True
        encounterStartTime = time.time()
        print('Start of Encounter?')

        #startOfEncounterTimer = time.time()

    #find text box after start of encounter

    #end of Encounter
    if (hsvFrame == blackScreen).all() and stateEncounter == True and ((time.time() - encounterStartTime) > 2):
        stateEncounter = False
        encountersCounter += 1
        #reset states and non-ongoing counters
        textBoxCounter = 0
        stateTextBox = False
        print(encountersCounter)
        print('blackscreen detected')


    #first text box of encounter: 'Wild Pokemon appears'
    if (hsvFrame == textBoxActual).all() and stateTextBox==False and textBoxCounter == 0 and stateEncounter==True:
        print('Wild Pokemon textbox detected')
        stateTextBox = True
        textBoxCounter += 1

    #first gap after wild pokemon textbox
    if stateTextBox == True and not ((hsvFrame == textBoxActual).all()):
        start = time.time()
        stateTextBox = False

    #second text box of encounter (you send out your pokemon)
    if (hsvFrame == textBoxActual).all() and textBoxCounter == 1 and stateTextBox == False:
        print('Your Pokemon detected')
        stateTextBox = True
        end = time.time()
        gap = end - start
        print(f'Gap: {gap} s')
        textBoxCounter += 1

        if gap > 1:
            print('It\'s shiny!!!!!!!!!!!!!!!!!!!')
            alert()


    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
stream.release()
cv.destroyAllWindows()