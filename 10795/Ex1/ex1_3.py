pedido = eval(input("Digite o dicionário: "))

match pedido:
    case {"tipo": "compra", "valor": valor}:
        print("Compra de " ,valor,"€")
    case {"tipo": "venda", "valor": valor}:
        print("Venda de ", valor,"€")
    case _:
        print("Pedido desconhecido")