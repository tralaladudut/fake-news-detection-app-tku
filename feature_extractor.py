# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 22:07:34 2018

@author: su_xin
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
import preprocessing_text
from sklearn.externals import joblib

# count vectorize


def count_vectorizer(X_train, X_test):
    word_vectorizer = CountVectorizer(analyzer="word", preprocessor=None, lowercase=False,
                                      max_df=0.5, min_df=0.03, tokenizer=preprocessing_text.tokenization)
    X_train = word_vectorizer.fit_transform(X_train)
    X_test = word_vectorizer.transform(X_test)
    #print(word_vectorizer.get_feature_names())
    save_vectorizer(word_vectorizer)
    return X_train, X_test

# tf-idf


def tf_idf(X_train, X_test):
    tfidf = TfidfVectorizer(ngram_range=(1, 2), preprocessor=None, lowercase=False,
                            max_df=0.5, min_df=0.03, tokenizer=preprocessing_text.tokenization)
    X_train = tfidf.fit_transform(X_train)
    X_test = tfidf.transform(X_test)
    #print(tfidf.get_feature_names())
    save_vectorizer(tfidf)
    return X_train, X_test


def save_vectorizer(vectorizer):
    joblib.dump(vectorizer, 'vectorizer.pkl')
