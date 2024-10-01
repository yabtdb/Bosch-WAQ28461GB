from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('avaleht.html') # malli renderdamine
@app.route('/joogid', methods=['GET', 'POST'])
def joogid():
    return render_template('joogid.html')
    selected_options = request.form.getlist('checkbox')
    print(selected_options)
    return f'Selected options: {", ".join(selected_options)}'

if __name__ == '__main__':
    app.run()
