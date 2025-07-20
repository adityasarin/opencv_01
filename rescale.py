import cv2 as cv
import numpy as np


def rescaleFrame(frame, scale=0.75):
    width=int(frame.shape[1]*scale)
    height = int(frame.shape[0] * scale)

    dimension = (width,height)
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

img = cv.imread('Day1/Cat2.jpg')
cv.imshow('Cat',img)
print(type(img))
vid = cv.VideoCapture('./Day1/video1.mp4')

while True:
    isTrue,frame = vid.read()
    frame_resize = rescaleFrame(frame)
    cv.imshow('vid',frame)
    cv.imshow('vid resized', frame_resize)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
vid.release()
cv.destroyAllWindows()