#!/usr/bin/env python
"""
A new system policy has been put in place that requires all accounts to use a passphrase instead of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

To ensure security, a valid passphrase must contain no duplicate words.

For example:

aa bb cc dd ee is valid.
aa bb cc dd aa is not valid - the word aa appears more than once.
aa bb cc dd aaa is valid - aa and aaa count as different words.
The system's full passphrase list is available as your puzzle input. How many passphrases are valid?

For added security, yet another system policy has been put in place. Now, a valid passphrase must contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's letters can be rearranged to form any other word in the passphrase.

For example:

abcde fghij is a valid passphrase.
abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
iiii oiii ooii oooi oooo is valid.
oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
Under this new system policy, how many passphrases are valid?
"""

import argparse
import sys


PASS = 'data/4.txt'

def main(args):
    """Main."""
    pass_data = dict()
    valid = 0
    with open(PASS, 'r') as fh:
        for line in fh:
            data = dict()
            repeat = False
            line = line.rstrip().split(' ')
            for entry in line:
                entry2 = sorted(list(entry))
                entry2 = ' '.join(entry2)
                if entry2 in data:
                    repeat = True
                    break
                else:
                    data[entry2] = 1
            if not repeat:
                valid += 1
    print valid


if __name__ == '__main__':
    desc = 'Advent of Code 2'
    parser = argparse.ArgumentParser(description=desc)
    # parser.add_argument('dir1', type=str, help='Dir 1')
    args = parser.parse_args()

    main(args)
