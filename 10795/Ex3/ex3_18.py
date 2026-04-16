limite = int(input("Ate que numero quer verificar numeros perfeitos? "))

print("\nNumeros perfeitos encontrados até " + str(limite) + ":")

quant = 0

for num in range(1, limite + 1):
    somDiv = 0
    
    for div in range(1, num):
        if (num % div) == 0:
            somDiv = somDiv + div
    
    if (somDiv == num):
        print(str(num) + " é um numero perfeito!")
        quant = quant + 1

print("\nTotal de numeros perfeitos encontrados: " + str(quant))