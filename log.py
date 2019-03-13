from datetime import datetime


class Log:
    def error(self, error):
        try:
            with open('logs.txt', 'a') as file:
                text = '[' + str(datetime.now()) + '] ' + error
                file.write(text + '\n')
        except Exception:
            pass

    def addPerson(self, name):
        try:
            with open('logs.txt', 'a') as file:
                text = '[' + str(datetime.now()) + '] added ' + name
                file.write(text + '\n')
        except Exception:
            pass

    def successfulAnalyse(self):
        try:
            with open('logs.txt', 'a') as file:
                text = '[' + str(datetime.now()) + '] successful analysis'
                file.write(text + '\n')
        except Exception:
            pass

class Console:
    def write(self, textC):
        try:
            with open('console.txt', 'a') as file:
                text = '[' + str(datetime.now()) + '] ' + textC
                file.write(text + '\n')
        except Exception:
            pass
