#!/usr/bin/env python

import argparse
import pickle

parser = argparse.ArgumentParser(description='print the size of the intersection of two pickled sets')
parser.add_argument("s1", type=argparse.FileType('r'))
parser.add_argument("s2", type=argparse.FileType('r'))
args = parser.parse_args()

s1 = pickle.load( args.s1 )
s2 = pickle.load( args.s2 )

def jaccard_index(first, *others):
    return float( len( first.intersection(*others))) / float(len(first.union(*others)))

print jaccard_index(s1, s2)
