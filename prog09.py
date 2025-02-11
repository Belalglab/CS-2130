#Belal Glab 
#Prog09 Test 
def recursive_fibonacci(n):
    """Recursive implementation of the Fibonacci sequence."""
    if n < 2:
        return n
    return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

def iterative_fibonacci(n):
    """Iterative implementation of the Fibonacci sequence."""
    if n < 2:
        return n
    n2, n1 = 0, 1
    for _ in range(2, n + 1):
        fib = n1 + n2
        n2, n1 = n1, fib
    return fib

def main():
    # Ask the user for input
    i = int(input("Please enter a value to determine the Fibonacci sequence element for: "))
    
    # Calculate and print the Fibonacci number using the recursive method
    print("The recursively determined result is: ")
    print(recursive_fibonacci(i))
    print()  # Print a newline for readability
    
    # Calculate and print the Fibonacci number using the iterative method
    print("The iterative value is: ")
    print(iterative_fibonacci(i))
    print()  # Print a newline for readability

if __name__ == "__main__":
    main()
