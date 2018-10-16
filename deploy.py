from flask import Flask, request
from flask import jsonify
from string_to_val import calculate
from exceptions import InvalidParam
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1> testaus 8 </h1>"

@app.route('/calculus', methods=['GET'])
def getCalculus():
    query = request.args.get('query')
    if query is None:
        raise InvalidParam("Missing parameter \"query\"")

    result = calculate(query)

    return jsonify({ 'error': False, 'result': result})

if __name__ == '__main__':
    app.run()

@app.errorhandler(InvalidParam)
def handle_invalid_param(error):
    response = jsonify(error.to_dict())
    response.status_code = 400
    return response
