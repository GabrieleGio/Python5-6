
import requests, json, sys


base_url = "https://172.20.140.152:8080"


def GetDatiCittadino():
    nome = input("Inserisci il nome: ")
    cognome = input("Inserisci il cognome: ")
    dataN = input("Inserisci la data di nascita (gg/mm/aaaa): ")
    codF = input("Inserisci il codice fiscale: ")
    datiCittadino = {
        "nome": nome, 
        "cognome": cognome, 
        "data di nascita": dataN, 
        "codice_fiscale": codF
    }
    return datiCittadino


def GetCodicefiscale():
    cod = input('Inserisci codice fiscale: ')
    return {"codice_fiscale": cod}

def GetDatiAdmin():
    nomeutente = input("Inserisci il nome utente: ")
    password = input("Inserisci la password: ")
    diz = {}
    diz[nomeutente] = password
    return diz

while True:
    print("\nOperazioni disponibili:")
    print("1. Login")
    print("2. Esci")
    try:
        sOper1 = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue

    if sOper1 == 1:
        print("Login utente")
        api_url = base_url + "/login_utente"
        jsonDataRequest = GetDatiAdmin()
        response = requests.post(api_url, json=jsonDataRequest, verify=False)
        jsonResp = response.json()
        login = jsonResp["login"]
        if login == True:
            print(response.json())
            break
        else:
            print(response.json())
            continue
    
    if sOper1 == 2:
        print("Buona giornata!")
        sys.exit()

    else:
        print("Operazione non disponibile, riprova.")



while True:
    print("\nOperazioni disponibili:")
    print("1. Inserisci cittadino")
    print("2. Richiedi cittadino")
    print("3. Modifica cittadino")
    print("4. Elimina cittadino")
    print("5. Esci")


    try:
        sOper = int(input("Cosa vuoi fare? "))
    except ValueError:
        print("Inserisci un numero valido!")
        continue


    if sOper == 1:
        print("Aggiunta cittadino")
        api_url = base_url + "/add_cittadino"
        jsonDataRequest = GetDatiCittadino()
        response = requests.post(api_url, json=jsonDataRequest, verify=False)

    # Richiesta dati cittadino
    elif sOper == 2:
        print("Richiesta dati cittadino")
        api_url = base_url + "/read_cittadino"
        jsonDataRequest = GetCodicefiscale()
        response = requests.get(api_url + "/" + jsonDataRequest['codice_fiscale'], verify=False)
        print(response.json())

    elif sOper == 3:
        print("Modifica cittadino")
        api_url = base_url + "/update_cittadino"
        jsonDataRequest = GetDatiCittadino()
        response = requests.post(api_url, json=jsonDataRequest, verify=False)
        print(response.json())


    elif sOper == 4:
        print("Eliminazione cittadino")
        api_url = base_url + "/elimina_cittadino"
        jsonDataRequest = GetCodicefiscale()
        response = requests.post(api_url, json=jsonDataRequest, verify=False)
        print(response.json())


    elif sOper == 5:
        print("Buona giornata!")
        sys.exit()
        

    else:
        print("Operazione non disponibile, riprova.")


#