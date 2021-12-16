# Importing cv2 and imutils
import cv2
import imutils

# Importing PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage

# Class main window and UI for the application
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # Set the main window and main widget
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        # Set user input for "value" and its position
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setPlaceholderText("Value")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setMinimumHeight(40)
        self.lineEdit.setMaximumWidth(150)

        # Set user input for "width" and its position
        self.width = QtWidgets.QLineEdit(self.centralwidget)
        self.width.setPlaceholderText("Width")
        self.width.setObjectName("width")
        self.width.setAlignment(QtCore.Qt.AlignCenter)
        self.width.setMinimumHeight(40)
        self.width.setMaximumWidth(150)

        # Set user input for "height" and its position
        self.height = QtWidgets.QLineEdit(self.centralwidget)
        self.height.setPlaceholderText("Height")
        self.height.setObjectName("height")
        self.height.setAlignment(QtCore.Qt.AlignCenter)
        self.height.setMinimumHeight(40)
        self.height.setMaximumWidth(150)
        
        # Set a label and its position
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        
        # Set a horizontal layout
        self.horizontalLayout_3 = QtWidgets.QVBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QVBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Set a slider for brightness
        self.brightness = QtWidgets.QSlider(self.centralwidget)
        self.brightness.setOrientation(QtCore.Qt.Horizontal)
        self.brightness.setObjectName("brightness")
        
        # Set the slider for blur
        self.blur = QtWidgets.QSlider(self.centralwidget)
        self.blur.setOrientation(QtCore.Qt.Horizontal)
        self.blur.setObjectName("blur")

        # Set the labels for all value
        self.brightness_label = QLabel('')
        self.brightness_label.setText("Brightness")

        self.blur_label = QLabel('')
        self.blur_label.setText("Blur")

        self.rotate_label = QLabel('')
        self.rotate_label.setText("Rotation")
        
        self.contrast_label = QLabel('')
        self.contrast_label.setText("Contrast")
        
        # Set the slider for rotate
        self.rotate = QtWidgets.QSlider(self.centralwidget)
        self.rotate.setOrientation(QtCore.Qt.Horizontal)
        self.rotate.setObjectName("rotate")
        self.rotate.setMaximum(360)

        # Set the slider for brightness
        self.contrast = QtWidgets.QSlider(self.centralwidget)
        self.contrast.setOrientation(QtCore.Qt.Horizontal)
        self.contrast.setObjectName("brightness")
        self.contrast.setMaximum(254)
        self.contrast.setSliderPosition(127)
        
        # Set all widget to horizontal layout
        self.horizontalLayout.addWidget(self.brightness_label)
        self.horizontalLayout.addWidget(self.brightness)
        self.horizontalLayout.addWidget(self.blur_label)
        self.horizontalLayout.addWidget(self.blur)
        self.horizontalLayout.addWidget(self.rotate_label)
        self.horizontalLayout.addWidget(self.rotate)
        self.horizontalLayout.addWidget(self.contrast_label)
        self.horizontalLayout.addWidget(self.contrast)

        # Set the show label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("Input your image by clicking the 'Open' button")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)

        # Set the label for store the value
        self.bri = QLabel('')
        self.bri.setAlignment(QtCore.Qt.AlignCenter)
        self.blu = QLabel('')
        self.blu.setAlignment(QtCore.Qt.AlignCenter)
        self.rot = QLabel('')
        self.rot.setAlignment(QtCore.Qt.AlignCenter)
        self.con = QLabel('')
        self.con.setAlignment(QtCore.Qt.AlignCenter)

        # Set the horizontal layout of the widgets to grid layout
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Set the buttons
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

        self.resize = QtWidgets.QPushButton(self.centralwidget)
        self.resize.setObjectName("blackwhite")
        self.horizontalLayout_2.addWidget(self.resize)

        # Set the grid layout position
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.horizontalLayout.addWidget(self.blu)
        self.horizontalLayout.addWidget(self.bri)
        self.horizontalLayout.addWidget(self.rot)
        self.horizontalLayout.addWidget(self.con)

        # Set the slider and button to connect to the value
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.blur.valueChanged['int'].connect(self.valueBlur)
        self.brightness.valueChanged['int'].connect(self.valueBrightness)
        self.rotate.valueChanged['int'].connect(self.valueRotate)
        self.contrast.valueChanged['int'].connect(self.valueContrast)

        # Set the slider and button signal connection to the function
        self.open.clicked.connect(self.openFile)
        self.save.clicked.connect(self.saveFile)
        self.negative.clicked.connect(self.imgNegative)
        self.blackwhite.clicked.connect(self.blackWhite)
        self.resize.clicked.connect(self.imgResize)
        
        # Set the default value
        self.filename = None 
        self.tmp = None
        self.briVal = 0 
        self.bluVal = 0 
        self.rotVal = 0
        self.conVal = 127

    # Function to open file
    def openFile(self):
        try:
            self.filename = QFileDialog.getOpenFileName(filter = "Image (*.*)")[0]
            self.image = cv2.imread(self.filename)
            self.setPhoto(self.image)
        except:
            print("Open file canceled")
    
    # Function to set the photo from opened file to the show label
    def setPhoto(self, image):
        self.tmp = image
        image = imutils.resize(image, width = 400)
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)		  
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))
  
    # Function to save the file
    def saveFile(self):
        try:
            filename = QFileDialog.getSaveFileName(filter = "JPG(*.jpg);;PNG(*.png);;TIFF(*.tiff);;BMP(*.bmp)")[0]   
            cv2.imwrite(filename, self.tmp)
            print('Image saved as:', self.filename)
        except:
            print("Save file canceled")

    # Function to set and show the value of the brightness
    def valueBrightness(self, brightness):
        self.briVal = brightness
        print('Brightness:', brightness)
        self.imgUpdate()

    # Function to implement the value from slider to the picture
    def changeBrightness(self, img, brightness):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        lim = 255 - brightness # Each RGB light represent by number 255 as maximum value
        v[v > lim] = 255
        v[v <= lim] += brightness
        final_hsv = cv2.merge((h, s, v))
        img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
        return img
	
    # Function to set and show the value of the blur
    def valueBlur(self, blur):
        self.bluVal = blur
        print('Blur:', blur)
        self.imgUpdate()
    
    # Function to implement the value from slider to the picture
    def changeBlur(self, img, blur):
        kernel_size = (blur + 1, blur + 1) # kernel_size is represent of x and y of the picture
        img = cv2.blur(img, kernel_size)
        return img

    # Function to set and show the value of the rotate
    def valueRotate(self, rotate):
        self.rotVal = rotate
        print('Rotate:', rotate)
        self.imgUpdate()

    # Function to implement the value from slider to the picture
    def changeRotate(self, img, rotate):
        height, width = img.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), rotate, 1) #((center), angle, scale)
        img = cv2.warpAffine(img, rotation_matrix, (width, height)) # Applies an affine transformation(rotating, miroring, scaling, etc)
        #warpAffine(source file, transformation, size of the output)
        return img

    # Function to set and show the value of the contrast
    def valueContrast(self, contrast):
        self.conVal = contrast
        print('Contrast:', contrast)
        self.imgUpdate()

    # Function to implement the value from slider to the picture
    def changeContrast(self, img, contrast):
        contrast = float((contrast - 0) * (127 - (-127)) / (254 - 0) + (-127)) # 127 the center value in order not to overvalue
        if contrast != 0:
            Alpha = float(131 * (contrast + 127)) / (127 * (131 - contrast))
            Gamma = 127 * (1 - Alpha)
            img = cv2.addWeighted(img, Alpha, img, 0, Gamma)
        return img

    # Function to set and show the picture in negative mode
    def imgNegative(self):
        try:
            img = cv2.bitwise_not(self.image)
            self.setPhoto(img)
        except:
            print("Must Input number")

    # Function to set and show the picture in black and white mode
    def blackWhite(self):
        try:
            input = int(self.lineEdit.text())
            gray_img = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            img = cv2.threshold(gray_img, input, 255, cv2.THRESH_BINARY)[1]  
            self.setPhoto(img)
        except:
            print("Must Input number")

    # Function to set and show the picture in resized mode
    def imgResize(self):
        try:
            width = int(self.width.text())
            height = int(self.height.text())
            dim = (width, height) # dimension
            resize = cv2.resize(self.image, dim, interpolation = cv2.INTER_AREA)
            self.setPhoto(resize)
        except:
            print("Must Input number")

    # Function to update and show the default value of every picture mode
    def imgUpdate(self):
        try:
            img = self.changeBrightness(self.image, self.briVal)
            img = self.changeBlur(img, self.bluVal)
            img = self.changeRotate(img, self.rotVal)
            img = self.changeContrast(img, self.conVal)
            self.blu.setText('Brightness: %d' % self.briVal)
            self.bri.setText('Blur: %d' % self.bluVal)
            self.rot.setText('Rotation: %d' % self.rotVal)
            self.con.setText('Contrast: %d' % self.conVal)
            self.setPhoto(img)
        except:
            print("Insert the image")
  
    # Function to set the window title and logo, also set the label of every button
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowIcon(QtGui.QIcon('logo.png')) 
        MainWindow.setWindowTitle(_translate("MaPikcer", "MaPikcer"))
        self.open.setText(_translate("MainWindow", "Open"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.negative.setText(_translate("MainWindow", "Negative"))
        self.resize.setText(_translate("MainWindow", "Resize"))
        self.blackwhite.setText(_translate("MainWindow", "Black&White"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout.addWidget(self.width)
        self.horizontalLayout.addWidget(self.height)

# Function to start the application
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
