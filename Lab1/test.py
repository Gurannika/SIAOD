

def selectionSort(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            min_i, min_j = i, j
            for x in range(i, len(matrix)):
                for y in range(j if x == i else 0, len(matrix[0])):
                    if matrix[x][y] < matrix[min_i][min_j]:
                        min_i, min_j = x, y
            matrix[i][j], matrix[min_i][min_j] = matrix[min_i][min_j], matrix[i][j]
    return matrix







    return arr


array = [[30, 60, 20], [50, 40, 10], [70, 90, 80]]
sorted_array = selection_sort(array)
print(sorted_array)