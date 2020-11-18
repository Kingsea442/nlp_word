from __future__ import division

import math
# from nltk.book import *
import os
import re
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from txt_utils import TxtUtils
from file_utils import FileUitls

import constant
from stopwords import PapperStopWords

def df(txt):
    tokenize_words = word_tokenize(txt, language='english', preserve_line=True)
    filter_tokenize_word = [w for w in tokenize_words if not w in stop_words]
    fdist = nltk.FreqDist(filter_tokenize_word)
    total_word_count = fdist.B()
    items = fdist.items()
    for k, v in items:
        tf = v / total_word_count
        if tf > 0.1:
            print(k, tf)

def dist(txt):
    tokenize_words = word_tokenize(txt, language='english', preserve_line=True)
    filter_tokenize_word = [w for w in tokenize_words if not w in stop_words]
    freq_dist = nltk.FreqDist(filter_tokenize_word)
    most_common = freq_dist.most_common(math.ceil(len(freq_dist)/3))
    # most_common = freq_dist.most_common(50)
    for k, v in most_common:
        stop_words.add(k)
    filter_tokenize_word = [w for w in tokenize_words if not w in stop_words]
    return nltk.FreqDist(filter_tokenize_word)

def count_word_document(word, document_freq_dists):
    count = 0
    for fd in document_freq_dists:
        if fd.get(word) is not None:
            # count = count + 1
            count = count + fd.get(word)
    return count

def top200(word_dict):
    for k, v in word_dict.items():
        if v > 0.01 and v < 0.1:
            print(k, v)


if __name__ == '__main__':
    file_parent_path = constant.paper_data_file_path

    stop_words = set(stopwords.words('english'))
    for word in PapperStopWords.load_stop_words():
        stop_words.add(word)

    dir = os.listdir(file_parent_path)
    document_count = len(dir)
    print(document_count)

    freq_dist = []
    for f in dir:
        f_content = open(file_parent_path + f, 'r').read()
        f_content = TxtUtils.clean_txt(f_content)
        fd = dist(f_content)
        freq_dist.append(fd)

    word_tf_idf = {}
    word_freq = {}
    for fd in freq_dist:
        items = fd.items()
        total_word_count = fd.N()

        for k, v in items:
            tf = v / total_word_count

            word_in_document_count = count_word_document(k, freq_dist)
            idf = math.log((document_count / (word_in_document_count + 1)))

            tf_idf = tf * idf  + math.log(min(10, len(k)))

            word_tf_idf[k] = [tf, idf, tf_idf]
    result = sorted(word_tf_idf.items(), key=lambda d: d[1][2])
    result.reverse()

    lemmatizer = WordNetLemmatizer()
    for k, v in result:
        k = lemmatizer.lemmatize(k)
        if len(k) >= 4:
            word_freq[k] = v[2]
            print(k,  v)

    final_result = ''
    for k, v in word_freq.items():
        line = str.format('{} {}\n', k, round(v, 7))
        final_result = final_result + line
    FileUitls.write(final_result, constant.result_file)