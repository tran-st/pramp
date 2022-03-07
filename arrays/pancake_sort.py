def pancake_sort(arr):
    # 1.  Find the maximum on each iteration
    # 2.  Call flip with k = index of the maximum + 1
    # 3.  Call flip again with k = length of array - i

    arr_length = len(arr)
    for i in range(arr_length):
        max_index = 0

        # 1.
        for j in range(arr_length - i):
            if arr[j] > arr[max_index]:
                max_index = j
        
        # 2.
        flip(arr, max_index + 1)
        flip(arr, arr_length - i) # 3.

    return arr

def flip(arr, k):
    if k > len(arr):
        return -1

    left = 0
    right = k - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

input = [3, 1, 6, 4, 2, 5]
print(pancake_sort(input))

"""
input = [3, 2, 1, 4, 5]
print(flip(input, 2))

flip(arr, 5) -> [5, 4, 1, 2, 3]
flip(arr, 5) -> [3, 2, 1, 4, 5]

flip(arr, 4) -> [4, 3, 2, 1, 5]
flip(arr, 4) -> [1, 2, 3, 4, 5]

Approach 1: 

Step through the entire array, finding the maximum for each iteration.
Call the flip function from 0 until the index of the maximum number to
bring that highest number to the front. Call the flip again from 0 until
the index of the last maximum number

Time  : O(n^2)
Space : O(1)
"""