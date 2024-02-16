import functools


def ignore_exception(*_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as err:
                for error in _types:
                    if isinstance(err, error):
                        print(f'Исключение {error.__name__} обработано')
                return type(err)
        return wrapper
    return decorator


min = ignore_exception(ZeroDivisionError)(min)
try:
    print(min(1, '2', 3, [4, 5]))
except Exception as e:
    print(type(e))
