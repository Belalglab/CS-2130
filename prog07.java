import java.util.Scanner;

public class PrimeFactorization {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String answer;

        System.out.println("This program prints the prime factorization of positive integers");

        do {
            System.out.print("\nPlease enter a positive integer for prime factorization: ");
            int num = scanner.nextInt();

            if (num < 2) {
                System.out.println("Error: Please enter a number greater than 1.");
                continue;
            }

            System.out.print("The prime factorization of " + num + " is:\n\t");
            int k = num;

            // Prime factorization logic
            for (int i = 2; i * i <= num; i++) {
                while (k % i == 0) {
                    System.out.print(i + ", ");
                    k = k / i;
                }
            }
            if (k > 1) {
                System.out.println(k);
            } else {
                System.out.println(); 
            }

            System.out.print("Would you like to try another number (N for no, anything else is yes): ");
            answer = scanner.next();
        } while (!answer.equalsIgnoreCase("N"));

        System.out.println("Bye!!");
    }
}
