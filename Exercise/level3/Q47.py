'''Build a calculator split across 3 files: operations.py (add/subtract/multiply/divide),
validator.py (input validation), main.py (menu loop). Each file properly uses if
__name__=='__main__'.'''


from operation import add, subtract, multiply, divide
from validator import validate_numbers, validate_choice

def menu():
    print("\n=== Simple Calculator ===")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Choose operation (1-5): ").strip()
        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break
        try:
            choice = validate_choice(choice)
            a_str = input("Enter first number: ").strip()
            b_str = input("Enter second number: ").strip()
            a, b = validate_numbers(a_str, b_str)

            if choice == 1:
                result = add(a, b)
            elif choice == 2:
                result = subtract(a, b)
            elif choice == 3:
                result = multiply(a, b)
            elif choice == 4:
                result = divide(a, b)

            print(f"Result: {result}")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
