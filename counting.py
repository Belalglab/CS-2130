def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def permutations(n, x):
    # P(n, x) = n! / (n-x)!
    return factorial(n) // factorial(n-x)

def combinations(n, x):
    # C(n, x) = n! / (x! * (n-x)!)
    return factorial(n) // (factorial(x) * factorial(n-x))

# Problem 1: Vaccine Administration
# a. Ways of selecting doctors for the first batch
doctors_first_batch = combinations(12, 4)
# b. Ways of selecting nurses for the first batch
nurses_first_batch = combinations(36, 12)
# c. Ways to administer the first dose to the 48 people (16 in the first batch)
first_dose = doctors_first_batch * nurses_first_batch
# Assuming each batch must be distinct, the second and third doses follow a similar process but with reduced numbers.
# Since the problem description lacks clarity on how subsequent batches are selected, we'll focus on correct calculations for the first dose.

# Problem 2: Bonus Distribution
# a. Ways to distribute 4 different bonuses to 23 people
bonuses_different = permutations(23, 4)
# b. If all the bonuses are $1,000, how many ways can they be distributed?
bonuses_same = combinations(23, 4)

# Check correctness of functions
perm_test = permutations(35, 12)
comb_test = combinations(23, 11)

# Output the results
print("Check for correctness of functions:")
print("Permutations:    P(35,12) =", perm_test)
print("Combinations:    C(23,11) =", comb_test)

print("\nProblem 1:")
print("Ways of selecting doctors for the first batch:", doctors_first_batch)
print("Ways of selecting nurses for the first batch:", nurses_first_batch)
print("Ways to administer the first dose to the 48 people:", first_dose)

print("\nProblem 2:")
print("The number of ways to distribute 4 bonuses to 23 people if different:", bonuses_different)
print("If the bonuses are the same, there are:", bonuses_same)
