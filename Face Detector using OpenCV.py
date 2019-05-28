import cv2
import datetime

def capture():
    video = cv2.VideoCapture(0)
    check,frame=video.read()
    return frame


def detect():
    im = capture()
    im = cv2.resize(im,(int(im.shape[1]/8),int(im.shape[0]/8)))
    grim = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    fc = cv2.CascadeClassifier(r"H:\PYTHON\Practise\venv\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml")

    face = fc.detectMultiScale(grim)

    for x,y,w,h in face:
        img = cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,0),3)

    cv2.imshow("face",img)
    cv2.waitKey(0)

detect()





