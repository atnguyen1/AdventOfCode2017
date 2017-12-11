#!/usr/bin/env python
"""
You come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...
While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

Data from square 1 is carried 0 steps, since it's at the access port.
Data from square 12 is carried 3 steps, such as: down, left, left.
Data from square 23 is carried only 2 steps: up twice.
Data from square 1024 must be carried 31 steps.
How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?

Your puzzle input is 325489

--- Part Two ---
As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.

So, the first few squares' values are chosen as follows:

Square 1 starts with the value 1.
Square 2 has only one adjacent filled square (with value 1), so it also stores 1.
Square 3 has both of the above squares as neighbors and stores the sum of their values, 2.
Square 4 has all three of the aforementioned squares as neighbors and stores the sum of their values, 4.
Square 5 only has the first and fourth squares as neighbors, so it gets the value 5.
Once a square is written, its value does not change. Therefore, the first few squares would receive the following values:

147  142  133  122   59
304    5    4    2   57
330   10    1    1   54
351   11   23   25   26
362  747  806--->   ...
What is the first value written that is larger than your puzzle input?

"""

import argparse
import math
import numpy as np
import sys

PUZZLE_INPUT = 325489
INPUT = 4000     # Number of squares to traverse

def get_area(mat, posx, posy):
    """Get surrounding areas."""
    a = mat[posy, posx + 1]
    b = mat[posy - 1, posx + 1]
    c = mat[posy - 1, posx]
    d = mat[posy - 1, posx - 1]
    e = mat[posy, posx - 1]
    f = mat[posy + 1, posx - 1]
    g = mat[posy + 1, posx]
    h = mat[posy + 1, posx + 1]
    # May overflow with large square inputs
    return long(a + b + c + d + e + f + g + h)


def main(args):
    """Main."""
    global INPUT
    global PUZZLE_INPUT
    # Determine Data Structure Size
    dim = math.ceil(math.sqrt(INPUT))
    fib_data = list()

    # If our matrix is unbalanced and can't have a single origin
    if dim % 2 != 1:
        print >>sys.stderr, 'No Breakpoint Row, adding 1'
        dim += 1

    # add additional buffer rows to the edge so we can ignore edge cases
    dim += 2
    
    midpoint = float(dim) / 2.0
    midpoint = math.floor(midpoint)
    midpoint = int(midpoint)

    mat = np.zeros((int(dim), int(dim)), dtype=int)
    
    # Fill in Matrix
    # mat[midpoint, midpoint] = 1
    posx = midpoint
    posy = midpoint
    prevx = None
    prevy = None
    current_direction = None
    print >>sys.stderr, 'Midpoint', midpoint, midpoint

    for x in range(1, INPUT + 1):
        # print mat
        # print current_direction
        if current_direction is None:
            mat[posy, posx] = 1
            current_direction = 'R'
            prevx = posx
            prevy = posy
            posx += 1
            continue
        if current_direction == 'R':
            val = get_area(mat, posx, posy)
            fib_data.append(val)
            mat[posy, posx] = val
            # If we can spiral up
            if mat[posy - 1, posx] == 0:
                current_direction = 'U'
                prevx = posx
                prevy = posy
                posy -= 1
            else:
                # Can't spiral up continue R
                prevx = posx
                prevy = posy
                posx += 1
            continue
        if current_direction == 'U':
            val = get_area(mat, posx, posy)
            fib_data.append(val)
            mat[posy, posx] = val
            # If we can spiral left
            if mat[posy, posx - 1] == 0:
                current_direction = 'L'
                prevx = posx
                prevy = posy
                posx -= 1
            else:
                # Can't spiral left continue U
                prevx = posx
                prevy = posy
                posy -= 1
            continue
        if current_direction == 'L':
            val = get_area(mat, posx, posy)
            fib_data.append(val)
            mat[posy, posx] = val
            # if we can spiral down
            if mat[posy + 1, posx] == 0:
                current_direction = 'D'
                prevx = posx
                prevy = posy
                posy += 1
            else:
                # Can't spiral down continue L
                prevx = posx
                prevy = posy
                posx -= 1
            continue
        if current_direction == 'D':
            val = get_area(mat, posx, posy)
            fib_data.append(val)
            mat[posy, posx] = val
            # if we can spiral right
            if mat[posy, posx + 1] == 0:
                current_direction = 'R'
                prevx = posx
                prevy = posy
                posx += 1
            else:
                # Can't spiral right continue down
                prevx = posx
                prevy = posy
                posy += 1
            continue
    #print mat
    #print current_direction
    #print posx, posy
    #print prevx, prevy
    #print 'Steps', abs(prevx - midpoint) + abs(prevy - midpoint)
    for d in fib_data:
        if d >= PUZZLE_INPUT:
            print d
            break


if __name__ == '__main__':
    desc = 'Advent of Code 3'
    parser = argparse.ArgumentParser(description=desc)
    # parser.add_argument('dir1', type=str, help='Dir 1')
    args = parser.parse_args()

    main(args)
