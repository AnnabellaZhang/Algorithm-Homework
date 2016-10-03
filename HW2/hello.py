# -*- coding: utf-8 -*-

test = "yahoo!" if 1> 2 else "FALSE"[0]
print test

li = []
li.append((1,2))
a,b = li[0]
print a,b

def varargs(*args):
    ss = float(sum(args))/len(args)
    return ss

test = varargs(1,2,3,7,9)  # => (1,2,3)
print  test

import math
print dir(math)