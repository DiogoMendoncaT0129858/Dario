soma = 0
cont = 0

print("Introduza 30 numeros pares entre 1 e 50:")

while cont < 30:
    num = int(input("Numero " + str(cont + 1) + ": "))
    
    if (num >= 1 and num <= 50 and num % 2 == 0):
        soma = soma + num
        cont = cont + 1
    else:
        print("Invalido. \nDeve ser par e estar entre 1 e 50.")

media = soma / 30

print("\nMedia dos 30 numeros pares: " + str(round(media, 2)))