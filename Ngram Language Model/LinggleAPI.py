#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

API_URL = "http://linggle.com/query/"


class Linggle:
    def __getitem__(self, query):
        return self.search(query)

    def search(self, query):
        req = requests.get('http://linggle.com/query/' + query)
        results = req.json()
        results = [(' '.join(item['phrase']), item['count']) for item in results]
        return results


if __name__ == "__main__":
    SE = Linggle()
    # Search_Result = SE.search("approach that *")
    # print Search_Result
    # at * time
    test = 'when the brake is finished'.split()
    print(test)
    # test = '? is finished'
    # test = 'brake is finished'

    for i in range(len(test) - 2):
        print(i)
        res = SE[' '.join(test[i:i + 3])]
        if res:
            print('\n'.join('\t'.join([str(y) for y in x]) for x in res))
        else:
            print('not found')
