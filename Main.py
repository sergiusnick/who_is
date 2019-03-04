from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import (QMainWindow, QLabel, QApplication, QFileDialog)
from PyQt5 import uic
import shutil
import sys
import os
from log import Log
from script import Verification


# Main menu
class MainMenu(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 370)
        self.setWindowTitle('Whois')
        self.init_UI()

    def init_UI(self):
        # LOAD IMAGE
        set_background(self)

        # Загрузка GUI
        uic.loadUi('GUI/MainMenu.ui', self)

        self.pushExit.clicked.connect(self.close)
        self.pushStart.clicked.connect(lambda: show_window(self, startWin))
        self.pushAddPerson.clicked.connect(lambda: show_window(self, addPersonWin))

        self.show()


class Analyze(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 370)
        self.setWindowTitle('Whois')
        self.init_UI()

    def init_UI(self):
        try:
            # LOAD IMAGE
            self.setWindowIcon(QIcon(QPixmap('GUI/images_for_GUI/icon.jpg')))

            # Загрузка GUI
            uic.loadUi('GUI/Analyze.ui', self)
            self.textError.hide()
            self.textSuccess.hide()

            self.pushBack.clicked.connect(lambda: show_window(self, mainWin))
            self.pushOK.clicked.connect(self.search)

            self.show()
        except Exception as error:
            print(str(error))
            Log.error(None, str(error))
            self.textError.show()

    def search(self):
        try:
            print('start find')
            v = Verification(self.textEdit.toPlainText(), self.textName.toPlainText())
            self.need = v.search()


            self.textSuccess.show()

        except Exception as error:
            print(str(error))
            Log.error(None, str(error))
            self.textError.show()


class AddPerson(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 370)
        self.setWindowTitle('Whois')
        self.init_UI()

    def init_UI(self):
        self.directory = os.getcwd()
        self.filename = None

        # LOAD IMAGE
        self.setWindowIcon(QIcon(QPixmap('GUI/images_for_GUI/icon.jpg')))

        # Загрузка GUI
        uic.loadUi('GUI/AddPerson.ui', self)
        self.textError.hide()
        self.textSuccess.hide()

        self.pushBack.clicked.connect(lambda: show_window(self, mainWin))
        self.pushView.clicked.connect(self.choosePhotos)
        self.pushAdd.clicked.connect(self.addPerson)

        self.show()

    def choosePhotos(self):
        try:
            self.filename = QFileDialog.getOpenFileName(self, 'Open file', '/home')
            text = self.filename[0]
            self.textFiles.setText(text)
            self.textError.hide()

        except Exception as error:
            print(str(error))
            Log.error(None, str(error))
            self.textError.show()

    def addPerson(self):
        try:
            shutil.copy2(self.filename[0],
                         self.directory + '/static/faces/' + self.textName.toPlainText() + '.' +
                         self.filename[0].split('.')[-1])
            Log.addPerson(None, self.textName.toPlainText())

        except Exception as error:
            print(str(error))
            Log.error(None, str(error))
            self.textError.show()
        else:
            self.textSuccess.show()


# LOAD IMAGE
def set_background(self):
    self.setWindowIcon(QIcon(QPixmap('GUI/images_for_GUI/icon.jpg')))

    self.bg = QLabel(self)
    self.bg.resize(700, 370)
    self.bg.setPixmap(QPixmap("GUI/images_for_GUI/background.jpg").scaled(700, 370))


def show_window(old, new):
    if not (new is None):
        new.show()
    if not (old is None):
        old.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainMenu()
    startWin = Analyze()
    startWin.hide()
    addPersonWin = AddPerson()
    addPersonWin.hide()
    sys.exit(app.exec_())
