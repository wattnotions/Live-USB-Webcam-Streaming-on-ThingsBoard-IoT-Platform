"""
A Simple program to detect the human faces using Haarcascade Classifier

Date : 21 March 2019
Author : Shiyaz T
"""


import cv2
#haar_cascade_face = cv2.CascadeClassifier('/home/shiyaztech/Documents/Applications/OpenCV/opencv/data/haarcascades/haarcascade_frontalface_default.xml')


class VideoCamera(object):
    def __init__(self):
       self.cap = cv2.VideoCapture(0)
       # self.frameWidth = int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH))
       # self.frameHeight = int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT))
       

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        success, image = self.cap.read()
        image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
