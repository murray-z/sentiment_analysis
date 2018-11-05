# -*- coding: utf-8 -*-

"""
@Time    : 2018/11/5 19:50
@Author  : fazhanzhang
@Function :
"""


import json
import jieba.analyse
import jieba

sentiment_path = './data/sentimentDict.json'
stopwords_path = './data/stopwords.txt.json'
degree_path = './data/degreeDict.json'
not_path = './data/notDict.json'
jieba_dic_path = './data/jieba.dic'


jieba.load_userdict(jieba_dic_path)


class SentimentAnalysis():
    def __init__(self):
        self.sentiment_score_dic = self.load_json(sentiment_path)
        self.degree_score = self.load_json(degree_path)
        self.notwords = self.load_json(not_path)

    def load_json(self, json_file_path):
        with open(json_file_path, 'r', encoding='utf-8') as f:
            return json.loads(f.read(), encoding='utf-8')

    def analysis(self, sentence):
        words = jieba.lcut(sentence)
        score = self.sentiment_score_dic.get(words[0], 0)
        if len(words) > 1:
            score += self.sentiment_score_dic.get(words[1], 0) * self.notwords.get(words[0], 1) * self.degree_score.get(words[0], 1)
            if len(words) > 2:
                for i in range(2, len(words)):
                    score += self.sentiment_score_dic.get(words[i], 0) * self.notwords.get(words[i-1], 1) * \
                             self.degree_score.get(words[i-1], 1) * self.degree_score.get(words[i-2], 1) * \
                             self.notwords.get(words[i-2], 1)
        if score < 0:
            return {'negative': score}
        if score > 0:
            return {'positive': score}
        return {'middle': score}


if __name__ == '__main__':
    sentiment_analysis = SentimentAnalysis()
    print(sentiment_analysis.analysis('小明今天非常不开心'))
    print(sentiment_analysis.analysis('本来这一分都不想给的，这是我从苹果5使用到这最差的一款手机，新机@的过程中死机，传说中的不怕锤子，轻轻的掉地下就这样了，这是一万多的手机吗，信号差死，放了一张电信卡网络就很慢，除了开机快点，其他也没啥'))
    print(sentiment_analysis.analysis('客观的说，价值一万多的手机硬件方面还有很多需要改进的地方，但是苹果的系统就是牛啊，没办法，相机比安卓的好用太多，它没有在屏占比上浪费时间，而是花更多的时间来优化用户体验，做更有意义的事。就拿双卡的放置方式来说，值得学习～'))

