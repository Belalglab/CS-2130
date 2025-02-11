def sum_range(val1, val2):
    """
    Recursively sums all integers in the range between val1 and val2, inclusive.
    Assumes val1 and val2 are integers.
    """
    # Ensure val1 is the larger number
    if val1 < val2:
        val1, val2 = val2, val1
    # Base case: if the range has only one number
    if val1 == val2:
        return val1
    # Recursive step
    return val1 + sum_range(val1 - 1, val2)

def print_rev_string(s, position=0):
    """
    Recursively prints the string s in reverse.
    """
    if position < len(s):
        print_rev_string(s, position + 1)
        print(s[position], end='')

def main():
    print("Please enter your range of integers (on one or more lines):")
    val1, val2 = map(int, input().split())
    print(f"The sum of all the integers from {val1} to {val2} is {sum_range(val1, val2)}")
    
    print("Please enter a string:")
    the_string = input()
    print("\nThe reverse of your input is:")
    print_rev_string(the_string)

if __name__ == "__main__":
    main()
