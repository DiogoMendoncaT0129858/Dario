import os 
os.system("cls")

p1Name = " "
p2Name = " "
player1 = "Nada"
player2 = "Nada"
vic = "Noone"

print("PEDRA!\nPAPEL!\nTESOURA!")
p1Name = input("Insira o seu nome, P1!: ")
p2Name = input("Insira o seu nome, P2!: ")

while vic == "Noone":
    player1 = input(f"{p1Name} escolha Pedra, Papel ou Tesoura: ")
    os.system("cls")
    player2 = input(f"{p2Name} escolha Pedra, Papel ou Tesoura: ")
    os.system("cls")
    match player1:
        case "Papel":
            match player2:
                case "Pedra":
                    vic = "Papel > Pedra"
                    print(f"{p1Name}, WINS!, {vic}")
                case "Tesoura":
                    vic = "Tesoura > Papel"
                    print(f"{p2Name}, WINS!, {vic}")
                case "Papel":
                    vic = "Papel = Papel"
                    print("DRAW! ", vic)
        case "Pedra":
            match player2:
                case "Tesoura":
                    vic = "Pedra > Tesoura"
                    print(f"{p1Name}, WINS!, {vic}")
                case "Papel":
                    vic = "Papel > Pedra"
                    print(f"{p2Name}, WINS!, {vic}")
                case "Pedra":
                    vic = "Pedra = Pedra"
                    print("DRAW! ", vic)
        case "Tesoura":
            match player2:
                case "Papel":
                    vic = "Tesoura > Papel"
                    print(f"{p1Name}, WINS!, {vic}")
                case "Pedra":
                    vic = "Pedra > Tesoura"
                    print(f"{p2Name}, WINS!, {vic}")
                case "Tesoura":
                    vic = "Tesoura = Tesoura"
                    print("DRAW! ", vic)

