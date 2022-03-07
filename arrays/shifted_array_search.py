def shifted_arr_search(shiftArr, num):
  # 1.  Perform modified binary search, comparing arr[0] and arr[mid]
  # 2.  Find the correct sub array where num can possibly live
  # 3.  Perform regular binary search

  pivot = find_pivot(shiftArr)

  # num lives in second part of array
  if pivot == 0 or num < shiftArr[0]: # if pivot == 0, we need to start searching from 0
    result = binary_search(shiftArr, pivot, len(shiftArr) - 1, num)
  else:
    result = binary_search(shiftArr, 0, pivot, num)

  return result

def find_pivot(shiftArr):
  left = 0
  right = len(shiftArr) - 1

  while left <= right:
    mid = left + (right - left) // 2

    # 1.
    if mid == 0 or mid == len(shiftArr) - 1 or shiftArr[mid] < shiftArr[mid - 1]:
      return mid
    elif shiftArr[mid] > shiftArr[0]:
      left = mid + 1
    else:
      right = mid - 1

def binary_search(arr, left, right, num):
  while left <= right:
    mid = left + (right - left) // 2

    if arr[mid] == num:
      return mid
    elif num > arr[mid]:
      left = mid + 1
    else:
      right = mid - 1

  return -1
        
shiftArr = [0,1,2,3,4,5]
num = 1

print(shifted_arr_search(shiftArr, num))

"""
input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left

output: 3 # since its the index of 2 in arr

Approach 1:

Step through the entire array. Find where the array pivots.
The array's pivot would be where arr[i] < arr[i - 1].
From there, determine which subarray is appropriate to perform 
binary search on

Time  : O(n)
Space : O(1)


Approach 2:

Use a modified version of binary search to find where the array pivots.
This can be accomplished by comparing arr[0] with mid. Mid is greater 
than arr[0], that means that section is still sorted, so we can check the
second part of the array.

The modified binary search will terminate once we find when arr[mid] < arr[mid - 1].
It will also terminate in case of mid == 0 or mid == len(arr) to prevent infinite loops

Once the pivot point is found, we can then perform regular binary search on the 
appropriate sub array

Time:  O(log n)
Space: O(1)
"""