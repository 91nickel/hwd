# Задания к лекции 13.25 — Преобразования типов

| № | Задание |
|---|---------|
| 13.25.1 | [Сумма двух целых чисел](#задание-13251) |
| 13.25.2 | [Стоимость покупки](#задание-13252) |
| 13.25.3 | [Секунды в M:SS](#задание-13253) |
| 13.25.4 | [Возраст и совершеннолетие](#задание-13254) |
| 13.25.5 | [Карточка пользователя](#задание-13255) |
| 13.25.6 | [Повтор слова n раз](#задание-13256) |
| 13.25.7 | [Исправь сравнение a > b](#задание-13257) |

---

## Задание 13.25.1

Напиши программулечку, которая получает из командной строки два аргумента `a` и `b` (оба — целые числа) и печатает их сумму:

```
$ python3 main.py 2 3
5

$ python3 main.py 20 -7
13

$ python3 main.py 0004 0006
10
```

## Ответ

```python
import sys

x, y = map(int, sys.argv[1:])

print(sum([x, y]))
```

---

## Задание 13.25.2

Напиши программулечку, которая получает два аргумента `price` и `qty`. `price` — число с плавающей точкой, `qty` — целое число. Программулечка должна посчитать итоговую стоимость `price * qty` и вывести число ровно с двумя знаками после точки (например, `10.00`):

```
$ python3 main.py 19.99 3
59.97

$ python3 main.py 19.016 1
19.02

$ python3 main.py 2.5 4
10.00

$ python3 main.py 0.1 1
0.10
```

## Ответ

```python
import sys
from decimal import ROUND_HALF_UP, Decimal

x = Decimal(sys.argv[1]).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
y = int(sys.argv[2])

print(x * y)
```

---

## Задание 13.25.3

Напиши программулечку, которая получает один аргумент `seconds` (целое число) и печатает количество полных минут и оставшихся секунд в формате `M:SS` (секунды всегда двумя цифрами, количество цифр в минутах — одна или больше):

```
$ python3 main.py 0
0:00

$ python3 main.py 5
0:05

$ python3 main.py 125
2:05

$ python3 main.py 600
10:00
```

## Ответ

```python
import sys

x = int(sys.argv[1])

minutes = int(x / 60)
seconds = int(x % 60)

print(f"{minutes}:{seconds:02d}")
```

---

## Задание 13.25.4

Напиши программулечку, которая получает один аргумент — возраст (целое число) и печатает `True`, если пользователю 18 или больше, иначе печатает `False`:

```
$ python3 main.py 18
True

$ python3 main.py 17
False

$ python3 main.py 100
True
```

## Ответ

```python
import sys

print(int(sys.argv[1]) > 17)
```

---

## Задание 13.25.5

Напиши программулечку, которая получает три аргумента: `name` (строка), `is_admin` (строка `True` или `False`), `age` (целое число). Нужно вывести одну строку строго в формате: `name= admin= age= adult=` где `adult` — это `True`, если `age >= 18`, иначе `False`. `is_admin` нужно преобразовать в настоящее булево значение так: `is_admin == "True"`:

```
$ python3 main.py Иннокентий True 20
name=Иннокентий admin=True age=20 adult=True

$ python3 main.py Вася False 17
name=Вася admin=False age=17 adult=False

$ python3 main.py "Кирилл Полухин" True 18
name=Кирилл Полухин admin=True age=18 adult=True
```

## Ответ

```python
import sys

name, is_admin, age = sys.argv[1:]

print(
    f"name={name} admin={is_admin == 'True'} "
    + f"age={int(age)} adult={int(age) >= 18}"
)
```

---

## Задание 13.25.6

Напиши программулечку, которая получает один аргумент `n` (целое число) и один аргумент `word` (строка). Нужно вывести строку, состоящую из `word`, повторённого `n` раз подряд:

```
$ python3 main.py 3 ha
hahaha

$ python3 main.py 1 Python
Python

$ python3 main.py 0 wow
```

## Ответ

```python
import sys

x, y = sys.argv[1:]

print(y * int(x))
```

---

## Задание 13.25.7

Дан код программулечки, который должен печатать `True`, если первый аргумент (число) строго больше второго аргумента (число), иначе `False`. Сейчас оно работает неправильно. Исправь программулечку!

Код в main.py:

```python
import sys

a = sys.argv[1]
b = sys.argv[2]

print(a > b)
```

Должно работать так:

```
$ python3 main.py 2 10
False

$ python3 main.py 10.5 2
True

$ python3 main.py -1 -2
True
```

## Ответ

```python
import sys
from decimal import Decimal

a = Decimal(sys.argv[1])
b = Decimal(sys.argv[2])

print(a > b)
```