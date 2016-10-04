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

#朴素递归法求斐波那契数
def re_f(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return re_f(n-1)+re_f(n-2)

#递归平方法求斐波那契
def rs_f(n):
    # 矩阵相乘
    def mul_metrix((a, b, c, d), (e, f, g, h)):
        return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)
    #矩阵n次幂
    def metrix_pow(n, (a, b, c, d)):
        if n == 0:
            return (1, 0, 0, 1)
        if n == 1:
            return (a, b, c, d)
        if n%2 == 0:
            return mul_metrix(metrix_pow(n/ 2, (a, b, c, d)), metrix_pow(n/2, (a, b, c, d)))
        else:
            return mul_metrix(metrix_pow((n+1) / 2, (a, b, c, d)), metrix_pow((n-1)/2, (a, b, c, d)))
    return metrix_pow(n,(1,1,1,0))[1]

#朴素递归法求斐波那契
def nrs_f(n):
    #求x的n次幂
    def a_pow(a, n):
        if n == 0:
            return 1
        if n == 1:
            return a
        if n % 2 == 0:
            return a_pow(a, n / 2) * a_pow(a, n / 2)
        else:
            return a_pow(a, (n + 1) / 2) * a_pow(a, (n - 1) / 2)
    a = (1 + math.sqrt(5))/2
    return int(round(a_pow(a,n)/math.sqrt(5)))


k = 1
while k < 20:
    #num = 25 + 2*k
    num = pow(2,k)
    print num
    t0 = time.clock()
    result = bu_f(num)
    print result
    t1 = time.clock()
    print ("Total time running bu_f(%s) : %s seconds" %
           (str(num),  str(t1 - t0))
           )
    '''
    t0 = time.clock()
    result = re_f(num)
    print result
    t1 = time.clock()
    print ("Total time running re_f(%s) : %s seconds" %
           (str(num), str(t1 - t0))
           )
    '''
    t0 = time.clock()
    result = rs_f(num)
    print result
    t1 = time.clock()
    print ("Total time running rs_f(%s) : %s seconds" %
           (str(num),  str(t1 - t0))
           )
    '''
    t0 = time.clock()
    result = nrs_f(num)
    print result
    t1 = time.clock()
    print ("Total time running nrs_f(%s) : %s seconds" %
           (str(num),  str(t1 - t0))
           )
    '''
    k += 1