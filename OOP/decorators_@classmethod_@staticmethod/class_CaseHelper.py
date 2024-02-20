class CaseHelper:
    """Класс описывает набор функций для работы со строками
    в стилях Snake Case и Upper Camel Case"""
    @staticmethod
    def is_snake(str_):
        """Метод возвращает True, если переданная строка записана
        в стиле Snake Case, или False в противном случае"""
        return all((all(i.lower() == i for i in str_), '__' not in str_))

    @staticmethod
    def is_upper_camel(str_):
        """Метод возвращает True, если переданная строка записана
        в стиле Upper Camel Case, или False в противном случае"""
        return all((str_[0].upper() == str_[0], '_' not in str_))

    @staticmethod
    def to_snake(str_):
        """Метод принимает в качестве аргумента строку в стиле Upper Camel Case,
        записывает ее в стиле Snake Case и возвращает полученный результат"""
        if CaseHelper.is_upper_camel(str_):
            temp_lst = list()
            temp_record = ''
            for i in str_:
                if not temp_record:
                    temp_record += i
                    continue
                if i.islower():
                    temp_record += i
                else:
                    temp_lst.append(temp_record)
                    temp_record = i
            temp_lst.append(temp_record)
            return '_'.join(map(str.lower, temp_lst))
        else:
            return str_

    @staticmethod
    def to_upper_camel(str_):
        """Метод принимает в качестве аргумента строку в стиле Snake Case, записывает
        ее в стиле Upper Camel Case и возвращает полученный результат"""
        if CaseHelper.is_snake(str_):
            return ''.join(map(str.title, str_.split('_')))
        else:
            return str_


# INPUT DATA:

# TEST_1:
print(CaseHelper.is_snake('beegeek'))
print(CaseHelper.is_snake('bee_geek'))
print(CaseHelper.is_snake('Beegeek'))
print(CaseHelper.is_snake('BeeGeek'))

# TEST_2:
print(CaseHelper.is_upper_camel('beegeek'))
print(CaseHelper.is_upper_camel('bee_geek'))
print(CaseHelper.is_upper_camel('Beegeek'))
print(CaseHelper.is_upper_camel('BeeGeek'))

# TEST_3:
print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))

# TEST_4:
print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))

# TEST_5:
cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp', 'tearDown', 'run', 'exit', 'setup']

for case in cases:
    print(CaseHelper.is_snake(case))

# TEST_6:
cases = ['assert_equal', 'tear_down', '__init__', 'assertEqual', 'setUp',
         'tearDown', 'run', 'exit', 'setup', 'AssertEqual', 'SetUp']

for case in cases:
    print(CaseHelper.is_upper_camel(case))

# TEST_7:
cases = ['AssertEqual', 'SetUp', 'TearDown', 'AddModuleCleanup', 'AssertRaisesRegex',
         'AssertAlmostEqual', 'AssertNotAlmostEqual']

for case in cases:
    print(CaseHelper.to_snake(case))

# TEST_8:
cases = ['assert_equal', 'tear_down', 'assert_raises_regex', 'assert_almost_equal',
         'assert_not_almost_equal', 'beegeek']

for case in cases:
    print(CaseHelper.to_upper_camel(case))

# TEST_9:
obj = CaseHelper()
print(type(obj.is_snake))
print(type(obj.is_upper_camel))
print(type(obj.to_snake))
print(type(obj.to_upper_camel))
