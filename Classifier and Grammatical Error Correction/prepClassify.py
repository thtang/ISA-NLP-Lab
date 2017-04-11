from __future__ import division
from sklearn.linear_model import LogisticRegression
from nltk.classify.scikitlearn import SklearnClassifier


if __name__ == '__main__':
    corrections = open('wiki.prep.corrections.clean.10k')
    data = list(map(open("wiki.prep.sents.clean.genia.10k")))

    size = len(data)
    train = data[:-(size//10)]
    test = data[-(size//10):]

    # prepare your train and test data
    trainData = ...
    testData = ...

    # train your classifier
    classifier = SklearnClassifier(LogisticRegression())
    classifier.train(trainData)

    # test your classifier
    # ...
    correct = 0

    precision = correct / len(testData)

    print('precision:', precision)
    print('recall:')
    print('f1-measure:')
