class Time:
    def __init__(self, hours, minutes):
        self.hours = hours % 24 + minutes // 60
        self.minutes = minutes % 60

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.hours + other.hours + (self.minutes + other.minutes) // 60,
                        (self.minutes + other.minutes) % 60)
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            return Time(self.hours + other.hours + (self.minutes + other.minutes) // 60,
                        (self.minutes + other.minutes) % 60)
        else:
            return NotImplemented

    def __str__(self):
        return f'{str(self.hours).zfill(2)}:{self.minutes}'


# Test №1
time1 = Time(2, 30)
time2 = Time(3, 10)

print(time1 + time2)
print(time2 + time1)

# Test №2
time1 = Time(2, 30)
time2 = Time(3, 10)

time1 += time2

print(time1)
print(time2)

# Test №3
time1 = Time(25, 20)
time2 = Time(10, 130)
print(time1)
print(time2)
