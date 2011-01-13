#!/usr/bin/env python
# encoding: utf-8

# test_chain.py
# Jim Bagrow
# Last Modified: 2010-12-30

import sys, os
from itertools import chain
import time

"""
There's a special case we need to deal with when returning the
similarity heap iterator, specifically we need to tack an element onto
the end. This is done using itertools.chain, but is there a performance
hit?

Here we investigate...
"""

if __name__ == '__main__':
    
    num = int(float(sys.argv[1]))
    
    t1 = time.time()
    total_all = 0
    for x in xrange(num): 
        total_all += x
    #total_all = sum( xrange(num) )                  # so much faster!
    t2 = time.time()
    total_prt = 0
    for x in chain(xrange(num-1),[num-1]):
        total_prt += x
    #total_prt = sum( chain(xrange(num-1),[num-1]) ) # so much faster!
    t3 = time.time()
    
    assert total_prt == total_all
    
    
    print "        t2 - t1 =", t2-t1 
    print "        t3 - t2 =", t3-t2
    print "(t2-t1)/(t3-t2) =", (t2-t1)/(t3-t2)
    
    """
    >>> python test_chain.py 1e7
            t2 - t1 = 2.89197516441
            t3 - t2 = 3.08671998978
    (t2-t1)/(t3-t2) = 0.936908813884
    
    >>> python test_chain.py 5e7
            t2 - t1 = 14.5919158459
            t3 - t2 = 16.61850214
    (t2-t1)/(t3-t2) = 0.878052409471
    
    >>> python test_chain.py 1e8
            t2 - t1 = 34.3898971081
            t3 - t2 = 39.5938608646
    (t2-t1)/(t3-t2) = 0.868566397848
    """
    
    """
    If we used the shorter sum(xrange(num)) vs. 
    sum( chain(xrange(num-1),[num-1]) ), the 
    difference is even more dramatic:
    
    >>> python test_chain.py 1e8
            t2 - t1 = 1.84194803238
            t3 - t2 = 3.1525349617
    (t2-t1)/(t3-t2) = 0.584275211776
    
    >>> python test_chain.py 1e9
            t2 - t1 = 18.6334838867
            t3 - t2 = 34.3149030209
    (t2-t1)/(t3-t2) = 0.543014324575
    
    """
    