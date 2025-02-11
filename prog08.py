# Define a function to check if a number is prime.
def is_prime(n):
    """Check if a number is prime."""
    # Prime numbers are greater than 1.
    if n <= 1:
        return False  # Not prime if less than or equal to 1.
    # Check for factors from 2 to the square root of n.
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:  # If n is divisible by i, it's not prime.
            return False
    return True  # If no factors were found, n is prime.

# Define a function to compute the greatest common divisor using Euclid's algorithm.
def gcd(a, b):
    """Compute the greatest common divisor using Euclid's algorithm."""
    # Keep replacing a and b with b and a%b until b becomes zero.
    while b:
        a, b = b, a % b  # The magic step that performs the modulo operation.
    return a  # When b is 0, a is the gcd.

# Define a function to compute the least common multiple using the relationship between gcd and lcm.
def lcm(a, b, gcd_value):
    """Compute the least common multiple using Theorem 5."""
    # The lcm is the product of the numbers divided by their gcd.
    return abs(a*b) // gcd_value  # Use integer division for a whole number.

# Main program function.
def main():
    # Greet the user and explain what the program does.
    print("This program reads in two integers and determines if they are prime.")
    print("It then computes the greatest common divisor of the two integers using Euclid's Algorithm.")

    # Ask the user to input two integers.
    a = int(input("Enter the first integer: "))
    b = int(input("Enter the second integer: "))

    # Determine if the entered numbers are prime.
    is_a_prime = is_prime(a)
    is_b_prime = is_prime(b)

    # Tell the user whether each number is prime or not.
    print(f"{a} is {'a prime' if is_a_prime else 'not a prime'} number.")
    print(f"{b} is {'a prime' if is_b_prime else 'not a prime'} number.")

    # Compute the greatest common divisor (gcd) of the two numbers.
    gcd_value = gcd(a, b)
    # Compute the least common multiple (lcm) of the two numbers using the gcd.
    lcm_value = lcm(a, b, gcd_value)

    # Print out the gcd and lcm to the user.
    print(f"The gcd({a}, {b}) is {gcd_value}.")
    print(f"The lcm({a}, {b}) is {lcm_value}.")

# Calling the main funcation
if __name__ == "__main__":
    main()
