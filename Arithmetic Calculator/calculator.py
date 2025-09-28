def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

def get_number(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def get_operation():
    print("\nSelect an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        choice = input("Enter choice (1/2/3/4/5): ")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

def calculator():
    print("========== Simple Command-Line Calculator ==========")

    while True:
        choice = get_operation()

        if choice == '5':
            print("Exiting calculator. Thank you!")
            break

        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            result = divide(num1, num2)
            operation = '/'

        print(f"\nResult: {num1} {operation} {num2} = {result}\n")

if __name__ == "__main__":
    calculator()
