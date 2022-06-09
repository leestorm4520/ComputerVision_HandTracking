import cv2
import time
import mediapipe as mp


class handDetector():
    def __init__(self, static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5):
        self.static_image_mode=static_image_mode
        self.max_num_hands=max_num_hands
        self.min_detection_confidence=min_detection_confidence
        self.min_tracking_confidence=min_tracking_confidence
        #find the hands on the camera
        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(self.static_image_mode, self.max_num_hands, self.min_detection_confidence, self.min_tracking_confidence)
        self.mpDraw=mp.solutions.drawing_utils
    def findHands(self, img, draw=True):
        imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results=self.hands.process(imgRGB)
        if(results.multi_hand_landmarks):
            for handLM in results.multi_hand_landmarks:
                if draw:
                    # for id, lm in enumerate(handLM.landmark):
                    #     #print(id+"\n"+lm)
                    #     h,w,c=img.shape 
                    #     cx,cy=int(lm.x*w), int(lm.y*h) #find the postion of the landmark
                    #     #if id==0:
                    #     #   cv2.circle(img,(cx,cy),25,(57,255,20),cv2.FILLED)
                    self.mpDraw.draw_landmarks(img, handLM, self.mpHands.HAND_CONNECTIONS)
        return img

