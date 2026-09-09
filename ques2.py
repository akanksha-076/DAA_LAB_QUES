"""
Q2. 1.1 Recursive and Iterative Computation Analyzer  (10 marks)

Write a function analyze_recursive_iterative(n) that:
- Computes n! (factorial) both recursively and iteratively, counting the
  number of recursive calls made by the recursive version.
- Computes the nth Fibonacci number both recursively and iteratively,
  counting the number of recursive calls made by the recursive version.
- Returns a report as a list of strings showing:
    "Computation Analysis Report",
    the recursive and iterative factorial values,
    the recursive and iterative Fibonacci values,
    an "Operation Count Comparison" section listing the call/iteration
    counts for each of the four computations.
"""

def analyze_recursive_iterative(n):
    rec_fact_calls = 0

    def fact_rec(x):
        nonlocal rec_fact_calls
        rec_fact_calls += 1
        if x <= 0:
            return 1
        return x * fact_rec(x - 1)

    rec_fact_val = fact_rec(n)

    iter_fact_val = 1
    iter_fact_count = n
    for i in range(1, n + 1):
        iter_fact_val *= i

    rec_fib_calls = 0

    def fib_rec(x):
        nonlocal rec_fib_calls
        rec_fib_calls += 1
        if x <= 0:
            return 0
        if x == 1:
            return 1
        return fib_rec(x - 1) + fib_rec(x - 2)

    rec_fib_val = fib_rec(n)

    if n == 0:
        iter_fib_val = 0
    elif n == 1:
        iter_fib_val = 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        iter_fib_val = b
    iter_fib_count = n

    return [
        "Computation Analysis Report",
        f"Recursive Factorial: {rec_fact_val}",
        f"Iterative Factorial: {iter_fact_val}",
        f"Recursive Fibonacci: {rec_fib_val}",
        f"Iterative Fibonacci: {iter_fib_val}",
        "Operation Count Comparison",
        f"Recursive Factorial Count: {rec_fact_calls}",
        f"Iterative Factorial Count: {iter_fact_count}",
        f"Recursive Fibonacci Count: {rec_fib_calls}",
        f"Iterative Fibonacci Count: {iter_fib_count}",
    ]


# Example usage / test
if __name__ == "__main__":
    result = analyze_recursive_iterative(6)
    for line in result:
        print(line)