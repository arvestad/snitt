# Computing shared edges in two graphs

_This project is for use in the course DA3018_.

This project contains a program called `snitt.py` that takes two files as input. The files are
supposed to contain one graph each, stored as lists of edges: each line is a pair of vertex names. I
have two very large graphs I want to compare and the program is therefore designed to be sparing
with memory, although that is not something I have worked hard to optimize. The idea is that I store
only one of the graphs in memory and then just read the edges from the other file to check whether
they are present in graph 1 or not. The output is a count of shared and unique edges.

Currently, there is something wrong with the program. I have two small test files, `t1.txt` and `t2.txt`,
that share two edges and have one unique edge each.

There are also two larger test files, `pairs1.txt` and `pairs2.txt` if you want to work with
that. They are taken from the original graph data, which contained roughly 80 million and 50 million
edges.


