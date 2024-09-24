import csv
from flask import Flask, render_template, request

api = Flask("__name__")
"""
utenti = [['mario','password1','M','0'],
          ['gianni','password2','M','0'],
          ['AnitaGaribaldi','pass3','F','0']
          ]
"""
with open('utenti.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        utenti = list(reader)
print("Tutti gli utenti")
print(utenti)
print("Un utente alla volta:")
for utente in utenti:
    print("Utente:")
    print(utente)
    print("Nome:")
    print(utente[0])
    print("Password:")
    print(utente[2])

@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@api.route('/index2', methods=['GET'])
def index2():
    nome = request.args.get("nome")
    cognome = request.args.get("cognome")
    password = request.args.get("password")
    sesso = request.args.get("sesso")
    numero = request.args.get("numero")
    with open('utenti.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        utenti = list(reader)
        
    for utente in utenti:
        if utente[0] == nome and utente[2] == password:
            print("Match found!")
            return render_template('errore.html')
    
        else:
            print(f"{nome} e {password} non trovato in {utenti}")
            print("Registrazione in corso...")
            with open('utenti.csv', 'a', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([nome, cognome, password, sesso, numero])
            return render_template('index2.html', nome=nome, cognome=cognome, password=password, sesso=sesso, numero=numero)

@api.route('/errore', methods=['GET'])
def index3():
    return render_template('errore.html')


api.run(host="0.0.0.0", port=8085)