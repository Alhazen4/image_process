import cv2
import imutils

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QImage

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(619, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.brightness = QtWidgets.QSlider(self.centralwidget)
        self.brightness.setOrientation(QtCore.Qt.Vertical)
        self.brightness.setObjectName("brightness")

        self.horizontalLayout.addWidget(self.brightness)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("foto/baboon.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.blur = QtWidgets.QSlider(self.centralwidget)
        self.blur.setOrientation(QtCore.Qt.Vertical)
        self.blur.setObjectName("blur")

        self.horizontalLayout.addWidget(self.blur)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.open = QtWidgets.QPushButton(self.centralwidget)
        self.open.setObjectName("open")

        self.horizontalLayout_2.addWidget(self.open)

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setObjectName("save")

        self.horizontalLayout_2.addWidget(self.save)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")

        self.horizontalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")

        self.horizontalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        
        self.horizontalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")

        self.horizontalLayout_2.addWidget(self.pushButton_3)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.blur.valueChanged['int'].connect(self.blur_value)
        self.brightness.valueChanged['int'].connect(self.brightness_value)

        self.open.clicked.connect(self.openfile)
        self.save.clicked.connect(self.savefile)

        self.filename = None # Will hold the image address location
        self.tmp = None # Will hold the temporary image for display
        self.brightness_value_now = 0 # Updated brightness value
        self.blur_value_now = 0 # Updated blur value

    def openfile(self):
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv2.imread(self.filename)
        self.setPhoto(self.image)
      
    def setPhoto(self,image):
        self.tmp = image
        image = imutils.resize(image,width=640)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)		  
        image = QImage(frame, frame.shape[1],frame.shape[0],frame.strides[0],QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
  
    def savefile(self):
        filename = QFileDialog.getSaveFileName(filter="JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]
        
        cv2.imwrite(filename,self.tmp)
        print('Image saved as:',self.filename)

    def brightness_value(self,value):
        self.brightness_value_now = value
        print('Brightness: ',value)
        self.update()
		
		
    def blur_value(self,value):
            self.blur_value_now = value
            print('Blur: ',value)
            self.update()
	
	
    def changeBrightness(self,img,value):
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
        h,s,v = cv2.split(hsv)
        lim = 255 - value
        v[v>lim] = 255
        v[v<=lim] += value
        final_hsv = cv2.merge((h,s,v))
        img = cv2.cvtColor(final_hsv,cv2.COLOR_HSV2BGR)
        return img
		
    def changeBlur(self,img,value):
        kernel_size = (value+1,value+1) # +1 is to avoid 0
        img = cv2.blur(img,kernel_size)
        return img

    def update(self):
        img = self.changeBrightness(self.image,self.brightness_value_now)
        img = self.changeBlur(img,self.blur_value_now)
        self.setPhoto(img)
    

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open.setText(_translate("MainWindow", "Open"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
