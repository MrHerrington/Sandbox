# Class Singleton realization №1

class SingletonConfig1:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self):
        self.program_name = 'GenerationPy'
        self.environment = 'release'
        self.loglevel = 'verbose'
        self.version = '1.0.0'


# Class Singleton realization №2 without __init__

class SingletonConfig2:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.program_name = 'GenerationPy'
            cls._instance.environment = 'release'
            cls._instance.loglevel = 'verbose'
            cls._instance.version = '1.0.0'
        return cls._instance


config = SingletonConfig1()
print(config.program_name)
print(config.environment)
print(config.loglevel)
print(config.version)

config1 = SingletonConfig2()
config2 = SingletonConfig2()
config3 = SingletonConfig2()
print(config1 is config2)
print(config1 is config3)
