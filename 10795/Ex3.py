print("Insere um tipo (Compra ou Venda) e valor: ")
userTipo = str(input("Tipo: "))
userInt = int(input("Valor: "))

coisa = {
    "tipo": userTipo,
    "valor": userInt
}

match userTipo:
    case "Compra" | "compra":
        print("Compra de ", coisa["valor"], "$")
    case "Venda" | "venda":
        print("Venda de ", coisa["valor"], "$")