"""
Q1. 1.2 Linear Search and Binary Search Comparison  (5 marks)

Write a function compare_search_algorithms(arr, target) that:
- Performs a Linear Search on arr to find target, counting the number
  of comparisons made and the index at which it is found (-1 if not found).
- Performs a Binary Search on arr to find target, counting the number
  of comparisons made and the index at which it is found (-1 if not found).
  (Note: on finding a match, it keeps searching the left half to locate
  the first occurrence, since 'high' is set to mid-1 even after a match.)
- Compares the number of comparisons taken by each algorithm and decides
  which one performed better (fewer comparisons), or if both are equal.
- Returns a report as a list of strings containing:
    "Search Comparison Report",
    Linear Search section (Index, Comparisons),
    Binary Search section (Index, Comparisons),
    and the "Better Algorithm" verdict.
"""

def compare_search_algorithms(arr, target):
    linear_idx = -1
    linear_comps = 0
    for i in range(len(arr)):
        linear_comps += 1
        if arr[i] == target:
            linear_idx = i
            break

    binary_idx = -1
    binary_comps = 0
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        binary_comps += 1
        if arr[mid] == target:
            binary_idx = mid
            high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if linear_comps < binary_comps:
        better = "Better Algorithm: Linear Search"
    elif binary_comps < linear_comps:
        better = "Better Algorithm: Binary Search"
    else:
        better = "Better Algorithm: Both Equal"

    return [
        "Search Comparison Report",
        "Linear Search",
        f"Index: {linear_idx}",
        f"Comparisons: {linear_comps}",
        "Binary Search",
        f"Index: {binary_idx}",
        f"Comparisons: {binary_comps}",
        better,
    ]


# Example usage / test
if __name__ == "__main__":
    arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    target = 14
    result = compare_search_algorithms(arr, target)
    for line in result:
        print(line)