#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json

import constant



class BaiduTranslate:
    appid = constant.baidu_translate_appid
    secretKey = constant.baidu_translate_secretKey

    httpClient = None
    myurl = '/api/trans/vip/translate'
    fromLang = 'auto'  # 原文语种
    toLang = 'zh'  # 译文语种

    word_translate_cache = {}

    word_translate_cache_file = open(constant.translate_cache, 'r', encoding='utf-8')
    lines = word_translate_cache_file.readlines()
    for l in lines:
        l = str.replace(l, '\n', '')
        split = str.split(l, ' -> ')
        word_translate_cache[split[0]] = split[1]


    def __init__(self) -> None:
        super().__init__()

    def write_to_file(self, file_path, translate_result):
        f = open(file_path, mode='a', encoding='utf-8')
        f.write(translate_result)
        f.close()

    def translate(self, q):
        result = self.word_translate_cache.get(q)
        if result is not None:
            return result

        salt = random.randint(32768, 65536)
        sign = self.appid + q + str(salt) + self.secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = self.myurl + '?appid=' + self.appid + '&q=' + urllib.parse.quote(q) + '&from=' + self.fromLang + '&to=' + self.toLang + '&salt=' + str(salt) + '&sign=' + sign
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            cn = result['trans_result'][0]['dst']
            self.word_translate_cache[q] = cn
            self.write_to_file(constant.translate_cache, str.format('{} -> {} \n', q, cn))
            return cn

        except Exception as e:
            print (e)
        finally:
            if httpClient:
                httpClient.close()