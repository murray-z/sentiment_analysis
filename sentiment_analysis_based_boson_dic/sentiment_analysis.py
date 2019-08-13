# -*- coding: utf-8 -*-


import jieba


class SentimentAnalysisBoson():
    def __init__(self, sentiment_path='./BosonNLP_sentiment_score.txt'):
        self.sentiment_path = sentiment_path
        self.sent_dict = self.load_sentiment_dict()
        self.sent_words = self.sent_dict.keys()
        for word in self.sent_words:
            jieba.add_word(word)

    def load_sentiment_dict(self):
        ret = {}
        with open(self.sentiment_path, encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    lis = line.strip().split()
                    ret[lis[0].lower()] = float(lis[1])
        return ret

    def analysis(self, text):
        score = 0.
        text = text.lower()
        words = jieba.lcut(text)
        for word in words:
            score += self.sent_dict.get(word, 0)
        return score


if __name__ == '__main__':
    sent_analysis = SentimentAnalysisBoson()
    print(sent_analysis.analysis("小明今天心情不错哦"))
    print(sent_analysis.analysis("今天天气很晴朗，阳光明媚"))
    print(sent_analysis.analysis("good, nice"))
    print(sent_analysis.analysis("他看上去有点失落"))
