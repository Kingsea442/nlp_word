import os
import string

import nltk

import constant
from txt_utils import TxtUtils
file_parent_path = constant.paper_data_file_path

class PapperStopWords:
    def load_stop_words():
        stop_words_file = open(constant.paper_stop_words, 'r', encoding='utf-8')
        lines = stop_words_file.readlines()
        stop_words = []
        for l in lines:
            stop_words.append(str.replace(l, '\n', ''))
        return stop_words


if __name__ == '__main__':
    freq_dist = []
    dir = os.listdir(file_parent_path)
    all_papper_content = ''
    for f in dir:
        f_content = open(file_parent_path + f, 'r').read()
        f_content = TxtUtils.clean_txt(f_content)
        all_papper_content = all_papper_content + ' ' + f_content

    tokenize_words = nltk.word_tokenize(all_papper_content, language='english', preserve_line=True)
    freq_dist = nltk.FreqDist(tokenize_words)
    print(freq_dist.B())
    print(freq_dist.N())
    print(freq_dist.freq('the'))
    print(freq_dist.most_common())
    print(freq_dist.most_common(400))
    top_400_words = freq_dist.most_common(400)
    stop_words_line = ''
    for k,v in top_400_words:
        stop_words_line = stop_words_line + k + '\n'

    f = open(constant.paper_stop_words, 'w', encoding='utf-8')
    f.write(stop_words_line)
    f.close()

    words = PapperStopWords.load_stop_words()
    print(words)
