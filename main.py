import os
os.environ["IMAGEIO_FFMPEG_EXE"] = r"ffmpeg.exe" #Put ffmpeg.exe file to the folder of the program.
from moviepy.video.io.VideoFileClip import VideoFileClip
import threading
from converterui import Ui_MainWindow
from proglog import ProgressBarLogger
from PyQt5 import QtWidgets
import sys

class Observer():
    _observers = []
    def __init__(self):
        self._observers.append(self)
        self._observables = {}
    def observe(self, event_name, callback):
        self._observables[event_name] = callback


class Event():
    def __init__(self, name, data, autofire = True):
        self.name = name
        self.data = data
        if autofire:
            self.fire()
    def fire(self):
        for observer in Observer._observers:
            if self.name in observer._observables:
                observer._observables[self.name](self.data)

class App(QtWidgets.QMainWindow, Observer):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Observer.__init__(self)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.log = MyBarLogger()
        self.numberOfFiles = 0
        self.choosenfileOrFiles = ()
        self.savePathStr = ""
        self.fps=5

        self.ui.fpsSpinBox.valueChanged.connect(self.setFPS)


        self.ui.chooseFileButton.clicked.connect(self.chooseFile)
        self.ui.saveButton.clicked.connect(self.setSavePathText)

        self.ui.convertButton.clicked.connect(self.startConvertionInThread)

    def setFPS(self,i):
        self.fps = i
    
    def chooseFile(self):
        self.choosenfileOrFiles = QtWidgets.QFileDialog.getOpenFileNames(self, 'File(s)', 'c:\\',"Video (*.mp4 *.avi *.flv *.mkv)")
        str=""
        self.numberOfFiles=0
        if(self.choosenfileOrFiles[0] != []):
            for i in self.choosenfileOrFiles[0]:
                str = str + i + "\n\n"
                self.numberOfFiles+=1
        self.ui.chooseFileEditText.setText(str)
        self.ui.numberOfFilesLabel.setText(f"(0/{self.numberOfFiles})")

    def setSavePathText(self):
        self.savePathStr = QtWidgets.QFileDialog.getExistingDirectory(self, 'Choose save folder', None)
        self.ui.fileSavePathEditText.setText(self.savePathStr)

    def setProgress(self, value):
        if value == 1 or value == 20 or value == 40 or value == 60 or value == 80 or value == 100:
            self.ui.progressLabel.setText(str(value)+"%")
            

    def startConvertionInThread(self):
        if (self.savePathStr != "" and self.choosenfileOrFiles[0] != []):
            threading.Thread(target=self.convert, daemon=True).start()
        else:
            dlg = QtWidgets.QMessageBox(self)
            dlg.setWindowTitle("ERROR!")
            dlg.setText("ERROR!")
            dlg.exec()

            #if button == QtWidgets.QMessageBox.Ok:
                #print("OK!")

    def convert(self):
        counter=1
        for i in self.choosenfileOrFiles[0]:
            self.ui.numberOfFilesLabel.setText(f"{counter}/{self.numberOfFiles}")
            clip = VideoFileClip(i)
            indexOfFirstLetterInFileName = i[::-1].find("/")
            fileNameWithoutFileFormat = i[-indexOfFirstLetterInFileName:].split(".")[0]
            filePathAndName=self.savePathStr +"/"+ fileNameWithoutFileFormat + ".gif"
            clip.write_gif(filePathAndName, fps = self.fps, program = "ffmpeg", logger = self.log)
            clip.close()
            counter+=1
       

class MyBarLogger(ProgressBarLogger):

    def callback(self, **changes):
        for (parameter, value) in changes.items():
            print ('Parameter %s is now %s' % (parameter, value))

    def bars_callback(self, bar, attr, value,old_value=None):    
        percentage = (value / self.bars[bar]['total']) * 100
        Event("progress", int(percentage))

            


def program():
    program = QtWidgets.QApplication(sys.argv)
    win = App()
    win.observe("progress", win.setProgress)
    win.show()
    sys.exit(program.exec_())

program()