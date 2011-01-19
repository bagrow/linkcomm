#!/usr/bin/env python
import unittest
from link_clustering import *

class TestLinkClustering(unittest.TestCase):

    def setUp(self):
        self.small_float_num = 1e-6

    def test_partition_density(self):
        '''make sure the partition density function Dc(m,n)'''
        mn_pairs = [(1,2), (3,4)] # trees
        for m,n in mn_pairs:
            self.assertTrue(abs(0.0*m/2.0 - Dc(m,n)) < self.small_float_num)

        mn_pairs = [(3,3), (6,4)] # cliques
        for m,n in mn_pairs:
            self.assertTrue(abs(1.0*m/2.0 - Dc(m,n)) < self.small_float_num)


if __name__ == '__main__':
    unittest.main()
