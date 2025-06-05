# vim: set numberwidth=4 number noignorecase :
"""

    	--- Day 6: Guard Gallivant ---

    The Historians use their fancy device again, this time to whisk you all
    away to the North Pole prototype suit manufacturing lab... in the year
    1518! It turns out that having direct access to history is very convenient
    for a group of historians.

    You still have to be careful of time paradoxes, and so it will be important
    to avoid anyone from 1518 while The Historians search for the Chief.
    Unfortunately, a single guard is patrolling this part of the lab.

    Maybe you can work out where the guard will go ahead of time so that The
    Historians can search safely?

    You start by making a map (your puzzle input) of the situation. For
    example:

    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#..^.....
    ........#.
    #.........
    ......#...

    The map shows the current position of the guard with ^ (to indicate the
    guard is currently facing up from the perspective of the map). Any
    obstructions - crates, desks, alchemical reactors, etc. - are shown as #.

    Lab guards in 1518 follow a very strict patrol protocol which involves
    repeatedly following these steps:

        If there is something directly in front of you, turn right 90 degrees.
        Otherwise, take a step forward.

    Following the above protocol, the guard moves up several times until she
    reaches an obstacle (in this case, a pile of failed suit prototypes):

    ....#.....
    ....^....#
    ..........
    ..#.......
    .......#..
    ..........
    .#........
    ........#.
    #.........
    ......#...

    Because there is now an obstacle in front of the guard, she turns right
    before continuing straight in her new facing direction:

    ....#.....
    ........>#
    ..........
    ..#.......
    .......#..
    ..........
    .#........
    ........#.
    #.........
    ......#...

    Reaching another obstacle (a spool of several very long polymers), she
    turns right again and continues downward:

    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#......v.
    ........#.
    #.........
    ......#...

    This process continues for a while, but the guard eventually leaves the
    mapped area (after walking past a tank of universal solvent):

    ....#.....
    .........#
    ..........
    ..#.......
    .......#..
    ..........
    .#........
    ........#.
    #.........
    ......#v..

    By predicting the guard's route, you can determine which specific positions
    in the lab will be in the patrol path. Including the guard's starting
    position, the positions visited by the guard before leaving the area are
    marked with an X:

    ....#.....
    ....XXXXX#
    ....X...X.
    ..#.X...X.
    ..XXXXX#X.
    ..X.X.X.X.
    .#XXXXXXX.
    .XXXXXXX#.
    #XXXXXXX..
    ......#X..

    In this example, the guard will visit 41 distinct positions on your map.

    Predict the path of the guard. How many distinct positions will the guard visit
    before leaving the mapped area?



"""

# from collections import defaultdict
import argparse
import re
# from collections import defaultdict
# from typing import DefaultDict, List  # , Tuple
# from helpers.day_5_rules_and_updates import get_rules_and_updates
# from helpers.day_5_fix import fix_updates
# from helpers.day_5_valid import update_is_valid
# from helpers.day_5_verify import verify_updates
from utils.get_data_path import get_data_path
# from utils.verbose_msg import verbose_msg

# Constants
__DAYNUM__ = 6  # this is us
__PART__ = 1


def part_1(example: bool, verbose: int = 0):
    """
        part 1()
    """
    print("= " * 10)
    print(" PART 1")
    print("= " * 10)
    if example or verbose:
        print("spam")
    data_path = get_ 
    #
    # The Plan
    #   - get data
    #   -
    #   - find startposition
    #   - determine direction (it's UP)
    #   REPEAT until REACHES A WALL:
    #       - take one step forward
    #         in the current direction
    #         (take_a_step(cur_pos, direction) -> new_pos)
    #       - if there's a wall ahead
    #           (if current row == 0 and we're moving up, or
    #            if current row = -1 and we're moving down, or
    #            if current col == 0 and we're moving left, or
    #            if current col == -1 and we're moving right)
    #               current_col ))
    #             - update the step-counter
    #             - set the break-the-loop flag
    #       - if the step wasn't successful:
    #             - do not update counter
    #             - turn right
    #       - update counter


def part_2(example: bool, verbose: int = 0):
    """make invalid updates valid"""
    print("= " * 10)
    print(" PART 2")
    print("= " * 10)
    if example or verbose:
        print("ham")


def main():
    """main"""

    parser = argparse.ArgumentParser(description=f"aoc 2024 day {__DAYNUM__}",
                                     prog=f"day_{__DAYNUM__}",
                                     add_help=True)
    parser.add_argument('--part', type=int, default=1,
                        choices=[1, 2],
                        help='part number (1 or 2)')
    parser.add_argument('--example', default=False,
                        action='store_true',
                        help='use example datafile')
    parser.add_argument('--input', type=argparse.FileType('r'),
                        help='not used')
    parser.add_argument('--verbose', type=int, default=0,
                        choices=[0, 1, 2],
                        help='get diagnostics')
    args = parser.parse_args()
    if args.part == 1:
        part_1(args.example, args.verbose)
    else:
        part_2(args.example, args.verbose)


if __name__ == "__main__":
    main()
