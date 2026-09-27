# Задания к лекции 13.23 — Булевы

| № | Задание |
|---|---------|
| 13.23.1 | [Чётное ли число](#задание-132301) |
| 13.23.2 | [Первая буква заглавная](#задание-132302) |
| 13.23.3 | [Длина больше 10](#задание-132303) |
| 13.23.4 | [Первая и последняя буквы](#задание-132304) |
| 13.23.5 | [Есть ли цифра](#задание-132305) |
| 13.23.6 | [Число больше 28](#задание-132306) |
| 13.23.7 | [Палиндром](#задание-132307) |
| 13.23.8 | [Чётная ли длина](#задание-132308) |
| 13.23.9 | [Числа равны](#задание-132309) |
| 13.23.10 | [Одна чётность](#задание-1323010) |
| 13.23.11 | [Ровно два положительных](#задание-1323011) |
| 13.23.12 | [Хотя бы один ноль, не все](#задание-1323012) |
| 13.23.13 | [Делится на 3 и на 5](#задание-1323013) |
| 13.23.14 | [Различаются на 1](#задание-1323014) |
| 13.23.15 | [Двузначное и не кратно 11](#задание-1323015) |
| 13.23.16 | [Буква и цифра по краям](#задание-1323016) |
| 13.23.17 | [Кот или пёс, не оба](#задание-1323017) |
| 13.23.18 | [Палиндром без учёта регистра](#задание-1323018) |
| 13.23.19 | [Строка в строке](#задание-1323019) |
| 13.23.20 | [Три условия для строки](#задание-1323020) |
| 13.23.21 | [Только цифры и делится на 2 или 5](#задание-1323021) |
| 13.23.22 | [Точка в первой или третьей четверти](#задание-1323022) |
| 13.23.23 | [Строго возрастающая](#задание-1323023) |
| 13.23.24 | [Хотя бы два равны, не все три](#задание-1323024) |
| 13.23.25 | [Кратно 4 или 6, не 12](#задание-1323025) |
| 13.23.26 | [Отрицательное произведение](#задание-1323026) |
| 13.23.27 | [Пробелы внутри](#задание-1323027) |
| 13.23.28 | [@ левее точки](#задание-1323028) |
| 13.23.29 | [Равны без учёта регистра](#задание-1323029) |
| 13.23.30 | [Один в диапазоне 10–20](#задание-1323030) |
| 13.23.31 | [Три разных символа](#задание-1323031) |
| 13.23.32 | [Заканчивается на t](#задание-1323032) |
| 13.23.33 | [Между b и c](#задание-1323033) |
| 13.23.34 | [Корректная дата](#задание-1323034) |

---

## Задание 13.23.1

Напиши программулечку, которая получает аргументом командной строки число и печатает True, если оно чётное, и False в противном случае.

```
$ python3 main.py 100
True

$ python3 main.py 100123241
False
```

## Ответ

```python
import sys

num = int(sys.argv[1].strip())

print(num % 2 == 0)
```

---

## Задание 13.23.2

Напиши программулечку, которая получает аргументом командной строки строку и печатает True, если первая буква заглавная, и False в противном случае.

```
$ python3 main.py "Василий"
True

$ python3 main.py "не Василий"
False
```

## Ответ

```python
import sys

string = sys.argv[1].strip()

print(string[0].isupper())
```

---

## Задание 13.23.3

Напиши программулечку, которая получает аргументом командной строки строку и печатает True, если длина этой строки больше 10 символов, и False в противном случае.

```
$ python3 main.py "упс"
False

$ python3 main.py "синхрофазотронище"
True
```

## Ответ

```python
import sys

string = sys.argv[1].strip()

print(len(string) > 10)
```

---

## Задание 13.23.4

Напиши программулечку, которая получает аргументом командной строки строку и печатает True, если строка начинается и заканчивается одной и той же буквой без учёта регистра, и False в противном случае.

```
$ python3 main.py "упс"
False

$ python3 main.py "синхрофазотронище"
False

$ python3 main.py "баобаб"
True

$ python3 main.py "Баобаб"
True
```

## Ответ

```python
import sys

string = sys.argv[1].strip()

print(string[0].upper() == string[-1].upper())
```

---

## Задание 13.23.5

Напиши программулечку, которая получает аргументом командной строки строку и печатает True, если в строке есть хотя бы одна цифра, и False в противном случае.

```
$ python3 main.py "упс"
False

$ python3 main.py "синхрофазотронище, 2 штуки или нет"
True

$ python3 main.py "баобаб"
False

$ python3 main.py "три баобаба"
False

$ python3 main.py "3 баобаба"
True
```

## Ответ

```python
import re
import sys

string = sys.argv[1].strip()

print(re.search(r"\d", string) is not None)
```

---

## Задание 13.23.6

Напиши программулечку, которая получает аргументом командной строки число и печатает True, если число больше 28, и False в противном случае.

```
$ python3 main.py 28
False

$ python3 main.py 29
True

$ python3 main.py 0
False

$ python3 main.py 128
True
```

## Ответ

```python
import sys

num = int(sys.argv[1].strip())

print(num > 28)
```

---

## Задание 13.23.7

Напиши программулечку, которая получает аргументом командной строки строку и печатает True, если строка палиндром (одинаково читается вперёд и назад), и False в противном случае.

```
$ python3 main.py дед
True

$ python3 main.py банан
False

$ python3 main.py заказ
True
```

## Ответ

```python
import sys

normal = sys.argv[1].strip()
reverse = normal[::-1]

print(normal == reverse)
```

---

## Задание 13.23.8

Напиши программулечку, которая получает аргументом командной строки строку и определяет, чётная ли длина этой строки:

```
$ python3 main.py "паника в селе"
В строке «паника в селе» количество символов: 13, чётное ли это число? False

$ python3 main.py "дед сбесился"
В строке «дед сбесился» количество символов: 12, чётное ли это число? True
```

Используй f-string.

## Ответ

```python
import sys

string = sys.argv[1]
length = len(string)
is_even = length % 2 == 0
output = f"В строке «{string}» количество символов: {length},"
output2 = f"чётное ли это число? {is_even}"
print(f"{output} {output2}")
```

---

## Задание 13.23.9

Напиши программулечку, которая получает аргументом командной два целых числа и печатает True, если они равны, и False в противном случае.

```
$ python3 main.py 21 21
True

$ python3 main.py 21 12
False
```

## Ответ

```python
import sys

numA = int(sys.argv[1])
numB = int(sys.argv[2])

print(numA == numB)
```

---

## Задание 13.23.10

Напиши программулечку, которая получает двумя аргументами целые числа a и b и печатает True, если a и b одной чётности, и False в противном случае.

```
$ python3 main.py 10 4
True

$ python3 main.py 10 5
False

$ python3 main.py -3 7
True
```

Как получить несколько аргументов командной строки? Просто — по индексу. Например, в первом примере sys.argv[1] это 10, а sys.argv[2] это 4.

Обрати внимание на будущее:

```
$ python3 main.py Алексей Иванович
```

тут sys.argv[1] это Алексей, а sys.argv[2] это Иванович. Это два разных параметра командной строки.

А вот так:

```
$ python3 main.py "Алексей Иванович"
```

уже один параметр, sys.argv[1] это Алексей Иванович, а sys.argv[2] здесь нет. Аналогично будет, если экранировать пробел обратным слешем:

```
$ python3 main.py Алексей\ Иванович
```

Тут тоже только один параметр, sys.argv[1] это Алексей Иванович.

Это важные особенности. Попрактикуйся с ними.

## Ответ

```python
import sys

numA = int(sys.argv[1])
numB = int(sys.argv[2])

print((numA % 2) == (numB % 2))
```

---

## Задание 13.23.11

Напиши программулечку, которая получает тремя аргументами целые числа a, b, c и печатает True, если ровно два из них положительные, и False в противном случае.

```
$ python3 main.py 5 1 -2
True

$ python3 main.py 5 1 2
False

$ python3 main.py -1 -2 3
False
```

## Ответ

```python
import sys

number_list = map(int, sys.argv[1:])

above_zero_counter = 0

for number in number_list:
    if number > 0:
        above_zero_counter += 1


print(above_zero_counter == 2)
```

### Сообщение от преподавателя

Конечно, можно в лоб — перебирать все комбинации чисел и смотреть, выполняются ли условия.

Вариант рабочий, но унылый.

Можно так:

```python
import sys

a, b, c = map(int, sys.argv[1:4])
positive_count = (a > 0) + (b > 0) + (c > 0)
print(positive_count == 2)
```

map мы пока не знаем. Можно и с текущим синтаксисом, чуть длиннее:

```python
import sys

a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
positive_count = (a > 0) + (b > 0) + (c > 0)
print(positive_count == 2)
```

Как видишь, bool тоже можно складывать — работает как int. True это 1, False это 0.

---

## Задание 13.23.12

Напиши программулечку, которая получает тремя аргументами целые числа a, b, c и печатает True, если хотя бы одно из них равно нулю, но не все три одновременно, иначе False.

```
$ python3 main.py 0 2 3
True

$ python3 main.py 0 0 5
True

$ python3 main.py 0 0 0
False
```

## Ответ

```python
import sys

number_list = sys.argv[1:]
sum = sum(map(lambda v: int(v) == 0, sys.argv[1:]))

print(sum > 0 and sum < len(number_list))
```

### Сообщение от преподавателя

Например:

```python
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

has_zero = a == 0 or b == 0 or c == 0
all_zero = a == 0 and b == 0 and c == 0

print(has_zero and not all_zero)
```

---

## Задание 13.23.13

Напиши программулечку, которая получает двумя аргументами целые числа a и b и печатает True, если одно из чисел делится на 3, а другое делится на 5, иначе False.

```
$ python3 main.py 9 20
True

$ python3 main.py 10 18
True

$ python3 main.py 6 25
True

$ python3 main.py 6 11
False
```

## Ответ

```python
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])


print((a % 3 == 0 and b % 5 == 0) or (a % 5 == 0 and b % 3 == 0))
```

---

## Задание 13.23.14

Напиши программулечку, которая получает двумя аргументами целые числа a и b и печатает True, если они различаются ровно на 1, иначе False.

```
$ python3 main.py 10 11
True

$ python3 main.py -2 -1
True

$ python3 main.py 10 12
False
```

## Ответ

```python
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

print((a - b == 1) or (b - a == 1))
```

---

## Задание 13.23.15

Напиши программулечку, которая получает одним аргументом целое число n и печатает True, если n — двузначное число и при этом не кратно 11, иначе False.

```
$ python3 main.py 42
True

$ python3 main.py 99
False

$ python3 main.py 7
False
```

## Ответ

```python
import sys

a = int(sys.argv[1])

print(len(str(a)) == 2 and (a % 11 != 0))
```

---

## Задание 13.23.16

Напиши программулечку, которая получает одним аргументом строку s и печатает True, если строка начинается с буквы и заканчивается цифрой, либо начинается с цифры и заканчивается буквой, иначе False.

```
$ python3 main.py я9
True

$ python3 main.py 9з
True

$ python3 main.py w9
True

$ python3 main.py ab
False
```

## Ответ

```python
import sys

if len(sys.argv) > 1 and len(sys.argv[1]) > 1:
    string = sys.argv[1]
    first_cond = string[0].isalpha() and string[-1].isdigit()
    second_cond = string[-1].isalpha() and string[0].isdigit()
    print(first_cond or second_cond)
else:
    print(False)
```

### Сообщение от преподавателя

Например, что-то такое:

```python
import sys

s = sys.argv[1]
is_lenght_ok = len(s) >= 2
print(
    is_lenght_ok
    and (
        (s[0].isalpha() and s[-1].isdigit())
        or (s[-1].isalpha() and s[0].isdigit())
    )
)
```

---

## Задание 13.23.17

Напиши программулечку, которая получает одним аргументом строку s и печатает True, если в строке есть подстрока "кот" или "пёс", но не обе одновременно, иначе False.

```
$ python3 main.py "мой кот"
True

$ python3 main.py "пёс хороший мальчик"
True

$ python3 main.py "котопёс"
False
```

## Ответ

```python
import sys

has_dog = sys.argv[1].find("пёс") != -1
has_cat = sys.argv[1].find("кот") != -1

print(has_dog ^ has_cat)
```

---

## Задание 13.23.18

Напиши программулечку, которая получает одним аргументом строку s и печатает True, если строка является палиндромом без учёта регистра, но при этом не пустая, иначе False.

```
$ python3 main.py Abba
True

$ python3 main.py level
True

$ python3 main.py ""
False
```

## Ответ

```python
import sys

normal = sys.argv[1]
reverse = sys.argv[1][::-1]

print(normal.casefold() == reverse.casefold() and len(normal) > 0)
```

---

## Задание 13.23.19

Напиши программулечку, которая получает двумя аргументами строки a и b и печатает True, если a содержится в b или b содержится в a, но при этом строки не равны, иначе False.

```
$ python3 main.py he hello
True

$ python3 main.py hello hello
False

$ python3 main.py abc zzz
False
```

## Ответ

```python
import sys

a = (sys.argv[1])
b = (sys.argv[2])

print((a in b or b in a) and a != b)
```

---

## Задание 13.23.20

Напиши программулечку, которая получает одним аргументом строку s и печатает True, если строка не пустая, длина строки чётная и строка не меняется при преобразовании всех символов к нижнему регистру, иначе False.

```
$ python3 main.py Привет
False

$ python3 main.py привет
True

$ python3 main.py aBcd
False

$ python3 main.py ABC
False

$ python3 main.py abcd
True

$ python3 main.py ""
False
```

## Ответ

```python
import sys

a = (sys.argv[1])

print(len(a) > 0 and len(a) % 2 == 0 and a.lower() == a)
```

---

## Задание 13.23.21

Напиши программулечку, которая получает одним аргументом строку s и печатает True, если строка состоит только из цифр и представляет число, которое делится без остатка на 2 или на 5, иначе False.

```
$ python3 main.py 120
True

$ python3 main.py 33
False

$ python3 main.py 17a
False
```

## Ответ

```python
import sys

a = (sys.argv[1])

print(a.isdigit() and (int(a) % 2 == 0 or int(a) % 5 == 0))
```

---

## Задание 13.23.22

Напиши программулечку, которая получает двумя аргументами целые числа x и y и печатает True, если точка (x, y) лежит в первой или третьей четверти, но не на осях, иначе False.

```
$ python3 main.py 3 4
True

$ python3 main.py -2 -7
True

$ python3 main.py 0 5
False
```

## Ответ

```python
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

is_abs_positive = abs(x) > 0 and abs(y) > 0
both_negative = x < 0 and y < 0
both_positive = x > 0 and y > 0

print(is_abs_positive and (both_negative or both_positive))
```

### Сообщение от преподавателя

Например:

```python
import sys

x = int(sys.argv[1])
y = int(sys.argv[2])

print(x * y > 0)
```

---

## Задание 13.23.23

Напиши программулечку, которая получает тремя аргументами целые числа a, b, c и печатает True, если из них можно составить строго возрастающую последовательность перестановкой, иначе False.

```
$ python3 main.py 1 2 3
True

$ python3 main.py 3 1 2
True

$ python3 main.py 2 2 3
False
```

## Ответ

```python
import sys

x, y, z = map(int, sys.argv[1:])

print(
    (
        x > y > x
        or x > z > y
        or y > x > z
        or y > z > x
        or z > x > y
        or z > y > x
    ) or (
        x < y < x
        or x < z < y
        or y < x < z
        or y < z < x
        or z < x < y
        or z < y < x
    )
)
```

---

## Задание 13.23.24

Напиши программулечку, которая получает тремя аргументами целые числа a, b, c и печатает True, если хотя бы два из них равны между собой, но не все три, иначе False.

```
$ python3 main.py 5 5 1
True

$ python3 main.py 7 7 7
False

$ python3 main.py 1 2 3
False
```

## Ответ

```python
import sys

x, y, z = map(int, sys.argv[1:])

print((x == y or x == z or y == z) and not (x == y == z))
```

---

## Задание 13.23.25

Напиши программулечку, которая получает одним аргументом целое число n и печатает True, если n кратно 4 или 6, но не кратно 12, иначе False.

```
$ python3 main.py 8
True

$ python3 main.py 18
True

$ python3 main.py 24
False
```

## Ответ

```python
import sys

x = int(sys.argv[1])

print((x % 4 == 0 or x % 6 == 0) and not x % 12 == 0)
```

---

## Задание 13.23.26

Напиши программулечку, которая получает двумя аргументами целые числа a и b и печатает True, если произведение a * b отрицательное, иначе False.

```
$ python3 main.py -3 5
True

$ python3 main.py -3 -5
False

$ python3 main.py 0 10
False
```

## Ответ

```python
import sys

x, y = map(int, sys.argv[1:])

print((x * y) < 0)
```

---

## Задание 13.23.27

Напиши программулечку, которая получает одним аргументом строку s и печатает True, если строка содержит хотя бы один пробел и при этом не начинается и не заканчивается пробелом, иначе False.

```
$ python3 main.py "hello world"
True

$ python3 main.py " hello world"
False

$ python3 main.py "helloworld"
False
```

## Ответ

```python
import sys

x = sys.argv[1]

print(len(x) > 0 and x[0] != ' ' and x[-1] != ' ' and x.find(' ') != -1)
```

### Сообщение от преподавателя

Например:

```python
import sys

s = sys.argv[1]

result = (" " in s) and (not s.startswith(" ")) and (not s.endswith(" "))
print(result)
```

---

## Задание 13.23.28

Напиши программулечку, которая получает одним аргументом строку s и печатает True, если строка содержит символ @ и символ ., причём @ стоит левее точки, иначе False.

```
$ python3 main.py "a@b.com"
True

$ python3 main.py "ivan.petrov@mail.ru"
True

$ python3 main.py "a.b@com"
False

$ python3 main.py "abc"
False
```

## Ответ

```python
import sys

x = sys.argv[1]

dog_found = False
point_found = False
mainCondition = False

for symbol in x:
    if symbol == '@':
        dog_found = True
    if symbol == '.':
        point_found = True
        if dog_found:
            mainCondition = True
        else:
            mainCondition = False

print(dog_found and point_found and mainCondition)
```

---

## Задание 13.23.29

Напиши программулечку, которая получает двумя аргументами строки s и t и печатает True, если s и t равны без учёта регистра, но не равны с учётом регистра, иначе False.

```
$ python3 main.py Hello hello
True

$ python3 main.py test test
False

$ python3 main.py Abc aBd
False
```

Почитай о методе строк casefold.

## Ответ

```python
import sys

x, y = sys.argv[1:]

print(x != y and x.casefold() == y.casefold())
```

---

## Задание 13.23.30

Напиши программулечку, которая получает двумя аргументами целые числа a и b и печатает True, если хотя бы одно из чисел находится в диапазоне от 10 до 20 включительно, но не оба одновременно, иначе False.

```
$ python3 main.py 15 30
True

$ python3 main.py 12 19
False

$ python3 main.py 9 25
False
```

## Ответ

```python
import sys

x, y = map(int, sys.argv[1:])

print((9 < x < 21) ^ (9 < y < 21))
```

### Сообщение от преподавателя

Например:

```python
import sys

a = int(sys.argv[1])
b = int(sys.argv[2])

in_a = 10 <= a <= 20
in_b = 10 <= b <= 20

print(in_a != in_b)
```

---

## Задание 13.23.31

Напиши программулечку, которая получает одним аргументом строку s и печатает True, если строка длины 3 и все её символы различны, иначе False.

```
$ python3 main.py abc
True

$ python3 main.py aba
False

$ python3 main.py abcd
False
```

## Ответ

```python
import sys

x = sys.argv[1]

print(len(x) == 3 and x[0] != x[1] and x[1] != x[2] and x[0] != x[2])
```

---

## Задание 13.23.32

Напиши программулечку, которая получает двумя аргументами строки s и t и печатает True, если s заканчивается на t и при этом t не пустая, иначе False.

```
$ python3 main.py "hello" "lo"
True

$ python3 main.py "hello" ""
False

$ python3 main.py "hello" "la"
False
```

## Ответ

```python
import sys

x, y = sys.argv[1:]

print(y != '' and x[::-1].find(y[::-1]) == 0)
```

---

## Задание 13.23.33

Напиши программулечку, которая получает тремя аргументами целые числа a, b, c и печатает True, если a находится строго между b и c (то есть либо b < a < c, либо c < a < b), иначе False.

```
$ python3 main.py 5 1 10
True

$ python3 main.py 5 10 1
True

$ python3 main.py 5 1 5
False
```

## Ответ

```python
import sys

x, y, z = map(int, sys.argv[1:])

print(y < x < z or z < x < y)
```

---

## Задание 13.23.34

Напиши программулечку, которая получает тремя аргументами целые числа day, month, year и печатает True, если month в диапазоне 1..12 и day в диапазоне 1..31, и при этом не бывает 31-го числа в апреле, июне, сентябре и ноябре, иначе False.

```
$ python3 main.py 30 4 2024
True

$ python3 main.py 31 4 2024
False

$ python3 main.py 15 13 2024
False
```

## Ответ

```python
import sys

x, y, z = map(int, sys.argv[1:])

day = x
month = y
year = z

print(
    1 <= month <= 12
    and (
        (month in [2] and 1 <= day <= 29)
        or (month in [4, 6, 9, 11] and 1 <= day <= 30)
        or (month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31)
    )
)
```