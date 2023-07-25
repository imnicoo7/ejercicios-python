# Ejericio 4 prueba técnica The Maximum Subarray
# Nicolas Gutierrez

# ------------------------------------------------------------------------------------------------------------
# función 
def maxSubarray(arr):
    max_subarray_sum = float('-inf')
    max_subsequence_sum = 0
    current_sum = 0
    all_negative = True  # Assume all elements are negative initially
    
    for num in arr:
        if num > 0:
            all_negative = False
            max_subsequence_sum += num
        
        current_sum = max(num, current_sum + num)
        max_subarray_sum = max(max_subarray_sum, current_sum)

    if all_negative:
        max_subsequence_sum = max(arr)
    
    return [max_subarray_sum, max_subsequence_sum]
# ------------------------------------------------------------------------------------------------------------
print(maxSubarray([2, -1, 2, 3, 4]))
