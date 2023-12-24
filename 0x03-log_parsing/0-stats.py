#!/usr/bin/python3
"""script to analyze stdin values line by line"""
from sys import stdin
from collections import defaultdict


def int_checker(value: str):
    try:
        a = int(value)
        if a == 200 or 301 or 400 or 401 or 403 or 404 or 405 or 500:
            return True
        else:
            return False
    except Exception:
        return False


def checker(line_array):
    """checks if the format is up to par"""
    counter = 0
    if len(line_array) != 9:
        return False
    for item_index in range(0, len(line_array)):
        if item_index == 1:
            if line_array[item_index] == '-':
                continue
            else:
                return False
        if item_index == 2:
            if line_array[item_index][0] == '[':
                continue
            else:
                return False
        if item_index == 3:
            if line_array[item_index].endswith(']'):
                continue
            else:
                return False
        if item_index == 4:
            if line_array[item_index] == '"GET':
                continue
            else:
                return False
        if item_index == 5:
            if line_array[item_index] == '/projects/260':
                continue
            else:
                return False
        if item_index == 6:
            if line_array[item_index] == 'HTTP/1.1"':
                continue
            else:
                return False
        if item_index == 7:
            if int_checker(line_array[item_index]):
                continue
            else:
                return False
        if item_index == 8:
            if int_checker(line_array[item_index]):
                continue
            else:
                return False
    return True


try:
    file_size = 0
    lines = 0
    status_counts = defaultdict(int)
    status_counts['200'] = 0
    status_counts['301'] = 0
    status_counts['400'] = 0
    status_counts['401'] = 0
    status_counts['403'] = 0
    status_counts['404'] = 0
    status_counts['405'] = 0
    status_counts['500'] = 0
    for line in stdin:
        lines += 1
        if lines % 10 == 0:
            line_array = line.split(' ')
            if checker(line_array):
                file_size += int(line_array[8])
                status_code = line_array[7]
                status_counts[status_code] += 1
            else:
                continue
            print('File size: {}'.format(file_size))
            for code, count in status_counts.items():
                if count > 0:
                    print('{}: {}'.format(code, count))
            lines = 0
        else:
            line_array = line.split(' ')
            if checker(line_array):
                file_size += int(line_array[8])
                status_code = line_array[7]
                status_counts[status_code] += 1
            else:
                continue
    if lines % 10 != 0:
        print('File size: {}'.format(file_size))
        for code, count in status_counts.items():
            if count > 0:
                print('{}: {}'.format(code, count))

except KeyboardInterrupt:
    print('File size: {}'.format(file_size))
    for code, count in status_counts.items():
        if count > 0:
            print('{}: {}'.format(code, count))
