//Belal 

import java.util.HashMap;
import java.util.HashSet;
import java.util.InputMismatchException;
import java.util.Scanner;

public class FunctionCheckerImproved {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Prompt user to specify the maximum value for the domain and range
        System.out.println("Enter the maximum value for the domain and range:");
        int maxValue;
        try {
            // Attempt to read the maximum value
            maxValue = scanner.nextInt();
        } catch (InputMismatchException e) {
            // Handle case where input is not an integer
            System.out.println("Invalid input. Please enter an integer.");
            return;
        }
        
        // Ask for the number of ordered pairs
        System.out.println("Enter the number of ordered pairs:");
        int n;
        try {
            // Attempt to read the number of pairs
            n = scanner.nextInt();
        } catch (InputMismatchException e) {
            // Handle non-integer input for the number of pairs
            System.out.println("Invalid input. Please enter an integer.");
            return;
        }
        
        // Initialize collections to store function mappings and unique domain/range values
        HashMap<Integer, Integer> functionMap = new HashMap<>();
        HashSet<Integer> domainSet = new HashSet<>();
        HashSet<Integer> rangeSet = new HashSet<>();
        
        boolean isValid = true;
        
        // Instructions for inputting ordered pairs
        System.out.println("Enter each pair as two integers separated by a space (x y):");
        for (int i = 0; i < n; i++) {
            int x, y;
            try {
                // Attempt to read the next ordered pair
                x = scanner.nextInt();
                y = scanner.nextInt();
            } catch (InputMismatchException e) {
                // Handle case where pair is not in the expected format
                System.out.println("Invalid input. Please enter two integers separated by a space.");
                scanner.nextLine(); // Clear the scanner buffer
                i--; // Decrement to retake the input for this iteration
                continue;
            }
            
            // Validate domain and range values against specified limits
            if (x < 1 || x > maxValue || y < 1 || y > maxValue) {
                System.out.println("Invalid domain or range. Please enter values between 1 and " + maxValue + ".");
                i--; // Retake input for this iteration
                continue;
            }
            
            // Check for existing domain value to maintain function validity
            if (functionMap.containsKey(x)) {
                isValid = false;
                break; // Exit loop if function is invalid
            } else {
                // Store valid ordered pair and update domain/range sets
                functionMap.put(x, y);
                domainSet.add(x);
                rangeSet.add(y);
            }
        }
        
        if (!isValid) {
            // Notify user if the input does not represent a valid function
            System.out.println("This function is not valid because it maps a single domain value to multiple range values.");
            return;
        }
        
        // Determine if function is one-to-one (injective) and onto (surjective)
        boolean isOneToOne = functionMap.size() == new HashSet<>(functionMap.values()).size();
        boolean isOnto = rangeSet.size() == maxValue; // Check if function covers the entire specified range
        boolean isBijection = isOneToOne && isOnto; // Check if function is both injective and surjective
        
        // Output the function mapping
        System.out.println("Function described by:");
        functionMap.forEach((x, y) -> System.out.println("f(" + x + ") = " + y));
        
        // Report findings about the function's properties
        System.out.println("\nThis function is valid.");
        if (isOneToOne) {
            System.out.println("It is a one-to-one function.");
        } else {
            System.out.println("It is not a one-to-one function.");
        }
        
        if (isOnto) {
            System.out.println("It is onto.");
        } else {
            System.out.println("It is not onto.");
        }
        
        if (isBijection) {
            System.out.println("It is a bijection.");
        } else {
            System.out.println("It is not a bijection.");
        }
    }
}
