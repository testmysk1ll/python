# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number_1 = int(input("Please enter an integer: "))
benchmark = 0
while number_1 > 0:
    number_last = number_1 % 10
    if number_last >= benchmark:
        benchmark = number_last
    number_1 = number_1 // 10
print(f"The largest number is: {benchmark}")