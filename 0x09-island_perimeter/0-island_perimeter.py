#!/usr/bin/python3
"""
Island_paramenter module
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid

    Args:
    grid (list of list of int)

    Returns:
    int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Assume the celll contribute 4 tpo the perimeter
                perimeter += 4

                # chaeck if there'e land to the left
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 2

                # check if theres land above
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 2

    return perimeter
