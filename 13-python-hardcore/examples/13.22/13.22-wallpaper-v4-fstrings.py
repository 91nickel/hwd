from decimal import Decimal
import math

# Запрашиваем размеры комнаты
room_length = Decimal(input("Введите длину комнаты (м): ").replace(",", ".").strip())
room_width = Decimal(input("Введите ширину комнаты (м): ").replace(",", ".").strip())
room_height = Decimal(input("Введите высоту комнаты (м): ").replace(",", ".").strip())
room_windows_doors_area = Decimal(input("Введите общую площадь окон и дверей (м²): ").replace(",", ".").strip())

# Запрашиваем параметры обоев
roll_width = Decimal(input("Введите ширину рулона обоев (м): ").replace(",", ".").strip())
roll_length = Decimal(input("Введите длину рулона обоев (м): ").replace(",", ".").strip())

# Общая площадь стен за минусом площади дверей и окон
walls_area = 2 * (room_length + room_width) * room_height - room_windows_doors_area

# Площадь одной полосы обоев от пола до потолка
one_strip_area = roll_width * room_height

# Требуемое количество полос
strips_needed = math.ceil(walls_area / one_strip_area)

# Сколько полос в рулоне
strips_per_roll = math.floor(roll_length / room_height)

# Количество рулонов
rolls_needed = math.ceil(strips_needed / strips_per_roll)

print(f"""
{"-" * 10}
Площадь стен: {walls_area} м²
Площадь одной полосы обоев: {one_strip_area} м²
Нужно полос: {strips_needed}
Полос в рулоне: {strips_per_roll}
Необходимо рулонов: {rolls_needed}
""".strip())