# -*- coding: utf-8 -*-
import math
import datetime



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





n = 0
while n < 10:
    print nrs_f(n)
    n += 1
