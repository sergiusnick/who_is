import cv2
import numpy as np
import os

faces = []
labels = []

path_data = 'faces/'

names = os.listdir(path_data)
i = -1

# read each image in the faces folder
for root, dirs, files in os.walk(path_data):
    i = i + 1
    # for the recognizer we need an array of images_for_GUI and corresponding labels
    for name in files:
        faces.append(cv2.imread(root + '/' + name, cv2.IMREAD_GRAYSCALE))
        labels.append(i)

# create our LBPH face recognizer
face_recognizer = cv2.face.LBPHFaceRecognizer_create()

# import face detection cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# train model
face_recognizer.train(faces, np.array(labels))

cap = cv2.VideoCapture(0)
while True:
    # capture frame-by-frame
    ret, img = cap.read()

    # put a rectangle and a label for each recognized face
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_color = img[y:y + h, x:x + w]
        roi_gray = gray[y:y + h, x:x + w]
        label = face_recognizer.predict(roi_gray)
        cv2.putText(img, names[label[0] - 1] + ' ts:' + str(label[1]), (x, y),
                    cv2.FONT_HERSHEY_PLAIN, 1.5, (0, 255, 0), 2)
    # display the resulting frame
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
