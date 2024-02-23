from functools import total_ordering


@total_ordering
class Version:
    """Класс описывает версию какого-либо ПО"""
    def __init__(self, version):
        self._version = version

    def __eq__(self, other):
        """self == other"""
        if isinstance(other, Version):
            _temp = Version.same_len_version(self.version, other.version)
            for i, j in _temp:
                if i != j:
                    return False
            return True
        else:
            return NotImplemented

    def __ge__(self, other):
        """self >= other"""
        if isinstance(other, Version):
            _temp = Version.same_len_version(self.version, other.version)
            for i in _temp:
                if i[0] > i[-1]:
                    return True
                elif i[0] < i[-1]:
                    return False
            return True
        else:
            return NotImplemented

    def __str__(self):
        return f'{self.version}'

    def __repr__(self):
        return f"Version('{self._version}')"

    @property
    def version(self):
        return self._version

    @staticmethod
    def same_len_version(_version1, _version2):
        """Метод задает одинаковую длину для сравниваемых версий"""
        _temp_version1 = list(map(int, _version1.split('.')))
        _temp_version2 = list(map(int, _version2.split('.')))
        _max_len = max(map(len, (_temp_version1, _temp_version2)))
        while len(_temp_version1) < _max_len:
            _temp_version1.append(0)
        while len(_temp_version2) < _max_len:
            _temp_version2.append(0)
        return tuple(zip(_temp_version1, _temp_version2))


# Test №1
print(Version('3.0.3') == Version('1.11.28'))
print(Version('3.0.3') < Version('1.11.28'))
print(Version('3.0.3') > Version('1.11.28'))
print(Version('3.0.3') <= Version('1.11.28'))
print(Version('3.0.3') >= Version('1.11.28'))

# Test №2
print(Version('3') == Version('3.0'))
print(Version('3') == Version('3.0.0'))
print(Version('3.0') == Version('3.0.0'))

# Test №3
versions = [Version('2'), Version('2.1'), Version('1.9.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))
