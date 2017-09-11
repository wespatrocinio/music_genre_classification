from nltk.tokenize import RegexpTokenizer

import nltk

# Checking if the nltk dependecies are already satisfied. If not, downloads the dependencies
nltk.download('rslp')
nltk.download('stopwords')

def text_tokenizer(text):
    stemmer = nltk.stem.RSLPStemmer()
    lower_case = text.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(lower_case)
    return [stemmer.stem(t) for t in tokens]
