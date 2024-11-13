"""A simpler helper module."""


def get_input() -> tuple[int, str, int]:
    """
    Get expression from the user.

    Parameters:
        None
    Return:
        epression tuple(int, str, int): Expression according as a tuple
    """
    while True:
        try:
            expression = (input("Please enter your expression: ")).split()
            number1, operand, number2 = (
                int(expression[0]),
                str(expression[1]),
                int(expression[2]),
            )
            if operand not in ["+", "-", "*", "/"]:
                raise ValueError

            break
        except Exception as e:
            print(f"You have entered an invalid expression {e}. Please try again.")
    return (number1, operand, number2)


def addition(a: int, b: int) -> int:
    return a + b


def subtract(a: int, b: int) -> int:
    return a - b


def division(a: int, b: int) -> float:
    return round((a / b), 1)


def multiply(a: int, b: int) -> int:
    return a * b

def int_division(a: int, b: int) -> int:
    return a // b

def modulo_division(a: int, b: int) -> int:
    return a % b
