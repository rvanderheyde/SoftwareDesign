# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:44:20 2014

@author: radmer
"""

def check_fermat(a,b,c,n):
    if n>2 and a**n+b**n==c**n:
        print 'Holy smokes, Fermat was wrong!'
    else:
        print 'No, that doesnt work'
def check_fermat2(a,b,c,n):
    a=int(a)
    b=int(b)
    c=int(c)
    n=int(n)
    check_fermat(a,b,c,n)

