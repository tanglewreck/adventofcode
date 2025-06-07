#!/usr/bin/env python
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

    Predict the path of the guard. How many distinct positions will the guard
    visit before leaving the mapped area?

        --> 4964 <--

    That's the right answer! You are one gold star closer to finding
    the Chief Historian.

    --- Part Two ---

    While The Historians begin working around the guard's patrol route, you
    borrow their fancy device and step outside the lab. From the safety of a
    supply closet, you time travel through the last few months and record the
    nightly status of the lab's guard post on the walls of the closet.

    Returning after what seems like only a few seconds to The Historians, they
    explain that the guard's patrol area is simply too large for them to safely
    search the lab without getting caught.

    Fortunately, they are pretty sure that adding a single new obstruction
    won't cause a time paradox. They'd like to place the new obstruction in
    such a way that the guard will get stuck in a loop, making the rest of the
    lab safe to search.

    To have the lowest chance of creating a time paradox, The Historians would
    like to know all of the possible positions for such an obstruction. The new
    obstruction can't be placed at the guard's starting position - the guard is
    there right now and would notice.

    In the above example, there are only 6 different positions where a new
    obstruction would cause the guard to get stuck in a loop. The diagrams of
    these six situations use O to mark the new obstruction, | to show a
    position where the guard moves up/down, - to show a position where the
    guard moves left/right, and + to show a position where the guard moves both
    up/down and left/right.

    Option one, put a printing press next to the guard's starting position:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ....|..#|.
    ....|...|.
    .#.O^---+.
    ........#.
    #.........
    ......#...

    Option two, put a stack of failed suit prototypes in the bottom right
    quadrant of the mapped area:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    ......O.#.
    #.........
    ......#...

    Option three, put a crate of chimney-squeeze prototype fabric next to the
    standing desk in the bottom right quadrant:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    .+----+O#.
    #+----+...
    ......#...

    Option four, put an alchemical retroencabulator near the bottom left
    corner:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    ..|...|.#.
    #O+---+...
    ......#...

    Option five, put the alchemical retroencabulator a bit to the right
    instead:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    ....|.|.#.
    #..O+-+...
    ......#...

    Option six, put a tank of sovereign glue right next to the tank of
    universal solvent:

    ....#.....
    ....+---+#
    ....|...|.
    ..#.|...|.
    ..+-+-+#|.
    ..|.|.|.|.
    .#+-^-+-+.
    .+----++#.
    #+----++..
    ......#O..

    It doesn't really matter what you choose to use as an obstacle so long as
    you and The Historians can put it into position without the guard noticing.
    The important thing is having enough options that you can find one that
    minimizes time paradoxes, and in this example, there are 6 different
    positions you could choose.

    You need to get the guard stuck in a loop by adding a single new
    obstruction. How many different positions could you choose for this
    obstruction?

    --> <--
"""

# from collections import defaultdict
import argparse
import time
from typing import List, Tuple
from utils.get_data_path import get_data_path
from utils.verbose_msg import verbose_msg

# Constants
__DAYNUM__ = 6  # this is us
__PART__ = 1

UP, RIGHT, DOWN, LEFT = '^', '>', 'v', '<'
DIRECTIONS: Tuple[str, str, str, str] = (UP, RIGHT, DOWN, LEFT)
OUTSIDE: Tuple[int, int] = (-1, -1)


def part_1(example: bool, verbose: int = 0):
    """
        part 1()

    --------
    The Plan
    --------
      - get data
      - find startposition
      - determine direction (it's UP)
      REPEAT until REACHES A WALL:
          - take one step forward
            in the current direction
            (take_a_step(cur_pos, direction) -> new_pos)
          - if there's a wall ahead
              (if current row == 0 and we're moving up, or
               if current row = -1 and we're moving down, or
               if current col == 0 and we're moving left, or
               if current col == -1 and we're moving right)
                  current_col ))
                - update the step-counter
                - set the break-the-loop flag
          - if the step wasn't successful:
                - do not update counter
                - turn right
          - update counter
    """
    def get_data() -> List[str]:
        """
            read data
            return start-position
        """
        data: List[str] = []
        data_path = get_data_path(6, 1, example=example)
        try:
            with open(data_path, 'r', encoding="UTF-8") as fp:
                data = fp.read()[:-1].split("\n")
        except OSError as exception:
            raise SystemExit(1, repr(exception)) from exception
        return data

    def get_start_position() -> Tuple[int, int]:
        startrow, startcol = OUTSIDE  # (-1, -1)
        direction: str = UP
        for ind, row in enumerate(data):
            rowstr = "".join(row)
            verbose_msg(f"{ind}:\t{rowstr}", 2, verbose)
            try:
                # str.index() will raise a ValueError if the
                # search-string is not found
                startcol = rowstr.index(direction)
            except ValueError:
                pass
            if not startcol == -1:
                startrow = ind
                return (startrow, startcol)
        return OUTSIDE

    def check_for_obstacles(position) -> bool:
        """
            check if there is an obstacle at 'positon' (which is
            a tuple = (row, col)
        """
        row, col = position
        assert 0 <= row < len(data)
        assert 0 <= col < len(data)
        return bool(data[row][col] == "#")

    def check_for_boundary(position) -> bool:
        """
            check if we're outside the perimeter
        """
        row, col = position
        n = len(data)
        assert -1 <= row <= n
        assert -1 <= col <= n
        return row in (-1, n) or col in (-1, n)

    def turn_right(direction) -> str:
        """
            change direction clockwise:
                UP --> RIGHT --> DOWN --> LEFT --> UP
        """
        assert direction in DIRECTIONS
        if direction is UP:
            return RIGHT
        if direction is RIGHT:
            return DOWN
        if direction is DOWN:
            return LEFT
        if direction is LEFT:
            return UP
        return str(direction)

    def walk(position, direction, verbose=verbose) -> Tuple[int, int]:
        """
            take a step in the indicated direction
            return the new position
            if we encounter an obstruction, return
            the current position
        """
        row, col = position
        assert 0 <= row < len(data)
        assert 0 <= col < len(data)
        assert direction in DIRECTIONS
        if direction is UP:
            new_position = row - 1, col
        elif direction is DOWN:
            new_position = row + 1, col
        elif direction is LEFT:
            new_position = row, col - 1
        elif direction is RIGHT:
            new_position = row, col + 1
        else:
            new_position = (-1, -1)
        if verbose > 0:
            verbose_msg(f"moving {direction}", 1, verbose)
            verbose_msg(f"new_position = {new_position}", 1, verbose)
        return new_position

    # here we go...
    print("= " * 10)
    print(" PART 1")
    print("= " * 10)
    #
    data: List[str] = get_data()
    # get initial position
    initial_position: Tuple[int, int] = get_start_position()
    row, col = initial_position
    # get the initial direction from the data array
    # (initial direction is always UP)
    initial_direction = data[row][col]
    # diagnostics
    verbose_msg("- " * 10, 1, verbose)
    verbose_msg(f"INITIAL POSITION = {initial_position}", 1, verbose)
    verbose_msg(f"INITIAL DIRECTION = {initial_direction}", 1, verbose)
    verbose_msg("- " * 10, 1, verbose)
    # initialise counter
    n_unique_steps = 0
    # initialise position and direction
    position = initial_position
    direction = initial_direction
    # visited: defaultdict[tuple[int, int], int] = {}
    visited: dict[tuple[int, int], int] = {}
    # loop until we reach the edge of the matrix
    while True:
        # save position
        old_position = position
        # get new position on step ahead in the current direction
        position = walk(position, direction)
        # if we've reach the boundary, we're done
        if check_for_boundary(position):
            verbose_msg(f"hit the boundary at {position}", 1, verbose)
            break
        if check_for_obstacles(position):
            # we've encountered an obstacle ("#");
            # back up one step in the opposite direction,
            # turn right and continue walking
            verbose_msg(f"stop at {position}, moving {direction}", 1, verbose)
            verbose_msg(f"backing up to {old_position}), turning", 1, verbose)
            new_direction = turn_right(direction)
            position = old_position
            direction = new_direction
        else:
            # no obstacle found; now check if we've already been here
            row, col = position
            if position in visited:
                visited[position] += 1
            else:
                visited[position] = 1
                n_unique_steps += 1
            verbose_msg(f"n_unique_steps = {n_unique_steps}", 1, verbose)
    # And we're out!
    print(f"n_unique_steps = {n_unique_steps}")


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
    parser.add_argument('--time', default=False,
                        action='store_true',
                        help='time it')
    parser.add_argument('--example', default=False,
                        action='store_true',
                        help='use example datafile')
    parser.add_argument('--verbose', type=int, default=0,
                        choices=[0, 1, 2],
                        help='get diagnostics')
    args = parser.parse_args()
    if args.part == 1:
        pre = time.time()
        part_1(args.example, args.verbose)
        post = time.time()
        if args.time:
            print(f"elapsed = {(post - pre):.4f}s")
    else:
        part_2(args.example, args.verbose)


if __name__ == "__main__":
    main()
# vim: set numberwidth=4 number noignorecase :
