# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'jambooz_login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from jambooz_main import Ui_MainPage





class Ui_MainWindow(object):
    

    def LogIn(self):
        text = self.lineEdit.text()
        if text == 'jambooz123':
            self.MainPage = QtWidgets.QMainWindow()
            self.ui = Ui_MainPage()
            self.ui.setupUi(self.MainPage)
            self.MainPage.show()

            
        else:
            self.msg = QMessageBox()
            self.msg.setIcon(QMessageBox.Warning)
            self.msg.setText("Incorrect Password")
            self.msg.setWindowTitle("access denied")
            self.det = '''forgot password...??
            contact the author
            Email: abdullazulkifl7@gmail.com
            phone: +94765353503''' 
            self.msg.setDetailedText(self.det)
            self.msg.setStandardButtons(QMessageBox.Retry)
            x = self.msg.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(245, 244)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))

        # setting the window icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/20200227_152412_4fk_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)


        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # adding jambooz logo on the screen
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 20, 191, 71))
        self.label1.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label1.setMouseTracking(True)
        self.label1.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label1.setTextFormat(QtCore.Qt.PlainText)
        self.label1.setPixmap(QtGui.QPixmap("photos/20200227_152427.jpg"))
        self.label1.setScaledContents(True)
        self.label1.setWordWrap(False)
        self.label1.setObjectName("label1")

        # adding the label with text password
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(30, 100, 67, 19))
        self.label2.setObjectName("label2")

        # adding the password field
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(30, 120, 191, 21))
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit.setObjectName("lineEdit")

        
        # thin box frame around the password field
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(110, 110, 121, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(13, 120, 20, 31))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(220, 110, 20, 41))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(24, 140, 207, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        # creating the log in button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 160, 100, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.LogIn)

        # menu bar
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 245, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        MainWindow.setCentralWidget(self.centralwidget) # setting the width to the center
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jambooz-login"))
        self.label2.setText(_translate("MainWindow", "password"))
        
        self.pushButton.setText(_translate("MainWindow", "Log In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
