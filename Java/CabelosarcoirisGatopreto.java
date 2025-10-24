package Java;

import java.io.IOException;
import java.util.Optional;

public class CabelosarcoirisGatopreto {

    // Códigos de Reset
    public static final String ANSI_RESET = "\u001B[0m";

    // Códigos de Cores (Texto)
    public static final String ANSI_BLACK = "\u001B[30m";
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_YELLOW = "\u001B[33m";
    public static final String ANSI_BLUE = "\u001B[34m";
    public static final String ANSI_PURPLE = "\u001B[35m";
    public static final String ANSI_CYAN = "\u001B[36m";
    public static final String ANSI_WHITE = "\u001B[37m";

    public static final String ANSI_BOLD = "\u001B[1m";
    public static final String ANSI_ITALIC = "\u001B[3m";
    public static final String ANSI_INVERT = "\u001B[7m";

    public void letters(String text, int time, int delay, Optional<String> style){

        String appliedStyle = style.orElse(ANSI_RESET);
        for(int i=0; i<text.length();i++){
            System.out.print(appliedStyle + text.charAt(i));
            try {
                Thread.sleep(time);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        System.out.println();
        try {
            Thread.sleep(delay);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

    public void rainbow(String text, int time, int delay){

        String[] colors = {
                ANSI_RED, ANSI_YELLOW, ANSI_GREEN,
                ANSI_CYAN, ANSI_BLUE, ANSI_PURPLE
        };

        for(int i=0; i<text.length();i++){
            System.out.print(colors[i % colors.length] + text.charAt(i) + ANSI_RESET);
            try {
                Thread.sleep(time);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }

        System.out.println();

        try {
            Thread.sleep(delay);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

    }

    public void clearScreen() {  
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

    public static void main(String[] args) {
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

        CabelosarcoirisGatopreto obj = new CabelosarcoirisGatopreto();

        obj.letters(line1, 60, 800, Optional.empty());
        obj.letters(line2, 50, 1000, Optional.of(ANSI_ITALIC + ANSI_CYAN));
        obj.rainbow(line3,60,100);
        obj.clearScreen();
        obj.letters(line4, 40, 0, Optional.of(ANSI_ITALIC));
        obj.clearScreen();
        obj.letters(line5, 70, 1500, Optional.of(ANSI_BOLD + ANSI_GREEN));
        obj.clearScreen();
        obj.letters(line6, 90, 1500, Optional.of(ANSI_ITALIC + ANSI_PURPLE));
        obj.rainbow(line7, 90, 1000);
        obj.letters(line8,90, 700, Optional.of(ANSI_ITALIC + ANSI_YELLOW));
        obj.rainbow(line9, 80, 1500);
        obj.clearScreen();
        obj.letters(line10,100, 1500, Optional.empty());
        obj.clearScreen();
        obj.letters(line11,50, 0, Optional.empty());
        obj.rainbow(line12, 80, 1500);
        obj.clearScreen();
        obj.letters(line13,40, 500, Optional.empty());
        obj.rainbow(line14, 80, 1000);
        obj.clearScreen();
        obj.letters(line15,80, 0, Optional.of(ANSI_ITALIC));
        obj.letters(line16,50, 1000, Optional.of(ANSI_ITALIC + ANSI_RED));

    }

}
