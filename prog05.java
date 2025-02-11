//Belal Glab
import java.util.HashMap;
import java.util.HashSet;
import java.util.Scanner;

public class FunctionChecker {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter the number of ordered pairs:");
        int n = scanner.nextInt();
        
        HashMap<Integer, Integer> functionMap = new HashMap<>();
        HashSet<Integer> domainSet = new HashSet<>();
        HashSet<Integer> rangeSet = new HashSet<>();
        
        boolean isValid = true;
        
        System.out.println("Enter each pair as two integers separated by a space (x y):");
        for (int i = 0; i < n; i++) {
            int x = scanner.nextInt();
            int y = scanner.nextInt();
            
            // Check for domain and range validity
            if (x < 1 || x > 5 || y < 1 || y > 5) {
                System.out.println("Invalid domain or range. Please enter values between 1 and 5.");
                i--; // Decrement to retake the input
                continue;
            }
            
            if (functionMap.containsKey(x)) {
                isValid = false;
                break;
            } else {
                functionMap.put(x, y);
                domainSet.add(x);
                rangeSet.add(y);
            }
        }
        
        if (!isValid) {
            System.out.println("This function is not a valid function.");
            return;
        }
        
        boolean isOneToOne = functionMap.size() == new HashSet<>(functionMap.values()).size();
        boolean isOnto = rangeSet.size() == 5;
        boolean isBijection = isOneToOne && isOnto;
        
        System.out.println("Function described by:");
        functionMap.forEach((x, y) -> System.out.println("f(" + x + ") = " + y));
        
        System.out.println("\nThis function is a valid function.");
        if (isOneToOne) {
            System.out.println("This function is a one-to-one function.");
        } else {
            System.out.println("This function is not a one-to-one function.");
        }
        
        if (isOnto) {
            System.out.println("This function is onto.");
        } else {
            System.out.println("This function is not onto.");
        }
        
        if (isBijection) {
            System.out.println("This function is a bijection.");
        } else {
            System.out.println("This function is not a bijection.");
        }
    }
}
