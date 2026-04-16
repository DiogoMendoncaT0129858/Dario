notas = []
for i in range(10):
    nota = float(input("Nota do aluno ", i+1, ":" ))
    notas.append(nota)

media = sum(notas) / 10

for nota in notas:
    if (nota >= media):
      acima_media += 1  

print(f"Média: {media:.2f}")
print("Alunos com nota igual ou acima da média: ", acima_media)