from nltk.tokenize import RegexpTokenizer

import nltk

def text_tokenizer(text):
    stemmer = nltk.stem.RSLPStemmer()
    lower_case = text.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(lower_case)
    return [stemmer.stem(t) for t in tokens]
