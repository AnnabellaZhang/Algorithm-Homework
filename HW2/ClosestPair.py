# -*- coding: utf-8 -*-
import math
import random
import time


#求取两点间欧式距离
def distance((a,b),(c,d)):
    return math.sqrt((a-c)*(a-c)+(b-d)*(b-d))

#生成n个点对
nodes = []
n = 20000

for i in range(0,n):
    nodes.append((random.uniform(-1000,1000),random.uniform(-1000,1000)))
    #nodes.append((random.randint(0, 1000), random.randint(0, 1000)))

#nodes = [(544, 317), (420, 788), (87, 311), (536, 738), (351, 548), (458, 395), (822, 132), (665, 11), (793, 623), (721, 403), (878, 856), (59, 490), (316, 133), (171, 524), (794, 874), (982, 634), (875, 121), (779, 13), (247, 97), (891, 674), (689, 14), (623, 665), (585, 620), (858, 856), (438, 614), (374, 926), (644, 734), (504, 235), (833, 107), (661, 931), (61, 524), (496, 334), (145, 491), (643, 576), (725, 688), (853, 757), (474, 731), (701, 493), (538, 215), (857, 462), (716, 601), (514, 476), (870, 673), (167, 810), (831, 645), (901, 125), (49, 746), (166, 274), (894, 138)]

print len(nodes)

#暴力算法找最近点对
def brute_cp(nodes,n):
    result = [(0, 0), (0, 0), 3000]
    for i in range(0, n):
        if i % 1000 == 0:
            print i
        for j in range(i + 1, n):
            dis = distance(nodes[i], nodes[j])
            if dis < result[2]:
                result = [nodes[i], nodes[j], dis]
    return result

#用分治法找最近点对
def divide_cp(nodes,n):
    result = [(0, 0), (0, 0), 1500]
    if n < 2:
        return result
    if n == 2:
        dis = distance(nodes[0], nodes[1])
        return [nodes[0], nodes[1], dis]
    x_nodes = sorted(nodes,key = lambda x:x[0])
    if n%2 == 0:
        m = (x_nodes[n/2][0] + x_nodes[n/2-1][0])/2
    else:
        m = x_nodes[n/2][0]
    result1 = divide_cp(x_nodes[0:n/2+1],len(x_nodes[0:n/2+1]))
    result2 = divide_cp(x_nodes[n/2+1:n],len(x_nodes[n/2+1 :n]))
    d = min(result1[2],result2[2])
    if result1[2] >= result2[2]:
        result = result2
    else:
        result = result1
    temp = filter(lambda x:m+d > x[0] > m-d,nodes)
    m_nodes = sorted(temp,key = lambda x:x[1])
    for i in range(0,len(m_nodes)):
        j = i + 1
        while j < i+8 and j < len(m_nodes):
            dis = distance(m_nodes[i],m_nodes[j])
            if dis < result[2] :
                result = [m_nodes[i],m_nodes[j],dis]
            j +=1
    return result

t0 = time.clock()
r1 = brute_cp(nodes,n)
t1 = time.clock()
print ("Total time running brute_cp(%s) : %s seconds" %
           (str(n),  str(t1 - t0))
           )
t0 = time.clock()
r2 = divide_cp(nodes,n)
t1 = time.clock()
print ("Total time running brute_cp(%s) : %s seconds" %
           (str(n),  str(t1 - t0))
           )
print "brute_cp: ", r1
print "divide_cp: ", r2
print r1[2] - r2[2]
print nodes



