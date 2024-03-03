import random
import time

m = int(input())
n = int(input())
min_limit = int(input())
max_limit = int(input())

def rand_arr(m, n, min_limit, max_limit):
    arr = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(min_limit, max_limit))
        arr.append(row)
    return arr

arr1 = rand_arr(m, n, min_limit, max_limit)
print(arr1)


