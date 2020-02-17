from flask import Flask
from flask_restful import Api, Resource, reqparse, request


app = Flask(__name__)
api = Api(app)
app.config["DEBUG"] = True


@app.route('/ww_client', methods=['GET'])
def home():
    if 'id' in request.args:
        id = int(request.args['id'])
        print(id)
        return 'all good bro', 200
    else:
        return 'nope', 404


if __name__ == '__main__':
    app.run(debug=True)