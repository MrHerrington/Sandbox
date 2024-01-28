class MaxRetriesException(Exception):
    pass


def retry(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            nonlocal times
            while times > 0:
                try:
                    func(*args, **kwargs)
                    break
                except:
                    times -= 1
                    if times == 0:
                        raise MaxRetriesException
                    continue
        return wrapper
    return decorator


@retry(8)
def beegeek():
    beegeek.calls = beegeek.__dict__.get('calls', 0) + 1
    if beegeek.calls < 5:
        raise ValueError
    print('beegeek')


beegeek()


# @retry(3)
# def no_way():
#     raise ValueError
#
# try:
#     no_way()
# except Exception as e:
#     print(type(e))
