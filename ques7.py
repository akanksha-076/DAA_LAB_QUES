import math
def generate_runtime_chart_report(sizes):
    output = []
    output.append("Runtime Comparison Chart Data")
    output.append("InputSize LinearSearch BinarySearch BubbleSort InsertionSort")
    for n in sizes:
        linear_count = n
        binary_count = math.floor(math.log2(n)) + 1
        bubble_count = (n * (n - 1)) // 2
        insertion_count = (n * (n - 1)) // 2
        row = f"{n} {linear_count} {binary_count} {bubble_count} {insertion_count}"
        output.append(row)
    output.append("Scalability Summary")
    output.append("Algorithm Complexity Scalability")
    output.append("Linear Search O(n) Moderate")
    output.append("Binary Search O(log n) Excellent")
    output.append("Bubble Sort O(n^2) Poor")
    output.append("Insertion Sort O(n^2) Poor")
    output.append("Key Observations")
    output.append("Best Algorithm: Binary Search")
    output.append("Most Expensive Algorithm: Bubble Sort")
    output.append("Conclusion: Logarithmic algorithms scale better for large inputs")
    return output
