# 5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника

Revenue = float(input("Please enter your revenues: "))
Costs = float(input("Please enter your costs: "))
if Revenue > Costs:
    print(f"You company is profitable with Net Income of {Revenue - Costs:.01f} and your Net Income margin is {(Revenue-Costs)/Revenue:%}")
    Staff = int(input("How many full time workers do you employ? "))
    print(f"You Net Income per one employee is {(Revenue-Costs)/Staff:.01f}")
elif Revenue == Costs:
    print("You Company is breakeven")
else:
    print(f"Your Company is loss making with Net Loss of {Revenue-Costs:.01f}")
