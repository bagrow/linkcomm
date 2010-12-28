About
=====

Here are the codes for finding link communities [1] in complex networks.
Currently, we have two version: Python and C++. 

* Python version: it implements the whole algorithm: it calculates
  similarities, constructs the dendrogram, and extracts the optimal
  communities. It is suitable in many occasions. It's easier to use and gives
  you the exact solution. However, it may be too slow for very large networks,
  in which you may want to use C++ version.  

* C++ version: to save computing time and memory usage, it calculates
  similarities but does not construct the dendrogram. You can specify
  similarity threshold to obtain the communities.

References
==========

1. Yong-Yeol Ahn, James P. Bagrow, and Sune Lehmann, Link communities reveal
   multiscale complexity in networks, _Nature_ **466**, 761 (2010).
