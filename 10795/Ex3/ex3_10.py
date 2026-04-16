num = int(input("Digite um numero: "))
div = 0
for i in range(1, num+1):
    if (num % i == 0):
        div += 1
        
print("O numero ", num, " tem " ,div," divisores.")