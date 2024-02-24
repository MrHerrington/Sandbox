class Strip:
    def __init__(self, chars):
        self.chars = chars

    def __call__(self, string):
        return str.strip(string, self.chars)


# Test №1
strip = Strip('!? ')

print(strip(' ?beegeek!'))
print(strip('!bee?geek!'))

# Test №2
strip = Strip('.,+-')

print(strip(' --++beegeek++--'))
print(strip('-bee...geek-'))
print(strip('-+,.b-e-e-g-e-e-k-+,.'))
