import threading
import time
import cv2

class FaceDetection(threading.Thread):
    
    def __init__(self, frame, font, face_cascade):
        threading.Thread.__init__(self)
        self.frame = frame
        self.font = font
        self.done = False
        self.face_cascade = face_cascade
        self.faces = None
        print("Starting...")
        self.start()
        
    def run(self):
        frameYCC = cv2.cvtColor(self.frame, cv2.COLOR_BGR2YCR_CB)
        self.faces = self.face_cascade.detectMultiScale(frameYCC[:, :, 0], 1.8, 5, minSize=(30, 30), flags = cv2.cv.CV_HAAR_SCALE_IMAGE)
        self.done = True
        while(self.done):
            time.sleep(1)
        
