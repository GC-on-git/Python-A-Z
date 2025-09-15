x_1 = float(input("Enter first number: "))
x_2 = float(input("Enter second number: "))

operation = input("Enter operation [ +, -, *, / ]: ")

if operation == "+":
    print(f"{x_1} {operation} {x_2} = {x_1 + x_2}")
elif operation == "-":
    print(f"{x_1} {operation} {x_2} = {x_1 - x_2}")
elif operation == "*":
    print(f"{x_1} {operation} {x_2} = {x_1 * x_2}")
elif operation == "/":
    print(f"{x_1} {operation} {x_2} = {x_1 / x_2}")
else:
    print("Invalid operation")

## Add error handling for end user