from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('avaleht.html') # malli renderdamine
@app.route('/joogid', methods=['GET', 'POST'])
def joogid():
        poed = {}
        valik = request.args.getlist('pood') or request.form.getlist('pood')
        if len(valik) == 1 and ',' in valik[0]:
            poed['pood'] = comma_separated_params_to_list(valik[0])
        else:
            poed['pood'] = valik
        print(poed)
        
        
        return render_template('joogid.html', poed2=valik)
@app.route('/joogid', methods=['GET', 'POST'])
def comma_separated_params_to_list(param):
    result = []
    for val in param.split(','):
        if val:
            result.append(val)
    return result
