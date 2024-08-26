#!/bin/python
import os
import cv2
import shutil
import time
from config import Config


def config_things():
    if Config.WEBCAM_RTSP:
        print("WEBCAM_RTSP: {}".format(Config.WEBCAM_RTSP))
    else:
        print("RTSP stream URL is not set. Pass in ENVVAR WEBCAM_RTSP. Exiting.")
        exit(1)
    vcap = cv2.VideoCapture(Config.WEBCAM_RTSP)

    if Config.WEBCAM_RTSP:
        print("WEBCAM_PICS_DIR: {}".format(Config.WEBCAM_PICS_DIR))
    else:
        print("Webcam pics directoryu is not set. Pass in ENVVAR WEBCAM_PICS_DIR. Exiting.")
        exit(1)
    topdir = Config.WEBCAM_PICS_DIR

    print("WEBCAM_LOOP_TIME: {} seconds".format(Config.WEBCAM_LOOP_TIME))
    looptime = Config.WEBCAM_LOOP_TIME

def get_image_from_rtsp(vcap, topdir):
  if vcap.isOpened():
      ret, frame = vcap.read()
      if ret:
         cv2.imwrite('.tmp.png', frame)
         filename = time.strftime("%Y%m%d-%H%M%S")
         dirpath = time.strftime("%Y/%m/%d/")
         if not os.path.isdir(f'{topdir}/{dirpath}'):
             os.makedirs(f'{topdir}/{dirpath}')

         print("Generated image", f'{topdir}/{dirpath}{filename}.png')
         shutil.move('.tmp.png', f'{topdir}/{dirpath}{filename}.png')
      else:
          print("Failed to Capture Frame")
  else:
      print("Failed to open camera")


if __name__ == "__main__":
    vcap, topdir, looptime = config_things()
    get_image_from_rtsp(vcap, topdir)