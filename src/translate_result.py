import src.constant
from file_utils import FileUitls
from baidu_transalte import BaiduTranslate

lines = FileUitls.reade_lines(src.constant.result_file)
b_translate = BaiduTranslate()

result_cn = ''
for l in lines[0:500]:
    l = str.replace(l, '\n', '')
    split = l.split(' ')
    word = split[0]
    cn = b_translate.translate(word)
    line = str.format('{} {} {}\n', word, cn, split[1])
    result_cn  = result_cn + line
    print(word, cn)
FileUitls.write(result_cn, src.constant.result_cn_file)
