# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 19:50:46 2019

@author: eagle
"""
from sklearn.feature_extraction.text import TfidfVectorizer


def tfidf_similarity_matrix(texts):
    tvec = TfidfVectorizer()
    vectors = tvec.fit_transform(texts)
    return (vectors * vectors.T).A[0, 1]


corpus = ["None of that is important right now", "That's not important right now"]
#corpus = [i.split(' ') for i in corpus]

print(tfidf_similarity_matrix(corpus))