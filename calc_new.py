# My calculate
print("Simply calculate")


def plus_fn(n, m):
    l = n + m
    return l


def minus_fn(n, m):
    l = n - m
    return l
number_one = float(input("Enter first operation: "))
number_two = float(input("Enter second operation: "))
choose = input("Enter your operation + or - : ")
if choose == '+':
    result = plus_fn(number_one, number_two)
    print(f"Result: {plus_fn(number_one, number_two)}")
elif choose == '-':
    result = minus_fn(number_one, number_two)
    print(f"Result: {minus_fn(number_one, number_two)}")
else:
    print("You dont enter number!")


