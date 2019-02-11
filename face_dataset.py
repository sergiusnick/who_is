import numpy as np
import cv2
import os

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For each person, enter one numeric face id
face_id = input('[INFO]    enter user id end press  ==> ')

count = int(input('[INFO]    enter the number of photos for the train (MIN 5) ==> '))
while count < 5:
    print('[WARNING] You entered', count, 'photos instead at least 5')
    count = int(input('[INFO]    enter the number of photos for the train (MIN 5) ==> '))

paths = []
for i in range(count):
    path = input('[INFO]    enter the path to your photo ==> ')
    while not os.path.isfile(path) and not (path.endswith('jpg') or path.endswith('png')):
        print('[WARNING] the specified path to photo does not exist')
        path = input('[INFO]    enter the path to your photo ==> ')
    paths.append([path])
print(paths)

i = 0
for img in paths:
    img = np.asarray(img)
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        i += 1

    # Save the captured image into the datasets folder
    cv2.imwrite("dataset/User." + str(face_id) + '.' + str(i) + ".jpg", gray[y:y + h, x:x + w])

cv2.imshow('image', img)
cv2.waitKey(0)
