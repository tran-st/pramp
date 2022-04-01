def toeplitz_matrix(arr):
    column_length = len(arr[0])
    row_length = len(arr)

    for i in range(column_length):
        if check_diagonals(arr, i, column_length, row_length, True) == False:
            return False

    for j in range(row_length):
        if check_diagonals(arr, j, column_length, row_length, False) == False:
            return False

    return True

def check_diagonals(arr, index, column_length, row_length, is_column):
    if is_column:
        number_to_check = arr[0][index]
        current_column = index
        current_row = 0
    else:
        number_to_check = arr[index][0]
        current_row = index
        current_column = 0

    while current_column + 1 < column_length and current_row + 1 < row_length:
        if arr[current_row + 1][current_column + 1] != number_to_check:
            return False

        current_column += 1
        current_row += 1

    return True

"""
Approach 1 :

# 1.  Step through the first row with i
# 2.  Have a second "pointer" starting at 0
# 3.  Check if arr[i + 1][pointer + 1] is within bounds
# 4.  Check if arr[i + 1][pointer + 1] is equal to the diagonal that's being checked
# 5.  Store the diagonal currently being checked
# 6.  If at any point the next diagonal is not equal, return false
# 7.  Step through the first column with j
# 8.  Repeat what we did with the first row, but the first diagonal will be arr[j][0] instead of arr[0][i]

Time  : O(n * m) 
Space : O(1)

"""

input = [
    [1,2,3,4],
    [5,1,2,3],
    [6,5,1,2]
]

# input = [
#     [3],[5],[6]
# ]

print(toeplitz_matrix(input))