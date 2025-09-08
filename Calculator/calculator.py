

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def power(a, b):
    return a ** b

def calculator():
    print("="*30)
    print("   Welcome to Calculator   ")
    print("="*30)

    while True:
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. Exit")

        choice = input("\nEnter choice (1-6): ")

        if choice == "6":
            print("Exiting... Thank you!")
            break

        if choice in ["1", "2", "3", "4", "5"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            if choice == "1":
                result = add(num1, num2)
                symbol = "+"
            elif choice == "2":
                result = subtract(num1, num2)
                symbol = "-"
            elif choice == "3":
                result = multiply(num1, num2)
                symbol = "*"
            elif choice == "4":
                result = divide(num1, num2)
                symbol = "/"
            elif choice == "5":
                result = power(num1, num2)
                symbol = "^"

            print(f"\nResult: {num1} {symbol} {num2} = {result}")
        else:
            print(" Invalid choice! Please select between 1-6.")

if __name__ == "__main__":
    calculator()
