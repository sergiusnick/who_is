import dlib
from skimage import io
from scipy.spatial import distance
import os
from log import Log, Console
import shutil


class Verification:
    def __init__(self, dirFind, name):
        try:
            self.sp = dlib.shape_predictor('libs/shape_predictor_68_face_landmarks.dat')
            self.facerec = dlib.face_recognition_model_v1(
                'libs/dlib_face_recognition_resnet_model_v1.dat')
            self.detector = dlib.get_frontal_face_detector()
            self.directory = os.getcwd()
            self.countDIR = len(os.listdir(self.directory + '/static'))
            os.mkdir(self.directory + '/static/' + str(self.countDIR))

            pathsToFind = []
            for img in os.listdir(dirFind):
                if img.endswith('.jpg') or img.endswith('.JPEG') or img.endswith('.png'):
                    pathsToFind.append(dirFind + '/' + img)

            self.img = self.directory + '/faces/' + name + '.jpg'
            print(pathsToFind)
            Console.write(None, str(pathsToFind))
            # self.findImg = [self.openImg(path) for path in pathsToFind]
            self.paths = pathsToFind

        except Exception as error:
            print(str(error))
            Log.error(None, str(error))

    def openImg(self, pathToImg):
        try:
            return io.imread(pathToImg)
        except FileNotFoundError:
            print('File not found', pathToImg)
            Console.write(None, 'File not found' + str(pathToImg))
        except Exception as error:
            print(str(error))
            Log.error(None, str(error))
            Console.write(None, str(error))

    def findDescriptor(self, img):
        try:
            self.added = False
            print(img)
            Console.write(None, str(img))
            img = io.imread(img)
            dets = self.detector(img, 1)

            for k, d in enumerate(dets):
                print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                    k, d.left(), d.top(), d.right(), d.bottom()))
                Console.write(None, "Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                    k, d.left(), d.top(), d.right(), d.bottom()))
                shape = self.sp(img, d)
                descriptor = self.facerec.compute_face_descriptor(img, shape)

                try:
                    if distance.euclidean(self.mainImgDescriptor, descriptor) <= 0.6:
                        self.need.append(self.paths[self.count])
                        shutil.copy2(self.paths[self.count],
                                     self.directory + '/static/' + str(self.countDIR))
                        self.added = True

                    print(distance.euclidean(self.mainImgDescriptor, descriptor))
                    Console.write(None, str(distance.euclidean(self.mainImgDescriptor, descriptor)))
                    return descriptor

                except AttributeError:
                    return descriptor

        except Exception as error:
            print(str(error))
            Log.error(None, str(error))
            Console.write(None, str(error))

    def search(self):
        try:
            self.need = []
            self.mainImgDescriptor = self.findDescriptor(self.img)

            for self.count in range(len(self.paths)):
                faceDescriptor = self.findDescriptor(self.paths[self.count])
                if distance.euclidean(self.mainImgDescriptor, faceDescriptor) <= 0.6:
                    if self.added is False:
                        self.need.append(self.paths[self.count])
                        shutil.copy2(self.paths[self.count],
                                     self.directory + '/static/' + str(self.countDIR))

            return self.need

        except Exception as error:
            print(str(error))
            Log.error(None, str(error))
            Console.write(None, str(error))
