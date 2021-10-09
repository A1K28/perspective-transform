import cv2 
import numpy as np 

if __name__ == "__main__":
    width = 635
    height = 618
    # Turn on Laptop's webcam
    # cap = cv2.VideoCapture(0)
    while True:
        # ret, frame = cap.read()
        frame = cv2.imread('media/frame.png', 0) 
      
        # Locate points of the documents or object which you want to transform
        pts1 = np.float32([[52, 38], [527, 191], [89, 562], [536, 442]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
          
        # Apply Perspective Transform Algorithm
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        result = cv2.warpPerspective(frame, matrix, (width, height))
        # Wrap the transformed image
      
        cv2.imshow('frame', frame) # Inital Capture
        cv2.imshow('frame1', result) # Transformed Capture
      
        #press 'esc' to exit
        if cv2.waitKey(24) == 27:
            break
      
    # cap.release()
    cv2.destroyAllWindows()