import dlib
from skimage import io
from scipy.spatial import distance
import os


class Verification:
    def __init__(self, dirFind, name):
        self.sp = dlib.shape_predictor('libs/shape_predictor_68_face_landmarks.dat')
        self.facerec = dlib.face_recognition_model_v1(
            'libs/dlib_face_recognition_resnet_model_v1.dat')
        self.detector = dlib.get_frontal_face_detector()
        directory = os.getcwd()

        pathsToFind = []
        for img in os.listdir(dirFind):
            if img.endswith('.jpg') or img.endswith('.JPEG') or img.endswith('.png'):
                pathsToFind.append(dirFind + '/' + img)

        self.img = directory + '/faces/' + name + '.jpg'
        # print(pathsToFind)
        # self.findImg = [self.openImg(path) for path in pathsToFind]
        self.paths = pathsToFind

    def openImg(self, pathToImg):
        try:
            return io.imread(pathToImg)
        except FileNotFoundError:
            print('File not found', pathToImg)

    def findDescriptor(self, img):
        print(img)
        img = io.imread(img)
        dets = self.detector(img, 1)

        for k, d in enumerate(dets):
            print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                k, d.left(), d.top(), d.right(), d.bottom()))
            shape = self.sp(img, d)
        return self.facerec.compute_face_descriptor(img, shape)

    def search(self):
        need = []
        mainImgDescriptor = self.findDescriptor(self.img)
        # print(mainImgDescriptor)

        for img in self.paths:
            faceDescriptor = self.findDescriptor(img)
            if distance.euclidean(mainImgDescriptor, faceDescriptor) <= 0.6:
                need.append(img)
            print(distance.euclidean(mainImgDescriptor, faceDescriptor))

        return need
