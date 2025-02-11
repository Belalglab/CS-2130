#Belal - 30/26/24
from math import factorial

class DiscreteProbability:
    @staticmethod
    def Permutations(N, X):
        """Calculate permutations: P(N, X) = N! / (N-X)!"""
        return factorial(N) // factorial(N - X)

    @staticmethod
    def Combinations(N, X):
        """Calculate combinations: C(N, X) = N! / (X! * (N-X)!)"""
        return factorial(N) // (factorial(X) * factorial(N - X))

    @staticmethod
    def Binomial(N, K, P):
        """Calculate binomial distribution probability."""
        # Binomial distribution formula: P(X = k) = C(N, k) * P^k * (1-P)^(N-k)
        return DiscreteProbability.Combinations(N, K) * (P ** K) * ((1 - P) ** (N - K))

    def problem_1(self):
        """Solve problem 1: Probability of no more than 1 car failing to start."""
        N = 10  # Number of trials
        P_failure = 0.05  # Probability of failure (dead battery)
        # Calculate probabilities of exactly 0 and 1 car failing to start
        prob_0_failures = self.Binomial(N, 0, P_failure)
        prob_1_failure = self.Binomial(N, 1, P_failure)
        # Sum the probabilities
        return prob_0_failures + prob_1_failure

    def problem_2(self):
        """Solve problem 2: Probability of at most 2 defective cars."""
        N = 20 
        # Number of trials
        P_defective = 0.08  # Probability of a car being defective
        # Sum probabilities of 0, 1, and 2 defective cars
        return sum(self.Binomial(N, k, P_defective) for k in range(3))

# Creating an instance of the class
dp = DiscreteProbability()

# Solving the problems
print("Problem 1 Probability:", dp.problem_1())
print("Problem 2 Probability:", dp.problem_2())
