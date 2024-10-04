import json
def Serializza(diz:dict,file_path):
    try:
        dizstringa = json.dumps(diz)
        with open(file_path, 'w') as file:
            file.write(dizstringa)
        print("File json scritto correttamente")
        return True
    except Exception as e:
        print(e)
        return False
    

def Deserializza(file_path:str):
    try:
        with open (file_path,"r") as file:
            dizionario = json.load(file)
            print
            return dizionario
    except Exception as e:
        print(e)
        return None