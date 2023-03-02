#server side
from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from ClassProcessing import Process

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Process,"/start-one-process") 

if __name__ == "__main__":
    app.run(debug=True, port=5001)
    #Change debug to false when deploy
    
    
    
    