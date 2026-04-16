pare = 0
impare = 0
listNum = []

for i in range(10):
    num = float(input(f"Digite o {i+1}º: "))
    listNum.append(num)

for n in listNum:
    if (n % 2 == 0):
        pare += 1
    else:
        impare += 1    

print("Pares: ", pare)
print("Ímpares: ", impare)