import random
num = [random.randint(1, 10) for i in range(10)]
print(num)
result = lambda x: x > 5
num = list(filter(result, num))
print(num)