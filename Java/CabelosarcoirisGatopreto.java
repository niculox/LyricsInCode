package Java;

import java.io.IOException;

public class CabelosarcoirisGatopreto {

    // --- Constantes ANSI
    public static final String ANSI_RESET = "\u001B[0m";
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_YELLOW = "\u001B[33m";
    public static final String ANSI_BLUE = "\u001B[34m";
    public static final String ANSI_PURPLE = "\u001B[35m";
    public static final String ANSI_CYAN = "\u001B[36m";
    public static final String ANSI_ITALIC = "\u001B[3m";
    public static final String ANSI_BOLD = "\u001B[1m";

    /**
     * Imprime um texto letra por letra com um estilo opcional.
     * Esta é a versão "completa" do método.
     *
     * @param text O texto a ser impresso.
     * @param charDelayMs O delay em milissegundos entre cada caractere.
     * @param postLineDelayMs O delay em milissegundos após a linha terminar.
     * @param style O código de estilo ANSI (ex: ANSI_RED + ANSI_BOLD).
     */
    public void letters(String text, int charDelayMs, int postLineDelayMs, String style) {

        System.out.print(style);

        for (char c : text.toCharArray()) {
            System.out.print(c);
            sleepMs(charDelayMs); 
        }

        System.out.print(ANSI_RESET);
        System.out.println();
        sleepMs(postLineDelayMs); 
    }


    public void letters(String text, int charDelayMs, int postLineDelayMs) {
        letters(text, charDelayMs, postLineDelayMs, ""); 
    }


    public void rainbow(String text, int charDelayMs, int postLineDelayMs) {
        String[] colors = {
                ANSI_RED, ANSI_YELLOW, ANSI_GREEN,
                ANSI_CYAN, ANSI_BLUE, ANSI_PURPLE
        };

        int i = 0;
        for (char c : text.toCharArray()) {
            System.out.print(colors[i % colors.length] + c + ANSI_RESET);
            sleepMs(charDelayMs);
            i++;
        }

        System.out.println();
        sleepMs(postLineDelayMs);
    }

    public static void clearScreen() {  
        try {
            String os = System.getProperty("os.name");

            if (os.contains("Windows")) {
                // Comando para Windows (cls)
                new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
            } else {
                // Comando para Linux/macOS (clear)
                new ProcessBuilder("clear").inheritIO().start().waitFor();
            }
        } catch (IOException | InterruptedException e) {
            // Tratar erros, se houver
            e.printStackTrace();
        }
    }

    private void sleepMs(int milliseconds) {
        if (milliseconds <= 0) return; 
        try {
            Thread.sleep(milliseconds);
        } catch (InterruptedException e) {
            e.printStackTrace();
            Thread.currentThread().interrupt();
        }
    }

    public void executarRoteiro() {
        String line1 = "é o rei da batidinha";
        String line2 = "kamaitachi";
        String line3 = "cabelos arco-íris";
        String line4 = "tô só ensaiando viu pai";
        String line5 = "vamo assim ó";
        String line6 = "Me perdi no abismo e voltei";
        String line7 = "Teu amor diminui minha vontade de querer morrer";
        String line8 = "Teu abraço é como um terapeuta que vem socorrer";
        String line9 = "Todos os medos que eu guardo mesmo sem querer";
        String line10 = "Estou te esperando na calçada";
        String line11 = "Bem em frente sua casa";
        String line12 = "Nessa bela madrugada";
        String line13 = "Vamos sentar nesse meio-fio";
        String line14 = "E tentar encontrar a estrela D'alva";
        String line15 = "E esquecer que segunda-feira, no caso";
        String line16 = "Amanhã, já tem aula";

        letters(line1, 60, 800);
        letters(line2, 50, 1000, ANSI_ITALIC + ANSI_CYAN);
        rainbow(line3, 60, 100);
        clearScreen();
        letters(line4, 40, 0, ANSI_ITALIC);
        clearScreen();
        letters(line5, 70, 1500, ANSI_BOLD + ANSI_GREEN);
        clearScreen();
        letters(line6, 90, 1500, ANSI_ITALIC + ANSI_PURPLE);
        rainbow(line7, 90, 1000);
        letters(line8, 90, 700, ANSI_ITALIC + ANSI_YELLOW);
        rainbow(line9, 80, 1500);
        clearScreen();
        letters(line10, 100, 1500);
        clearScreen();
        letters(line11, 50, 0);
        rainbow(line12, 80, 1500);
        clearScreen();
        letters(line13, 40, 500);
        rainbow(line14, 80, 1000);
        clearScreen();
        letters(line15, 80, 0, ANSI_ITALIC);
        letters(line16, 50, 1000, ANSI_ITALIC + ANSI_RED);
    }

    public static void main(String[] args) {
        CabelosarcoirisGatopreto printer = new CabelosarcoirisGatopreto();
        printer.executarRoteiro();
    }

}