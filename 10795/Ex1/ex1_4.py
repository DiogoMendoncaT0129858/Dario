valor = eval(input("Digite o valor: "))

match valor:
    case int():          
        print("Numero Inteiro")
    case float():        
        print("Numero Decimal")
    case str() if valor.isdigit(): 
        print("String Numerica")
    case str():          
        print("String de Texto")
    case list():        
        print("Lista")
    case _:              
        print("Esse tipo nao existe")