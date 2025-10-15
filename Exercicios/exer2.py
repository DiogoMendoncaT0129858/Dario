num1 = 0
num2 = 0
num3 = 0

num1 = int(input("Insira um numero: "))
num2 = int(input("Insira outro numero: "))
num3 = int(input("Insira mais um numero: "))

"""print(f"numero 1: {num1}")
print(type(num1))"""

print("Orden: \n")

if num1 > num2 > num3:
    print("Maior: ", num1, "\nMenor: ", num3)

elif num1 > num3 > num2:
    print("Maior: ", num1, "\nMenor: ", num2)

elif num2 > num1 > num3:
    print("Maior: ", num2, "\nMenor: ", num3)

elif num2 > num3 > num1:
    print("Maior: ", num2, "\nMenor: ", num1)

elif num3 > num2 > num1:
    print("Maior: ", num3, "\nMenor: ", num1)

elif num3 > num1 > num2:
    print("Maior: ", num3, "\nMenor: ", num2)


