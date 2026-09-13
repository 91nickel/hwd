from decimal import Decimal
import math

room_length = Decimal(input("Введите длину комнаты (м): "))
room_width = Decimal(input("Введите ширину комнаты (м): "))
room_height = Decimal(input("Введите высоту комнаты (м): "))
room_windows_doors_area = Decimal(input("Введите общую площадь окон и дверей (м²): "))

roll_width = Decimal(input("Введите ширину рулона обоев (м): "))
roll_length = Decimal(input("Введите длину рулона обоев (м): "))

walls_area = 2 * (room_length + room_width) * room_height - room_windows_doors_area
one_strip_area = roll_width * room_height
strips_needed = math.ceil(walls_area / one_strip_area)
strips_per_roll = math.floor(roll_length / room_height)
rolls_needed = math.ceil(strips_needed / strips_per_roll)

print("-" * 10)
print("Площадь стен:", walls_area, "м²")
print("Площадь одной полосы обоев:", one_strip_area, "м²")
print("Нужно полос:", strips_needed)
print("Полос в рулоне:", strips_per_roll)
print("Необходимо рулонов:", rolls_needed)
