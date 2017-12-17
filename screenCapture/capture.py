import pyscreenshot as ImageGrab
from PIL import ImageTk, Image
import tkinter as tk
import numpy as np
import cv2
import time

def processImg(img):
    orgImg = img
    processedImg = cv2.cvtColor(img, cv2.COLOR_BRG2GRAY)

def main():
    window = tk.Tk()
    window.geometry('500x500')
    im = ImageTk.PhotoImage(ImageGrab.grab(bbox=(50,50,550,550)))  # X1,Y1,X2,
    panel = tk.Label(window, image = im)
    panel.pack()
    window.update()
    updt(window,panel, im)

def updt(window,panel, im):
    lasttime = time.time()
    while True:
        window.update()
        print(time.time()-lasttime)
        lasttime = time.time()
        im = ImageTk.PhotoImage(ImageGrab.grab(bbox=(50,50,550,550)))  # X1,Y1,X2,
        panel.configure(image = im)
        panel.image = im
        
    
main()
