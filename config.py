import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    WEBCAM_RTSP = os.getenv('WEBCAM_RTSP')
    WEBCAM_PICS_DIR = os.getenv('WEBCAM_PICS_DIR')