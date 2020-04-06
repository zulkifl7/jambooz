# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Jambooz-main .ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainPage(object):


    def setupUi(self, MainPage):
        MainPage.setObjectName("MainPage")
        MainPage.resize(342, 231)
        MainPage.setMouseTracking(False)

        # setup icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/20200227_152412_4fk_icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainPage.setWindowIcon(icon)

        # set the tab shaape
        MainPage.setTabShape(QtWidgets.QTabWidget.Rounded)


        self.centralwidget = QtWidgets.QWidget(MainPage)
        self.centralwidget.setObjectName("centralwidget")

        # Add button
        self.AddButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddButton.setGeometry(QtCore.QRect(20, 40, 100, 31))
        self.AddButton.setObjectName("AddButton")

        # Categories button
        self.CategoriesButton = QtWidgets.QPushButton(self.centralwidget)
        self.CategoriesButton.setGeometry(QtCore.QRect(130, 40, 100, 31))
        self.CategoriesButton.setObjectName("CategoriesButton")

        # search bar
        self.SearchBar = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchBar.setGeometry(QtCore.QRect(20, 110, 241, 33))
        self.SearchBar.setText("")
        self.SearchBar.setCursorPosition(0)
        self.SearchBar.setObjectName("SearchBar")

        # search text before the search bar
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 90, 67, 19))
        self.label.setObjectName("label")

        # the box around the search bar
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(81, 90, 231, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(303, 98, 20, 53))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 150, 304, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(10, 110, 3, 40))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        # set a label with text (search with serial number)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 211, 19))
        self.label_2.setObjectName("label_2")

        # search icon
        self.SearchButton = QtWidgets.QLabel(self.centralwidget)
        self.SearchButton.setGeometry(QtCore.QRect(270, 111, 30, 29))
        self.SearchButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.SearchButton.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SearchButton.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.SearchButton.setText("")
        self.SearchButton.setPixmap(QtGui.QPixmap("icons/index.png"))
        self.SearchButton.setScaledContents(True)
        self.SearchButton.setWordWrap(True)
        self.SearchButton.setOpenExternalLinks(False)
        self.SearchButton.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.SearchButton.setObjectName("SearchButton")


        MainPage.setCentralWidget(self.centralwidget)

        # menu bar
        self.menubar = QtWidgets.QMenuBar(MainPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 342, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainPage.setMenuBar(self.menubar)

        # status bar
        self.statusbar = QtWidgets.QStatusBar(MainPage)
        self.statusbar.setObjectName("statusbar")
        MainPage.setStatusBar(self.statusbar)
        self.actionAdd_Item = QtWidgets.QAction(MainPage)
        self.actionAdd_Item.setObjectName("actionAdd_Item")
        self.actionAdd_Item.setShortcut('Ctrl+I')

        self.actionCategories = QtWidgets.QAction(MainPage)
        self.actionCategories.setObjectName("actionCategories")
        self.actionCategories.setShortcut('Ctrl+G')

        self.actionSearch = QtWidgets.QAction(MainPage)
        self.actionSearch.setObjectName("actionSearch")
        self.actionSearch.setShortcut('Ctrl+O')

        self.actionLog_Out = QtWidgets.QAction(MainPage)
        self.actionLog_Out.setObjectName("actionLog_Out")
        self.menuFile.addAction(self.actionAdd_Item)
        self.menuFile.addAction(self.actionCategories)
        self.menuFile.addAction(self.actionSearch)
        self.menuFile.addAction(self.actionLog_Out)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainPage)
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "Jambooz-main"))
        self.AddButton.setText(_translate("MainPage", "Add Item"))
        self.CategoriesButton.setText(_translate("MainPage", "Cetagories"))
        self.label.setText(_translate("MainPage", "Search"))
        self.label_2.setText(_translate("MainPage", "(search with the serial number)"))
        self.menuFile.setTitle(_translate("MainPage", "File"))
        self.actionAdd_Item.setText(_translate("MainPage", "Add Item"))
        self.actionAdd_Item.setShortcut(_translate("MainPage", "Ctrl+I"))
        self.actionCategories.setText(_translate("MainPage", "Categories"))
        self.actionSearch.setText(_translate("MainPage", "Search"))
        self.actionLog_Out.setText(_translate("MainPage", "Log Out"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainPage = QtWidgets.QMainWindow()
    ui = Ui_MainPage()
    ui.setupUi(MainPage)
    MainPage.show()
    sys.exit(app.exec_())
