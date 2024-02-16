"""BOH = Binary, Octal, Hex / преобразование числа в двоичную, восьмиричную и шестнадцатиричную системы"""
n = int(input('n: '))
binary = bin(n)
octal = oct(n)
hexx = hex(n)
print(binary[2:], octal[2:], hexx[2:].upper(), sep='\n')
