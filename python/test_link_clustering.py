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
            self.assertTrue(abs(0.0 - Dc(m,n)) < self.small_float_num)

        mn_pairs = [(3,3), (6,4)] # cliques
        for m,n in mn_pairs:
            self.assertTrue(abs(1.0 - Dc(m,n)) < self.small_float_num)

    def test_similarities_unweighted(self):
        '''similarities_unweighted(adj) returns a list of decoredted edge pairs.
        (1.0-sim, eij, eik)
        '''
        # a triangle.
        triangle_adj = { 'a': set(['b', 'c']),
                         'b': set(['a', 'c']),
                         'c': set(['a', 'b']),
                       }

        # every edge pair has similarity 1.0. We only need to check the following
        # pairs because everything is sorted inside each edge pair and each edge.
        triangle_similarities = [(0.0, (('a', 'b'), ('a', 'c'))),
                                 (0.0, (('a', 'b'), ('b', 'c'))),
                                 (0.0, (('a', 'c'), ('b', 'c'))),
                                ]

        similarities = similarities_unweighted(triangle_adj, verbose=False)
        for answer in triangle_similarities:
            self.assertTrue(answer in similarities)


class TestDirectedLinkClustering(unittest.TestCase):

    def setUp(self):
        self.small_float_num = 1e-6

    def test_read_edgelist(self):
        '''test whether the function correctly read the directed edges.'''
        pass

    def test_similarities(self):
        '''test whether the similarities for directed network is correct.'''
        pass

    def test_partition_density(self):
        '''test directed partition density.'''
        pass


if __name__ == '__main__':
    unittest.main()
