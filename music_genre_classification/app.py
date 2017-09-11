# -*- coding: utf-8 -*-
from flask import Flask
from flask_restplus import Api
from flask_restplus import fields
from flask_restplus import Resource

from pandas import DataFrame
from sklearn.externals import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

from text_utils import text_tokenizer

import pickle

# API settings
app = Flask(__name__)
api = Api(
    app,
    title='Music Genre Prediction API',
    description='An API which predicts the genre of a music based on its lyrics.',
    version='1.0'
)

ns = api.namespace('genre_precition', description='Predict music genre')

# Parser
parser = api.parser()
parser.add_argument(
    'SongLyrics',
    type=unicode,
    required=True,
    help='Full lyrics of the song in raw format, without any text treatment.',
    location='form'
)

# web app
resource_fields = api.model('Resource', {'result': fields.String})
@ns.route('/')
class MusicGenreApi(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    @api.expect(validate=False)
    def post(self):
        args = parser.parse_args()
        result = self.get_result(args)
        return result, 201

    def get_result(self, args):
        lyrics = args["SongLyrics"]
        with open('../model/vectorizer.pkl', 'rb') as f:
            tfidf = pickle.load(f)
        with open('../model/classifier.pkl', 'rb') as f:
            classifier = pickle.load(f)
        X = DataFrame(tfidf.transform([lyrics]).toarray())
        return {"result": classifier.predict(X)}

if __name__ == '__main__':
    app.run(debug=True)
