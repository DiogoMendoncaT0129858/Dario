user = input("Digite uma mensagem: ").strip().lower()

match user:
    case "ola" | "bom dia":
        print("Saudações")
    case m if m.endswith("?"):
        print("Pergunta")
    case m if "tchau" in m or "adeus" in m or "embora" in m:
        print("Despedida")
    case _:
        print("Mensagem muito generica")