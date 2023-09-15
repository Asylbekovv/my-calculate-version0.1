def add_elem(x, y):
    return x + y

def multy(x, y):
    return x * y

def substract(x, y):
    return x - y

def devide(x, y):
    return x / y

while True:
    print("Select operation:")
    print("+ Plus")
    print("- Minuse")
    print("* Multy")
    print("/ Devide")
    print("exit")

    choose = input("Enter your operation: + - * /: ")
    if choose == 1:
        break
if choose in input("1", "2", "3","4"):
    number1 = float(input("Enter your first number: "))
    number2 = float(input("Enter your second number: "))

if choose == "+":
    print("Result:", add_elem(number1, number2))
elif choose == "-":
    print("Result: ", substract(number1, number2))
elif choose == "*":
    print("Result: ", multy(number1, number2))
else:
    print("Is not correct element")



