from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
import numpy as np
import playsound
import threading
import imutils
import time
import dlib
import cv2

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
(mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]
(nStart, nEnd) = face_utils.FACIAL_LANDMARKS_IDXS["nose"]

def warningSound(path):
	playsound.playsound(path)
	
sound = "./siren.mp3"
COUNTER = 0
vs = cv2.VideoCapture(0)
time.sleep(1.0)

while True:
        ret, frame = vs.read()
        frame = imutils.resize(frame, width=800)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        th, th_f = cv2.threshold(gray, 130, 255, cv2.THRESH_BINARY)
        
        rects = detector(th_f, 0)
        mouthHull = []
        noseHull = []

        for rect in rects:
                shape = predictor(gray, rect)
                shape = face_utils.shape_to_np(shape)

                nose = shape[nStart:nEnd]
                noseHull = cv2.convexHull(nose)
                mouth = shape[mStart:mEnd]
                mouthHull = cv2.convexHull(mouth)
        	
                cv2.drawContours(frame, [mouthHull], -1, (0, 255, 0), 1)
                cv2.drawContours(frame, [noseHull], -1, (0, 255, 0), 1)
                if not t.is_alive():
                        print("warning")
                        t.run()
                        plkop0[







                                
        cv2.imshow("Frame", frame)
        
        t = threading.Thread(target=warningSound, args=(sound,))
                        
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
                break


vs.release()
cv2.destroyAllWindows()
