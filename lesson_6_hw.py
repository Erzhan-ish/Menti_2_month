def two_sum(nums, target):
    # Создаём словарь для хранения уже встреченных чисел и их индексов
    seen = {}

    # Перебираем массив по индексам и значениям
    for i, num in enumerate(nums):
        # Вычисляем, какое число нужно, чтобы в сумме получилось target
        complement = target - num

        # Если это число уже встречалось — возвращаем пару индексов
        if complement in seen:
            return [seen[complement], i]

        # Если не встречалось — запоминаем текущее число и его индекс
        seen[num] = i


print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))  # [1, 2]
print(two_sum([3, 3], 6))  # [0, 1]
