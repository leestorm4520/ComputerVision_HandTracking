import cv2
import mediapipe as mp
import time
import HandTrackingModule as htm

pTime=0
cTime=0

# define a video capture object
vid = cv2.VideoCapture(0)
detector=htm.handDetector() #create a handDetector object (no argument, use default value)

while(True):
    
    # Capture the video frame
    # by frame
    ret, img= vid.read()
    img=detector.findHands(img) #pass the image recorded by the camera
    lmList=detector.findPosition(img)
    if len(lmList)!=0:
        print(lmList[4])

    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img, str(int(fps)), (10,70),cv2.FONT_HERSHEY_COMPLEX,3, (57,255,20),3)
    # Display the resulting frame
    cv2.imshow('Image', img)
    
    # the 'q' button is set as the quitting button 
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
