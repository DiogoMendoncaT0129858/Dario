print("-----Começe uma conversa!-----")
user = str(input())

match user:
    case u if "Ola" in user or "Bom Dia" in user:
        print("Saudações!")
    case u if "?" in user:
        print("Pergunta")
    case u if "tchau" in user or "adeus" in user:
        print("Despedida")
    case _:
        print("Mensagem generica")

