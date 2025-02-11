#Belal 
#04/20/2024
def read_relation():
    """Reads ordered pairs until '0 0' is entered and returns a Boolean matrix and its size."""
    max_size = 20  # Maximum size for the relation
    relation = [[0] * max_size for _ in range(max_size)]
    size = 0

    while True:
        input_pair = input("Please enter the matrix as ordered pairs x y (0 0 to end matrix input): ")
        x, y = map(int, input_pair.split())
        if x == 0 and y == 0:
            break
        if x < 1 or y < 1 or x > max_size or y > max_size:
            print("Error: x and y must be between 1 and 20.")
            continue
        relation[x-1][y-1] = 1
        size = max(size, x, y)

    return relation, size

def print_matrix(matrix, size):
    """Prints the matrix."""
    print("Array:")
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end=' ')
        print()

def compute_meet(A, B, size):
    """Computes the meet of two relations."""
    C = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = A[i][j] and B[i][j]
    return C

def compute_join(A, B, size):
    """Computes the join of two relations."""
    C = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = A[i][j] or B[i][j]
    return C

def compute_boolean_product(A, B, size):
    """Computes the Boolean product of two relations."""
    C = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = any(A[i][k] and B[k][j] for k in range(size))
    return C

def compute_complement(A, size):
    """Computes the complement of a relation."""
    C = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = 1 - A[i][j]
    return C

def compute_transpose(A, size):
    """Computes the transpose of a relation."""
    C = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[j][i] = A[i][j]
    return C

def is_reflexive(A, size):
    """Checks if a relation is reflexive."""
    return all(A[i][i] for i in range(size))

def is_symmetric(A, size):
    """Checks if a relation is symmetric."""
    return all(A[i][j] == A[j][i] for i in range(size) for j in range(size))

def is_antisymmetric(A, size):
    """Checks if a relation is antisymmetric."""
    return all(not (A[i][j] and A[j][i]) for i in range(size) for j in range(size) if i != j)

def is_transitive(A, size):
    """Checks if a relation is transitive."""
    for i in range(size):
        for j in range(size):
            if A[i][j]:
                for k in range(size):
                    if A[j][k] and not A[i][k]:
                        return False
    return True

def compute_reflexive_closure(A, size):
    """Computes the reflexive closure of a relation."""
    C = [row[:] for row in A]
    for i in range(size):
        C[i][i] = 1
    return C

def compute_symmetric_closure(A, size):
    """Computes the symmetric closure of a relation."""
    C = [row[:] for row in A]
    for i in range(size):
        for j in range(size):
            if C[i][j]:
                C[j][i] = 1
    return C

def compute_transitive_closure(A, size):
    """Computes the transitive closure using the Warshall algorithm."""
    C = [row[:] for row in A]
    for k in range(size):
        for i in range(size):
            for j in range(size):
                C[i][j] = C[i][j] or (C[i][k] and C[k][j])
    return C

def main():
    # Read and process the first relation
    print("Input for relation A")
    A, size_A = read_relation()
    print_matrix(A, size_A)

    # Read and process the second relation
    print("Input for relation B")
    B, size_B = read_relation()
    print_matrix(B, size_B)

    # Ensure the size used for operations is the max of sizes from both relations
    size = max(size_A, size_B)

    # Compute meet, join, and Boolean product
    meet = compute_meet(A, B, size)
    print("The meet of A and B:")
    print_matrix(meet, size)

    join = compute_join(A, B, size)
    print("The join of A and B:")
    print_matrix(join, size)

    bool_product = compute_boolean_product(A, B, size)
    print("The Boolean product of A and B:")
    print_matrix(bool_product, size)

    # Operations on just relation A
    complement = compute_complement(A, size)
    print("The complement of A:")
    print_matrix(complement, size)

    transpose = compute_transpose(A, size)
    print("The transpose of A:")
    print_matrix(transpose, size)

    print("Relation A is", "reflexive" if is_reflexive(A, size) else "NOT reflexive")
    print("Relation A is", "symmetric" if is_symmetric(A, size) else "NOT symmetric")
    print("Relation A is", "antisymmetric" if is_antisymmetric(A, size) else "NOT antisymmetric")
    print("Relation A is", "transitive" if is_transitive(A, size) else "NOT transitive")

    reflexive_closure = compute_reflexive_closure(A, size)
    print("The reflexive closure of A:")
    print_matrix(reflexive_closure, size)

    symmetric_closure = compute_symmetric_closure(A, size)
    print("The symmetric closure of A:")
    print_matrix(symmetric_closure, size)

    transitive_closure = compute_transitive_closure(A, size)
    print("The transitive closure of A:")
    print_matrix(transitive_closure, size)

if __name__ == "__main__":
    main()
