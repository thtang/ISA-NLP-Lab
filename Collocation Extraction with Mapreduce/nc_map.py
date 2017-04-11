#!/usr/bin/env python
# echo 'aaa bbb ccc\naaa bbb aaa' | python nc-map.py
import re
import fileinput


def tokens(str1):
    return re.findall('[a-z]+', str1.lower())


def to_ngrams(words, length):
    return zip(*[words[i:] for i in range(length)])


if __name__ == '__main__':
    for line in fileinput.input():
        words = tokens(line)
        for n in range(1, 6):
            for ngram in to_ngrams(words, n):
                print(' '.join(ngram))
