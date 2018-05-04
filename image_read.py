from PIL import Image
import StringIO
import cv2
import time

import numpy

'''while(True):
    frames = cv2.imread('stream.jpg')
    cv2.imshow('i', frames)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
'''


img = None

while True:
    with open('stream.jpg', 'rb') as img_bin:
        buff = StringIO.StringIO()
        buff.write(img_bin.read())
        buff.seek(0)
        temp_img = numpy.asarray(Image.open(buff), dtype=numpy.uint8)
        img = cv2.cvtColor(temp_img, cv2.COLOR_RGB2BGR)

    cv2.imshow('i', img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
