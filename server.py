from counter import counter
from flask import Flask, request


app = Flask(__name__)


@app.route('/', methods=['GET'])
def post_route():
    if request.method == 'GET':
        answer = counter.count_fd()
        try:
            
            if answer.isdigit:
                return f'{answer}\n'

        except:
            print(answer)
            return f'Internal error, check console log\n'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
