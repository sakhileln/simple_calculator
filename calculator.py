from helper import (
    get_input,
    addition,
    subtract,
    multiply,
    division,
    int_division,
    modulo_division,
    check_division_zero,
)
import sys

print("Welcome to the Calculator App")
print("Usage: 2 + 3")


def main() -> None:
    """Main diver for the program."""
    # Get expression from the user
    expression = get_input()
    number1, operand, number2 = expression

    # Perform the mathematical operation according to operand
    match operand:
        case "+":
            result = addition(number1, number2)
        case "-":
            result = subtract(number1, number2)
        case "/":
            number2 = check_division_zero(number2)
            result = int(division(number1, number2))
        case "//":
            number2 = check_division_zero(number2)
            result = int_division(number1, number2)
        case "*":
            result = multiply(number1, number2)
        case "%":
            result = modulo_division(number1, number2)
        case _:
            print("Invalid operand")
    print(f"Result is: {result}")

    while True:
        try:
            choice = input("Continue 'y' or Exit 'n': ")
            if choice.lower() not in ["y", "n"]:
                raise ValueError
            break
        except Exception as e:
            print(f"Invalid input. Please choose 'y' or 'n' {e}")
    if choice == "y":
        main()
    else:
        print("Thank you for using this program. Goodbye...")
        sys.exit()


if __name__ == "__main__":
    # Test case for main
    main()
