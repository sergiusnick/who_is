from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import (QMainWindow, QLabel, QApplication, QFileDialog)
from PyQt5 import uic
import sys


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
        uic.loadUi('MainMenu.ui', self)

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
            self.setWindowIcon(QIcon(QPixmap('images/icon.jpg')))

            # Загрузка GUI
            uic.loadUi('Analyze.ui', self)
            self.textError.hide()
            self.textSuccess.hide()

            self.pushBack.clicked.connect(lambda: show_window(self, mainWin))

            self.show()
        except Exception:
            self.textError.setText('Error')
            self.textError.show()


class AddPerson(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 370)
        self.setWindowTitle('Whois')
        self.init_UI()

    def init_UI(self):
        # LOAD IMAGE
        self.setWindowIcon(QIcon(QPixmap('images/icon.jpg')))

        # Загрузка GUI
        uic.loadUi('AddPerson.ui', self)
        self.textError.hide()
        self.textSuccess.hide()

        self.pushBack.clicked.connect(lambda: show_window(self, mainWin))
        self.pushView.clicked.connect(self.choosePhotos)

        self.show()

    def choosePhotos(self):
        try:
            self.filenames = QFileDialog.getOpenFileNames(self, 'Open file', '/home')
            text = ''
            for i in range(len(self.filenames[0]) - 1):
                text += self.filenames[0][i] + '; '
            self.textFiles.setText(text)
            print(self.filenames[0])
            self.textError.hide()

        except Exception:
            self.textError.setText('Error')
            self.textError.show()

    def setDataset(self):
        pass


# LOAD IMAGE
def set_background(self):
    self.setWindowIcon(QIcon(QPixmap('images/icon.jpg')))

    self.bg = QLabel(self)
    self.bg.resize(700, 370)
    self.bg.setPixmap(QPixmap("images/background.jpg").scaled(700, 370))


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
