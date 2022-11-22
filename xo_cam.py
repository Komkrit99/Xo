from xml.dom import VALIDATION_ERR
import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
while(True):
    rat,img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gauss = cv2.GaussianBlur(gray,(21,21),cv2.BORDER_DEFAULT)
    #cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
    cv2.imshow('img',gauss)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break