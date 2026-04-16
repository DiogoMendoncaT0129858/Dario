metd = str(input("Digite o metodo: ").upper())
cont = str(input("Digite o conteudo: "))

dic = {
    "metodo": metd,
    "conteudo": cont
}


match dic:
    case {"metodo": "GET", "conteudo": str()}:
        print("Requisição GET recebida")
    case {"metodo": "POST", "conteudo": c} if c != "":
        print("Requisição POST com dados válidos")
    case {"metodo": "POST", "conteudo": ""}:
        print("Requisição POST sem dados")
    case _:
        print("Metodo nao suportado")