from cmath import sqrt


def drawLine(x1, y1, x2, y2):
    pass
    # draws line, assume implementation available

def drawHTree(x, y, length, depth):
    if depth == 0:
        return

    x0 = x - length / 2
    x1 = x + length / 2
    y0 = y - length / 2
    y1 = y + length / 2

    #   1.
    drawLine(x0, y, x1, y)
    drawLine(x0, y0, x0, y1) #    3.
    drawLine(x1, y1, x1, y1)

    #   8.
    new_length = sqrt(length)
    new_depth = depth - 1

    drawHTree(x0, y0, new_length, new_depth)
    drawHTree(x0, y1, new_length, new_depth)
    drawHTree(x1, y0, new_length, new_depth)
    drawHTree(x1, y1, new_length, new_depth)

"""
Approach:

x0 = x - length / 2
x1 = x + length / 2
y0 = y - length / 2
y1 = y + length / 2

1.  Base case, draw initial straight horizontal line
2.  drawLine(x0, y, x1, y)
3.  Draw two verticle lines, making the H
4.  drawLine(x0, y0, x0, y1)
5.  drawLine(x1, y0, x1, y1)
6.  Identify corners
7.  For depth amount of times, draw Hs for each existing corner
8.  Prepare new length for next call
"""