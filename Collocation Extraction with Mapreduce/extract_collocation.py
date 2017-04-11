# coding: utf-8

# -----
#
# # Lab3
#
# # word tokenize
# - 使用 nltk, pattern 或 textblob 做 word tokenize。
# - 資料取原始檔案的前 50000 行

# # 計算 skip bigram
#
# - $p_j^i$
# - ngram 任何位置不包含符號
# - skip bigram 不包含 stop words 與數字

from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords
from collections import defaultdict, Counter
from collocation import Collocation
import fileinput

max_distance = 5

eng_stopwords = set(stopwords.words('english'))
eng_symbols = set('{}"\'()[].,:;+!?-*/&|<>=~$')


def to_ngrams(words, length):
    return zip(*[words[i:] for i in range(length)])


def to_skipbigrams(words, distance):
    return zip(*[words, words[distance:]])


def ngram_is_valid(ngram):
    first, last = ngram[0], ngram[-1]
    if first in eng_stopwords or last in eng_stopwords:
        return False
    if any(num in first or num in last for num in '0123456789'):
        return False
    if any(eng_symbol in word for word in ngram for eng_symbol in eng_symbols):
        return False
    return True


def compute_skipbigrams(lines):
    skipbigrams = defaultdict(lambda: defaultdict(Counter))
    for line in lines:
        words = wordpunct_tokenize(line.strip())
        for n in range(1, max_distance+1):
            for ngram in filter(ngram_is_valid, to_ngrams(words, n+1)):
                first, last = ngram[0], ngram[-1]
                skipbigrams[first][last][n] += 1
                skipbigrams[last][first][-n] += 1
    return skipbigrams


def main():
    skipbigrams = compute_skipbigrams(fileinput.input())
    colls = Collocation(skipbigrams)

    # load all collocations
    for baseword in skipbigrams:
        for word, collocate in colls[baseword].items():
            for i, freq in collocate.items():
                print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(baseword, word, i, collocate.strength, collocate.spread, collocate.peak, freq))


if __name__ == '__main__':
    main()
