prod = str(input("Digite o categoria: "))
valor = int(input("Digite o preco: "))

dic = {
    "categoria": prod,
    "preco": valor
}


match dic:
    case {"categoria": "eletronico", "preco": p} if p > 1000:
        print("Produto de luxo")
    case {"categoria": "eletronico", "preco": p} if p <= 1000:
        print("Produto comum")
    case {"categoria": "alimento", "preco": int()}:
        print("Produto alimentar")
    case _:
        print("Categoria desconhecida")