class PowerOf:
    def __init__(self, power):
        self.power = power
        self.point = -1
        self.start = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.point += 1
        if bool(self.point) is False:
            self.start = 1
        else:
            self.start *= self.power
        return self.start


power_of_two = PowerOf(11)
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
