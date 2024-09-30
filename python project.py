import random # подключаем модуль random
# Приветствие пользователю
print("Здравствуйте! Я ваш личный генератор сложных паролей.")
print("Как вас зовут?")
name = input('Напишите своё имя: ')
print(' Приятно познакомиться,', name,',' ' Представляю вам список моих возможностей: ')
print('''=================================
«Генератор сложных паролей»
  Команды:
    (1)десятка случайных чисел
    (2)случайные числа
    (3)случайные буквы
    (4)буквы и цифры вместе
    (5)сложный пароль(цифры,буквы,символы)
    для завершения работы напишите 0
''')
command = '100000'
parol =[]
while command != '0':
    print("=================================")
    command = input('Введите  номер команды: ')  # в переменную command записывается значение введённое пользователем
    if command ==  '1':
            for _ in range(10):
                parol.append(random.randint( 0,9))
            print(name,', ваш сгенерированный пароль:', *parol) # выводим случайный число из списка
    if command == '2':  # если True или True
            print(f'Случайное число {random.randint(0, 100)}')  # выводим результат выражения введенного пользователем
    if command ==  '3':  # если True или True
            alfa = 'абвгдеёжз'
            print(random.sample(alfa,3))  # выводим случайные буквы
    if command ==  '4':
            ллл = '12345абвгд'
            print(random.sample(ллл,10))  # выводим буквы и цифры вместе
    if command  == '5':
            chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
            num = input('Введите количество паролей: ') # вводим количество паролей
            leng = input('Введите длину пароля: ') # вводим длину пароля
            num = int(num)
            leng = int(leng)

            for n in range(num):
                password = ''
                for i in range(leng):
                    password += random.choice(chars)

                print(password)  # выводим сложный пароль
