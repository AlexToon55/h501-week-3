import seaborn as sns
import pandas as pd


# update/add code below ...


#exercise 1
# A simple function to compute the nth Fibonacci number
def fibonacci(n):
    "Return the nth Fibonacci number."
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(1, n):
            a, b = b, a + b
        return b
# Example usage

n = 1  # Example input
print(fibonacci(n))  # print the answer
n = 2  # Example input
print(fibonacci(n))  # print the answer
n = 3  # Example input
print(fibonacci(n))  # print the answer
n = 4  # Example input
print(fibonacci(n))  # print the answer
n = 5  # Example input
print(fibonacci(n))  # print the answer
n = 6  # Example input
print(fibonacci(n))  # print the answer
n = 7  # Example input
print(fibonacci(n))  # print the answer
n = 8  # Example input
print(fibonacci(n))  # print the answer
n = 9  # Example input
print(fibonacci(n))  # print the answer



#exercise 2
# A function to convert a positive integer to its binary representation
def to_binary(n):
    "Convert an integer to its binary representation as a string."
    if n < 0:
        return "Input should be a non-negative integer."
    elif n == 0:
        return "0"
    bits = []
    # Convert to binary
    while n:
        bits.append(str(n % 2))
        n //= 2
    return ''.join(reversed(bits))
# Example usage
num = 18  # Example input
print(to_binary(num))  # print the answer




#exercise 3



