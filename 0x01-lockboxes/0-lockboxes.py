#!/usr/bin/python3
"""solve the lockboxes problem"""


def length(b):
    """returns the length of the supplied array"""
    i = 0
    for j in b:
        i = i + 1
    return i


def check_availability(number, a):
    """returns 1 if the number is already in the array"""
    for n in a:
        if (n == number):
            return 1
    return 0


def canUnlockAll(boxes):
    """returns a boolean determining if all boxes can be opened"""
    unlocked_boxes = [0]
    for box in unlocked_boxes:
        for key in boxes[box]:
            if check_availability(key, unlocked_boxes) == 0:
                unlocked_boxes.append(key)
    if (length(unlocked_boxes) == length(boxes)):
        return True
    else:
        return False
