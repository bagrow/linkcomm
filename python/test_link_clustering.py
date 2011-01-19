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

    def test_similarities_unweighted(self):
        '''similarities_unweighted(adj) returns a list of decoredted edge pairs.
        (1.0-sim, eij, eik)
        '''
        adj = { 'a': set(['b', 'c']),  # a triangle
                'b': set(['a', 'c']),
                'c': set(['a', 'b']) 
                }
        answers = [(0.0, (('a', 'b'), ('a', 'c'))),  # every edge pair has 
                  (0.0, (('a', 'b'), ('b', 'c'))),   # similarity 1.0.
                  (0.0, (('a', 'c'), ('b', 'c'))),   # everything is sorted inside.
                  ]                                  # each edge pair. 
        similarities = similarities_unweighted(adj, verbose=False)
        for answer in answers:
            self.assertTrue(answer in similarities)


if __name__ == '__main__':
    unittest.main()
