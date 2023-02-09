"""
Даны два неупорядоченных набора целых чисел (может быть, с
повторениями). Выдать без повторений в порядке возрастания все те числа, которые
встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
элементов второго множества. Затем пользователь вводит сами элементы множеств.

"""
"""
n = int(input("Задайте количество элементов первого множества:"))
m = int(input("Задайте количество элементов второго множества:"))

n_list = []
m_list = []

for i in range(n):
    n_list.append(int(input(f'Введите число {i}-e:')))
for i in range(m):
    m_list.append(int(input(f'Введите число {i}-e:')))

n_list.sort()
n_set = set(n_list)
m_set = set(m_list)

result = n_set.intersection(m_set)
result = list(result)
result.sort()

print(*result, sep=" ")
"""

"""
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
круглой грядке, причем кусты высажены только по окружности. Таким образом, у
каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai
 ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
"""
"""

import random
n = 0
while n < 3:
    n = int(input("Сколько кустов в грядке? "))
    if n < 3: print("Круглой грядки не получится. Введите число больше 2.")

berries = []

#for i in range(n):
#    berries.append(int(input(f'Введите количество ягод на {i}-м кусте:')))

for i in range(n):
    berries.append(random.randint(0,10))
print(berries)

max_basket = berries[n-1]+berries[0]+berries[1]
for i in range(n-1):
    basket = berries[i] + berries[i+1] + berries[i-1]
    if basket > max_basket: max_basket = basket
basket = berries[0] + berries[n-1] + berries[n-2]
if basket > max_basket: max_basket = basket

print(max_basket)

"""
"""
Задача FOOTBALL необязательная. 
Напишите программу, которая принимает на стандартный вход список игр футбольных команд с результатом матча 
и выводит на стандартный вывод сводную таблицу результатов всех матчей.

За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число nn — количество завершенных игр.
После этого идет nn строк, в которых записаны результаты игры в следующем формате:
Перваякоманда;Забитопервойкомандой;Втораякоманда;Забитовторойкомандой

Вывод программы необходимо оформить следующим образом:
Команда:Всегоигр Побед Ничьих Поражений Всегоочков

Конкретный пример ввода-вывода приведён ниже.

Порядок вывода команд произвольный.

Sample Input:

3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6
"""
def arr_El(stroka):           # Разделение строки на части
  arr = ['', '','', '']
  arr_n = find_El(stroka)
  arr_n.insert(0,0)
  for i in range(3):
    arr[i] = stroka[arr_n[i]:(arr_n[i+1]-1)]
  arr[3] = stroka[(arr_n[3]):]
  return arr

def find_El(stroka):      # Номера ;
  arr = [0,0,0] 
  n = 0
  for i in range(3):
    while n < len(stroka):
      if stroka[n] != ';':
        n +=1
      else:
        n +=1
        break
    arr[i] = n
  return arr

n = int(input('Введите количество игр:'))
arr_game1 = list(range(n))            # Массив из строк
for i in range(n):
  arr_game1[i] = input(f'Введите результат игры {i}:')

#n=6                 # Test
#arr_game1 = ['Локомотив;12;Зенит;3','Спартак;9;Зенит;10','Спартак;8;Локомотив;15', 'Спартак;8;Локомотив;8', 'Динамо;8;Локомотив;5', 'Спартак;8;Динамо;15']  # Test
arr_game = list(range(n))
for i in range(n):                  # Формирование прямоугольного массива
  arr_game[i] = arr_El(arr_game1[i])
arr_name = []                       # Матрица с названиями команд           
for i in range(n):
  for j in range(0,4,2):
    if arr_game[i][j] not in arr_name:
      arr_name.append(arr_game[i][j])
result = []                      # обработка данных
for i in range(len(arr_name)):  # имя i 
  name = arr_name[i]
  count = 0
  win = 0
  draw = 0
  defeat = 0
  
  for j in range(n):            # строка с игрой
    if name == arr_game[j][0]: 
      n1 = int(arr_game[j][1])
      n2 = int(arr_game[j][3])
    elif name == arr_game[j][2]: 
      n1 = int(arr_game[j][3])
      n2 = int(arr_game[j][1])
    else: continue
    count += 1
    if n1 > n2: win +=1
    elif n1 < n2: defeat += 1
    else: draw += 1
    score = 3 * win + draw
  result.append([name, count, win, draw, defeat, score])
for i in range(len(arr_name)):
 print(f'{result[i][0]}: {result[i][1]} {result[i][2]} {result[i][3]} {result[i][4]} {result[i][5]}')

"""
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных (где только буквы присутствуют для простоты).
например декодирование
"""

"""

def Decode_Letter(letter, word):
  result = ''
  if Number_exam(letter):
    n = Decode_number(letter, word)
    m = Number_chek(n)
    for j in range(n - 1):
      result = result + word[m - 1]
  else: result = result + letter
  return result

def Decode_number(letter, word): # Возвращает число символов в серии
  n = 0
  flag = True
  while len(word) > 0 and flag:
    if Number_exam(letter):
      n = n * 10 + int(letter)
      letter = word[0]
      word = word[1:]
    else: flag = False
  return n

def Number_exam(letter):         # Проверяет цифра или буква
  if 48<=ord(letter)<=57: result = True
  else: result = False
  return result

def Number_chek(n):             # Вычисляет количество разрядов
  m = 0
  while n > 0:
    n = n // 10
    m = m + 1
  return m

def Decode(word):              # Декодирование
  result = ''
  while len(word) > 0:
    letter = word[0]
    word = word[1:]
    result = result + Decode_Letter(letter, word)
    if Number_exam(letter):
      n = Decode_number(letter, word)
      m = Number_chek(n)
      word = word[(m-1):]
  print(result)

def Letter_count(letter, word):    # Подсчет символов в серии
  n = 1
  flag = True
  while flag and len(word) > 0:
    if word[0] == letter:
     n = n + 1
     word = word[1:]
    else:
      flag = False
  return n


def Code(word):     # Кодирование
  result = ''
  while len(word) > 0:
    n=0
    letter = word[0]
    word = word[1:]
    n = Letter_count(letter, word)
    if n > 1:
      result = result + str(n) + letter
      word = word[n-1:]
    else: 
      result = result + letter
  print(result)

word = input("Введите закодированную фразу: ")
print('Выберите действие:\n 1 - кодирование;\n 2 - декодирование.')
choice = input()
if choice == '1': 
 Code(word)
else:
 Decode(word) 
"""
