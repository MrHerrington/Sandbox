from enum import Enum, unique


@unique
class HTTPStatusCodes(Enum):
    CONTINUE = 100
    OK = 200
    USE_PROXY = 305
    NOT_FOUND = 404
    BAD_GATEWAY = 502

    def info(self):
        return self.name, self.value

    def code_class(self):
        groups = ('информация', 'успех', 'перенаправление', 'ошибка клиента', 'ошибка сервера')
        codes = dict(zip(HTTPStatusCodes, groups))
        return codes[self]


print(HTTPStatusCodes.OK.info())
print(HTTPStatusCodes.OK.code_class())
