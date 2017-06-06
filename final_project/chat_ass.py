from os import listdir
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import jieba.analyse
import jieba
from joblib import Parallel, delayed
import spacy
import gensim
from operator import itemgetter

# load chat data (could store to database)
huge_df = pd.read_csv("/home/thtang/all_chat_v3.csv")

import re
def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    '''
    def atoi(text):
        return int(text) if text.isdigit() else text

    return [atoi(c) for c in re.split('(\d+)', text)]
huge_df = huge_df.reindex(columns=sorted(huge_df.columns, key=natural_keys))


import gensim
# create index matrix
# index = gensim.similarities.MatrixSimilarity(corpus=huge_matrix)
# index.save('all_chat_vec_v3.index')
index = gensim.similarities.MatrixSimilarity.load('all_chat_vec_v3.index') # load index matrix

def query2Vec(string):
    string_list = jieba.lcut(string)
    sent_matrix = []
    for word in string_list:
        try:
            wv = model[word]
            sent_matrix.append(wv)
        except:
            sent_matrix.append(np.zeros(100))
    q_vector = np.mean(np.array(sent_matrix),axis = 0)
    return(q_vector)


def query_sent(q_string):
	sims = index[query_sent(q_string)]  #將 query餵入 index 這個 model，他算出 query 與 那些回覆 的相似度
	np_sort = np.argsort(sims) #照相似度排序
	sims_top = np_sort[::-1][:50] #取前五十個像的
	output_tup = []
	for sim in sims_top:
	    #找到像的句子後，去找那句的下一個回覆，即是我們要推薦的
	    try:                                                    
	        if huge_df.loc[sim,"sender_gender"] != huge_df.loc[sim+1,"sender_gender"]:  #篩掉連續兩個回覆都同一個人打的句子
	            output_tup.append((huge_df.loc[sim,"text"],huge_df.loc[sim+1,"text"], huge_df.loc[sim+1,"number_to_end"]))
	    except:
	        print(sim)
	return (sorted(output_tup , key=lambda item: -item[2])[:10])

if __name__ == "__main__":
	while(1):
		q_string = input()
		result = query_sent(q_string)
		print(result)