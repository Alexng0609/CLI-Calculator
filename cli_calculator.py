def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y


def power(x, y):
    return x**y


def modulus(x, y):
    return x % y


def exponent(x):
    return 2.71828**x


def square_root(x):
    if x < 0:
        return "Error: Square root of a negative number is not defined."
    return x**0.5


def main():
    print("Welcome to the CLI Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Modulus")
    print("7. Exponent")
    print("8. Square Root")

    while True:
        choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

        if choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            if choice in ["1", "2", "3", "4", "5", "6"]:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            elif choice == "7":
                num1 = float(input("Enter the number: "))
            elif choice == "8":
                num1 = float(input("Enter the number: "))

            if choice == "1":
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == "2":
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == "3":
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == "4":
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            elif choice == "5":
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            elif choice == "6":
                print(f"{num1} % {num2} = {modulus(num1, num2)}")
            elif choice == "7":
                print(f"e^{num1} = {exponent(num1)}")
            elif choice == "8":
                print(f"√{num1} = {square_root(num1)}")
        else:
            print("Invalid input. Please enter a number between 1 and 8.")

        next_calculation = input(
            "Do you want to perform another calculation? (yes/no): "
        )
        if next_calculation.lower() != "yes":
            break
    print("Thank you for using the CLI Calculator. Goodbye!")


if __name__ == "__main__":
    main()
