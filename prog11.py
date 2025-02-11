# Belal Glab
# Prog 11 // Relations: Properties and Closures
def read_relation():
    # Strating the 20x20 matrix with zeros
    matrix = [[0 for _ in range(20)] for _ in range(20)]
    size = 0
    while True:
        x, y = map(int, input("Please enter an ordered pair x y (0 0 to end input): ").split())
        if x == 0 and y == 0:
            break
        if x < 0 or x > 20 or y < 0 or y > 20:
            print("Error: Please enter values between 1 and 20.")
            continue
        matrix[x-1][y-1] = 1
        size = max(size, x, y)
    return matrix, size

def print_relation(matrix, size):
    print("Array:")
    for i in range(size):
        for j in range(size):
            print(matrix[i][j], end=" ")
        print()

def meet(A, B, size):
    C = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = 1 if A[i][j] and B[i][j] else 0
    return C

def join(A, B, size):
    C = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = 1 if A[i][j] or B[i][j] else 0
    return C

def boolean_product(A, B, size):
    C = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                C[i][j] = C[i][j] or (A[i][k] and B[k][j])
    return C

def complement(A, size):
    C = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[i][j] = 0 if A[i][j] else 1
    return C

def transpose(A, size):
    C = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            C[j][i] = A[i][j]
    return C

def is_reflexive(A, size):
    return all(A[i][i] for i in range(size))

def is_symmetric(A, size):
    return all(A[i][j] == A[j][i] for i in range(size) for j in range(size))

def is_antisymmetric(A, size):
    return all(not (A[i][j] and A[j][i]) for i in range(size) for j in range(size) if i != j)

def is_transitive(A, size):
    for i in range(size):
        for j in range(size):
            if A[i][j]:
                for k in range(size):
                    if A[j][k] and not A[i][k]:
                        return False
    return True

def reflexive_closure(A, size):
    C = [row[:] for row in A]  # Copy A to C
    for i in range(size):
        C[i][i] = 1
    return C

def symmetric_closure(A, size):
    C = [row[:] for row in A]  # Copy A to C
    for i in range(size):
        for j in range(size):
            if A[i][j]:
                C[j][i] = 1
    return C

def transitive_closure(A, size):
    W = [row[:] for row in A]  # Copy A to W
    for k in range(size):
        for i in range(size):
            for j in range(size):
                W[i][j] = W[i][j] or (W[i][k] and W[k][j])
    return W

