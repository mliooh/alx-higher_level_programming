# calculation_1.py

import calculator_1

if __name__ == "__main__":
    a = 10
    b = 5

    result_add = calculator_1.add(a, b)
    result_subtract = calculator_1.sub(a, b)
    result_multiply = calculator_1.mul(a, b)
    result_divide = calculator_1.div(a, b)

    print("Addition:", result_add)
    print("Subtraction:", result_subtract)
    print("Multiplication:", result_multiply)
    print("Division:", result_divide)
