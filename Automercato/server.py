from flask import Flask, json, request, render_template
import random
import os
import dbclient as db
import sys

api = Flask(__name__)
mydb = db.connect()
if mydb is None:
    print("Errore connessione al DB")
    sys.exit()
    

@api.route('/add_automobile', methods=['POST'])
def GestisciAddAutomobile():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        dati = request.json
        for key, value in dati.items():
            sQuery = f"insert into automobile(targa,modello,colore) values ('{key}', '{value['modello']}', '{value['colore']}')"
            iRetValue = db.write_in_db(mydb,sQuery)
            if iRetValue == -2:
                return "Targa già esistente"
            elif iRetValue == 0:
                return "Registrazione avvenuta con successo"
            else:
                return "Errore non gestito nella registrazione"
        return "Errore richiesta non conforme"
    else:
        return 'Content-Type not supported!'
    
    
@api.route('/cerca_automobile', methods=['POST'])
def GestisciCercaAutomobile():
    content_type = request.headers.get('Content-Type')
    print("Ricevuta chiamata " + content_type)
    if (content_type == 'application/json'):
        dati = request.json
        """with open("anagrafe.json") as json_file:
            cittadini = json.load(json_file)
        for key, value in cittadini.items():
            if dati == key:
                return cittadini[key]
        return "Cittadino non trovato"""
        sQuery = f"select * from automobile where codFisc = '{dati}'"
        iRetValue = db.read_in_db(mydb,sQuery)
        if iRetValue == 1:
            sValue = db.read_next_row(mydb)
            return sValue
        return "Cittadino non trovato"
    else:
        return 'Content-Type not supported!'
    

api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')   