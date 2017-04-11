import fileinput

from nltk.tokenize import wordpunct_tokenize
from nltk.corpus import stopwords

max_distance = 5
eng_stopwords = set(stopwords.words('english'))
eng_symbols = '{}"\'()[].,:;+!?-*/&|<>=~$#'


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


if __name__ == '__main__':
    for line in fileinput.input():
        words = wordpunct_tokenize(line)
        for n in range(1, max_distance + 1):
            for ngram in filter(ngram_is_valid, to_ngrams(words, n+1)):
                first = ngram[0]
                second = ngram[-1]
                print (first,second,str(n),sep="\t")
                print (second,first,str(-n),sep="\t")
