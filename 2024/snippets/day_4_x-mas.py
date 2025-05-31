# pylint: disable=invalid-name
"""
    Look for X-MAS patterns

    --- Part Two ---

    The Elf looks quizzically at you. Did you misunderstand the assignment?

    Looking for the instructions, you flip over the word search to find that
    this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're
    supposed to find two MAS in the shape of an X. One way to achieve that is
    like this:

    M.S
    .A.
    M.S

    Irrelevant characters have again been replaced with . in the above diagram.
    Within the X, each MAS can be written forwards or backwards.

    Here's the same example from before, but this time all of the X-MASes have
    been kept instead:

    .M.S......
    ..A..MSMS.
    .M.S.MAA..
    ..A.ASMSM.
    .M.S.M....
    ..........
    S.S.S.S.S.
    .A.A.A.A..
    M.M.M.M.M.
    ..........

    In this example, an X-MAS appears 9 times.

    Pattern variants 
    ----------------
    M.M     M.S     S.M     S.S
    .A.     .A.     .A.     .A.
    S.S     M.S     S.M     M.M

    - For every 'A' found at position (i, j), check if
        - df[i-1, j-1] == 'M' and df[i+1, j+1] == 'M'
                          AND
          df[i-1, j-1] == 'S' and df[i+1, j+1] == 'S'

        OR

        - df[i-1, j-1] == 'M' and df[i+1, j+1] == 'S'
                          AND
          df[i-1, j-1] == 'M' and df[i+1, j+1] == 'S'

        OR

        - df[i-1, j-1] == 'S' and df[i+1, j+1] == 'M'
                          AND
          df[i-1, j-1] == 'S' and df[i+1, j+1] == 'M'

        OR

        - df[i-1, j-1] == 'S' and df[i+1, j+1] == 'S'
                          AND
          df[i-1, j-1] == 'M' and df[i+1, j+1] == 'M'

"""
