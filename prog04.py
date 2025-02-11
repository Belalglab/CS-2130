## Belal Glab
def read_set(prompt):
    while True:
        try:
            n = int(input(f"Please enter the number of elements in {prompt}: "))
            if n < 0 or n > 10:
                print("The number of elements should be between 0 and 10.")
                continue
            set_bits = 0
            for i in range(n):
                while True:
                    element = int(input(f"Please enter element {i+1}: "))
                    if 0 <= element <= 9:
                        set_bits |= 1 << element
                        break
                    else:
                        print("Value entered is not allowed, please try again.")
            return set_bits
        except ValueError:
            print("Invalid input. Please enter an integer.")

def complement(set_bits):
    return ~set_bits & 0b1111111111

def union(set_a, set_b):
    return set_a | set_b

def intersection(set_a, set_b):
    return set_a & set_b

def difference(set_a, set_b):
    return set_a & ~set_b

def symmetric_difference(set_a, set_b):
    return (set_a | set_b) & ~(set_a & set_b)

def display_set(operation, set_bits):
    elements = [str(i) for i in range(10) if set_bits & (1 << i)]
    print(f"{operation} = {{{','.join(elements)}}}")

def main():
    print("CS 2130 - Computational Structures  Waldo Wildcat")
    print("This program reads in the values of two sets and displays the results of several operations on the sets.\n")
    
    set_a = read_set("set A")
    set_b = read_set("set B")

    print("\nInput Sets")
    display_set("Set A", set_a)
    display_set("Set B", set_b)

    print("\nResults")
    display_set("Complement of A", complement(set_a))
    display_set("Union of A and B", union(set_a, set_b))
    display_set("Intersection of A and B", intersection(set_a, set_b))
    display_set("Difference of A and B", difference(set_a, set_b))
    display_set("Symmetric Difference of A and B", symmetric_difference(set_a, set_b))

if __name__ == "__main__":
    main()
