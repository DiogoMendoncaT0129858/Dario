num = int(input("Introduza um numero int positivo: "))

if num <= 1:
    print("Por favor, introduza um numero maior que 1.")
else:
    som = 0
    sub = 0
    multi = 1
    contOp = 0

    for i in range(1, num):
        som = som + i
        sub = sub - i
        multi = multi * i
        contOp = contOp + 1

    print("\nResultados para o numero " + str(num))
    print("Soma: " + str(som))
    print("Subtração: " + str(sub))
    print("Multiplicação: " + str(multi))
    print("numero de operações realizadas: " + str(contOp))