def calculate(expression):
    num1, operator, num2 = expression.split()
    num1 = int(num1)
    num2 = int(num2)
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 // num2
    else:
        raise ValueError("無效的運算子")
    return result
expression = input().strip()
result = calculate(expression)
print(result)
