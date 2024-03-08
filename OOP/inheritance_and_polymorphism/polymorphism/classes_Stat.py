class MinStat:
    def __init__(self, iterable=None):
        if iterable is None:
            self.iterable = list()
        else:
            self.iterable = iterable

    def add(self, num):
        self.iterable.append(num)

    def result(self):
        if len(self.iterable) > 0:
            return min(self.iterable)
        return None

    def clear(self):
        self.iterable.clear()


class MaxStat(MinStat):
    def result(self):
        if len(self.iterable) > 0:
            return max(self.iterable)
        return None


class AverageStat(MinStat):
    def result(self):
        if len(self.iterable) > 0:
            return sum(self.iterable) / len(self.iterable)
        return None


# Test №1
minstat = MinStat([1, 2, 4])
maxstat = MaxStat([1, 2, 4])
averagestat = AverageStat([1, 2, 4])

minstat.add(5)
maxstat.add(5)
averagestat.add(5)

print(minstat.result())
print(maxstat.result())
print(averagestat.result())

# Test №2
minstat = MinStat()
maxstat = MaxStat()
averagestat = AverageStat()

for i in range(1, 6):
    minstat.add(i)
    maxstat.add(i)
    averagestat.add(i)

print(minstat.result())
print(maxstat.result())
print(averagestat.result())

# Test №3
minstat = MinStat()
maxstat = MaxStat()
averagestat = AverageStat()

print(minstat.result())
print(maxstat.result())
print(averagestat.result())
