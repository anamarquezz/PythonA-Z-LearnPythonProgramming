# Objective of the program given is to dtect face with provided image
# pip install opencv-python
# pip
#
#   ONLY FOR FACE
#   A Haar Cascade is basically a classifier wich is used to detect particular objects from the source.
#   The hearcascade_frontalface_default.xml is a haar cascade designed by OpenCV to detect the frontal face.

import cv2

detect = cv2.CascadeClassifier(
    "C:\\Users\\anamarquez\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

imp_img = cv2.VideoCapture(
    "C:\\Users\\anamarquez\\source\\Repass\\PythonA-Z-LearnPythonProgramming\\Project_FaceDetection\\elon.jpg")


res, img = imp_img.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detects faces of different sizes in the input image
faces = detect.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2) # ( image, pt1, pt2, color, thikness) p1= Vertex of rectangle p2= vertex of rectangle opp. to pt1

cv2.imshow("Elon Image", img)
cv2.waitKey(0)
imp_img.release()
cv2.destroyAllWindows()
