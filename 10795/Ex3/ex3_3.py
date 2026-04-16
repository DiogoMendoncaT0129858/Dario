soma = 0

for i in range(10):
    nota = float(input(f"Nota Nº{i+1} (0-20): "))
    soma += nota

media = soma / 10
print(f"Média: {media:.2f}")