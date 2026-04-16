print("ASCII de 0 a 255\n")

i = 0
while i <= 255:
    
    linha = ""
    for j in range(20):
        if (i > 255):
            break
        linha = linha + str(i) + ": " + chr(i) + "   "
        i = i + 1
    
    print(linha)
    
    if (i <= 255):
        input("\nPressione ENTER para ver os próximos 20 códigos")

print("\nTabela concluída.")