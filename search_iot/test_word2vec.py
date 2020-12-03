import os

import gensim


def test():
    model = gensim.models.KeyedVectors.load_word2vec_format('search_iot/model.vec', binary=False)
    while True:
        word = input()
        if word == ";;break": break
        result = [res[0] for res in model.most_similar(positive=word) if
                  res[1] > 0.70]  # model.most_similar(positive=[word])
        print(result)
