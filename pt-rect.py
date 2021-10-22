import cv2 
import numpy as np 

if __name__ == "__main__":
    # Turn on Laptop's webcam
    # cap = cv2.VideoCapture(0)
    while True:
        # ret, frame = cap.read()
        frame = cv2.imread("media/life-is-strange.jpg", 3)
        height, width, dim = frame.shape

        points = [[28,28], [699,15], [0,height], [width, height]]

        # Locate points of the documents or object which you want to transform
        pts1 = np.float32([points[0], points[1], points[2], points[3]])
        pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
          
        # Apply Perspective Transform Algorithm
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        result = cv2.warpPerspective(frame, matrix, (width, height))
        # Wrap the transformed image

        # Plot points on selected square
        for point in points:
            frame = cv2.circle(frame, point, 5, (0,0,255), thickness=-1)
      
        cv2.imshow('frame', frame) # Inital Capture
        cv2.imshow('frame1', result) # Transformed Capture
      
        # press 'esc' to exit
        if cv2.waitKey(24) == 27:
            cv2.imwrite('media/result-colorless.png', result)
            break
      
    # cap.release()
    cv2.destroyAllWindows()