#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2


class NetSpeak:
    def __init__(self):
        self.opener = urllib2.build_opener()
        self.opener.addheaders = [('User-Agent', 'Mozilla/5.0 (compatible; MSIE 5.5; Windows NT)')]
        self.page = None

    def __getPageContent(self, url):
        return self.opener.open(url).read()

    def __rolling(self, url, maxfreq):
        webdata = self.__getPageContent(url.replace("'", "''") + "&maxfreq=%s" % maxfreq)
        if webdata:
            Result = [(data2[2], float(data2[1])) for data2 in [data.split("\t") for data in webdata.strip().split("\n")]]
            lastFreq = int(Result[-1][1])
            if lastFreq != maxfreq:
                return Result + self.__rolling(url, lastFreq)
            else:
                return []
        else:
            return []

    def search(self, query):
        queries = query.split()
        new_query = []
        for token in queries:
            if token.count("|") > 0:
                new_query.append("%5B+" + "+".join(token.split("|")) + "+%5D")
            elif token == "*":
                new_query.append("?")
            else:
                new_query.append(token)
        new_query = "+".join(new_query)
        url = "http://api.netspeak.org/netspeak3/search?query=%s" % (new_query.replace(" ", "+"))
        webdata = self.__getPageContent(url.replace("'", "''"))
        if webdata:
            Result = [(data2[2], float(data2[1])) for data2 in [data.split("\t") for data in webdata.strip().split("\n")]]
            lastFreq = int(Result[-1][1])
            Result += self.__rolling(url, lastFreq)
            return Result
        else:
            return None


if __name__ == "__main__":
    SE = NetSpeak()
    # Search_Result = SE.search("approach that *")
    # print Search_Result
    # at * time
    test = 'when the break is finished'.split()
    print(test)
    # test = '? is finished'
    # test = 'brake is finished'

    for i in range(len(test) - 3):
        print(i)
        res = SE.search(' '.join(test[i:i + 3]))
        if res:
            print('\n'.join('\t'.join([str(y) for y in x]) for x in res))
        else:
            print('not found')
