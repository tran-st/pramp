from collections import deque

def shortest_cell_path(grid, start_row, start_column, target_row, target_column):
    # a.  Set boundaries of the grid
    # b.  Initiate a double ended queue with starting row and column
    # c.  While the queue isn't empty, pop and check if that is the target
    # d.  Add visited steps in a set
    # e.  If it isn't, append all 4 directions into the queue if they are legal moves
    # e2. Do this for the length of the current queue
    # f.  Each time we pop the length of the initial queue, increment steps

    # 1.
    row_length, column_length = len(grid), len(grid[0])
    queue = deque([[start_row, start_column]]) # b.
    visited = set([(start_row, start_column)])
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    steps = 0

    while queue:
        # pop_count = len(queue)

        # e2.
        # for _ in range(pop_count):
        row, column = queue.popleft()

        # c.
        if row == target_row and column == target_column:
            return steps
        else:
            for x, y in directions: # e.
                new_row = row + x
                new_column = column + y

                if (new_row in range(row_length) and new_column in range(column_length) and (new_row, new_column) not in visited and grid[new_row][new_column] == 1):
                    queue.append([new_row, new_column])
                    visited.add((new_row, new_column)) # d.

        # f.
        steps += 1

    return -1

# 0 1 1 1
# 0 0 1 1
# 0 1 1 1
# 1 1 1 1

# start_row = 1, start_column = 3
# target_row = 3, target_column = 2
# queue.append((1, 3))

grid = [
    [1,1,1,1],
    [0,0,0,1],
    [1,1,1,1]
]

grid = [[1,1,1],
        [0,0,0],
        [0,0,0]]
sr = 0
sc = 1
tr = 0
tc = 0

print(shortest_cell_path(grid, sr, sc, tr, tc))