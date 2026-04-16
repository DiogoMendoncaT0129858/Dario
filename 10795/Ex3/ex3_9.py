while True:
    num = int(input("Digite um numero entre 1 e 100: "))
    if (1 <= num <= 100):
        print("Numero valido!")
        break
    else:
        print("Valor fora do intervalo")