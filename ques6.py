"""
Q2. 1.5 Runtime and Complexity Comparison Table  (5 marks)

Write a function generate_runtime_complexity_table(n) that:
- Takes a single input size n.
- Builds a comparison table (as a list of strings) showing, for each
  of Linear Search, Binary Search, Bubble Sort, and Insertion Sort:
    - the observed operation count for that input size n
      (Linear Search: n, Binary Search: floor(log2(n))+1,
       Bubble Sort: n*(n-1)//2, Insertion Sort: n*(n-1)//2)
    - its expected theoretical complexity (O(n), O(log n),
      O(n^2), O(n^2) respectively)
    - a short observation describing its growth pattern
      (linear, logarithmic, or quadratic growth)
- Returns the completed table, starting with a title line and a
  header line naming each column.
"""

from math import log2, floor


def generate_runtime_complexity_table(n):
    output = [
        "Runtime Complexity Comparison",
        "Method ObservedCount ExpectedComplexity Observation",
        f"Linear Search {n} O(n) Grows linearly",
        f"Binary Search {floor(log2(n)) + 1} O(log n) Grows logarithmically",
        f"Bubble Sort {n * (n - 1) // 2} O(n^2) Grows quadratically",
        f"Insertion Sort {n * (n - 1) // 2} O(n^2) Grows quadratically"
    ]
    return output


# Example usage / test
if __name__ == "__main__":
    result = generate_runtime_complexity_table(8)
    for line in result:
        print(line)