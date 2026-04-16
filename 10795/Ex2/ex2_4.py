saldo = float(input("Saldo inicial: "))
cheque = float(input("Valor do cheque: "))

if (cheque <= saldo):
    saldo_atual = saldo - cheque
    print("Cheque descontado, saldo: ", saldo_atual)
else:
    print("Cheque não pode ser descontado")