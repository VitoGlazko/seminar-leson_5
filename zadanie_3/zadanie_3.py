import random
numbers = [random.randint(1, 10) for i in range(10)]
print(numbers)
print("Количество повторяющихся элементов ", len(list(filter(lambda x: numbers.count(x) > 1, numbers))))
result = []
for i in numbers:
    if numbers.count(i) > 1:
        numbers.remove(i)
print("Список уникальных элементов:")
print(numbers)
