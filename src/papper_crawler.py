import json

import requests
import constant

paper_ids = ['5e42416ae4b7745e164e6382','5c2ec74ec085a550e9237ac2','5a420e82c5e0db08308b4573','5963231fc5e0dbc9048b4568','597fdb1dc5e0db551a8b4567','5981735dc5e0db21748b4567','59828541c5e0db8e2d8b4567','5983eaadc5e0db26798b4567','598415f3c5e0dbe6058b4567','59883a61c5e0dba1558b4567','598aa068c5e0db31568b4567']
paper_request_url = 'https://ktiku.doxue.com/port/paper/getPaper?callback=jQuery1910669929729173304_1605606764006&uid=0&paperID={}&record_id=&_=1605606764007'

file_parent_path = constant.paper_data_file_path

def convert_json(paper):
    left = str.find(paper, '(') + 1
    right = str.rfind(paper, ')')
    json_str = paper[left:right]
    paper_data = json.loads(json_str)
    return paper_data

def parse_title(paper):
    return paper['data']['paper']['paper']

def parse_reading(paper):
    result = []
    questions = paper['data']['paper']['questions']
    all_reading = ''
    for q in questions:
        for item in q:
            question_type = item['question_type']['question_type']
            if '阅读理解'.__eq__(question_type) or '完形填空'.__eq__(question_type):
                all_reading = all_reading +  item['question'] + ' '
                result.append(item['question'])
    return result

def write_to_file(file_path, reading_content):
    f = open(file_path, mode='w', encoding='utf-8')
    f.write(reading_content)
    f.close()


for id in paper_ids:
    url = str.format(paper_request_url, id)
    print(url)
    response = requests.get(url)
    result = bytes.decode(response.content)
    paper_data = convert_json(result)

    # papaer_data = scraper.response(url).content
    title = parse_title(paper_data)
    reading = parse_reading(paper_data)
    i = 0
    for r in reading:
        file_path = file_parent_path + title + '_' + str(i)
        write_to_file(file_path, r)
        i = i + 1
        print(str.format('progress:{}', i))
