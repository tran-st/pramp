def sort_k_messed_array(arr, k):
  pass # your code goes here

  # 1. Traverse array in blocks of k
  # 2. Keep track of smallest number
  # 3. Swap with smallest number
  
  
  
  for i in range(len(arr)):
    smallest_number = float('inf')
    smallest_number_index = 0
    
    for j in range(k + 1):
      if i + j >= len(arr):
        break
        
      if smallest_number > arr[i + j]:
        smallest_number = arr[i + j]
        smallest_number_index = i + j
        
    if arr[i] > smallest_number:
      temp = arr[i]
      arr[i] = smallest_number
      arr[smallest_number_index] = temp
      
  return arr
      

# [1, 4, 5, 2, 3, 7, 8, 6, 10, 9] k = 2
#  i

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

input = [1, 0]

print(sort_k_messed_array(input, 1))