from spider import get_name
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)


@app.route('/stock')
def add_numbers():
    a = request.args.get('a', 'iflytek-a', )
    result=get_name(a)
    # print(result)
    return jsonify(result=result)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()