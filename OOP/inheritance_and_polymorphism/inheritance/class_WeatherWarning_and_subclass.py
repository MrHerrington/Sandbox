from datetime import date


class WeatherWarning:
    @staticmethod
    def rain(*args, **kwargs):
        print('Ожидаются сильные дожди и ливни с грозой')

    @staticmethod
    def snow(*args, **kwargs):
        print('Ожидается снег и усиление ветра')

    @staticmethod
    def low_temperature(*args, **kwargs):
        print('Ожидается сильное понижение температуры')


class WeatherWarningWithDate(WeatherWarning):
    @staticmethod
    def rain(date_):
        print(date.strftime(date_, '%d.%m.%Y'))
        print('Ожидаются сильные дожди и ливни с грозой')

    @staticmethod
    def snow(date_):
        print(date.strftime(date_, '%d.%m.%Y'))
        print('Ожидается снег и усиление ветра')

    @staticmethod
    def low_temperature(date_):
        print(date.strftime(date_, '%d.%m.%Y'))
        print('Ожидается сильное понижение температуры')


# Test №1
print(issubclass(WeatherWarningWithDate, WeatherWarning))

# Test №2
weatherwarning = WeatherWarning()

weatherwarning.rain()
weatherwarning.snow()
weatherwarning.low_temperature()

# Test №3
weatherwarning = WeatherWarningWithDate()
dt = date(2022, 12, 12)
weatherwarning.rain(dt)
weatherwarning.snow(dt)
weatherwarning.low_temperature(dt)
