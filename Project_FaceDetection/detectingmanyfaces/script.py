import cv2
import glob  # glob: to traverse a whole directory

gimg = glob.glob(
    "C:\\Users\\anamarquez\\source\\Repass\\PythonA-Z-LearnPythonProgramming\\Project_FaceDetection\\*.jpg")
# The glob.glob returns the list files with their full path (unlike os.listdir()) and is more powerful
# than os.listdir that foes not use wildcards.

detect = cv2.CascadeClassifier(
    "C:\\Users\\anamarquez\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")


for timg in gimg:
    img = cv2.imread(timg)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    face = detect.detectMultiScale(gray, 1.20, 5)

    for(x, y, w, h) in face:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Detect Multiple Images", img)  # Display resulting frame
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
