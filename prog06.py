# Main Funcation
def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

# Reading the first integer 
first_integer = int(input("Enter the first integer: "))
print(fibo(first_integer))

# Reading the second integer
second_integer = int(input("Enter the second integer: "))

# compute the sum of all numbers from 1 to second_integer
loop_Sum = sum(range(1, second_integer + 1))

# Computing the sum using the formula
formela_sum = second_integer * (second_integer + 1) // 2

# Displaying the results 
print(f"Summation by loop: {loop_Sum}")
print(f"Summation by formula: {formela_sum}")

# Comparing the results
if loop_Sum == formela_sum:
    print("The summation results are the same.")
else:
    print("The summation results are different.")
