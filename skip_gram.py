#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
from itertools import izip, combinations

class SkipGram(object):
    def __init__(self, text, skip = 2, n = 2):
        self._text_list = text.strip().split()
        self._n = n
        self._skip = skip

    @property
    def skip_grams(self):
        mask = [i * self._skip for i in range(self._n)]
        for selector in combinations(xrange(len(self._text_list)), self._n):
            if any([a_i - b_i - selector[0] > 1 for a_i, b_i in izip(selector, mask)]):
                continue
            yield tuple(self._text_list[i] for i in selector)

    def __repr__(self):
        return """text_list:{0},
n:{1},
skip:{2},
skip_gram_token_list:{3}""".format(
        repr(self._text_list),
        repr(self._n),
        repr(self._skip),
        repr(self._skip_gram_token_list))
