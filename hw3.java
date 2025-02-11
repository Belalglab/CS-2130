//Belal Glab
def printBinary(theValue):
    """
    Function to print the binary representation of an integer.
    :param theValue: Integer value to be converted to binary.
    """
    for i in range(31, -1, -1):
        if (theValue >> i) & 1 > 0:
            print("1 ", end="")
        else:
            print("0 ", end="")
        if i % 8 == 0:
            print("  ", end="")  # Extra space for byte separation
    print("\n")

def main():
    print("Welcome to Waldo's Bitopia program\n")

    while True:
        try:
            number = int(input("Please enter an integer to display the bit representation: "))
            print("\nThe bit representation of", number, "is:")
            printBinary(number)

            choice = input("Enter Zero to quit, any other integer to do it again: ")
            if int(choice) == 0:
                break
        except ValueError:
            print("Please enter a valid integer.")
    
    print("\nThanks! Have a great day!!")

if __name__ == "__main__":
    main()
