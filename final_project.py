import cv2
import imutils

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
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

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setPlaceholderText("Value")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setContentsMargins(2, 2, 2, 2)
        
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setMinimumHeight(40)
        self.lineEdit.setMaximumWidth(150)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        
        self.horizontalLayout_3 = QtWidgets.QVBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QVBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.brightness = QtWidgets.QSlider(self.centralwidget)
        self.brightness.setOrientation(QtCore.Qt.Horizontal)
        self.brightness.setObjectName("brightness")
        
        self.blur = QtWidgets.QSlider(self.centralwidget)
        self.blur.setOrientation(QtCore.Qt.Horizontal)
        self.blur.setObjectName("blur")

        self.brightness_label = QLabel('')
        self.brightness_label.setText("Brightness")

        self.blur_label = QLabel('')
        self.blur_label.setText("Blur")

        self.rotate_label = QLabel('')
        self.rotate_label.setText("Rotation")
        
        self.contrast_label = QLabel('')
        self.contrast_label.setText("Contrast")
        
        self.rotate = QtWidgets.QSlider(self.centralwidget)
        self.rotate.setOrientation(QtCore.Qt.Horizontal)
        self.rotate.setObjectName("rotate")
        self.rotate.setMaximum(360)

        self.contrast = QtWidgets.QSlider(self.centralwidget)
        self.contrast.setOrientation(QtCore.Qt.Horizontal)
        self.contrast.setObjectName("brightness")
        self.contrast.setMaximum(254)
        self.contrast.setSliderPosition(127)
        
        self.horizontalLayout.addWidget(self.brightness_label)
        self.horizontalLayout.addWidget(self.brightness)
        self.horizontalLayout.addWidget(self.blur_label)
        self.horizontalLayout.addWidget(self.blur)
        self.horizontalLayout.addWidget(self.rotate_label)
        self.horizontalLayout.addWidget(self.rotate)
        self.horizontalLayout.addWidget(self.contrast_label)
        self.horizontalLayout.addWidget(self.contrast)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("Input your image by clicking the 'Open' button \n If the image doesn't exist and you start editing, the program will crash!")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        self.bri = QLabel('')
        self.bri.setAlignment(QtCore.Qt.AlignCenter)
        self.blu = QLabel('')
        self.blu.setAlignment(QtCore.Qt.AlignCenter)
        self.rot = QLabel('')
        self.rot.setAlignment(QtCore.Qt.AlignCenter)
        self.con = QLabel('')
        self.con.setAlignment(QtCore.Qt.AlignCenter)

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

        self.negative = QtWidgets.QPushButton(self.centralwidget)
        self.negative.setObjectName("negative")
        self.horizontalLayout_2.addWidget(self.negative)
        
        self.blackwhite = QtWidgets.QPushButton(self.centralwidget)
        self.blackwhite.setObjectName("blackwhite")
        self.horizontalLayout_2.addWidget(self.blackwhite)

        self.crop = QtWidgets.QPushButton(self.centralwidget)
        self.crop.setObjectName("crop")
        self.horizontalLayout_2.addWidget(self.crop)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.horizontalLayout.addWidget(self.blu)
        self.horizontalLayout.addWidget(self.bri)
        self.horizontalLayout.addWidget(self.rot)
        self.horizontalLayout.addWidget(self.con)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.blur.valueChanged['int'].connect(self.blur_value)
        self.brightness.valueChanged['int'].connect(self.brightness_value)
        self.rotate.valueChanged['int'].connect(self.rotate_value)
        self.contrast.valueChanged['int'].connect(self.contrast_value)

        self.open.clicked.connect(self.openfile)
        self.save.clicked.connect(self.savefile)
        self.negative.clicked.connect(self.negative_image)
        self.crop.clicked.connect(self.cropimg)
        self.blackwhite.clicked.connect(self.blwh)
        
        self.filename = None # Will hold the image address location
        self.tmp = None # Will hold the temporary image for display
        self.brightness_value_now = 0 # Updated brightness value
        self.blur_value_now = 0 # Updated blur value
        self.rotate_value_now = 0
        self.contrast_value_now = 127

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
        cv2.imwrite(filename, self.tmp)
        print('Image saved as:', self.filename)

    def brightness_value(self,value):
        self.brightness_value_now = value
        print('Brightness: ',value)
        self.update()
		
    def blur_value(self,value):
        self.blur_value_now = value
        print('Blur: ',value)
        self.update()

    def rotate_value(self, value):
        self.rotate_value_now = value
        print('Roteate:', value)
        self.update()

    def contrast_value(self, value):
        self.contrast_value_now = value
        print('Blur: ',value)
        self.update()

    def cropimg(self, img):
        # img = self.update()
        roi = cv2.selectROI(img)
        img = img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
        self.setPhoto(img)

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

    def changeRotation(self, img, value):
        height, width = img.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), value, 1)
        img = cv2.warpAffine(img, rotation_matrix, (width, height))
        return img

    def changeContrast(self, img, contrast):
        contrast = int((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127))  
        if contrast != 0:
            Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
            Gamma = 127 * (1 - Alpha)
            img = cv2.addWeighted(img, Alpha, img, 0, Gamma)
        return img

    def negative_image(self):
        try:
            input = int(self.lineEdit.text())
            img = cv2.threshold(self.image, input, 255, cv2.THRESH_BINARY)[1]
            self.setPhoto(img)
        except:
            print("Error")

    def blwh(self):
        try:
            input = int(self.lineEdit.text())
            gray_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            img = cv2.threshold(gray_img, input, 255, cv2.THRESH_BINARY)[1]  
            self.setPhoto(img)
        except:
            print("Error")

    def update(self):
        img = self.changeBrightness(self.image,self.brightness_value_now)
        img = self.changeBlur(img,self.blur_value_now)
        img = self.changeRotation(img, self.rotate_value_now)
        img = self.changeContrast(img, self.contrast_value_now)
  
        self.blu.setText('Brightness: %d' % self.brightness_value_now)
        self.bri.setText('Blur: %d' % self.blur_value_now)
        self.rot.setText('Rotation: %d' % self.rotate_value_now)
        self.con.setText('Contrast: %d' % self.contrast_value_now)
        
        self.setPhoto(img)
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowIcon(QtGui.QIcon('logo.png')) 
        MainWindow.setWindowTitle(_translate("MaPikcer", "MaPikcer"))
        self.open.setText(_translate("MainWindow", "Open"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.negative.setText(_translate("MainWindow", "Negative"))
        self.crop.setText(_translate("MainWindow", "Crop"))
        self.blackwhite.setText(_translate("MainWindow", "Black&White"))
        self.horizontalLayout.addWidget(self.lineEdit)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
