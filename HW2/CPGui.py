# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
'''
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
import matplotlib.pyplot as plt
'''

import math
sys.path.append('E:\Code\GitHub\Algorithm-Homework\HW2\CP.py')
import CP
import random
import time

class MyApp(QtGui.QMainWindow, CP.Ui_mainWindow):
    nodes = []
    num = -1
    isHand = False
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        #CP.Ui_MainWindow.setupUi()
        self.setupUi(self)
        self.RandomAppend.setChecked(True)
        self.ConfirmAppendFunc.clicked.connect(self.confirmFunc)
        self.RandomButton.clicked.connect(self.randomAppendFunc)
        self.HandButton.clicked.connect(self.handAppendFunc)
        self.StartCP.clicked.connect(self.CPCompute)

    def mousePressEvent(self,event):
        if event.button() == QtCore.Qt.LeftButton:
            pos = event.pos()
            if pos.x() <= 800 and pos.y() <= 800:
                self.ball_x.setText(str(pos.x()))
                self.ball_y.setText(str(pos.y()))
            if self.isHand and self.HandButton.isEnabled():
                nownum = int(self.PointNum.text())
                self.nodes.append((pos.x(),pos.y()))
                nownum += 1
                self.PointNum.setText(str(nownum))
                #print self.nodes


    def confirmFunc(self):
        self.BruteCP.setEnabled(False)
        self.DivideCP.setEnabled(False)
        self.DivideCP.setChecked(False)
        self.StartCP.setEnabled(False)
        if self.HandAppend.isChecked() == True:
            self.nodes = []
            self.RandomPointNum.setEnabled(False)
            self.RandomButton.setEnabled(False)
            self.HandButton.setEnabled(True)
            self.PointNum.setText("0")
            self.isHand = True
        if self.RandomAppend.isChecked() == True:
            self.isHand = False
            self.RandomPointNum.setEnabled(True)
            self.RandomButton.setEnabled(True)
            self.HandButton.setEnabled(False)
            self.PointNum.setText("")

    def randomAppendFunc(self):
        self.num = -1
        self.num = self.RandomPointNum.text()
        #此处加一段格式检查
        self.nodes = []
        for i in range(0, int(self.num)):
            x = random.uniform(0, 1.5*int(self.num))
            y = random.uniform(0, 1.5*int(self.num))
            self.nodes.append((round(x,2), round(y,2)))
            #self.nodes.append((x, y))
            #此处将生成的点在view上标出
        if len(self.nodes) >= 2:
            self.BruteCP.setEnabled(True)
            self.DivideCP.setEnabled(True)
            self.DivideCP.setChecked(True)
            self.StartCP.setEnabled(True)
            self.RandomButton.setEnabled(False)
            #self.RandomPointNum.setText("")
            self.RandomPointNum.setEnabled(False)

       # print self.nodes
        print int(self.num)
        print len(self.nodes)

    def handAppendFunc(self):
        if len(self.nodes) >= 2:
            self.BruteCP.setEnabled(True)
            self.DivideCP.setEnabled(True)
            self.DivideCP.setChecked(True)
            self.StartCP.setEnabled(True)
            self.HandButton.setEnabled(False)
        print self.nodes
        print len(self.nodes)

    def CPCompute(self):
        if self.BruteCP.isChecked() == True:
            t0 = time.clock()
            r1 = self.brute_cp(self.nodes,len(self.nodes))
            t1 = time.clock()
            self.FuncTime.setText(str(t1-t0))
            self.Point1.setText(str(r1[0]))
            self.Point2.setText(str(r1[1]))
            self.ShortDis.setText(str(r1[2]))
        if self.DivideCP.isChecked() == True:
            t0 = time.clock()
            r1 = self.divide_cp(self.nodes,len(self.nodes))
            t1 = time.clock()
            self.FuncTime.setText(str(t1-t0))
            self.Point1.setText(str(r1[0]))
            self.Point1.adjustSize()
            self.Point2.setText(str(r1[1]))
            self.Point2.adjustSize()
            self.ShortDis.setText(str(r1[2]))



    # 暴力算法找最近点对
    def brute_cp(self,nodes, n):
        result = [(0, 0), (0, 0), 3000]
        for i in range(0, n):
            if i % 1000 == 0:
                print i
            for j in range(i + 1, n):
                dis = self.distance(nodes[i], nodes[j])
                if dis < result[2]:
                    result = [nodes[i], nodes[j], dis]
        return result

    # 用分治法找最近点对
    def divide_cp(self,nodes, n):
        result = [(0, 0), (0, 0), 3000]
        if n < 2:
            return result
        if n == 2:
            dis = self.distance(nodes[0], nodes[1])
            return [nodes[0], nodes[1], dis]
        x_nodes = sorted(nodes, key=lambda x: x[0])
        if n % 2 == 0:
            m = (x_nodes[n / 2][0] + x_nodes[n / 2 - 1][0]) / 2
        else:
            m = x_nodes[n / 2][0]
        result1 = self.divide_cp(x_nodes[0:n / 2 ], len(x_nodes[0:n / 2 ]))
        result2 = self.divide_cp(x_nodes[n / 2 :n], len(x_nodes[n / 2 :n]))
        d = min(result1[2], result2[2])
        if result1[2] >= result2[2]:
            result = result2
        else:
            result = result1
        temp = filter(lambda x: m + d > x[0] > m - d, nodes)
        m_nodes = sorted(temp, key=lambda x: x[1])
        for i in range(0, len(m_nodes)):
            j = i + 1
            while j < i + 8 and j < len(m_nodes):
                dis = self.distance(m_nodes[i], m_nodes[j])
                if dis < result[2]:
                    result = [m_nodes[i], m_nodes[j], dis]
                j += 1
        return result

    # 求取两点间欧式距离
    def distance(self,(a, b), (c, d)):
        return math.sqrt((a - c) * (a - c) + (b - d) * (b - d))






if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    window.num = 123
    sys.exit(app.exec_())