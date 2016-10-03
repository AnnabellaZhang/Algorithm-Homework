# -*- coding: utf-8 -*-
import time
import math


#自底向上求斐波那契数
def bu_f(n):
    f0 = 0
    f1 = 1
    if n==0:
        return f0
    if n==1:
        return f1
    i = 1
    while i < n:
        f0, f1 = f1, f0+f1
        i += 1
    return f1


#分治法求斐波那契数
def re_f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return re_f(n-1)+re_f(n-2)

k = 1
while k < 7:
    num = math.pow(2, k)
    print num
    t0 = time.time()
    result = bu_f(num)
    print result
    t1 = time.time()
    print ("Total time running bu_f(%s) = %s : %s seconds" %
           (str(num), str(result), str(t1 - t0))
           )
    t0 = time.time()
    result = re_f(num)
    print result
    t1 = time.time()
    print ("Total time running re_f(%s) = %s : %s seconds" %
           (str(num), str(result), str(t1 - t0))
           )
    k += 1