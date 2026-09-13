from decimal import Decimal

room_length = Decimal(input("Введите длину комнаты (м): "))
room_width = Decimal(input("Введите ширину комнаты (м): "))
room_height = Decimal(input("Введите высоту комнаты (м): "))

roll_width = Decimal(input("Введите ширину рулона обоев (м): "))
roll_length = Decimal(input("Введите длину рулона обоев (м): "))

walls_area = 2 * (room_length + room_width) * room_height
roll_area = roll_width * roll_length
rolls_needed = walls_area / roll_area

print("-" * 10)
print("Площадь стен:", walls_area, "м²")
print("Площадь одного рулона:", roll_area, "м²")
print("Необходимо рулонов:", rolls_needed)
