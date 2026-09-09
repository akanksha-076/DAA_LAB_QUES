import random
import time
import tracemalloc

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def measure(n):
    arr = [random.randint(0, 1_000_000) for _ in range(n)]

    tracemalloc.start()          # start tracking memory allocations
    start_time = time.perf_counter()

    merge_sort(arr)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return end_time - start_time, peak

if __name__ == "__main__":
    sizes = [1000, 5000, 10000, 50000, 100000, 500000]

    print(f"{'Input Size':<12}{'Time (s)':<12}{'Peak Memory (KB)':<20}")
    print("-" * 44)
    for n in sizes:
        t, peak = measure(n)
        print(f"{n:<12}{t:<12.4f}{peak/1024:<20.2f}")