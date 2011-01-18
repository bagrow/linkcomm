#!/usr/bin/env python
import unittest
from link_clustering import *

class TestLinkClustering(unittest.TestCase):

    def setUp(self):
        pass

    def test_partition_density(self):
        '''make sure the partition density function Dc(m,n)'''
        # Trees 
        m,n = 1,2 # single link
        self.assertEqual(0.0*m/2.0, Dc(m,n))

        m,n = 3,4
        self.assertEqual(0.0*m/2.0, Dc(m,n))

        # cliques
        m,n = 3,3
        self.assertEqual(1.0*m/2.0, Dc(m,n))

        m,n = 6,4
        self.assertEqual(1.0*m/2.0, Dc(m,n))


if __name__ == '__main__':
    unittest.main()
