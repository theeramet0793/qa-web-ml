#server side
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

#==== Import =======================================================
from WordTokenize import word_tokenize

#===================================================================
#design resource
app = Flask(__name__)
api = Api(app)
CORS(app)

if __name__ == "__main__":
    app.run(debug=True)
    #Change debug to false when deploy