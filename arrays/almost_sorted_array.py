from heapq import heapify, heappop, heappush

def sort_k_messed_array(arr, k):
  # 1. Traverse array in blocks of k
  # 2. Keep track of smallest number
  # 3. Swap with smallest number
  
#   for i in range(len(arr)):
#     smallest_number = float('inf')
#     smallest_number_index = 0
    
#     for j in range(k + 1):
#       if i + j >= len(arr):
#         break
        
#       if smallest_number > arr[i + j]:
#         smallest_number = arr[i + j]
#         smallest_number_index = i + j
        
#     if arr[i] > smallest_number:
#       temp = arr[i]
#       arr[i] = smallest_number
#       arr[smallest_number_index] = temp
  
# End verbose insertion sort

    # for i in range(1, len(arr)):
    #     key = arr[i]
    #     j = i - 1

    #     while(j >= i - k and j >= 0 and key < arr[j]):
    #         arr[j + 1] = arr[j]
    #         j -= 1

    #     arr[j + 1] = key
    
    # return arr

    # End optimized solution with insertion sort

    arr_length = len(arr)
    min_heap = []
    heapify(min_heap)

    # Initialize heap
    for num in arr[:k + 1]:
        heappush(min_heap, num)

    # Start from beginning of the array
    # This loop will sort all elements from 0 to the length - (k + 1)
    for i in range(k + 1, arr_length):
        arr[i - (k + 1)] = heappop(min_heap)
        heappush(min_heap, arr[i])

    # After the second loop finishes, the last k elements need to be sorted
    for i in range(0, k + 1):
        arr[arr_length - 1 - k + i] =  heappop(min_heap)

    return arr
      

# [1, 4, 5, 2, 3, 7, 8, 6, 10, 9] k = 2
#           i
#           k

# [1, 0] k = 1
#  i
#     j

# Now I can't hear you
# Okay. I heard what you said about O(n) time by the way

# Hey Steven, I have to go I think we are still having connection problems.  
# I'm not sure why your solution isn't working maybe you can find it through some debugging

# This can be solved in O(nlog(k)) do you want to talk about how real quick or try and figure it out?

# I follow what you are saying. With min heaps. Lol. Okay man, thanks for talking it out. Sorry for technical difficulties. Take care! Same to you. Bye

# can you hear me?

input = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]

print(sort_k_messed_array(input, 2))