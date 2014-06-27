#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from __future__ import print_function, unicode_literals
from itertools import izip, combinations

class SkipGram(object):
    def __init__(self, text, skip = 2, n = 2):
        self._text_list = text.strip().split()
        self._n = n
        self._skip = skip
        self._mask = tuple(i * self._skip for i in xrange(self._n))

    @property
    def skip_grams(self):
        for selector in combinations(xrange(len(self._text_list)), self._n):
            if any(a_i - b_i - selector[0] > 1 for a_i, b_i in izip(selector, self._mask)):
                continue
            yield tuple(self._text_list[i] for i in selector)

    @property
    def old_skip_grams(self):
        for i in xrange(len(self._text_list) - self._n + 1):
            for j in xrange(i + 1, min(i + self._n + self._skip, len(self._text_list))):
                yield (self._text_list[i], self._text_list[j],)

    def __repr__(self):
        return """text_list:{0},
n:{1},
skip:{2},
skip_gram_token_list:{3}""".format(
        repr(self._text_list),
        repr(self._n),
        repr(self._skip),
        repr(self._skip_gram_token_list))
