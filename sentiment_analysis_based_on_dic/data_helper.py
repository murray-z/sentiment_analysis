# -*- coding: utf-8 -*-

"""
@Time    : 2018/11/4 11:47
@Author  : fazhanzhang
@Function :
"""

import json

sentiment_path = './data/sentimentDict.json'
stopwords_path = './data/stopwords.txt.json'
degree_path = './data/degreeDict.json'
not_path = './data/notDict.json'
jieba_dic_path = './data/jieba.dic'


def get_stopwords_json(file_path='./data/stopwords.txt'):
    with open(file_path, encoding='utf-8') as f:
        with open(stopwords_path, 'w', encoding='utf-8') as f_w:
            json.dump([line.strip() for line in f], f_w, ensure_ascii=False)


def get_degree_json(file_path='./data/degreeDict.txt'):
    ret = {}
    with open(degree_path, 'w', encoding='utf-8') as f_w:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                lis = line.strip().split()
                ret[lis[1]] = float(lis[0])+1
            json.dump(ret, f_w, ensure_ascii=False)


def get_not_json(file_path='./data/notDict.txt'):
    with open(not_path, 'w', encoding='utf-8') as f_w:
        with open(file_path, encoding='utf-8') as f:
            ret = {word: -1 for word in f.read().strip().split()}
            json.dump(ret, f_w, ensure_ascii=False)


def get_sentiment_json(file_path='./data/sentimentDict.txt'):
    ret = {}
    with open(sentiment_path, 'w', encoding='utf-8') as f_w:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    lis = line.strip().split()

                    ret[lis[0]] = float(lis[1])
            json.dump(ret, f_w, ensure_ascii=False)


def load_json(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as f:
        return json.loads(f.read(), encoding='utf-8')


def get_jieba_dict():
    jieba = []
    sentiments = load_json(sentiment_path).keys()
    degrees = load_json(degree_path).keys()
    nots = load_json(not_path).keys()
    jieba.extend(sentiments)
    jieba.extend(degrees)
    jieba.extend(nots)
    with open(jieba_dic_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(jieba))


if __name__ == '__main__':
    get_stopwords_json()
    get_degree_json()
    get_not_json()
    get_sentiment_json()
    get_jieba_dict()