
def count_increasing_subsequences(nums1, nums2):
    n = len(nums1)
    
    # Create a mapping of positions in the second list
    pos_in_nums2 = {}
    for i in range(n):
        pos_in_nums2[nums2[i]] = i
    
    # Convert nums1 to their positions in nums2
    nums1_in_nums2_pos = [pos_in_nums2[num] for num in nums1]
    print((nums1_in_nums2_pos))
    
    # Count the number of increasing subsequences of length 3
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                # Check if the sequence is increasing in nums1_in_nums2_pos
                if nums1_in_nums2_pos[i] < nums1_in_nums2_pos[j] < nums1_in_nums2_pos[k]:
                    count += 1
                    
    return count

# Reading input
nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

# Calculate and print the result
result = count_increasing_subsequences(nums1, nums2)
print(result)