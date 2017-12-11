#!/usr/bin/env python
"""

"""

import argparse


def main(args):
    """Main."""

if __name__ == '__main__':
    desc = 'Advent of Code 2'
    parser = argparse.ArgumentParser(description=desc)
    # parser.add_argument('dir1', type=str, help='Dir 1')
    args = parser.parse_args()

    main(args)
