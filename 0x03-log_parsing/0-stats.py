#!/usr/bin/python3
"""script to analyze stdin values line by line"""
from sys import stdin
from collections import defaultdict

try:
    file_size = 0
    lines = 0
    status_counts = defaultdict(int)

    for line in stdin:
        lines += 1
        line_array = line.split(' ')
        if len(line_array) == 9:
            try:
                file_size += int(line_array[8])
            except ValueError:
                pass

            status_code = line_array[7]
            status_counts[status_code] += 1

        if lines == 10:
            lines = 0
            print('File size: {}'.format(file_size))
            for code, count in status_counts.items():
                if count > 0:
                    print('{}: {}'.format(code, count))

except KeyboardInterrupt:
    print('File size: {}'.format(file_size))
    for code, count in status_counts.items():
        if count > 0:
            print('{}: {}'.format(code, count))
