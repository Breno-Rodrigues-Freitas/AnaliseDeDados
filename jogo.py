import random
import os

def limpar_tela():
    """Limpa a tela do terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_cabecalho():
    """Exibe o cabeçalho do jogo"""
    print("=" * 50)
    print("🎮 BEM-VINDO AO JOKENPÔ! 🎮".center(50))
    print("=" * 50)
    print()

def exibir_opcoes():
    """Exibe as opções de forma mais organizada"""
    print("📋 OPÇÕES DISPONÍVEIS:")
    print("-" * 30)
    print("  [ 1 ] ✊ PEDRA")
    print("  [ 2 ] ✋ PAPEL")
    print("  [ 3 ] ✌️ TESOURA")
    print("-" * 30)
    print()

def obter_escolha_jogador():
    """Obtém e valida a escolha do jogador"""
    while True:
        try:
            escolha = input("👉 Digite o número da sua escolha (1-3): ")
            escolha_int = int(escolha)
            
            if 1 <= escolha_int <= 3:
                return escolha_int - 1  # Converte para índice 0-2
            else:
                print("❌ Por favor, digite um número entre 1 e 3!\n")
        except ValueError:
            print("❌ Entrada inválida! Digite apenas números!\n")

def exibir_escolhas(jogador_idx, computador_idx, options):
    """Exibe as escolhas de forma visual"""
    icones = ["✊", "✋", "✌️"]
    
    print("\n" + "=" * 40)
    print(" RESULTADO ".center(40, "="))
    print(f"🧑 VOCÊ: {options[jogador_idx].upper()} {icones[jogador_idx]}")
    print(f"🤖 COMPUTADOR: {options[computador_idx].upper()} {icones[computador_idx]}")
    print("=" * 40)

def determinar_vencedor(jogador_idx, computador_idx):
    """Determina quem ganhou e retorna o resultado"""
    if jogador_idx == computador_idx:
        return "empate"
    elif (jogador_idx == 0 and computador_idx == 2) or \
         (jogador_idx == 1 and computador_idx == 0) or \
         (jogador_idx == 2 and computador_idx == 1):
        return "jogador"
    else:
        return "computador"

def exibir_resultado(resultado):
    """Exibe o resultado de forma visual"""
    print()
    if resultado == "empate":
        print(" 🤝 EMPATE! 🤝 ".center(40, "!"))
        print("Tente novamente!".center(40))
    elif resultado == "jogador":
        print(" 🎉 VOCÊ GANHOU! 🎉 ".center(40, "!"))
        print("Parabéns! 👏".center(40))
    else:
        print(" 💻 COMPUTADOR GANHOU! 💻 ".center(40, "!"))
        print("Mais sorte na próxima! 🍀".center(40))
    print()

def jogar_novamente():
    """Pergunta se o jogador quer jogar novamente"""
    print("-" * 40)
    resposta = input("🔄 Quer jogar novamente? (s/n): ").lower().strip()
    return resposta == 's' or resposta == 'sim'

def jogar():
    """Função principal do jogo"""
    while True:
        limpar_tela()
        exibir_cabecalho()
        
        options = ["pedra", "papel", "tesoura"]
        
        exibir_opcoes()
        
        # Jogador escolhe
        jogador_idx = obter_escolha_jogador()
        
        # Computador escolhe aleatoriamente
        computador_idx = random.randint(0, 2)
        
        # Exibe as escolhas
        exibir_escolhas(jogador_idx, computador_idx, options)
        
        # Determina e exibe o resultado
        resultado = determinar_vencedor(jogador_idx, computador_idx)
        exibir_resultado(resultado)
        
        # Pergunta se quer jogar novamente
        if not jogar_novamente():
            print("\n" + "=" * 40)
            print(" OBRIGADO POR JOGAR! 👋 ".center(40, "="))
            print(" Até a próxima! ".center(40))
            print("=" * 40)
            break

# Inicia o jogo
if __name__ == "__main__":
    jogar()
