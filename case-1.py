def sum_negative_between_max_min(arr):
    if not arr:
        return 0

    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))

    # Определение правильного порядка индексов
    if max_index > min_index:
        start, end = min_index, max_index
    else:
        start, end = max_index, min_index

    # Суммирование отрицательных элементы между максимальным и минимальным (исключая сами max и min)
    sum_negatives = sum(x for x in arr[start+1:end] if x < 0)

    return sum_negatives

# Пример:
A = [3, -1, -4, 2, -6, 7, -2, 5, -3, 8]
result = sum_negative_between_max_min(A)
print(result)  # Вывод: -5