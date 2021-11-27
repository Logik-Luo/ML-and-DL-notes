# -*- codeing = utf-8 -*-
# @time : 2021/11/20 10:23
# @Author : logik
# @file : 算法课.py
# @software : PyCharm

import numpy as np
a = np.array([1,2,3,4])
print(a)

import time
a = np.random.rand(1000000)
b = np.random.rand(1000000) # Randomly obtain two arrays with one million dimensions through rand
tic = time.time() # Measure current time
print(a)

import time
a = np.random.rand(1000000)
b = np.random.rand(1000000) # Randomly obtain two arrays with one million dimensions through rand
tic = time.time()
c = np.dot(a,b)
toc = time.time()
print('''time for vectorization:''')
print(str(1000*(toc-tic)))

c = 0
tic = time.time()
for i in range(1000000):
    c += a[i]*b[i]
toc = time.time()
print('''time for [for] cycle:''')
print( str(1000*(toc-tic)))


