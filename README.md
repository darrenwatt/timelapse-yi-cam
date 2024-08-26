# timelapse-yi-cam
Pull images from yi-camera rtsp stream and make it video.
Based on code by [James Lloyd](https://james.lloyd.ws/)

## pre-requisites - working ffmpeg install
sudo apt-get update && sudo apt-get install ffmpeg libsm6 libxext6  -y


## Running from Docker image:

Build docker image if you need to with:
`docker build -t darrenwatt/timelapse-yicam:v0.0.1 .`

Pull and run from Dockerhub with this:
`docker run -it -v '/home/username/temp-pics:/data' -e WEBCAM_RTSP='rtsp://192.168.0.180/ch0_0.h264' -e WEBCAM_PICS_DIR='/data' darrenwatt/timelapse-yicam:v0.0.1`

Or docker-compose with this:

```
  timelapse-yicam:
    container_name: timelapse-yicam
    image: darrenwatt/timelapse-yicam:v0.0.1
    volumes:
      - /mnt/media/timelapse-yicam:/data
    environment:
      - WEBCAM_RTSP=rtsp://<ip address>/ch0_0.h264
      - WEBCAM_PICS_DIR='/data'
      - WEBCAM_LOOP_TIME=300
    restart: unless-stopped
```