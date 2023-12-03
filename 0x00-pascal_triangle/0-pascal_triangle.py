def pascal_triangle(n):
    arr = [];
    for i in range(1, n+1):
        arr.append([]);
        for j in range(0, i):
            if (j > 0 and j < i - 1):
                arr[i - 1].append(arr[i - 2][j] + arr[i - 2][j - 1]);
            else:
                arr[i - 1].append(1);
    return arr;
