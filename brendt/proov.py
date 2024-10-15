from flask import Flask, render_template, request
app = Flask(__name__)

def loe_failist(failinimi):     # Defineerib funktsiooni, mis loeb andmeid antud failist
    joogid = []          # Loob tühja järjendi
    with open(failinimi) as fail:     # Avab faili ning suleb selle automaatselt peale sisu lugemist
        for rida in fail:           # Käib läbi iga rea failis
            osad = rida.strip().split(',')      # Eemaldab reast tühikud ja jagab selle komade kaupa osadeks
            joogid.append(osad)      # Lisab jaotatud osad järjendisse
    return joogid        # Tagastab järjendi

@app.route('/')
def avaleht():           # Definerrib funktsiooni
    joogid = loe_failist('joogid.txt')   # Kutsub esile funktsiooni, et lugeda andmeid failist 'joogid.txt'
    return render_template('avaleht.html', joogid = joogid)    # Edastab joogid 'avaleht.html' lehele

@app.route('/avaleht.html')
def index():
    return render_template('avaleht.html') # malli renderdamine
@app.route('/alkohol.html')
def alkohol():
    return render_template('alkohol.html')
@app.route('/karastusjoogid.html')
def karastusjoogid():
    return render_template('karastusjoogid.html')
@app.route('/vesi.html', methods=['GET', 'POST'])
def vesi():
    
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
            print(valik)
        
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

        
        return render_template('vesi.html', poed2=valik, tooted2=tooted)
if __name__ == '__main__':
    app.run()
