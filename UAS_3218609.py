# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 18:48:26 2021

@author: Pezzek
"""

import numpy as np
import cv2

im = cv2.imread('gambar.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,100,110,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(im, contours, -1, (0, 0, 200), 3)

cv2.imshow("Hasil", img)
cv2.imwrite("hasil_3218609.jpg", img)
