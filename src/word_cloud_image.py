import src.constant
from file_utils import FileUitls
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


lines = FileUitls.reade_lines(src.constant.result_file)

result_cn = ''
word_freq = {}
for l in lines[0:500]:
    l = str.replace(l, '\n', '')
    split = l.split(' ')
    word_freq[split[0]] = float(split[1])
print(word_freq)
color_mask = np.array(Image.open("/Users/wlh/asea/workspace/python/nlp_word/data/sxc.png"))

w = WordCloud(mask=color_mask, background_color='white', width=1000, height=1000)
w.generate_from_frequencies(word_freq)
image_colors = ImageColorGenerator(color_mask)

# 在只设置mask的情况下 会得到一个拥有图片形状的词云 axis默认为on 会开启边框
plt.imshow(w, interpolation="bilinear")
plt.axis("on")
plt.savefig("a.jpg")
# 直接在构造函数中直接给颜色 这种方式词云将会按照给定的图片颜色布局生成字体颜色策略
plt.imshow(w.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("on")
plt.savefig("w_i.jpg")
w.to_file("w.jpg")