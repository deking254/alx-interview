#!/usr/bin/python3
"""This modules rotates a matrix by 90 degrees"""

def rotate_2d_matrix(matrix):
    """rotates a matrix by 90 degrees"""
    i = 0
    k = 0
    overall_replacement = []

    for array in range(len(matrix)):
        replacement_array = []
        for arr in range(len(matrix[array])):
            replacement_array.append(matrix[len(matrix) - arr - 1][array])
        overall_replacement.append(replacement_array)
    matrix.clear()
    matrix.extend(overall_replacement)
