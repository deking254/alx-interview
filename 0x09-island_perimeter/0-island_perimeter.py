#!/usr/bin/python3
"""This project returns the premeter described in a grid"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    width_used_indexes = []
    width = 0
    height = 0
    for height_index in range(len(grid)):
        ht = False
        for row_index in range(len(grid[height_index])):
            if grid[height_index][row_index] == 1:
                ht = True
                skip = False
                if len(width_used_indexes) > 0:
                    for ind in width_used_indexes:
                        if row_index == ind:
                            skip = True
                if skip is False:
                    width_used_indexes.append(row_index)
                    width += 1
        if ht is True:
            height += 1
    return (height * 2) + (width * 2)
