from time import time 

print("Insere estatus do servidor")
userTipo = str(input("Tipo: "))

timeMsStrt = int(time())

timeMsEnd = int(time())

coisaInt = (timeMsEnd - timeMsStrt)  / 1000

coisa = {
    "tipo": userTipo,
    "valor": coisaInt
}

print(coisa["valor"])