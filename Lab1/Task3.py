import random
import time


# создание массива
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

# Сортровка выбором (ищем минимум и ставим на первое место)
def selectionSort(array):
    for i in range(len(array)-1):
        min_idx = i
        for idx in range(i + 1, len(array)-1):
            if array[idx] < array[min_idx]:
                min_idx = idx
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

# Сортировка вставкой (часть массива принимаеться за сортированный)
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array

# Сортировка обменом (Сравниваются соседние элементы)

def bubbleSort(array):
    swapped = False
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array

# Сортировка Шелла (Сравнение чисел с шагом
def shellSort(array):
    import math

    n = len(array)
    k = int(math.log2(n))
    interval = 2**k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval
            array[j] = temp
        k -= 1
        interval = 2**k - 1
    return array

# Быстрая сортровка
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = [x for x in arr[1:] if x < pivot]
        right = [x for x in arr[1:] if x >= pivot]
        return quickSort(left) + [pivot] + quickSort(right)



# Турнирная сортировка

def tournamentSort(array):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def tournament(array):
        if len(array) <= 1:
            return array
        else:
            mid = len(array) // 2
            left = tournament(array[:mid])
            right = tournament(array[mid:])
            return merge(left, right)

    return tournament(array)


#Преобразуем матрицу в массив
def join(matrix):
    result = []
    for row in matrix:
        for item in row:
            result.append(item)
    return result
#преобразуем массив в матрицу
def fold(array, rowLength):
    result = []
    for i in range(0, len(array), rowLength):
        result.append(array[i : i + rowLength])
    return result
#Вывод результата
def sort_matrix(matrix, sort_func):
    array = join(matrix)

    start_time = time.time()
    sorted = sort_func(array)
    end_time = time.time()
    delta = end_time - start_time
    print(f"{sort_func.__name__}: {delta*1000} ms")

    return fold(sorted, len(matrix[0]))


x = sort_matrix(arr1, insertionSort)
print(x)