"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

create_dict = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую.', 'Нравится?': 'Да.'}
print('Введите ваш вопрос:')
def ask_user():
  try:
    while True:
      user_say = input()
      if user_say in create_dict.keys():
          print(create_dict[user_say])
      else:
          print('Вопрос неверный.')
  except KeyboardInterrupt:
      print('\n''Пока!')
if __name__ == "__main__":
    ask_user()