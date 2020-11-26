# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:03:41 2020

@author: jebro
"""



def dive(n):
    s = 0
    for i in range(1, n):
        
        if i % 2 == 0:
            print(i)
            s = s+1
    print(s)
            
        
dive(10)

