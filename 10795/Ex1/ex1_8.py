op = str(input("Operação (+,-,*,/): ").strip().lower())
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))


match op:
    case "+":       
        print(num1 + num2)
    case "-":    
        print(num1 - num2)
    case "*": 
        print(num1 * num2)
    case "/":   
        if (num2 != 0):
            print(num1 / num2)
        else:
            print("Erro: divisão por zero")
    case _:            
        print("Operação nao existe")