import cv2 as cv
import numpy
import numpy as np

#blank = np.zeros((500,500,3),dtype='uint8')
#cv.imshow('Blank',blank)
#blank[:]=0,255,255
#cv.imshow('Colour',blank)
#blank[200:300,300:500]=0,0,255
#cv.imshow('Shape',blank)
#cv.rectangle(blank,(50,50),(300,450),(0,230,5),thickness=cv.FILLED)
#cv.circle(blank,(250,250),200,(2,220,4),thickness=cv.FILLED)
#cv.line(blank,(0,0),(255,255),(66,22,12),thickness=5)
#cv.putText(blank,'Captions here',(100,400),cv.FONT_HERSHEY_SIMPLEX,1.0,(5,255,255),1)
#cv.imshow('rectangle',blank)
img = cv.imread('./Day1/Cat2.jpg')
cv.imshow('Cat1',img)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('GrayCat1',gray)

blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
cv.waitKey(0)