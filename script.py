import dlib
from skimage import io
from scipy.spatial import distance


class Verification:
    def __init__(self, pathsToMainImgs, pathsToExistImgs):
        self.sp = dlib.shape_predictor('libs/shape_predictor_68_face_landmarks.dat')
        self.facerec = dlib.face_recognition_model_v1(
            'libs/dlib_face_recognition_resnet_model_v1.dat')
        self.detector = dlib.get_frontal_face_detector()

        self.findImgs = []
        for path in pathsToMainImgs:
            self.findImgs.append(self.openImg(path))

        self.existImgs = []
        for path in pathsToExistImgs:
            self.existImgs.append(self.openImg(path))

        self.search()

    def openImg(self, pathToImg):
        try:
            return io.imread(pathToImg)
        except FileNotFoundError:
            print('File not found')

    def search(self):
