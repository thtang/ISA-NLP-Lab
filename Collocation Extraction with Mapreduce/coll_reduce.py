from __future__ import division

from collections import defaultdict, Counter
from itertools import groupby
from operator import itemgetter
from collocation import BaseWord
from collocation import Collocation
import fileinput


def parse_line(line):
    # baseword, collocate, distance = line.strip().split('\t')
    return line.strip().split('\t')


if __name__ == '__main__':
    skipgrams = defaultdict(lambda: defaultdict(Counter))
    
    for baseword, colls in groupby(map(parse_line, fileinput.input()), key=itemgetter(0)):
        # write your code here...
        for _, collword, distance in colls:
            skipgrams[baseword][collword][int(distance)] += 1


    colls = Collocation(skipgrams)
    for first in skipgrams:
        for word, collocate in colls[first].items():
            for i, freq in collocate.items():
                print (first, word, i, collocate.strength, collocate.spread, collocate.peak, freq, sep="\t")
