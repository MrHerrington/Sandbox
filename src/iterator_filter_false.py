def filter_false(predicate, iterator):
    if predicate is None:
        return filter(lambda x: bool(x) is False, iterator)
    else:
        return (i for i in iterator if i not in filter(predicate, iterator))


objects = [0, 1, True, False, 17, []]
print(*filter_false(None, objects))


numbers = [1, 2, 3, 4, 5]
print(*filter_false(lambda x: x >= 3, numbers))


numbers = (1, 2, 3, 4, 5)
print(*filter_false(lambda x: x % 2 == 0, numbers))
