nome = input("Nome do cliente: ")
cmpr = float(input("Valor da cmpr: "))

if (cmpr <= 200):
    descont = cmpr * 0.10
elif (cmpr <= 500):
    descont = cmpr * 0.15
else:
    descont = cmpr * 0.20

total = cmpr - descont

print(f"Nome: {nome}")
print(f"Compra: {cmpr:.2f}€")
print(f"Desconto: {descont:.2f}€")
print(f"Total a pagar: {total:.2f}€")