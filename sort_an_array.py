def merge(left, right):
    merged = []
    i = j = 0

    # Compare each element and merge them into a single sorted array
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged

def merge_sort(arr):
    # Base case: if the array is of size 1 or less, it's already sorted
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the sorted halves and return the result
    return merge(sorted_left, sorted_right)

# Example usage
array = [38, 27, 43, 3, 9, 82, 10]
array = [-1,2,-8,-10]
sorted_array = merge_sort(array)
print("Sorted array:", sorted_array)
