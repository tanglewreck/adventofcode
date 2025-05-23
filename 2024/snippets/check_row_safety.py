# coding: utf-8
"""
    check_row_safety
"""
import numpy as np
def checkrowsafety(arr: np.ndarray, verbose=0) -> bool | None:
    """
        Check a sequence of numbers for 'safety':

        A sequence is considered safe if
            1. the sequence is monotonically and strictly
               increasing or decreasing (all differences
               between successive elements have the same sign
               and is not zero), and
            2. the absolute value of the difference between any pair
               of successive elements less than or equal to 3.

        In other words, if a is a sequence (a zero-based array) of real
        numbers of length n, i ∈ ℕ: i ∈ (0, n - 1), and 
        d[i] = a[i] - a[i+1] is the difference between two successive
        elements in that array, then , a is safe iff 
            1. d[i] > 0 or diff[i] < 0, for all i ∈ (0, n - 1), and
            2. abs(d[i]) <= 3 for all i ∈ (0, n - 1).

    """
    if len(arr) <2:
        return None
    # Create two temp-arrays
    tmparr1 = np.append([0], arr)   # add zero at the start
    tmparr2 = np.append(arr, [0])  # add zero at the end

    # Calculate the difference btw the temp-arrays;
    # this gives us the differences between successive
    # elements in the input array (the first and last
    # diffs are discarded since we are only interested
    # in the 'internal' differences between elements)
    # diff_arr = (np.array(tmparr2) - np.array(tmparr1))[1:len(arr)]
    diff_arr = (tmparr2 - tmparr1)[1:len(arr)]
    # diff_arr = (np.array(tmparr1) - np.array(tmparr2))[1:len(arr)]

    # Print diagnostics if verbose
    if verbose > 1:
        print("arr:", arr, f"({len(arr)})")
        print("tmparr1:", tmparr1, f"({len(tmparr1)})")
        print("tmparr2:", tmparr2, f"({len(tmparr2)})")
        print("diff_arr:", diff_arr, f"({len(diff_arr)})")
    # Return true if all diffs have same sign, and  all diffs
    # are less than or equal to 3:
    return (all(diff_arr > 0) or all(diff_arr < 0)) and all(abs(diff_arr) <= 3)
