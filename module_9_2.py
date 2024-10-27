# Домашнее задание по теме "Списковые, словарные сборки"

first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Первая часть
first_result = [len(s) for s in first_strings if len(s) >= 5]

# Вторая часть
second_result = [
    (s1, s2)
    for s1 in first_strings
    for s2 in second_strings
    if len(s1) == len(s2)
]

# Третья часть
all_strings = first_strings + second_strings
third_result = {
    s: len(s)
    for s in all_strings
    if len(s) % 2 == 0
}

# Вывод результатов
print("Первая часть:", first_result)
print("Вторая часть:", second_result)
print("Третья часть:", third_result)