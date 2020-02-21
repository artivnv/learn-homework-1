"""
Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""
school_list = [
{'school_class': '4a', 'scores': [5,4,4,5,2]},
{'school_class': '4b', 'scores': [3,4,5,5,2]},
{'school_class': '5a', 'scores': [5,5,4,5,3]},
{'school_class': '5b', 'scores': [1,3,4,2,3]},
{'school_class': '6b', 'scores': [5,3,4,5,5]},
]

for group in school_list:
    sum_score = 0
    sum_group = 0
    all_school = 0
    for score in group['scores']:
        sum_score += score
        sum_group += 1
        all_school += (sum_score/sum_group)
    print(f'Средний балл по классу {group["school_class"]}: {sum_score/sum_group}')
print(f'Средний балл по всей школе: {all_school/sum_group}')









