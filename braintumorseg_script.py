# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'es.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import numpy as np
global a
import glob, os, os.path
import cv2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900,600)
        MainWindow.setStyleSheet("background-color: #005bea;")
        MainWindow.setWindowIcon(QIcon("C:\\Users\HASSAN\Desktop\doc.png"))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        
        # Get screen geometry
        screen_geometry = QtWidgets.QDesktopWidget().screenGeometry()
        screen_center = screen_geometry.center()

        frame_width = screen_geometry.width() * 8 // 10  # Integer division
        frame_height = screen_geometry.height() * 6 // 10  # Integer division

        # Get the frame position to center it
        frame_x = screen_center.x() - frame_width // 2
        frame_y = screen_center.y() - frame_height // 2
        
        self.frame.setGeometry(QtCore.QRect(frame_x, frame_y, frame_width, frame_height))
        self.frame.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.630318, y1:0.392, x2:0.068, y2:0, stop:0.551136 #4facfe, stop:1 #00f2fe);\n"
                                 "border-radius: 25px;\n"
                                 "border: 2px solid #00c6fb;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.image_dir = "C://Users/HASSAN/OneDrive/Python/test"  # Define image directory
        
        self.slctimg = QtWidgets.QPushButton(self.frame)
        self.slctimg.setGeometry(QtCore.QRect(600, 10, 171, 61))
        self.slctimg.setStyleSheet("color:white;\n"
                                   "font: 14pt \"Gadugi\";\n"
                                   "border-radius: 20px;\n"
                                   "border: 2px solid #00c6fb;\n"
                                   "background-color:#005bea;")
      
        self.slctimg.setObjectName("slctimg")
        
        self.rgbtgray = QtWidgets.QPushButton(self.frame)
        self.rgbtgray.setGeometry(QtCore.QRect(600, 80, 171, 61))
        self.rgbtgray.setStyleSheet("color:white;\n"
                                    "font: 14pt \"Gadugi\";\n"
                                    "   border-radius: 20px;\n"
                                    "    border: 2px solid #00c6fb;\n"
                                    "background-color:#005bea;\n"
                                    "width:171px;\n"
                                    "height:61px;")
        self.rgbtgray.setObjectName("rgbtgray")
        self.bilfil = QtWidgets.QPushButton(self.frame)
        self.bilfil.setGeometry(QtCore.QRect(600, 150, 171, 61))
        self.bilfil.setStyleSheet("color:white;\n"
                                  "font: 14pt \"Gadugi\";\n"
                                  "   border-radius: 20px;\n"
                                  "    border: 2px solid #00c6fb;\n"
                                  "background-color:#005bea;\n"
                                  "width:171px;\n"
                                  "height:61px;")
        self.bilfil.setObjectName("bilfil")
        self.medfil = QtWidgets.QPushButton(self.frame)
        self.medfil.setGeometry(QtCore.QRect(600, 220, 171, 61))
        self.medfil.setStyleSheet("color:white;\n"
                                  "font: 14pt \"Gadugi\";\n"
                                  "   border-radius: 20px;\n"
                                  "    border: 2px solid #00c6fb;\n"
                                  "background-color:#005bea;\n"
                                  "width:171px;\n"
                                  "height:61px;")
        self.medfil.setObjectName("medfil")
        self.gaufil = QtWidgets.QPushButton(self.frame)
        self.gaufil.setGeometry(QtCore.QRect(390, 150, 111, 41))
        self.gaufil.setStyleSheet("background-color: #008CBA;\n"
                                  "text-align: center;\n"
                                  "\n"
                                  "")
        self.gaufil.setObjectName("gaufil")
        self.thres = QtWidgets.QPushButton(self.frame)
        self.thres.setGeometry(QtCore.QRect(600, 290, 171, 61))
        self.thres.setStyleSheet("color:white;\n"
                                 "font: 14pt \"Gadugi\";\n"
                                 "   border-radius: 20px;\n"
                                 "    border: 2px solid #00c6fb;\n"
                                 "background-color:#005bea;\n"
                                 "width:171px;\n"
                                 "height:61px;")
        self.thres.setObjectName("thres")
        self.dilate = QtWidgets.QPushButton(self.frame)
        self.dilate.setGeometry(QtCore.QRect(600, 360, 171, 61))
        self.dilate.setStyleSheet("color:white;\n"
                                  "font: 14pt \"Gadugi\";\n"
                                  "   border-radius: 20px;\n"
                                  "    border: 2px solid #00c6fb;\n"
                                  "background-color:#005bea;\n"
                                  "width:171px;\n"
                                  "height:61px;")
        self.dilate.setObjectName("dilate")
        self.morpho = QtWidgets.QPushButton(self.frame)
        self.morpho.setGeometry(QtCore.QRect(600, 430, 171, 61))
        self.morpho.setStyleSheet("color:white;\n"
                                  "font: 14pt \"Gadugi\";\n"
                                  "   border-radius: 20px;\n"
                                  "    border: 2px solid #00c6fb;\n"
                                  "background-color:#005bea;\n"
                                  "width:171px;\n"
                                  "height:61px;")
        self.morpho.setObjectName("morpho")
        self.addcol = QtWidgets.QPushButton(self.frame)
        self.addcol.setGeometry(QtCore.QRect(600, 500, 171, 61))
        self.addcol.setStyleSheet("color:white;\n"
                                  "font: 14pt \"Gadugi\";\n"
                                  "   border-radius: 20px;\n"
                                  "    border: 2px solid #00c6fb;\n"
                                  "background-color:#005bea;\n"
                                  "width:171px;\n"
                                  "height:61px;")
        self.addcol.setObjectName("addcol")
        self.savimg = QtWidgets.QPushButton(self.frame)
        self.savimg.setGeometry(QtCore.QRect(600, 570, 171, 61))
        self.savimg.setStyleSheet("color:white;\n"
                                  "font: 14pt \"Gadugi\";\n"
                                  "   border-radius: 20px;\n"
                                  "    border: 2px solid #00c6fb;\n"
                                  "background-color:#005bea;\n"
                                  "width:171px;\n"
                                  "height:61px;")
        self.savimg.setObjectName("savimg")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 90, 261, 421))
        self.label.setStyleSheet("background-color: rgb(218, 218, 218);\n"
                                 "   border-radius: 20px;\n"
                                 "    border: 2px solid #00c6fb;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(299, 90, 261, 421))
        self.label_2.setStyleSheet("background-color: rgb(218, 218, 218);\n"
                                   "   border-radius: 20px;\n"
                                   "    border: 2px solid #00c6fb;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.titlelbl = QtWidgets.QLabel(self.centralwidget)
        self.titlelbl.setGeometry(QtCore.QRect(450, 10, 501, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.titlelbl.setFont(font)
        self.titlelbl.setStyleSheet("opacity:0.6;\n"
                                    "font: 26pt \"MS Shell Dlg 2\";\n"
                                    "color: rgb(216, 216, 216);")
        self.titlelbl.setObjectName("titlelbl")
        MainWindow.setCentralWidget(self.centralwidget)

         # Define and set up other buttons similarly
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.setWindowTitle('Image processing tool')
        error_dialog.setWindowIcon(QIcon('C:\\Users\HASSAN\Desktop\error.png'))
        error_dialog.showMessage('Please click the buttons in Sequential order to proceed!')
        error_dialog.exec()


        path = "C://Users/HASSAN/OneDrive/Python/test"

        filelist = glob.glob(os.path.join(path, "*.png"))
        for f in filelist:
            os.remove(f)
            print('deleted')

        self.original_image = None
        self.segmented_image = None

        self.slctimg.clicked.connect(self.setImage)
        self.rgbtgray.clicked.connect(self.filter1)
        self.bilfil.clicked.connect(self.filter2)
        self.medfil.clicked.connect(self.filter3)
        self.thres.clicked.connect(self.threshing)
        self.dilate.clicked.connect(self.dilation)
        self.morpho.clicked.connect(self.contouring)
        self.addcol.clicked.connect(self.applyingcolor)
        self.savimg.clicked.connect(self.saving)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tumor Segmentation Panel"))
        self.slctimg.setText(_translate("MainWindow", "Select Image"))
        self.rgbtgray.setText(_translate("MainWindow", "Bilateral Filter"))
        self.bilfil.setText(_translate("MainWindow", "Median Filter"))
        self.medfil.setText(_translate("MainWindow", "Gaussian Filter"))
        self.thres.setText(_translate("MainWindow", "Thresholding"))
        self.dilate.setText(_translate("MainWindow", "Dilation"))
        self.morpho.setText(_translate("MainWindow", "Morphology"))
        self.addcol.setText(_translate("MainWindow", "Add Color Map"))
        self.savimg.setText(_translate("MainWindow", "Save Image"))
        self.titlelbl.setText(_translate("MainWindow", "Tumor Segmentation Panel"))

    def setImage(self):
        global a
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "D://BrainTumorSegmentation/resources/",
                                                            "Image Files (*.png *.jpg *jpeg *.bmp)")  # Ask for file

        if fileName:
            self.a = fileName

            pixmap = QtGui.QPixmap(fileName)  # Setup pixmap with the provided image
            pixmap = pixmap.scaled(self.label.width(), self.label.height(),
                                   QtCore.Qt.KeepAspectRatio)  # Scale pixmap
            self.label.setPixmap(pixmap)  # Set the pixmap onto the label
            self.label.setAlignment(QtCore.Qt.AlignCenter)  # Align the label to center

    def filter1(self):
        global a
        
        if a:
            img = cv2.imread(a)
            grey = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            self.bilateral = cv2.bilateralFilter(grey, 2, 50, 50)
            
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(self.bilateral.data, self.bilateral.shape[1], self.bilateral.shape[0],
                                                          self.bilateral.strides[0], QtGui.QImage.Format_Grayscale8))
            pixmap = pixmap.scaled(self.label_2.width(), self.label_2.height(),
                                   QtCore.Qt.KeepAspectRatio)
            self.label_2.setPixmap(pixmap)
            
    def filter2(self):
       if self.bilateral is not None:
            self.median = cv2.medianBlur(self.bilateral, 5)
            
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(self.median.data, self.median.shape[1], self.median.shape[0],
                                                          self.median.strides[0], QtGui.QImage.Format_Grayscale8))
            pixmap = pixmap.scaled(self.label_2.width(), self.label_2.height(),
                                   QtCore.Qt.KeepAspectRatio)
            self.label_2.setPixmap(pixmap)
    
    def filter3(self):
        if self.median is not None:
            self.Gaussian = cv2.GaussianBlur(self.median, (5, 5), cv2.BORDER_CONSTANT)
            
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(self.Gaussian.data, self.Gaussian.shape[1], self.Gaussian.shape[0],
                                                          self.Gaussian.strides[0], QtGui.QImage.Format_Grayscale8))
            pixmap = pixmap.scaled(self.label_2.width(), self.label_2.height(),
                                   QtCore.Qt.KeepAspectRatio)
            self.label_2.setPixmap(pixmap)
    
    def threshing(self):
        if self.Gaussian is not None:
            # Apply adaptive thresholding
            thresh1 = cv2.adaptiveThreshold(self.Gaussian, 127, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
            
            self.segmented_image = thresh1  # Update segmented_image with the thresholded image
    
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(thresh1.data, thresh1.shape[1], thresh1.shape[0],
                                                          thresh1.strides[0], QtGui.QImage.Format_Grayscale8))
            pixmap = pixmap.scaled(self.label_2.width(), self.label_2.height(),
                                   QtCore.Qt.KeepAspectRatio)
            self.label_2.setPixmap(pixmap)

    def dilation(self):
        if self.segmented_image is not None:
            kernel = np.ones((5, 5), np.uint8)
            opening1 = cv2.dilate(self.segmented_image, kernel, iterations=1)
            opening2 = cv2.morphologyEx(opening1, cv2.MORPH_CLOSE, kernel)
            
            self.segmented_image = opening2
            
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(opening2.data, opening2.shape[1], opening2.shape[0],
                                                          opening2.strides[0], QtGui.QImage.Format_Grayscale8))
            pixmap = pixmap.scaled(self.label_2.width(), self.label_2.height(),
                                   QtCore.Qt.KeepAspectRatio)
            self.label_2.setPixmap(pixmap)
    
    def contouring(self):
        if a is not None and self.segmented_image is not None:
            # Read the image
            image_copy = cv2.imread(a)
            
            print(image_copy.shape, 'img')
            print(self.segmented_image.shape, 'seg')  # Corrected line
            
            contours, hierarchy = cv2.findContours(self.segmented_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[-2:]
    
            # Create a copy of the image
            image_copy_with_contours = image_copy.copy()
    
            b = cv2.drawContours(image_copy_with_contours, contours, -1, (0, 0, 255), 3)
    
            # Resize the images to have the same dimensions
            b_resized = cv2.resize(b, (self.segmented_image.shape[1], self.segmented_image.shape[0]))
    
            # Convert the grayscale image to color
            segmented_color = cv2.cvtColor(self.segmented_image, cv2.COLOR_GRAY2BGR)
            
            
            # Perform weighted addition
            dst = cv2.addWeighted(segmented_color, 0.7, b_resized, 0.3, 0)
    
            self.colorimg = dst
            
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(dst.data, dst.shape[1], dst.shape[0],
                                                          dst.strides[0], QtGui.QImage.Format_RGB888))  # Format_RGB888 for color image
            pixmap = pixmap.scaled(self.label_2.width(), self.label_2.height(),
                                   QtCore.Qt.KeepAspectRatio)
            self.label_2.setPixmap(pixmap)
   
    def applyingcolor(self):
        if self.colorimg is not None:
            img3 = cv2.applyColorMap(self.colorimg, cv2.COLORMAP_HOT)
            self.img3 = img3
            
            pixmap = QtGui.QPixmap.fromImage(QtGui.QImage(img3.data, img3.shape[1], img3.shape[0],
                                                          img3.strides[0], QtGui.QImage.Format_RGB888))
            pixmap = pixmap.scaled(self.label_2.width(), self.label_2.height(),
                                   QtCore.Qt.KeepAspectRatio)
            self.label_2.setPixmap(pixmap)
    
    def saving(self):
        if self.img3 is not None:
            fname, _ = QtWidgets.QFileDialog.getSaveFileName(None, 'Save Image',
                                                            self.image_dir, "Image files (*.jpg)")
            if fname:
                cv2.imwrite(fname, self.img3)
            else:
                print('Image not saved')
    
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showMaximized()
    MainWindow.show()
    sys.exit(app.exec_())