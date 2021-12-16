import collections
from typing import Iterable

import math


class CountVectorizer:
    stop_words = ('am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'a',
                  'an', 'the', 'while', 'of', 'at', 'by', 'for', 'with')

    "Class that transforms words into vector using 'bag of words' model"

    def __init__(self, lowercase: bool = True):
        self.lowercase = lowercase
        self.punct_marks = (',', '?', '!', ';', ':')
        self.vocabulary = collections.defaultdict(int)
        self.ngrams = []
        self.names1 = []

    def fit_transform(self, corpus: Iterable) -> list:
        """"Создает словарь терминов"""
        bag = []
        for ind, doc in enumerate(corpus):
            if self.lowercase:
                doc = doc.lower()
                corpus[ind] = doc
            for mark in self.punct_marks:
                doc = doc.replace(mark, ' ')
                corpus[ind] = doc
            bag_of_words = doc.split()
            bag.append(list(bag_of_words))

            for word in bag_of_words:
                self.vocabulary[word] += 1

            self.ngrams.append(list.copy(list(self.vocabulary.values())))
            name = [key for key in self.vocabulary.keys() if self.vocabulary[key] > 0]
            self.names1.append(name)

            for key in self.vocabulary:
                self.vocabulary[key] = 0

        for ngram in self.ngrams:
            for i in range(len(self.vocabulary) - len(ngram)):
                ngram.append(0)
        return self.ngrams

    def get_feature_names(self):
        return list(self.vocabulary.keys())

    def get_feature_names_by_text(self):
        return self.names1


def tf_transform(list_of_ngrams: []) -> []:
    list_of_freq = []
    for ngram in list_of_ngrams:
        freqs = []
        s = sum(ngram)
        freqs = [round(x / s, 3) for x in ngram]
        list_of_freq.append(freqs)
    return list_of_freq


def idf(matrix):
    num_docs = float(len(matrix) + 1)
    idfs = []
    counter = 0
    for word_num in range(len(matrix[0])):
        for vec in matrix:
            if vec[word_num] > 0:
                counter += 1
        idfs.append(math.log(num_docs / (counter + 1)) + 1)
        counter = 0

    return idfs


def transform(matrix):
    vectors = tf_transform(matrix)
    idfs = idf(matrix)
    tfidf = []
    tfidfs = []
    c = 0

    for vec in vectors:
        for indx, el in enumerate(vec):
            c = el * idfs[indx]
            tfidfs.append(c)
        tfidf.append(tfidfs)
    return tfidf

class TfidfTransformer():
    def fit_transform(self, matrix):
        tf = transform(matrix)
        idf = idf(matrix)

        tf_idf = []
        for text in tf:
            tf_idf.append([round(a * b, 3) for a, b in zip(text, idf)])

        return tf_idf


class TfidfVectorizer(CountVectorizer):
    def __init__(self) -> None:
        super().__init__()
        self._tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        count_matrix = super().fit_transform(corpus)
        return self._tfidf_transformer.fit_transform(count_matrix)
    
    
if __name__ == '__main__':
    countvec = CountVectorizer()
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste',

    ]
    matrix = CountVectorizer().fit_transform(corpus)
    print(tf_transform(matrix))

    print(idf(matrix))

print(transform(matrix))
