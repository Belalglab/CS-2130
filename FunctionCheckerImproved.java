import java.util.HashMap;
import java.util.HashSet;
import java.util.InputMismatchException;
import java.util.Scanner;

public class FunctionCheckerImproved {

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        System.out.println("Enter the maximum value for the domain and range:");
        int maxValue = readPositiveInteger();
        
        System.out.println("Enter the number of ordered pairs:");
        int n = readPositiveInteger();

        HashMap<Integer, Integer> functionMap = new HashMap<>();
        HashSet<Integer> domainSet = new HashSet<>();
        HashSet<Integer> rangeSet = new HashSet<>();

        System.out.println("Enter each pair as two integers separated by a space (x y):");
        for (int i = 0; i < n; i++) {
            System.out.println("Pair " + (i + 1) + ":");
            int[] pair = readOrderedPair(maxValue);
            if (pair == null) {
                i--; // Decrement to retake the input for this iteration
                continue;
            }

            int x = pair[0];
            int y = pair[1];
            
            // Store valid ordered pair and update domain/range sets
            functionMap.put(x, y);
            domainSet.add(x);
            rangeSet.add(y);
        }

        analyzeAndPrintFunctionProperties(functionMap, maxValue, domainSet.size(), rangeSet.size());
    }

    private static int readPositiveInteger() {
        while (true) {
            try {
                int value = scanner.nextInt();
                if (value > 0) {
                    return value;
                }
                System.out.println("Invalid input. Please enter a positive integer.");
            } catch (InputMismatchException e) {
                System.out.println("Invalid input. Please enter an integer.");
                scanner.next(); // Consume the invalid input
            }
        }
    }

    private static int[] readOrderedPair(int maxValue) {
        int x, y;
        try {
            x = scanner.nextInt();
            y = scanner.nextInt();

            if (x < 1 || x > maxValue || y < 1 || y > maxValue) {
                System.out.println("Invalid domain or range. Please enter values between 1 and " + maxValue + ".");
                return null;
            }
            return new int[]{x, y};
        } catch (InputMismatchException e) {
            System.out.println("Invalid input. Please enter two integers separated by a space.");
            scanner.nextLine(); // Clear the scanner buffer
            return null;
        }
    }

    private static void analyzeAndPrintFunctionProperties(HashMap<Integer, Integer> functionMap, int maxValue, int domainSize, int rangeSize) {
        boolean isOneToOne = functionMap.size() == new HashSet<>(functionMap.values()).size();
        boolean isOnto = rangeSize == maxValue;
        boolean isBijection = isOneToOne && isOnto;

        System.out.println("\nFunction described by:");
        functionMap.forEach((x, y) -> System.out.println("f(" + x + ") = " + y));

        System.out.println("\nThis function is valid.");
        System.out.println(isOneToOne ? "It is a one-to-one function." : "It is not a one-to-one function.");
        System.out.println(isOnto ? "It is onto." : "It is not onto.");
        System.out.println(isBijection ? "It is a bijection." : "It is not a bijection.");
    }
}
