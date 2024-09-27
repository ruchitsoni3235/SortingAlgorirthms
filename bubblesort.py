def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already sorted, so no need to check them
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("Sorted array:", arr)
arr = [1, 6, 7, 3, 56, 34, 78, 23]
bubble_sort(arr)

