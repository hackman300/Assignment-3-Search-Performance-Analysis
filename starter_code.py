"""
Search Assignment Starter Code
Implement three search algorithms and benchmark their performance.
"""

import json
import time
import random


def linear_search(data, target):
    """
    Search for target in data using linear search.
    
    Linear search checks each element sequentially until finding the target
    or reaching the end of the list.
    
    Args:
        data (list): List to search (can be sorted or unsorted)
        target: Item to find
    
    Returns:
        int: Index of target if found, -1 if not found
    
    Time Complexity: O(n) - must check up to n elements
    Space Complexity: O(1) - uses constant extra space
    
    Example:
        linear_search([5, 2, 8, 1, 9], 8) returns 2
        linear_search([5, 2, 8, 1, 9], 7) returns -1
    """
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


def binary_search_iterative(data, target):
    """
    Search for target in SORTED data using iterative binary search.

    Binary search repeatedly divides the search space in half by comparing
    the target to the middle element.

    Args:
        data (list): SORTED list to search
        target: Item to find

    Returns:
        int: Index of target if found, -1 if not found

    Time Complexity: O(log n) - divides search space in half each iteration
    Space Complexity: O(1) - uses constant extra space

    IMPORTANT: This only works on SORTED data!

    Example:
        binary_search_iterative([1, 2, 5, 8, 9], 8) returns 3
        binary_search_iterative([1, 2, 5, 8, 9], 7) returns -1
    """
    left = 0
    right = len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        if data[middle] == target:
            return middle
        elif data[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1


def binary_search_recursive(data, target, left=None, right=None):
    """
    Search for target in SORTED data using recursive binary search.

    This is the recursive version of binary search, which naturally expresses
    the divide-and-conquer approach.

    Args:
        data (list): SORTED list to search
        target: Item to find
        left (int): Left boundary of search space (defaults to 0)
        right (int): Right boundary of search space (defaults to len(data)-1)

    Returns:
        int: Index of target if found, -1 if not found

    Time Complexity: O(log n)
    Space Complexity: O(log n) - recursion call stack

    Example:
        binary_search_recursive([1, 2, 5, 8, 9], 8) returns 3
    """
    if left is None:
        left = 0
    if right is None:
        right = len(data) - 1

    if left > right:
        return -1

    middle = (left + right) // 2

    if data[middle] == target:
        return middle
    elif data[middle] < target:
        return binary_search_recursive(data, target, middle + 1, right)
    else:
        return binary_search_recursive(data, target, left, middle - 1)


def load_dataset(fn):
    """Load a dataset from JSON file."""
    with open(f"datasets/{fn}", "r") as f:
        return json.load(f)


def load_test_cases():
    """Load test cases for validation."""
    with open("datasets/test_cases.json", "r") as f:
        return json.load(f)


def test_search_correctness():
    """Test that search func work correctly."""

    sorted_data = [1, 3, 5, 7, 9, 11, 13, 15]
    unsorted_data = [7, 2, 9, 1, 5, 13, 3, 11]

    print("Test 1: Linear search on unsorted data")
    result = linear_search(unsorted_data, 9)
    print(f"    linear_search({unsorted_data}, 9) = {result}")
    print(f"    Expected: 2, Got: {result}, {'✓ PASS' if result == 2 else '✗ FAIL'}")

    print("\nTest 2: Linear search - item not found")
    result = linear_search(unsorted_data, 99)
    print(f"    linear_search({unsorted_data}, 99) = {result}")
    print(f"    Expected: -1, Got: {result}, {'✓ PASS' if result == -1 else '✗ FAIL'}")

    print("\nTest 3: Binary search iterative on sorted data")
    result = binary_search_iterative(sorted_data, 9)
    print(f"    binary_search_iterative({sorted_data}, 9) = {result}")
    print(f"    Expected: 4, Got: {result}, {'✓ PASS' if result == 4 else '✗ FAIL'}")

    print("\nTest 4: Binary search iterative - item not found")
    result = binary_search_iterative(sorted_data, 10)
    print(f"    binary_search_iterative({sorted_data}, 10) = {result}")
    print(f"    Expected: -1, Got: {result}, {'✓ PASS' if result == -1 else '✗ FAIL'}")

    print("\nTest 5: Binary search recursive on sorted data")
    result = binary_search_recursive(sorted_data, 13)
    print(f"    binary_search_recursive({sorted_data}, 13) = {result}")
    print(f"    Expected: 6, Got: {result}, {'✓ PASS' if result == 6 else '✗ FAIL'}")

    print("\nTest 6: Binary search recursive - item not found")
    result = binary_search_recursive(sorted_data, 8)
    print(f"    binary_search_recursive({sorted_data}, 8) = {result}")
    print(f"    Expected: -1, Got: {result}, {'✓ PASS' if result == -1 else '✗ FAIL'}")


def benchmark_algorithm(search_function, data, targets):
    """
    Benchmark a search algorithm on given data with multiple targets.

    Args:
        search_func: The search func to test
        data: The dataset to search
        targets: List of items to search for

    Returns:
        float: Average time per search in seconds
    """
    start = time.time()

    for target in targets:
        search_function(data, target)

    end = time.time()
    return (end - start) / len(targets)


def benchmark_all_datasets():
    """Benchmark all search algorithms on all datasets."""

    datasets = {
        "customer_ids.json": "Unsorted Customer IDs (100K)",
        "product_catalog.json": "Pre-sorted Product Catalog (50K)",
        "config_settings.json": "Small Config Settings (500)",
        "dictionary_words.json": "Dictionary Words (10K)"
    }

    test_cases = load_test_cases()

    for fn, desc in datasets.items():
        print(f"Dataset: {desc}")
        print("-" * 70)

        data = load_dataset(fn)
        dataset_key = fn.replace(".json", "")

        targets = test_cases[dataset_key]["present"][:50] + test_cases[dataset_key]["absent"][:50]
        random.shuffle(targets)

        linear_time = benchmark_algorithm(linear_search, data, targets)
        print(f"  Linear Search: {linear_time*1000:.4f} ms per search")

        if "unsorted" in desc.lower() or "small config" in desc.lower():
            sort_start = time.time()
            sorted_data = sorted(data)
            sort_time = time.time() - sort_start
            print(f"    Time to sort data: {sort_time*1000:.2f} ms (one-time cost)")
        else:
            sorted_data = data
            sort_time = 0

        binary_iter_time = benchmark_algorithm(binary_search_iterative, sorted_data, targets)
        print(f"    Binary Search (Iterative):  {binary_iter_time*1000:.4f} ms per search")

        binary_rec_time = benchmark_algorithm(binary_search_recursive, sorted_data, targets)
        print(f"    Binary Search (Recursive):  {binary_rec_time*1000:.4f} ms per search")

        if binary_iter_time > 0:
            speedup = linear_time / binary_iter_time
            print(f"    Binary speedup: {speedup:.2f}x faster than linear")

        print()


def analyze_preprocessing_costs():
    """Analyze when sorting overhead is worth it."""

    data = load_dataset("customer_ids.json")
    test_cases = load_test_cases()
    targets = test_cases["customer_ids"]["present"][:100]

    sort_start = time.time()
    sorted_data = sorted(data)
    sort_time = time.time() - sort_start

    linear_time = benchmark_algorithm(linear_search, data, targets[:10])
    binary_time = benchmark_algorithm(binary_search_iterative, sorted_data, targets[:10])

    print(f"Dataset: Customer IDs (100,000 unsorted entries)")
    print(f"    One-time sort cost: {sort_time*1000:.2f} ms")
    print(f"    Linear search time: {linear_time*1000:.4f} ms per search")
    print(f"    Binary search time: {binary_time*1000:.4f} ms per search")
    print(f"    Time saved per search: {(linear_time - binary_time)*1000:.4f} ms\n")

    time_saved_per_search = linear_time - binary_time
    if time_saved_per_search > 0:
        searches_to_break_even = sort_time / time_saved_per_search
        print(f"Break-even point: {int(searches_to_break_even)} searches")
        print(f"After {int(searches_to_break_even)} searches, sorting + binary search becomes faster\n")


if __name__ == "__main__":
    print("SEARCH ASSIGNMENT - STARTER CODE")
    print("Implement the search func above, then run tests.\n")

    test_search_correctness()
    benchmark_all_datasets()
    analyze_preprocessing_costs()



"""
The benchmarks reveal significant performance differences across algorithms and datasets. For the Unsorted Customer IDs with 100K entries, the linear 
search averaged 1.8646 ms per search, while both iterative and recursive binary searches averaged 0.0023 ms, yielding a 832.88x speedup. On the Pre-sorted 
Product Catalog with 50K entries, the linear was 1.0949 ms, the binary iterative was 0.0017 ms, and the recursive was 0.0021 ms, yielding a 651.40x speedup. For Small 
Config Settings with 500 entries, the linear took 0.0084 ms, the binary iterative 0.0008 ms, and the recursive 0.0011 ms, yielding a 10.3x speedup. Finally, 
Dictionary Words with 10K entries showed a linear search at 0.1950 ms, a binary iterative search at 0.0022 ms, and a recursive search at 0.0019 ms, resulting in a 87.47x speedup.

The binary search consistently outperformed linear search, with the gap widening as dataset sizes increased. Iterative and recursive binary performed similarly, with their 
differences consistently under 00.0004 ms. Overall, these types of algorithms shine in large-scale scenarios. Preprocessing via sorting incurs a one-time cost but allows for 
faster binary searches. For the Unsorted Customer IDs, sorting took 13.57 ms, with linear search at 1.8646 ms per search. 

For infrequent searches, linear search avoids unnecessary overheads. Additionally, if data frequently changes, maintaining sorted order could get complicated, making a linear 
approach preferable. For small datasets like Config Settings, the absolute savings are tiny, so sorting is rarely useful unless the number of searches is large. 

For Unsorted Customer IDs, I recommend sorting once and using an iterative binary search because of the high volume and potential for frequent lookups. Trade-offs include 
the 13 ms sort cost, though this is negligible for persistent systems; linear's 2 ms per search would accumulate quickly.

For the Pre-sorted Product Catalog, iterative binary search is ideal. The data is already sorted, eliminating preprocessing, and provides a 651x speedup over linear. This 
suits frequent queries in online shopping, prioritizing speed and low overhead; recursive is similar, but iterative avoids stack risks in high-traffic scenarios.

For Small Config Setting's linear search, with only a 10.73x speedup. Sorting's 0.61 ms is not justified unless searches are extraordinarily frequent. Simplicity and the 
absence of preprocessing make linear methods appropriate for small, static data sets.

For Dictionary Words, an iterative binary search is best. Already sorted for prefix matching, it leverages the order for 87.47x speedup, crucial for real-time typing. 
Factors include data size and usage, where low latency is key.
"""
