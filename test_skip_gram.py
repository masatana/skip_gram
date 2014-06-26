#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import unittest
from skip_gram import SkipGram

class TestSkipGram(unittest.TestCase):
    def setUp(self):
        self.two_skip_bi_gram = SkipGram("Insurgents killed in ongoing fighting.", 2, 2)
        self.two_skip_tri_gram = SkipGram("Insurgents killed in ongoing fighting.", 2, 3)

    def test_skip_grams(self):
        self.assertEqual(self.two_skip_bi_gram.skip_grams, [
                ("Insurgents", "killed"),
                ("Insurgents", "in"),
                ("Insurgents", "ongoing"),
                ("killed", "in"),
                ("killed", "ongoing"),
                ("killed", "fighting."),
                ("in", "ongoing"),
                ("in", "fighting."),
                ("ongoing", "fighting.")])

        self.assertEqual(self.two_skip_tri_gram.skip_grams, [
                ("Insurgents", "killed", "in"),
                ("Insurgents", "killed", "ongoing"),
                ("Insurgents", "killed", "fighting."),
                ("Insurgents", "in", "ongoing"),
                ("Insurgents", "in", "fighting."),
                ("Insurgents", "ongoing", "fighting."),
                ("killed", "in", "ongoing"),
                ("killed", "in", "fighting."),
                ("killed", "ongoing", "fighting."),
                ("in", "ongoing", "fighting.")])

if __name__ == "__main__":
    unittest.main()
