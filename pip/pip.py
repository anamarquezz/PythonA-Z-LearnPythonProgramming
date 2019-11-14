# pip
#   is a package management system used to install and manage software packages written in python.
#   Many packages can be found in the defaul source for packages and their dependencies - Python Package Index
#
#
# pip --version
# pip --help
# pip install opencv-python
# pip search opencv
# pip show  opencv-python
#

import cv2
face_cascade = cv2.CascadeClassifier(
    "C:\\Users\\anamarquez\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(
    "https://www.ergcouncil.com/home/images/group-cheering-diversity.jpg")

ret, img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for(x, y, w, h) in faces:
    # to draw a rectangle in a face
    cv2.rectangle(img, (x, y), (x+w, y+h), (221, 74, 228), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv2.imshow('img', img)
k = cv2.waitKey(0)

# Clone the window
cap.release()

# de-allocate any associates memory usage
cv2.destroyAllWindows()
