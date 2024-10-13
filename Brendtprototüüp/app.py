from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('avaleht.html') # malli renderdamine
@app.route('/joogid', methods=['GET', 'POST'])
def joogid():
    
        poed = {}
        joogidC = ["vesi", "coca-cola", "jäätis"]
        joogidR = ["limpa", "marinaad", "süütevedelik"]
        joogidS = ["maasikad", "kolmteist", "vs"]
        joogidP = ["pepsi", "leonardo", "plastiliin"]
        tooted = []
        
        
        valik = request.args.getlist('pood') or request.form.getlist('pood')
        if len(valik) == 1 and ',' in valik[0]:
            poed['pood'] = comma_separated_params_to_list(valik[0])
        else:
            poed['pood'] = valik
        print(poed)
        
        for l in range(len(valik)):
            if valik[l] == "Coop":
                for m in range(len(joogidC)):
                    tooted.append(joogidC[m])
                    
            if valik[l] == "Rimi":
                for m in range(len(joogidR)):
                    tooted.append(joogidR[m])
                    
                    
            if valik[l] == "Selver":
                for m in range(len(joogidS)):
                    tooted.append(joogidS[m])
                    
            
            if valik[l] == "Prisma":
                for m in range(len(joogidP)):
                    tooted.append(joogidP[m])

        return render_template('joogid.html', poed2=valik, tooted2=tooted)
        
@app.route('/joogid', methods=['GET', 'POST'])
def comma_separated_params_to_list(param):
    result = []
    for val in param.split(','):
        if val:
            result.append(val)
    return result
