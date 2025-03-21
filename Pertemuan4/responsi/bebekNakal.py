def count_inversions(arr):
    """
    Count the number of inversions in an array using modified merge sort.
    An inversion occurs when i < j and arr[i] > arr[j].
    
    Args:
        arr (list): List of integers representing the naughtiness values
        
    Returns:
        int: Number of inversions in the array
    """
    # Base case for recursion
    if len(arr) <= 1:
        return arr, 0
    
    # Split array in half
    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])
    
    # Merge the two halves and count split inversions
    merged, split_inv = merge_and_count(left, right)
    
    # Total inversions = inversions in left + inversions in right + split inversions
    return merged, inv_left + inv_right + split_inv

def merge_and_count(left, right):
    """
    Merge two sorted arrays and count the number of split inversions.
    
    Args:
        left (list): First sorted array
        right (list): Second sorted array
        
    Returns:
        tuple: (merged array, number of split inversions)
    """
    merged = []
    inv_count = 0
    i = j = 0
    
    # Merge the two arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            # If left[i] > right[j], then all elements from i to end of left
            # form an inversion with right[j]
            merged.append(right[j])
            inv_count += len(left) - i
            j += 1
    
    # Add remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inv_count

def main():
    # Read input
    n = int(input())
    naughtiness = list(map(int, input().split()))
    
    # Count inversions
    _, inversions = count_inversions(naughtiness)
    
    # Print result
    print(inversions)

if __name__ == "__main__":
    main()