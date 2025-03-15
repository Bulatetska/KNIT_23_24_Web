number = int(input("Введіть двоцифрове число: "))

if 10 <= abs(number) <= 99:
    sum = abs(number) // 10 + abs(number) % 10
    print(f"Сума цифр числа {number} дорівнює {sum}")
else:
    print("Будь ласка, введіть двоцифрове число!")
