"""
Q3. 1.3 Bubble Sort and Insertion Sort Performance Comparison  (10 marks)

Write a function compare_bubble_insertion(random_data, sorted_data, reverse_data) that:
- Implements bubble_sort(arr), counting comparisons and swaps, with an
  early-exit optimization if no swaps occur in a pass.
- Implements insertion_sort(arr), counting comparisons and shifts.
- Runs both sorts on three datasets: a random dataset, an already-sorted
  dataset, and a reverse-sorted dataset (without modifying the originals).
- For each dataset, determines which algorithm made fewer comparisons
  ("Bubble Sort", "Insertion Sort", or "Both Equal").
- Builds and returns a report as a list of strings containing:
    "Sorting Performance Report",
    then for each dataset: its name, the sorted result from each
    algorithm, their comparison/swap/shift counts, and the verdict
    on which algorithm performed better.
"""

def compare_bubble_insertion(random_data, sorted_data, reverse_data):
    def bubble_sort(arr):
        a = list(arr)
        n = len(a)
        comps = 0
        swaps = 0
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                comps += 1
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    swaps += 1
                    swapped = True
            if not swapped:
                break
        return a, comps, swaps

    def insertion_sort(arr):
        a = list(arr)
        n = len(a)
        comps = 0
        shifts = 0
        for i in range(1, n):
            key = a[i]
            j = i - 1
            while j >= 0:
                comps += 1
                if a[j] > key:
                    a[j + 1] = a[j]
                    shifts += 1
                    j -= 1
                else:
                    break
            a[j + 1] = key
        return a, comps, shifts

    datasets = [
        ("Random Dataset", random_data),
        ("Sorted Dataset", sorted_data),
        ("Reverse Dataset", reverse_data),
    ]

    report = ["Sorting Performance Report"]
    for name, data in datasets:
        b_sorted, b_comps, b_swaps = bubble_sort(data)
        i_sorted, i_comps, i_shifts = insertion_sort(data)

        if b_comps < i_comps:
            better = "Better Algorithm: Bubble Sort"
        elif i_comps < b_comps:
            better = "Better Algorithm: Insertion Sort"
        else:
            better = "Better Algorithm: Both Equal"

        b_str = " ".join(map(str, b_sorted))
        i_str = " ".join(map(str, i_sorted))

        report.extend([
            name,
            f"Bubble Sorted: {b_str}",
            f"Bubble Comparisons: {b_comps}",
            f"Bubble Swaps: {b_swaps}",
            f"Insertion Sorted: {i_str}",
            f"Insertion Comparisons: {i_comps}",
            f"Insertion Shifts: {i_shifts}",
            better,
        ])

    return report


# Example usage / test
if __name__ == "__main__":
    random_data = [5, 2, 9, 1, 5, 6]
    sorted_data = [1, 2, 3, 4, 5, 6]
    reverse_data = [6, 5, 4, 3, 2, 1]

    result = compare_bubble_insertion(random_data, sorted_data, reverse_data)
    for line in result:
        print(line)