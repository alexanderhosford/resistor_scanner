import numpy as np
import cv2 as cv

cap = cv.VideoCapture(1)
while(True):
  ret,frame = cap.read()

  #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

  cv.imshow('frame',frame)

  k = cv.waitKey(1)


  if k == 27:
    cap.release()
    cv.destroyAllWindows()

  elif k == ord('s'):
    cv.imwrite('capture.png',frame)
    cap.release()
    cv.destroyAllWindows()

  #if cv.waitKey(1) & 0xFF == ord('q'):
   # break

 # if cv.waitKey(1) & 0xFF == ord('s'):
  #  cv.imwrite('capture.png',frame)
   # break

#cap.release()

#cv.destroyAllWindows()

