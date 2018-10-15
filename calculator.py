from flask import Flask, request
from flask import jsonify
import time

app = Flask(__name__)

@app.route('/calculus', methods=['GET'])
def getCalculus():
    start = time.time()
    max_distance_km = 300
    query = request.args.get('query')

    if query is None:
        raise InvalidParam("Missing parameter \"query\"")

    try:
        result = eval(query)
    except:
        raise InvalidParam("Could not parse query \"%s\"" % (query))

    end = time.time()
    print("query time", end - start)

    return jsonify({ 'error': False, 'result': result})

if __name__ == '__main__':
    app.run()

# Error handler
##########
class InvalidParam(Exception):
    def __init__(self, message):
        Exception.__init__(self)
        self.message = message
    def to_dict(self):
        return {'message': self.message, 'error': True}

@app.errorhandler(InvalidParam)
def handle_invalid_param(error):
    response = jsonify(error.to_dict())
    response.status_code = 400
    return response
