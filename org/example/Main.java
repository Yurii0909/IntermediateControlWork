import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Raffle r = new Raffle();
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.print(
                    "Main menu:\n" +
                            "1 - Add a new toy into the prize fund\n" +
                            "2 - Change the frequency of dropping out some toy\n" +
                            "3 - Hold a raffle and save results\n" +
                            "0 - EXIT\n" +
                            "> ");
            var selection = sc.next();
            switch (selection) {
                case "1":
                    r.addToy();
                    break;
                case "2":
                    r.setFrequency();
                    break;
                case "3":
                    r.raffle();
                    break;
                case "0":
                    System.out.println("Bye");
                    System.exit(0);
                default:
                    System.out.println("Incorrect selection. Try again.");
                    break;
            }
        }
    }
}