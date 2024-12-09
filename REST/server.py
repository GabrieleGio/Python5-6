from flask import Flask, jsonify, request
from myjson import JsonDeserialize, JsonSerialize

api = Flask(__name__)


file_path_cittadini = "anagrafe.json"
file_path_utenti = "utenti.json"
cittadini = JsonDeserialize(file_path_cittadini)
utenti = JsonDeserialize(file_path_utenti)

@api.route('/add_cittadino', methods=['POST'])
def GestisciAddCittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        if login_utente():
            jsonReq = request.json
            codice_fiscale = jsonReq.get('codice_fiscale')
            if codice_fiscale in cittadini:
                return jsonify({"Esito": "200", "Msg": "Cittadino già esistente"}), 200
            else:
                cittadini[codice_fiscale] = jsonReq
                JsonSerialize(cittadini, file_path_cittadini) 
                return jsonify({"Esito": "200", "Msg": "Cittadino aggiunto con successo"}), 200
        else:
            return jsonify({"Esito": "200", "Msg": "Login fallito","login":False}), 200
    else:
        return 'Content-Type non supportato!'

@api.route('/read_cittadino/<codice_fiscale>', methods=['GET'])
def read_cittadino(codice_fiscale):
    if login_utente():
        cittadino = cittadini.get(codice_fiscale)
        if cittadino:
            return jsonify({"Esito": "200", "Msg": "Cittadino trovato", "Dati": cittadino}), 200
        else:
            return jsonify({"Esito": "404", "Msg": "Cittadino non trovato"}), 404
    else:
        return jsonify({"Esito": "200", "Msg": "Login fallito","login":False}), 200
    
@api.route('/update_cittadino', methods=['POST'])
def update_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        if login_utente():
            jsonReq = request.json
            codice_fiscale = jsonReq.get('codice_fiscale')
            if codice_fiscale in cittadini:
                cittadini[codice_fiscale] = jsonReq
                JsonSerialize(cittadini, file_path_cittadini)  
                return jsonify({"Esito": "200", "Msg": "Cittadino aggiornato con successo"}), 200
            else:
                return jsonify({"Esito": "404", "Msg": "Cittadino non trovato"}), 404
        else:
            return jsonify({"Esito": "200", "Msg": "Login fallito","login":False}), 200
    else:
        return 'Content-Type non supportato!'

@api.route('/elimina_cittadino', methods=['POST'])
def elimina_cittadino():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        if login_utente():
            cod = request.json.get('codice_fiscale')
            if cod in cittadini:
                del cittadini[cod]
                JsonSerialize(cittadini, file_path_cittadini)  
                return jsonify({"Esito": "200", "Msg": "Cittadino rimosso con successo"}), 200
            else:
                return jsonify({"Esito": "404", "Msg": "Cittadino non trovato"}), 404
        else:
            return jsonify({"Esito": "200", "Msg": "Login fallito","login":False}), 200
    else:
        return 'Content-Type non supportato!'
    

@api.route('/login_utente', methods=['POST'])
def login_utente():
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':  
        JsonReq = request.json
        nomeutente = next(iter(JsonReq))
        passwordutente = JsonReq[nomeutente]
        if nomeutente in utenti:
            if utenti[nomeutente] == passwordutente:
                return jsonify({"Esito": "200", "Msg": "Utente loggato con successo","login":True}), 200
            else:
                return jsonify({"Esito": "200", "Msg": "Nome utente trovato ma password errata","login":False}), 200
        else:
            return jsonify({"Esito": "200", "Msg": "Nome utente non trovato nel database","login":False}), 200
    else:
        return 'Content-Type non supportato!'
            

api.run(host="127.0.0.1", port=8080, ssl_context='adhoc')
