# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Code\GitHub\Algorithm-Homework\HW2\CP.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys
#from myview import MyView

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainWindow(object):
    def confirmFunc(self):
        if self.HandAppend.isChecked() == True:
            self.RandomAppend.setChecked(False)
        else:
            self.HandAppend.setChecked(False)
            self.PointNum.setEnabled(True)

    def setupUi(self, mainWindow):
        mainWindow.setObjectName(_fromUtf8("mainWindow"))
        mainWindow.setEnabled(True)
        mainWindow.resize(992, 869)
        self.centralwidget = QtGui.QWidget(mainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.PointZone = QtGui.QGraphicsView(self.centralwidget)
        self.PointZone.setGeometry(QtCore.QRect(10, 20, 800, 800))
        self.PointZone.setMinimumSize(QtCore.QSize(800, 800))
        self.PointZone.setMaximumSize(QtCore.QSize(800, 800))
        self.PointZone.setObjectName(_fromUtf8("PointZone"))
        self.ball_x = QtGui.QLineEdit(self.centralwidget)
        self.ball_x.setEnabled(False)
        self.ball_x.setGeometry(QtCore.QRect(846, 200, 58, 20))
        self.ball_x.setObjectName(_fromUtf8("ball_x"))
        self.ball_mouse = QtGui.QLabel(self.centralwidget)
        self.ball_mouse.setGeometry(QtCore.QRect(828, 180, 121, 16))
        self.ball_mouse.setObjectName(_fromUtf8("ball_mouse"))
        self.ball_y = QtGui.QLineEdit(self.centralwidget)
        self.ball_y.setEnabled(False)
        self.ball_y.setGeometry(QtCore.QRect(928, 200, 58, 20))
        self.ball_y.setObjectName(_fromUtf8("ball_y"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(910, 200, 12, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(828, 200, 12, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.AppendFunc = QtGui.QGroupBox(self.centralwidget)
        self.AppendFunc.setGeometry(QtCore.QRect(830, 20, 120, 80))
        self.AppendFunc.setObjectName(_fromUtf8("AppendFunc"))
        self.HandAppend = QtGui.QRadioButton(self.AppendFunc)
        self.HandAppend.setGeometry(QtCore.QRect(10, 20, 89, 16))
        self.HandAppend.setObjectName(_fromUtf8("HandAppend"))
        self.RandomAppend = QtGui.QRadioButton(self.AppendFunc)
        self.RandomAppend.setGeometry(QtCore.QRect(10, 50, 89, 16))
        self.RandomAppend.setObjectName(_fromUtf8("RandomAppend"))
        self.ConfirmAppendFunc = QtGui.QPushButton(self.centralwidget)
        self.ConfirmAppendFunc.setGeometry(QtCore.QRect(850, 110, 75, 23))
        self.ConfirmAppendFunc.setObjectName(_fromUtf8("ConfirmAppendFunc"))
        self.ball_mouse_2 = QtGui.QLabel(self.centralwidget)
        self.ball_mouse_2.setGeometry(QtCore.QRect(830, 150, 121, 16))
        self.ball_mouse_2.setObjectName(_fromUtf8("ball_mouse_2"))
        self.ball_mouse_3 = QtGui.QLabel(self.centralwidget)
        self.ball_mouse_3.setGeometry(QtCore.QRect(830, 230, 121, 16))
        self.ball_mouse_3.setObjectName(_fromUtf8("ball_mouse_3"))
        self.PointNum = QtGui.QLineEdit(self.centralwidget)
        self.PointNum.setEnabled(False)
        self.PointNum.setGeometry(QtCore.QRect(890, 230, 58, 20))
        self.PointNum.setObjectName(_fromUtf8("PointNum"))
        self.ball_mouse_4 = QtGui.QLabel(self.centralwidget)
        self.ball_mouse_4.setGeometry(QtCore.QRect(830, 290, 121, 16))
        self.ball_mouse_4.setObjectName(_fromUtf8("ball_mouse_4"))
        self.ball_mouse_5 = QtGui.QLabel(self.centralwidget)
        self.ball_mouse_5.setGeometry(QtCore.QRect(830, 320, 121, 16))
        self.ball_mouse_5.setObjectName(_fromUtf8("ball_mouse_5"))
        self.RandomPointNum = QtGui.QLineEdit(self.centralwidget)
        self.RandomPointNum.setEnabled(True)
        self.RandomPointNum.setGeometry(QtCore.QRect(890, 320, 58, 20))
        self.RandomPointNum.setObjectName(_fromUtf8("RandomPointNum"))
        self.CPFunc = QtGui.QGroupBox(self.centralwidget)
        self.CPFunc.setGeometry(QtCore.QRect(830, 380, 120, 80))
        self.CPFunc.setObjectName(_fromUtf8("CPFunc"))
        self.BruteCP = QtGui.QRadioButton(self.CPFunc)
        self.BruteCP.setGeometry(QtCore.QRect(10, 20, 89, 16))
        self.BruteCP.setObjectName(_fromUtf8("BruteCP"))
        self.RandomAppend_2 = QtGui.QRadioButton(self.CPFunc)
        self.RandomAppend_2.setGeometry(QtCore.QRect(10, 50, 89, 16))
        self.RandomAppend_2.setObjectName(_fromUtf8("RandomAppend_2"))
        self.StartCP = QtGui.QPushButton(self.centralwidget)
        self.StartCP.setGeometry(QtCore.QRect(850, 470, 75, 23))
        self.StartCP.setObjectName(_fromUtf8("StartCP"))
        self.ball_mouse_6 = QtGui.QLabel(self.centralwidget)
        self.ball_mouse_6.setGeometry(QtCore.QRect(820, 520, 121, 16))
        self.ball_mouse_6.setObjectName(_fromUtf8("ball_mouse_6"))
        self.FuncTime = QtGui.QLineEdit(self.centralwidget)
        self.FuncTime.setEnabled(False)
        self.FuncTime.setGeometry(QtCore.QRect(910, 520, 58, 20))
        self.FuncTime.setObjectName(_fromUtf8("FuncTime"))
        self.Point2 = QtGui.QLineEdit(self.centralwidget)
        self.Point2.setEnabled(False)
        self.Point2.setGeometry(QtCore.QRect(918, 570, 58, 20))
        self.Point2.setObjectName(_fromUtf8("Point2"))
        self.Point1 = QtGui.QLineEdit(self.centralwidget)
        self.Point1.setEnabled(False)
        self.Point1.setGeometry(QtCore.QRect(836, 570, 58, 20))
        self.Point1.setObjectName(_fromUtf8("Point1"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(818, 570, 12, 20))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.ball_mouse_7 = QtGui.QLabel(self.centralwidget)
        self.ball_mouse_7.setGeometry(QtCore.QRect(818, 550, 121, 16))
        self.ball_mouse_7.setObjectName(_fromUtf8("ball_mouse_7"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(900, 570, 12, 20))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.ShortDis = QtGui.QLineEdit(self.centralwidget)
        self.ShortDis.setEnabled(False)
        self.ShortDis.setGeometry(QtCore.QRect(880, 610, 91, 20))
        self.ShortDis.setObjectName(_fromUtf8("ShortDis"))
        self.ball_mouse_8 = QtGui.QLabel(self.centralwidget)
        self.ball_mouse_8.setGeometry(QtCore.QRect(820, 610, 121, 16))
        self.ball_mouse_8.setObjectName(_fromUtf8("ball_mouse_8"))
        self.RandomButton = QtGui.QPushButton(self.centralwidget)
        self.RandomButton.setGeometry(QtCore.QRect(950, 320, 31, 21))
        self.RandomButton.setObjectName(_fromUtf8("RandomButton"))
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(mainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        QtCore.QObject.connect(self.ConfirmAppendFunc,QtCore.SIGNAL('clicked()'),self.confirmFunc)



    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(_translate("mainWindow", "最近邻点对程序", None))
        self.ball_mouse.setText(_translate("mainWindow", "鼠标位置", None))
        self.label_12.setText(_translate("mainWindow", "y:", None))
        self.label_11.setText(_translate("mainWindow", "x:", None))
        self.AppendFunc.setTitle(_translate("mainWindow", "选点方式", None))
        self.HandAppend.setText(_translate("mainWindow", "手动选点", None))
        self.RandomAppend.setText(_translate("mainWindow", "随机生成", None))
        self.ConfirmAppendFunc.setText(_translate("mainWindow", "确定", None))
        self.ball_mouse_2.setText(_translate("mainWindow", "手动选点：", None))
        self.ball_mouse_3.setText(_translate("mainWindow", "已选点数", None))
        self.ball_mouse_4.setText(_translate("mainWindow", "随机生成：", None))
        self.ball_mouse_5.setText(_translate("mainWindow", "生成点数", None))
        self.CPFunc.setTitle(_translate("mainWindow", "选点方式", None))
        self.BruteCP.setText(_translate("mainWindow", "蛮力算法", None))
        self.RandomAppend_2.setText(_translate("mainWindow", "分治算法", None))
        self.StartCP.setText(_translate("mainWindow", "开始计算", None))
        self.ball_mouse_6.setText(_translate("mainWindow", "响应时间（秒）", None))
        self.label_13.setText(_translate("mainWindow", "1", None))
        self.ball_mouse_7.setText(_translate("mainWindow", "最近点对", None))
        self.label_14.setText(_translate("mainWindow", "2", None))
        self.ball_mouse_8.setText(_translate("mainWindow", "最短距离", None))
        self.RandomButton.setText(_translate("mainWindow", "生成", None))

#from myview import MyView

app = QtGui.QApplication(sys.argv)
ui = Ui_mainWindow()
mainwindow = QtGui.QMainWindow()
ui.setupUi(mainwindow)
mainwindow.show()
sys.exit(app.exec_())