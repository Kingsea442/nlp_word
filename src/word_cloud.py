import src.constant
from file_utils import FileUitls
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


lines = FileUitls.reade_lines(src.constant.result_file)

result_cn = ''
word_freq = {}
for l in lines:
    l = str.replace(l, '\n', '')
    split = l.split(' ')
    word_freq[split[0]] = float(split[1])

w = WordCloud(background_color='white', width=800, height=450, scale=2)
w.generate_from_frequencies(word_freq)
w.to_file("top_500_word.jpg")