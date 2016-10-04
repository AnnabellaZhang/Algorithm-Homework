# -*- coding: utf-8 -*-

#矩阵相乘
def metrix_pow(n,(a,b,c,d)):
    if n == 1:
        return (a,b,c,d)
    if n == 2:
        return (a*a+b*c,a*b+b*d,a*c+c*d,b*c+d*d)

print metrix_pow(2,(1,1,1,0))