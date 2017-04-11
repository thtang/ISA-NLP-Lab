# uniq -c
import fileinput
from itertools import groupby

if __name__ == '__main__':
    for word, lines in groupby(map(str.strip, fileinput.input())):
        print(word, sum(1 for _ in lines))
