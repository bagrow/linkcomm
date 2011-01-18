#!/usr/bin/env python
import unittest
from link_clustering import *

class TestLinkClustering(unittest.TestCase):

    def setUp(self):
        pass

    def test_partition_density(self):
        '''make sure the partition density function Dc(m,n)'''
        # single edge: (m,n) = (1,2)
        self.assertEqual(0.0, Dc(1,2))

if __name__ == '__main__':
    unittest.main()
