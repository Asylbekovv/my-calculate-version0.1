print("Welcome to my simple calculator!")
num_fs = int(input("Enter first num: "))
num_sd = int(input("Enter second num: "))

# Запрос пользователя о выборе операции
choose = int(input("Enter the operation number (1 for +, 2 for -, 3 for *, 4 for /): "))


# Часть для сложения
def my_fn_plus(a, b):
    c = a + b
    return c


# Это часть для вычитания
def my_fn_minus(a, b):
    c = a - b
    return c


# Это часть для умножения
def my_fn_multi(a, b):
    c = a * b
    return c


# Это часть для деления
def my_fn_divide(a, b):
    if b != 0:
        c = a / b
        return c
    else:
        return "Division by zero is not allowed."


if choose == 1:
    result = my_fn_plus(num_fs, num_sd)
    print(f"You choose addition (+): {result}")
elif choose == 2:
    result = my_fn_minus(num_fs, num_sd)
    print(f"You choose subtraction (-): {result}")
elif choose == 3:
    result = my_fn_multi(num_fs, num_sd)
    print(f"You choose multiplication (*): {result}")
elif choose == 4:
    result = my_fn_divide(num_fs, num_sd)
    print(f"You choose division (/): {result}")
else:
    print("You did not enter a valid choice.")
