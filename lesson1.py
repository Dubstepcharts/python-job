# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print(' - FizzBuzz')
#     if i % 5 == 0:
#         print(' - Buzz')
#     if i % 3 == 0:
#         print(' - Fizz')

# squares = [x**2 for x in range(1,10)]
# print(squares)

# squares = [1, 2, 3, 4, 5, 6]
# result = [x for x in squares if x % 2 == 0]
# print(result)

# squares = ["кот", "пёс", "лис"]
# result = [len(x) for x in squares]
# print(result)

# string = "hello world"
# result = [x for x in string if x.isalnum()]
# print(result)

# result = [x for x in range(10, 0, -1)]
# print(result)

# squares = [3, -1, 0, 7, -5, 2]
# result = [x if x >= 0 else 0 for x in squares]
# print(result)

# squares = [22, 2, 7, 55, 102, 2, 10]
# print([x for x in squares if x >= 10])

# strings = ["Hello", "", "WORLD", "Python", "", "  ", "TeSt", "123", "Привет", "", "Мир"]
# print([x.lower() for x in strings if x.isalnum()])

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -3, 0, -7, 12, 15]
# print([x**2 for x in nums if x % 2 != 0])

# names = ["Аня", "Борис", "Вика", "Глеб", "Даша", "Егор"]
# print(['Привет, ' + x + '!' for x in names])

# Вложенный for и работа с двумя источниками

#print([i for i in ["арбуз", "кот", "осень", "тигр", "ирис", "ёж", "слон", "утка"] if i[0] in "аеёиоуыэюя"])

#print([(i,j) for i in range(1, 4) for j in range(1, 4) if i != j])

# nums = [1, 2, 3]
# print([(i + j) for i in nums for j in nums])

# nested = [[1, 2], [3, 4], [5]]
# print([x for i in nested for x in i])

# strings = ["кот", "дом", "лес"]
# letters = "аеёиоуыэюя"
# print([j for i in strings for j in i if j not in letters])

# nums = [3, -1, 0, 7, -5, 2]
# print(['чёт' if x % 2 == 0 else 'нечёт' for x in nums])

# people = [("Аня", 17), ("Борис", 22), ("Вика", 18), ("Глеб", 15), ("Даша", 30)]
# print([i[0] for i in people if i[1] >= 18 ])

# print([i * j for i in range(3) for j in range(3)])

# s = "abc"
# print([i for x in range(len(s) - 1) for i in s[x]])

# nums = [1, 2, 3, 4, 5]
# print([(x + 1) * i for x in range(len(nums) - 1)] for i in nums)