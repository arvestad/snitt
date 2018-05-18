# -*- coding: utf-8 -*-
"""
Created on Thu May 17 23:03:37 2018

@author: tondar.jahangiri
"""

import argparse


def load_pairs(h):
    
    pairs = dict()
    for line in h:
        a, b = line.split()
        pairs[(a,b)] = True
        
    return pairs


def filter_pairs(h, known_pairs):
    
    n_shared = 0
    n_unique = 0
    for line in h:
        a, b = line.split()
        if (a,b) in known_pairs:
            n_shared += 1
        elif (b,a) in known_pairs:
            n_shared += 1
        else:
            n_unique += 1
    
    return n_shared, n_unique

def main(file1, file2):
    with open(file1, "r") as h1, open(file2, "r") as h2:
        pairs = load_pairs(h1)
        
        n_shared, n_unique = filter_pairs(h2, pairs)
        print("Shared:   ", n_shared)
        print("Unique 1:   ", len(pairs) - n_shared)
        print("Unique 2:   ", n_unique)
        


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    args = parser.add_argument("file1")
    args = parser.add_argument("file2")
    
    args = parser.parse_args()
    
    main(args.file1, args.file2)

    
