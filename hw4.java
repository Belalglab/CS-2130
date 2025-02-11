// Belal Glab
import java.util.Scanner;

public class Homework {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Part 1: Bubble Sort
        System.out.print("Enter the number of elements: ");
        int n = scanner.nextInt();
        int[] array = new int[n];

        System.out.println("Enter " + n + " integers:");
        for (int i = 0; i < n; i++) {
            array[i] = scanner.nextInt();
        }

        bubbleSort(array);

        System.out.println("Sorted array:");
        for (int num : array) {
            System.out.print(num + " ");
        }
        System.out.println();

        // Part 2: Counting Letters
        scanner.nextLine(); // Clear buffer
        System.out.print("Please enter your string: ");
        String inputString = scanner.nextLine();
        int[] letterArray = countLetters(inputString);

        System.out.println("\nLetter frequencies:");
        System.out.println(" A  B  C  D  E  F  G  H  I  J  K  L  M  N  O  P  Q  R  S  T  U  V  W  X  Y  Z");
        for (int count : letterArray) {
            System.out.print(" " + count);
        }
        System.out.println();

        scanner.close();
    }

    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            boolean didSwap = false;
            for (int j = n - 1; j > i; j--) {
                if (arr[j] < arr[j - 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j - 1];
                    arr[j - 1] = temp;
                    didSwap = true;
                }
            }
            if (!didSwap)
                break;
        }
    }

    public static int[] countLetters(String str) {
        int[] letterArray = new int[26];
        for (char c : str.toCharArray()) {
            if (Character.isLetter(c)) {
                letterArray[Character.toUpperCase(c) - 'A']++;
            }
        }
        return letterArray;
    }
}
