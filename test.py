#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from itertools import ifilter, compress, combinations
from functools import partial

def ngrams(l, n = 2):
    for i in xrange(len(l) - n + 1):
        yield l[i:i+n]

text = "Insurgents killed in ongoing fighting."
def f(skip, l):
    for token in ngrams(l):
        if token[1] - token[0] > skip:
            return False
    return True

if __name__ == "__main__":
    skip = 2
    f = partial(f, skip + 1)
    for selector in ifilter(f, combinations(xrange(len(text.split())), 3)):
        print(tuple([text.split()[i] for i in selector]))
