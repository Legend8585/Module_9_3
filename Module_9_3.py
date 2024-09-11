first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

##Пример выполнения кода:
print(list(first_result))   # [1, 2]
print(list(second_result))  # [False, False, True]