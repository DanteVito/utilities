# https://opencv-python-tutroals.readthedocs.io/en/latest/
# http://stackoverflow.com/questions/11094481/capturing-a-single-image-from-my-webcam-in-java-or-python
# install python-opencv bindings, numpy
from cv2 import *
# initialize the camera
cam = VideoCapture(0)   # 0 -> index of camera
s, img = cam.read()
if s:    # frame captured without any errors
    namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    imshow("cam-test",img)
    waitKey(0)
    destroyWindow("cam-test")
    imwrite("filename.jpg",img) #save image

#pip install qrtools
import qrtools
# https://github.com/primetang/qrtools
# http://stackoverflow.com/questions/27233351/how-to-decode-a-qr-code-image-in-preferably-pure-python
qr = qrtools.QR()
qr.decode("imgQrcode.png")
linkQrCode = qr.data 

