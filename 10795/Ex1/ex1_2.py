nota = int(input("Digite a nota (0-100): "))

match nota:
    case n if nota >= 90: 
        print("Excelente")
    case n if nota >= 70: 
        print("Bom")
    case n if nota >= 50: 
        print("Suficiente")
    case _:            
        print("Insuficiente")