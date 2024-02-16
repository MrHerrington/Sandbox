def tribonacci(n):
    """
    Функция принимает один аргумент и возвращает n-ый член последовательности
    Трибоначчи с использованием рекурсии и мемоизации
    """
    memorization = {1: 1, 2: 1, 3: 1}

    def tribonacci_rec(m):
        val = memorization.get(m)
        if val is None:
            val = tribonacci_rec(m - 3) + tribonacci_rec(m - 2) + tribonacci_rec(m - 1)
            memorization[m] = val
        return val

    return tribonacci_rec(n)


print(*map(tribonacci, range(1, 16)))
