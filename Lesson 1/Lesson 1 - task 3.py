# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3
# + 33 + 333 = 369.

n = str(input("Please enter a number: "))
sum_n1 = n + n
sum_n2 = n + n + n
sum_total_1 = int(n)
sum_total_2 = int(sum_n1)
sum_total_3 = int(sum_n2)

print(sum_total_1 + sum_total_2 + sum_total_3)