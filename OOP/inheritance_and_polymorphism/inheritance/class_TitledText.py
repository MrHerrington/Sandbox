class TitledText(str):
    def __new__(cls, content, text_title):
        instance = super().__new__(cls, content)
        instance.text_title = text_title
        return instance

    def title(self):
        return self.text_title


# Test №1
titled = TitledText('Сreate a class Soda', 'Homework')

print(titled)
print(titled.title())
print(issubclass(TitledText, str))

# Test №2
titled1 = TitledText('Сreate a class Soda', 'Homework')
titled2 = TitledText('Сreate a class Soda', 'Exam')

print(titled1 == titled2)
