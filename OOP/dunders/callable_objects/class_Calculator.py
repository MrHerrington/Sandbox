class Calculator:
    def __call__(self, a, b, operation):
        try:
            return eval(f'{a} {operation} {b}')
        except ZeroDivisionError:
            return 'Деление на ноль невозможно!'


# Test №1
calculator = Calculator()
print(calculator(10, 5, '+'))
print(calculator(10, 5, '-'))
print(calculator(10, 5, '*'))
print(calculator(10, 5, '/'))

# Test №2
calculator = Calculator()
try:
    print(calculator(10, 0, '/'))
except ValueError as e:
    print(e)
