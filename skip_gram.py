#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from itertools import ifilter, combinations

class SkipGram(object):
    def __init__(self, text, skip = 2, n = 2):
        self._text_list = text.strip().split()
        self._n = n
        self._skip = skip
        self._ngram_token_list = []
        self._skip_gram_token_list = []

    def _ngrams(self, l, n):
        for i in xrange(len(l) - n + 1):
            yield l[i:i+n]

    @property
    def skip_grams(self):
        if self._skip_gram_token_list:
            return self._skip_gram_token_list
        self._skip_gram_token_list = [tuple(self._text_list[i] for i in selector)
                for selector in ifilter(self._checker, combinations(xrange(len(self._text_list)), self._n))]
        return self._skip_gram_token_list

    def _checker(self, l):
        skip_biased = self._skip + 1
        for token in self._ngrams(l, 2):
            if token[1] - token[0] > skip_biased:
                return False
        return True

    def __repr__(self):
        return """text_list:{0},
n:{1},
skip:{2},
ngram_token_list:{3},
skip_gram_token_list:{4}""".format(
        repr(self._text_list),
        repr(self._n),
        repr(self._skip),
        repr(self._ngram_token_list),
        repr(self._skip_gram_token_list))
