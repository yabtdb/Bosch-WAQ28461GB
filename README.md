Karel
Mathias
Brendt

Probleem on järgnev: 

Elanikud peavad parima hinna leidmiseks otsima läbi kõikide erinevate toidukaupluste e-poed. See on ajakulukas ning on vaja paremat viisi. Selleks otsustasime otsida üles populaarsemate poodide populaarsemate toodete hinnad ja panna need üles ühele veebilehele.

Brendt ja Mathias tegelevad rohkem programmi backendiga ja Karel frontendiga.

Projekti pealkiri: DrinkViewer

Projekti lühikirjeldus on järgnev: 

Teeme veebilehe, kus on võimalik otsida erinevatest joogikateooriatest kõige odavam liitri hinnaga jook. Nt "karastusjoogid" ja leiad sealt nimekirjast, et kõige odavam on fanta. Näitab, millistes populaarsemates toidupoes on otsitud joogi hind kõige odavam.

Trello: https://trello.com/invite/b/66e00a7c36bd292eca0f253c/ATTIff4b8b9924d3b65616eeb76630047fc7AB838BA2/bosch

paberprototüüp: https://www.canva.com/design/DAGQWWuHJ8M/rXpP0hlUgv9oEL1ioxkmow/edit?utm_content=DAGQWWuHJ8M&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

Karel: 

veebilehe link: https://karel696969.pythonanywhere.com/avaleht.html

Disainin avalehe, teen headeri, loon nuppe, lisasin pildid ja jookide nimed

JUHEND: Mine leheküljele  https://karel696969.pythonanywhere.com/avaleht.html (hetkel ei tööta, vajab parandust), kuid teised alamleheküljed  https://karel696969.pythonanywhere.com/vesi.html  https://karel696969.pythonanywhere.com/karastusjoogid.html ja  https://karel696969.pythonanywhere.com/alkohol.html töötavad

Brendt: Tegin flaskiga nupu, millega saab teisele lehele ning poe filtreerimise süsteemi. Programm on leitav Brendtprototüüp kaustast.

Juhend:

Vajalik on Flask'i moodul.

Tuleb alla tõmmata app.py, avaleht.html ja joogid.html ning need peab panema samasse kausta. 
avaleht.html ja joogid.html tuleb panna eraldi kausta nimega "templates" (nagu ka Brendtprototüüp kaustas).
Siis saab tööle panna app.py programmi.

Avalehelt saab minna edasi teisele lehele, kus saab valid poe/poed ning see tagastab igale poele omased joogid. 

Mathias: Tegin andmete failist lugemise flaskis

JUHEND:
1. Vajalik Flask'i moodul
2. "mathias_prot kaustas on drinking.zip kaust, see tuleb alla laadida ja vajutada "extract all"(kaustas on drinking kaust, milles on on templates kaust, app.py ja joogid.txt fail).
3. Kõik failid peavad asetsema täpselt nii nagu on Mathiase "drinking" kaustas.
4. Käivitada tuleb app.py ja valida tuleb alumine veebiaadress:
   * Running on http://127.0.0.1:5000
   * Running on http://192.168.1.199:5000 <- näeb välja midagi sellist

Tulemuseks on failist lugemine, kus öeldakse, mis joogid on millistes poodides saadaval, koos hindadega. 



