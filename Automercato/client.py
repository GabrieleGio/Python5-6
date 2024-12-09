import requests,json
import sys

# Scrivere il programma client e server di un automercato in cui c'è una casa madre con un server e un database e le filiali.
# Il database contiene le seguenti tabelle:
# automobili
# motociclette
# accessori
# I servizi da implementare tenendo presente che il dialogo client/server avviene in json, sono:
# CercaAutomobile: il servizio fornisce l'elenco delle automobili che rispecchiano le richieste del cittadino che si rivolge alla filiale. 
# Ciascuna filiale è anche magazzino e quindi il rappresentante della filiale comunica 
# al cittadino se l'automobile è disponibile per essere vista oppure è disponibile in un altro magazzino
# Stesso servizio per le motociclette. 
# Il server è usato anche dalla divisione marketing della casa madre. In questo caso esiste un servizio che 
# fornisce, dati DATA INIZIO de DATA FINE, le vendite giornaliere di automobile e di motociclette per filiale. 
# I dati dell'interrogazione sono salvati sul client in un file json. 

base_url = "https://127.0.0.1:8080"
auth = False

def GetDatiAutomobile():
    targa = input("Qual'è la targa? ")
    modello = input("Qual'è il modello? ")
    colore = input("Qual'è il colore della macchina? ")
    datiAutomobile = {targa:{"modello":modello, "colore": colore}}
    return datiAutomobile

def GetAutomobile():
    return input("Inserisci la targa dell'automobile richiesta: ")

# def UpdateAutomobile():
#     dati_da_modifcare = [None for _ in range(3)]
#     dati_da_modifcare[0] = input("Inserisci il codice fiscale della persona a cui vuoi modificarei i dati: ")
#     nome = input("Inserisci il nome modificato (Lascia vuoto per non cambiare): ")
#     cognome = input("Inserisci il cognome modificato (Lascia vuoto per non cambiare): ")
#     dataN = input("Inserisci la data di nascita modificata (Lascia vuoto per non cambiare): ")
#     if cognome:
#         dati_da_modifcare[1] = cognome
#     if dataN:
#         dati_da_modifcare[2] = dataN
#     if nome:
#         dati_da_modifcare[3] = nome
#     return dati_da_modifcare

def DeleteAutomobile():
    return input("Inserisci la targa dell' automobile da eliminare: ")

#stato = -1

while True:
    print("Operazioni disponibili:")
    print("1. Inserisci automobile")
    print("2. Cerca automobile")
    print("3. Elimina automobile")
    print("4. Esci")
    sOper = input("Cosa vuoi fare? ")
    if sOper == "1":
        print("Richiesti dati dell'automobile")
        api_url = base_url + "/add_automobile"
        jsonDataRequest = GetDatiAutomobile()
        try:
            response = requests.post(api_url,json=jsonDataRequest, verify=False)
            print(response.content)
        
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")
    elif sOper == "2":
        print("Richiesta automobile")
        api_url = base_url + "/cerca_automobile"
        jsonDataRequest = GetAutomobile()
        try:
            response = requests.post(api_url,json=jsonDataRequest, verify=False)
            print(response.content)
            
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")

    elif sOper == "4":
        print("Richiesta automobile")
        api_url = base_url + "/delete_cittadino"
        jsonDataRequest = DeleteAutomobile()
        try:
            response = requests.post(api_url,json=jsonDataRequest, verify=False)
            print(response.content)
            
        except:
            print("Problemi di comunicazione con il server, riprova più tardi")
            
    elif sOper=="6":
        print("Buona giornata!")
        sys.exit()  
