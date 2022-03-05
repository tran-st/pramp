def quadruplet(arr, sum):
    # 1.  Two nested for loops
    # 2.  While loop inside the inner for loop
    # 3.  Declare the last pointer before the inner for loop
    # 4.  Sum all 4 pointers
    # 5.  If sum is less than target, increment the second to last pointer
    # 6.  Else, decrement the last pointer

    arr_length = len(arr)
    arr.sort()

    # 1.
    for i in range(arr_length - 3):
        # 3
        l = arr_length - 1
        for j in range(i + 1, arr_length - 2):
            k = j + 1

            while k < l:
                # 4.
                total = arr[i] + arr[j] + arr[k] + arr[l]

                if total == sum:
                    return [arr[i], arr[j], arr[k], arr[l]]
                elif total < sum: # 5.
                    k += 1
                else:
                    l -= 1

    return -1

arr = [2, 7, 4, 0, 9, 5, 1, 3]
s = 20

print(quadruplet(arr, s))

"""
input:  arr = [2, 7, 4, 0, 9, 5, 1, 3], s = 20
               i
                  j
                     k
                                    l

output: [0, 4, 7, 9] # The ordered quadruplet of (7, 4, 0, 9)
                     # whose sum is 20. Notice that there
                     # are two other quadruplets whose sum is 20:
                     # (7, 9, 1, 3) and (2, 4, 9, 5), but again you’re
                     # asked to return the just one quadruplet (in an
                     # ascending order)


Approach 1:

Walk through the array with 4 pointers through 4 for loops, comparing their sum
to see if there is a quadruple

Time  : O(n^4)
Space : O(1)


Approach 2:

Sort the array. Walk through the array with 4 pointers. 2 pointers i and j will be used
in the 2 outer for loops. The other 2 pointers will start from j + 1 and the end of the array.
On each iteration, all pointers will be summed and if their sum is more than the target, we can
decrement the last pointer. If their sum is less, we can increment the second to last pointer

Time  : O(n^3)
Space : O(1)
"""