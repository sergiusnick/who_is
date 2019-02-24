import os
import numpy as np
import cv2
from PIL import Image

# create folder to save pictures of a person
name = input('Enter your name:')
if not os.path.exists('faces'):
    os.mkdir('faces')
os.mkdir('faces/' + name)
print(name + ' folder created!')
path = 'faces/' + name

# import face detection cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# create capture object
cap = cv2.VideoCapture(0)

# take 10 pictures
for i in range(1, 11):
    image = input('Input ' + str(i) + ' >> ')
    image = Image.open(image)
    image = image.getdata()
    image = np.asarray(image)

    # capture frame-by-frame
    ret, img = cap.read()

    # convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # detect face
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # for each face draw a rectangle around and copy the face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_color = img[y:y + h, x:x + w]
        roi_gray = gray[y:y + h, x:x + w]

    # display the resulting frame
    cv2.imshow('frame', img)

    # when pressing space resize face image and save it
    roi_gray = cv2.resize(roi_gray, (100, 100))
    cv2.imwrite(path + '/' + str(i) + '.jpg', roi_gray)

# when everything done, release the capture
cap.release()
cv2.destroyAllWindows()
