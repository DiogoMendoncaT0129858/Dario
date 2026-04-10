print("Insira um dia: ")
day = input()

match day:

    case "Segunda" | "Terca" | "Quarta" | "Quinta" | "Sexta":
        print("Dia de Semana")
    case "Sabado" | "Domingo":
        print("Fim de Semana")
    case _:
        print("Tem de inserir com a primeira letra capitalizada")

    