"""
Q1. 1.4 Algorithm Execution Observation Table  (5 marks)

Write a function generate_execution_observation_table(sizes) that:
- Takes a list of input sizes.
- Defines a helper rfib(n) that computes the number of calls made by
  a naive recursive Fibonacci computation (recursively: 1 call for
  n<=1, otherwise 1 + rfib(n-1) + rfib(n-2)).
- For each input size n, computes the theoretical/expected operation
  counts for various algorithms:
    - Recursive Factorial: n+1 calls
    - Iterative Factorial: n iterations
    - Recursive Fibonacci: rfib(n) calls
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

from math import floor, log2


def generate_execution_observation_table(sizes):
    def rfib(n):
        if n <= 1:
            return 1
        return 1 + rfib(n - 1) + rfib(n - 2)

    output = [
        "Algorithm Execution Observation Table",
        "InputSize RecursiveFactorial IterativeFactorial RecursiveFibonacci IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort"
    ]

    for n in sizes:
        rfact = n + 1
        ifact = n
        rfibc = rfib(n)
        ifib = n
        lsearch = n
        bsearch = floor(log2(n)) + 1
        bubble = n * (n - 1) // 2
        insertion = n * (n - 1) // 2

        row = f"{n} {rfact} {ifact} {rfibc} {ifib} {lsearch} {bsearch} {bubble} {insertion}"
        output.append(row)

    return output


# Example usage / test
if __name__ == "__main__":
    sizes = [1, 2, 4, 8, 16]
    result = generate_execution_observation_table(sizes)
    for line in result:
        print(line)