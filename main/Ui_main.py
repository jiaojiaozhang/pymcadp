# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\tmp\fossil\wd\pymcadp\main\main.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuCalculator = QtWidgets.QMenu(self.menuBar)
        self.menuCalculator.setObjectName("menuCalculator")
        self.menuUtilities = QtWidgets.QMenu(self.menuBar)
        self.menuUtilities.setObjectName("menuUtilities")
        self.menuDesign = QtWidgets.QMenu(self.menuBar)
        self.menuDesign.setObjectName("menuDesign")
        self.menuWeb = QtWidgets.QMenu(self.menuBar)
        self.menuWeb.setObjectName("menuWeb")
        MainWindow.setMenuBar(self.menuBar)
        self.actionSimple = QtWidgets.QAction(MainWindow)
        self.actionSimple.setObjectName("actionSimple")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionEngr_Calculator = QtWidgets.QAction(MainWindow)
        self.actionEngr_Calculator.setObjectName("actionEngr_Calculator")
        self.actionGrouping = QtWidgets.QAction(MainWindow)
        self.actionGrouping.setObjectName("actionGrouping")
        self.actionHP_11C_Calculator = QtWidgets.QAction(MainWindow)
        self.actionHP_11C_Calculator.setObjectName("actionHP_11C_Calculator")
        self.actionSpur_Gear_Width = QtWidgets.QAction(MainWindow)
        self.actionSpur_Gear_Width.setObjectName("actionSpur_Gear_Width")
        self.actionCMSimfly = QtWidgets.QAction(MainWindow)
        self.actionCMSimfly.setObjectName("actionCMSimfly")
        self.actionPyGrouf = QtWidgets.QAction(MainWindow)
        self.actionPyGrouf.setObjectName("actionPyGrouf")
        self.actionGraphics_Viewer = QtWidgets.QAction(MainWindow)
        self.actionGraphics_Viewer.setObjectName("actionGraphics_Viewer")
        self.action2D_cad = QtWidgets.QAction(MainWindow)
        self.action2D_cad.setObjectName("action2D_cad")
        self.actionPaint = QtWidgets.QAction(MainWindow)
        self.actionPaint.setObjectName("actionPaint")
        self.actioncal_ex1 = QtWidgets.QAction(MainWindow)
        self.actioncal_ex1.setObjectName("actioncal_ex1")
        self.menuFile.addAction(self.actionQuit)
        self.menuCalculator.addAction(self.actionSimple)
        self.menuCalculator.addAction(self.actionEngr_Calculator)
        self.menuCalculator.addAction(self.actionHP_11C_Calculator)
        self.menuCalculator.addAction(self.actioncal_ex1)
        self.menuUtilities.addAction(self.actionGrouping)
        self.menuUtilities.addAction(self.actionGraphics_Viewer)
        self.menuDesign.addAction(self.actionSpur_Gear_Width)
        self.menuDesign.addAction(self.action2D_cad)
        self.menuDesign.addAction(self.actionPaint)
        self.menuWeb.addAction(self.actionCMSimfly)
        self.menuWeb.addAction(self.actionPyGrouf)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuCalculator.menuAction())
        self.menuBar.addAction(self.menuUtilities.menuAction())
        self.menuBar.addAction(self.menuDesign.menuAction())
        self.menuBar.addAction(self.menuWeb.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuCalculator.setTitle(_translate("MainWindow", "Calculator"))
        self.menuUtilities.setTitle(_translate("MainWindow", "Utilities"))
        self.menuDesign.setTitle(_translate("MainWindow", "Design"))
        self.menuWeb.setTitle(_translate("MainWindow", "Web"))
        self.actionSimple.setText(_translate("MainWindow", "Simple Calculator"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionEngr_Calculator.setText(_translate("MainWindow", "Engr Calculator"))
        self.actionGrouping.setText(_translate("MainWindow", "Grouping"))
        self.actionHP_11C_Calculator.setText(_translate("MainWindow", "HP 11C Calculator"))
        self.actionSpur_Gear_Width.setText(_translate("MainWindow", "Spur Gear Width"))
        self.actionCMSimfly.setText(_translate("MainWindow", "CMSimfly"))
        self.actionPyGrouf.setText(_translate("MainWindow", "PyGrouf"))
        self.actionGraphics_Viewer.setText(_translate("MainWindow", "Graphics Viewer"))
        self.action2D_cad.setText(_translate("MainWindow", "2D cad"))
        self.actionPaint.setText(_translate("MainWindow", "Paint"))
        self.actioncal_ex1.setText(_translate("MainWindow", "cal_ex1"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

