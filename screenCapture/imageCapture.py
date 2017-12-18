import pyscreenshot as ImageGrab
import numpy as np
import cv2
import time
import tkinter as tk


def main():
    im = np.array(ImageGrab.grab(bbox=(175,102,500,430)))
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    im = cv2.Canny(im, threshold1 = 200, threshold2 = 300)
    im = cv2.GaussianBlur(im, (5,5), 1)
    cv2.imshow('window', im)

        
    
if __main__ == '__name__':
    main()
