#!/usr/bin/env python3


"""--- Day 9: Mirage Maintenance ---\r
You ride the camel through the sandstorm and stop where the ghost's maps told
you to stop. The sandstorm subsequently subsides, somehow seeing you standing
at an oasis!

The camel goes to get some water and you stretch your neck. As you look up, you
discover what must be yet another giant floating island, this one made of
metal! That must be where the parts to fix the sand machines come from.

There's even a hang glider partially buried in the sand here; once the sun
rises and heats up the sand, you might be able to use the glider and the hot
air to get all the way up to the metal island!

While you wait for the sun to rise, you admire the oasis hidden here in the
middle of Desert Island. It must have a delicate ecosystem; you might as well
take some ecological readings while you wait. Maybe you can report any
environmental instabilities you find to someone so the oasis can be around for
the next sandstorm-worn traveler.

You pull out your handy Oasis And Sand Instability Sensor and analyze your
surroundings. The OASIS produces a report of many values and how they are
changing over time (your puzzle input). Each line in the report contains the
history of a single value. For example:

0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
To best protect the oasis, your environmental report should include a
prediction of the next value in each history. To do this, start by making a new
sequence from the difference at each step of your history. If that sequence is
not all zeroes, repeat this process, using the sequence you just generated as
the input sequence. Once all of the values in your latest sequence are zeroes,
you can extrapolate what the next value of the original history should be.

In the above dataset, the first history is 0 3 6 9 12 15. Because the values
increase by 3 each step, the first sequence of differences that you generate
will be 3 3 3 3 3. Note that this sequence has one fewer value than the input
sequence because at each step it considers two numbers from the input. Since
these values aren't all zero, repeat the process: the values differ by 0 at
each step, so the next sequence is 0 0 0 0. This means you have enough
information to extrapolate the history! Visually, these sequences can be
arranged like this:

0   3   6   9  12  15
  3   3   3   3   3
    0   0   0   0
To extrapolate, start by adding a new zero to the end of your list of zeroes;
because the zeroes represent differences between the two values above them,
this also means there is now a placeholder in every sequence above it:

0   3   6   9  12  15   B
  3   3   3   3   3   A
    0   0   0   0   0
You can then start filling in placeholders from the bottom up. A needs to be
the result of increasing 3 (the value to its left) by 0 (the value below it);
this means A must be 3:

0   3   6   9  12  15   B
  3   3   3   3   3   3
    0   0   0   0   0
Finally, you can fill in B, which needs to be the result of increasing 15 (the
value to its left) by 3 (the value below it), or 18:

0   3   6   9  12  15  18
  3   3   3   3   3   3
    0   0   0   0   0
So, the next value of the first history is 18.

Finding all-zero differences for the second history requires an additional
sequence:

1   3   6  10  15  21
  2   3   4   5   6
    1   1   1   1
      0   0   0
Then, following the same process as before, work out the next value in each
sequence from the bottom up:

1   3   6  10  15  21  28
  2   3   4   5   6   7
    1   1   1   1   1
      0   0   0   0
So, the next value of the second history is 28.

The third history requires even more sequences, but its next value can be found
the same way:

10  13  16  21  30  45  68
   3   3   5   9  15  23
     0   2   4   6   8
       2   2   2   2
         0   0   0
So, the next value of the third history is 68.

If you find the next value for each history in this example and add them
together, you get 114.

Analyze your OASIS report and extrapolate the next value for each history. What
is the sum of these extrapolated values?

"""

import argparse
import json
import numpy as np
import sys


def main():

    def parse_arguments():
        try:
            parser = argparse.ArgumentParser(epilog=__doc__)
            parser.add_argument('-d', '--debug', default=False, action='store_true', help="Produce debugging info")
            parser.add_argument('-v', '--verbose', default=0, action='count', help="Verbose output")
            parser.add_argument('-n', "--iterations",  type=int, default=1, help="Number of iterations", metavar="iterations", dest="iterations")
            parser.add_argument('--series', '--sequence', type=argparse.FileType('r'))
            arguments = parser.parse_args()
        except Exception as e:
            """Never gets here, it seems; argparse handles errors """
            print(str(e))
        return arguments
    

    def compute_differences(seq):
        """Compute the differences between consecutive elements in the sequence."""
        return [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
    

    def find_next_value(seq):
        """Find the next value in the sequence using the described method."""
        sequences = [seq]
        if args.debug:
            print("sequence:", seq)
                    
        while True:
            new_seq = compute_differences(sequences[-1])
            sequences.append(new_seq)
                                                
            if all(v == 0 for v in new_seq):
                if args.debug:
                    print("break")
                break
            
        for i in range(len(sequences) - 1, 0, -1):
            next_value = sequences[i][-1] + sequences[i-1][-1]
            sequences[i-1].append(next_value)
                            
        return sequences[0][-1]

    
    def sum_of_next_values(sequences):
        """Compute the sum of the next values for all sequences."""
        return sum(find_next_value(seq) for seq in sequences)

    
    # Get command-line arguments
    args = parse_arguments()
    if args.series:
        """Got a json filename on the command line (option: --series)."""
        try:
            with args.series as f:
                """Load the json data and append the sequences to the list of sequences"""
                sequences = list()
                seqs = json.load(f)
                [sequences.append(seq['seq']) for seq in seqs]
                #for seq in seqs:
                #    sequences.append(seq['seq'])
                #    if args.debug:
                #        print(seq['seq'])
        except (json.JSONDecodeError, ValueError) as e:
            print("Got a JSONDecodeError:", file=sys.stderr)
            print(str(e), file=sys.stderr)
            raise SystemExit(1)
        except (OSError) as e:
            # Will probably never get here since argparse will complain if the
            # file doesn't exist or isn't readable...
            print("Got an OSError:", file=sys.stderr)
            print(str(e), file=sys.stdout)
            raise SystemExit(2)
    else:
        sequences = [ [0, 3, 6, 9, 12, 15],
            [1, 3, 6, 10, 15, 21],
            [10, 13, 16, 21, 30, 45] ]

    if args.debug:
        print("sequences:", sequences)

    for k in range(args.iterations):
        if args.verbose:
            print("Iteration #", k+1, sep="")
            if args.verbose >=2:
                for seq in sequences:
                    print("Updated sequences (post):", seq)
        print("Sum of last elements:", sum_of_next_values(sequences))  # Output: 114, 158, ...


if __name__ == "__main__":
    main()

