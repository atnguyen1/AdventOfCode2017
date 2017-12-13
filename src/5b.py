#!/usr/bin/env python
"""
An urgent interrupt arrives from the CPU: it's trapped in a maze of jump instructions, and it would like assistance from any programs with spare cycles to help find the exit.

The message includes a list of the offsets for each jump. Jumps are relative: -1 moves to the previous instruction, and 2 skips the next one. Start at the first instruction in the list. The goal is to follow the jumps until one leads outside the list.

In addition, these instructions are a little strange; after each jump, the offset of that instruction increases by 1. So, if you come across an offset of 3, you would move three instructions forward, but change it to a 4 for the next time it is encountered.

For example, consider the following list of jump offsets:

0
3
0
1
-3
Positive jumps ("forward") move downward; negative jumps move upward. For legibility in this example, these offset values will be written all on one line, with the current instruction marked in parentheses. The following steps would be taken before an exit is found:

(0) 3  0  1  -3  - before we have taken any steps.
(1) 3  0  1  -3  - jump with offset 0 (that is, don't jump at all). Fortunately, the instruction is then incremented to 1.
 2 (3) 0  1  -3  - step forward because of the instruction we just modified. The first instruction is incremented again, now to 2.
 2  4  0  1 (-3) - jump all the way to the end; leave a 4 behind.
 2 (4) 0  1  -2  - go back to where we just were; increment -3 to -2.
 2  5  0  1  -2  - jump 4 steps forward, escaping the maze.
In this example, the exit is reached in 5 steps.

How many steps does it take to reach the exit?
"""

import argparse

data = 'data/5.txt'


def main(args):
    """Main."""
    steps = list()
    with open(data, 'r') as fh:
        for line in fh:
            line = line.rstrip()
            steps.append(int(line))
    # steps = [0, 3, 0, 1, -3]
    pos = 0
    iteration = 1
    # print len(steps)
    while True:
        # print steps, pos
        jumps = steps[pos]
        if (pos + jumps + 1) > len(steps):
            break
        if (pos + jumps + 1) < 0:
            break
        if jumps > 2:
            steps[pos] = steps[pos] - 1
        else:
            steps[pos] = steps[pos] + 1        
        pos = pos + jumps
        iteration += 1
    print iteration


if __name__ == '__main__':
    desc = 'Advent of Code 2'
    parser = argparse.ArgumentParser(description=desc)
    # parser.add_argument('dir1', type=str, help='Dir 1')
    args = parser.parse_args()

    main(args)
