import os
from flask import Flask, render_template, request
app = Flask(__name__)

def loe_failist(failinimi):
    joogid = []
    failitee = os.path.join(app.root_path, 'static', failinimi)
    with open(failitee) as fail:
        for rida in fail:
            osad = rida.strip().split(',')
            joogid.append(osad)
    return joogid

@app.route('/')
def index():
    return render_template('avaleht.html')

@app.route('/avaleht.html')
def avaleht():
    return render_template('avaleht.html')

@app.route('/alkohol.html', methods=['GET', 'POST'])
def alkohol():
    alkohol = loe_failist('alkohol.txt')
    alkohol.sort()
    valik = request.args.getlist('pood') or request.form.getlist('pood')


    return render_template('alkohol.html', alkohol = alkohol, poed2 = valik)

@app.route('/karastusjoogid.html', methods=['GET', 'POST'])
def karastusjoogid():
    karastusjoogid = loe_failist('karastusjoogid.txt')
    karastusjoogid.sort()
    valik = request.args.getlist('pood') or request.form.getlist('pood')

    return render_template('karastusjoogid.html', karastusjoogid = karastusjoogid, poed2 = valik)

@app.route('/vesi.html', methods=['GET', 'POST'])
def vesi():
        joogid = loe_failist('vesi.txt')
        joogid.sort()
        valik = request.args.getlist('pood') or request.form.getlist('pood')

        return render_template('vesi.html', vesi=joogid, poed2 = valik)

if __name__ == '__main__':
    app.run()

