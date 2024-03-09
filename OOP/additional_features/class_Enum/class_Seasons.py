from enum import Enum, unique, auto


@unique
class Seasons(Enum):
    WINTER = auto()
    SPRING = auto()
    SUMMER = auto()
    FALL = auto()

    def text_value(self, country_code):
        seasons_translate = {
            'en': {
                self.WINTER: 'winter',
                self.SPRING: 'spring',
                self.SUMMER: 'summer',
                self.FALL: 'fall'
            },
            'ru': {
                self.WINTER: 'зима',
                self.SPRING: 'весна',
                self.SUMMER: 'лето',
                self.FALL: 'осень'
            },
        }
        return seasons_translate[country_code][self]


print(Seasons.FALL.text_value('ru'))
print(Seasons.FALL.text_value('en'))
