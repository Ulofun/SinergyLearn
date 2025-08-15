def sum_negative_between_min_max(A):
    # Нахождение индекса первого появления минимального и максимального элемента
    min_idx = A.index(min(A))
    max_idx = A.index(max(A))

    # Определяем начальную и конечную позицию диапазона
    start_idx = min(min_idx,
                    max_idx) + 1  # добавляем единицу, потому что диапазон начинается после одного из крайних элементов
    end_idx = max(min_idx, max_idx)

    # Суммируем отрицательные элементы внутри указанного диапазона
    result_sum = sum(x for x in A[start_idx:end_idx] if x < 0)

    return result_sum


# Пример использования
A = [-7, 3, -2, 8, -5, 4]
N = len(A)
result = sum_negative_between_min_max(A)
print("Сумма отрицательных элементов:", result)