def Serializza(stringa:str)->list:
    lista = []
    for parola in stringa[1:-1].split(","): #Tolgo i doppi apici
        lista.append(parola[1:-1])
    return lista

def Deserializza(lista:list)->str:
    return "['" + "','".join(lista) + "']"

stringa = "['mario','giovanni','lucrezia']"
lista = ['mario','giovanni','lucrezia']

print(Serializza(stringa))
print(Deserializza(lista))
