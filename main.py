#!/bin/python
import os
import cv2
import shutil
import time
from config import Config

# static vars
max_retries=5

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
        print("Webcam pics directory is not set. Pass in ENVVAR WEBCAM_PICS_DIR. Exiting.")
        exit(1)
    topdir = Config.WEBCAM_PICS_DIR

    print("WEBCAM_LOOP_TIME: {} seconds".format(Config.WEBCAM_LOOP_TIME))
    looptime = int(Config.WEBCAM_LOOP_TIME)

    return vcap, topdir, looptime

def get_image_from_rtsp(vcap, topdir):
    for attempt in range(max_retries):
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
                break
            else:
                print(f"Failed to Capture Frame (attempt {attempt+1}/{max_retries})")
        else:
            print(f"Failed to open camera (attempt {attempt+1}/{max_retries})")
            vcap.release()  # Release capture object
            vcap = cv2.VideoCapture(vcap)  # Re-open the stream
        print("Failed to capture image after all retries.")  


if __name__ == "__main__":
    # do config things
    vcap, topdir, looptime = config_things()

    # do main loop things
    while True:
        get_image_from_rtsp(vcap, topdir)
        time.sleep(looptime)