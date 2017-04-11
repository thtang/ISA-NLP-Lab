from __future__ import division
from math import sqrt
import numpy

k0 = 1
k1 = 1
U0 = 10
max_distance = 5


class Collocate:
    def __init__(self, collocation):
        self.collocation = dict(collocation)
        values = list(self.collocation.values())
        self.freq = sum(values)
        self.spread = numpy.var(values + [0] * (max_distance * 2 - len(values)))
        self.peak = self.freq / (max_distance * 2) + k1 * sqrt(self.spread)
        self.strength = -1

    def __getitem__(self, key):
        return self.collocation[key]

    def __repr__(self):
        reprformat = 'Collocates(freq={}, strength={}, spread={}, peak={}, {})'
        return reprformat.format(self.freq, self.strength, self.spread, self.peak, self.collocation)

    def keys(self):
        return self.collocation.keys()

    def values(self):
        return self.collocation.values()

    def items(self):
        return self.collocation.items()

    def compute(self, avg_freq, dev):
        self.strength = (self.freq - avg_freq) / dev if dev else 0

    def prune_collocation(self):
        self.collocation = {index: freq for index, freq in self.items() if freq > self.peak}
        return len(self.collocation) > 0


class BaseWord:
    def __init__(self, colls):
        self.collocates = {coll: Collocate(value) for coll, value in colls.items()}
        # compute_statistical_info
        freqs = [collocate.freq for collocate in self.collocates.values()]
        self.avg_freq = numpy.mean(freqs)
        self.dev = numpy.std(freqs)
        for collocate in self.collocates.values():
            collocate.compute(self.avg_freq, self.dev)
        self.filter_collocates()

    def __getitem__(self, key):
        return self.collocates[key]

    def __repr__(self):
        return 'BaseWord(avg_freq={}, dev={},\n{}\n}})'.format(self.avg_freq, self.dev, self.collocates)

    def values(self):
        return self.collocates.values()

    def items(self):
        return self.collocates.items()

    def smadjas(self, collocate):
        # Smadja's filtering skip-bigrams C1
        if collocate.strength <= k0:
            return False
        # Smadja's filtering skip-bigrams C2
        if collocate.spread <= U0:
            return False
        # Smadja's filtering skip-bigrams C3
        if collocate.prune_collocation():
            return True
        return False

    def filter_collocates(self):
        self.collocates = {word: collocate for word, collocate in self.collocates.items() if self.smadjas(collocate)}


class Collocation(dict):
    def __init__(self, skipbigrams):
        self.factory = BaseWord
        self.skipbigrams = skipbigrams

    def __missing__(self, key):
        self[key] = self.factory(self.skipbigrams[key])
        return self[key]
