# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 10:00:00 2020

@author: hamad
"""


for i in range(1,101):
    if i % 15 == 0:
        print('Fizz Buzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fizz')
    else:
        print(i)