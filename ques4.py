"""
Q1. 1.4 Algorithm Execution Observation Table  (5 marks)

Write a function generate_execution_observation_table(sizes) that:
- Takes a list of input sizes.
- For each input size n, computes the theoretical/expected operation
  counts for various algorithms:
    - Recursive Factorial: n+1 calls
    - Iterative Factorial: n iterations
    - Recursive Fibonacci: number of calls made by a recursive
      Fibonacci computation (approximated here via a helper
      fib_calls(n) that grows similarly to the Fibonacci sequence)
    - Iterative Fibonacci: n iterations
    - Linear Search: n comparisons (worst case)
    - Binary Search: floor(log2(n)) + 1 comparisons (worst case)
    - Bubble Sort: n*(n-1)/2 comparisons (worst case)
    - Insertion Sort: n*(n-1)/2 comparisons (worst case)
- Builds an observation table as a list of strings: a title line,
  a header line naming each column, and one row per input size with
  all the computed values space-separated.
- Returns the completed table.
"""

import math


def generate_execution_observation_table(sizes):
    def fib_calls(n):
        if n <= 1:
            return 1
        a, b = 1, 1
        for _ in range(2, n + 1):
            a, b = b, 1 + a + b
        return b

    table = [
        "Algorithm Execution Observation Table",
        "InputSize RecursiveFactorial IterativeFactorial RecursiveFibonacci IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort"
    ]

    for n in sizes:
        n = int(n)
        rec_fact = n + 1
        iter_fact = n
        rec_fib = fib_calls(n)
        iter_fib = n
        lin_search = n
        bin_search = math.floor(math.log2(n)) + 1
        bubble = n * (n - 1) // 2
        insertion = n * (n - 1) // 2

        row = f"{n} {rec_fact} {iter_fact} {rec_fib} {iter_fib} {lin_search} {bin_search} {bubble} {insertion}"
        table.append(row)

    # for line in table:
    #   print(line)

    return table


# Example usage / test
if __name__ == "__main__":
    sizes = [1, 2, 4, 8, 16]
    result = generate_execution_observation_table(sizes)
    for line in result:
        print(line)