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
        self.hands=self.mpHands.Hands(self.static_image_mode, self.min_detection_confidence, self.min_tracking_confidence )
        self.mpDraw=mp.solutions.drawing_utils
    def findHands(self):
        imgRGB= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results=hands.process(imgRGB)
            if(results.multi_hand_landmarks):
                for handLM in results.multi_hand_landmarks:
                    for id, lm in enumerate(handLM.landmark):
                        #print(id+"\n"+lm)
                        h,w,c=img.shape 
                        cx,cy=int(lm.x*w), int(lm.y*h) #find the postion of the landmark
                        #if id==0:
                        #   cv2.circle(img,(cx,cy),25,(57,255,20),cv2.FILLED)
                    mpDraw.draw_landmarks(img, handLM, mpHands.HAND_CONNECTIONS)


   

def main():
    pTime=0
    cTime=0

    # define a video capture object
    vid = cv2.VideoCapture(0)
    
    while(True):
        
        # Capture the video frame
        # by frame
        ret, img= vid.read()
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime
        cv2.putText(img, str(int(fps)), (10,70),cv2.FONT_HERSHEY_COMPLEX,3, (57,255,20),3)
        # Display the resulting frame
        cv2.imshow('Image', img)
        
        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
  
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()


if __name__=="__main__":
    main()