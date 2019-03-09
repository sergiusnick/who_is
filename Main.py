try:
    from log import Log, Console
    from PyQt5.QtGui import QPixmap, QIcon
    from PyQt5.QtWidgets import (QMainWindow, QLabel, QApplication, QFileDialog)
    from PyQt5 import uic
    import shutil
    import sys
    import os
    from script import Verification
    import webbrowser
    from flask import Flask, send_from_directory
    from flask import url_for
    from win32api import GetSystemMetrics


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
                print('start finding')
                Console.write(None, 'start finding')
                v = Verification(self.textEdit.toPlainText(), self.textName.toPlainText())
                self.need = v.search()
                self.pushLink.setText('http://127.0.0.1:8080/')

                for i in range(len(self.need)):
                    self.need[i] = self.need[i].replace('\\', '/')

                self.textSuccess.show()
                self.pushLink.clicked.connect(self.openBrowser)

            except Exception as error:
                print(str(error))
                Log.error(None, str(error))
                self.textError.show()

        def openBrowser(self):
            try:
                app = Flask(__name__)

                width = GetSystemMetrics(0)
                height = GetSystemMetrics(1)
                print(width, height)
                print(self.need)
                Console.write(None, self.need)

                @app.route('/')
                def index():
                    text = '''<!doctype html>
                                <html lang="en">
                                  <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width,
                                    initial-scale=1, shrink-to-fit=no">
                                    <link rel="stylesheet"
                                    href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
                                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
                                    crossorigin="anonymous">
                                    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                                    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
                                    <title>Привет, Яндекс!</title>
                                  </head>
                                  <body>
                                    <h1>Привет, Яндекс!</h1>
                                    <div class="alert alert-primary" role="alert">
                                      А мы тут компонентами Bootstrap балуемся
                                    </div>
                                    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                                      <ol class="carousel-indicators">
                                        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                                        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                                        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                                      </ol>
                                      <div class="carousel-inner">'''

                    # text += '''<div class="carousel-item active">
                    #               <img class="d-block w-100" src="{}" alt="Блин блинский">
                    #             </div>'''.format(url_for('static', filename='dima_2.jpg'))
                    for i in range(2):
                        text += '''<div class="carousel-item">
                                      <img class="d-block w-100" src="{}" alt="Блин блинский">
                                    </div>'''.format(url_for('static',
                                                             filename='C:/CicadaInc/whois/test_versions/fotoVerification/dimas.jpg'))

                    text += '''</div>
                              <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                              </a>
                              <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                              </a>
                            </div>
                          </body>
                        </html>'''

                    return text

                webbrowser.open('http://127.0.0.1:8080/')

                if __name__ == '__main__':
                    app.run(port=8080, host='127.0.0.1')

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
                             self.directory + '/faces/' + self.textName.toPlainText() + '.' +
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

except Exception as error:
    Console.write(None, str(error))
    print(error)
