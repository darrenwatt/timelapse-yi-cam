import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    WEBCAM_RTSP = os.getenv('WEBCAM_RTSP') # rtsp URL, e.g. 'rtsp://<ip address>/ch0_0.h264'
    WEBCAM_PICS_DIR = os.getenv('WEBCAM_PICS_DIR') # base url to store snapshots
    WEBCAM_LOOP_TIME = os.getenv('WEBCAM_LOOP_TIME') or 300 # loop time, in seconds
