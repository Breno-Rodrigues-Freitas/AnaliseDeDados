import java.util.Scanner;
import java.util.Random;

public class PedraPapelTesoura {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int jogador;
        int computador;

        System.out.println("=== Pedra, Papel e Tesoura ===");
        System.out.println("1 - Pedra");
        System.out.println("2 - Papel");
        System.out.println("3 - Tesoura");
        System.out.print("Escolha uma opção: ");

        jogador = scanner.nextInt();

        computador = random.nextInt(3) + 1;

        System.out.println("Computador escolheu: " + computador);

        if (jogador == computador) {
            System.out.println("Empate!");
        } 
        else if ((jogador == 1 && computador == 3) ||
                 (jogador == 2 && computador == 1) ||
                 (jogador == 3 && computador == 2)) {
            System.out.println("Você venceu!");
        } 
        else {
            System.out.println("Computador venceu!");
        }

        scanner.close();
    }
}