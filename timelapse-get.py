#!/bin/python
import os
import cv2
import shutil
import time
from config import Config


vcap = cv2.VideoCapture(Config.WEBCAM_RTSP)

topdir = Config.WEBCAM_PICS_DIR

if vcap.isOpened():
    ret, frame = vcap.read()
    if ret:
       cv2.imwrite('/code/src/static/img/webcam.png', frame)
       filename = time.strftime("%Y%m%d-%H%M%S")
       dirpath = time.strftime("%Y/%m/%d/")
       if not os.path.isdir(f'{topdir}{dirpath}'):
           os.makedirs(f'{topdir}{dirpath}')
           
       print(f'{topdir}{dirpath}{filename}.png')
       shutil.copy2('/code/src/static/img/webcam.png', f'{topdir}{dirpath}{filename}.png')
    else:
        print("Failed to Capture Frame")
else:
    print("Failed to open camera")