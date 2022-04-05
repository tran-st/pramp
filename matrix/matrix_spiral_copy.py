def spiral_copy(inputMatrix):
    row_length = len(inputMatrix)
    col_length = len(inputMatrix[0])

    left = 0
    top = 0
    right = col_length
    bottom = row_length

    result = []

    while left < right and top < bottom:
        for i in range(left, right):
            result.append(inputMatrix[top][i])

        top += 1

        for i in range(top, bottom):
            result.append(inputMatrix[i][right - 1])

        right -= 1

        if not (left < right and top < bottom):
            break

        for i in range(right - 1, left - 1, -1):
            result.append(inputMatrix[bottom - 1][i])

        bottom -= 1
        
        for i in range(bottom - 1, top - 1, -1):
            result.append(inputMatrix[i][left])

        left += 1

    return result

"""
                                                c
input:  inputMatrix  = [ r[1,    2,   3,  4,    5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ]

Time    : O(n * m)
Space   : O(1)

output: [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]
"""
inputMatrix = [[1],
               [2],
               [3]]

print(spiral_copy(inputMatrix))