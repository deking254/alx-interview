#!/usr/bin/python3
"""script to analyse stdin values line by line"""
from sys import stdin
try:
    file_size = 0
    lines = 0
    count_200 = 0
    count_301 = 0
    count_400 = 0
    count_401 = 0
    count_403 = 0
    count_404 = 0
    count_405 = 0
    count_500 = 0
    for line in stdin:
        lines += 1
        line_array = line.split(' ')
        if len(line_array) == 9:
            try:
                file_size += int(line_array[8])
            except Exception as e:
                lines -= 1
            if (line_array[7] == '200'):
                count_200 += 1
            if (line_array[7] == '301'):
                count_301 += 1
            if (line_array[7] == '400'):
                count_400 += 1
            if (line_array[7] == '401'):
                count_401 += 1
            if (line_array[7] == '403'):
                count_403 += 1
            if (line_array[7] == '404'):
                count_404 += 1
            if (line_array[7] == '405'):
                count_405 += 1
            if (line_array[7] == '500'):
                count_500 += 1
        else:
            lines -= 1
        if lines == 10:
            print('File size: {}'.format(file_size))
            if (count_200 > 0):
                print('{}: {}'.format(200, count_200))
            if (count_301 > 0):
                print('{}: {}'.format(301, count_301))
            if (count_400 > 0):
                print('{}: {}'.format(400, count_400))
            if (count_401 > 0):
                print('{}: {}'.format(401, count_401))
            if (count_403 > 0):
                print('{}: {}'.format(403, count_403))
            if (count_404 > 0):
                print('{}: {}'.format(404, count_404))
            if (count_405 > 0):
                print('{}: {}'.format(405, count_405))
            if (count_500 > 0):
                print('{}: {}'.format(500, count_500))
            file_size = 0
            lines = 0
            count_200 = 0
            count_301 = 0
            count_400 = 0
            count_401 = 0
            count_403 = 0
            count_404 = 0
            count_405 = 0
            count_500 = 0
except KeyboardInterrupt as e:
    print('File size: {}'.format(file_size))
    if (count_200 > 0):
        print('{}: {}'.format(200, count_200))
    if (count_301 > 0):
        print('{}: {}'.format(301, count_301))
    if (count_400 > 0):
        print('{}: {}'.format(400, count_400))
    if (count_401 > 0):
        print('{}: {}'.format(401, count_401))
    if (count_403 > 0):
        print('{}: {}'.format(403, count_403))
    if (count_404 > 0):
        print('{}: {}'.format(404, count_404))
    if (count_405 > 0):
        print('{}: {}'.format(405, count_405))
    if (count_500 > 0):
        print('{}: {}'.format(500, count_500))
