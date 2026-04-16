num1 = int(input("Primeiro = "))
num2 = int(input("Segundo = "))
num3 = int(input("Terceiro = "))

if (num1 > num2 > num3):
    numMaior = num1
    numMenor = num3
elif (num2 > num1 > num3):
    numMaior = num2
    numMenor = num3    
elif (num1 > num3 > num2):
    numMaior = num1
    numMenor = num2    
elif (num3 > num1 > num2):
    numMaior = num3
    numMenor = num2  
elif (num2 > num3 > num1):
    numMaior = num2
    numMenor = num1    
elif (num3 > num2 > num1):
    numMaior = num3
    numMenor = num1 

print("Maior: ", numMaior)
print("Menor: ", numMenor)