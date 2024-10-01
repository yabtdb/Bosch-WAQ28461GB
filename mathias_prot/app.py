from flask import Flask

app = Flask(__name__)


@app.route('/')

@app.route('/avaleht')

def hhh():
    fail = open("joogid.txt", encoding="UTF-8")
    for rida in fail:
        rida= rida.strip()
    return rida


if __name__ == '__main__':
    app.run()