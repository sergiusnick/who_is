import dlib
from skimage import io
from scipy.spatial import distance
import os
from log import Log, Console
import shutil


class Verification:
    def __init__(self, dirFind, nameList):
        try:
            # Подключение моделей
            self.sp = dlib.shape_predictor('libs/shape_predictor_68_face_landmarks.dat')
            self.facerec = dlib.face_recognition_model_v1(
                'libs/dlib_face_recognition_resnet_model_v1.dat')

            self.detector = dlib.get_frontal_face_detector()
            self.directory = os.getcwd()
            self.countDIR = len(os.listdir(self.directory + '/static'))
            os.mkdir(self.directory + '/static/' + str(self.countDIR))

            # Поиск изображений в каталоге
            pathsToFind = []
            for img in os.listdir(dirFind):
                if img.endswith('.jpg') or img.endswith('.JPEG') or img.endswith(
                        '.png') or img.endswith('.JPG'):
                    pathsToFind.append(dirFind + '/' + img)

            self.imgs = [self.directory + '/faces/' + name + '.jpg' for name in nameList]
            print(pathsToFind)

            Console.write(None, str(pathsToFind))
            self.paths = pathsToFind

        except Exception as    error:
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

            # Открытие изображения
            img = io.imread(img)
            dets = self.detector(img, 1)

            # print(img)
            Console.write(None, str(img))

            # Определение фигур лиц
            for k, d in enumerate(dets):
                print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                    k, d.left(), d.top(), d.right(), d.bottom()))
                Console.write(None, "Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(
                    k, d.left(), d.top(), d.right(), d.bottom()))
                shape = self.sp(img, d)
                try:
                    descriptor = self.facerec.compute_face_descriptor(img, shape)

                    return descriptor
                except NameError:
                    print('there are no faces')
                    Console.write(None, 'there are no faces')

        except Exception as error:
            print(str(error))
            Log.error(None, str(error))
            Console.write(None, str(error))

    def search(self):
        try:
            self.need = []
            self.mainImgDescriptors = [self.findDescriptor(img) for img in self.imgs]

            for self.count in range(len(self.paths)):
                faceDescriptor = self.findDescriptor(self.paths[self.count])
                for descriptor in self.mainImgDescriptors:
                    try:
                        if distance.euclidean(descriptor, faceDescriptor) <= 0.6:
                            self.need.append(self.paths[self.count])
                            shutil.copy2(self.paths[self.count],
                                         self.directory + '/static/' + str(self.countDIR))
                        print(distance.euclidean(descriptor, faceDescriptor))
                        Console.write(None, str(distance.euclidean(descriptor, faceDescriptor)))
                    except NameError:
                        pass
                    except TypeError:
                        pass
                    except Exception as error:
                        print(str(error))
                        Console.write(None, str(error))

            return self.need

        except Exception as error:
            print(str(error))
            Log.error(None, str(error))
            Console.write(None, str(error))
