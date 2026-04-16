status = input("Digite o status: ").lower()
tempRes = int(input("Digite o tempo de resposta: "))

servidor = {
    "status": status,
    "tempo_resposta": tempRes
}

match servidor:
    case {"status": "ok", "tempo_resposta": t} if t > 200:
        print("Servidor lento")
    case {"status": "ok"}:
        print("Servidor ativo")
    case {"status": "erro"}:
        print("Servidor indisponível")
    case _:
        print("Estado desconhecido")