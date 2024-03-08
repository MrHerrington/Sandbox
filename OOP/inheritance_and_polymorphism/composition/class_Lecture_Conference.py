class Lecture:
    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = start_time
        self.duration = duration
        self.identifier = range(type(self).to_minutes(start_time),
                                type(self).to_minutes(start_time) + type(self).to_minutes(duration) + 1)

    @staticmethod
    def to_minutes(time):
        return int(time.split(':')[0]) * 60 + int(time.split(':')[-1])


class Conference:
    __PROGRAMM = []

    def add(self, new_lecture):
        if any(map(lambda x: len(set(new_lecture.identifier) & set(x.identifier)) > 0, type(self).__PROGRAMM)):
            raise ValueError('Провести выступление в это время невозможно')
        type(self).__PROGRAMM.append(new_lecture)

    def total(self):
        duration = sum(map(lambda x: max(x.identifier) - min(x.identifier), type(self).__PROGRAMM))
        return f'{str(duration // 60).zfill(2)}:{str(duration % 60).zfill(2)}'

    def longest_lecture(self):
        duration = max(map(lambda x: max(x.identifier) - min(x.identifier), type(self).__PROGRAMM))
        return f'{str(duration // 60).zfill(2)}:{str(duration % 60).zfill(2)}'


conference = Conference()
conference.add(Lecture('Простые числа', '08:00', '01:30'))
conference.add(Lecture('Жизнь после ChatGPT', '10:00', '02:00'))
conference.add(Lecture('Муравьиный алгоритм', '13:30', '01:50'))
print(conference.total())
print(conference.longest_lecture())
