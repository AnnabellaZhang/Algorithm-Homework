# -*- coding: utf-8 -*-
import math
import random


#求取两点间欧式距离
def distance((a,b),(c,d)):
    return math.sqrt((a-c)*(a-c)+(b-d)*(b-d))

nodes = []
n = 5
result = [(0,0),(0,0),1500]
for i in range(0,n):
    nodes.append((random.uniform(0,10),random.uniform(0,10)))
for i in range(0,n):
    if i % 1000 == 0:
        print i
    for j in range(i+1,n):
        dis = distance(nodes[i],nodes[j])
        if dis < result[2]:
            result = [nodes[i],nodes[j],dis]

print result
print nodes
def choosey((a,b)):
    return b
def choosex((a,b)):
    return a
print sorted(nodes,key = choosey)
print sorted(nodes,key = choosex)
print sorted(nodes,key = lambda x:x[0])
print filter(lambda x:7 > x[1] > 5,nodes)

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
'''
self.main_frame = mainWindow
        self.figure = plt.figure(figsize=(8,6))
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setGeometry(QtCore.QRect(0,0, 800, 800))
        self.canvas.setParent(self.main_frame)
        self.canvas.mousePressEvent = self.mousePressEvent
'''



