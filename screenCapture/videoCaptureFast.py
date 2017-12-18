import numpy as np
from mss import mss
import cv2
#import time


def main():
    mon = {'top': 0, 'left':0, 'width':500, 'height':500}
    sct = mss()
    #lastTime = time.time()
    while True:
        #print(lastTime)
        #lastTime = time.time() - lastTime
        sct_img = sct.grab(mon)
        img = sct_img
        cv2.imshow('test', np.array(img))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        
    
if __name__ == '__main__':
    main()
