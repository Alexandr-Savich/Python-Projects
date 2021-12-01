import collections
from typing import Iterable


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


if __name__ == '__main__':
    countvec = CountVectorizer()
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    print(countvec.fit_transform(corpus))
    print(countvec.get_feature_names())
    print(countvec.get_feature_names_by_text())
