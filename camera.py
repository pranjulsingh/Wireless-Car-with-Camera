#!/usr/bin/python
#Author: Pranjul Singh
#Date: 13, October, 2017
#Time: 01:20 am

import cv2
import time


class Camera:

    def __init__(self):

        frame_width = 640
        frame_height = 480
        frame_rate = 20
        resolution = (frame_width, frame_height)
        self.frames = None
        self.cap = cv2.VideoCapture(0)
        print("Initilizing Camera .....")
        time.sleep(1)

    def get_frame(self):

        self.frames = open('stream.jpg', 'wb+')
        s, img = self.cap.read()
        if s:
            cv2.imwrite('stream.jpg', img)
        return self.frames.read()
