from flask import Flask, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

## Resource class
class Post(Resource):
    def post(self):
        print(request.json)        
        return request.json, 201
    def get(self, prueba):
        return prueba,200

##
## Actually setup the Api resource routing here
##
api.add_resource(Post,'/dummy','/dummy/<prueba>')

if __name__ == '__main__':
    app.run(host='0.0.0.0',ssl_context=('localhost.cert','localhost.key'))