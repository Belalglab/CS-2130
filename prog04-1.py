def read_set(prompt):
    n = int(input(prompt + " number of elements: "))
    set_bits = 0
    for i in range(n):
        while True:
            try:
                value = int(input(f"Please enter element {i+1}: "))
                if 0 <= value <= 9:
                    set_bits |= 1 << value
                    break
                else:
                    print("Value entered is not allowed, please try again.")
            except ValueError:
                print("Invalid input, please enter an integer.")
    return set_bits

def display_set(s, name="Set"):
    """Displays the set elements from the bit representation."""
    elements = [str(i) for i in range(10) if s & (1 << i)]
    print(f"{name} = {{{','.join(elements)}}}")

def complement(s):
    """Returns the complement of the set."""
    return s ^ 0b1111111111

def union(a, b):
    """Returns the union of two sets."""
    return a | b

def intersection(a, b):
    """Returns the intersection of two sets."""
    return a & b

def difference(a, b):
    """Returns the difference of two sets (A - B)."""
    return a & ~b

def symmetric_difference(a, b):
    """Returns the symmetric difference of two sets."""
    return (a | b) & ~(a & b)

def main():
    print("CS 2130 - Computational Structures Waldo Wildcat")
    print("This program reads in the values of two sets and displays the results of several operations on the sets.\n")

    set_a = read_set("Please enter the number of elements in set A")
    set_b = read_set("Please enter the number of elements in set B")

    print("\nInput Sets")
    display_set(set_a, "Set A")
    display_set(set_b, "Set B")

    print("\nComplement of A")
    display_set(complement(set_a), "Complement of A")
    
    print("\nUnion of A and B")
    display_set(union(set_a, set_b), "Union of A and B")

    print("\nIntersection of A and B")
    display_set(intersection(set_a, set_b), "Intersection of A and B")

    print("\nDifference of A and B")
    display_set(difference(set_a, set_b), "Difference of A and B")

    print("\nSymmetric Difference of A and B")
    display_set(symmetric_difference(set_a, set_b), "Symmetric Difference of A and B")

if __name__ == "__main__":
    main()
