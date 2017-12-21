import cv2
import sys
from button import Button
from FaceDetection import FaceDetection
import time

allowed_args = ["canny", "psycho", "face", "red", "green", "blue"]
colors = {"red": 2, "green": 1, "blue": 0}

font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, thickness=1, lineType=8)

def canny(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2YCR_CB)
    frame = cv2.Canny(frame[:, :, 0], 100, 200)
    cv2.cv.PutText(cv2.cv.fromarray(frame),"Edge Detection", (10, 30), font, (255, 255, 255))
    return frame


def limited_channels(frame, colors2):
    text = "Channels: "
    for c in colors.keys():
        if c not in colors2:
            frame[:,:,colors[c]] = 0
        else:
            text += c
            text += " "
            
    cv2.cv.PutText(cv2.cv.fromarray(frame),text, (10, 30), font, (255, 255, 255))
    return frame

def psycho_delic(frame):
    frame = cv2.applyColorMap(frame, cv2.COLORMAP_HSV)
    cv2.cv.PutText(cv2.cv.fromarray(frame),"Psycho", (10, 30), font, (0,0,0))
    return frame


def choose_function(frame, button_state):
    if button_state == 1:
        return canny(frame)
    elif button_state == 2:
        return psycho_delic(frame)
    elif button_state == 3:
        return limited_channels(frame, ["red"])
    elif button_state == 4:
        return limited_channels(frame, ["red", "green"])
    elif button_state == 5:
        return limited_channels(frame, ["green"])
    elif button_state == 6:
        return limited_channels(frame, ["blue", "green"])
    elif button_state == 7:
        return limited_channels(frame, ["blue"])
    elif button_state == 8:
        return limited_channels(frame, ["red", "blue"])
    else:
        cv2.cv.PutText(cv2.cv.fromarray(frame),"Normal", (10, 30), font, (255, 255, 255))
        return frame

def main():
    button = Button(10, 12, 13, 8, 11)

    cv2.namedWindow("preview", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty('preview', cv2.WND_PROP_FULLSCREEN, cv2.cv.CV_WINDOW_FULLSCREEN)
    #cv2.namedWindow("preview", cv2.WINDOW_AUTOSIZE)
    vc = cv2.VideoCapture(0)
    
    if vc.isOpened():
        rval, frame = vc.read()
    else:
        rval = False
    
    while rval:
        frame = choose_function(frame, button.button_state)
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27:
            button.state = False
            button.join()
            break
    vc.release()
    cv2.destroyWindow("preview")


main()
