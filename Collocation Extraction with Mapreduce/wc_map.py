import re
import fileinput


def tokens(text):
    return re.findall('[a-z]+', text.lower())


if __name__ == '__main__':
    for line in fileinput.input():
        for word in tokens(line):
            print word
