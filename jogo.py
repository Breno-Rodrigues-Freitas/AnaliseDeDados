import random

def jogar():
    print("Welcome to Jokenpol")

    options = ["pedra", "papel", "tesoura"]

    print("Options On")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")

    escolha_jogador = input("Digite sua escolha: ")

    # Computador escolhe entre 0, 1, 2 (índices da lista)
    escolha_computador = random.randint(0, 2)

    # Converter escolha do jogador (1,2,3) para índice (0,1,2)
    jogador_idx = int(escolha_jogador) - 1

    print(f"Você escolheu: {options[jogador_idx]}")
    print(f"Computador escolheu: {options[escolha_computador]}")

    # Lógica com índices 0,1,2
    if jogador_idx == escolha_computador:
        print("EMPATE!!!")
    elif (jogador_idx == 0 and escolha_computador == 2) or \
         (jogador_idx == 1 and escolha_computador == 0) or \
         (jogador_idx == 2 and escolha_computador == 1):
        print("VOCÊ GANHOU!! PARABÉNS!!")
    else:
        print("COMPUTADOR GANHOU!!!")

jogar()

