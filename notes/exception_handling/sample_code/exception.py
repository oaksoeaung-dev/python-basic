while True:
    try:
        number1 = int(input("Please enter your first number: "))
        number2 = int(input("Please enter your second number: "))

        result = number1 / number2
    except ValueError as ex:
        print("Please enter a number\n")
    except ZeroDivisionError as ex:
        print("Cannot divide by zero\n")
    else:
        print(f"result = {result}")
        break
    finally:
        print("Cleaning up...")

print("Program stopped")