from functools import cmp_to_key

# 1. Use a custom comparator
# 2. If abs(x) == abs(y), we need to check if either are negative
# 3. If not, just sort by value

def absolute_value_sort(input):
    return sorted(input, key = cmp_to_key(custom_comparator))

def custom_comparator(x, y):
    absolute_x = abs(x)
    absolute_y = abs(y)

    result = x < y if absolute_x == absolute_y else absolute_x < absolute_y

    return -1 if result else 1

input = [ -2, 2, 1, -1, -7, -5, 0]

print(absolute_value_sort(input))