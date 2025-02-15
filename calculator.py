def calculator():
    print("Simple Calculator")
    print("Operations: +, -, *, /")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation: ")
        num2 = float(input("Enter second number: "))

        if op == '+':
            print(f"Result: {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1 * num2}")
        elif op == '/':
            print(f"Result: {num1 / num2}" if num2 != 0 else "Error: Division by zero")
        else:
            print("Invalid operation")
    except ValueError:
        print("Invalid input")

calculator()
