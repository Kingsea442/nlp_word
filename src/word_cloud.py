from wordcloud import WordCloud

import src.constant
from file_utils import FileUitls

lines = FileUitls.reade_lines(src.constant.result_file)

result_cn = ''
word_freq = {}
for l in lines:
    l = str.replace(l, '\n', '')
    split = l.split(' ')
    word_freq[split[0]] = float(split[1])

w = WordCloud(background_color='white', width=800, height=450, scale=1.5)
w.generate_from_frequencies(word_freq)
w.to_file("top_word.jpg")