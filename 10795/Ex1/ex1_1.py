day = input("Digite o dia da semana: ").strip().lower()

match day:
    case "sábado" | "sabado" | "domingo":
        print("Fim de semana")
    case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
        print("Dia de Semana")
    case _:
        print("Esse dia nao existe!")