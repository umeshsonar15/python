def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def mult(x, y):
    return x * y
def div(x, y):
    return x / y
print("Select operation")
print("1.Add")
print("2.Sub")
print("3.Mult")
print("4.Div")
while True:
    choice = input("Enter ch(1/2/3/4):")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
                print(num1, "-", num2, "=", sub(num1, num2))
        elif choice == '3':
                print(num1, "*", num2, "=", mult(num1, num2))
        elif choice == '4':
                print(num1, "/", num2, "=", div(num1, num2))
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
           break
    else:
        print("Invalid Input")
