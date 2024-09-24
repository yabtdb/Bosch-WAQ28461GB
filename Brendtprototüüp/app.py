from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('avaleht.html') # malli renderdamine
@app.route('/joogid')
def joogid():
    return render_template('joogid.html')
if __name__ == '__main__':
    app.run()
