import seaborn as sns
import pandas as pd


# update/add code below ...


#excersie 1
def fib(n):
    "Return the nth Fibonacci number."
    if n <= 0:
        return "Input should be an integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
# A simple function to compute the nth Fibonacci number
n = 9  # Example input
print(fib(n))  # print the answer



#excersie 2




#excersie 3



