# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:23:31 2014

@author: radmer
"""

def doTwice(f):
    f()
    f()

def doFourTime(f):
    doTwice(f)
    doTwice(f)

def makeH():
   print  '+ - - - -',

def print_H():
    doTwice(makeH)
    print '+'
    
def makeV():
    print '|        ',

def print_V():
    doTwice(makeV)
    print '|'

def box():
    print_H()
    doFourTime(print_V)

#doTwice(box)
#print_H()

def print_H2():
    doFourTime(makeH)
    print '+'

def print_V2():
    doFourTime(makeV)
    print '|'

def box2():
    print_H2()
    doFourTime(print_V2)

doFourTime(box2)
print_H2()