def criaconta(numero,titular, saldo, limite):
    conta = {"numero" : numero,
             "titular" : titular,
             "saldo" : saldo,
             "limite" : limite
        }
    return conta

def deposita(conta,valor):
    conta["saldo"] += conta

def saca(conta,valor):
    conta["saldo"]-= conta

def extrato(conta):
    print("Saldo {}".format(conta["saldo"]))
