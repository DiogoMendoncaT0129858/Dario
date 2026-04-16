num1 = float(input("Nota1 = "))
num2 = float(input("Nota2 = "))
num3 = float(input("Nota3 = "))

media = (num1*2 + num2*3 + num3*5) / 10

print(f"Média: {media:.1f}")

if (media >= 6):
   print("Aprovado")
else:
   print("Reprovado")  
