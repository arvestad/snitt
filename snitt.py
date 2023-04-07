#! /usr/bin/env python3

import argparse


def load_pairs(h):
    '''
    Read identifier pairs, i.e., two identifiers separated by whitespace from the file
    represented by handle h. Return all pairs as a dictionary.
    '''
    pairs = dict()
    for line in h:
        a, b = line.split()
        pairs[(a,b)] = True

    return pairs


def filter_pairs(h, known_pairs):
    '''
    Read pairs (like in load_pairs) from the input file h and count how many of the pairs 
    are shared with what is stored in the dictionary known_pairs. Also count how many
    of the pairs in h are unique to that file. Return the number of shared and unique pairs.
    '''
    n_shared = 0
    n_unique = 0
    for line in h:
        a, b = line.split()
        if (a,b) in known_pairs or (b,a) in known_pairs:
            n_shared += 1
        else:
            n_unique += 1
    return n_shared, n_unique


def main(file1, file2):
    with open(file1) as h1, open(file2) as h2:
        pairs = load_pairs(h1)

        n_shared, n_unique = filter_pairs(h2, pairs)
        print("Shared:   ", n_shared)
        print("Unique 1: ", len(pairs) - n_shared)
        print("Unique 2: ", n_unique)

        
if __name__=='__main__':
    parser = argparse.ArgumentParser()
    args = parser.add_argument("file1")
    args = parser.add_argument("file2")

    args=parser.parse_args()

    main(args.file1, args.file2)
