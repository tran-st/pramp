"""
Approach:

[0,1,2,6,4,5,3]
             i

 temp = 2

1.  Walk through array
2.  Put each value on their corresponding index
3.  Loop through array again
4.  If value does not match it's index, return that index

Time    : O(n)
Space   : O(1)
"""

def get_different_number(arr):
    arr_length = len(arr)

    #   1.
    for i in range(arr_length):
        temp = arr[i]
        
        while temp < arr_length and arr[temp] != temp:
            arr[temp], arr[i] = arr[i], arr[temp]
            temp = arr[i]

    for i in range(arr_length):
        if arr[i] != i:
            return i

    return arr[i] + 1

"""
input:  arr = [0, 4, 2, 1]

output: 4 
"""

arr = [0,5,4,1,3,6,2]
print(get_different_number(arr))